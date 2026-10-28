from dataclasses import replace
import json
from urllib.parse import quote

import httpx

from conftest import cognigy_response
from uc4_runner.redact import Redactor
from uc4_runner.runner import execute_batch


def test_credentials_and_personal_information_never_reach_any_artifact(tmp_path, scenario, config, good_replies):
    config = replace(config, api_key="dummy-secret-key-765", retain_raw=True, redact_values=("Jane Private", "private-order-89"))
    sensitive = [config.url, "dummy-endpoint-token-9a4b", config.api_key, "merchant@example.invalid",
                 "+60123456789", "Jane Private", "private-order-89", "unknown-secret-abc", "foreign-person-123"]

    def handler(request):
        data = json.loads(request.content)
        index = 0 if data["text"] == scenario.turns[0]["merchant"] else 1
        text = good_replies[index] + " " + " ".join(sensitive[:7])
        return cognigy_response(request, text, data={
            "nested": [{"Authorization": "unknown-secret-abc", "api_key": config.api_key,
                        "email": sensitive[3], "phoneNumber": sensitive[4], "userId": sensitive[-1]}],
            "echo": quote(config.api_key), "requestUrl": str(request.url),
        })

    directory, batch = execute_batch(scenario, config, tmp_path / "reports", repeat=1, transport=httpx.MockTransport(handler))
    for path in directory.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for value in sensitive:
                assert value not in text, f"Sensitive value escaped into {path.name}"
    turn = batch["runs"][0]["turns"][0]
    assert turn["traceIds"] == ["trace-fixture-001"]
    assert turn["rawResponse"]["outputStack"]
    assert batch["runs"][0]["sessionId"] == turn["sessionId"]


def test_invalid_json_body_is_also_redacted(tmp_path, scenario, config):
    config = replace(config, api_key="dummy-secret-999", retain_raw=True)
    transport = httpx.MockTransport(lambda request: httpx.Response(
        502, text=f"<html>{config.url} {config.api_key} merchant@example.invalid</html>"
    ))
    directory, batch = execute_batch(scenario, config, tmp_path / "reports", repeat=1, transport=transport)
    assert batch["runs"][0]["turns"][0]["rawBody"]
    all_evidence = "\n".join(path.read_text(encoding="utf-8") for path in directory.rglob("*") if path.is_file())
    assert config.url not in all_evidence and config.api_key not in all_evidence
    assert "merchant@example.invalid" not in all_evidence


def test_config_repr_and_public_metadata_exclude_secrets(config):
    config = replace(config, api_key="dummy-api-key-123", redact_values=("private-name",))
    text = repr(config) + json.dumps(config.public())
    assert config.url not in text and config.api_key not in text and "private-name" not in text


def test_secret_keys_and_values_are_redacted_recursively(config):
    config = replace(config, api_key="test-api-secret", redact_values=("private-person",))
    redactor = Redactor(config, {"synthetic-session"})
    safe = redactor.clean({
        "test-api-secret": "echo test-api-secret",
        "nested": [{"token": "unknown-secret", "name": "Unknown Person", "sessionId": "synthetic-session"}],
        "traceIds": ["trace-123456789012", "test-api-secret"],
    })
    serialized = json.dumps(safe)
    assert "test-api-secret" not in serialized and "unknown-secret" not in serialized
    assert "Unknown Person" not in serialized
    assert "synthetic-session" in serialized and "trace-123456789012" in serialized


def test_unstructured_authorization_scheme_and_value_are_both_redacted(config):
    redactor = Redactor(config)
    assert "unknown-bearer-secret" not in redactor.text("Authorization: Bearer unknown-bearer-secret")
