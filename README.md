# UC4 Automated Test Runner v0.1.1

A standalone Python CLI for repeated Cognigy REST conversations, deterministic
behavior checks, and redacted evidence reports. Includes `GM-CONTINUITY-001`:
Malaysia GrabMart approval timing followed by compensation status location.

## Install

Python 3.11+ is required. From this project directory, on Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

On macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
cp .env.example .env
```

Activate the virtual environment, or substitute its Python executable for `python`
in all commands below. Windows activation: `.\.venv\Scripts\Activate.ps1`;
macOS/Linux: `source .venv/bin/activate`. Activation is optional.

## Configure

Edit `.env` locally. Set `COGNIGY_REST_ENDPOINT_URL` to the **existing POC REST
Endpoint URL**. Leave `COGNIGY_ENDPOINT_API_KEY` blank for the current unauthenticated
Endpoint. Shell environment variables take precedence over `.env`.

| Variable | Default | Meaning |
|---|---|---|
| `COGNIGY_REST_ENDPOINT_URL` | empty | Required only for real execution; HTTPS, final path segment is token |
| `COGNIGY_ENDPOINT_API_KEY` | empty | Optional Endpoint-specific key |
| `COGNIGY_API_KEY_HEADER` | `x-cognigy-endpoint-key` | Use `x-rest-endpoint-key` for Cognigy 2026.14/2026.15 |
| `COGNIGY_TEST_MODE` | `true` | Insert `/test/` before the token, once |
| `COGNIGY_REQUEST_TIMEOUT_SECONDS` | `60` | HTTPX connect/read/write/pool inactivity timeout, not a whole-batch deadline |
| `COGNIGY_DELAY_BETWEEN_REQUESTS_SECONDS` | `0.5` | Wait between turns within each conversation |
| `COGNIGY_DELAY_BETWEEN_RUNS_SECONDS` | `1` | Sequential inter-run wait; concurrent launch spacing |
| `UC4_MAX_CONCURRENCY` | `1` | Maximum independent conversations in flight, 1–8 |
| `UC4_RETAIN_RAW_EVIDENCE` | `false` | Opt in to redacted full JSON responses, including `outputStack` |
| `UC4_REDACT_VALUES` | `[]` | JSON array of additional exact strings to remove from evidence |

`/test/` enables Cognigy Test Mode; it is **not** the runner's dry-run. Real Test
Mode requests still execute the Flow. The runner does not configure Cognigy
resources. Confirm that the supplied URL already selects the intended isolated POC.

**Raw evidence warning:** enabling `UC4_RETAIN_RAW_EVIDENCE=true` retains full
response structures after redaction; they may still contain sensitive business or
personal data. Review storage permissions and your retention period. All reports
are local; automatic deletion and uploading are not implemented. `.env` and the
default `reports/` directory are git-ignored. Keep custom output directories private.

## Validate, dry-run, execute

```bash
python -m uc4_runner validate
python -m uc4_runner run --scenario GM-CONTINUITY-001 --repeat 5 --dry-run
python -m uc4_runner run --scenario GM-CONTINUITY-001 --repeat 5
```

Validation and dry-run work without an Endpoint or network access. Dry-run creates
five planned conversations with fresh identities and **no simulated Agent replies**;
outcomes and pass rates are null, not passes. Real runs make two sequential POSTs per
successful conversation. Each repetition has independent user/session IDs and a
fresh HTTP client; IDs remain constant across its turns.

Optional flags: `--scenario-file path.yaml`, `--scenarios-dir path`,
`--output-dir reports`, `--concurrency 2`. Validation accepts `--scenario-file` or
`--scenarios-dir` too. `python -m uc4_runner --help` lists commands.

## Regrade saved evidence offline

```bash
python -m uc4_runner regrade --batch reports/20261028T130852758495Z-277613428598 --scenario GM-CONTINUITY-001
```

On Windows, use `.\.venv\Scripts\python.exe` if the environment is not activated.
`--batch` accepts a batch directory or its `aggregate.json`. Select another definition
with `--scenario-file path.yaml` or `--scenarios-dir path --scenario ID`.

Regrade uses the **same production assertion engine** as a real run. It evaluates
saved normalized text and merchant history, without creating an HTTP client or
requiring an Endpoint URL. The selected scenario must retain the original ID,
business line, turn IDs/order, and merchant messages; only expectations may change.
Incomplete captures, dry-run plans, and incompatible scripts are rejected.

Each regrade writes a fresh `reports/regrade-<timestamp>-<id>/` directory. The
original batch stays unchanged. New reports include the source aggregate's SHA-256,
source/current scenario versions, original-versus-updated outcomes, and assertion
changes. Reported HTTP results and capture times remain **historical**; requests
sent by regrading are zero. Raw response copying follows `UC4_RETAIN_RAW_EVIDENCE`
and redaction settings, and cannot recover data absent from the original report.

The supplied first-live-batch regression changes behavioral passes from **2/5 to
3/5**, with warnings. The command exits **1** because two genuine failures remain;
that exit code does not mean offline regrading failed to generate its reports.

## Reports

Each batch creates `reports/<UTC-timestamp>-<unique-id>/`:

```text
manifest.json             # STARTED / COMPLETE; interrupted batches remain STARTED
scenario.json             # versioned, redacted assertion definition
aggregate.json            # metrics, configuration, all runs and conversations
comparison.json           # regrades only: original/current metrics and assertion changes
summary.md                # rates, per-run outcomes, defects, supporting replies/traces
transcripts.json          # all normalized conversations without raw payloads
runs/run-001.json ...     # full per-run evidence (five files with --repeat 5)
transcripts/run-001.md ...
```

Every attempted turn records input, normalized reply, status, timing, correlation
IDs, trace IDs, and assertion results. Raw JSON/body is populated only when opted
in. Raw evidence is structurally complete **subject to redaction**, not byte-exact.
The combined top-level Cognigy `text` is used once, without appending `outputStack`.
See [normalization details](docs/ARCHITECTURE.md).

`PASS_WITH_WARNINGS` counts toward the behavioral pass rate. `ERROR` runs are
excluded from the complete-conversation behavioral denominator and counted in
Endpoint reliability. Partial observations and skipped turns remain visible.
Aggregate reports also show strict passes, end-to-end passes, HTTP success, and
usable-reply rates. A successful HTTP status alone never gives a behavioral pass.

Exit codes: **0** pass / pass with warnings / valid dry-run; **1** behavioral fail;
**2** usage, configuration, validation, or transport/protocol error; **130** interrupted.
An ERROR takes precedence over FAIL for the process exit code. Completed per-run
files are checkpointed; only `manifest.json` with `COMPLETE` denotes a finalized batch.

## Tests

```bash
python -m pytest -q
```

Tests inject `httpx.MockTransport` and block real sockets. They cover successful and
deviating replies, five isolated sessions, timeouts without retries, response parsing,
redaction, concurrency, reporting, configuration, and the offline CLI. Reviewed text
from the first live batch is also tested with synthetic identities and metadata.

## Troubleshooting

- **Windows `python` opens the Store:** use `py` to create the environment, then
  `.\.venv\Scripts\python.exe`. No PowerShell execution-policy change is needed.
- **PyYAML requests Visual C++ build tools on a new Python version:** use its
  pure-Python build (the runner does not need the optional C extension):

  ```powershell
  $env:PYYAML_FORCE_LIBYAML = "0"
  .\.venv\Scripts\python.exe -m pip install -e ".[dev]"
  Remove-Item Env:PYYAML_FORCE_LIBYAML
  ```

  On macOS/Linux, prefix installation with `PYYAML_FORCE_LIBYAML=0`.
- **401/403:** check the existing Endpoint's authentication and key/header locally.
  The runner never prints request URLs or credentials.
- **404:** check the URL and Test Mode compatibility of your deployment. A URL
  already containing `/test/` is accepted with Test Mode enabled.
- **Timeout / 429 / 5xx / redirect:** recorded as ERROR, with no retry. Remaining
  turns in that session are skipped. Increase timeout/delays if appropriate, then
  start a fresh batch. Never replay an ambiguous turn into the same session.
- **Unexpected JSON / empty reply:** inspect trace IDs and, if needed, opt-in raw
  evidence. Custom transformers and non-text-only responses may need a parser change.
- **Behavioral FAIL:** inspect the failed concept, turn, and supporting reply.
  Review wording before widening regexes; increment scenario version after changes.
- **Missing trace IDs:** the Endpoint may omit them. Generated run/session IDs still
  correlate local evidence; no trace ID is fabricated.
- **Corporate proxy / private CA:** environment proxy settings are deliberately not
  inherited by the client; custom network settings need a future explicit option.

## Further documentation

- [Architecture and data flow](docs/ARCHITECTURE.md)
- [Decisions, tradeoffs, and human review](docs/DECISIONS.md)
- [Scenario schema and interpreting results](docs/TESTING_GUIDELINES.md)
- [Recorded local verification results](docs/VERIFICATION.md)
- [Domain vocabulary](GLOSSARY.md)

The shipped expectations are derived from the UC4 specification and the v0.1.1
grading corrections. The initial implementation used mocked responses; the user
subsequently supplied a live batch, regraded offline for v0.1.1. See the dated
verification record for the scope of each result. Scheduling, CI uploads, and
unattended execution are not enabled.
