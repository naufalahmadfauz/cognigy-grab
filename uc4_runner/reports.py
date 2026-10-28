"""Atomic, redacted evidence files and explicit reliability denominators."""

from collections import Counter
import html
import json
from pathlib import Path

from .redact import Redactor


OUTCOMES = ("PASS", "PASS_WITH_WARNINGS", "FAIL", "ERROR")


def _rate(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 6) if denominator else None


def metrics(runs: list[dict]) -> dict:
    executed = [run for run in runs if run["executionStatus"] == "COMPLETED"]
    complete = [run for run in executed if run["outcome"] != "ERROR"]
    turns = [turn for run in executed for turn in run["turns"]]
    attempted = [turn for turn in turns if turn["executionStatus"] == "EXECUTED"]
    usable = [turn for turn in attempted if not turn["error"]]
    http_ok = sum(200 <= (turn["httpStatus"] or 0) < 300 for turn in attempted)
    counts = Counter(run["outcome"] for run in executed)
    passing = counts["PASS"] + counts["PASS_WITH_WARNINGS"]
    return {
        "requestedRuns": len(runs), "executedRuns": len(executed),
        "plannedRuns": len(runs) - len(executed),
        "outcomes": {outcome: counts[outcome] for outcome in OUTCOMES},
        "transport": {
            "attemptedTurns": len(attempted),
            "httpSuccessfulTurns": http_ok, "httpSuccessRate": _rate(http_ok, len(attempted)),
            "usableReplyTurns": len(usable), "usableReplyRate": _rate(len(usable), len(attempted)),
            "errorTurns": len(attempted) - len(usable),
            "skippedTurns": sum(turn["executionStatus"] == "SKIPPED" for turn in turns),
            "completeRuns": len(complete), "completeRunRate": _rate(len(complete), len(executed)),
        },
        "behavior": {
            "evaluatedRuns": len(complete), "excludedErrorRuns": counts["ERROR"],
            "passingRuns": passing, "strictPassingRuns": counts["PASS"], "failedRuns": counts["FAIL"],
            "passRate": _rate(passing, len(complete)),
            "strictPassRate": _rate(counts["PASS"], len(complete)),
            "endToEndPassRate": _rate(passing, len(executed)),
            "evaluatedTurns": len(usable),
            "observedHardFailures": sum(
                assertion["outcome"] == "FAIL" and assertion["category"] != "transport"
                for turn in turns for assertion in turn["assertions"]
            ),
        },
    }


def defects(runs: list[dict]) -> list[dict]:
    collected = {}
    for run in runs:
        for turn in run["turns"]:
            for assertion in turn["assertions"]:
                if assertion["outcome"] not in {"FAIL", "WARN"}:
                    continue
                key = (assertion["id"], turn["turnIndex"], assertion["outcome"])
                entry = collected.setdefault(key, {
                    "assertionId": assertion["id"], "turn": turn["turnIndex"],
                    "category": assertion["category"], "outcome": assertion["outcome"],
                    "occurrences": 0, "runIndexes": [], "exampleReason": assertion["reason"],
                })
                entry["occurrences"] += 1
                entry["runIndexes"].append(run["runIndex"])
    return sorted(collected.values(), key=lambda item: (-item["occurrences"], item["assertionId"], item["turn"]))


def _quote(text: str) -> str:
    return "\n".join("> " + html.escape(line) for line in (text or "(no reply)").splitlines())


def transcript(run: dict) -> str:
    lines = [
        f"# Run {run['runIndex']:03d}: {run['outcome'] or 'PLANNED — NOT EXECUTED'}",
        "", f"- Run ID: `{run['runId']}`", f"- User ID: `{run['userId']}`",
        f"- Session ID: `{run['sessionId']}`", f"- Started: {run['startedAt'] or 'not started'}", "",
    ]
    for turn in run["turns"]:
        lines.extend([
            f"## Turn {turn['turnIndex']} — {turn['executionStatus']}", "",
            "**Merchant**", _quote(turn["merchantInput"]), "", "**Agent**",
            _quote(turn["agentText"]), "",
            f"HTTP: {turn['httpStatus']}; duration: {turn['durationSeconds']} seconds",
            "", "Trace IDs: " + (", ".join(turn["traceIds"]) or "not supplied"), "",
        ])
        for assertion in turn["assertions"]:
            lines.append(f"- {assertion['outcome']} `{assertion['id']}`: {html.escape(assertion['reason'])}")
        lines.append("")
    return "\n".join(lines) + "\n"


def summary(batch: dict) -> str:
    def percent(value):
        return f"{value:.1%}" if value is not None else "not evaluated"

    stats = batch["metrics"]
    transport, behavior = stats["transport"], stats["behavior"]
    lines = [
        f"# UC4 batch {batch['batchId']}", "",
        f"Mode: **{batch['mode']}**; runner {batch['runnerVersion']}; scenario "
        f"**{batch['scenario']['id']} v{batch['scenario']['version']}**.",
        f"Scenario SHA-256: `{batch['scenario']['sha256']}`", "",
        "## Reliability", "",
        f"- Complete conversations: **{transport['completeRuns']}/{stats['executedRuns']}** "
        f"({percent(transport['completeRunRate'])}).",
        f"- HTTP 2xx: **{transport['httpSuccessfulTurns']}/{transport['attemptedTurns']}** "
        f"({percent(transport['httpSuccessRate'])}).",
        f"- Usable replies: **{transport['usableReplyTurns']}/{transport['attemptedTurns']}** "
        f"({percent(transport['usableReplyRate'])}); skipped turns: {transport['skippedTurns']}.",
        f"- Behavioral pass rate (warnings accepted): **{behavior['passingRuns']}/{behavior['evaluatedRuns']}** "
        f"({percent(behavior['passRate'])}); excluded ERROR runs: {behavior['excludedErrorRuns']}.",
        f"- Strict behavioral pass rate: {percent(behavior['strictPassRate'])}.",
        f"- End-to-end pass rate across executed repetitions: {percent(behavior['endToEndPassRate'])}.", "",
        "## Runs", "", "| Run | Outcome | Session ID | Evidence |",
        "|---|---|---|---|",
    ]
    for run in batch["runs"]:
        index = run["runIndex"]
        lines.append(
            f"| {index} | {run['outcome'] or 'PLANNED'} | `{run['sessionId']}` | "
            f"[JSON](runs/run-{index:03d}.json), [transcript](transcripts/run-{index:03d}.md) |"
        )
    lines.extend(["", "## Recurring defects and warnings", ""])
    if not batch["defects"]:
        lines.append("None observed." if batch["mode"] == "EXECUTED" else "Not evaluated in dry-run.")
    for item in batch["defects"]:
        lines.append(
            f"- **{item['outcome']}** `{item['assertionId']}`, turn {item['turn']}: "
            f"{item['occurrences']} occurrence(s), runs {', '.join(map(str, item['runIndexes']))}. "
            f"{html.escape(item['exampleReason'])}"
        )
    lines.extend(["", "## Supporting responses and trace IDs", ""])
    for run in batch["runs"]:
        lines.extend([f"### Run {run['runIndex']:03d} — {run['outcome'] or 'PLANNED'}", ""])
        for turn in run["turns"]:
            lines.append(f"- Turn {turn['turnIndex']} traces: {', '.join(turn['traceIds']) or 'not supplied'}")
            problems = [item for item in turn["assertions"] if item["outcome"] in {"FAIL", "WARN"}]
            if problems:
                lines.extend(["", _quote(turn["agentText"]), ""])
                for item in problems:
                    lines.append(f"- {item['outcome']} `{item['id']}`: {html.escape(item['reason'])}")
        lines.append("")
    lines.extend([
        "## Configuration", "", "```json",
        json.dumps(batch["configuration"], indent=2, ensure_ascii=False), "```", "",
        "Raw evidence is redacted and retained only when configured. Review it for residual sensitive data.",
    ])
    return "\n".join(lines) + "\n"


class ReportWriter:
    def __init__(self, directory: Path, redactor: Redactor):
        self.directory = directory
        self.redactor = redactor
        directory.mkdir(parents=True, exist_ok=False)

    def _write(self, relative: str, text: str):
        path = self.directory / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(text, encoding="utf-8")
        temporary.replace(path)

    def write_json(self, relative: str, value):
        self._write(relative, json.dumps(self.redactor.clean(value), indent=2, ensure_ascii=False, allow_nan=False) + "\n")

    def write_run(self, run: dict):
        safe = self.redactor.clean(run)
        self.write_json(f"runs/run-{run['runIndex']:03d}.json", safe)
        self._write(f"transcripts/run-{run['runIndex']:03d}.md", transcript(safe))

    def finish(self, batch: dict):
        safe = self.redactor.clean(batch)
        self.write_json("aggregate.json", safe)
        conversations = []
        for run in safe["runs"]:
            conversations.append({
                "runId": run["runId"], "runIndex": run["runIndex"],
                "userId": run["userId"], "sessionId": run["sessionId"], "outcome": run["outcome"],
                "turns": [{key: turn[key] for key in (
                    "turnIndex", "merchantInput", "agentText", "executionStatus", "traceIds", "outcome"
                )} for turn in run["turns"]],
            })
        self.write_json("transcripts.json", {"batchId": batch["batchId"], "mode": batch["mode"], "conversations": conversations})
        self._write("summary.md", summary(safe))
        self.write_json("manifest.json", {
            "batchId": batch["batchId"], "executionStatus": "COMPLETE", "mode": batch["mode"],
            "requestedRuns": len(batch["runs"]), "createdAt": batch["createdAt"], "completedAt": batch["completedAt"],
        })
