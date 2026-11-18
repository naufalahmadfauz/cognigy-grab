# OD-004 Q2 — recent-navigation entry and guidance contract

**OD004-RECENT-GUIDANCE-REVIEW-0.2 · 2026-11-03 · Q8 Option B approved with seven qualifications: VERIFIED [POC] / ENGINEERING_AGREED_POC.**

**Agreed provisional internal design basis:** reuse the existing guidance path with a coordinated, bounded
admission/continuation adjustment. Changing only `start_guidance` is insufficient:
the GrabFood checkpoint Tool and validator also exclude recent orders, and the age
resolver deletes their progress. Align those rules with Job precedence and separate
education applicability from evidence that education was actually delivered.
The requesting project-side user's [qualified approval](#recorded-q8-approval-and-provenance)
preserves the **Agent-first architecture** and prefers the smallest existing
instruction/contract changes. It excludes a new controller protocol, unnecessary
persistent walkthrough state and additional Flow infrastructure.

The qualified [OD-004/005 Q1–Q7 agreements](OD004_OD005_TRIGGER_TIMING_REVIEW.md#recorded-q1q7-approval-and-provenance)
remain **VERIFIED [POC] / ENGINEERING_AGREED_POC**. They are inputs, not questions
in this review. **Q8 is answered** for documentation and design direction only;
precise implementation choices and dependent fixture/BR acceptance remain open.
No implementation, current-runtime conformance or official early-form acceptance
is established. `behavior_verdict=NOT_RUN`; `coverage_verdict=NOT_RUN`.
**Business Acceptance Baseline v1.0 remains NOT FROZEN.**

[Decision register](OPEN_DECISIONS.md) · [Requirements/sources](BASELINE_MODEL.md) ·
[Pilots/variants](JOURNEY_PILOT.md) · [Historical findings](DEFECT_GROUP_IMPACT_MATRIX.md)

## 1. Settled behavior and evidence boundary

| Layer | Controlling input / conclusion | Limit |
|---|---|---|
| **Approved provisional behavior** | Q2: explicitly requested or accepted navigation takes priority over unsolicited routine education, including a same-order age correction; retain applicable mandatory disclosures and necessary intake. | Internal POC agreement only; not implementation authorization or guaranteed UI/form support. |
| **Other settled Round 3 choices** | Q1 protects recent age-only education; Q3 protects TC-027 upfront dual entry; Q4 clarifies only genuine ambiguity; Q5 answers new timing questions after decline without automatically re-offering; Q6 supplies the same-session Asia/Kuala_Lumpur (UTC+8) fixture convention; Q7 qualifies supported no-photo continuation. | All original qualifications, formal policy/content/date gaps and source conflicts remain. |
| **Earlier engineering agreements** | OD-001 TC-006 declined-retry primary; OD-008 TC-009 Portal submit-only; OD-003 TC-027 explicit App→computer-Portal readiness; OD-015 staged governance; OD-002 GF A/B/C/D status decisions. | B/C do not complete TC-003 submission coverage; D requires a subsequent established and exercised A target. No blanket GM status-policy adoption. |
| **Current documented implementation** | Fingerprinted October 30 Job/Tool/Code/chart definitions below, plus adopted POC KB. | Static source facts, not today's served configuration, actual Tool invocation, authenticated UI or voice evidence. |
| **Q8 design agreement** | Option B's coordinated existing-path adjustment, compatible-progress retention/selective invalidation and actual-output-based education accounting, governed by the user's seven qualifications. | **VERIFIED [POC] / ENGINEERING_AGREED_POC** for documentation/design direction only; no particular schema, controller protocol or implementation approved. |
| **Dependent acceptance** | Candidate coverage profiles, detailed fixtures, impact selection and future assessment criteria. | Detailed acceptance remains **PROPOSED**; regression protection is agreed, but no new BR/TC/VAR/DF/DG identities, full fixture acceptance or results are supplied. |
| **Unsupported outcomes** | Early form acceptance, current controls/access, official eligibility/evidence/status/duplicate policy and payment remedies. | **UNKNOWN/CONFLICT** where relevant. Neither age classification nor navigation consent supplies these facts. |

The protected **direct GrabMart status-only exception** is retained exactly in
scope: clear current-order GM where/how status navigation, no conflicting identity
or LOB, no timing/eligibility/submission/dual request. It bypasses age-first,
resolver-only LOB lookup, recent/older routing, loudspeaker and mandatory
`start_guidance`; it still requires supported Portal navigation, applicable notice,
readiness and observations. Missing platform/style does not cancel this exception.
Safety, terminal handling and greeting ownership retain precedence.

## 2. Source-grounded static trace

### Provenance and member ledger

Source: `C:\Users\Nau\Downloads\Package-Naufal_2026-10-30_06-38-33.zip`, SHA-256
`e92afdf8d41c5a348e65e18e0a1cad77f827d26dab5c6d3fe136d3439c1a8a1f`.
`JOB30` instruction-string SHA-256, original UTF-8:
`d89731bb49f09959e0c9c35550cb0b9fa71fa03a88295916887672c20390d860`.
Original workbook member SHA-256:
`12e17ad51b6ee2053a4e2c56d3ae8b5ff56f544a6f9a1487dd274c05af5c797e`;
its containing archive/member path and older fingerprints remain in the
[source manifest](BASELINE_MODEL.md#sources-and-authority).

All `config` pointers below mean `/localizedData/0/config`. Code line numbers
refer to the decoded **original `config/code` string**, not Markdown wrapping or
the separately retained `transpiled` string. G/H identifiers are local citations.

| Ref / archive member | SHA-256 | Exact surface inspected |
|---|---|---|
| G01 / `nodeData/6ae43b6f90878ce305636d9a` | `f7d23262e30e4c80f45ad55e240b0a8c98aa2f737f8ea6c9da9e7e8c07f0783c` | `start_guidance`: config `condition`, `parameters`, `description`. |
| G02 / `nodeData/6ae43b6f90878ce305636dae` | `cc6ac64579622ee5abbddd9eb7e20f77ae15c07d6449a3e6a56314acb7d70f50` | Guidance Resolve: config `answer`, `maxLoops`. |
| G03 / `nodeData/6ae43b6f90878ce305636d99` | `d1a22c2045241a9b6360f09f44528321619c27166de75cd4faf54bff10284e48` | Age Tool: required `days_ago`/`lob`, correction description, condition `true`. |
| G04 / `nodeData/6ae43b6f90878ce305636da4` | `29b9f4a6999f4681afb1097a9acbdecee1a8d29febd4ebeb8ccae9189647ae03` | Age Code L14–18, L26–48, L51–60: classification, marker writes, checkpoint deletion/result. |
| G05 / `nodeData/6ae43b6f90878ce305636da6` | `af267f43fa2595f6381b52d346bec3e1867bffdc1f128c80afda62ca93b2aadc` | Age Resolve: config `answer` serializes `input.uc4Result`. |
| G06 / `nodeData/6ae43b6f90878ce305636d9e` | `43d7a5ea63ca44f835b101fa16639f1a8f0a4be85abfde5579aa772587342484` | Checkpoint Tool: condition, schema and commit-before-instruction description. |
| G07 / `nodeData/6ae43b6f90878ce305636dc1` | `aaa8ec129336de863980f6ed026f2676dc0fe6d743853f2b2b422854bf6ea6cc` | Checkpoint Code L19–28, L30–60, L61–84: validation, reset, admission and ordered progression. |
| G08 / `nodeData/6ae43b6f90878ce305636dc3` | `8fdc5cee9cd569798cad2a9880a4e01f2c5885dd9988f26da76896e35d74a912` | Checkpoint Resolve: config `answer` serializes `input.guidanceCheckpointResult`. |
| G09 / `nodeData/6ae43b6f90878ce305636d97` | `71d62956ae2b91db64deef08dcd0aaab37ba1a38f16d43c292f916a622f756c0` | Job instructions; config `memoryContextInjection`, `memoryType`, `toolChoice`, `useStrict`. |
| G10 / `nodeData/6ae43b6f90878ce305636da1` | `b9a453fa3f38cce7bca593115dc06c8c090659396c840ab2c2968f690605506c` | Default-branch output capture: greeting and person-offer state, **no education-delivery capture**. |
| G11 / `nodeData/6ae43b6f90878ce305636d90` | `9e1622e789b519b83df8db5b66b98b851ce457a03c218efaa20f14a25c40643f` | Initializer: stored UTC+8 date/weekday, unknown age/threshold, education/greeting markers. |
| G12 / `chart/6ae43b6f90878ce305636d80` | `d3d37e7042055993ba7f0bda4270cba1b0040cdee047e95f3f41f1262a69b1f5` | Top-level `relations`: Job children, Tool→Code/Resolve and Default→output-capture wiring. |
| G13 / `nodeData/6ae43b6f90878ce305636d8e` | `3169a02b1aa3cc0b500b6f1eb9bbe25d50dbd94c8da9a48d08887210ad4045ea` | First-input LOB capture: bounded initial LOB write, not later correction/progress ownership. |
| G14 / `nodeData/6ae43b6f90878ce305636d8a` | `f49f7b821a438f8aa66f34d3abbaa30f89027b932851b695725adb9b5e2cde5c` | Initialize Once node. |
| G15 / `nodeData/6ae43b6f90878ce305636d8c` | `01114306633149c42c42e3bd4b6f226ca327da877931d6128f62abdbf3fe7cc6` | On First Time child leading to G11. |

### Job contract locators

| Ref / exact JOB30 headings | Relevant current instruction |
|---|---|
| H01 / `CANCELLATION DATE`; `MERCHANT CONTEXT` | Required age/authoritative LOB outside the GM exception; use a newer age only on a clear correction; preserve goal through intake. |
| H02 / `FIXED LOB TIMELINES`; `RECENT CANCELLED ORDER`; `GRABMART RECENT CANCELLED ORDER` | First within + `presentTimeline=true` directs education; age-only open-question wording conflicts with agreed Q1. Recent rules have no explicit requested-guidance precedence. |
| H03 / `OLDER CANCELLED ORDER`; `STATUS AND SUBMISSION TOGETHER` | Direct requested status/submission/dual handling; older elicited education/offer rules retain their specific applicability (general GM offer optional; dual offer required). Dual intent retains status-before-submission observation. |
| H04 / `CURRENT ORDER LOB CORRECTION` | Retain intent, consent and preferences; no repeated start. Newly-within correction explicitly stops prior beyond walkthrough and applies recent education. This paragraph is specifically within the LOB-correction section, not an independently explicit age-only stop rule. |
| H05 / `GUIDANCE`; `GUIDANCE PREFERENCES` | Request or acceptance before guidance; decline stops it. Collect only missing preferences; loudspeaker refusal is not guidance refusal; start once. |
| H06 / `MANDATORY GUIDANCE CHECKPOINTS`; `GUIDANCE TURN BEHAVIOR` | GF App one-by-one begins managed checkpoints after Cancelled-open confirmation; persist before advancing, no backward replay. Reset only abandoned/different-order route; LOB correction invalidates incompatible route. |
| H07 / `PLATFORM SCOPE`; `GRABMART GUIDANCE RULES` | GF App status, GM computer-Portal status; App or Portal submit-only; once-only GM notice; retain original platform preference separately from actual redirected location. |
| H08 / `DIRECT GRABMART STATUS NAVIGATION — ISOLATED POC` | Explicit narrow bypass and retained preferences/location; no mandatory age, loudspeaker or standard start Tool. |
| H09 / `GRABFOOD APP — COMPENSATION STATUS`; `GRABMART PORTAL — COMPENSATION STATUS`; `GRABMART PORTAL STATUS — ONE-BY-ONE SEGMENTATION`; `ALL-AT-ONCE DECISION SEGMENTS` | Current-step waits; missing order differs from blank status; grouped guidance still stops at status/form/submission observations. |
| H10 / `REQUEST FOR COMPENSATION — GRABMERCHANT APP`; `PORTAL SUBMISSION — SEARCH BAR ROUTE`; `APP REQUEST LINK MISSING — PORTAL FALLBACK` | Continue from known location, no restart on fallback; observe link/article/scroll/form; separately accepted Portal fallback. |
| H11 / `FORM NOT VISIBLE — ROLE ACCESS AND ONE RETRY`; `CONNECTION AFTER FAILED FORM RETRY`; `GRABMART PORTAL UNAVAILABLE — SUPPORT OFFER` | Role, retry and transfer decisions remain separate; access recovery retains completed steps and preferences. |
| H12 / `RESOLVED TOOL INFORMATION`; `CONTROLLED FLOW CONTENT`; `GREETING OWNERSHIP`; `CLOSING` | Tool results are internal information, Agent owns ordinary education, Flow owns designated opening/terminal content; continuation is not a new call. |
| H13 / `FOLLOW-UP`; `KNOWLEDGE` | New factual questions answered from grounded information; a request-option explanation/offer is not proof of form access or consent to every task. |

### Complete entry, return and continuation chain

G12 wires three independent Job children:

1. **Age:** G03 → G04 → G05 → returned age facts for Job continuation. G04 writes
   `lob`, `ageDays`, `dateSource`, `threshold`, education marker and conditional
   checkpoint deletion. Returned fields are `success`, `lob`, `lobRequired`,
   `ageDays`, `threshold`, `dateRequired`, `presentTimeline`, `guidanceCheckpoint`.
2. **Start:** G01 → **G02 directly**. There is no intervening guidance Code node.
   G02's answer is exactly `{{JSON.stringify(input.aiAgent.toolArgs)}}`.
   G01 requires four strings: `platform`, `style`, `loudspeaker`, `journey`, with
   `additionalProperties=false`; allowed-value guidance is in descriptions, not
   schema enums. Neither node persists a start flag, consent, preferences, current
   location or completed steps. There is no returned success/admission verdict.
   The Job owns the once-only start and supported-route interpretation.
3. **Managed progress:** G06 → G07 → G08 → authoritative checkpoint result for the
   next managed action. Required args are `operation`, `route`, `checkpoint`,
   `visibility`; the sole route is `grabfood_app_history`. Its name also covers
   the initial **Cancelled-list visibility** gate; History is conditional, not
   mandatory for every order. G09 injects this checkpoint snapshot, but H06 gives
   fresh Tool results precedence. Other navigation uses conversation history.

**Four concrete age restrictions, not one:**

| Surface | Exact current restriction / mutation | Consequence established by definition |
|---|---|---|
| G01 condition | `context.shortTermMemory.uc4.threshold === "beyond"` | Standard start unavailable for within. |
| G06 condition | Requires UC4 state and either an existing `guidanceCheckpoint` **or** `lob === "GrabFood"` with `threshold === "beyond"`. | Fresh within GF cannot initialize; a retained object may make the Tool available without making an operation valid. |
| G07 Code L43 | Rejects unless LOB is GrabFood and threshold is beyond; returns `route_not_applicable`. Exact guard below. | Within initialization/confirmation rejected even if G06 were loosened or an object survived. Reset is handled earlier, at L38–42. |
| G04 Code L48 | Deletes checkpoint if its LOB differs, age is invalid **or** `state.threshold !== "beyond"`. | A valid same-LOB beyond→within correction destroys compatible progress before any continuation. |

G07 L43, verbatim inspected source:

```javascript
if (state.lob !== "GrabFood" || state.threshold !== "beyond") return result(false, "route_not_applicable");
```

G07 additionally validates argument sets, route/version/LOB and stored-state shape;
requires `input.inputId`; rejects repeated progression on the same input and
out-of-order confirmations. Stored fields are `version`, `route`, `lob`,
`completedCheckpoint`, `nextCheckpoint`, `routeComplete`, `orderVisible`,
`lastProgressInputId`. It stores **no cancellation date/age binding, order identity,
style, journey or consent**. Those applicability facts are currently Job-owned.
An initialized route records Cancelled open because the Agent called initialize;
Code does not independently observe the screen. A visible result completes this
visibility route, **not status reading or submission**. Negative post-History
visibility leaves progression blocked. There is no selective date-correction
invalidation operation in the current three-operation API.

**Search boundary:** all 31 exported node definitions, their config strings, all
eight Code nodes and retained transpiled forms were inspected/searched as data.
`educateDelivered` writes occur in G11 initialization and G04 reset/selection;
G10 captures greeting/person offers, not education. No general persisted
guidance-consent/preferences/location state or second recent-start implementation
was found in this export. These negative findings are bounded to the supplied
export; no claim is made about platform internals or today's served deployment.

### Confirmed conflicts versus unproved effects

- **Admission conflict:** agreed recent navigation versus G01, G06 and G07.
  Tool availability is also not evidence of merchant consent or supported UI.
- **Continuity conflict:** G04 deletes compatible GF progress solely because the
  new threshold is within. H04 separately directs a stop after a newly-within LOB
  correction; H02 can replace an age-only correction's active goal with education.
  The precise age-only conflict is therefore Code deletion plus unqualified recent
  routing, not a fabricated quote extending H04's LOB-specific paragraph.
- **Education-accounting conflict:** G04 L44 computes `presentTimeline` from valid
  age/LOB/within/marker only; L45 immediately sets `educateDelivered=true`, with no
  merchant output. Intent is not an input. LOB change resets it, age-only change
  does not. Selection and delivery are demonstrably different events.
- **Representation gap:** the managed checkpoint cannot express a selective
  rollback of date-dependent work after a genuine correction. This is an explicit
  design dependency, not proof that a historical conversation lost progress.
- **No runtime finding:** none of these facts establishes a new live failure,
  common cause for a DG, or invalidates an owner-reported historical closure.

## 3. Requested and accepted recent-entry matrix

Rows below operationalize agreed Q2 and qualified Q8; **precise fixture and
dependent acceptance details remain proposed**. Standard entry retains valid current-order age and resolved
LOB, supported route and genuinely missing preferences. It never changes a real
within value to beyond. A clear request supplies guidance consent; an offer still
requires its answer. Necessary disclosures/intake are not unsolicited education.

| Profile | Consent and goal | Supported handling / retained boundary |
|---|---|---|
| N01 — requested recent status | Explicit help viewing status, not merely asking when money arrives. | GF: App `check_status`; no GF Portal status. GM: apply H08 whenever its exact status-only scope is met; otherwise retain applicable standard context. No inferred submission. |
| N02 — accepted recent status | Affirmative response to a clearly scoped status-navigation offer. | Retain the offered status task, collect only missing applicable facts and continue; no second offer or routine education replay. For GM, assess H08's full current scope, not just a `check_status` label; an unresolved timing/eligibility/dual request is not the exception. |
| N03 — requested recent submission | Explicit request for submission help without a status goal. | `submit_request`, documented App or Portal entry for either LOB; no forced status detour. GM App submit-only stays App. Link/form/access observations remain necessary. |
| N04 — accepted recent submission | Acceptance of an offer explicitly scoped to request-entry/submission help. | Same supported route and observations as N03; consent is to assistance, not Agent-submission or guaranteed acceptance. An offer merely to locate the cancelled order does not automatically authorize every later step. |
| N05 — requested recent dual | Clear status plus conditional review-request goal. | `status_then_submit`; no unsolicited timeline or redundant offer. GF App status; GM Portal status, with App→computer readiness if needed. Observe status before deciding submission; retain pending goal. |
| N06 — accepted recent dual | Both goals already explicit; scoped guidance offer accepted. | Preserve both goals without asking them again. Grouping style never merges status decision, form visibility and submission-report boundaries. GM stays Portal for the later submission segment. |
| N07 — after recent education, generic cancelled-order offer accepted | Bind acceptance to the actual preceding offer and merchant goal. | WB TC-002/026 E5/E15 do **not** show this acceptance. Their App wording cannot create a GM App status route or silently select dual intent. Clarify once only if the full context genuinely leaves the task ambiguous. A clear task needs no clarification/re-offer. |
| N08 — no request/acceptance, or guidance declined | No navigation consent, or consent withdrawn for that task. | Preserve TC-001/025 applicable education and TC-002/026 follow-up/decline. No unsolicited preference collection/start/walkthrough. New timing questions get answers without automatic repeated offers; a genuinely new navigation request may establish new task consent. |

A clear acceptance can establish a now-explicit GM where/how-only navigation goal
when the full conversation meets H08. Merely having offered some help, already
knowing the age, or receiving an unscoped “yes” does not establish the exception.
It must never acquire mandatory age/loudspeaker/Tool intake through this review.
When scope changes to submission/dual/timing, leave the exception, retain valid
facts/location and collect only missing facts needed for the new request. This
transition is a regression boundary, not a fabricated GM App status capability.

### Policy and UI limits on these profiles

The relevant KB statements remain provisional POC, formal approval pending:

| Exact chunk / claim IDs | Evidence boundary |
|---|---|
| `UC4-MY-GF-STATUS-001-C01`; `UC4-MY-GF-CLAIM-005` | App status reference; current authenticated screens untested; approval is not bank receipt. |
| `UC4-MY-GM-STATUS-001-C01`; `UC4-MY-GM-CLAIM-003`, `UC4-MY-GM-CLAIM-004` | Portal status; no GM App status supplied; missing transaction is not rejection. |
| `UC4-MY-GF-SUBMIT-001-C01`; `UC4-MY-GF-CLAIM-012`, `UC4-MY-GF-CLAIM-013`, `UC4-MY-GF-CLAIM-014` | App link when present; Portal alternative. **“Current screens and early form acceptance are untested.”** |
| `UC4-MY-GM-SUBMIT-001-C01`; `UC4-MY-GM-CLAIM-012`, `UC4-MY-GM-CLAIM-013` | Same early-form limit; absent App link proves neither ineligibility nor wrong role. |
| `UC4-MY-SHARED-REQUEST-001-C01`; `UC4-MY-SHARED-CLAIM-007` | Authorized Owner/Manager submission; merchant submits; actual form/access untested. |
| `UC4-MY-SHARED-PORTAL-001-C01`; `UC4-MY-SHARED-CLAIM-011`, `UC4-MY-SHARED-CLAIM-012`, `UC4-MY-SHARED-CLAIM-013` | Reference destinations, not tested menus; the adopted standard remains Search Bar. |

The [existing threshold/evidence/claim ledger](OD004_OD005_TRIGGER_TIMING_REVIEW.md#kb-article-chunk-and-claim-ledger)
also remains controlling: routing age is not an eligibility/deadline gate; Q7's
qualified no-photo guidance neither waives a separately established mandatory
condition nor promises completeness. A compliant guide may reach an access or
specification boundary. It must not manufacture a visible link, successful submit,
compensation approval, early-acceptance rule or payment remedy.

<a id="4-smallest-defensible-proposed-adjustment"></a>

## 4. Qualified Option B design basis

**Controlling interpretation:** B1–B3 describe the agreed behavioral/design
obligations under [all seven Q8 qualifications](#recorded-q8-approval-and-provenance).
The Agent continues to own intent, task consent, preferences and ordinary guidance;
existing deterministic tools/checkpoints retain their bounded roles. Prefer the
smallest changes to existing instructions and contracts. Selective invalidation
does not authorize a new controller protocol, unnecessary persistent walkthrough
state or additional Flow infrastructure. No particular schema, new operation,
field migration or general progress store is selected by this approval.

### Options and recorded selection

| Option | Surface and tradeoff | Recommendation / recorded disposition |
|---|---|---|
| A — change only G01's visible gate | Smallest textual edit; recent Tool settings could be returned. H02/H04 still conflict; G04 still deletes progress; G06/G07 still block mandatory recent GF checkpoints; education marker still overclaims. | **Reject as incomplete.** A returned settings object cannot demonstrate a usable guidance contract. |
| B — align the existing path's admission, continuation and education ownership | Coordinate Job precedence, G01, G04 and G06/G07. Keep supported routes, observation/consent rules and narrow GM bypass. Add only the correction semantics needed to retain valid progress and invalidate stale date-dependent progress. | **Selected with seven qualifications**, requesting project-side user, 2026-11-03. **VERIFIED [POC] / ENGINEERING_AGREED_POC** design direction only; Agent-first/minimal existing-contract adjustment governs. Exact implementation representation is unselected. |
| C — separate recent Tool/path or generalized prompt-only bypass | Adds another start/continuation convention; still needs correction/education reconciliation. A bypass could evade mandatory GF checkpoint commits and blur H08's deliberate narrow scope. | No source-grounded need for this additional path. Not the minimum adjustment. |
| D — pretend the order is beyond, or defer navigation until older | Evades the gate by corrupting classification or overriding agreed priority. | Incompatible with settled Q2 and truthful age routing; not an admissible implementation choice. |

### B1 — admission and start ownership

- Retain deterministic, truthful age/LOB classification. A **valid within or beyond
  classification** may support standard requested/accepted navigation; missing or
  invalid age/LOB still requires its existing necessary clarification. H08 remains
  age-independent and outside this standard admission rule.
- Job authorizes the **specific task** from request or accepted offer and applies
  supported-platform rules. Gate availability alone is not consent. Preserve the
  existing four-setting start interface where possible; returning settings does
  not assert form access, status, completion or delivery.
- Reconcile H02/H03/H04/H05 precedence explicitly: active requested/accepted
  navigation wins over **routine unsolicited** recent education, including a valid
  same-order age correction. Answer a new factual question when actually asked;
  retain safety, applicable disclosures, intake and older elicited-inquiry rules.
- Start once per new supported walkthrough. An active walkthrough, fallback,
  status→submission continuation or same-order correction is not a second start.
  The existing start return may remain an echo; it is not a progress/recovery API.

### B2 — retain compatible context, invalidate only what changed

| Context | Qualified design retention rule | Current ownership / necessary limit |
|---|---|---|
| Order and routing facts | Same-order valid correction updates age/threshold; retain the authoritative LOB unless actually corrected. Clarify genuinely uncertain identity before switching. | G03/G04 plus H01/H04; never carry another order's age or observations. No new merchant order-ID collection. |
| Intent and guidance consent | Retain the requested/accepted task and pending dual submission across age-only correction. Respect a subsequent decline. | Job/conversation owns these facts; no persisted general consent field exists. Retry, fallback and transfer consent are separate, not implied. |
| Preferences | Reuse platform choice, style and loudspeaker answer; a loudspeaker “no” remains a preference. | Start echo is not stored preference state. Preserve original platform choice separately from actual route/location, especially GM App→Portal. |
| Current location and completed actions | Keep established actions/observations that remain valid for the same order and supported route; advance from the outstanding action, not from the beginning. | H09/H10/H11 conversation context; managed GF route must use its authoritative persisted checkpoint, not reconstruct commits from recollection. |
| Date-dependent actions | A corrected cancellation date can invalidate a chosen filter/date and dependent visibility even if order and route stay the same. Retain unrelated completed actions. | G07 stores no selected date/age binding and offers no selective invalidation. Future design must reconcile that limit within existing instructions/contracts; no new rebase operation, persistent field or controller protocol is approved or presumed necessary. |
| Status, form and submission observations | Reuse only observations still attributable to the corrected current order and relevant screen. Correction alone confirms none of them. | Status reading, form visibility and merchant-reported submission remain distinct. No backend acceptance/approval is inferred. |
| Disclosures and education | Keep applicable once-only greeting/GM notice history separate from education. Track what was actually presented for the relevant LOB/context. | G10 greeting/person-offer capture does not capture education; neither a checkpoint nor `educateDelivered` supplies delivery evidence. |

**Correction cases illustrating the agreed obligation — detailed fixtures pending, not executed examples:**

| Same-session situation | Correct continuation / invalidation boundary |
|---|---|
| GF age 14 corrected to 1 on the declared Tuesday reference; Cancelled open, visibility answer pending | Keep within classification and valid Cancelled-open checkpoint; ask the still-required visibility question. No education takeover, second start or inferred order visibility. |
| Same correction after History opened, before date selection | Keep History-open completion; select the corrected cancellation date next. Do not replay Orders/Cancelled/History simply because the age is now recent. |
| Same correction after selecting/confirming the old date or observing a date-filtered result | Validate whether the selected date/range still covers the corrected order. If incompatible, retain History-open and invalidate date-selection/confirmation/dependent visibility, returning to the earliest genuinely invalid action. This **explicit correction** is a narrow amendment to existing monotonic/reset rules, not arbitrary backward replay. |
| GM Portal period/store already chosen | Keep Portal/Finance/Transactions and other compatible actions. Revisit only a period/date-dependent observation made invalid by the correction; retain store/Category where valid and wait for the relevant result. No GF History or invented App status. |
| App/Portal submission underway; no date-dependent navigation invalidated | Continue from confirmed article/scroll/form stage as applicable, retaining task and observations. Recent age is not proof that the form accepts an early request, nor a reason to restart status first. |
| Valid same-order LOB correction | Keep intent/consent/preferences, but discard incompatible route/status/evidence assumptions. Apply corrected supported route/readiness; GF checkpoint completion is never inherited by GM or a different order. Newly-within classification alone must not cancel active consent. |
| Age/identity unclear, missing state, stale/inconsistent checkpoint | Clarify or use the supported recovery boundary without inventing a successful commit. Retain trustworthy conversational facts; no fabricated checkpoint reconstruction, forced reset or UI advancement. Exact recovery beyond the documented contract remains blocked. |
| Merchant abandons walkthrough, chooses another order, or terminal/safety path applies | Do not retain active progress as authority to continue the old task. Existing abandonment/reset and higher-priority handling still apply. |

G06 availability, G07 applicability and G04 checkpoint retention must agree on
recent **valid** GF progress. Retain route/version/LOB validation, one-input/one-
progression, earliest-incomplete step, explicit visibility and commit-before-next-
instruction. Merely deleting `threshold !== "beyond"` from G04 would still leave
G07 refusing progress; merely retaining everything would retain stale selected-date
work. The narrow correction rule above is essential to a defensible adjustment.
Future design must establish compatibility through the smallest defensible
existing instruction/contract adjustments, without collecting an order ID,
inventing absolute-date policy, or using a reset to bypass an observation.
The current API limitation is a source fact, not a mandate for additional
infrastructure or a replacement state model. If minimal adjustments cannot meet
the agreed behavior, that design limitation requires review rather than silently
expanding Q8's scope.

### B3 — education applicability is not delivery

**Qualified Agent-first responsibility split:** the resolver supplies classification
and an education-applicability hint; the Job chooses whether education applies now
and deduplicates it using actual prior Agent output for the relevant context.
Age resolution must not mark education delivered. The legacy `educateDelivered`
value is not delivery authority; preserving it for compatibility must not suppress
an owed explanation or certify education that never appeared. `presentTimeline`
must no longer mean “education is owed now regardless of intent” or “already spoken.”
No new general delivery-tracking Tool or broad persistent journey store is required
by this agreement. Existing output/history supports content accounting; it must
not certify unobserved delivery. Any necessary legacy-marker adjustment is a
future minimal-contract design item, not approval of a new delivery protocol.

| Evidence / event | Qualified design interpretation |
|---|---|
| Resolver returns `presentTimeline=true`, then navigation takes priority | Education was eligible/suggested, not delivered. Preserve navigation; do not create a compulsory education backlog or replace its next action with anything-else. |
| Actual relevant education already appears in Agent output/history | May support deduplication of that presented content; do not repeat the full bundle because age was recomputed. It does not certify audible completion. |
| `educateDelivered=true` but no matching education output | Delivery unestablished. Do not count this as TC-001/025 education coverage or use it to refuse a genuine later timing question. |
| Partial/generated/displayed output with missing or interrupted audio | Record what each evidence channel shows; audible delivery remains unverified under OD-013. A marker must not erase the distinction or automatically force a full replay. |
| New timing question during/after guidance, including after decline | Answer the question with applicable qualified facts; keep pending step/goal where still active and respect Q5's no-automatic-repeat-offer rule. |
| Different LOB/order or unsupported history | Reassess applicability and known delivery for that context; do not carry an incompatible explanation's completion across it or treat unknown evidence as delivered. |

This split protects both opposite errors: suppressing education that a real trigger
requires, and interrupting consented navigation merely because the resolver set a
first-recent flag. It introduces no new merchant acknowledgement requirement and
no change to greeting or transfer-offer ownership.

## 5. Independent behavior and coverage criteria

Q8 qualification 7 agrees to protect the education, decline, navigation and
same-order correction coverage below. The following remain **proposed future
assessment criteria**, with exact fixtures and dependent BR acceptance pending.
Current outcomes on both
axes remain `NOT_RUN`; no example below is an observed PASS. Keep the
[existing two-verdict vocabulary](BASELINE_MODEL.md#two-independent-verdicts), not
new runner result fields or a reinterpretation of historical automated grades.

| Target | Behavior criterion on the observed branch | Evidence required for target coverage |
|---|---|---|
| Requested recent navigation | Honor the explicit task without unsolicited education/re-offer; retain intake/disclosures, supported route, pacing and observations. | Actual within fixture, explicit request and the declared navigation milestones. An offered-but-unaccepted or beyond path does not cover it. |
| Accepted recent navigation | Actual scoped offer and acceptance precede navigation; preserve that task without repeated consent collection or invented submission intent. | Offer, merchant acceptance, actual recent classification where standard, and the selected status/submission/dual path. A direct request is a separate entry profile. |
| Recent status-only | Supported GF App or GM Portal; merchant-observed result, no invented submission/eligibility. | Applicable location/actions and actual status observation. Returning Tool settings, opening a tab or only reading a status-location answer is not full walkthrough coverage. |
| Recent submission-only | No forced status detour; supported request entry, observed form/access, qualified evidence and merchant self-submission/report. | For a full submission target: entry/link or Portal route, article/scroll, form visibility, completion guidance and explicit submission report. A justified missing-form stop can be correct behavior but incomplete full-submit coverage. |
| Recent dual | Preserve both goals, observe status before conditional submission, keep separate business observations in either pacing style. | For a submission target: observed status/remaining intent establishes its reviewed branch, then all required submission stages. Correct approval-only handling cannot substitute. GM alternatives retain their own policy blockers. |
| Active beyond→within correction | Truthful recomputation; retain valid consent/preferences/progress, selectively invalidate incompatible date work, no routine education takeover or restart. | Actual active beyond stage, clear same-order correction to within, evidence of retained/invalidated facts and subsequent supported progression. Starting recent is not correction coverage. |
| TC-001/025 education control | Applicable recent age-only education, correct LOB/stage evidence wording and qualified approval/payout facts; no unnecessary goal question, inferred preparation/packing or unsolicited navigation. | Original recent education and finish milestones, from actual replies. Neither marker nor a successful navigation variant supplies education coverage. |
| TC-002/026 decline control | Recent education/follow-up/offer; respect explicit decline; further help/finish without continuing guidance. | Original offered-and-declined sequence and finish. Accepted recent guidance is a different target and cannot count toward these originals. |

For OD-002, preserve exact existing identities: A is TC-003's visible-blank
submission target; B/C/D are `VAR-TC-003-A/B/C`. Correct B/C remains incomplete
original submission coverage; D counts only after A's conditions and full stages
are actually established/exercised. A full target traversed with a supported
behavioral violation can still have coverage independently recorded. Unsupported
UI/policy judgments are `BLOCKED_SPEC` or `NEEDS_REVIEW` as applicable, not inferred
Agent failures; missing environmental evidence is assessed separately.

### Proposed regression selection

No executable fixtures are created here. **N01–N08 are review-profile aliases, not
registered variants.** New recent accepted/requested and correction fixtures need
their own reviewed version/identity before future execution; changing an original
beyond TC's age does not preserve that TC's target coverage.

| Selection | Reason / conditions to exercise | Identity and scope protection |
|---|---|---|
| N01–N06 across GF/GM and direct request/offer acceptance | Cover all three tasks and both consent entry mechanisms. Include one-by-one and all-at-once where supported; known/missing preferences and loudspeaker refusal. | Separate recent candidates; H08-qualified GM status stays bypassed. No unsupported GF Portal or GM App status cross-product. |
| N07 offer-scope boundary | Recent nonreceipt follow-up acceptance with explicit status, submission or dual scope; genuinely ambiguous versus already-clear context. | Derived from, but not replacements for, TC-002/026 declined targets. No registered accepted-recent variants currently exist. |
| Same-order correction at start intake, Cancelled visibility, History/date/Confirm, observed status, form access and pending submission | Detect lost consent, blanket resets, stale date filters, false completion and unwanted education. Include within→within and unchanged beyond controls when the same changed rule applies. | Use explicit cancellation ages, declared same-session Asia/Kuala_Lumpur reference and actual initialized weekday. No midnight/absolute-date convention inferred. |
| GF managed checkpoint positive and negative controls | Visible Cancelled order avoids History; missing order exercises History→Date→Confirm→separate visibility. Include duplicate-input, out-of-order, invalid-state and negative visibility conditions. | Protect existing commit, monotonicity and visibility gates; explicit compatible correction versus justified date-dependent invalidation are distinct. |
| Education/delivery controls | TC-001/025; TC-002/026; suggested-but-suppressed education versus actual output; repeated classification, new timing inquiry after decline, partial/absent voice evidence. | Actual education and original decline remain independent targets; transcript-only evidence cannot settle audibility. |
| Existing older direct versus elicited controls | TC-003/027 upfront dual; TC-005/029 older open-question→education/offer→accept; TC-004/028 education/no-walkthrough. | Q3 and earlier agreements stand. TC-004 stays beyond despite DF-018 N22's within fix note; source omissions of offer/finish answers remain explicit. |
| Submission/recovery controls | TC-006 declined retry with its separate accepted-success/failure variants; TC-007 stuck step; TC-008 missing link/fallback; TC-009 Portal submit-only with failed accepted retry and later transfer consent. | Age correction does not renew a declined retry or spent retry allowance; guidance consent does not authorize retry/fallback/transfer. |
| GM bypass/transition controls | `VAR-TC-027-F` no age/loudspeaker; App→Portal readiness, Portal-first, unavailable/recovered Portal, App submit-only `VAR-TC-027-G`; exception→new submission scope. | Retain once-only notice, style/location and separate readiness. No repeat start solely for transition, no expansion of bypass to dual intent. |
| Boundary controls | Known/unknown/ambiguous LOB/order, valid versus invalid age, withdrawn guidance, TC-010 genuine unrelated scope, applicable safety/terminal/greeting ownership. | No fabricated age/LOB/state or terminal resumption; specific unavailable outcomes remain blocked rather than invented. |

Select cases by the changed requirement and actual precondition, using the
[existing impact-selection procedure](DEFECT_GROUP_IMPACT_MATRIX.md#requirement-driven-regression-selection--reviewer-procedure-proposed).
This is a scope proposal, not a claim that every Cartesian combination or every
variant needs identical repetition. Record acceptance/fixture/configuration/channel
versions, entry/offer evidence, declared versus observed clock, pre/post correction
state, committed checkpoints and actual replies/observations. Sampling, named
reviewers, implementation and any execution remain separately pending.

## 6. Affected requirements, cases, variants and findings

### Requirements and existing identities

| Requirement / family | Relationship to the qualified design basis | Existing cases / variants affected by applicability |
|---|---|---|
| BR-001/002/003/005/014 | **Direct contract core:** truthful age/LOB, intent and consent retention, education applicability/delivery, preferences and decline. | BP-01 TC-001/025; BP-02 TC-002/026; BP-03 TC-004/028; applicable entry/continuation in the other journeys. |
| BR-006/007/008/009/019 | **Direct progression/decision boundary:** ordered checkpoints, valid current location, status-before-conditional-submit and supported recovery. | BP-04 TC-003/005/027/029, TC-007 status segment; BP-06 TC-007/008. `VAR-TC-003-A/B/C/D`, `VAR-TC-027-A/B/D/F`; GM B remains proposed, not the agreed GF policy. |
| BR-010/011/012/013 | **Downstream reachability and retained observations:** entry/form/access/evidence/self-submission; no early-UI guarantee. | BP-05 TC-006/009 and applicable TC-003/005/007/008/027/029. `VAR-TC-003-E/F`, `VAR-TC-006-A/B/C/D/E`, `VAR-TC-027-E/G`; unsupported access outcomes remain open. |
| BR-004/018 | **Disclosure protection:** one applicable opening; once-only GM notice and explicit Portal readiness. | TC-001 entry; TC-027/029 and applicable GM variants; recent education-only and GF negative controls. Notice certainty remains OD-006. |
| BR-015/016 | **Consent/scope boundary**, not new transfer authority. | BP-07 TC-010, TC-009; applicable TC-006 and `VAR-TC-027-C`. Recovery consent and terminal ownership remain separate. |
| BR-017/020 | **Evidence/adjudication**, not extra merchant instructions. | Voice/display and semantic-versus-controlled-text judgments; specifically reported TC-026/003 voice concerns and other applicable channel controls. |

This table accounts for all 15 original TCs through existing conditional mappings,
not 15 new failures or expanded journey specs. All **18 registered variant rows**
retain their meanings and approval states. The new recent profiles supplement
future coverage; they do not rename the original three pilots or their variants.

### Existing defect groups: historical evidence versus plausible impact

| Group | Direct historical findings relevant to the boundary | Proposed regression relationship / limit |
|---|---|---|
| DG-002 — context/intent | DF-002/F01; DF-006/F01, DF-007/F01, DF-009/F01; DF-011/F01–F02; DF-008/F01 and DF-015/F01 positive context observations. | Core plausible retention/intake regression. No report proves this new same-order age-correction failure or a shared state cause. |
| DG-003 — education/timing | DF-005/F01; DF-006/F02, DF-007/F02, DF-009/F02, DF-010/F01, DF-014/F01, DF-015/F02–F03; DF-018/F01–F02. | Core trigger/delivery controls. Direct TC union stays TC-004/005/007/008/027/028; recent controls are additional impact, not new DF links. DF-014/018 owner resolutions remain. |
| DG-004 — status/progression | DF-004/F01, DF-007/F03, DF-014/F03; positive DF-008/F02, DF-009/F03, DF-016/F01, DF-017/F02. | Checkpoint/route/date-observation regression; conditional Date selector concerns are not evidence that every order must visit History. |
| DG-006 — status/submission | DF-008/F03, DF-009/F04–F05, DF-017/F01–F02; DF-016/F01 positive control. | Retained pending intent, no blind duplicate and supported fallback. OD-002 behavior/coverage distinctions remain; no new approved GM status policy. |
| DG-005 — role/access | DF-003/F01, DF-004/F02, DF-007/F04, DF-009/F06; DF-011/F03 positive role advice. | Plausible downstream reachability/correction impact. Universal spoken-role reminder and current form support remain unresolved, not solved by wider age admission. |
| DG-007 — consent/finish/scope | DF-003/F02–F03, DF-005/F02, DF-008/F04, DF-009/F04, DF-011/F04–F05, DF-014/F04, DF-015/F03–F04; DF-012 terminal contexts. | Protect decline/retry/transfer separation and unresolved intent; no automatic transfer on age correction or access failure. Disconnect attribution remains unproved. |
| DG-008 — GM notice | DF-014/F02 reports delayed notice, not wholly missing disclosure. | Once-only applicable notice retained through status/submission and corrections; historical parent closure and OD-006 certainty issue remain independent. |
| DG-001 / DG-009 | DF-001/F01 opening; DF-013/F01 silence, DF-017/F03 voice/display divergence; DF-005/F02 and DF-012/F02 terminal/capture contexts. | Boundary evidence controls. Education marker cannot prove audio; no fresh opening/voice defect, numeric SLA or barge-in remedy is asserted. |

Membership authority remains the unchanged
[49-row atomic ledger and nine-group matrix](DEFECT_GROUP_IMPACT_MATRIX.md#atomic-finding-ledger).
Original DF statuses/severities and direct TC associations are untouched. In
particular DF-018 remains directly linked to **beyond TC-004**, DF-016 remains
**Not a defect**, and DF-017's blank historical status remains blank. The static
contract conflicts here are not newly assigned DF findings or regrades.

## 7. Human-review frontier

**Decision tree:** settled Q1–Q7/earlier agreements → established static chain
facts → **Q8 Option B agreed with seven qualifications** → scoped business-
acceptance fixture/BR review → later minimal Agent-first implementation design
and separately authorized implementation/evidence work. Official UI/policy and
formal acceptance evidence remain parallel dependencies. Q8 is not asked again.

### Original Q8 question and recommendation — historical

The following question and recommendation were presented in v0.1. Their original
pending disposition is retained in the pre-approval snapshot; the answer below
supersedes that pending status and constrains the proposed representation details.

❓ **Q8 — Existing-path contract adjustment:** Shall Option B be the provisional
internal design basis: align standard admission and GF checkpoints for valid recent
navigation, retain compatible progress with narrow date-correction invalidation,
and make education delivery depend on actual output rather than resolver selection?

➡️ **Recommended: yes**, within B1–B3 and the protected GM exception. This chooses
the smallest coherent contract surface; it does not authorize implementation,
new executions, official early-form acceptance or a baseline freeze. Q1–Q7 remain
settled. **Historical v0.1 disposition: PROPOSED / unanswered.** Superseded by the
actual qualified approval below, not by inference from the investigation request.

### Recorded Q8 approval and provenance

**Decision:** Approved with seven qualifications — **Option B**, provisional
internal POC engineering design basis, **VERIFIED [POC] / ENGINEERING_AGREED_POC**.

**Source and decision-maker:** requesting project-side user's explicit approval
message in this conversation, **2026-11-03**. Personal name, official role and
formal Grab business/benchmark or QA authority were **not supplied**. This record
attributes only the stated project-side internal agreement. Formal sign-off fields
remain unassigned. AI-assisted preparation is not approval authority.

**User's approval and qualifications (verbatim):**

> I agree with **Q8 — Option B** as the provisional internal POC engineering design basis.
>
> Please record the following qualifications:
>
> 1. Use coordinated adjustments to existing guidance admission, checkpoint validation and age-correction handling. Do not treat changing `start_guidance` alone as sufficient.
>
> 2. Preserve compatible merchant intent, consent, guidance preferences, current location and completed actions after a same-order age correction. Invalidate only progress that is no longer valid under the corrected facts.
>
> 3. Distinguish education selected or flagged internally from education actually delivered to the merchant. Do not mark a disclosure as delivered merely because the resolver selected that branch.
>
> 4. Preserve our existing Agent-first architecture. Prefer the smallest changes to existing instructions and contracts. Do not introduce a new controller protocol, unnecessary persistent walkthrough state, or additional Flow infrastructure.
>
> 5. Keep the existing GrabMart direct status-only exception and all previously agreed Q1–Q7 behaviors intact.
>
> 6. This agreement does not establish early-order eligibility, guarantee compensation, authorize unsupported form submission, or override unresolved business policy and UI restrictions.
>
> 7. Preserve regression coverage for recent education (TC-001/025), declined guidance (TC-002/026), affected navigation variants and same-order age corrections.
>
> **This approval is for documentation and design direction only.**
>
> Do not modify Cognigy, the Agent Job, Tools, Code, Knowledge Base or Python runner. Do not execute live tests or freeze the full acceptance baseline.
>
> Record Option B, update the impacted documentation, preserve version history and report any remaining policy or fixture blockers.
>
> Once this review is complete, recommend the next focused business-acceptance workstream rather than starting implementation.

**Rationale and affected scope:** coordinated reuse addresses the four confirmed
restrictions while preserving supported guidance and correcting false delivery
accounting. The chosen constraint is minimal Agent-first adjustment, with
compatible-progress retention and invalidation limited to changed facts. Sections
3–6 identify affected BR/TC/VAR conditions; this v0.2 record overlays those design
obligations without promoting every candidate fixture or BR to accepted status.

**Superseded interpretation:** v0.1's unanswered Q8 and proposed Option B now have
an explicit answer. Its “correction/rebase representation” and “field/API migration”
language must not be read as requiring or approving a new controller protocol,
additional Flow infrastructure or unnecessary persistent walkthrough state.
Selective invalidation is an agreed behavioral obligation; its exact mechanism is
future work within qualification 4. The source trace, alternatives, original Q8,
audit and benchmark/defect history remain preserved. Q1–Q7 and earlier agreements
retain their full qualifications. Neither evidence verdict changes from `NOT_RUN`.

### Remaining blockers and next dependent work

| Blocker | What remains needed / scoped effect |
|---|---|
| Contract direction — settled | Q8 selects Option B with seven qualifications. This is no longer an unanswered blocker; current implementation contradictions remain source facts. Gate-only relaxation is insufficient. |
| Minimal implementation design — later work | Reconcile existing admission, checkpoint validation, correction handling and legacy education accounting while retaining Agent ownership and validation/consent boundaries. Exact representation remains unselected; no controller protocol, unnecessary persistent walkthrough state or additional Flow infrastructure is authorized. This work is not started by recording approval. |
| Coverage fixtures and dependent BR acceptance | Register/version new recent requested/accepted/correction targets; define exact starting observations and endings. Original TC-001/025 education and TC-002/026 decline remain intact. OD-007/010/009 recovery/access/finish details follow as scoped review. |
| UI/policy — OD-014, residual OD-002/005 | Authoritative early-form conditions/access, statuses/duplicates, evidence requirements/substitutes and unpaid remedies. Navigation reachability cannot certify an accepted early request or payment outcome. |
| Timing/content — OD-005/006/011 | Absolute-date/midnight/business-calendar conventions; GM notice certainty and controlled text. Existing qualified fixtures/content remain their scoped reference. |
| Configuration/evidence/governance — OD-012/013/015 | Current served revision, separately authorized future verification, actual reply/voice evidence and named business/benchmark/QA reviewers. Historical closure/Problem #1 retrieval scope is preserved. |

**Recommended next focused business-acceptance workstream: OD-007/010/009 —
recovery, access and consent/finish fixtures.** Its scope and deliverables are in
[the next-batch recommendation](OPEN_DECISIONS.md#remaining-blockers-and-next-review-batch):
make missing-order versus stuck-action, missing-link versus missing-form, role/
retry and separate handoff/finish observations explicit, preserving the agreed
TC-006/009/027 targets and Q8 correction obligations. Review candidate fixture
versions and independent behavior/coverage criteria before implementation.
This recommendation is not a new approval of those open choices. Obtain relevant
policy/UI and reviewer evidence alongside that future review; formal sign-off,
implementation approval and execution authorization remain distinct.

## 8. Preservation and documentation verification

| Version / date | Record / scope |
|---|---|
| `OD004-RECENT-GUIDANCE-REVIEW-0.1` / 2026-11-03 | Static investigation, four restrictions, proposed Option B, original Q8 and independent impact/coverage proposals. Completed audit retained below as history. |
| `OD004-RECENT-GUIDANCE-REVIEW-0.2` / 2026-11-03 | Records the user's qualified Q8 approval, Agent-first limit, synchronized applicability/status and recommended next business-acceptance batch. Documentation/design agreement only. |

**Exact pre-Q8-approval snapshot:** [twelve-member v0.1 package](../../reference/UC4_Problem2_OD004_Recent_Guidance_Review_v0.1_2026-11-03.zip),
SHA-256 `dfc73a2217b69bc4106fc8bd27009c6844035febc50f34ed79ee81f568da7b41`.
It preserves all eleven Problem #2 Markdown documents plus the glossary before
this approval-recording edit. It is a local preservation artifact, not a policy
release or replacement for any earlier snapshot.

### Historical v0.1 preservation record

The following preservation narrative and audit describe the **completed v0.1
investigation**, before Q8 approval recording. Their counts and zero-new-approval
statement are historical, not claims about v0.2's agreement-recording work.

**Pre-task snapshot:** [completed OD004-OD005-REVIEW-0.2 package](../../reference/UC4_Problem2_OD004_OD005_Review_v0.2_2026-11-03.zip),
SHA-256 `a21fd2d7a1fe0f3ccab22e46e22269bed939181ce297c01cda7ae72ea41a0e2a`.
Its eleven repository-relative members preserve all ten Problem #2 documents plus
the glossary before this contract investigation. Earlier snapshots/fingerprints
retain their identities. This is a local preservation artifact, not a policy release.

The completed v0.2 approval report, Round 1/OD-002 records, BR register, pilots,
TC/BP classification and DF/DG mappings are retained byte-for-byte. Current-review
links/status are updated only in README, OPEN_DECISIONS and the worksheet. New
glossary terms distinguish guidance consent, accepted offers, checkpoint/step
completion and education delivery; all previous glossary bytes are preserved.

Static extraction and documentation-audit evidence is retained under
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-recent-guidance-contract-2026-11-03`:
`capture-before.py`, `preservation-before.json`, `guidance-chain-project.py`,
`guidance-chain-manifest.json`, line-labelled member projections,
`verify-documents.py`, `contract-review-documents.diff` and
`documentation-verification.json`. Exported code is read as text, never executed.

### Completed static audit — 2026-11-03

Executed from the repository root, using inert source extraction and documentation
checks only:

```powershell
.\.venv\Scripts\python.exe 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-recent-guidance-contract-2026-11-03\guidance-chain-project.py'
.\.venv\Scripts\python.exe 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-recent-guidance-contract-2026-11-03\verify-documents.py'
```

| Check | Result |
|---|---|
| Documentation | **PASS:** 11 Problem #2 documents, 144 relative links/anchors, registered ID references, table structure and new-whitespace checks; `git diff --check` passed. |
| Static sources | **PASS:** export authentication, 15 cited member fingerprints, original Job text hash, 13 exact Job-heading rows, six KB claim rows and 17 provisional article metadata records. Census: 31 node definitions, eight Code nodes; relevant chart edges/conditions/result shapes checked as data. |
| Original workbook | **PASS:** member fingerprint and 311 nonempty cached cells authenticated without recalculation; recent education/decline fixtures and TC-004/DF-018 mismatch retained. |
| Agreements and mappings | **PASS:** seven Problem #2 documents byte-identical, including completed v0.2 and earlier agreements, BR register, three pilots/18 registered variants, TC/BP and DF/DG records. No reclassification, new defect association or historical regrade. Original glossary bytes retained as a prefix. |
| Preservation boundary | **PASS:** eleven-member pre-task snapshot verified; four existing documentation files changed, one report and one preservation archive added. Other 175 captured repository files, 467 historical report files and six external sources unchanged; HEAD unchanged. |
| Authority and execution | Zero new approvals, runtime/Knowledge/runner/scenario changes, test executions, live requests or saved-evidence regrades. Exported code was not executed. Both verdicts remain **NOT_RUN**, full baseline **NOT FROZEN**. |

These checks establish source/document preservation and internal documentation
consistency. They are not evidence of Agent behavior, current UI acceptance or
audible education delivery.

### Q8 approval-recording audit — v0.2

The successor static audit is retained separately under
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-q8-agreement-2026-11-03`:
`capture-before.py`, `preservation-before.json`, `verify-documents.py`,
`q8-agreement-documents.diff` and `documentation-verification.json`.
The original v0.1 scripts, projections, diff and results are preserved unchanged.

Executed from the repository root on **2026-11-03**, static documentation/source
checks only:

```powershell
.\.venv\Scripts\python.exe 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-q8-agreement-2026-11-03\verify-documents.py'
```

| Check | Result |
|---|---|
| Approval and scope | **PASS:** one qualified internal Q8 design approval recorded, all seven qualifications quoted verbatim, source/date/authority limits explicit. Q1–Q7 and earlier agreements retain their scope; no formal approval recorded. |
| Documentation | **PASS:** 11 Problem #2 documents, 162 relative links/anchors, registered ID references, table structure and new-whitespace checks; `git diff --check` passed. |
| Static sources | **PASS:** unchanged full source-trace section; 15 cited member fingerprints, original Job text hash, 13 Job-heading rows, six KB claim rows and 17 provisional article metadata records reauthenticated. Original workbook hash and 311 nonempty cached values checked as inert data. |
| Requirements and history | **PASS:** 20 original BR rows and prior source/fingerprint rows preserved; complete three-pilot/18-variant, 15-TC/seven-BP and 18-DF/49-finding/nine-group history sections unchanged. The Round 1, OD-002 and Q1–Q7 approval documents remain byte-identical. Current applicability overlays are explicit. |
| Preservation | **PASS:** twelve-member pre-Q8 snapshot verified; original question/alternatives and v0.1 audit retained; all 44 prior audit files unchanged. Nine documentation files changed, one preservation archive added; other 172 captured repository files, 467 historical report files and six external sources unchanged. Original glossary bytes remain a prefix; HEAD unchanged. |
| Runtime and evidence boundary | No Cognigy, Agent Job, Tool, Code, KB, runner or scenario changes; zero test executions, live requests or saved-evidence regrades. Exported code was not executed. `behavior_verdict=NOT_RUN`; `coverage_verdict=NOT_RUN`; full baseline **NOT FROZEN**. |

This successor audit verifies approval-recording consistency and preservation;
it establishes no runtime conformance, authenticated UI acceptance or audible
delivery. The recommended next acceptance batch remains a recommendation.
