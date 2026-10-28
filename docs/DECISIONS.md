# v0.1 decisions and tradeoffs

These are reversible MVP implementation decisions. There is no new durable
infrastructure or hard-to-reverse architectural commitment requiring an ADR.

| Decision | Reason and tradeoff |
|---|---|
| Python 3.11+, argparse, synchronous HTTPX | Small CLI with straightforward debugging; dependencies limited to HTTPX, PyYAML, python-dotenv and pytest for development. |
| Sequential by default; optional 1–8 run workers | Makes the initial five-run experiment easy to inspect. Each worker owns a complete conversation, preserving turn order. Per-session pacing is not a global rate limiter. |
| Fresh synthetic user/session IDs and HTTP client per run | Prevents conversation and cookie carryover. Stable IDs inside the run exercise follow-up continuity. |
| No POST retries, including HTTP errors and timeouts | A duplicate turn can change behavior and invalidate the experiment. Sacrifices automatic recovery; start a fresh run after review. |
| Stop only the affected session after transport/protocol error | Unknown session state makes later turns uninterpretable. Continue independent repetitions to measure reliability. |
| Record failures while continuing after behavioral deviations | Captures the complete multi-turn behavior rather than hiding later context failures. |
| Deterministic scenario assertions | Reproducible and independent of LLM APIs. Regex concepts approximate behavior; they are not semantic proof and need wording calibration. |
| Require ordered Portal navigation | Merely mentioning Finance and Transactions somewhere is insufficient. Time period/store share a step and may appear in either order. |
| Raw evidence disabled by default | Normalized evidence remains available while minimizing retention. Full redacted response structure is available by explicit opt-in. |
| One redaction boundary; no URL in metadata | Removes known secrets even if echoed into Agent text, nested JSON, or error bodies. Unknown personal data still requires review. |
| Test Mode true by default | Aligns with the intended POC testing. It does not make a real request offline or prevent configured Flow side effects. |
| Dry-run is a plan, not a fabricated success | Produces identities, turns, rules, and files with null outcomes/rates. Mocked execution belongs in development tests. |
| Separate transport and behavioral denominators | Prevents Endpoint outages being disguised as incorrect advice, and HTTP success being mistaken for behavioral success. End-to-end rate keeps total repetition reliability visible. |
| Package the canonical YAML fixture | Default scenario works from an installed distribution. JSON example is a separate minimal authoring demonstration. |
| Schema version, scenario version/hash, stable filenames, exit codes | Supports later Git regression comparisons and CI/cron integration without enabling unattended execution now. |
| Preserve existing repository license and agent instructions | New application files fit alongside existing repository assets. |

## Human review items

1. **Business wording and severity.** Confirm that approval is 3–5 business days,
   payment follows the next regular payout cycle, and the Portal labels/order are
   current for Malaysian GrabMart. These came from the task specification, not a
   live Knowledge Store inspection. Unsupported preparation, redundant help, and
   repeated greetings default to warnings; change scenario severity if they should
   block releases.
2. **Order-age follow-up policy.** Asking about cancellation age fails when the reply
   omits any required status-location concept. A complete location answer followed
   by an age question is permitted. Wrong route order still fails separately.
3. **Deterministic matching tolerance.** The fixture is English-only. It treats an
   explicit 1–2 business-day period or GrabMerchant app route as forbidden, including
   some negated comparisons. Confirm whether these comparisons should be permitted.
   Review initial real responses before adjusting synonyms or condition rules.
4. **Existing Endpoint selection and version.** Supply the isolated POC URL locally.
   Test Mode and any API-key header must match the deployed Endpoint. This runner
   cannot verify which Flow/Knowledge Store the URL selects without separate read-only
   inspection. No resources were inspected or changed during implementation.
5. **Evidence retention and residual PII.** Decide whether to opt into raw evidence,
   where to store it, who may access it, additional redaction values, and deletion
   timing. The runner has no automatic expiration or exhaustive PII classifier.
6. **Future automation.** Choose regression thresholds, treatment of warnings, and
   CI secrets/retention before scheduling anything. Current exit codes already
   distinguish behavioral failure from execution/configuration errors.

These review items are documented defaults, not additional approval prompts in the
application. The supplied CLI can execute once its Endpoint environment is populated.

## Known limitations

- No live Endpoint experiment has been executed during implementation; all HTTP
  verification uses synthetic responses. Actual model variability remains unmeasured.
- Text-based regex evaluation cannot reliably understand negation, indirect claims,
  implication, or novel paraphrases. It can both miss defects and flag valid wording.
- Normalization supports documented REST JSON and conservative stream-copy patterns;
  custom response transformers, arbitrary token overlaps, rich-card-only replies,
  and SSE/WebSocket streams need adapters.
- Missing response identity echoes cannot prove server-side continuity; they warn.
  Missing trace IDs are retained as an empty list, not inferred.
- Reports are redacted representations, not byte-exact responses. Raw retention may
  still retain unrecognized sensitive free text.
- The application holds a batch in memory; very large repetition counts or raw
  payloads may need incremental aggregation. Complete runs are checkpointed locally.
- HTTP timeout applies to individual I/O operations. No global request/run deadline,
  global distributed rate limiter, resume/replay, retry, or resume-after-crash exists.
- Environment proxy settings are not inherited. Custom proxy/private-CA options and
  other authentication schemes are not exposed in v0.1.
- Runtime dependencies have compatible version bounds rather than a platform lock
  file. A tested environment snapshot belongs with future CI setup. Very new Python
  versions may require the documented PyYAML pure-Python installation fallback.
