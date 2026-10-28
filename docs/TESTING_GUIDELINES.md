# Writing scenarios and interpreting results

## Commands

```bash
python -m uc4_runner validate
python -m uc4_runner validate --scenario-file examples/STATUS-LOCATION-JSON.json
python -m uc4_runner validate --scenarios-dir my-scenarios
python -m uc4_runner run --scenario GM-CONTINUITY-001 --repeat 5 --dry-run
python -m uc4_runner run --scenario-file my-scenarios/custom.yaml --repeat 5
python -m uc4_runner regrade --batch reports/<original-batch> --scenario GM-CONTINUITY-001
python -m pytest -q
```

The default catalog is `uc4_runner/scenarios/`. To customize the packaged scenario,
copy it into a separate directory and use `--scenario-file` or `--scenarios-dir`.
YAML and JSON share one schema. Validation checks unknown/missing fields, duplicate
keys/IDs, regex syntax, concept references, applicable hard behavior checks, and
environment values. It never probes an Endpoint. Scenario files are trusted local
test definitions; keep real credentials and merchant PII out of them.

## Scenario schema v1

```yaml
schema_version: 1
id: MY-EXAMPLE-001
version: "0.1.0"
description: Optional human description
product: GrabMart
country: MY
concepts:
  portal: ['\bGrabMerchant\s+Portal\b']
  finance: ['\bFinance\b']
  transactions: ['\bTransactions?\b']
assertions:
  - id: stable-identity
    type: session_continuity
    reason: Keep the same conversation identity.
turns:
  - id: status
    merchant: "I'm a Malaysian GrabMart merchant. Where can I check compensation status?"
    assertions:
      - id: location
        type: ordered
        steps: [portal, finance, transactions]
        reason: Explain the Portal navigation in order.
```

### Top-level fields

| Field | Required | Meaning |
|---|---|---|
| `schema_version` | yes | Integer `1` |
| `id` | yes | Unique 1–100 character ID: letters/digits, then letters/digits/underscore/hyphen |
| `version` | yes | Nonempty string; bump when meaning/rules change |
| `product` | yes | Business line used to select product-scoped rules |
| `description`, `country` | no | Nonempty strings when supplied |
| `concepts` | yes | Nonempty mapping of name → nonempty regex alternative list |
| `concept_exclusions` | no | Existing concept name → nonempty regex list of locally excluded match spans |
| `assertions` | no | Rules applied to every turn |
| `turns` | yes | Nonempty ordered list of `{id, merchant, assertions}` |

Each turn needs a unique string `id`, nonempty merchant message, and assertions
list. At least one applicable hard behavioral rule is required per turn, including
common rules; identity checks and warnings alone cannot constitute behavioral grading.
Common and turn-specific assertion IDs must not collide within a turn. The
`transport.` ID prefix is reserved for built-in transport checks.

### Rule fields

Every rule has `id`, `type`, and a human-readable `reason`. Optional `severity`
is `fail` (default) or `warning`. Optional `products: [GrabMart]` scopes the rule to
listed business lines; a mismatch produces SKIP. Unknown fields are errors.

| Type | Additional fields | Evaluation |
|---|---|---|
| `required` | `concepts: [a, b]`, optional `allow_merchant_context: [a]` | Every concept must match the reply, or an explicitly allowed concept may match merchant history |
| `forbidden` | `concepts: [a, b]` | No listed concept may match |
| `ordered` | `steps: [a, [b, c], d]` | At least two steps; steps must follow one another without overlapping; all concepts inside a grouped step must appear, in either order |
| `session_continuity` | none | Check stable request identity and echoed user/session IDs |
| `no_repeated_greeting` | `concepts: [greeting]` | Warn/fail if multiple greeting spans occur in one reply or a greeting occurs after turn 1 |

For `forbidden` only:

- `unless_merchant_concepts: [a, b]` skips the rule when **all** concepts appear in
  the merchant inputs up to and including this turn. Agent claims are never used
  as evidence that the merchant supplied a fact.
- `unless_response_concepts: [a, b]` skips the rule when **all** concepts appear in
  the current reply. If both exception fields exist, satisfying either skips it.
- `warn_if_response_concepts: [a, b]` applies to hard forbidden rules. When a
  forbidden concept matches and **all** listed response concepts also match, record
  WARN instead of FAIL. Without the forbidden behavior the result is PASS. Existing
  `unless_*` exceptions take precedence. This condition checks concept presence;
  ordered navigation remains an independent assertion.

For `required`, `allow_merchant_context` must be a subset of `concepts`. Only those
concepts can be satisfied by merchant inputs up to and including the current turn.
Previous Agent replies never supply merchant context; unlisted required concepts
must occur in the current Agent reply. Result reasons identify concepts supplied
by merchant context.

For each concept, any regex alternative suffices. Matching is Python `re` with
IGNORECASE and MULTILINE. Unicode dashes/apostrophes and horizontal whitespace are
normalized; Markdown `*`, `_`, and backticks are removed for matching only.
No DOTALL flag is added. Use YAML single quotes for regexes; JSON needs double
backslashes. Patterns matching an empty string are rejected.

`concept_exclusions` (optional since v0.1.1) uses the same regex rules. A candidate
concept match is ignored if its span overlaps an exclusion match in the **same
source text**. Other matches remain eligible, so one negated sentence cannot excuse
a separate affirmative sentence. Exclusions also apply when searching merchant
context and exception conditions. They are explicit wording filters, not semantic
negation or fuzzy matching; keep each exclusion narrow and test counterexamples.

## GM-CONTINUITY-001 rubric

**Hard failures**:

- Turn 1 lacks approval in 3–5 business days or next regular payout-cycle guidance;
  or recommends the 1–2 business-day period. GrabMart identity may come from the
  merchant's established context; repeating the name in the reply is optional.
- Turn 2 omits/misorders GrabMerchant Portal → Finance → Transactions → time
  period/store → Compensation for cancelled orders. Both period and store matter.
- Turn 2 instructs use of an app route or asks which business line the merchant uses.
  A harmless App-versus-Portal clarification does not itself fail the app rule;
  incomplete Portal guidance can still fail separately.
- Turn 2 asks cancellation age instead of supplying the complete status location.
- Response user/session identity conflicts with the run's expected identity.

**Warnings**:

- Unsupported order-preparation claim (unless supplied by the merchant).
- Redundant “How may/can I help/assist you [today]?” after a clear question.
- Multiple greetings or greeting again on the follow-up turn.
- Response does not echo both user/session IDs; request continuity remains checked.
- An unnecessary cancellation-age question accompanies otherwise complete status
  guidance. The restriction is configured for this question, not for future scenarios
  where age-based routing is necessary.

An ordered-navigation rule can find each concept's earliest match after the previous
step. Extra mentions earlier in a reply do not invalidate a correctly ordered route.
Grouping `[time_period, store]` permits either order within that selection step.

## Outcomes and report interpretation

| Run outcome | Meaning |
|---|---|
| `PASS` | All evaluated hard checks pass; no warnings |
| `PASS_WITH_WARNINGS` | All evaluated hard checks pass, at least one warning |
| `FAIL` | At least one hard behavior/continuity assertion fails |
| `ERROR` | HTTP/network/timeout/JSON/empty-reply failure prevented reliable full execution |

ERROR has precedence over FAIL. Earlier behavioral failures in an ERROR run are
still recorded. Assertion-level results are PASS / FAIL / WARN / SKIP, with a turn
and reason. Planned/skipped turns and dry-run runs have `outcome: null`.

Read `summary.md` first: complete-conversation reliability and behavioral pass rate
have separate denominators. An all-ERROR batch has null behavioral pass rate, not
0% or 100%. `aggregate.json.metrics.behavior.endToEndPassRate` measures passes across
all executed repetitions. Strict passes exclude warnings; the usual behavioral
pass rate includes them. Recurring defects report occurrences and affected runs.

Use a per-run transcript to see user-facing conversation only. Use per-run JSON
for assertions, HTTP status, request duration, IDs, and optional raw response.
Follow trace IDs into your existing Cognigy investigation workflow. Reported
durations measure the request/response handling, excluding configured sleep delays.

### Concrete examples

- “When was the order cancelled?” on turn 2: HTTP can succeed, but the route and
  answer-location assertions FAIL.
- Correct timing/route plus “How may I help you today?”: PASS_WITH_WARNINGS.
- Correct response text but different echoed session ID: FAIL (continuity).
- HTTP 200 with invalid JSON: ERROR; HTTP success rate can be 100% while usable-reply
  rate is 0%. The next turn is SKIPPED.
- Read timeout: ERROR, exactly one attempt for that turn. Do not infer that Cognigy
  did not process the message, and do not manually resume the abandoned session.

## Offline regrade workflow

1. Select a recorded batch directory or `aggregate.json`, and a current scenario
   with identical scenario ID/business line, turn IDs/order, and merchant messages.
2. Run the [regrade command](../README.md#regrade-saved-evidence-offline). It calls
   the same captured-run evaluator as REST execution, with saved normalized replies
   and original merchant history; no network client is constructed.
3. Inspect the new REGRADE directory's `summary.md`, `comparison.json`, and per-run
   assertions. Verify each changed grade against its supporting reply. Review
   outcome changes and newly detected warnings even when a run's outcome is unchanged.

Regrading is complete when all captured runs have new assertion results and the
new manifest is COMPLETE. Existing ERRORs/skipped turns remain historical transport
evidence. The source aggregate hash and source/current versions identify provenance;
original reports are untouched. HTTP counters refer to the source experiment, not
new requests. Exit codes follow updated outcomes; FAIL runs yield exit 1.

Regrades use saved redacted text and cannot reconstruct omitted raw payloads or
test a new normalization implementation. The output directory must be outside the
source batch. Normalized `transcripts.json` alone lacks required execution/identity
evidence; supply the full aggregate instead.

## Development verification and future regression use

`tests/conftest.py` blocks real sockets, removes Cognigy/UC4 environment variables,
and changes to an isolated temporary directory. Tests inject HTTPX MockTransport;
normal pytest execution cannot call a real Endpoint. Protocol fixtures are synthetic.
`tests/fixtures/gm-continuity-live-v0.1.0.json` contains reviewed text and selected
grades from the first live batch; original IDs, traces, raw payloads, and credentials
are omitted. Regrade tests supply synthetic capture metadata for those conversations.

Tests exercise protocol errors, semantic deviations, five-run isolation, bounded
concurrency/turn order, auth headers, normalization, raw retention/redaction, metrics,
CLI behavior, and validation. Keep behavior examples meaningful: add positive and
negative wording for a rubric change rather than testing implementation internals.

For future Git regression work, commit scenario definitions and code, bump scenario
versions for changed expectations, and compare scenario hashes and runner versions.
Use external CI secrets and explicitly reviewed live-run authorization when CI is
introduced. Do not commit `.env`, raw evidence, or report directories. No workflow,
cron entry, task scheduler job, or unattended test execution is installed in v0.1.
