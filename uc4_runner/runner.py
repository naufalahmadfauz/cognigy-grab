"""Independent run scheduling; turns inside each run are always sequential."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import platform
import time
from uuid import uuid4

import httpx

from . import __version__
from .assertions import classify, evaluate, skipped_assertions
from .client import CognigyClient
from .config import Config, ConfigError, endpoint_url
from .redact import Redactor
from .reports import ReportWriter, defects, metrics
from .scenario import Scenario


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _plan_run(scenario: Scenario, index: int, batch_id: str) -> dict:
    run_id = str(uuid4())
    user_id = f"uc4-user-{uuid4()}"
    session_id = f"uc4-session-{uuid4()}"
    planned = utc_now()
    return {
        "runId": run_id, "batchId": batch_id, "runIndex": index,
        "userId": user_id, "sessionId": session_id,
        "scenarioId": scenario.id, "scenarioVersion": scenario.version,
        "scenarioSha256": scenario.sha256,
        "plannedAt": planned, "startedAt": None, "completedAt": None,
        "executionStatus": "PLANNED", "outcome": None,
        "turns": [{
            "turnId": turn["id"], "turnIndex": turn_index,
            "runId": run_id, "batchId": batch_id, "userId": user_id, "sessionId": session_id,
            "merchantInput": turn["merchant"], "agentText": "",
            "startedAt": None, "completedAt": None, "durationSeconds": None,
            "executionStatus": "PLANNED", "outcome": None, "attempts": 0,
            "httpStatus": None, "traceIds": [], "echoedIdentity": {},
            "rawResponse": None, "rawBody": None, "rawEvidenceRetained": False,
            "normalizationNotes": [], "error": None,
            "assertions": skipped_assertions(scenario, turn, turn_index, "Dry-run plan; response not evaluated."),
        } for turn_index, turn in enumerate(scenario.turns, 1)],
    }


def _execute_run(scenario: Scenario, config: Config, run: dict, transport, sleep) -> dict:
    run["startedAt"] = utc_now()
    identity = {"userId": run["userId"], "sessionId": run["sessionId"]}
    history = []
    merchants = []
    stopped = False
    # Each run owns its HTTP client/cookie jar as well as its Cognigy identities.
    with CognigyClient(config, transport=transport) as client:
        for definition, turn in zip(scenario.turns, run["turns"], strict=True):
            index = turn["turnIndex"]
            if stopped:
                turn["executionStatus"] = "SKIPPED"
                turn["assertions"] = skipped_assertions(
                    scenario, definition, index, "Earlier transport/protocol error left session state uncertain."
                )
                continue
            if index > 1 and config.request_delay:
                sleep(config.request_delay)
            turn["startedAt"] = utc_now()
            turn["executionStatus"] = "EXECUTED"
            turn["attempts"] = 1
            requested = {"userId": turn["userId"], "sessionId": turn["sessionId"]}
            reply = client.send(user_id=requested["userId"], session_id=requested["sessionId"], text=turn["merchantInput"])
            turn.update({
                "completedAt": utc_now(), "durationSeconds": reply.duration_seconds,
                "httpStatus": reply.http_status, "agentText": reply.text,
                "traceIds": reply.trace_ids, "echoedIdentity": reply.echoed_identity,
                "normalizationNotes": reply.normalization_notes,
                "rawResponse": reply.raw if config.retain_raw else None,
                "rawBody": reply.raw_body if config.retain_raw else None,
                "rawEvidenceRetained": config.retain_raw,
                "error": {"kind": reply.error_kind, "reason": reply.error_reason} if reply.error_kind else None,
            })
            transport_check = {
                "id": "transport.usable-reply", "type": "transport", "category": "transport",
                "turn": index, "severity": "fail", "outcome": "FAIL" if reply.error_kind else "PASS",
                "reason": reply.error_reason or "HTTP 2xx with a supported, nonempty text reply.", "evidence": "",
            }
            merchants.append(turn["merchantInput"])
            if reply.error_kind:
                assertions = skipped_assertions(scenario, definition, index, "No usable reply; behavior not evaluated.")
                stopped = True
            else:
                assertions = evaluate(
                    scenario, definition, index, reply.text, history, merchants,
                    requested, identity, reply.echoed_identity,
                )
                history.append(reply.text)
            turn["assertions"] = [transport_check, *assertions]
            turn["outcome"] = classify(turn["assertions"], transport_error=bool(reply.error_kind))
    run["completedAt"] = utc_now()
    run["executionStatus"] = "COMPLETED"
    run["outcome"] = classify(
        [assertion for turn in run["turns"] for assertion in turn["assertions"]], transport_error=stopped,
    )
    return run


def execute_batch(
    scenario: Scenario, config: Config, output_root: Path,
    *, repeat: int = 5, dry_run: bool = False,
    transport: httpx.BaseTransport | None = None, sleep=time.sleep,
) -> tuple[Path, dict]:
    """The transport/sleep injection points keep development tests fully offline."""
    if type(repeat) is not int or repeat < 1:
        raise ConfigError("repeat must be a positive integer.")
    if not 1 <= config.concurrency <= 8:
        raise ConfigError("Concurrency must be between 1 and 8.")
    if not dry_run:
        endpoint_url(config.url, config.test_mode)
    created = utc_now()
    batch_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + "-" + uuid4().hex[:12]
    runs = [_plan_run(scenario, index, batch_id) for index in range(1, repeat + 1)]
    safe_ids = {run[key] for run in runs for key in ("runId", "userId", "sessionId")}
    redactor = Redactor(config, safe_ids)
    directory = output_root / batch_id
    writer = ReportWriter(directory, redactor)
    mode = "DRY_RUN" if dry_run else "EXECUTED"
    writer.write_json("manifest.json", {
        "batchId": batch_id, "executionStatus": "STARTED", "mode": mode,
        "requestedRuns": repeat, "createdAt": created,
    })
    writer.write_json("scenario.json", scenario.definition)
    if dry_run:
        for run in runs:
            writer.write_run(run)
    elif config.concurrency == 1:
        for index, run in enumerate(runs):
            if index and config.run_delay:
                sleep(config.run_delay)
            writer.write_run(_execute_run(scenario, config, run, transport, sleep))
    else:
        # A worker owns an entire conversation, never an individual turn. Pacing
        # here spaces launches; request_delay is enforced within each worker.
        with ThreadPoolExecutor(max_workers=config.concurrency) as pool:
            futures = []
            for index, run in enumerate(runs):
                if index and config.run_delay:
                    sleep(config.run_delay)
                futures.append(pool.submit(_execute_run, scenario, config, run, transport, sleep))
            for future in as_completed(futures):
                writer.write_run(future.result())
    batch = {
        "reportSchemaVersion": "1.0", "runnerVersion": __version__, "pythonVersion": platform.python_version(),
        "batchId": batch_id, "mode": mode, "createdAt": created, "completedAt": utc_now(),
        "scenario": {"id": scenario.id, "version": scenario.version, "sha256": scenario.sha256, "product": scenario.product},
        "configuration": config.public(), "metrics": metrics(runs), "defects": defects(runs), "runs": runs,
    }
    writer.finish(batch)
    return directory, redactor.clean(batch)
