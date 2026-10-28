"""One POST per turn. This module contains no business-behavior rules."""

from dataclasses import dataclass, field
from time import perf_counter

import httpx

from .config import Config, endpoint_url
from .normalize import ResponseError, normalize_response, trace_ids


def _reject_nonfinite(value: str):
    raise ValueError("Non-finite numbers are not valid JSON.")


@dataclass
class Reply:
    http_status: int | None = None
    duration_seconds: float = 0
    raw: object = None
    raw_body: str | None = None
    text: str = ""
    trace_ids: list[str] = field(default_factory=list)
    echoed_identity: dict = field(default_factory=dict)
    normalization_notes: list[str] = field(default_factory=list)
    error_kind: str | None = None
    error_reason: str | None = None


class CognigyClient:
    def __init__(self, config: Config, transport: httpx.BaseTransport | None = None):
        self.url = endpoint_url(config.url, config.test_mode)
        headers = {"Accept": "application/json"}
        if config.api_key:
            headers[config.api_key_header] = config.api_key
        self.http = httpx.Client(
            headers=headers,
            timeout=config.timeout,
            transport=transport if transport is not None else httpx.HTTPTransport(retries=0),
            follow_redirects=False,
            trust_env=False,
        )

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.http.close()

    def send(self, *, user_id: str, session_id: str, text: str) -> Reply:
        reply = Reply()
        start = perf_counter()
        try:
            response = self.http.post(
                self.url, json={"userId": user_id, "sessionId": session_id, "text": text, "data": {}}
            )
            reply.http_status = response.status_code
            try:
                reply.raw = response.json(parse_constant=_reject_nonfinite)
            except (ValueError, UnicodeError, RecursionError):
                reply.raw_body = response.text
            reply.trace_ids = trace_ids(reply.raw, dict(response.headers))
            if not 200 <= response.status_code < 300:
                reply.error_kind = "http_error"
                reply.error_reason = f"Endpoint returned HTTP {response.status_code}; request was not retried."
            elif reply.raw_body is not None:
                reply.error_kind = "invalid_json"
                reply.error_reason = "Endpoint returned a non-JSON response."
            else:
                try:
                    normalized = normalize_response(reply.raw, dict(response.headers))
                    reply.text = normalized.text
                    reply.trace_ids = normalized.trace_ids
                    reply.echoed_identity = normalized.echoed_identity
                    reply.normalization_notes = normalized.notes
                    if not reply.text:
                        reply.error_kind = "empty_reply"
                        reply.error_reason = "Endpoint returned no user-facing text."
                except ResponseError as error:
                    reply.error_kind = "unexpected_json"
                    reply.error_reason = str(error)
        except httpx.TimeoutException:
            reply.error_kind = "timeout"
            reply.error_reason = (
                "Request timed out; processing may have occurred. No retry was attempted; "
                "remaining turns in this session are skipped."
            )
        except httpx.RequestError:
            # HTTPX exception strings can contain the complete credential-bearing URL.
            reply.error_kind = "network_error"
            reply.error_reason = "HTTP transport failed; processing may have occurred. Request was not retried."
        finally:
            reply.duration_seconds = round(perf_counter() - start, 6)
        return reply
