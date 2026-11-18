# Writing scenarios and interpreting results

Read the section for your task:

- **Authoring:** Use the [schema](#scenario-schema-v1); when adding a gate, also use [advancement conditions](#advancement-conditions).
- **Reports:** Use [outcome interpretation](#outcomes-and-report-interpretation).
- **Regrading:** Follow the [offline workflow](#offline-regrade-workflow).
- **Verification:** Use [development conventions](#development-verification-and-future-regression-use) and, for gate changes, [advancement verification](#advancement-verification).

## Commands

For installation and batch commands, use the [operator guide](../README.md).
When validating a custom scenario, use:

```bash
python -m uc4_runner validate --scenario-file examples/STATUS-LOCATION-JSON.json
python -m uc4_runner validate --scenarios-dir my-scenarios
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
| `turns` | yes | Nonempty ordered list of `{id, merchant, assertions}`; for optional `advance_when`, see [advancement conditions](#advancement-conditions) |

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

### Concept matching

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

An ordered-navigation rule can find each concept's earliest match after the previous
step. Extra mentions earlier in a reply do not invalidate a correctly ordered route.
Grouping `[time_period, store]` permits either order within that selection step.

## Advancement conditions

The optional `advance_when` field (v0.2+) selects existing assertions as a turn's
advancement gate. This excerpt from the
[Portal demo](../uc4_runner/scenarios/GM-PORTAL-STEPS-001.yaml) selects its Finance,
pacing, and Portal-route checks:

```yaml
advance_when: [finance-step, one-step-only, no-app-substitution]
```

For a complete definition, use the linked scenario's concepts, assertions, and
merchant script. For the five-run command, use the [operator example](../README.md#one-by-one-portal-demonstration).

### Gate eligibility

A gate must satisfy these constraints:

- The list is nonempty, with unique assertion IDs from that turn's local or common assertions.
- Each referenced rule is `required`, `forbidden`, or `ordered`, with severity `fail`
  (the default) and applicable to the scenario's business line.
- Each rule checks the current reply: `allow_merchant_context`, `unless_*`, and
  `warn_if_response_concepts` fields are absent.
- The turn has a following scripted turn. Final turns use ordinary grading.

These constraints make each selected assertion PASS or FAIL for a usable reply.
Matching follows the shared [concept rules](#concept-matching), including alternatives
and local exclusions. A required instruction concept can match an action verb and
menu label; a bare menu-name match alone does not establish an instruction.

### Gate results

| Captured result | Progression and grading |
|---|---|
| All selected assertions PASS | Send the next scripted message, even if an unselected assertion fails or warns; those results still affect the run's grade |
| A selected assertion FAILs | Preserve the unexpected reply, grade the run FAIL, and mark every subsequent turn SKIPPED |
| Missing/empty reply or transport/protocol failure | Grade the run ERROR; the gate is unevaluated and subsequent turns are SKIPPED |
| Dry-run or a skipped turn | Gate is unevaluated; its scripted message is unsent |
| No `advance_when` | Continue the fixed script after behavioral deviations; transport/protocol failures still stop the run |

For persisted fields and capture provenance, use [gate evidence](ARCHITECTURE.md#gate-evidence).
Before treating a gate change as verified, satisfy [advancement verification](#advancement-verification).

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

## GM-PORTAL-STATUS-FULL-001 rubric

The [five-turn scenario](../uc4_runner/scenarios/GM-PORTAL-STATUS-FULL-001.yaml)
uses the POC business instructions **GRABMART PORTAL — COMPENSATION STATUS** and
**ONE-BY-ONE SEGMENTATION**. The merchant has already supplied GrabMart, Portal
sign-in, and one-by-one pacing; later messages acknowledge only the gated action.

| Turn | Required current reply | Advancement |
|---|---|---|
| 1 | Instruct opening Finance | Gate before acknowledging Finance |
| 2 | Instruct opening Transactions | Gate before acknowledging Transactions |
| 3 | Instruct selecting a time period covering the order date and the applicable store | Gate before acknowledging both filters |
| 4 | Under Category, instruct selecting Compensation for cancelled orders | Gate before acknowledging Category |
| 5 | Ask whether the cancelled order appears there as compensated | Final grading; no further merchant message |

Required steps must be instructions, not bare labels or common negated directions.
Period/store selection may share a verb or use separate verbs in either order.
Both filters and explicit order-date coverage are required. Known later-step
labels/actions and premature status questions fail pacing; repeating completed
navigation actions also fails. In particular, **period/store plus Category** and
**Category plus status observation** fail even when their individual content is
correct. Each reply ends at its current action/observation, waiting for the next
merchant input; a literal “wait” sentence is not required.

Each of the first four gates selects the required step, `one-step-only`,
`no-app-substitution`, and `no-submission-navigation`. A failure suppresses **all**
remaining merchant messages with zero attempts and preserved stopping evidence.
The final reply must request an observation, rather than assert that compensation
has occurred or ask only about eligibility/order visibility. It must not repeat
navigation or add submission guidance.

**Observed notice / separate human policy review:**

> Please note that compensation will be partial, based on the assessment of the perishable items.

The POC instructions place this once before the first navigation action. This
scenario retains actual emitted wording and records
`partial-compensation-policy-review` as a non-blocking conversation-quality warning
when “compensation will be partial” (or the configured equivalent) occurs. The
review question is whether that certainty is justified before eligibility or an
award is established. This warning records observed behavior, not a newly approved
policy or a requirement to emit the notice. Absence does not fail the run; its
once-only placement is not a new hard gate. With otherwise correct replies, the
notice yields `PASS_WITH_WARNINGS` and appears in the summary and transcripts.

These are deterministic English checks, not a browser or semantic model. Novel
paraphrases and harmless references to future labels may need manual review.
The [mocked tests](../tests/test_portal_status_full.py) exercise actual request
suppression, wording variants, final grading, warning reports, transport errors,
mixed five-run isolation, dry-run planning, and same-path regrading.
Use the [operator commands](../README.md#complete-portal-status-journey) for offline
preparation and future authorized live repetitions.

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

Read `summary.md` first for per-run outcomes and recurring defects. For rate
denominators, null rates, and gate-stop counts, use
[evidence and reliability](ARCHITECTURE.md#evidence-and-reliability).

Read per-run Markdown for the conversation and assertion explanations. Check each
turn's execution status: PLANNED/SKIPPED merchant text is a scripted message that
was never sent. Use per-run JSON for structured assertions, gate results, HTTP status,
request duration, IDs, and optional raw response.
Follow trace IDs into your existing Cognigy investigation workflow. Reported
durations measure the request/response handling, excluding configured sleep delays.

### Concrete examples

- “When was the order cancelled?” on turn 2: HTTP can succeed, but the route and
  answer-location assertions FAIL.
- Correct timing/route plus “How may I help you today?”: PASS_WITH_WARNINGS.
- Portal demo replies “Open Finance, then Transactions” before acknowledgment:
  FAIL; the `one-step-only` gate assertion fails and the scripted acknowledgment is SKIPPED.
- Correct response text but different echoed session ID: FAIL (continuity).
- HTTP 200 with invalid JSON: ERROR; HTTP success rate can be 100% while usable-reply
  rate is 0%. The next turn is SKIPPED.
- Read timeout: ERROR, exactly one attempt for that turn. Do not infer that Cognigy
  did not process the message, and do not manually resume the abandoned session.

## Offline regrade workflow

1. **Select evidence.** Check the source aggregate and selected scenario against the
   [input contract](ARCHITECTURE.md#regrade-input-contract). Record the source batch ID,
   scenario version/hash, and an inventory of relative paths and SHA-256 hashes for
   every file beneath the source directory.
   Keep that inventory outside the source directory and select an output root that
   satisfies the contract. This step is complete when compatible inputs and the
   integrity baseline are recorded.
2. **Generate reports.** Run the [regrade command](../README.md#regrade-saved-evidence-offline)
   with those inputs. Inspect the fresh directory printed by the CLI: its manifest
   must have `executionStatus: COMPLETE`, and every source run must appear in the
   aggregate, comparison, per-run JSON, and transcripts. Verify `mode: REGRADE`,
   `requestsSent: 0`, and [provenance fields](ARCHITECTURE.md#regrade-evaluation-and-provenance)
   against the source and selected scenario. Interpret the process result using
   [exit codes](../README.md#reports); report completion and passing grades are separate checks.
3. **Review grades and integrity.** Read `summary.md`, then check every entry in
   `comparison.json`'s `runs[].assertionChanges` against the saved reply, merchant
   context, and selected rule. Include added/removed assertions and warnings in runs
   whose overall outcome stayed the same. For gated runs, also compare current gate
   evaluations with the source using [gate evidence](ARCHITECTURE.md#gate-evidence);
   review gate-reference or reason changes even when `assertionChanges` is empty.
   Confirm historical transport metrics agree and recompute the source file
   inventory: file names and hashes must match the baseline. Completion requires
   every grade change to be explained by the rubric
   or recorded for follow-up with its run, turn, and assertion ID.

Report the new directory, checks performed, and unresolved grade discrepancies.
Regrading is complete when all three steps meet their criteria; identify any unmet
criterion as unverified.

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
cron entry, task scheduler job, or unattended test execution is installed.

### Advancement verification

When changing a gate's assertions, references, execution, or reports, start with
the mocked examples in [test_advancement.py](../tests/test_advancement.py). Gate
assertion changes also affect progression, so verify the sent script, not just the
final grade. Completion requires passing evidence for every affected boundary:

| Boundary | Completion evidence |
|---|---|
| Authoring | Scenario validation accepts eligible references and rejects ineligible ones; changed expectations have a new version |
| Request sequence | Passing gates send the exact next scripted message; failing gates send no later messages; unselected failures/warnings and ungated failures still continue |
| Capture and reports | Unexpected replies, failing assertion IDs/reasons, and unsent turns are visible; skipped turns have zero attempts and empty replies; per-run evidence agrees with aggregate counts |
| Unevaluated gates | Missing/empty replies and transport failures remain ERRORs; dry-runs send zero requests and keep null outcomes |
| Isolation and aggregation | A mixed five-run mocked batch has independent identities and the expected behavioral/transport denominators, with each failed assertion counted once |
| Regrading | Same-path regrades preserve captured turns and stop metadata; changed paths fail before output creation, per the [input contract](ARCHITECTURE.md#regrade-input-contract) |
