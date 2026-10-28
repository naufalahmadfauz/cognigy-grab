"""Offline regrading of recorded batches through the production assertion engine."""

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
from uuid import uuid4

from . import __version__
from .assertions import evaluate_run
from .config import Config
from .redact import Redactor
from .reports import OUTCOMES, ReportWriter, defects, metrics


class RegradeError(ValueError):
    pass


def _fields(value, required: set[str], where: str):
    if not isinstance(value, dict) or not required <= value.keys():
        raise RegradeError(f"{where}: incomplete recorded evidence.")


def _strings(value, keys, where: str):
    if any(not isinstance(value.get(key), str) or not value[key] for key in keys):
        raise RegradeError(f"{where}: expected nonempty recorded strings.")


def validate_evidence(batch: object, scenario) -> None:
    """Reject incompatible/incomplete captures instead of manufacturing passes.

    Grading expectations may change; the merchant script and turn order must still
    describe the captured experiment. HTTP results are evidence, not re-executed.
    """
    _fields(batch, {"reportSchemaVersion", "batchId", "runnerVersion", "mode", "scenario", "configuration", "runs", "createdAt", "completedAt"}, "batch")
    if batch["reportSchemaVersion"] != "1.0" or batch["mode"] not in ("EXECUTED", "REGRADE"):
        raise RegradeError("Regrade needs an executed reportSchemaVersion 1.0 aggregate; dry-run plans are not evidence.")
    _strings(batch, ("batchId", "runnerVersion", "createdAt", "completedAt"), "batch")
    _fields(batch["scenario"], {"id", "version", "sha256", "product"}, "scenario")
    _strings(batch["scenario"], ("id", "version", "sha256", "product"), "scenario")
    if batch["scenario"]["id"] != scenario.id or batch["scenario"]["product"] != scenario.product:
        raise RegradeError("Selected scenario ID/business line differs from the recorded batch.")
    if not isinstance(batch["configuration"], dict) or not isinstance(batch["runs"], list) or not batch["runs"]:
        raise RegradeError("Batch must contain recorded configuration and a nonempty run list.")
    indexes, run_ids = set(), set()
    for run in batch["runs"]:
        _fields(run, {"runId", "runIndex", "batchId", "userId", "sessionId", "scenarioId", "scenarioVersion", "scenarioSha256", "startedAt", "completedAt", "executionStatus", "outcome", "turns"}, "run")
        _strings(run, ("runId", "batchId", "userId", "sessionId", "startedAt", "completedAt"), "run")
        if type(run["runIndex"]) is not int or run["runIndex"] < 1 or run["runIndex"] in indexes or run["runId"] in run_ids:
            raise RegradeError("Run indexes and run IDs must be unique; indexes must be positive integers.")
        indexes.add(run["runIndex"])
        run_ids.add(run["runId"])
        if run["executionStatus"] != "COMPLETED" or run["outcome"] not in OUTCOMES:
            raise RegradeError("Only completed runs with recorded outcomes can be regraded.")
        if run["batchId"] != batch["batchId"] or any(run[key] != batch["scenario"][source] for key, source in (
            ("scenarioId", "id"), ("scenarioVersion", "version"), ("scenarioSha256", "sha256")
        )):
            raise RegradeError("Recorded run provenance does not match its batch.")
        if not isinstance(run["turns"], list) or len(run["turns"]) != len(scenario.turns):
            raise RegradeError("Recorded turn count differs from the selected scenario.")
        stopped = False
        for index, (turn, definition) in enumerate(zip(run["turns"], scenario.turns, strict=True), 1):
            _fields(turn, {"turnId", "turnIndex", "batchId", "runId", "userId", "sessionId", "merchantInput", "agentText", "executionStatus", "outcome", "httpStatus", "durationSeconds", "traceIds", "echoedIdentity", "error", "assertions"}, "turn")
            _strings(turn, ("userId", "sessionId"), "turn")
            if type(turn["turnIndex"]) is not int or turn["turnIndex"] != index or turn["turnId"] != definition["id"] or turn["merchantInput"] != definition["merchant"]:
                raise RegradeError("Recorded turn IDs/order/merchant messages differ from the selected scenario; regrading changes expectations only.")
            if turn["runId"] != run["runId"] or turn["batchId"] != batch["batchId"]:
                raise RegradeError("Recorded turn provenance does not match its run.")
            if not isinstance(turn["agentText"], str) or not isinstance(turn["echoedIdentity"], dict):
                raise RegradeError("Turn must retain normalized text and echoed-identity evidence.")
            if not isinstance(turn["traceIds"], list) or any(not isinstance(trace, str) for trace in turn["traceIds"]):
                raise RegradeError("Recorded trace IDs must be a string list.")
            if not isinstance(turn["assertions"], list):
                raise RegradeError("Recorded assertion results are required for comparison.")
            assertion_ids = set()
            for item in turn["assertions"]:
                _fields(item, {"id", "outcome", "reason", "category"}, "assertion")
                _strings(item, ("id", "reason", "category"), "assertion")
                if item["id"] in assertion_ids or item["outcome"] not in ("PASS", "FAIL", "WARN", "SKIP"):
                    raise RegradeError("Recorded assertion IDs must be unique and outcomes recognized.")
                assertion_ids.add(item["id"])
            if turn["executionStatus"] == "SKIPPED":
                if not stopped or turn["outcome"] is not None or turn["error"] is not None:
                    raise RegradeError("Skipped turns must follow a recorded transport/protocol error.")
                continue
            if turn["executionStatus"] != "EXECUTED" or stopped or turn["outcome"] not in OUTCOMES:
                raise RegradeError("Recorded turn execution order/status is inconsistent.")
            if turn["httpStatus"] is not None and (type(turn["httpStatus"]) is not int or not 100 <= turn["httpStatus"] <= 599):
                raise RegradeError("Recorded HTTP status is invalid.")
            if not isinstance(turn["durationSeconds"], (int, float)) or turn["durationSeconds"] < 0:
                raise RegradeError("Executed turns need a nonnegative recorded request duration.")
            if turn["error"] is not None:
                _fields(turn["error"], {"kind", "reason"}, "transport error")
                _strings(turn["error"], ("kind", "reason"), "transport error")
                stopped = True
            elif not (200 <= (turn["httpStatus"] or 0) < 300 and turn["agentText"].strip()):
                raise RegradeError("Unusable replies need a recorded transport/protocol error.")
            if (turn["outcome"] == "ERROR") != stopped:
                raise RegradeError("Recorded turn outcome contradicts transport evidence.")
        if (run["outcome"] == "ERROR") != stopped:
            raise RegradeError("Recorded run outcome contradicts transport evidence.")


def compare_grades(original: list[dict], updated: list[dict]) -> dict:
    comparisons = []
    for before, after in zip(original, updated, strict=True):
        changes = []
        for old_turn, new_turn in zip(before["turns"], after["turns"], strict=True):
            old = {item["id"]: item for item in old_turn["assertions"]}
            new = {item["id"]: item for item in new_turn["assertions"]}
            for key in sorted(old.keys() | new.keys()):
                prior, current = old.get(key, {}), new.get(key, {})
                if prior.get("outcome") != current.get("outcome"):
                    changes.append({
                        "turn": new_turn["turnIndex"], "assertionId": key,
                        "before": prior.get("outcome"), "after": current.get("outcome"),
                        "originalReason": prior.get("reason"), "updatedReason": current.get("reason"),
                    })
        comparisons.append({
            "runIndex": after["runIndex"], "runId": after["runId"],
            "originalOutcome": before["outcome"], "updatedOutcome": after["outcome"], "assertionChanges": changes,
        })
    return {"originalMetrics": metrics(original), "updatedMetrics": metrics(updated), "runs": comparisons}


def regrade_batch(source: Path, scenario, config: Config, output_root: Path) -> tuple[Path, dict]:
    """Write a new evaluation, retaining original correlation IDs and capture times."""
    path = source / "aggregate.json" if source.is_dir() else source
    try:
        captured = path.read_bytes()
        original = json.loads(captured)
        json.dumps(original, allow_nan=False)
    except (OSError, ValueError, UnicodeError, RecursionError):
        raise RegradeError("Cannot read recorded aggregate JSON; supply a batch directory or aggregate.json.") from None
    validate_evidence(original, scenario)
    if output_root.resolve().is_relative_to(path.parent.resolve()):
        raise RegradeError("Choose an output directory outside the original batch directory.")

    now = datetime.now(timezone.utc)
    evaluated_at = now.isoformat(timespec="milliseconds").replace("+00:00", "Z")
    batch_id = "regrade-" + now.strftime("%Y%m%dT%H%M%S%fZ") + "-" + uuid4().hex[:12]
    runs = deepcopy(original["runs"])
    for run in runs:
        evaluate_run(scenario, run)
        run.update({
            "batchId": batch_id, "scenarioVersion": scenario.version, "scenarioSha256": scenario.sha256,
            "evaluationMode": "REGRADE", "evaluatedAt": evaluated_at,
        })
        for turn in run["turns"]:
            turn["batchId"] = batch_id
            turn["rawEvidenceRetained"] = bool(config.retain_raw and turn.get("rawEvidenceRetained"))
            if not turn["rawEvidenceRetained"]:
                turn["rawResponse"] = turn["rawBody"] = None
    comparison = compare_grades(original["runs"], runs)
    for run, change in zip(runs, comparison["runs"], strict=True):
        run["originalOutcome"] = change["originalOutcome"]
    batch = {
        "reportSchemaVersion": "1.0", "runnerVersion": __version__, "pythonVersion": platform.python_version(),
        "batchId": batch_id, "mode": "REGRADE", "createdAt": evaluated_at, "completedAt": evaluated_at,
        "requestsSent": 0,
        "scenario": {"id": scenario.id, "version": scenario.version, "sha256": scenario.sha256, "product": scenario.product},
        "configuration": {"retainRawEvidence": config.retain_raw, "additionalRedactionValueCount": len(config.redact_values)},
        "source": {
            "batchId": original["batchId"], "mode": original["mode"], "runnerVersion": original["runnerVersion"],
            "scenario": original["scenario"], "configuration": original["configuration"],
            "createdAt": original["createdAt"], "completedAt": original["completedAt"],
            "aggregateSha256": hashlib.sha256(captured).hexdigest(),
        },
        "metrics": metrics(runs), "defects": defects(runs), "runs": runs, "comparison": comparison,
    }
    safe_ids = {run[key] for run in runs for key in ("runId", "userId", "sessionId")}
    redactor = Redactor(config, safe_ids)
    directory = output_root / batch_id
    writer = ReportWriter(directory, redactor)
    writer.write_json("manifest.json", {"batchId": batch_id, "executionStatus": "STARTED", "mode": "REGRADE"})
    writer.write_json("scenario.json", scenario.definition)
    for run in runs:
        writer.write_run(run)
    writer.finish(batch)
    return directory, redactor.clean(batch)
