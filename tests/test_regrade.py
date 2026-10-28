"""Regrade uses production evaluation and reporting, with network creation blocked."""

from copy import deepcopy
from dataclasses import replace
import hashlib
import json

import httpx
import pytest

from conftest import PROJECT
from uc4_runner import cli
from uc4_runner.assertions import evaluate_run
from uc4_runner.config import Config
from uc4_runner.regrade import RegradeError, regrade_batch
from uc4_runner.runner import execute_batch
from uc4_runner.scenario import parse_scenario


EXPECTED_OUTCOMES = ["FAIL", "PASS_WITH_WARNINGS", "PASS_WITH_WARNINGS", "PASS_WITH_WARNINGS", "FAIL"]


@pytest.fixture
def recorded_batch(tmp_path, scenario):
    """Reviewed live text + synthetic capture metadata, no historical credentials/PII."""
    fixture = json.loads((PROJECT / "tests/fixtures/gm-continuity-live-v0.1.0.json").read_text(encoding="utf-8"))
    batch_id = fixture["sourceBatchId"]
    version = fixture["sourceScenarioVersion"]
    scenario_hash = "dc5cefdd2e931a08aeff5c54b5f8cb4d3a9cd7b802d070b3c08df0becad35be0"
    captured_at = "2026-10-28T13:08:52.758Z"
    runs = []
    for item in fixture["runs"]:
        index = item["runIndex"]
        run = {
            "runId": f"fixture-run-{index}", "batchId": batch_id, "runIndex": index,
            "userId": f"fixture-user-{index}", "sessionId": f"fixture-session-{index}",
            "scenarioId": scenario.id, "scenarioVersion": version, "scenarioSha256": scenario_hash,
            "plannedAt": captured_at, "startedAt": captured_at, "completedAt": captured_at,
            "executionStatus": "COMPLETED", "outcome": item["originalOutcome"], "turns": [],
        }
        for turn_index, text in enumerate(item["replies"], 1):
            turn = {
                "turnId": scenario.turns[turn_index - 1]["id"], "turnIndex": turn_index,
                "runId": run["runId"], "batchId": batch_id, "userId": run["userId"], "sessionId": run["sessionId"],
                "merchantInput": fixture["merchantInputs"][turn_index - 1], "agentText": text,
                "startedAt": captured_at, "completedAt": captured_at, "durationSeconds": 0.25,
                "executionStatus": "EXECUTED", "attempts": 1, "httpStatus": 200, "traceIds": [f"fixture-trace-{index}-{turn_index}"],
                "echoedIdentity": {"userId": run["userId"], "sessionId": run["sessionId"]},
                "rawResponse": {"text": text, "outputStack": [{"text": text, "source": "bot"}]},
                "rawBody": None, "rawEvidenceRetained": True, "normalizationNotes": [], "error": None,
                "assertions": [{
                    "id": name, "turn": turn_index, "outcome": outcome, "category": "behavior",
                    "reason": "Recorded v0.1.0 assertion outcome.",
                } for name, outcome in item["originalAssertionOutcomes"][turn_index - 1].items()],
            }
            turn["outcome"] = "FAIL" if any(a["outcome"] == "FAIL" for a in turn["assertions"]) else (
                "PASS_WITH_WARNINGS" if any(a["outcome"] == "WARN" for a in turn["assertions"]) else "PASS"
            )
            run["turns"].append(turn)
        runs.append(run)
    batch = {
        "reportSchemaVersion": "1.0", "runnerVersion": "0.1.0", "batchId": batch_id, "mode": "EXECUTED",
        "scenario": {"id": scenario.id, "version": version, "sha256": scenario_hash, "product": scenario.product},
        "configuration": {"testMode": True, "retainRawEvidence": True},
        "createdAt": captured_at, "completedAt": captured_at, "runs": runs,
    }
    source = tmp_path / "original"
    source.mkdir()
    (source / "aggregate.json").write_text(json.dumps(batch, ensure_ascii=False), encoding="utf-8")
    (source / "summary.md").write_text("Original report must remain unchanged.", encoding="utf-8")
    return source, batch


def no_client(*args, **kwargs):
    raise AssertionError("Offline regrade must never construct an HTTP client.")


def fingerprints(directory):
    return {str(path.relative_to(directory)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in directory.rglob("*") if path.is_file()}


def test_live_transcripts_match_review_targets_through_production_engine(recorded_batch, scenario):
    _, batch = recorded_batch
    outcomes = []
    for run in batch["runs"]:
        evaluate_run(scenario, run)
        outcomes.append(run["outcome"])
        assert any(a["id"] == "unsupported-preparation" and a["outcome"] == "WARN"
                   for a in run["turns"][0]["assertions"])
    assert outcomes == EXPECTED_OUTCOMES
    first_followup = {a["id"]: a["outcome"] for a in batch["runs"][0]["turns"][1]["assertions"]}
    assert first_followup["portal-route"] == "FAIL" and first_followup["no-app-substitution"] == "PASS"
    fourth_followup = {a["id"]: a["outcome"] for a in batch["runs"][3]["turns"][1]["assertions"]}
    assert fourth_followup["answer-location-before-order-age"] == "WARN"


def test_offline_regrade_preserves_original_and_compares_all_five_runs(tmp_path, recorded_batch, scenario, monkeypatch):
    source, original = recorded_batch
    before = fingerprints(source)
    monkeypatch.setattr(httpx, "Client", no_client)
    directory, batch = regrade_batch(source, scenario, Config(retain_raw=True), tmp_path / "regrades")
    assert fingerprints(source) == before
    assert batch["mode"] == "REGRADE" and batch["requestsSent"] == 0
    assert batch["source"]["aggregateSha256"] == before["aggregate.json"]
    assert batch["source"]["batchId"] == original["batchId"]
    assert batch["source"]["scenario"]["version"] == "0.1.0" and batch["scenario"]["version"] == "0.1.1"
    assert [run["outcome"] for run in batch["runs"]] == EXPECTED_OUTCOMES
    assert batch["metrics"]["outcomes"] == {"PASS": 0, "PASS_WITH_WARNINGS": 3, "FAIL": 2, "ERROR": 0}
    comparison = json.loads((directory / "comparison.json").read_text(encoding="utf-8"))
    assert comparison["originalMetrics"]["behavior"]["passRate"] == 0.4
    assert comparison["updatedMetrics"]["behavior"]["passRate"] == 0.6
    assert comparison["originalMetrics"]["transport"] == comparison["updatedMetrics"]["transport"]
    assert batch["metrics"]["transport"]["httpSuccessfulTurns"] == 10
    for old, new in zip(original["runs"], batch["runs"], strict=True):
        for key in ("runId", "userId", "sessionId", "startedAt", "completedAt"):
            assert new[key] == old[key]
        for old_turn, new_turn in zip(old["turns"], new["turns"], strict=True):
            for key in ("merchantInput", "agentText", "rawResponse", "traceIds", "httpStatus", "durationSeconds"):
                assert new_turn[key] == old_turn[key]
    preparation = next(item for item in batch["defects"] if item["assertionId"] == "unsupported-preparation")
    assert preparation["outcome"] == "WARN" and preparation["runIndexes"] == [1, 2, 3, 4, 5]
    assert len(list((directory / "runs").glob("*.json"))) == 5
    assert len(json.loads((directory / "transcripts.json").read_text(encoding="utf-8"))["conversations"]) == 5
    summary = (directory / "summary.md").read_text(encoding="utf-8")
    assert "40.0% → 60.0%" in summary and "Zero requests sent" in summary
    assert "| 2 | FAIL | PASS_WITH_WARNINGS |" in summary
    assert "answer-location-before-order-age" in summary and "fixture-trace-4-2" in summary
    assert json.loads((directory / "manifest.json").read_text())["executionStatus"] == "COMPLETE"


def test_cli_regrade_is_offline_and_returns_behavioral_fail_exit(tmp_path, recorded_batch, monkeypatch, capsys):
    source, _ = recorded_batch
    monkeypatch.setattr(httpx, "Client", no_client)
    code = cli.main(["regrade", "--batch", str(source), "--scenario", "GM-CONTINUITY-001", "--output-dir", str(tmp_path / "out")])
    assert code == 1  # Two genuine behavioral failures remain.
    assert "2/5 -> 3/5" in capsys.readouterr().out


def test_regrading_twice_is_deterministic_and_writes_new_directories(tmp_path, recorded_batch, scenario):
    source, _ = recorded_batch
    first_dir, first = regrade_batch(source / "aggregate.json", scenario, Config(), tmp_path / "out")
    second_dir, second = regrade_batch(source, scenario, Config(), tmp_path / "out")
    assert first_dir != second_dir and first["metrics"] == second["metrics"]
    assert first["comparison"] == second["comparison"]
    for old, new in zip(first["runs"], second["runs"], strict=True):
        assert [turn["assertions"] for turn in old["turns"]] == [turn["assertions"] for turn in new["turns"]]


def test_regrade_keeps_transport_errors_and_skipped_turns(tmp_path, scenario, config):
    def timeout(request):
        raise httpx.ReadTimeout("ambiguous timeout", request=request)

    source, original = execute_batch(scenario, config, tmp_path / "captures", repeat=1, transport=httpx.MockTransport(timeout))
    _, regraded = regrade_batch(source, scenario, Config(), tmp_path / "out")
    assert regraded["runs"][0]["outcome"] == "ERROR"
    assert regraded["runs"][0]["turns"][1]["executionStatus"] == "SKIPPED"
    assert regraded["metrics"] == original["metrics"]
    assert regraded["metrics"]["behavior"]["passRate"] is None


def test_regrade_matches_live_execution_grading(tmp_path, scenario, config, successful_transport):
    transport, _ = successful_transport
    source, original = execute_batch(scenario, config, tmp_path / "captures", repeat=2, transport=transport)
    _, updated = regrade_batch(source, scenario, Config(), tmp_path / "out")
    assert updated["metrics"] == original["metrics"]
    for old, new in zip(original["runs"], updated["runs"], strict=True):
        assert [t["assertions"] for t in old["turns"]] == [t["assertions"] for t in new["turns"]]


def test_mismatched_identity_remains_a_failure_after_regrade(tmp_path, recorded_batch, scenario):
    source, batch = recorded_batch
    batch["runs"][1]["turns"][1]["echoedIdentity"]["sessionId"] = "different-session"
    (source / "aggregate.json").write_text(json.dumps(batch), encoding="utf-8")
    _, result = regrade_batch(source, scenario, Config(), tmp_path / "out")
    assert result["runs"][1]["outcome"] == "FAIL"
    assert any(item["id"] == "identity-continuity" and item["outcome"] == "FAIL"
               for item in result["runs"][1]["turns"][1]["assertions"])


@pytest.mark.parametrize("retain", [False, True])
def test_regrade_raw_retention_and_redaction(tmp_path, recorded_batch, scenario, retain):
    source, batch = recorded_batch
    batch["runs"][0]["turns"][0]["rawResponse"]["data"] = {"apiKey": "fixture-private-key", "note": "fixture-personal-name"}
    batch["configuration"]["endpointUrl"] = "https://example.invalid/private-token"
    (source / "aggregate.json").write_text(json.dumps(batch), encoding="utf-8")
    before = fingerprints(source)
    directory, updated = regrade_batch(source, scenario, Config(retain_raw=retain, redact_values=("fixture-personal-name",)), tmp_path / "out")
    turn = updated["runs"][0]["turns"][0]
    assert turn["rawEvidenceRetained"] == retain
    assert (turn["rawResponse"] is not None) == retain
    assert fingerprints(source) == before
    for path in directory.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            assert "fixture-private-key" not in text and "fixture-personal-name" not in text and "private-token" not in text


@pytest.mark.parametrize("change", [
    lambda b: b.update(mode="DRY_RUN"),
    lambda b: b.update(reportSchemaVersion="99"),
    lambda b: b.update(runs=[]),
    lambda b: b["scenario"].update(id="other"),
    lambda b: b["scenario"].update(product="GrabFood"),
    lambda b: b["runs"][0].update(executionStatus="PLANNED"),
    lambda b: b["runs"][0].update(outcome="ERROR"),
    lambda b: b["runs"][1].update(runIndex=1),
    lambda b: b["runs"][0]["turns"].pop(),
    lambda b: b["runs"][0]["turns"][0].update(merchantInput="different conversation"),
    lambda b: b["runs"][0]["turns"][0].update(turnIndex=2),
    lambda b: b["runs"][0]["turns"][0].update(agentText=""),
    lambda b: b["runs"][0]["turns"][0].update(httpStatus=500),
    lambda b: b["runs"][0]["turns"][0].update(error={"kind": "timeout"}),
    lambda b: b["runs"][0]["turns"][0].update(traceIds="not-list"),
    lambda b: b["runs"][0]["turns"][0].update(echoedIdentity=[]),
    lambda b: b["runs"][0]["turns"][0].update(executionStatus="SKIPPED"),
    lambda b: b["runs"][0]["turns"][0].update(durationSeconds=-1),
])
def test_incompatible_evidence_is_rejected_before_writing(tmp_path, recorded_batch, scenario, change):
    source, batch = recorded_batch
    change(batch)
    (source / "aggregate.json").write_text(json.dumps(batch), encoding="utf-8")
    with pytest.raises(RegradeError):
        regrade_batch(source, scenario, Config(), tmp_path / "out")
    assert not (tmp_path / "out").exists()


def test_changed_merchant_script_cannot_be_regraded_as_the_same_experiment(tmp_path, recorded_batch, scenario):
    data = deepcopy(scenario.definition)
    data["turns"][0]["merchant"] = "A different question."
    with pytest.raises(RegradeError, match="merchant messages"):
        regrade_batch(recorded_batch[0], parse_scenario(data), Config(), tmp_path / "out")


def test_output_must_be_outside_original_batch(recorded_batch, scenario):
    source, _ = recorded_batch
    before = fingerprints(source)
    with pytest.raises(RegradeError, match="outside"):
        regrade_batch(source, scenario, Config(), source / "nested-output")
    assert fingerprints(source) == before


def test_invalid_json_regrade_fails_cleanly_without_echoing_content(tmp_path, capsys):
    path = tmp_path / "broken.json"
    path.write_text('{"secret":"private-value"', encoding="utf-8")
    assert cli.main(["regrade", "--batch", str(path), "--scenario", "GM-CONTINUITY-001"]) == 2
    assert "private-value" not in capsys.readouterr().err
