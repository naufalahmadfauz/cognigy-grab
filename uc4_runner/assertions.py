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

    def find(concept: str, source: str = normalized, start: int = 0):
        matches = [
            match for pattern in scenario.concepts[concept]
            if (match := re.compile(pattern, re.I | re.M).search(source, start))
        ]
        return min(matches, key=lambda match: (match.start(), match.end())) if matches else None

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
            missing = [name for name in rule["concepts"] if not find(name)]
            passed = not missing
            detail = "Missing concepts: " + ", ".join(missing) if missing else "All required concepts found."
        elif kind == "forbidden":
            conditions = (
                ("unless_merchant_concepts", matching_text("\n".join(merchant_history))),
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
            else:
                detail = "No forbidden concepts found."
        elif kind == "ordered":
            cursor = 0
            for step in rule["steps"]:
                names = [step] if isinstance(step, str) else step
                matches = [find(name, start=cursor) for name in names]
                if any(match is None for match in matches):
                    passed = False
                    detail = "Missing or out-of-order navigation step: " + ", ".join(names)
                    break
                cursor = max(match.end() for match in matches)
            if passed:
                detail = "Navigation steps appear in the configured order."
        elif kind == "no_repeated_greeting":
            # Count unique spans so overlapping regex alternatives don't double-count.
            spans = {
                (match.start(), match.end())
                for name in rule["concepts"] for pattern in scenario.concepts[name]
                for match in re.finditer(pattern, normalized, re.I | re.M)
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
