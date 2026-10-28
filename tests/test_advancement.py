"""Guarded progression at the HTTP, evidence, and offline-regrade boundaries."""

from copy import deepcopy
from dataclasses import replace
import hashlib
import json
from threading import Lock

import httpx
import pytest

from conftest import cognigy_response
from uc4_runner import cli
from uc4_runner.config import Config
from uc4_runner.regrade import RegradeError, regrade_batch
from uc4_runner.runner import execute_batch
from uc4_runner.scenario import DEFAULT_SCENARIOS, ScenarioError, load_scenario, parse_scenario


@pytest.fixture
def demo():
    return load_scenario(DEFAULT_SCENARIOS / "GM-PORTAL-STEPS-001.yaml")


def scripted_transport(replies):
    requests = []

    def handler(request):
        requests.append(json.loads(request.content))
        return cognigy_response(request, replies[len(requests) - 1])

    return httpx.MockTransport(handler), requests


def fingerprints(directory):
    return {path.relative_to(directory): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in directory.rglob("*") if path.is_file()}


@pytest.mark.parametrize("first", ["Open Finance.", "Please select the **Finance** menu.", "Go into Finance, please."])
def test_gate_pass_sends_exact_scripted_acknowledgment(tmp_path, demo, config, first):
    transport, requests = scripted_transport([first, "Now choose Transactions."])
    _, batch = execute_batch(demo, config, tmp_path / "out", repeat=1, transport=transport)
    run = batch["runs"][0]
    assert [item["text"] for item in requests] == [turn["merchant"] for turn in demo.turns]
    assert len({(item["userId"], item["sessionId"]) for item in requests}) == 1
    assert run["outcome"] == "PASS" and "stoppedByGate" not in run
    assert run["turns"][0]["advancement"]["outcome"] == "PASS"
    assert batch["metrics"]["progression"] == {"gateStoppedRuns": 0, "gateSkippedTurns": 0}


@pytest.mark.parametrize("reply,failed_rule", [
    ("When was the order cancelled?", "finance-step"),
    ("Finance contains the relevant information.", "finance-step"),
    ("Do not open Finance.", "finance-step"),
    ("Open Finance, then select Transactions.", "one-step-only"),
    ("Use the GrabMerchant app and open Finance.", "no-app-substitution"),
])
def test_unmet_gate_preserves_reply_and_stops_before_acknowledgment(tmp_path, demo, config, reply, failed_rule):
    transport, requests = scripted_transport([reply])
    directory, batch = execute_batch(demo, replace(config, retain_raw=True), tmp_path / "out", repeat=1, transport=transport)
    run = batch["runs"][0]
    first, skipped = run["turns"]
    assert len(requests) == 1 and run["outcome"] == "FAIL"
    assert first["agentText"] == first["rawResponse"]["text"] == reply
    assert first["httpStatus"] == 200 and first["error"] is None
    assert first["advancement"]["outcome"] == "FAIL"
    assert failed_rule in run["stoppedByGate"]["assertionIds"]
    assert failed_rule in skipped["skipReason"]
    assert skipped["executionStatus"] == "SKIPPED" and skipped["outcome"] is None
    assert skipped["attempts"] == 0 and skipped["agentText"] == ""
    assert all(skipped[key] is None for key in ("httpStatus", "durationSeconds", "startedAt", "completedAt", "error"))
    assert all(item["outcome"] == "SKIP" and "Advancement gate unmet" in item["reason"] for item in skipped["assertions"])
    assert batch["metrics"]["behavior"]["passRate"] == 0
    assert batch["metrics"]["transport"]["httpSuccessRate"] == 1
    assert batch["metrics"]["transport"]["errorTurns"] == 0
    summary = (directory / "summary.md").read_text(encoding="utf-8")
    assert "Gate-stopped runs: **1**" in summary and failed_rule in summary and reply in summary
    transcript = (directory / "transcripts/run-001.md").read_text(encoding="utf-8")
    assert "Merchant (scripted, not sent)" in transcript and "Advancement gate unmet" in transcript
    exported = json.loads((directory / "transcripts.json").read_text(encoding="utf-8"))["conversations"][0]
    assert exported["stoppedByGate"] == run["stoppedByGate"]
    assert exported["turns"][0]["agentText"] == reply
    assert exported["turns"][1]["skipReason"] == skipped["skipReason"]
    assert json.loads((directory / "manifest.json").read_text())["executionStatus"] == "COMPLETE"


@pytest.mark.parametrize("fail_at", [0, 1])
def test_all_remaining_turns_skip_without_requests_or_delays(tmp_path, demo, config, fail_at):
    data = deepcopy(demo.definition)
    data["turns"][1]["advance_when"] = ["transactions-step"]
    data["concepts"].update(time_period=[r"\btime period\b"], store=[r"\bstore\b"])
    data["turns"].append({"id": "filters", "merchant": "Done. Which filters should I select?", "assertions": [
        {"id": "filters-step", "type": "required", "concepts": ["time_period", "store"], "reason": "Explain both filters."},
    ]})
    scenario = parse_scenario(data)
    replies = ["Open Finance.", "Select Transactions."][:fail_at] + ["I cannot give that instruction."]
    transport, requests = scripted_transport(replies)
    pauses = []
    _, batch = execute_batch(scenario, replace(config, request_delay=0.5), tmp_path / "out", repeat=1,
                             transport=transport, sleep=pauses.append)
    run = batch["runs"][0]
    assert len(requests) == fail_at + 1 and pauses == [0.5] * fail_at
    assert run["outcome"] == "FAIL" and run["stoppedByGate"]["turnIndex"] == fail_at + 1
    assert all(turn["executionStatus"] == "SKIPPED" and turn["attempts"] == 0 for turn in run["turns"][fail_at + 1:])
    assert batch["metrics"]["progression"]["gateSkippedTurns"] == 2 - fail_at


@pytest.mark.parametrize("kind", ["missing", "empty", "invalid-json", "timeout"])
def test_unusable_reply_remains_transport_error_and_gate_is_unevaluated(tmp_path, demo, config, kind):
    requests = []

    def handler(request):
        requests.append(request)
        if kind == "timeout":
            raise httpx.ReadTimeout("ambiguous", request=request)
        if kind == "invalid-json":
            return httpx.Response(200, text="invalid-json")
        return httpx.Response(200, json={} if kind == "missing" else {"text": "  "})

    source, batch = execute_batch(demo, config, tmp_path / "out", repeat=1, transport=httpx.MockTransport(handler))
    run = batch["runs"][0]
    assert len(requests) == 1 and run["outcome"] == "ERROR"
    assert "stoppedByGate" not in run and run["turns"][0]["advancement"]["outcome"] is None
    assert run["turns"][1]["executionStatus"] == "SKIPPED"
    assert batch["metrics"]["behavior"]["passRate"] is None
    assert batch["metrics"]["progression"] == {"gateStoppedRuns": 0, "gateSkippedTurns": 0}
    _, regraded = regrade_batch(source, demo, Config(), tmp_path / "regrade")
    assert regraded["metrics"] == batch["metrics"]


@pytest.mark.parametrize("severity,expected", [("fail", "FAIL"), ("warning", "PASS_WITH_WARNINGS")])
def test_only_explicit_gate_controls_progression(tmp_path, demo, config, severity, expected):
    data = deepcopy(demo.definition)
    data["concepts"]["unrelated"] = [r"\breassurance\b"]
    data["turns"][0]["assertions"].append({
        "id": "other-check", "type": "required", "severity": severity,
        "concepts": ["unrelated"], "reason": "An ordinary grading expectation.",
    })
    transport, requests = scripted_transport(["Select Finance.", "Open Transactions."])
    _, batch = execute_batch(parse_scenario(data), config, tmp_path / "out", repeat=1, transport=transport)
    assert len(requests) == 2 and batch["runs"][0]["outcome"] == expected
    assert batch["runs"][0]["turns"][0]["advancement"]["outcome"] == "PASS"


def test_no_gate_preserves_continuation_after_early_behavior_failure(tmp_path, scenario, config, good_replies):
    transport, requests = scripted_transport(["I don't know.", good_replies[1]])
    _, batch = execute_batch(scenario, config, tmp_path / "out", repeat=1, transport=transport)
    assert len(requests) == 2 and batch["runs"][0]["outcome"] == "FAIL"
    assert all(turn["executionStatus"] == "EXECUTED" and "advancement" not in turn for turn in batch["runs"][0]["turns"])
    assert "progression" not in batch["metrics"]


@pytest.mark.parametrize("reply,expected", [
    ("Go to the Portal, then Finance.", "PASS"),
    ("Finance, followed by the Portal.", "FAIL"),
])
def test_gate_reuses_ordered_concept_matching(tmp_path, demo, config, reply, expected):
    data = deepcopy(demo.definition)
    data["concepts"].update(portal=[r"\bportal\b"], finance=[r"\bfinance\b"])
    rule = data["turns"][0]["assertions"][0]
    rule.pop("concepts")
    rule.update(type="ordered", steps=["portal", "finance"])
    transport, requests = scripted_transport([reply, "Select Transactions."])
    _, batch = execute_batch(parse_scenario(data), config, tmp_path / "out", repeat=1, transport=transport)
    assert batch["runs"][0]["outcome"] == expected
    assert len(requests) == (2 if expected == "PASS" else 1)


@pytest.mark.parametrize("reply", [
    "Open Finance, then select Transactions.",
    "Open Transactions and select the time period and store.",
])
def test_demo_final_reply_also_requires_one_navigation_step(tmp_path, demo, config, reply):
    transport, requests = scripted_transport(["Open Finance.", reply])
    _, batch = execute_batch(demo, config, tmp_path / "out", repeat=1, transport=transport)
    run = batch["runs"][0]
    assert len(requests) == 2 and run["outcome"] == "FAIL"
    assert "stoppedByGate" not in run  # Final-turn grading needs no advancement gate.
    assert any(item["id"] == "one-step-only" and item["outcome"] == "FAIL" for item in run["turns"][1]["assertions"])


@pytest.mark.parametrize("concurrency", [1, 3])
def test_five_isolated_runs_mix_gate_stops_errors_and_completed_grades(tmp_path, demo, config, concurrency):
    sessions, requests = {}, []
    lock = Lock()

    def handler(request):
        payload = json.loads(request.content)
        with lock:
            index, turn = sessions.setdefault(payload["sessionId"], [len(sessions), 0])
            sessions[payload["sessionId"]][1] += 1
            requests.append(payload)
        assert payload["text"] == demo.turns[turn]["merchant"]
        if index == 4:
            raise httpx.ReadTimeout("ambiguous", request=request)
        text = "Select Finance." if turn == 0 else "Open Transactions."
        if index == 2:
            text = "When was the order cancelled?"
        if index == 3 and turn == 1:
            text = "I don't know."
        response = cognigy_response(request, text)
        if index == 1:
            body = response.json()
            body.pop("userId")
            body.pop("sessionId")
            response = httpx.Response(200, json=body)
        return response

    directory, batch = execute_batch(demo, replace(config, concurrency=concurrency), tmp_path / "out",
                                     repeat=5, transport=httpx.MockTransport(handler))
    stats = batch["metrics"]
    assert stats["outcomes"] == {"PASS": 1, "PASS_WITH_WARNINGS": 1, "FAIL": 2, "ERROR": 1}
    assert len(requests) == 8 and len(sessions) == len({r["userId"] for r in requests}) == 5
    assert sorted(count for _, count in sessions.values()) == [1, 1, 2, 2, 2]
    assert stats["transport"]["attemptedTurns"] == 8 and stats["transport"]["skippedTurns"] == 2
    assert stats["transport"]["errorTurns"] == 1 and stats["transport"]["completeRunRate"] == 0.8
    assert stats["behavior"]["passRate"] == 0.5 and stats["behavior"]["endToEndPassRate"] == 0.4
    assert stats["behavior"]["observedHardFailures"] == 2  # Gate references don't double-count defects.
    assert stats["progression"] == {"gateStoppedRuns": 1, "gateSkippedTurns": 1}
    assert len(list((directory / "runs").glob("*.json"))) == 5
    assert [run["runIndex"] for run in batch["runs"]] == [1, 2, 3, 4, 5]
    assert all(len({(t["userId"], t["sessionId"]) for t in run["turns"]}) == 1 for run in batch["runs"])


def test_gate_dry_run_is_only_a_plan(tmp_path, demo, monkeypatch):
    def blocked(*args, **kwargs):
        raise AssertionError("Dry-run must not construct an HTTP client.")

    monkeypatch.setattr(httpx, "Client", blocked)
    _, batch = execute_batch(demo, Config(), tmp_path / "out", dry_run=True)
    assert batch["metrics"]["plannedRuns"] == 5 and batch["metrics"]["behavior"]["passRate"] is None
    for run in batch["runs"]:
        assert run["outcome"] is None and run["turns"][0]["advancement"]["outcome"] is None
        assert all(turn["executionStatus"] == "PLANNED" and turn["attempts"] == 0 for turn in run["turns"])


@pytest.mark.parametrize("gate", [None, [], "finance-step", ["unknown"], ["finance-step", "finance-step"], [42], [[]], ["identity-continuity"]])
def test_invalid_gate_references_are_rejected(demo, gate):
    data = deepcopy(demo.definition)
    data["turns"][0]["advance_when"] = gate
    with pytest.raises(ScenarioError, match="advance_when"):
        parse_scenario(data)


@pytest.mark.parametrize("change", [
    lambda d: d["turns"][0]["assertions"][0].update(severity="warning"),
    lambda d: d["turns"][0]["assertions"][0].update(products=["GrabFood"]),
    lambda d: d["turns"][0]["assertions"][0].update(allow_merchant_context=["finance_instruction"]),
    lambda d: d["turns"][0]["assertions"][1].update(unless_response_concepts=["finance_instruction"]),
    lambda d: d["turns"][0]["assertions"][1].update(unless_merchant_concepts=["finance_instruction"]),
    lambda d: d["turns"][0]["assertions"][1].update(warn_if_response_concepts=["finance_instruction"]),
    lambda d: d["turns"][1].update(advance_when=["transactions-step"]),
])
def test_gates_need_unconditional_hard_response_checks_and_a_next_turn(demo, change):
    data = deepcopy(demo.definition)
    change(data)
    with pytest.raises(ScenarioError, match="advance_when"):
        parse_scenario(data)


@pytest.mark.parametrize("replies", [
    ["Select Finance.", "Open Transactions."],
    ["When was the order cancelled?"],
])
def test_regrade_preserves_gate_path_capture_metadata_and_source_files(tmp_path, demo, config, replies, monkeypatch):
    transport, _ = scripted_transport(replies)
    source, original = execute_batch(demo, replace(config, retain_raw=True), tmp_path / "source", repeat=1, transport=transport)
    before = fingerprints(source)

    def blocked(*args, **kwargs):
        raise AssertionError("Regrade must never construct an HTTP client.")

    monkeypatch.setattr(httpx, "Client", blocked)
    first_dir, first = regrade_batch(source, demo, Config(retain_raw=True), tmp_path / "out")
    _, second = regrade_batch(first_dir, demo, Config(retain_raw=True), tmp_path / "out")
    assert fingerprints(source) == before
    assert original["metrics"] == first["metrics"] == second["metrics"]
    assert first["requestsSent"] == second["requestsSent"] == 0
    for result in (first, second):
        run = result["runs"][0]
        assert run.get("stoppedByGate") == original["runs"][0].get("stoppedByGate")
        for old, new in zip(original["runs"][0]["turns"], run["turns"], strict=True):
            for key in ("agentText", "merchantInput", "rawResponse", "executionStatus", "httpStatus", "traceIds", "startedAt", "completedAt", "advancement"):
                assert old.get(key) == new.get(key)


@pytest.mark.parametrize("change", ["relax", "remove", "tighten"])
def test_regrade_rejects_changed_progression_before_writing(tmp_path, demo, config, change):
    replies = ["Select Finance.", "Open Transactions."] if change == "tighten" else ["When was the order cancelled?"]
    transport, _ = scripted_transport(replies)
    source, _ = execute_batch(demo, config, tmp_path / "source", repeat=1, transport=transport)
    data = deepcopy(demo.definition)
    if change == "remove":
        data["turns"][0].pop("advance_when")
    else:
        data["concepts"]["finance_instruction"] = [r"\babsent phrase\b"] if change == "tighten" else [r"\bcancelled\b"]
    data["version"] = "0.2.1"
    before = fingerprints(source)
    with pytest.raises(RegradeError, match="captured progression path"):
        regrade_batch(source, parse_scenario(data), Config(), tmp_path / "regrade")
    assert not (tmp_path / "regrade").exists() and fingerprints(source) == before


def test_regrade_allows_changed_stopping_assertion_with_same_path(tmp_path, demo, config):
    transport, _ = scripted_transport(["When was the order cancelled?"])
    source, original = execute_batch(demo, config, tmp_path / "source", repeat=1, transport=transport)
    data = deepcopy(demo.definition)
    data["turns"][0]["assertions"][0]["id"] = "revised-finance-step"
    data["turns"][0]["advance_when"][0] = "revised-finance-step"
    revised = parse_scenario(data)
    directory, result = regrade_batch(source, revised, Config(), tmp_path / "out")
    _, again = regrade_batch(directory, revised, Config(), tmp_path / "out")
    assert again["runs"][0]["stoppedByGate"] == result["runs"][0]["stoppedByGate"] == original["runs"][0]["stoppedByGate"]
    assert result["runs"][0]["outcome"] == "FAIL"
    assert result["runs"][0]["turns"][0]["advancement"]["assertionIds"][0] == "revised-finance-step"


@pytest.mark.parametrize("change", [
    lambda r: r.pop("stoppedByGate"),
    lambda r: r.update(outcome="PASS"),
    lambda r: r["stoppedByGate"].update(turnIndex=2),
    lambda r: r["stoppedByGate"].update(turnId="different"),
    lambda r: r["turns"][0].pop("advancement"),
    lambda r: r["turns"][0]["advancement"].update(outcome="PASS"),
    lambda r: r["turns"][0]["advancement"].update(assertionIds=["unknown"]),
    lambda r: r["turns"][1].pop("skipReason"),
    lambda r: r["turns"][1].update(agentText="fabricated response"),
    lambda r: r["turns"][1].update(attempts=1),
])
def test_inconsistent_gate_capture_is_rejected(tmp_path, demo, config, change):
    transport, _ = scripted_transport(["When was the order cancelled?"])
    source, batch = execute_batch(demo, config, tmp_path / "source", repeat=1, transport=transport)
    change(batch["runs"][0])
    (source / "aggregate.json").write_text(json.dumps(batch), encoding="utf-8")
    with pytest.raises(RegradeError):
        regrade_batch(source, demo, Config(), tmp_path / "out")
    assert not (tmp_path / "out").exists()


def test_gate_failure_keeps_behavioral_cli_exit(tmp_path, demo, config):
    transport, _ = scripted_transport(["When was the order cancelled?"])
    source, _ = execute_batch(demo, config, tmp_path / "source", repeat=1, transport=transport)
    assert cli.main(["regrade", "--batch", str(source), "--scenario", demo.id, "--output-dir", str(tmp_path / "out")]) == 1
