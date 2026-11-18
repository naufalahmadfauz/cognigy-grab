# OD-002 — compensation-status decision review

**OD002-REVIEW-0.2 · 2026-11-02 · Q1–Q4 VERIFIED [POC] / ENGINEERING_AGREED_POC.**

**Authority:** explicit approval by the requesting project-side user, recorded in
§7. All four choices are provisional internal POC engineering agreements. Formal
Grab policy/benchmark approval remains pending; the acceptance baseline is not frozen.

[Decision register](OPEN_DECISIONS.md) · [TC-003 pilot](JOURNEY_PILOT.md#jrn-tc-003) ·
[Requirements / source manifest](BASELINE_MODEL.md) ·
[Defect impact](DEFECT_GROUP_IMPACT_MATRIX.md)

## 1. Decision in brief and continuity

**Agreed internal direction:** choose the next action from the merchant's observed
compensation status **and remaining goal**. Preserve TC-003's full App submission
target; a correct already-approved answer does not complete that target.

- **A:** A visible relevant order with no compensation status, plus a retained
  request for review, supports the existing POC submission guidance. It does not
  establish rejection, eligibility or an entitlement to compensation.
- **B:** For reported `Auto approved` and a status-only goal, explain the reported
  approval and avoid an unnecessary new compensation request; address unresolved concerns.
- **C:** For reported `Auto approved` and missing money, explain approval versus
  regular payout versus bank receipt; retain the unpaid concern. A guaranteed
  payment date, new-claim remedy or escalation rule is not established.
- **D:** If the status cannot be identified, clarify the current screen/observation
  before selecting a submission branch. A missing order is not a blank status.

Q1–Q4 are **settled for this internal scope**. Q2/Q3 provisionally adopt narrow
no-unnecessary-request handling and approval-aware explanation priority. There is
no blanket rule that an approved order can never be disputed again. The unchanged
Job's generic non-arrival wording retains a source-applicability conflict; Q3
settles the internal acceptance priority, not runtime implementation or an
approved-payment remedy. See §3.

### Preserved agreements and source continuity

The v0.3 [engineering decision record](ENGINEERING_DECISIONS_2026-11-02.md) and
the user's Round 2 instruction establish these **VERIFIED [POC] internal
engineering agreements**, not formal Grab approvals. This preserves the record's
`ENGINEERING_AGREED_POC` / `PROCESS_AGREED_POC` scope:

| Decision | Preserved scope |
|---|---|
| OD-001 | TC-006's primary fixture declines the role retry; successful and failed accepted retries remain distinct variants. |
| OD-008 | TC-009 targets Portal submission only; no invented GrabFood Portal-status route. |
| OD-003 | TC-027 explicitly transitions from App selection to computer Portal before Portal status controls. |
| OD-015 | Internal POC review and acceptance governance; review does not authorize execution or formal Grab acceptance. |

**Input reconciliation completed:** the repository initially held five v0.1
drafts. The supplied [Engineering Review Pack v0.3](../../reference/UC4_Problem2_Engineering_Review_Pack_v0.3.zip)
was located, authenticated and read against them; its eight documents were
integrated before this review's focused amendments. The pack is a
`P2-ENG-DECISIONS-0.3` overlay on `P2-DRAFT-0.2`, not a frozen acceptance baseline.
Its README's older v0.2 title and pending-decision prompts are historical residue;
the explicit v0.3 agreement record takes precedence for internal fixture choices.
Existing BP-01–BP-07 classifications/mappings are retained. Original v0.1, supplied
v0.2 and supplied v0.3 bytes are preserved in the [version history](README.md#version-history-and-preservation).

The newly agreed OD-002 scope is recorded separately from those four preserved
agreements. It supports bounded internal fixture/branch interpretation; dependent
requirements and formal acceptance remain pending. `behavior_verdict=NOT_RUN`
and `coverage_verdict=NOT_RUN` throughout. No saved conversation is regraded.
Business Acceptance Baseline v1.0 is not declared complete.

## 2. Source-backed findings

Source keys and original archive paths/hashes are retained in
[BASELINE_MODEL.md](BASELINE_MODEL.md#sources-and-authority).
`WB:S` means **Scenarios**; `WB:D` means **Defect Log**. A cell extraction is a
documentary fact, not an approved policy. `VERIFIED [POC]` means an existing
source-backed internal POC rule; `PROPOSED` means this review still needs a
decision; `UNKNOWN` means missing policy/evidence; `CONFLICT` preserves incompatible
statements or an unresolved rule interaction.

### Original benchmark and decision records

| Source | What a reviewer needs to know | Authority / consequence |
|---|---|---|
| `WB:S!A6:F6` | TC-003 is GrabFood, beyond threshold/about two weeks, App, one-by-one, no loudspeaker. D6 includes status then App submission; F6 calls it the full App happy path. E6 supplies both goals upfront and ends with a merchant completion report. | Original intended coverage. E6 never supplies an explicit not-compensated status or an individual eligibility decision. Greeting text does not prove preparation. |
| `WB:S!E6` | The Agent describes auto-approved statuses, but the merchant only confirms order/details visibility before submission. There is **no literal merchant reply “Auto approved.”** Date selector is used even after order visibility. | Preserve the missing status observation and OD-007's conditional-recovery conflict. Do not manufacture a transcript or require unnecessary date recovery. |
| `WB:D!D21,G21(1)` / `DF-017/F01` | DF-017 is directly associated with **TC-003**. Tester says Auto approved needs no new Request for Compensation and the merchant waits for the next payout cycle; the reported script comparison includes the quoted Auto approved answer missing from E6. | Source feedback for the narrow no-unnecessary-request interpretation now agreed under Q2/Q3. The feedback itself is not independent policy approval or proof of an actual payment. |
| `WB:D!G21(2)` / `DF-017/F02` | Tester positively describes asking what the merchant sees and adapting the next step. | Positive evidence for observation-based behavior, not a complete TC pass. |
| `WB:D!G21(3)` / `DF-017/F03` | Spoken/displayed response divergence during barge-in is reported separately; disabling barge-in is the tester's suggested remedy. | Voice evidence/cause remains **UNKNOWN**, under OD-013 / BR-017 / DG-009. OD-002 does not establish or resolve that cause. |
| `WB:D!K21,M21` | Original status and retest-result cells are blank. | Retain blanks; do not turn DF-017 into Open, Closed or Pass. |
| `PB §4`, `PLAN §5/P079–098` | Both present the four status/goal branches as candidates needing approval. PB D-09 forbids inferred branches becoming policy; PB D-10 separates behavior from coverage. | Preserve those historical candidates. Q1–Q4 now supply bounded project-side agreement; formal policy remains pending. PLAN/PB `D-*` numbers are separately namespaced. |

### KB v0.3 article and claim evidence

Each article below is version **0.3.0**, `adoption=provisional_poc`,
`formal_approval=pending` in the inspected **KB30** export. Full article ID is
the chunk ID without its `-C01`/`-C02` suffix. Metadata, claim associations and text
were read from the export and compared with the previously inspected KB29 source:
all 17 articles' metadata and 20 chunks' text/claim associations match. This agrees
with H1 §§2–3; neither static comparison establishes today's served configuration.

| Chunk / exact claim IDs | Supported fact | Limit relevant to OD-002 |
|---|---|---|
| `UC4-MY-GF-STATUS-001-C01`; `UC4-MY-GF-CLAIM-005` | App → Orders → Cancelled → relevant order's displayed compensation status. Describes current-month cancellations/auto-approved status. **“An approved status is not proof that the bank received payment.”** | Missing order/link is not rejection. No complete status dictionary, universal duplicate-request prohibition or authenticated-screen validation. |
| `UC4-MY-GF-TIMING-001-C01`; `UC4-MY-GF-CLAIM-007` | Usual approval within **1–2 business days after the order was made**, followed by the next regular payout cycle, subject to policy. Approval, processing, payout cycle and bank receipt are separate stages. | Not an end-to-end SLA, a new clock starting at the status inquiry, or a bank-credit guarantee. |
| `UC4-MY-GF-SUBMIT-001-C01`; `UC4-MY-GF-CLAIM-012`, `UC4-MY-GF-CLAIM-013`, `UC4-MY-GF-CLAIM-014` | Relevant cancelled order → present Request for compensation link → Report a payment dispute → scroll/form → details/evidence → merchant submission. Missing App link has a Portal alternative. | A missing link proves neither ineligibility nor wrong role; current screens and early request acceptance are untested. A route's existence does not decide when an approved-payment dispute is warranted. |
| `UC4-MY-SHARED-REQUEST-001-C01`; `UC4-MY-SHARED-CLAIM-007` | Authorized Owner/Manager login is required to submit; the merchant completes/submits the form. | Form visibility/authenticated access untested. Does not require a fresh role interrogation or identical spoken reminder on every successful path. |
| `UC4-MY-GF-EVIDENCE-001-C01`; `UC4-MY-GF-CLAIM-009`, `UC4-MY-GF-CLAIM-010` | Prepared-food photo guidance; documented request may proceed without already having a photo with clear, complete supporting information. | No photo is not denial, exemption, proof of non-preparation or approval. Substitutes/final evidence policy remain **UNKNOWN**. |
| `UC4-MY-GF-EVIDENCE-001-C02`; `UC4-MY-GF-CLAIM-011` | Existing isolated-POC assumption treats cancellation before preparation as outside compensation. | Provisional scope assumption, not an individual eligibility determination. Do not infer preparation from a greeting, missing photo or status. |
| `UC4-MY-GF-THRESHOLD-001-C01`; `UC4-MY-GF-CLAIM-015`, `UC4-MY-GF-CLAIM-016` | Elapsed-day thresholds select recent/older conversation handling; older orders retain review guidance. | Not eligibility, a submission deadline or a payment date; operating timezone/effective-version conventions unconfirmed. |
| `UC4-MY-SHARED-DEADLINES-001-C01`; `UC4-MY-SHARED-CLAIM-008`, `UC4-MY-SHARED-CLAIM-010` | Older-order routing is distinct from the public 90-day enquiry reference. | UC4 applicability unresolved; no automatic rejection or indefinite submission right. |
| `UC4-MY-SHARED-DEADLINES-001-C02`; `UC4-MY-SHARED-CLAIM-008`, `UC4-MY-SHARED-CLAIM-009` | Indexed five-working-day investigation/response and at-least-three-business-day bank-credit/contact wording concerns different stages. | UC4 applicability **UNKNOWN**. Do not add these numbers to the approval period or invent a contact/escalation trigger for C. |
| `UC4-MY-SHARED-PORTAL-001-C01`; `UC4-MY-SHARED-CLAIM-011`, `UC4-MY-SHARED-CLAIM-012`, `UC4-MY-SHARED-CLAIM-013` | Documents payment-dispute destinations. Existing standard POC route is Help Centre → Search Bar → dispute → Report a payment dispute. | Alternate indexed menus are not newly accepted POC routes or proof of live UI. |
| `UC4-MY-GF-SPLIT-001-C01`; `UC4-MY-GF-CLAIM-001`, `UC4-MY-GF-CLAIM-002` | Eligible split-large-order cancellations have automatic reimbursement/no merchant action and weekly App-record updates in that specific FAQ. | **Not** a general no-action rule or weekly payment schedule for every cancelled/Auto approved order. TC-003 does not establish this split-order precondition. |
| `UC4-MY-SHARED-ELIGIBILITY-001-C01`; `UC4-MY-SHARED-CLAIM-006` | Cancellation reasons are examples subject to policy. | No exhaustive eligibility checklist or authority to declare this order eligible. |

H1 §§0,4–6 and KBC's “Remaining limits and sign-off conditions” preserve Problem
#1's closure: **17 article-level Top 1 observations** (15 Agent, two Search Only)
and 15 functional KB scenarios, one manually completed. These establish neither
formal policy approval, all-chunk coverage, actual backend status nor original
TC-003 completion.

## 3. Existing POC Job rules and the decision gap

**JOB30 / KB30:** `C:\Users\Nau\Downloads\Package-Naufal_2026-10-30_06-38-33.zip`,
SHA-256 `e92afdf8d41c5a348e65e18e0a1cad77f827d26dab5c6d3fe136d3439c1a8a1f`,
matches H1's last verified export. Job member
`nodeData/6ae43b6f90878ce305636d97`, JSON pointer
`/localizedData/0/config/instructions`, has instructions UTF-8 SHA-256
`d89731bb49f09959e0c9c35550cb0b9fa71fa03a88295916887672c20390d860`.
KB article/chunk content comes from its `knowledgeSource/*` / `knowledgeChunk/*`.

Compared by heading with [JOB29](../../flow/poc-correction-2026-10-29/01-job-instructions.txt),
39 of 42 sections are unchanged after whitespace normalization. The three changed
sections, read in full, contain the H1-approved additions for current-order LOB
recognition (`MERCHANT CONTEXT`), provisional preparation/packing explanations
(`KNOWLEDGE`) and all-at-once form observation (`REQUEST FOR COMPENSATION —
GRABMERCHANT APP`). This table cites **JOB30** throughout. It is a verified
historical POC reference, not evidence of today's served binding; its ZIP excludes
the Endpoint and `[MAIN]`.

| Exact Job section | Existing source-backed POC rule | OD-002 implication |
|---|---|---|
| `STATUS AND SUBMISSION TOGETHER` | Dual goals remain active; status first; wait for observed status; submission second **only if still needed**. Submit-only does not require status first. | **VERIFIED [POC]** ordering. “Only if needed” does not itself define every approved-status outcome. Preserve OD-008's negative control. |
| `GRABFOOD APP — COMPENSATION STATUS` | Separates missing order from visible order/blank status. For the latter, status check is complete and an already-requested submission continues without re-asking the goal. History/date recovery is only for a missing order. | **VERIFIED [POC]** support for A's visible-blank continuation, not evidence of individual eligibility or support for “no observation → claim.” |
| `OLDER CANCELLED ORDER`; `STATUS AND SUBMISSION TOGETHER` | Upfront explicit dual guidance goes directly to missing preferences; no unsolicited timeline/re-offer. General status/dual intent supplied in response to the older-order open question gets the fixed GF timeline, existing-photo reminder and guidance offer; wait for acceptance. | TC-003 E6 uses the upfront-dual profile. This limited OD-004 dependency can use the existing rule without settling all education triggers. |
| `FIXED LOB TIMELINES`; `FOLLOW-UP` | When a timeline is needed, preserve the exact GF approval-plus-payout sentence. Generic non-arrival follow-up explains the request option and offers cancelled-order guidance. | **Source-applicability CONFLICT retained:** the inspected Job contains no explicit approved-but-unpaid exception. Q3 now establishes **VERIFIED [POC]** explanation/clarification priority for internal acceptance; the Job is unchanged and runtime conformance unverified. Payment remedies still require owner policy. |
| `REQUEST FOR COMPENSATION — GRABMERCHANT APP`; `POST-SUBMISSION RESPONSE CONSTRAINTS` | Article/scroll → observed form → details/evidence/self-submission → merchant submission report → conditional acknowledgement. Form visibility is not submission or eligibility. | **VERIFIED [POC]** procedural controls for A; no backend confirmation or promised result date. |
| `APP REQUEST LINK MISSING — PORTAL FALLBACK`; `FORM NOT VISIBLE — ROLE ACCESS AND ONE RETRY`; `CONNECTION AFTER FAILED FORM RETRY` | Missing link and missing form have different preconditions. Role confirmation, one retry offer, later retry consent, attempt/result, then any authorized person offer/consent are separate. | **VERIFIED [POC]** conditional recovery. A fallback/recovery cannot count as TC-003's normal full-App fixture merely because it is handled correctly. |
| `GROUNDING`; `OUT OF SCOPE`; `CLOSING` | No invented policy, outcome, callback or date. Cancelled-order payout concerns remain in scope. Normal close needs an appropriate finish signal. | B/C/D cannot use unknown status, the word payout, or a missing payment to manufacture a transfer. A conversation may finish while the financial outcome remains unverified. |

**Agreed priority, VERIFIED [POC] (Q3):** once a reported compensation status is
available, use that status and the remaining goal before applying generic
non-arrival/request-option wording. For approved/non-arrival, explain the supported
stages and acknowledge the limit of available order-specific payout information;
do not automatically issue a second request or borrow role-failure/out-of-scope
handoff authority. This is a provisional internal acceptance direction. The
unchanged Job-source conflict remains visible, implementation is unverified, and
business escalation policy remains unknown.

## 4. Four-branch decision and acceptance model

### Observation rules and shared prerequisites

Reuse `JRN-TC-003/M01–M10`; the letters below are this review's situation labels,
**not replacements for VAR suffixes**. A is the original target; B is
`VAR-TC-003-A`; C is `VAR-TC-003-B`; D is `VAR-TC-003-C` (PB §4).

Before selecting a branch, retain current-order identity/GrabFood, the merchant's
goal and already-known preferences (M01/M03; BR-001/005). Use the supported App
status route and required observations when navigation is needed (M04/M05;
BR-006/007/009). Do not ask for order IDs or credentials in chat; guiding the
merchant to their order/form does not authorize collecting its contents.

- **Visible order + explicitly blank/not-shown compensation status** is an
  observation supporting A under the POC rule. **No observation yet** belongs to D.
- **“Not compensated”** must be clarified if it could mean only “money has not
  arrived.” It is not assumed to be an exact documented screen label or rejection.
- **Missing order** invokes the existing conditional History/date/Confirm recovery
  (`VAR-TC-003-D`); observe the order/status afterward. Do not skip to submission.
- **Auto approved + bank non-receipt** is not inherently contradictory; it is C.
  Ambiguous order identity or contradictory *compensation-status reports* is D.
- A known pending/rejected/other unreviewed status is not silently folded into A
  or B. Its disposition remains **UNKNOWN** until its semantics are sourced.

If status is already clearly reported, reuse it for the behavioral decision. A run
that skips the target's required navigation may still lack original-target
coverage. Status comes from the merchant, not an Agent backend lookup.

### Source-backed decision table

| Situation / retained ID | Expected behavior and mandatory milestones | Forbidden actions | Source / approval status |
|---|---|---|---|
| **A — visible order, no compensation shown; wants review** / TC-003 target | M01/M03–M06: establish the actual visible-order/status observation and retain the requested review. M02 only for its applicable entry trigger. Then M07: relevant details → present App request link → article → scroll → observed form. M08: appropriate order details/evidence and merchant self-submission, one action/wait at a time. M09: obtain submission report and conditional acknowledgement. M10: further help/appropriate finish. Apply form-access constraints only where relevant. | No status absence ⇒ rejection/eligibility/mandatory claim; no submission before observations; no assumed preparation; no missing-photo denial; no forced History when order visible; no backend submission/approval claim. Do not repeat an already-clear submission request. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q1)** visible-blank review-request fixture; dependent acceptance remains pending. JOB30 GF status/request sections; GF-005/012/013/014; SHARED-007; GF-009/010/011 support the controls. PB's candidate eligibility-certified meaning remains **UNKNOWN** beyond the scoped review process. |
| **B — Auto approved; status inquiry only** / `VAR-TC-003-A` | M05/M06: confirm/reuse the compensation label on the relevant order and the status-only goal. Explain it as the merchant-reported approval indication; distinguish bank receipt. Do not initiate another request solely to obtain the same approval. M10: further help/finish only when appropriate. If the merchant still wants a dispute or reports unpaid funds, retain that concern and clarify/change branch. | No “money deposited,” guaranteed award/date, Agent-verified backend claim, automatic close, or universal ban on future disputes. Do not discard a previously pending submission goal without establishing that status confirmation now satisfies it. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q2, provisional)** narrow no-unnecessary-request decision: WB:D!G21(1), PB §4, PLAN P088–090; GF-005/007 support approval/receipt distinction. Formal `Auto approved` semantics and universal duplicate/dispute rules remain **UNKNOWN**. |
| **C — Auto approved; payment not received** / `VAR-TC-003-B` | M05/M06: reuse approval report and explicit unpaid goal. Explain the distinct stages and qualified usual approval/regular-payout reference when timing is asked; do not restart approval time from today. Ask only a genuinely missing, relevant question about what the merchant sees or what remains unanswered. State that order-specific payout/bank detail is unavailable when it is. Continue only supported guidance, preserving the unresolved financial concern. M10 permits an explicit finish, not a claim of financial resolution. | No 1–2-day bank guarantee, accumulated 1–2 + 5 + 3 SLA, arbitrary wait/contact threshold, fabricated payout/adjustment screens, automatic duplicate claim, out-of-scope dismissal, automatic transfer, callback or promised investigation. Approval does not negate non-receipt. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q3, provisional)** bounded explanation/clarification and status-aware priority over generic FOLLOW-UP; GF-005/007 and JOB30 grounding support the stage limits. Job-source applicability **CONFLICT** retained; a concrete overdue-payment remedy, authorized payout-dispute submission or escalation remains **UNKNOWN / blocking** under OD-014. |
| **D — unclear/inconsistent status** / `VAR-TC-003-C` | M05 remains unresolved. Ask one targeted clarification and wait: first order visibility if unknown; otherwise the actual compensation label or the specific inconsistency. Use only supported navigation from confirmed location. Once clarified, select A/B/C or retain an unsupported-status limitation. If still unclear, defer status-conditioned submission, explain the limit and preserve the open goal. | No guessing approved/rejected, no treating “order visible” as “approved,” no treating “cannot read” as blank, no repeated generic intake, no forced submission/transfer/claimed success. No indefinite invented recovery ladder. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q4)** clarify before status-dependent submission: JOB30 grounding/GF status, GF-005, PB §4, PLAN P094–096. Unresolved status meanings and further recovery remain **UNKNOWN**. |

The abbreviated claim references in that table expand to the exact IDs in §2.
Guidance consent, existing one-by-one pacing and separate observations remain
required. An action acknowledgement confirms only the action just requested.

### A's primary fixture and eligibility/access boundary

Under Q1's internal agreement, retain **beyond-threshold, upfront dual request,
App, one-by-one, no loudspeaker** from E6. Make these previously implicit branch-driving
facts explicit: relevant order visible; compensation status blank/not shown;
review still requested; App request link present; article reached and scrolled;
form visible; merchant reports completing submission, then finishes.

The agreed controlled POC fixture establishes an in-scope prepared-food order and
authorized Owner/Manager access as supplied merchant facts, not Agent inference
or authenticated validation. These are **internal fixture clarifications**, not
claims that E6 already contains them or new mandatory interview questions for all
callers. Reuse known facts; do not add a role retry to a form-visible happy path.
Universal spoken-role reminder timing stays under OD-010.

PB §4/PLAN P085's candidate says “eligible.” The inspected sources supply a
review/request procedure, provisional preparation scope and illustrative eligibility
examples, but no complete order-specific eligibility determination mechanism.
**Agreed Q1 scope, VERIFIED [POC]:** evaluate A as *guidance to request review
without asserting entitlement, automatic approval or guaranteed compensation*.
A mandatory eligibility-certified submission target remains
**BLOCKED_SPEC** until an owner supplies that policy/check. Known contrary scope
facts must not be ignored, but absent evidence is not a newly invented denial rule.

Form access is an operational prerequisite to form completion, not proof of
eligibility. Article/scroll and visibility must be established before instructing
completion. If the link is missing, use `VAR-TC-003-E`'s accepted Portal fallback;
if the form is absent, use `VAR-TC-003-F`/JRN-TC-006's conditional role recovery.
Keep the agreed TC-006 declined-retry target intact.

### Two independent acceptance verdicts

These are **future adjudication criteria**, not test results. Q1–Q4 no longer block
their bounded internal judgments for lack of a project-side answer. An unresolved
dependent requirement, formal-policy claim or unsupported outcome still yields
`BLOCKED_SPEC`/`NEEDS_REVIEW` for the affected judgment; independently established
violations must still be recorded. Both recorded verdicts remain `NOT_RUN`.

| Branch | Behavior criterion within the agreed internal scope | Original TC-003 submission coverage |
|---|---|---|
| A | Applicable M01–M10 and branch conditions met; correct entry-specific education, observation gates, pacing, access/evidence/self-submission and conditional acknowledgement; no unsupported claim. | **Potential PASS only with evidence of the full target fixture and stages.** A chosen branch, visible form, or submission instruction alone is insufficient. Correct decline/access recovery/Portal fallback does not prove the normal full-App target. |
| B | Correctly attribute approval to the displayed report; satisfy status-only goal without unnecessary new request; no bank claim; retain any changed/unresolved goal and finish appropriately. | **INCOMPLETE_COVERAGE** for original TC-003 even if behavior is PASS. The separately targeted B variant can have its own coverage PASS. |
| C | Correct stage explanation, preserved unpaid concern, justified clarification and explicit information limit; no invented remedy. Q3 permits this bounded explanatory outcome for internal acceptance, subject to applicable dependent requirements. | **INCOMPLETE_COVERAGE** for TC-003. Complete financial-resolution behavior remains **BLOCKED_SPEC** if the target requires an unsupported overdue-payment remedy; do not call explanatory success “payment resolved.” |
| D | Relevant clarification with wait; no fabricated status/submission; appropriate supported recovery or explicit unresolved outcome. | **INCOMPLETE_COVERAGE / NEEDS_REVIEW** while target stages are absent/uncertain. If later clarification genuinely establishes A and all target milestones occur, assess that observed continuation; D alone never supplies missing stages. |

Coverage and behavior are independent: fully traversing A with a false payment
promise can yield `FAIL / PASS`; handling B correctly can yield
`PASS / INCOMPLETE_COVERAGE`. Preserve fixture/requirement version, observed branch,
milestone evidence, merchant-reported versus independently confirmed facts, channel
and reviewer on both axes (BASELINE_MODEL, “Two independent verdicts”). Text-only
evidence cannot establish audible completeness for DF-017/F03.

## 5. Limited dependency disposition

Here **resolved** means sufficient for the stated internal POC sub-question,
**conditionally supported** means usable with explicit applicability/limits, and
**blocking** means the specified judgment/outcome cannot be authorized from the
available evidence. These dependency dispositions do not close the whole OD.

| Dependency | Disposition for OD-002 | Supported boundary and remaining approval |
|---|---|---|
| **OD-004 — education applicability** | **Conditionally supported**; the TC-003 upfront-dual versus older-open-question distinction is **resolved for the documented POC profile**. | JOB30 explicitly supplies both triggers (§3). For E6's upfront dual goal, do not add unsolicited education/re-offer; for an older-order open-question answer, education/photo reminder/offer precede accepted guidance. B/C factual timing answers do not force a new intake. Broader education table remains **CONFLICT**; preserve DF-018's owner-reported closure and its original/fix-note mismatch. |
| **OD-005 — timing and age** | **Conditionally supported**; approval ≠ bank receipt is **resolved [POC]**. A precise payment deadline or overdue trigger is **blocking**. | GF-007 plus the fixed Job sentence supports usual business-day approval after order made, then regular payout. Routing uses cancellation age/elapsed-day thresholds, not that approval interval. TC-003's beyond-threshold fixture does not require inventing timezone/boundary arithmetic. Do not reinterpret “two weeks” as proof of unpaid status or eligibility; exact date conventions/formal timing policy remain **UNKNOWN/CONFLICT**. |
| **OD-010 — form and role** | **Conditionally supported** for A; not a prerequisite to B/C/D explanation. | SHARED-007 and Job recovery provide authorized role, article/scroll, visibility, one separately accepted retry and outcome. Universal successful-path spoken reminder, unavailable-role disposition and authenticated UI remain **UNKNOWN**. They do not justify a blanket block on navigation or a fabricated role check. A known access problem blocks form completion until supported recovery succeeds. |
| **OD-014 — policy/UI unknowns** | **Blocking** for formal status/duplicate policy, authenticated UI assurance and C's end-to-end remedy; bounded Q1–Q4 internal handling is now **agreed**, with these limits. | No supplied policy establishes every status meaning, approved-payment dispute trigger, payout-screen route, escalation SLA, early acceptance or definitive individual eligibility. Q3 resolves internal explanation priority only. Preserve the scoped KB assumptions and test-fixture observations; a hypothetical screen or successful retrieval cannot resolve this dependency. |

OD-007's conditional History/date issue and OD-013's separate voice evidence remain
existing adjacent items, not expanded reviews. No dependency change reopens
OD-001/003/008/015 or the scoped Problem #1 closure.

## 6. Shared impact and proposed regression scope

**Directly documented** means the cited source explicitly supplies the association
or shared journey segment. **Plausible regression impact** means the same
requirement/boundary could be affected. **Unverified** means the status semantics,
failure, family mapping or common cause is not established. No selection is a
new failure report or permission to execute tests.

### Existing journeys and requirement boundaries

| Existing journey / variant | Association and confidence | Proposed regression reason / limit |
|---|---|---|
| `JRN-TC-003`; `VAR-TC-003-A/B/C` | **Direct:** WB:S!A6:F6, WB:D!D21/G21, PB §4; primary OD-002 subject. | Preserve A target plus B/C/D independent behavior/coverage. BR-001/003/006/007/009/010/012/013/014/020. |
| `VAR-TC-003-D/E/F` | **Direct register relationship** to JRN-TC-003; new failures unverified. | Order missing versus visible blank; absent link versus absent form; accepted fallback/retry must not bypass status/visibility or become original happy-path coverage. |
| `JRN-TC-005` / TC-005 | **Direct shared segment:** WB:S!D8:F8 documents status then submission, with no-status answer. **Plausible** changed-rule regression. | All-at-once must stop at status and form observations; retain pending submission. BR-006/007/009/010/012/013. No direct DF-017 association. |
| `JRN-TC-006`, `JRN-TC-007`, `JRN-TC-008` | **Direct shared segments:** WB:S!D9:F11 contains status before form recovery, stuck-step continuation or App-link fallback. **Plausible** upstream gate impact. | Ensure legitimate A reaches each distinct target; B/C/D must not be forced into a form to satisfy that target. Preserve TC-006 decline primary, TC-007's unresolved stuck fixture and TC-008's accepted Portal fallback. BR-007/009/010/012/014/015/019. |
| `JRN-TC-027`, `JRN-TC-029`; `VAR-TC-027-B` | **Direct shared structure:** WB:S!D16:F16,D18:F18; existing pilot's approved/compensated variant. **Plausible** cross-LOB status/goal and coverage impact. | Retain OD-003's App-to-Portal transition and GM-specific route/timing. KB `UC4-MY-GM-STATUS-001-C01` claims `UC4-MY-GM-CLAIM-003` and `UC4-MY-GM-CLAIM-004`, and `UC4-MY-GM-TIMING-001-C01` claim `UC4-MY-GM-CLAIM-006` support the GM boundaries. Exact GF `Auto approved` semantics applied to GM remain **unverified**, not approved by analogy. BR-008/009/011/013/018. |
| `JRN-TC-009`; `VAR-TC-027-G` | **Direct existing submit-only boundary**, reaffirmed by OD-008 / Job. **Plausible negative-control impact** if status-first is overgeneralized. | No new compulsory status detour for submit-only. Preserve Portal submission-only TC-009 and GM App submit-only support. |
| `JRN-TC-002/004/026/028`; `VAR-TC-027-F` | **Direct education/non-arrival or status-only descriptions** in inventory; **plausible** clarification/timing/finish impact. | Do not force submission into education-only, declined-guidance or direct navigation-only cases. Preserve the narrow GM status-only intake exception; do not extend it to GF/combined journeys by analogy. BR-001/003/014. |
| `JRN-TC-001/025`; `JRN-TC-010` | Shared timing or scope **negative controls**, not direct status-decision failures. | GF/GM recent education retains its own triggers. TC-010 remains genuine out-of-scope handoff; cancelled-order non-receipt must not be misclassified as unrelated payout. BR-003/015/016. |

Slash-separated journey/claim numbers retain their full prefix. The table reuses
existing inventory and pilot records; it does not expand the other 12 journey
specifications or redefine their primary classifications.

### Existing business-process families

Use the unchanged v0.3 [BP register and TC matrix](TC_CLASSIFICATION_MATRIX.md#candidate-shared-business-process-families-bp).
These families/memberships remain **PROPOSED taxonomy**, even though their presence
in the source pack is directly verified. This impact overlay adds no memberships.

| Existing BP / exact family name | Existing mapped journeys relevant here | OD-002 relationship and regression confidence |
|---|---|---|
| **BP-04 — Compensation status and conditional submission decision** | Primary TC-003/005/027/029; secondary TC-007. | **Direct core process association** through BR-006/007/008/009. Status/goal branching and separate coverage are primary review scope. Wider regression effect is **plausible**, not a reported failure of all members. |
| **BP-05 — Request/form submission and role access** | Primary TC-006/009; secondary/conditional TC-003/005/007/008/027/029 in the existing TC matrix. | **Direct downstream process association** for A; BR-010/011/012/013. **Plausible** reachability/overapplication impact. TC-009 is the agreed submit-only negative control, not an added status-first case. |
| **BP-06 — Navigation recovery, missing-link fallback and platform transition** | Primary TC-007/008; conditional TC-003/006/027. | **Direct conditional process association** for distinguishing missing order/status/link/form. **Plausible** BR-005/006/007/008/010/019 impact; preserve TC-027's agreed readiness transition. |
| **BP-02 — Recent follow-up and guidance declined** | TC-002/026; BP-01 prerequisite. | **Plausible shared follow-up impact** when qualifying generic non-arrival advice. Original declined-guidance targets remain intact; no claim they reported Auto approved or need new expanded variants. |
| **BP-03 — Older-order inquiry and education** | TC-004/028. | **Plausible** OD-004/005 timing/intent-trigger impact; preserve information-only targets. This does not move TC-003 into BP-03 merely because conditional education can apply. |
| **BP-07 — In-scope recovery boundary, out-of-scope handling and consented handoff** | Primary TC-010; secondary TC-009; conditional TC-006/027. | **Plausible negative-control/conditional impact** on BR-014/015/016. Unpaid compensation is not automatically out of scope. B/C/D ordinary finishing does not create BP-07 membership for TC-003 or authorize transfer. |
| **BP-01 — Recent cancellation education** | TC-001/025; prerequisite for TC-002/026. | **Plausible timing/education negative control** if shared wording changes later. A direct OD-002 status-branch failure association is **unverified**. |

BR-017 remains `QA_EVIDENCE` and BR-020 `QA_SEMANTIC_ACCEPTANCE` under v0.3;
they govern evidence/adjudication, not merchant-facing lines or extra process
families. No BP or DG is treated as a demonstrated implementation root cause.

### Existing defect groups and atomic evidence

| Group | Direct evidence versus plausible impact |
|---|---|
| **DG-006 — status-conditioned submission/fallback** | **Direct:** DF-017/F01 (policy/script concern) and F02 (positive adaptive guidance), linked to TC-003. DF-009/F04–F05 reports a further-help question after no status, then submission continuation after an explicit request on **TC-007**. Whether that earlier question was premature needs evidence; this is not another DF-017 association. DF-008/016 memberships retain their own observations/statuses. Shared-rule regressions are **plausible**, common cause **unverified**. |
| **DG-004 — status route/observations/pacing** | **Direct:** DF-017/F02 positive adaptation; DF-004/F01 reports date-instruction omission on TC-003. Applicability of that omission depends on the missing-order condition. Other route reports/controls are **plausible** regression scope; status policy does not prove a navigation failure. |
| **DG-002 — context and pending intent** | TC-003's DF-003/F03 is directly recorded but concerns the “phone issue” framing; it does not prove an approved-status error. Preserving dual goals and clarifying status versus payment has **plausible** BR-001 impact. |
| **DG-003 — education/timing** | Shared BR-003 impact is **plausible**. DF-018 directly belongs to **TC-004**, even though G22 compares TC003 scripts. Preserve DF-014/018 owner-reported resolutions; no blanket reopening. |
| **DG-005 — role/access** | TC-003's DF-003/F01 and DF-004/F02 directly report role-advice concerns; their universal-reminder applicability remains OD-010. A's downstream form stages have **plausible** impact; B/C/D do not automatically require form-role advice. |
| **DG-007 — unresolved goals/consent/closing** | DF-003/F02–F03 is direct TC-003 recovery/offer evidence. Premature closing of C/D and inappropriate handoff have **plausible** shared impact, not a proven recurring cause. |
| **DG-009 — voice continuity** | **Direct but separate:** DF-017/F03 ↔ TC-003 ↔ BR-017. Voice regression is relevant to audible observation/education; linkage of barge-in to the status decision's cause is **unverified**. No barge-in setting change follows. |
| **DG-001 / DG-008** | No direct OD-002 defect finding established. Greeting and GM once-only partial notice are boundary controls if adjacent guidance changes later; a shared failure or causal dependency is **unverified**. |

For a future authorized regression, select A/B/C/D first, then the existing
one-by-one/all-at-once, recovery and submit-only controls above. Record which
boundary motivated each selection. Preserve original fixtures and known closures;
use OD-015 governance for scope, reviewers and separate execution authorization.
Neither retrieval smoke results nor DF-016's positive TC-029 comment replaces this
coverage. No repeat count or new scenario is prescribed in this round.

## 7. Review frontier and adoption limits

| Adoption boundary | Recorded disposition |
|---|---|
| Existing POC controls | Retain status observation, goal retention, approval/receipt distinction, supported request/access sequencing and bounded education triggers as **VERIFIED [POC]**. They still do not certify official policy or live UI. |
| Internal OD-002 interpretation | Q1–Q4 below are **VERIFIED [POC] / ENGINEERING_AGREED_POC**, provisionally agreed by the requesting project-side user on 2026-11-02. They permit bounded review guidance/explanation; dependent acceptance remains separately scoped. |
| Formal business-policy approval | Still required for authoritative status meanings, universal duplicate/dispute rules, individual eligibility certification and an approved-but-unpaid remedy/trigger. These remain **UNKNOWN**. Generic-follow-up wording remains a Job-source **CONFLICT**, while internal explanation priority is settled by Q3. |
| Authenticated UI / backend assurance | Still requires independent evidence. Neither a fixture assertion nor KB retrieval establishes live form acceptance, approval, payout or bank receipt. |

### Recorded Q1–Q4 approval and provenance

**Decision date / recorded date:** 2026-11-02. **Approving party:** the requesting
project-side user in this conversation. Their personal name, official Grab role
and formal business/benchmark or QA sign-off authority were not supplied.
**Preparer/recorder:** AI assistant; not the approving party.

**Primary approval source:** the user's reply to the delivered `OD002-REVIEW-0.1`
review and its four questions, beginning:

> I agree with all four OD-002 recommendations (Q1–Q4) as **provisional internal POC engineering decisions**.

The same message expressly limits the authority:

> These are internal engineering agreements, **not formal Grab policy approval**. Keep unresolved policy semantics and payment remedies explicitly flagged.

The selections below record that message; they are answered decisions, not a new
approval request. All four remain provisional at the overall internal POC level,
including Q1/Q4 whose individual answer was “Approved.”

| Question / retained branch | User's selection and agreed scope | Outstanding dependency / limit |
|---|---|---|
| **Q1 / A — TC-003 target** | **Approved:** visible-blank-status review-request fixture; preserve merchant intention and applicable submission prerequisites. No assertion of eligibility, automatic approval or guaranteed compensation. | Full App status/submission milestones remain required. PB's candidate “eligible” becomes a request-for-review target only for this internal scope; individual eligibility, authenticated acceptance and dependent OD-004/005/007/010/014 requirements remain qualified. |
| **Q2 / B — VAR-TC-003-A** | **Approved provisionally:** when the merchant reports Auto approved and only wants status confirmation, explain the reported approval and avoid unnecessary duplicate submission; address unresolved concerns. | Canonical status semantics and universal duplicate/dispute policy remain unknown. No backend verification, bank receipt or blanket ban on later disputes is inferred. |
| **Q3 / C — VAR-TC-003-B** | **Approved provisionally:** when Auto approved is reported but payment has not arrived, distinguish approval, payout and bank receipt; prioritize explanation and clarification. No invented escalation remedies, payout dates or payment guarantees. | Internal priority over generic non-arrival request guidance is settled. Job-source wording is unchanged; remedy, approved-payment dispute/contact/escalation trigger and end-to-end financial resolution remain blocked under OD-005/014. |
| **Q4 / D — VAR-TC-003-C** | **Approved:** clarify the observed compensation status before choosing a status-dependent submission branch. | Keep unread status, missing order and visible blank distinct. Unsupported status meanings/recovery remain unknown; D supplies original coverage only if later clarification establishes A and all target stages are exercised. |

**Coverage agreement:** correct B/C handling remains distinct from original
TC-003 submission coverage. The two verdict axes in §4 remain independent; neither
an internal agreement nor a future correct alternative supplies missing target
evidence. Current behavior and coverage verdicts remain `NOT_RUN`.

**Rationale / source grounding:** §2's original WB/PB/PLAN and KB30 claim locators,
§3's JOB30 rules/conflict, and §5's limited dependencies are retained. The user's
approval supplies internal decision authority; the cited sources supply the
factual basis and limits. No new formal policy source has been supplied.

**Affected record version:** `OD002-REVIEW-0.2` is the scoped decision overlay on
`P2-DRAFT-0.2` / `P2-ENG-DECISIONS-0.3`: BR-009's GF status/goal interpretation;
JRN-TC-003's target fixture and M05/M06 decisions; VAR-TC-003-A/B/C's bounded
handling and independent coverage criteria. Related BR-001/003/006/007/010/012/013/014/020
retain their existing controls/dependencies; they are not approved wholesale.
GM alternatives, other variants and BP/DG mappings retain their prior review status.
OD-001/003/008/015 remain in force in the unchanged Round 1 record.

**Superseded wording:** v0.1's unanswered Q1–Q4, “PROPOSED” internal A/B/C/D
choices and pending internal explanation-priority decision are superseded within
this scope. Original source conflicts, unknown policy and dependent acceptance
are retained. The exact pre-approval nine-document state is archived in §8.

### Later decisions and owner evidence

The next frontier is the remaining dependencies. Business/policy owners still need to
supply the canonical status meanings, any duplicate/approved-payment dispute
exception, the eligibility rule if an eligibility-certified target is required,
and any overdue-payout check/contact/escalation route with its trigger and timing.
UI owners must validate current authenticated routes/access independently.
OD-004/005/010 remain separately scoped review work; this document does not settle
their complete trigger, date or reminder policies.

**Recommended next batch:** OD-004 education/intent triggers together with OD-005
stage-specific timing and date interpretation. Produce one source-qualified
trigger table and a date/stage convention sheet, preserving agreed direct-intent
exceptions and OD-002's approval-aware boundary. Seek OD-014 owner evidence for
status meanings and approved-but-unpaid remedies alongside that review; lack of
that evidence does not reopen Q1–Q4. The [decision register](OPEN_DECISIONS.md#remaining-blockers-and-next-review-batch)
lists the remaining blockers and later batches. Named business/benchmark and QA
appointments remain pending under OD-015. Implementation, new executions,
official acceptance and release remain separate later decisions; no full baseline
freeze is authorized here.

## 8. Version and verification record

| Version / date | Change and authority |
|---|---|
| `P2-DRAFT-0.1` / 2026-11-02 | Initial five local documents preserved byte-for-byte in the local-draft history ZIP. |
| `P2-DRAFT-0.2` / 2026-11-02 | Supplied structural pack introduced BP-01–BP-07, requirement kinds and BR-led regression selection; preserved unchanged. |
| `P2-ENG-DECISIONS-0.3` / 2026-11-02 | Supplied eight-document engineering pack read and integrated byte-identically before focused amendments. Preserves four limited agreements; classification and defect matrix are identical to the supplied v0.2 members. Immutable source archive retained. |
| `OD002-REVIEW-0.1` / 2026-11-02 | Additive A/B/C/D review, limited dependencies, independent acceptance/coverage, existing-family impact and unanswered frontier. Focused cross-reference/current-status corrections; four agreements preserved; new interpretations **PROPOSED**. No global acceptance-version freeze. |
| `OD002-REVIEW-0.2` / 2026-11-02 | Records the requesting project-side user's explicit Q1–Q4 approval as **VERIFIED [POC] / ENGINEERING_AGREED_POC**; synchronizes BR-009, JRN-TC-003/VAR-TC-003-A/B/C and linked current-state records. Original conflicts, formal policy/UI limits, independent verdicts and prior agreements retained. Full acceptance baseline remains unfrozen. |

**Pre-approval preservation:** [OD002-REVIEW-0.1 nine-document snapshot](../../reference/UC4_Problem2_OD002_Review_v0.1_2026-11-02.zip),
SHA-256 `9e34da889adf7847a6d519bf75dd60a7a6e900767876a3a9d8c53da298dd595e`.
Created from the current documents before recording this approval; it is local
version history, not a new externally supplied release. It preserves the exact
questions, recommendations, source analysis and previous audit record.

**Historical v0.1 audit, completed offline on 2026-11-02 — documentation/source only:**

- All **76 relative links/heading anchors** across nine Problem #2 documents and
  the glossary resolve; Markdown table structure and stable-ID references pass.
- **15 original TC inventory/direct-DF mappings, 18 historical DF records and
  49 atomic records** are retained; nine group memberships/direct-TC unions agree.
  All **seven BP definitions and 15 TC-family memberships** match the supplied
  v0.3 pack. Three pilots, 18 existing variants, 20 BRs and 15 OD IDs are retained.
- **12 claim-table rows** match KB30's exact chunk/claim associations. All 17
  article metadata and 20 chunk text/claim records match the prior KB source;
  39 Job sections match after whitespace normalization, and the three changed
  sections contain the handover-documented additions. **15 source/archive/member
  or instruction fingerprints** checked, including the original workbook.
- The five original local drafts are preserved byte-for-byte in the v0.1 snapshot;
  the supplied v0.2/v0.3 archives and v0.3 four-decision record are unchanged.
  **160 other pre-existing repository files and 467 historical report files** are
  unchanged. The previous glossary is an unchanged prefix with appended terms.
- `git diff --check` passed. **Zero new Agent/runner test executions, live requests,
  saved-evidence regrades or new business approvals.** These checks verify source
  accounting and documentation, not runtime behavior or a business baseline.

Read-only projections, the audit script/result and source comparisons are retained
at `C:\Users\Nau\AppData\Local\Temp\opencode\uc4-od002-review-qfm819b3`:
`preservation-before.json`, `v03/`, `v01-to-v03.diff`, `job30.txt`,
`job29-to-job30.diff`, `kb30-projection.json`, `audit-od002-documents.py` and
`documentation-verification.json`. The original archives and cited hashes remain
the primary provenance; these are offline review artifacts, not conversation runs.

### OD002-REVIEW-0.2 approval-recording audit

**Completed offline on 2026-11-02 — documentation/source/preservation checks only:**

- **87 relative links/heading anchors** across the nine Problem #2 documents and
  glossary resolve. Markdown tables, stable IDs, the four recorded selections and
  their preserved A/B/C/D-to-target/variant identities pass consistency checks.
- **15 original TC/direct-DF mappings, 18 historical DF records, 49 atomic records,
  nine groups, seven BP definitions and 15 TC-family memberships** are preserved.
  Three pilots, 18 variants, 20 BR IDs and 15 OD IDs remain. TC-003's normalized
  fixture wording is synchronized with Q1; source facts/direct links are retained.
  Other BR rows, TC-006/027 pilot bodies and TC-003 recovery variants are unchanged.
- **16 source/archive/member/instruction fingerprints** checked, including the
  original workbook and new pre-approval snapshot. **12 unchanged claim-table rows**
  match KB30's exact chunk/claim associations. The new ZIP's nine members match
  the fresh pre-edit hashes byte-for-byte; the Round 1 decision record still
  matches its supplied v0.3 member.
- **Eight Problem #2 documents updated; one history ZIP added.** All **165 other
  pre-existing repository files**, including the glossary and prior runtime work,
  **467 historical report files** and **six external source files** are unchanged.
  `git diff --check` passed; the snapshot-to-current diff has no newly introduced
  trailing whitespace. The Git HEAD is unchanged.
- **Zero Agent/runner test executions, live requests or saved-evidence regrades.**
  Four internal selections are recorded; no formal Grab approval, runtime
  conformance, financial resolution or baseline freeze is claimed. Behavior and
  coverage verdicts remain `NOT_RUN`.

Audit artifacts are retained at
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-od002-agreement-2026-11-02`:
`preservation-before.json`, `capture-before.py`, `audit-agreement.py`,
`approval-recording.diff` and `documentation-verification.json`. The repository
history ZIP and cited source fingerprints provide the durable preservation record.
