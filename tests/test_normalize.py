import pytest

from uc4_runner.normalize import ResponseError, normalize_response, trace_ids


def test_combined_text_and_stack_are_not_rendered_twice():
    raw = {"text": "Hello. Here is the answer.", "outputStack": [
        {"text": "Hello.", "traceId": "trace-a"},
        {"text": "Here is the answer.", "traceId": "trace-a"},
    ]}
    normalized = normalize_response(raw)
    assert normalized.text == "Hello. Here is the answer."
    assert normalized.trace_ids == ["trace-a"]


@pytest.mark.parametrize("parts,expected", [
    (["Approval", "Approval takes", "Approval takes 3–5 business days."], "Approval takes 3–5 business days."),
    (["Approval takes 3–5 business days.", "Payment follows.", "Approval takes 3–5 business days. Payment follows."],
     "Approval takes 3–5 business days. Payment follows."),
    (["Hello!", "Hello!", "Here is the answer."], "Hello!\nHello!\nHere is the answer."),
])
def test_stack_fallback_handles_fragments_without_hiding_repeated_greetings(parts, expected):
    raw = {"outputStack": [{"text": text} for text in parts]}
    assert normalize_response(raw).text == expected
    assert len(raw["outputStack"]) == len(parts)  # Raw evidence was not mutated.


def test_internal_data_and_user_messages_do_not_enter_transcript():
    raw = {"outputStack": [
        {"text": "Merchant echo", "source": "user"},
        {"data": {"internal": "Diagnostics are not user-facing output"}},
        {"text": "Agent answer", "source": "bot"},
    ]}
    assert normalize_response(raw).text == "Agent answer"


def test_combined_text_containing_stream_chunks_and_final_copy_is_deduplicated():
    parts = ["Hello!", "Approval takes 3–5 days.", "Payment follows.", "Approval takes 3–5 days. Payment follows."]
    raw = {"text": " ".join(parts), "outputStack": [{"text": part} for part in parts]}
    normalized = normalize_response(raw)
    assert normalized.text == "Hello!\nApproval takes 3–5 days. Payment follows."
    assert len(raw["outputStack"]) == 4


def test_combined_text_is_preserved_when_stack_cannot_explain_it():
    raw = {"text": "A transformed complete answer.", "outputStack": [
        {"text": "Approval"}, {"text": "Approval takes 3–5 days."},
    ]}
    assert normalize_response(raw).text == "A transformed complete answer."


@pytest.mark.parametrize("raw", [[], None, "string", {"text": 42}, {"outputStack": {}}, {"outputStack": ["bad"]}])
def test_unexpected_shapes_are_rejected(raw):
    with pytest.raises(ResponseError):
        normalize_response(raw)


def test_nested_and_header_trace_ids_are_retained_and_deduplicated():
    raw = {"traceId": "one", "outputStack": [{"data": {"traceIds": ["two", "one"]}}]}
    assert trace_ids(raw, {"x-trace-id": "two", "x-request-id": "request", "traceparent": "parent"}) == [
        "one", "two", "request", "parent"
    ]
