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

---

## v0.1.1 offline grading fix — 2026-10-28

This section records a later verification against the first live batch supplied
by the user. The initial v0.1 results above retain their original historical scope.
All v0.1.1 checks ran locally on Windows/CPython 3.15.2 with **zero Cognigy requests**.

### Reproduction and checks

The initial focused command,
`python -m pytest -q tests/test_grading_accuracy.py`, failed all four minimal
reproductions before the fix: product echo, App clarification, unsupported
preparation, and the hidden follow-up age question. Independent configuration probes
confirmed each cause; see [grading decisions](DECISIONS.md#v011-grading-corrections).

| Check | Result |
|---|---|
| Full suite: `python -m pytest -q` | **237 passed** in 3.23 seconds; 99 added cases, one existing age-question expectation updated |
| New grading/regrade regression files | **90 passed** in 1.86 seconds; remaining 9 new cases validate schema controls |
| `python -m uc4_runner validate` | Passed with scenario 0.1.1 |
| Five-run dry-run | Passed; batch `20261028T143132540071Z-646db957522e`, no requests or evaluated outcomes |
| Historical regrade through the production evaluator | Passed; **3/5 behavioral passes with warnings**, two genuine FAILs |
| Report generation | Five per-run JSON files and five normalized transcripts, aggregate, comparison, summary and COMPLETE manifest verified |
| Source immutability | SHA-256 comparison of **all 15 original files**: byte-identical |
| Reviewed fixture fidelity | All ten merchant/reply pairs and selected original assertion outcomes match the saved batch |
| Captured evidence preservation | Historical HTTP metrics, response text, IDs, trace IDs, durations, raw fields, and capture timestamps unchanged in this regrade |
| Offline packaging | v0.1.1 wheel built with cached tooling and no package-index access; separate installation validated and regraded the historical batch outside the checkout |
| Local editable installation | Updated to v0.1.1 using `--no-index --no-deps --no-build-isolation` |
| Documentation | Ten relative links/anchors verified; Git whitespace check passed |

### Original versus updated grades

Source batch: `20261028T130852758495Z-277613428598`, scenario 0.1.0.

Source aggregate SHA-256:
`be37ee95cc418922ff6bdc7c825d580174e12c11dc172b05c98dfc07923ad474`.

Regrade directory:
`reports/regrade-20261028T142639538423Z-86c7983e4928/` (git-ignored).

| Run | Original | v0.1.1 | Findings |
|---|---|---|---|
| 1 | FAIL | FAIL | Incomplete Portal navigation remains a failure; App clarification is no longer wrong-route evidence |
| 2 | FAIL | PASS_WITH_WARNINGS | Correct timing/payment accepted using merchant-established GrabMart context |
| 3 | PASS_WITH_WARNINGS | PASS_WITH_WARNINGS | Correct guidance; newly detected preparation assumption |
| 4 | PASS_WITH_WARNINGS | PASS_WITH_WARNINGS | Correct route; unnecessary age question now separately warned |
| 5 | FAIL | FAIL | Required approval timeline/payment guidance absent |

- Behavioral passes including warnings: **2/5 (40%) → 3/5 (60%)**.
- Historical transport: **10/10 HTTP successes and usable replies**, unchanged.
- Unsupported preparation: newly detected on turn 1 of **all five runs**.
- Redundant help question: existing warning remains on turn 1 of all five runs.
- Unnecessary age question after complete guidance: WARN on run 4, turn 2.
- No hard-coded per-run outcomes or expected pass counts exist in the evaluator.

### Reproduce

From the repository root in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m uc4_runner validate
.\.venv\Scripts\python.exe -m uc4_runner run --scenario GM-CONTINUITY-001 --repeat 5 --dry-run
.\.venv\Scripts\python.exe -m uc4_runner regrade --batch reports/20261028T130852758495Z-277613428598 --scenario GM-CONTINUITY-001
```

The regrade command writes a new directory each time and exits **1** for the two
remaining behavioral FAILs. Read its `summary.md` and `comparison.json`; original
files remain in place. The committed reviewed transcript fixture allows the suite
to run without the local, git-ignored live batch.

These results establish the grading correction on recorded conversations and
additional paraphrase/negative examples. They do not establish perfect semantic
accuracy or a new live experiment. Remaining risks are documented under
[known limitations](DECISIONS.md#known-limitations). No deployed Cognigy resources
were modified.
