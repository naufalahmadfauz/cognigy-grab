"""Behavioral regressions from the first live batch; these checks run offline."""

from copy import deepcopy

import pytest

from test_assertions import check, outcomes
from uc4_runner.assertions import classify
from uc4_runner.scenario import parse_scenario


PREPARATION_CLAIM = (
    "I understand that you're contacting us about an order that was cancelled "
    "after it had already been prepared."
)


def test_established_grabmart_context_does_not_require_product_echo(scenario):
    text = (
        "Compensation for a cancelled order is usually approved within three to five business days, "
        "and it is then paid in your next payout cycle."
    )
    assert outcomes(check(scenario, text))["grabmart-approval-and-payment"] == "PASS"


def test_app_portal_clarification_is_not_wrong_navigation(scenario):
    text = "Are you currently on the GrabMerchant app, or on the GrabMerchant portal?"
    result = outcomes(check(scenario, text, 2))
    assert result["no-app-substitution"] == "PASS"
    assert result["portal-route"] == "FAIL"


def test_relative_clause_preparation_claim_is_warned(scenario):
    assert outcomes(check(scenario, PREPARATION_CLAIM))["unsupported-preparation"] == "WARN"


def test_complete_route_does_not_hide_unnecessary_age_question(scenario, good_replies):
    text = good_replies[1] + " When was the order cancelled—today, yesterday, or two days ago?"
    result = outcomes(check(scenario, text, 2))
    assert result["portal-route"] == "PASS"
    assert result["answer-location-before-order-age"] == "WARN"


def test_merchant_context_is_allowlisted_not_an_agent_answer(scenario):
    items = check(scenario, "Payment follows the next payout cycle.", merchants=[
        "I'm a GrabMart merchant. Does approval take three to five business days?"
    ])
    assert outcomes(items)["grabmart-approval-and-payment"] == "FAIL"


def test_agent_claim_is_not_merchant_product_context(scenario, good_replies):
    items = check(scenario, good_replies[0].replace("For GrabMart, ", ""),
                  merchants=["I manage a store."], previous=["You're a GrabMart merchant."])
    assert outcomes(items)["grabmart-approval-and-payment"] == "FAIL"


def test_negated_product_identity_does_not_supply_context(scenario, good_replies):
    items = check(scenario, good_replies[0].replace("For GrabMart, ", ""), merchants=["I'm not a GrabMart merchant."])
    assert outcomes(items)["grabmart-approval-and-payment"] == "FAIL"


@pytest.mark.parametrize("text", [
    "Approval takes 1–2 business days, paid in the next payout cycle.",
    "For GrabFood, approval takes one to two working days and the next regular payout cycle.",
])
def test_wrong_food_timing_still_fails_in_grabmart_context(scenario, text):
    assert outcomes(check(scenario, text))["no-grabfood-timing"] == "FAIL"


def test_negated_wrong_timing_is_not_a_recommendation(scenario, good_replies):
    items = check(scenario, good_replies[0] + " Not 1–2 business days.")
    assert classify(items) == "PASS"


@pytest.mark.parametrize("text", [
    "Approval does not take three to five business days. Payment follows the next payout cycle.",
    "Approval takes 3–5 business days. Payment does not follow the next payout cycle.",
])
def test_negated_expected_guidance_cannot_pass(scenario, text):
    assert outcomes(check(scenario, text))["grabmart-approval-and-payment"] == "FAIL"


@pytest.mark.parametrize("text", [
    "Are you using the GrabMerchant App or the Portal?",
    "Do you currently use the GrabMerchant App or Portal?",
    "Did you open the GrabMerchant app or Portal?",
    "Which interface are you using: the GrabMerchant App or the Portal?",
    "Do not use the GrabMerchant App to check this status. Use the Portal.",
    "Don't open the GrabMerchant app for this. Use the Portal.",
    "You should not check compensation through the GrabMerchant app.",
    "Use the Portal, not the GrabMerchant App.",
])
def test_clarifications_and_negated_app_instructions_are_not_wrong_routes(scenario, text):
    assert outcomes(check(scenario, text, 2))["no-app-substitution"] == "PASS"


@pytest.mark.parametrize("text", [
    "Open the GrabMerchant app to check the status.",
    "For GrabMart, use the GrabMerchant App to find compensation.",
    "You can check compensation status in the GrabMerchant App.",
    "Please view the compensation status through the GrabFood app.",
    "Could you open the GrabMerchant app to check the status?",
    "The status can be checked in the GrabMerchant app.",
    "GrabMerchant App > Finance > Transactions.",
])
def test_actual_app_instructions_fail_even_alongside_correct_portal_route(scenario, good_replies, text):
    assert outcomes(check(scenario, text + " " + good_replies[1], 2))["no-app-substitution"] == "FAIL"


def test_a_negated_app_instruction_does_not_mask_a_later_positive_instruction(scenario):
    text = "Do not use the GrabMerchant app. Actually, open the GrabMerchant app to check compensation."
    assert outcomes(check(scenario, text, 2))["no-app-substitution"] == "FAIL"


@pytest.mark.parametrize("text", [
    PREPARATION_CLAIM,
    "Your order had already been prepared before it was cancelled.",
    "The order was cancelled after it was prepared.",
    "An order cancelled after preparation is what you're contacting us about.",
    "Since you've already prepared the order, I understand your concern.",
    "The order was already ready before cancellation.",
])
def test_preparation_paraphrases_are_warned(scenario, text):
    assert outcomes(check(scenario, text))["unsupported-preparation"] == "WARN"


@pytest.mark.parametrize("text", [
    "The order was not prepared when it was cancelled.",
    "If your order was already prepared, you may qualify.",
    "I don't know whether the order was already prepared.",
    "We cannot assume the order was already prepared.",
    "Was your order prepared before cancellation?",
])
def test_negations_conditionals_and_questions_are_not_preparation_claims(scenario, text):
    assert outcomes(check(scenario, text))["unsupported-preparation"] == "PASS"


def test_conditional_preparation_mention_does_not_hide_a_separate_claim(scenario):
    text = "If your order was prepared, you may qualify. Your order was already prepared."
    assert outcomes(check(scenario, text))["unsupported-preparation"] == "WARN"


@pytest.mark.parametrize("merchant", [
    "I already prepared the order.", "I'd prepared the order before it was cancelled.",
    "We have already prepared the order.", "The order had already been prepared.",
    "It was already prepared before cancellation.",
])
def test_earlier_merchant_preparation_supports_the_claim(scenario, merchant):
    items = check(scenario, PREPARATION_CLAIM, 2, merchants=[merchant, scenario.turns[1]["merchant"]])
    assert outcomes(items)["unsupported-preparation"] == "SKIP"


@pytest.mark.parametrize("merchant", [
    "I had not prepared the order.", "The order was not prepared.",
    "If I prepared the order, would I qualify?", "I never said the order was prepared.",
    "I don't know whether the order was prepared.", "Was the order prepared?",
])
def test_nonaffirmative_merchant_messages_do_not_excuse_a_claim(scenario, merchant):
    assert outcomes(check(scenario, PREPARATION_CLAIM, merchants=[merchant]))["unsupported-preparation"] == "WARN"


@pytest.mark.parametrize("question", [
    "When was the order cancelled?", "How long ago was it cancelled?",
    "What date was the order cancelled?", "Please tell me when the order was cancelled.",
    "Could you share the cancellation date?",
])
def test_age_question_severity_depends_on_guidance(scenario, good_replies, question):
    assert outcomes(check(scenario, good_replies[1] + " " + question, 2))["answer-location-before-order-age"] == "WARN"
    missing = outcomes(check(scenario, question, 2))
    assert missing["answer-location-before-order-age"] == "FAIL" and missing["portal-route"] == "FAIL"


@pytest.mark.parametrize("extra", [
    "The date filter covers when the order was cancelled.",
    "You do not need to tell me when the order was cancelled.",
    "No need to share the cancellation date.",
])
def test_age_statements_and_negated_requests_are_not_questions(scenario, good_replies, extra):
    assert classify(check(scenario, good_replies[1] + " " + extra, 2)) == "PASS"


def test_age_routing_is_allowed_when_the_scenario_requires_it(scenario):
    data = deepcopy(scenario.definition)
    data["turns"][1]["merchant"] = "Can you help determine eligibility based on cancellation age?"
    data["turns"][1]["assertions"] = [{
        "id": "ask-needed-age", "type": "required", "concepts": ["order_age_question"],
        "reason": "This scenario needs cancellation age before choosing an eligibility route.",
    }]
    configured = parse_scenario(data)
    assert classify(check(configured, "When was the order cancelled?", 2)) == "PASS"
