from dataclasses import replace
import json

import httpx
import pytest

from uc4_runner.client import CognigyClient


def test_documented_rest_request_and_api_key_header(config):
    config = replace(config, api_key="dummy-api-secret")

    def handler(request):
        assert request.method == "POST"
        assert request.url.path == "/rest/test/dummy-endpoint-token-9a4b"
        assert request.headers["x-cognigy-endpoint-key"] == config.api_key
        assert request.headers["content-type"] == "application/json"
        assert json.loads(request.content) == {"userId": "u", "sessionId": "s", "text": "hello", "data": {}}
        return httpx.Response(200, json={"text": "Hello", "userId": "u", "sessionId": "s"})

    with CognigyClient(config, httpx.MockTransport(handler)) as client:
        reply = client.send(user_id="u", session_id="s", text="hello")
    assert reply.http_status == 200 and reply.text == "Hello" and reply.error_kind is None
    assert reply.duration_seconds >= 0


@pytest.mark.parametrize("header", ["x-rest-endpoint-key", "x-cognigy-endpoint-key"])
def test_optional_authentication_can_use_either_documented_header(config, header):
    config = replace(config, api_key="dummy-api-secret", api_key_header=header)

    def handler(request):
        assert request.headers[header] == config.api_key
        return httpx.Response(200, json={"text": "ok"})

    with CognigyClient(config, httpx.MockTransport(handler)) as client:
        assert client.send(user_id="u", session_id="s", text="hi").error_kind is None


@pytest.mark.parametrize("response,kind", [
    (httpx.Response(301, headers={"location": "https://elsewhere.invalid"}), "http_error"),
    (httpx.Response(401, json={"error": "unauthorized"}), "http_error"),
    (httpx.Response(429, json={"error": "rate limited"}), "http_error"),
    (httpx.Response(500, text="server failed"), "http_error"),
    (httpx.Response(200, text="not json"), "invalid_json"),
    (httpx.Response(200, text='{"text": "hello", "data": NaN}'), "invalid_json"),
    (httpx.Response(200, json=[]), "unexpected_json"),
    (httpx.Response(200, content=b"null"), "unexpected_json"),
    (httpx.Response(200, json={"text": {"nested": "no"}}), "unexpected_json"),
    (httpx.Response(200, json={"outputStack": "bad"}), "unexpected_json"),
    (httpx.Response(200, json={"text": "   ", "outputStack": []}), "empty_reply"),
    (httpx.Response(200, json={"data": {"card": "non-text-only"}}), "empty_reply"),
    (httpx.Response(204), "invalid_json"),
])
def test_response_errors_do_not_trigger_retries_or_redirects(config, response, kind):
    calls = []

    def handler(request):
        calls.append(request)
        return response

    with CognigyClient(config, httpx.MockTransport(handler)) as client:
        reply = client.send(user_id="u", session_id="s", text="hi")
    assert reply.error_kind == kind
    assert reply.http_status == response.status_code
    assert len(calls) == 1


@pytest.mark.parametrize("error_type,kind", [
    (httpx.ReadTimeout, "timeout"), (httpx.ConnectTimeout, "timeout"),
    (httpx.WriteTimeout, "timeout"), (httpx.ConnectError, "network_error"),
])
def test_ambiguous_failures_are_never_retried_or_logged_with_url(config, error_type, kind):
    calls = []

    def handler(request):
        calls.append(request)
        raise error_type(f"Sensitive URL: {request.url}", request=request)

    with CognigyClient(config, httpx.MockTransport(handler)) as client:
        reply = client.send(user_id="u", session_id="s", text="hi")
    assert len(calls) == 1 and reply.error_kind == kind
    assert reply.http_status is None and reply.error_reason
    assert config.url not in reply.error_reason and "dummy-endpoint-token" not in reply.error_reason
