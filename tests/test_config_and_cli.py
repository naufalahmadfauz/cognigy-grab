from dataclasses import replace
import json

import httpx
import pytest

from uc4_runner import cli
from uc4_runner.config import Config, ConfigError, endpoint_url
from uc4_runner.runner import execute_batch
from conftest import PROJECT


@pytest.mark.parametrize("url,test,expected", [
    ("https://unit.invalid/rest/token", True, "https://unit.invalid/rest/test/token"),
    ("https://unit.invalid/rest/test/token/", True, "https://unit.invalid/rest/test/token"),
    ("https://unit.invalid/token", True, "https://unit.invalid/test/token"),
    ("https://unit.invalid/rest/token", False, "https://unit.invalid/rest/token"),
])
def test_test_mode_inserts_segment_once(url, test, expected):
    assert endpoint_url(url, test) == expected


@pytest.mark.parametrize("url", [
    "", "not-a-url", "http://unit.invalid/token", "https://unit.invalid/",
    "https://unit.invalid/test", "https://user:secret@unit.invalid/token",
    "https://unit.invalid/token?api_key=secret", "https://unit.invalid/token#fragment",
    "https://unit.invalid:bad/token", "https://unit.invalid/a token",
])
def test_invalid_endpoint_is_rejected_without_echoing_it(url):
    with pytest.raises(ConfigError) as error:
        endpoint_url(url, True)
    assert "secret" not in str(error.value)


def test_test_mode_url_conflict_is_explicit():
    with pytest.raises(ConfigError, match="already uses"):
        endpoint_url("https://unit.invalid/test/token", False)


@pytest.mark.parametrize("name,value", [
    ("COGNIGY_TEST_MODE", "maybe"), ("COGNIGY_REQUEST_TIMEOUT_SECONDS", "0"),
    ("COGNIGY_REQUEST_TIMEOUT_SECONDS", "NaN"), ("COGNIGY_DELAY_BETWEEN_RUNS_SECONDS", "-1"),
    ("COGNIGY_DELAY_BETWEEN_REQUESTS_SECONDS", "inf"), ("UC4_MAX_CONCURRENCY", "0"),
    ("UC4_MAX_CONCURRENCY", "9"), ("UC4_MAX_CONCURRENCY", "1.5"),
    ("UC4_RETAIN_RAW_EVIDENCE", "maybe"), ("UC4_REDACT_VALUES", "not-json"),
    ("UC4_REDACT_VALUES", '[""]'), ("COGNIGY_API_KEY_HEADER", "Authorization"),
])
def test_invalid_environment_fails_validation(monkeypatch, name, value):
    monkeypatch.setenv(name, value)
    with pytest.raises(ConfigError):
        Config.from_env()


def test_shell_environment_wins_over_local_dotenv(tmp_path, monkeypatch):
    (tmp_path / ".env").write_text("COGNIGY_REQUEST_TIMEOUT_SECONDS=12\nCOGNIGY_TEST_MODE=false\n")
    monkeypatch.setenv("COGNIGY_REQUEST_TIMEOUT_SECONDS", "35")
    config = Config.from_env()
    assert config.timeout == 35 and config.test_mode is False


def test_endpoint_required_only_for_real_runs():
    assert Config.from_env().url == ""
    with pytest.raises(ConfigError):
        Config.from_env(require_endpoint=True)


def test_default_cli_validation_is_offline(capsys):
    assert cli.main(["validate"]) == 0
    assert "Validated 1 scenario" in capsys.readouterr().out


def test_cli_accepts_json_scenario():
    assert cli.main(["validate", "--scenario-file", str(PROJECT / "examples" / "STATUS-LOCATION-JSON.json")]) == 0


def test_dry_run_never_constructs_http_client(tmp_path, monkeypatch, capsys):
    def forbidden(*args, **kwargs):
        raise AssertionError("Dry-run constructed an HTTP client")

    monkeypatch.setattr(httpx, "Client", forbidden)
    assert cli.main([
        "run", "--scenario", "GM-CONTINUITY-001", "--repeat", "5", "--dry-run",
        "--output-dir", str(tmp_path / "reports"),
    ]) == 0
    report = next((tmp_path / "reports").glob("*/aggregate.json"))
    batch = json.loads(report.read_text(encoding="utf-8"))
    assert len(batch["runs"]) == 5 and batch["mode"] == "DRY_RUN"
    assert batch["metrics"]["transport"]["attemptedTurns"] == 0
    assert batch["metrics"]["behavior"]["passRate"] is None
    assert all(run["outcome"] is None for run in batch["runs"])
    assert len({run["sessionId"] for run in batch["runs"]}) == 5
    assert "no requests sent" in capsys.readouterr().out


@pytest.mark.parametrize("args", [
    ["run", "--scenario", "GM-CONTINUITY-001"],
    ["run", "--scenario", "unknown", "--dry-run"],
    ["run", "--dry-run"],
])
def test_cli_actionable_errors_use_exit_two(args):
    assert cli.main(args) == 2


@pytest.mark.parametrize("args", [
    ["run", "--repeat", "0"], ["run", "--repeat", "-1"], ["run", "--concurrency", "9"],
])
def test_cli_rejects_invalid_counts(args):
    with pytest.raises(SystemExit) as error:
        cli.main(args)
    assert error.value.code == 2


@pytest.mark.parametrize("outcome,expected", [("PASS", 0), ("PASS_WITH_WARNINGS", 0), ("FAIL", 1), ("ERROR", 2)])
def test_cli_exit_codes_for_automation(tmp_path, monkeypatch, config, outcome, expected):
    monkeypatch.setenv("COGNIGY_REST_ENDPOINT_URL", config.url)

    def fake_batch(*args, **kwargs):
        return tmp_path / "batch", {"metrics": {"outcomes": {name: int(name == outcome) for name in (
            "PASS", "PASS_WITH_WARNINGS", "FAIL", "ERROR"
        )}}}

    monkeypatch.setattr(cli, "execute_batch", fake_batch)
    assert cli.main(["run", "--scenario", "GM-CONTINUITY-001"]) == expected


def test_dry_run_does_not_sleep(tmp_path, scenario, config):
    def forbidden(*args):
        raise AssertionError("Dry-run slept")

    execute_batch(scenario, replace(config, request_delay=10, run_delay=10), tmp_path / "reports", dry_run=True, sleep=forbidden)
