from dataclasses import replace
import json
from threading import Barrier, Lock

import httpx

from conftest import cognigy_response
from uc4_runner.runner import execute_batch


def test_five_independent_two_turn_runs_write_all_evidence(tmp_path, scenario, config, successful_transport):
    transport, requests = successful_transport
    config = replace(config, retain_raw=True)
    directory, batch = execute_batch(scenario, config, tmp_path / "reports", repeat=5, transport=transport)
    assert len(requests) == 10
    assert batch["metrics"]["outcomes"] == {"PASS": 5, "PASS_WITH_WARNINGS": 0, "FAIL": 0, "ERROR": 0}
    assert batch["metrics"]["behavior"]["passRate"] == 1
    assert batch["metrics"]["transport"]["completeRunRate"] == 1
    assert len({run["runId"] for run in batch["runs"]}) == 5
    assert len({request["userId"] for request in requests}) == 5
    assert len({request["sessionId"] for request in requests}) == 5
    for index, run in enumerate(batch["runs"]):
        first, second = requests[index * 2:index * 2 + 2]
        assert first["userId"] == second["userId"] == run["userId"]
        assert first["sessionId"] == second["sessionId"] == run["sessionId"]
        assert first["text"] == scenario.turns[0]["merchant"]
        assert second["text"] == scenario.turns[1]["merchant"]
        assert run["runIndex"] == index + 1 and run["startedAt"] and run["completedAt"]
        report = json.loads((directory / "runs" / f"run-{index + 1:03d}.json").read_text(encoding="utf-8"))
        assert len(report["turns"]) == 2
        for turn in report["turns"]:
            assert turn["traceIds"] == ["trace-fixture-001"]
            assert turn["rawResponse"]["outputStack"]
            assert turn["httpStatus"] == 200 and turn["durationSeconds"] >= 0
            assert turn["attempts"] == 1 and turn["assertions"]
    aggregate = json.loads((directory / "aggregate.json").read_text(encoding="utf-8"))
    assert len(aggregate["runs"]) == 5
    transcripts = json.loads((directory / "transcripts.json").read_text(encoding="utf-8"))
    assert len(transcripts["conversations"]) == 5
    assert len(list((directory / "transcripts").glob("*.md"))) == 5
    markdown = (directory / "summary.md").read_text(encoding="utf-8")
    assert "100.0%" in markdown and "trace-fixture-001" in markdown
    assert json.loads((directory / "manifest.json").read_text())["executionStatus"] == "COMPLETE"


def test_new_batch_never_reuses_identity(tmp_path, scenario, config, successful_transport):
    transport, _ = successful_transport
    _, first = execute_batch(scenario, config, tmp_path / "reports", repeat=1, transport=transport)
    _, second = execute_batch(scenario, config, tmp_path / "reports", repeat=1, transport=transport)
    for key in ("runId", "userId", "sessionId"):
        assert first["runs"][0][key] != second["runs"][0][key]


def test_mixed_batch_separates_transport_and_behavior(tmp_path, scenario, config, good_replies):
    sessions = {}

    def handler(request):
        data = json.loads(request.content)
        session = data["sessionId"]
        if session not in sessions:
            sessions[session] = len(sessions) + 1
        run_index = sessions[session]
        turn_index = 0 if data["text"] == scenario.turns[0]["merchant"] else 1
        if run_index == 5:
            raise httpx.ReadTimeout("ambiguous timeout", request=request)
        text = good_replies[turn_index]
        if run_index in {3, 4} and turn_index == 1:
            text = "When was the order cancelled?"
        if run_index == 2 and turn_index == 0:
            text += " How may I help you today?"
        return cognigy_response(request, text)

    directory, batch = execute_batch(scenario, config, tmp_path / "reports", transport=httpx.MockTransport(handler))
    stats = batch["metrics"]
    assert stats["outcomes"] == {"PASS": 1, "PASS_WITH_WARNINGS": 1, "FAIL": 2, "ERROR": 1}
    assert stats["transport"]["attemptedTurns"] == 9
    assert stats["transport"]["skippedTurns"] == 1
    assert stats["transport"]["completeRunRate"] == 0.8
    assert stats["behavior"]["evaluatedRuns"] == 4
    assert stats["behavior"]["passRate"] == 0.5
    assert stats["behavior"]["endToEndPassRate"] == 0.4
    assert stats["behavior"]["strictPassRate"] == 0.25
    defect = next(item for item in batch["defects"] if item["assertionId"] == "answer-location-before-order-age")
    assert defect["occurrences"] == 2 and defect["runIndexes"] == [3, 4]
    assert "When was the order cancelled?" in (directory / "summary.md").read_text(encoding="utf-8")
    assert batch["runs"][-1]["turns"][1]["executionStatus"] == "SKIPPED"


def test_200_invalid_json_is_error_not_behavior_failure(tmp_path, scenario, config):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, text="invalid-json")

    _, batch = execute_batch(scenario, config, tmp_path / "reports", repeat=1, transport=httpx.MockTransport(handler))
    assert len(calls) == 1
    assert batch["metrics"]["transport"]["httpSuccessRate"] == 1
    assert batch["metrics"]["transport"]["usableReplyRate"] == 0
    assert batch["metrics"]["behavior"]["passRate"] is None
    assert batch["runs"][0]["outcome"] == "ERROR"


def test_delays_are_applied_between_turns_and_runs(tmp_path, scenario, config, successful_transport):
    transport, requests = successful_transport
    pauses = []

    def sleep(seconds):
        pauses.append((seconds, len(requests)))

    execute_batch(
        scenario, replace(config, request_delay=0.5, run_delay=2), tmp_path / "reports",
        repeat=2, transport=transport, sleep=sleep,
    )
    assert pauses == [(0.5, 1), (2, 2), (0.5, 3)]


def test_bounded_concurrency_preserves_sequential_turns(tmp_path, scenario, config, good_replies):
    lock = Lock()
    pair = Barrier(2, timeout=5)
    sessions = {}
    active = set()
    peak = 0

    def handler(request):
        nonlocal peak
        data = json.loads(request.content)
        session = data["sessionId"]
        with lock:
            assert session not in active
            active.add(session)
            peak = max(peak, len(active))
            turn = sessions.get(session, 0)
            assert data["text"] == scenario.turns[turn]["merchant"]
            sessions[session] = turn + 1
        # Pair the first turns to prove actual inter-session concurrency.
        if turn == 0:
            pair.wait()
        response = cognigy_response(request, good_replies[turn])
        with lock:
            active.remove(session)
        return response

    _, batch = execute_batch(
        scenario, replace(config, concurrency=2), tmp_path / "reports", repeat=4,
        transport=httpx.MockTransport(handler),
    )
    assert peak == 2 and len(sessions) == 4 and set(sessions.values()) == {2}
    assert batch["metrics"]["outcomes"]["PASS"] == 4
    assert [run["runIndex"] for run in batch["runs"]] == [1, 2, 3, 4]


def test_raw_retention_is_off_by_default(tmp_path, scenario, config, successful_transport):
    transport, _ = successful_transport
    directory, batch = execute_batch(scenario, config, tmp_path / "reports", repeat=1, transport=transport)
    assert batch["runs"][0]["turns"][0]["rawResponse"] is None
    report = (directory / "runs" / "run-001.json").read_text(encoding="utf-8")
    assert '"rawEvidenceRetained": false' in report and '"outputStack"' not in report


def test_cookie_jars_are_isolated_between_runs(tmp_path, scenario, config, good_replies):
    sessions = {}

    def handler(request):
        data = json.loads(request.content)
        first = data["sessionId"] not in sessions
        if first:
            assert "cookie" not in request.headers
            sessions[data["sessionId"]] = True
        response = cognigy_response(request, good_replies[0 if first else 1])
        response.headers["set-cookie"] = "conversation=example; Path=/"
        return response

    execute_batch(scenario, config, tmp_path / "reports", repeat=2, transport=httpx.MockTransport(handler))
    assert len(sessions) == 2
