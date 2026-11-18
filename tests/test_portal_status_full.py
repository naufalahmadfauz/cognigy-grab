"""The complete Portal script must never acknowledge a missing or combined action."""

from dataclasses import replace
import html
import json
from threading import Lock

import httpx
import pytest

from conftest import cognigy_response
from uc4_runner.config import Config
from uc4_runner.regrade import regrade_batch
from uc4_runner.runner import execute_batch
from uc4_runner.scenario import DEFAULT_SCENARIOS, load_catalog, load_scenario


NOTICE = "Please note that compensation will be partial, based on the assessment of the perishable items."
REPLIES = (
    "Open Finance on the left sidebar. Let me know when it is open.",
    "Click the Transactions tab. Tell me when it is open.",
    "Choose a time period covering the order date and the applicable store. Let me know when done.",
    "Under Category, choose Compensation for cancelled orders. Let me know once selected.",
    "Does the cancelled order appear there as compensated?",
)


@pytest.fixture
def full_journey():
    return load_scenario(DEFAULT_SCENARIOS / "GM-PORTAL-STATUS-FULL-001.yaml")


def scripted_transport(replies):
    requests = []

    def handler(request):
        requests.append(json.loads(request.content))
        # An extra POST beyond the supplied prefix is a test failure, not a fake reply.
        return cognigy_response(request, replies[len(requests) - 1])

    return httpx.MockTransport(handler), requests


def test_catalog_includes_one_new_five_turn_scenario(full_journey):
    assert set(load_catalog()) == {"GM-CONTINUITY-001", "GM-PORTAL-STEPS-001", full_journey.id}
    assert len(full_journey.turns) == 5
    assert all(turn["advance_when"] for turn in full_journey.turns[:4])
    assert "advance_when" not in full_journey.turns[4]


@pytest.mark.parametrize("replies", [
    pytest.param(REPLIES, id="documented-route"),
    pytest.param((
        "Please select the **Finance** menu.", "Go into Transactions, please.",
        "Select the correct store. Set the date range so it includes your order's date.",
        "Select Compensation for canceled orders in Category.",
        "Is the order listed as compensated?",
    ), id="store-first-and-paraphrases"),
    pytest.param((
        "Open Finance.", "Select Transactions.",
        "Choose a time period that includes the date your order was placed. Select your store.",
        "In the Category dropdown, pick Compensation for cancelled orders.",
        "Let me know whether the cancelled order is shown as compensated.",
    ), id="separate-filter-verbs-and-indirect-question"),
    pytest.param((*REPLIES[:4], "Can you see the cancelled order as compensated?"), id="see-as-compensated"),
    pytest.param((
        *REPLIES[:2], "Choose your store and a date range covering the order date.", REPLIES[3],
        "Does the cancelled order show up there as compensated?",
    ), id="store-first-shared-verb-and-show-up"),
])
def test_complete_journey_sends_only_the_exact_gated_script(tmp_path, full_journey, config, replies):
    transport, requests = scripted_transport(replies)
    _, batch = execute_batch(full_journey, config, tmp_path / "out", repeat=1, transport=transport)
    run = batch["runs"][0]
    assert [item["text"] for item in requests] == [turn["merchant"] for turn in full_journey.turns]
    assert len({(item["userId"], item["sessionId"]) for item in requests}) == 1
    assert run["outcome"] == "PASS" and "stoppedByGate" not in run
    assert [turn["advancement"]["outcome"] for turn in run["turns"][:4]] == ["PASS"] * 4
    assert run["turns"][4]["outcome"] == "PASS" and "advancement" not in run["turns"][4]
    assert batch["metrics"]["transport"]["attemptedTurns"] == 5
    assert batch["metrics"]["progression"] == {"gateStoppedRuns": 0, "gateSkippedTurns": 0}


@pytest.mark.parametrize("index,reply,failed_rule", [
    pytest.param(0, "When was the order cancelled?", "finance-step", id="finance-missing"),
    pytest.param(0, "Finance contains reports.", "finance-step", id="finance-bare-label"),
    pytest.param(0, "Do not open Finance.", "finance-step", id="finance-negated"),
    pytest.param(0, "Open Finance, then Transactions.", "one-step-only", id="finance-and-transactions"),
    pytest.param(0, "Open Finance. " + REPLIES[4], "one-step-only", id="finance-and-observation"),
    pytest.param(1, "Transactions contains reports.", "transactions-step", id="transactions-bare-label"),
    pytest.param(1, "Don't click Transactions.", "transactions-step", id="transactions-negated"),
    pytest.param(1, "Open Finance, then Transactions.", "transactions-step", id="shared-verb-not-next-step"),
    pytest.param(1, "Open Transactions. Open Finance.", "one-step-only", id="repeat-finance"),
    pytest.param(1, REPLIES[1] + " " + REPLIES[2], "one-step-only", id="transactions-and-filters"),
    pytest.param(2, "Select a time period covering the order date.", "period-and-store-step", id="store-missing"),
    pytest.param(2, "Select the applicable store.", "period-and-store-step", id="period-missing"),
    pytest.param(2, "Time period covering the order date and applicable store.", "period-and-store-step", id="filter-labels-only"),
    pytest.param(2, "Choose the time period and the applicable store.", "period-and-store-step", id="order-date-coverage-missing"),
    pytest.param(2, "Choose a time period not covering the order date and the applicable store.", "period-and-store-step", id="order-date-excluded"),
    pytest.param(2, "Choose a time period covering the order date. Store information is displayed.", "period-and-store-step", id="store-not-an-instruction"),
    pytest.param(2, "Choose a time period covering the order date. Do not select the store.", "period-and-store-step", id="store-negated"),
    pytest.param(2, "Do not choose a time period covering the order date and the applicable store.", "period-and-store-step", id="filters-negated"),
    pytest.param(2, REPLIES[2] + " " + REPLIES[3], "one-step-only", id="filters-and-category"),
    pytest.param(2, REPLIES[2] + " Category > Compensation for cancelled orders.", "one-step-only", id="filters-and-breadcrumb"),
    pytest.param(2, REPLIES[2] + " " + REPLIES[4], "one-step-only", id="filters-and-observation"),
    pytest.param(3, "Choose Compensation for cancelled orders.", "category-step", id="category-control-missing"),
    pytest.param(3, "Category: Compensation for cancelled orders.", "category-step", id="category-labels-only"),
    pytest.param(3, "Under Category, select Payments.", "category-step", id="wrong-category"),
    pytest.param(3, "Under Category, do not choose Compensation for cancelled orders.", "category-step", id="category-negated"),
    pytest.param(3, REPLIES[2] + " " + REPLIES[3], "one-step-only", id="repeat-filters-with-category"),
    pytest.param(3, REPLIES[3] + " " + REPLIES[4], "one-step-only", id="category-and-observation"),
    pytest.param(3, REPLIES[3] + " Let me know whether the order appears as compensated.", "one-step-only", id="category-and-indirect-observation"),
    pytest.param(3, REPLIES[3] + " Do you see the order there?", "one-step-only", id="category-and-order-visibility"),
    *[pytest.param(i, REPLIES[i] + " Use the GrabMerchant app.", "no-app-substitution", id=f"app-at-gate-{i + 1}") for i in range(4)],
    *[pytest.param(i, REPLIES[i] + " Open Help Centre.", "no-submission-navigation", id=f"submission-at-gate-{i + 1}") for i in range(4)],
])
def test_deviation_suppresses_every_later_acknowledgment(tmp_path, full_journey, config, index, reply, failed_rule):
    transport, requests = scripted_transport((*REPLIES[:index], reply))
    pauses = []
    directory, batch = execute_batch(
        full_journey, replace(config, request_delay=0.5, retain_raw=True), tmp_path / "out",
        repeat=1, transport=transport, sleep=pauses.append,
    )
    run = batch["runs"][0]
    assert [item["text"] for item in requests] == [t["merchant"] for t in full_journey.turns[:index + 1]]
    assert pauses == [0.5] * index
    assert run["outcome"] == "FAIL" and run["stoppedByGate"]["turnIndex"] == index + 1
    assert failed_rule in run["stoppedByGate"]["assertionIds"]
    stopped = run["turns"][index]
    assert stopped["agentText"] == stopped["rawResponse"]["text"] == reply
    assert stopped["advancement"]["outcome"] == "FAIL" and stopped["httpStatus"] == 200
    for turn in run["turns"][index + 1:]:
        assert turn["executionStatus"] == "SKIPPED" and turn["outcome"] is None
        assert turn["attempts"] == 0 and turn["agentText"] == "" and turn["httpStatus"] is None
        assert failed_rule in turn["skipReason"]
        assert all(a["outcome"] == "SKIP" for a in turn["assertions"])
    assert batch["metrics"]["progression"] == {"gateStoppedRuns": 1, "gateSkippedTurns": 4 - index}
    assert batch["metrics"]["transport"]["attemptedTurns"] == index + 1
    assert json.loads((directory / "runs/run-001.json").read_text()) == run
    assert json.loads((directory / "aggregate.json").read_text())["runs"][0] == run
    transcript = (directory / "transcripts/run-001.md").read_text(encoding="utf-8")
    assert transcript.count("Merchant (scripted, not sent)") == 4 - index
    assert html.escape(reply) in transcript and failed_rule in transcript


@pytest.mark.parametrize("reply,failed_rule", [
    ("The order appears there as compensated.", "compensated-status-question"),
    ("Does the order appear there?", "compensated-status-question"),
    ("Is your order eligible for compensation?", "compensated-status-question"),
    ("Don't check whether the order appears as compensated.", "compensated-status-question"),
    (REPLIES[3] + " " + REPLIES[4], "observation-only"),
    (REPLIES[4] + " Select the date range.", "observation-only"),
    (REPLIES[4] + " Submit a compensation request.", "no-submission-navigation"),
    (REPLIES[4] + " Check the status in the GrabMerchant app.", "no-app-substitution"),
])
def test_final_observation_is_graded_without_a_fifth_gate(tmp_path, full_journey, config, reply, failed_rule):
    transport, requests = scripted_transport((*REPLIES[:4], reply))
    _, batch = execute_batch(full_journey, config, tmp_path / "out", repeat=1, transport=transport)
    run = batch["runs"][0]
    assert len(requests) == 5 and run["outcome"] == "FAIL" and "stoppedByGate" not in run
    assert "advancement" not in run["turns"][4]
    assert any(a["id"] == failed_rule and a["outcome"] == "FAIL" for a in run["turns"][4]["assertions"])


def test_observed_partial_notice_is_reported_without_blocking(tmp_path, full_journey, config):
    transport, requests = scripted_transport((NOTICE + " " + REPLIES[0], *REPLIES[1:]))
    directory, batch = execute_batch(full_journey, config, tmp_path / "out", repeat=1, transport=transport)
    run = batch["runs"][0]
    assert len(requests) == 5 and run["outcome"] == "PASS_WITH_WARNINGS"
    assert all(t["advancement"]["outcome"] == "PASS" for t in run["turns"][:4])
    warnings = [a for t in run["turns"] for a in t["assertions"] if a["outcome"] == "WARN"]
    assert len(warnings) == 1 and warnings[0]["id"] == "partial-compensation-policy-review"
    assert "Human policy review" in warnings[0]["reason"]
    summary = (directory / "summary.md").read_text(encoding="utf-8")
    assert "partial-compensation-policy-review" in summary and NOTICE in summary
    assert NOTICE in (directory / "transcripts/run-001.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("index", [2, 3])
@pytest.mark.parametrize("body", [{}, {"text": "  "}])
def test_missing_late_reply_leaves_gate_unevaluated(tmp_path, full_journey, config, index, body):
    requests = []

    def handler(request):
        requests.append(json.loads(request.content))
        turn = len(requests) - 1
        return httpx.Response(200, json=body) if turn == index else cognigy_response(request, REPLIES[turn])

    _, batch = execute_batch(full_journey, config, tmp_path / "out", repeat=1, transport=httpx.MockTransport(handler))
    run = batch["runs"][0]
    assert len(requests) == index + 1 and run["outcome"] == "ERROR" and "stoppedByGate" not in run
    assert run["turns"][index]["advancement"]["outcome"] is None
    assert all(t["executionStatus"] == "SKIPPED" and t["attempts"] == 0 for t in run["turns"][index + 1:])


@pytest.mark.parametrize("concurrency", [1, 3])
def test_five_mixed_journeys_preserve_isolation_and_metrics(tmp_path, full_journey, config, concurrency):
    sessions, requests = {}, []
    lock = Lock()

    def handler(request):
        payload = json.loads(request.content)
        with lock:
            index, turn = sessions.setdefault(payload["sessionId"], [len(sessions), 0])
            sessions[payload["sessionId"]][1] += 1
            requests.append(payload)
        assert payload["text"] == full_journey.turns[turn]["merchant"]
        if index == 4 and turn == 3:
            raise httpx.ReadTimeout("mock timeout", request=request)
        reply = REPLIES[turn]
        if index == 1 and turn == 0:
            reply = NOTICE + " " + reply
        if index == 2 and turn == 2:
            reply += " " + REPLIES[3]
        if index == 3 and turn == 4:
            reply = "Your order has been compensated."
        return cognigy_response(request, reply)

    _, batch = execute_batch(full_journey, replace(config, concurrency=concurrency), tmp_path / "out",
                             repeat=5, transport=httpx.MockTransport(handler))
    stats = batch["metrics"]
    assert stats["outcomes"] == {"PASS": 1, "PASS_WITH_WARNINGS": 1, "FAIL": 2, "ERROR": 1}
    assert len(requests) == 22 and len(sessions) == len({p["userId"] for p in requests}) == 5
    assert sorted(count for _, count in sessions.values()) == [3, 4, 5, 5, 5]
    assert stats["transport"]["attemptedTurns"] == 22 and stats["transport"]["skippedTurns"] == 3
    assert stats["transport"]["errorTurns"] == 1
    assert stats["behavior"]["passRate"] == 0.5 and stats["behavior"]["endToEndPassRate"] == 0.4
    assert stats["behavior"]["observedHardFailures"] == 2
    assert stats["progression"] == {"gateStoppedRuns": 1, "gateSkippedTurns": 2}
    assert all(len({(t["userId"], t["sessionId"]) for t in r["turns"]}) == 1 for r in batch["runs"])


def test_five_dry_run_plans_have_no_evaluated_replies(tmp_path, full_journey, monkeypatch):
    def blocked(*args, **kwargs):
        raise AssertionError("Dry-run must not construct an HTTP client.")

    monkeypatch.setattr(httpx, "Client", blocked)
    _, batch = execute_batch(full_journey, Config(), tmp_path / "out", repeat=5, dry_run=True)
    assert batch["mode"] == "DRY_RUN" and len(batch["runs"]) == 5
    assert batch["metrics"]["transport"]["attemptedTurns"] == 0
    assert batch["metrics"]["behavior"]["passRate"] is None
    for run in batch["runs"]:
        assert run["outcome"] is None and len(run["turns"]) == 5
        assert all(t["executionStatus"] == "PLANNED" and t["attempts"] == 0 and t["outcome"] is None for t in run["turns"])
        assert all(t["advancement"]["outcome"] is None for t in run["turns"][:4])


def test_late_gate_stop_can_be_regraded_without_changing_capture(tmp_path, full_journey, config, monkeypatch):
    transport, _ = scripted_transport((*REPLIES[:3], REPLIES[3] + " " + REPLIES[4]))
    source, original = execute_batch(full_journey, config, tmp_path / "source", repeat=1, transport=transport)
    before = {p: p.read_bytes() for p in source.rglob("*") if p.is_file()}

    def blocked(*args, **kwargs):
        raise AssertionError("Regrade must not construct an HTTP client.")

    monkeypatch.setattr(httpx, "Client", blocked)
    _, regraded = regrade_batch(source, full_journey, Config(), tmp_path / "regrade")
    assert regraded["requestsSent"] == 0 and regraded["metrics"] == original["metrics"]
    assert regraded["runs"][0]["stoppedByGate"] == original["runs"][0]["stoppedByGate"]
    for old, new in zip(original["runs"][0]["turns"], regraded["runs"][0]["turns"], strict=True):
        assert new == {**old, "batchId": regraded["batchId"]}
    assert {p: p.read_bytes() for p in source.rglob("*") if p.is_file()} == before
