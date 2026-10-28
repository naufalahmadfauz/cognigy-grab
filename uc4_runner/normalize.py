"""Normalize only documented user-facing fields; retain diagnostic data separately."""

from dataclasses import dataclass
import re
import unicodedata


class ResponseError(ValueError):
    pass


@dataclass
class NormalizedResponse:
    text: str
    trace_ids: list[str]
    echoed_identity: dict
    notes: list[str]


def matching_text(text: str) -> str:
    """Ignore presentation differences, but preserve sentence/line boundaries."""
    text = unicodedata.normalize("NFKC", text)
    text = text.translate(str.maketrans({"–": "-", "—": "-", "−": "-", "’": "'", "‘": "'"}))
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"[^\S\n]+", " ", text).strip()


def trace_ids(raw: object, headers: dict | None = None) -> list[str]:
    found = []

    def visit(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key.lower().replace("_", "") in {"traceid", "traceids"}:
                    candidates = item if isinstance(item, list) else [item]
                    found.extend(v for v in candidates if isinstance(v, str) and v)
                else:
                    visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(raw)
    for key, value in (headers or {}).items():
        if key.lower() in {"x-trace-id", "x-request-id", "traceparent"} and value:
            found.append(value)
    return list(dict.fromkeys(found))


def _stack_text(parts: list[str]) -> tuple[str, list[str]]:
    """Collapse cumulative snapshots/final copies, not genuine repeated utterances.

    Unmarked identical messages are intentionally preserved: deleting all duplicates
    would hide repeated greetings. Raw evidence preserves every original fragment.
    """
    result = []
    notes = []
    for part in parts:
        if result and part != result[-1] and part.startswith(result[-1]):
            result[-1] = part
            notes.append("Collapsed adjacent cumulative text snapshots.")
        else:
            # A streamed answer may follow a separate greeting. Collapse only the
            # matching suffix, leaving earlier independent outputs intact.
            suffix_start = next((
                start for start in range(len(result) - 1)
                if any(
                    matching_text(part) == matching_text(separator.join(result[start:]))
                    for separator in ("", " ", "\n")
                )
            ), None)
            if suffix_start is not None:
                result[suffix_start:] = [part]
                notes.append("Collapsed a final copy of preceding text fragments.")
            else:
                result.append(part)
    return "\n".join(result), list(dict.fromkeys(notes))


def normalize_response(raw: object, headers: dict | None = None) -> NormalizedResponse:
    if not isinstance(raw, dict):
        raise ResponseError("Expected a Cognigy JSON object.")
    top = raw.get("text")
    if top is not None and not isinstance(top, str):
        raise ResponseError("Cognigy text must be a string or null.")
    stack = raw.get("outputStack", [])
    if not isinstance(stack, list):
        raise ResponseError("Cognigy outputStack must be an array.")
    parts = []
    for item in stack:
        if not isinstance(item, dict) or (item.get("text") is not None and not isinstance(item["text"], str)):
            raise ResponseError("Cognigy outputStack entries must be objects with string or null text.")
        if item.get("source", "bot") == "bot" and item.get("text", ""):
            if item["text"].strip():
                parts.append(item["text"].strip())
    # Cognigy already concatenates normal outputs in top-level text. Never append
    # the stack to it, which would render the same reply twice.
    if top and top.strip():
        text, notes = top.strip(), ["Used Cognigy's combined top-level text."]
        stack_text, stack_notes = _stack_text(parts)
        if stack_notes and any(
            matching_text(top) == matching_text(separator.join(parts))
            for separator in ("", " ", "\n")
        ):
            # Some deployments concatenate both stream chunks and their final copy
            # into text. Rebuild only when the stack exactly explains that text.
            text = stack_text
            notes = ["Combined text included redundant streaming fragments.", *stack_notes]
    else:
        text, notes = _stack_text(parts)
        notes.insert(0, "Used outputStack because combined text was absent or empty.")
    identity = {key: raw[key] for key in ("userId", "sessionId") if key in raw}
    return NormalizedResponse(text, trace_ids(raw, headers), identity, notes)
