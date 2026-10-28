"""Environment configuration. Endpoint credentials never enter report metadata."""

from dataclasses import dataclass, field
import json
import math
import os
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from dotenv import load_dotenv


class ConfigError(ValueError):
    pass


def _boolean(name: str, default: bool) -> bool:
    value = os.getenv(name, str(default)).strip().lower()
    if value not in {"true", "false"}:
        raise ConfigError(f"{name} must be true or false.")
    return value == "true"


def _number(name: str, default: float, *, positive: bool = False) -> float:
    try:
        value = float(os.getenv(name, str(default)))
    except ValueError:
        raise ConfigError(f"{name} must be a number.") from None
    if not math.isfinite(value) or value < 0 or (positive and value == 0):
        raise ConfigError(f"{name} must be finite and {'positive' if positive else 'nonnegative'}.")
    return value


def endpoint_url(url: str, test_mode: bool) -> str:
    """Insert /test/ exactly once, immediately before the final URL token."""
    try:
        parsed = urlsplit(url)
        parts = parsed.path.rstrip("/").split("/")
        valid = (
            parsed.scheme == "https" and parsed.hostname and parsed.port != 0
            and not parsed.username and not parsed.password
            and not parsed.query and not parsed.fragment
            and len(parts) >= 2 and parts[-1] and parts[-1] != "test"
            and not any(char.isspace() for char in url)
            and not any(char in url for char in "<>\\")
        )
    except ValueError:
        valid = False
    if not valid:
        raise ConfigError(
            "COGNIGY_REST_ENDPOINT_URL must be an HTTPS URL ending in its token, "
            "without user credentials, a query, or a fragment."
        )
    if len(parts) > 2 and parts[-2] == "test":
        if not test_mode:
            raise ConfigError("URL already uses /test/ but COGNIGY_TEST_MODE is false.")
    elif test_mode:
        parts.insert(-1, "test")
    return urlunsplit((parsed.scheme, parsed.netloc, "/".join(parts), "", ""))


@dataclass(frozen=True)
class Config:
    url: str = field(default="", repr=False)
    api_key: str = field(default="", repr=False)
    api_key_header: str = "x-cognigy-endpoint-key"
    test_mode: bool = True
    timeout: float = 60.0
    request_delay: float = 0.5
    run_delay: float = 1.0
    concurrency: int = 1
    retain_raw: bool = False
    redact_values: tuple[str, ...] = field(default=(), repr=False)

    @classmethod
    def from_env(cls, *, require_endpoint: bool = False) -> "Config":
        # Explicit cwd prevents unexpectedly loading a parent's .env. Shell wins.
        load_dotenv(Path.cwd() / ".env", override=False, interpolate=False)
        url = os.getenv("COGNIGY_REST_ENDPOINT_URL", "").strip()
        test_mode = _boolean("COGNIGY_TEST_MODE", True)
        if require_endpoint and not url:
            raise ConfigError("Set COGNIGY_REST_ENDPOINT_URL in the environment or .env.")
        if url:
            endpoint_url(url, test_mode)
        header = os.getenv("COGNIGY_API_KEY_HEADER", "x-cognigy-endpoint-key").strip().lower()
        if header not in {"x-cognigy-endpoint-key", "x-rest-endpoint-key"}:
            raise ConfigError("COGNIGY_API_KEY_HEADER must be a documented Cognigy Endpoint key header.")
        key = os.getenv("COGNIGY_ENDPOINT_API_KEY", "").strip()
        if any(ord(char) < 32 or ord(char) > 126 for char in key):
            raise ConfigError("COGNIGY_ENDPOINT_API_KEY must contain printable ASCII characters only.")
        try:
            concurrency = int(os.getenv("UC4_MAX_CONCURRENCY", "1"))
        except ValueError:
            raise ConfigError("UC4_MAX_CONCURRENCY must be an integer from 1 to 8.") from None
        if not 1 <= concurrency <= 8:
            raise ConfigError("UC4_MAX_CONCURRENCY must be an integer from 1 to 8.")
        try:
            values = json.loads(os.getenv("UC4_REDACT_VALUES", "[]"))
        except ValueError:
            raise ConfigError("UC4_REDACT_VALUES must be a JSON array of nonempty strings.") from None
        if not isinstance(values, list) or any(not isinstance(v, str) or not v for v in values):
            raise ConfigError("UC4_REDACT_VALUES must be a JSON array of nonempty strings.")
        return cls(
            url=url, api_key=key, api_key_header=header, test_mode=test_mode,
            timeout=_number("COGNIGY_REQUEST_TIMEOUT_SECONDS", 60, positive=True),
            request_delay=_number("COGNIGY_DELAY_BETWEEN_REQUESTS_SECONDS", 0.5),
            run_delay=_number("COGNIGY_DELAY_BETWEEN_RUNS_SECONDS", 1),
            concurrency=concurrency,
            retain_raw=_boolean("UC4_RETAIN_RAW_EVIDENCE", False),
            redact_values=tuple(values),
        )

    def public(self) -> dict:
        return {
            "testMode": self.test_mode,
            "apiKeyConfigured": bool(self.api_key),
            "apiKeyHeader": self.api_key_header,
            "requestTimeoutSeconds": self.timeout,
            "delayBetweenRequestsSeconds": self.request_delay,
            "delayBetweenRunsSeconds": self.run_delay,
            "maxConcurrency": self.concurrency,
            "retainRawEvidence": self.retain_raw,
            "additionalRedactionValueCount": len(self.redact_values),
            "automaticRetries": 0,
        }
