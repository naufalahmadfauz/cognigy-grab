"""Deterministic assertions over normalized replies, configured entirely by scenarios."""

import re

from .normalize import matching_text
from .scenario import Scenario


def result(rule: dict, turn: int, passed: bool | None, reason: str, evidence: str = "") -> dict:
    severity = rule.get("severity", "fail")
    outcome = "SKIP" if passed is None else "PASS" if passed else "WARN" if severity == "warning" else "FAIL"
    return {
        "id": rule["id"], "type": rule["type"], "turn": turn,
        "category": "continuity" if rule["type"] == "session_continuity" else "behavior",
        "severity": severity, "outcome": outcome, "reason": reason, "evidence": evidence,
    }


def skipped_assertions(scenario: Scenario, turn: dict, index: int, reason: str) -> list[dict]:
    return [result(rule, index, None, reason) for rule in scenario.rules_for(turn)]


def evaluate(
    scenario: Scenario, turn: dict, index: int, text: str,
    previous_replies: list[str], merchant_history: list[str],
    requested_identity: dict, expected_identity: dict, echoed_identity: dict,
) -> list[dict]:
    normalized = matching_text(text)
    merchant_text = matching_text("\n".join(merchant_history))

    def matches(concept: str, source: str = normalized, start: int = 0):
        # Exclude only overlapping evidence spans, not the entire response. A
        # negated mention must not hide a separate affirmative claim later on.
        excluded = [
            match.span() for pattern in scenario.concept_exclusions.get(concept, [])
            for match in re.finditer(pattern, source, re.I | re.M)
        ]
        return [
            match for pattern in scenario.concepts[concept]
            for match in re.compile(pattern, re.I | re.M).finditer(source, start)
            if not any(match.start() < end and begin < match.end() for begin, end in excluded)
        ]

    def find(concept: str, source: str = normalized, start: int = 0):
        return min(matches(concept, source, start), key=lambda match: (match.start(), match.end()), default=None)

    results = []
    for rule in scenario.rules_for(turn):
        if scenario.product not in rule.get("products", [scenario.product]):
            results.append(result(rule, index, None, "Rule applies to a different business line."))
            continue
        kind = rule["type"]
        evidence = ""
        detail = ""
        passed = True
        if kind == "session_continuity":
            if requested_identity != expected_identity:
                passed, detail = False, "Request identity changed within this run."
            elif any(echoed_identity[key] != value for key, value in expected_identity.items() if key in echoed_identity):
                passed, detail = False, "Response userId or sessionId differs from the run's identity."
            elif any(key not in echoed_identity for key in expected_identity):
                item = result(rule, index, True, "Request identity is stable; response did not echo both identity fields.")
                item.update(outcome="WARN", severity="warning")
                results.append(item)
                continue
            else:
                detail = "Request and echoed user/session identities match this run."
        elif kind == "required":
            missing = []
            from_context = []
            for name in rule["concepts"]:
                if find(name):
                    continue
                if name in rule.get("allow_merchant_context", []) and find(name, merchant_text):
                    from_context.append(name)
                else:
                    missing.append(name)
            passed = not missing
            detail = "Missing concepts: " + ", ".join(missing) if missing else "All required concepts found."
            if from_context:
                detail += " Merchant context supplied: " + ", ".join(from_context) + "."
        elif kind == "forbidden":
            conditions = (
                ("unless_merchant_concepts", merchant_text),
                ("unless_response_concepts", normalized),
            )
            if any(key in rule and all(find(name, source) for name in rule[key]) for key, source in conditions):
                results.append(result(rule, index, None, "Configured exception condition was satisfied."))
                continue
            found = [(name, find(name)) for name in rule["concepts"] if find(name)]
            passed = not found
            if found:
                detail = "Forbidden concepts: " + ", ".join(name for name, _ in found)
                evidence = "; ".join(match.group() for _, match in found)
                if "warn_if_response_concepts" in rule and all(find(name) for name in rule["warn_if_response_concepts"]):
                    rule = {**rule, "severity": "warning"}
                    detail += ". Configured guidance concepts are present; deviation is a warning."
            else:
                detail = "No forbidden concepts found."
        elif kind == "ordered":
            cursor = 0
            for step in rule["steps"]:
                names = [step] if isinstance(step, str) else step
                step_matches = [find(name, start=cursor) for name in names]
                if any(match is None for match in step_matches):
                    passed = False
                    detail = "Missing or out-of-order navigation step: " + ", ".join(names)
                    break
                cursor = max(match.end() for match in step_matches)
            if passed:
                detail = "Navigation steps appear in the configured order."
        elif kind == "no_repeated_greeting":
            # Count unique spans so overlapping regex alternatives don't double-count.
            spans = {
                (match.start(), match.end())
                for name in rule["concepts"] for match in matches(name)
            }
            previous_greeting = any(
                find(name, matching_text(previous))
                for previous in previous_replies for name in rule["concepts"]
            )
            passed = not (len(spans) > 1 or (spans and (index > 1 or previous_greeting)))
            detail = "Unexpected greeting after conversation began or multiple greetings in one reply." if not passed else "No unexpected repeated greeting."
        results.append(result(
            rule, index, passed,
            f"{rule['reason']} {detail}" if not passed else detail,
            evidence or (text if not passed else ""),
        ))
    return results


def classify(assertions: list[dict], *, transport_error: bool = False) -> str:
    if transport_error:
        return "ERROR"
    if any(item["outcome"] == "FAIL" for item in assertions):
        return "FAIL"
    if any(item["outcome"] == "WARN" for item in assertions):
        return "PASS_WITH_WARNINGS"
    return "PASS"


def evaluate_run(scenario: Scenario, run: dict) -> None:
    """Grade captured turns in place, shared by REST execution and offline regrading.

    Only assertion results and outcomes change. Captured text, raw responses,
    identities, timestamps, HTTP status and transport errors remain evidence.
    """
    identity = {key: run[key] for key in ("userId", "sessionId")}
    previous_replies = []
    merchants = []
    for definition, turn in zip(scenario.turns, run["turns"], strict=True):
        index = turn["turnIndex"]
        if turn["executionStatus"] != "EXECUTED":
            reason = (
                "Dry-run plan; response not evaluated." if turn["executionStatus"] == "PLANNED"
                else "Earlier transport/protocol error left session state uncertain."
            )
            turn["assertions"] = skipped_assertions(scenario, definition, index, reason)
            turn["outcome"] = None
            continue
        error = turn["error"]
        transport_check = {
            "id": "transport.usable-reply", "type": "transport", "category": "transport",
            "turn": index, "severity": "fail", "outcome": "FAIL" if error else "PASS",
            "reason": error["reason"] if error else "HTTP 2xx with a supported, nonempty text reply.", "evidence": "",
        }
        merchants.append(turn["merchantInput"])
        if error:
            assertions = skipped_assertions(scenario, definition, index, "No usable reply; behavior not evaluated.")
        else:
            requested = {key: turn[key] for key in identity}
            assertions = evaluate(
                scenario, definition, index, turn["agentText"], previous_replies, merchants,
                requested, identity, turn["echoedIdentity"],
            )
            previous_replies.append(turn["agentText"])
        turn["assertions"] = [transport_check, *assertions]
        turn["outcome"] = classify(turn["assertions"], transport_error=bool(error))
    run["outcome"] = classify(
        [assertion for turn in run["turns"] for assertion in turn["assertions"]],
        transport_error=any(turn["error"] for turn in run["turns"]),
    ) if run["executionStatus"] == "COMPLETED" else None
