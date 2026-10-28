"""One redaction boundary for every persisted artifact, including raw evidence."""

import re
from urllib.parse import quote, unquote, urlsplit

from .config import Config, endpoint_url


SENSITIVE_KEYS = {
    "apikey", "endpointapikey", "cognigyendpointapikey", "xapikey",
    "xcognigyendpointkey", "xrestendpointkey", "authorization", "password",
    "secret", "token", "urltoken", "accesstoken", "refreshtoken",
    "cookie", "setcookie", "endpointurl", "cognigyrestendpointurl",
    "email", "emailaddress", "phone", "phonenumber", "mobile", "mobilenumber",
    "name", "fullname", "firstname", "lastname", "address", "ip", "ipaddress",
    "accountnumber", "bankaccount", "merchantid", "customerid", "orderid",
}


class Redactor:
    def __init__(self, config: Config, safe_ids: set[str] | None = None):
        self.safe_ids = safe_ids or set()
        secrets = [config.url, config.api_key, *config.redact_values]
        if config.url:
            secrets.extend([
                endpoint_url(config.url, config.test_mode),
                urlsplit(config.url).path.rstrip("/").rsplit("/", 1)[-1],
            ])
        self.secrets = sorted(
            {variant for secret in secrets if secret for variant in (secret, unquote(secret), quote(secret, safe=""))},
            key=len, reverse=True,
        )

    def text(self, value: str, *, personal: bool = True) -> str:
        for secret in self.secrets:
            value = value.replace(secret, "[REDACTED]")
        # URLs might be echoed by a gateway using a different host or encoding.
        value = re.sub(r"https?://[^\s<>\"']+", "[REDACTED_URL]", value, flags=re.I)
        value = re.sub(
            r"\b(?:api[_ -]?key|authorization|password|access[_ -]?token|url[_ -]?token)\s*[:=]\s*"
            r"(?:(?:Bearer|Basic|ApiKey)\s+)?[^\s,;]+",
            "[REDACTED_CREDENTIAL]", value, flags=re.I,
        )
        if personal:
            value = re.sub(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b", "[REDACTED_EMAIL]", value)
            value = re.sub(r"(?<![\w-])\+\d[\d ()-]{7,}\d(?![\w-])", "[REDACTED_PHONE]", value)
            value = re.sub(r"(?<![\w-])(?:60|0)1\d(?:[ -]?\d){7,9}(?![\w-])", "[REDACTED_PHONE]", value)
        return value

    def clean(self, value, key: str = ""):
        compact = re.sub(r"[^a-z0-9]", "", key.lower())
        if compact in SENSITIVE_KEYS:
            return "[REDACTED]"
        if compact in {"userid", "sessionid"} and (not isinstance(value, str) or value not in self.safe_ids):
            return "[REDACTED_ID]"
        if isinstance(value, dict):
            return {self.text(str(k)): self.clean(v, str(k)) for k, v in value.items()}
        if isinstance(value, list):
            return [self.clean(item, key) for item in value]
        if isinstance(value, str):
            return self.text(value, personal=compact not in {"traceids", "traceid", "runid", "batchid", "userid", "sessionid"})
        return value
