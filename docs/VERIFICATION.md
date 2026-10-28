# v0.1 implementation verification

Verified locally on 2026-10-28, Windows, CPython 3.15.2.

## Results

| Check | Result |
|---|---|
| Editable installation with development dependencies | Passed; used PyYAML's pure-Python fallback because this machine has no Visual C++ compiler |
| `python -m pytest -q` | **138 passed** in 1.08 seconds |
| `python -m uc4_runner validate` | Passed: packaged scenario and environment validation |
| `python -m uc4_runner run --scenario GM-CONTINUITY-001 --repeat 5 --dry-run` | Passed: five isolated plans, ten planned turns, zero requests, null pass rates |
| `python -m pip check` | No broken requirements |
| Wheel build and separate non-editable installation | Passed |
| Default CLI validation from the installed wheel outside the checkout | Passed; packaged YAML scenario present |

Installed runtime dependencies: HTTPX 0.28.1, PyYAML 6.0.3,
python-dotenv 1.2.4. Development test runner: pytest 9.2.0.

The offline batch is under
`reports/20261028T122646484965Z-9f2f9ef6b37b/` (git-ignored). Its outcomes are
PLANNED, not behavioral passes.

## What the mocked tests establish

- A five-run, two-turn batch sends ten mocked POSTs, preserves identity across each
  pair, and creates five unique run/user/session identities and five conversation reports.
- Correct approval/payment and Portal-route replies pass; wrong business-line
  timing, missing/misordered navigation, business-line re-asking, app substitution,
  and cancellation-age diversion fail with reasons and relevant turns.
- Unsupported preparation, redundant help, and repeated greetings produce warnings.
- A mixed batch reports one PASS, one PASS_WITH_WARNINGS, two FAILs, and one ERROR:
  80% complete-conversation reliability, 50% behavioral pass among complete runs,
  and 40% end-to-end pass across all five repetitions.
- Ambiguous timeouts are attempted exactly once, leave subsequent turns skipped,
  and do not prevent later independent runs.
- HTTP errors, redirects, malformed/unexpected JSON, non-finite JSON numbers, and
  empty replies cannot become behavioral passes.
- Bounded concurrent runs retain per-session sequential turn order and isolated cookies.
- Normalization avoids combined-text/stack duplication and supported stream-copy
  duplication while retaining genuine repeated greetings.
- Known credentials, Endpoint tokens, nested sensitive fields, and configured personal
  values are removed from every persisted artifact, including opt-in raw error bodies.
- Dry-run does not construct an HTTP client or sleep; real sockets are blocked
  throughout the development test suite.

## Live status

**No live Cognigy experiment was executed.** No Cognigy resources were inspected
or modified. These results verify the local implementation against mocked responses,
not the actual Flow's behavioral reliability. The first real batch requires the
existing POC Endpoint URL in the user's local environment.
