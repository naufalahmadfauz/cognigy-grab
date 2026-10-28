from copy import deepcopy

import pytest

from uc4_runner.assertions import classify, evaluate
from uc4_runner.scenario import parse_scenario


def check(scenario, text, index=1, *, previous=None, merchants=None, echo=None):
    identity = {"userId": "synthetic-user", "sessionId": "synthetic-session"}
    return evaluate(
        scenario, scenario.turns[index - 1], index, text, previous or [],
        merchants or [turn["merchant"] for turn in scenario.turns[:index]],
        identity, identity, identity if echo is None else echo,
    )


def outcomes(items):
    return {item["id"]: item["outcome"] for item in items}


def test_both_turns_pass(scenario, good_replies):
    assert classify(check(scenario, good_replies[0])) == "PASS"
    assert classify(check(scenario, good_replies[1], 2, previous=[good_replies[0]])) == "PASS"


@pytest.mark.parametrize("period", ["3-5", "3 – 5", "three to five", "**3–5**"])
def test_approval_typography_and_number_variants(scenario, period):
    text = f"GrabMart approval usually takes {period} business days. Payment follows the next scheduled payout."
    assert classify(check(scenario, text)) == "PASS"


@pytest.mark.parametrize("text,failed_id", [
    ("GrabFood approval takes 1–2 business days, then the next regular payout cycle.", "no-grabfood-timing"),
    ("GrabMart approval takes 3–5 business days.", "grabmart-approval-and-payment"),
    ("GrabMart payment takes 3–5 business days. Approval is instant. Next regular payout cycle.", "grabmart-approval-and-payment"),
])
def test_wrong_product_or_incomplete_timing_fails(scenario, text, failed_id):
    items = check(scenario, text)
    assert classify(items) == "FAIL"
    failed = next(item for item in items if item["id"] == failed_id)
    assert failed["outcome"] == "FAIL"
    assert failed["turn"] == 1 and failed["reason"] and failed["evidence"]


@pytest.mark.parametrize("text,failed_ids", [
    ("When was the order cancelled?", {"portal-route", "answer-location-before-order-age"}),
    ("Are you a GrabFood or GrabMart merchant?", {"portal-route", "no-business-line-reask"}),
    ("Open the GrabMerchant app to check the status.", {"portal-route", "no-app-substitution"}),
    ("GrabMerchant Portal > Transactions > Finance > time period and store > Compensation for cancelled orders.", {"portal-route"}),
    ("GrabMerchant Portal > Finance > Transactions > store > Compensation for cancelled orders.", {"portal-route"}),
])
def test_status_location_deviations(scenario, text, failed_ids):
    items = check(scenario, text, 2)
    assert failed_ids <= {item["id"] for item in items if item["outcome"] == "FAIL"}
    assert all(item["reason"] and item["turn"] == 2 for item in items if item["outcome"] == "FAIL")


def test_period_and_store_can_be_in_either_order(scenario, good_replies):
    text = good_replies[1].replace("time period and store", "store and date range")
    assert classify(check(scenario, text, 2)) == "PASS"


def test_order_age_followup_after_complete_answer_is_allowed(scenario, good_replies):
    items = check(scenario, good_replies[1] + " When was the order cancelled?", 2)
    assert outcomes(items)["answer-location-before-order-age"] == "SKIP"
    assert classify(items) == "PASS"


@pytest.mark.parametrize("extra,warning_id", [
    ("Your order was already prepared.", "unsupported-preparation"),
    ("Since you have already prepared the order, it qualifies.", "unsupported-preparation"),
    ("How may I help you today?", "redundant-help-question"),
    ("Hello! Hello again!", "repeated-greeting"),
])
def test_quality_issues_are_warnings(scenario, good_replies, extra, warning_id):
    items = check(scenario, extra + " " + good_replies[0])
    assert outcomes(items)[warning_id] == "WARN"
    assert classify(items) == "PASS_WITH_WARNINGS"


def test_followup_greeting_is_reported(scenario, good_replies):
    items = check(scenario, "Hello! " + good_replies[1], 2, previous=["Hello! " + good_replies[0]])
    assert outcomes(items)["repeated-greeting"] == "WARN"


def test_preparation_claim_supported_by_merchant_is_not_warned(scenario, good_replies):
    items = check(
        scenario, "Your order was already prepared. " + good_replies[0],
        merchants=["I already prepared the order."],
    )
    assert outcomes(items)["unsupported-preparation"] == "SKIP"


def test_identity_mismatch_is_hard_failure(scenario, good_replies):
    items = check(scenario, good_replies[0], echo={"userId": "other-user", "sessionId": "other-session"})
    assert outcomes(items)["identity-continuity"] == "FAIL"


def test_missing_echo_warns_without_claiming_verified_continuity(scenario, good_replies):
    items = check(scenario, good_replies[0], echo={})
    assert outcomes(items)["identity-continuity"] == "WARN"
    assert classify(items) == "PASS_WITH_WARNINGS"


def test_changed_request_identity_is_detected(scenario, good_replies):
    expected = {"userId": "a", "sessionId": "b"}
    actual = {"userId": "a", "sessionId": "changed"}
    items = evaluate(scenario, scenario.turns[0], 1, good_replies[0], [], [], actual, expected, actual)
    assert outcomes(items)["identity-continuity"] == "FAIL"


def test_product_scoped_rule_is_not_applied_to_another_business_line(scenario, good_replies):
    definition = deepcopy(scenario.definition)
    definition["turns"][0]["assertions"].append({
        "id": "food-only", "type": "forbidden", "products": ["GrabFood"],
        "concepts": ["grabmart"], "reason": "Only applicable to a GrabFood scenario.",
    })
    items = check(parse_scenario(definition), good_replies[0])
    assert outcomes(items)["food-only"] == "SKIP"
    assert classify(items) == "PASS"
