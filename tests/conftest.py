"""All development tests are offline, including accidental real-client calls."""

import json
import os
from pathlib import Path
import socket

import httpx
import pytest

from uc4_runner.config import Config
from uc4_runner.scenario import DEFAULT_SCENARIOS, load_scenario


PROJECT = Path(__file__).resolve().parents[1]
GOOD_REPLIES = (
    "For GrabMart, approval usually takes 3–5 business days. "
    "Once approved, payment follows the next regular payout cycle.",
    "Log in to the GrabMerchant Portal > Finance > Transactions. "
    "Choose the time period and store, then select Compensation for cancelled orders.",
)


@pytest.fixture(autouse=True)
def offline_environment(monkeypatch, tmp_path):
    def blocked(*args, **kwargs):
        raise AssertionError("Real network access is forbidden in development tests.")

    monkeypatch.setattr(socket.socket, "connect", blocked)
    monkeypatch.setattr(socket.socket, "connect_ex", blocked)
    monkeypatch.setattr(socket, "create_connection", blocked)
    for name in tuple(os.environ):
        if name.startswith(("COGNIGY_", "UC4_")) or name == "PYTHON_DOTENV_DISABLED":
            monkeypatch.delenv(name)
    # Never load a developer's real .env, even while exercising the CLI.
    monkeypatch.chdir(tmp_path)


@pytest.fixture
def scenario():
    return load_scenario(DEFAULT_SCENARIOS / "GM-CONTINUITY-001.yaml")


@pytest.fixture
def config():
    # Reserved .invalid address and dummy credentials; no real Endpoint information.
    return Config(url="https://unit.invalid/rest/dummy-endpoint-token-9a4b", request_delay=0, run_delay=0)


@pytest.fixture
def good_replies():
    return GOOD_REPLIES


def cognigy_response(request: httpx.Request, text: str, **extra) -> httpx.Response:
    payload = json.loads(request.content)
    return httpx.Response(200, json={
        "userId": payload["userId"], "sessionId": payload["sessionId"],
        "text": text, "data": {},
        "outputStack": [{"text": text, "data": {}, "source": "bot", "traceId": "trace-fixture-001"}],
        **extra,
    })


@pytest.fixture
def successful_transport(scenario):
    requests = []

    def handler(request):
        payload = json.loads(request.content)
        requests.append(payload)
        index = 0 if payload["text"] == scenario.turns[0]["merchant"] else 1
        return cognigy_response(request, GOOD_REPLIES[index])

    return httpx.MockTransport(handler), requests
