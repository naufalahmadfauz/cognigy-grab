# OD-004 / OD-005 — education triggers and timing conventions

**OD004-OD005-REVIEW-0.2 · 2026-11-03 · VERIFIED [POC] / ENGINEERING_AGREED_POC for qualified Q1–Q7 only.**

[Decision register](OPEN_DECISIONS.md) · [Source/BR manifest](BASELINE_MODEL.md) ·
[TC/process families](TC_CLASSIFICATION_MATRIX.md) ·
[Historical findings](DEFECT_GROUP_IMPACT_MATRIX.md)

This coupled review continues the completed `OD002-REVIEW-0.2` state. Its four
internal choices are settled and referenced through the
[existing approval record](OD002_STATUS_DECISION_REVIEW.md#recorded-q1q4-approval-and-provenance).
TC-009's agreed direct submission fixture and the narrow GrabMart status-only
navigation exception are preserved. The requesting project-side user has approved
[Q1–Q7 with explicit qualifications](#recorded-q1q7-approval-and-provenance) as
provisional internal POC engineering decisions. Q2/Q7 are conditional; Q4 is
approved **as modified, conditional rather than universal**. Formal policy,
Tool-contract/UI/timing conflicts, reviewer appointments and dependent acceptance
remain open. These agreements authorize documentation updates only.

The deliverable is an intent/entry/age/LOB trigger table, a timing/date convention
sheet, shared-impact analysis and the recorded decisions/remaining review frontier. It supplies no new
execution or evidence assessment: `behavior_verdict=NOT_RUN` and
`coverage_verdict=NOT_RUN`. Business Acceptance Baseline v1.0 remains **NOT FROZEN**.

## 1. Sources and authority

`WB:S` = original **Scenarios**, `WB:D` = original **Defect Log**. Source keys,
original archive locations and earlier fingerprints are retained in
[BASELINE_MODEL.md](BASELINE_MODEL.md#sources-and-authority). `JOB30`/`KB30` mean
the October 30 export identified by the Problem #1 handover as its last verified
POC reference. They are the current **documented** reference for this review,
not proof of today's served configuration or authenticated UI.

| Evidence layer | What it establishes | Authority limit |
|---|---|---|
| Original WB / PLAN / PB | Benchmark examples, intended branches, historical feedback and the agreed milestone/coverage review method. | Sample dialogue is not independently authoritative policy; preserve conflicting cells and missing observations. |
| JOB30 / KB30 and the explicitly adopted GM status-only POC policy | Documented POC behavior, factual source distinctions and the narrow accepted navigation exception. | Existing POC adoption is not formal Grab policy approval; Job wording and static code are not runtime evidence. KB articles retain `adoption=provisional_poc`, `formal_approval=pending`. |
| Round 1 and OD002-REVIEW-0.2 | Bounded internal fixture/governance/status choices already agreed by the project-side user. | These are settled inputs, not new questions in this review. They do not approve every related BR or resolve formal policy/UI gaps. |
| OD004-OD005-REVIEW-0.2 / requesting user's 2026-11-03 approval | Qualified Q1–Q7 settle the stated internal education/intent, fixture-reference and no-photo drafting choices. Full approval text and superseded interpretations are in §6. | **VERIFIED [POC] / ENGINEERING_AGREED_POC** only within the recorded qualifications; no formal Grab approval, implementation authorization, current-runtime conformance or test result. Other proposals retain their status. |
| Missing policy/calendar/UI evidence | Identifies the judgment that cannot yet be supported. | **UNKNOWN/CONFLICT**; a project-side convention cannot certify official eligibility, an operational calendar, bank receipt or a payment remedy. |

### Source fingerprints

| Artifact | SHA-256 |
|---|---|
| October 23 PLAN/PB bundle | `5fc1ac6e177af2706fa6deb694fa11bb892a7bbee0b13778feeb1aa640802349` |
| Original WB containing ZIP | `70af7a87677a5e4b0dd9a794513fa1640eb21eb2ef8fe9748a05b1500b2c5f4b` |
| Original WB XLSX member | `12e17ad51b6ee2053a4e2c56d3ae8b5ff56f544a6f9a1487dd274c05af5c797e` |
| JOB30 / KB30 export ZIP | `e92afdf8d41c5a348e65e18e0a1cad77f827d26dab5c6d3fe136d3439c1a8a1f` |
| JOB30 node `nodeData/6ae43b6f90878ce305636d97` | `71d62956ae2b91db64deef08dcd0aaab37ba1a38f16d43c292f916a622f756c0` |
| JOB30 `/localizedData/0/config/instructions`, original UTF-8 | `d89731bb49f09959e0c9c35550cb0b9fa71fa03a88295916887672c20390d860` |
| H1 handover | `42d47a69d9f0d392e17dea60d033f60c0ae6e10e616f129fd8c091b9a67408a1` |
| KBC closeout | `6907060c34d3d9207efbbf306d4974f0479a4dcd4e2c74795f8fed203b1b2c47` |

Problem #1 remains closed for its documented isolated-POC retrieval/tested-knowledge
scope. Retrieval success does not resolve the source conflicts or certify business
calendars, actual payment, original benchmark coverage or current voice behavior.

### Static Tool, Code and wiring ledger

All members below belong to the authenticated JOB30/KB30 ZIP. Config pointers are
`/localizedData/0/config`; node `type`/`label` and chart `relations` are top-level.
These are inspected definitions, not executed Tools or a platform-wide guarantee.

| Ref / member | SHA-256 | Relevant extraction fact |
|---|---|---|
| S01 / `nodeData/6ae43b6f90878ce305636d99` | `d1a22c2045241a9b6360f09f44528321619c27166de75cd4faf54bff10284e48` | `resolve_order_age`: required string `days_ago` and `lob`; `use_session` first; same-order correction exception. No date, timestamp, `as_of` or `now` parameter. |
| S02 / `nodeData/6ae43b6f90878ce305636da4` | `29b9f4a6999f4681afb1097a9acbdecee1a8d29febd4ebeb8ccae9189647ae03` | Resolver Code: trims whole-number text, requires a nonnegative safe integer; uses `state.today.weekday` and inclusive cutoffs. `presentTimeline` depends on age/LOB/marker, not intent. |
| S03 / `nodeData/6ae43b6f90878ce305636d90` | `9e1622e789b519b83df8db5b66b98b851ce457a03c218efaa20f14a25c40643f` | Initializer: `Date.now() + 8 * 3600 * 1000`, UTC accessors, stored `today.iso` and weekday; age -1, blank threshold and `educateDelivered=false`. |
| S04 / `nodeData/6ae43b6f90878ce305636d8a` | `f49f7b821a438f8aa66f34d3abbaa30f89027b932851b695725adb9b5e2cde5c` | `type=once`, label `Initialize Once`. |
| S05 / `nodeData/6ae43b6f90878ce305636d8c` | `01114306633149c42c42e3bd4b6f226ca327da877931d6128f62abdbf3fe7cc6` | `type=onFirstExecution`, label `On First Time`; S09 connects this child to S03. |
| S06 / `nodeData/6ae43b6f90878ce305636d9a` | `f7d23262e30e4c80f45ad55e240b0a8c98aa2f737f8ea6c9da9e7e8c07f0783c` | `start_guidance` condition is exactly `context.shortTermMemory.uc4.threshold === "beyond"`. Requires platform/style/loudspeaker/journey. Recent accepted guidance has no standard admission through this gate. |
| S07 / `nodeData/6ae43b6f90878ce305636da6` | `af267f43fa2595f6381b52d346bec3e1867bffdc1f128c80afda62ca93b2aadc` | Resolve returns `JSON.stringify(input.uc4Result)`; it does not supply merchant-facing education. |
| S08 / `nodeData/6ae43b6f90878ce305636d8e` | `3169a02b1aa3cc0b500b6f1eb9bbe25d50dbd94c8da9a48d08887210ad4045ea` | Bounded first-real-input LOB capture; later corrections remain resolver-owned. Not an absolute-date parser or weekday refresh. |
| S09 / `chart/6ae43b6f90878ce305636d80` | `d3d37e7042055993ba7f0bda4270cba1b0040cdee047e95f3f41f1262a69b1f5` | Once → On First Time → initializer; age Tool → age Code → Resolve; guidance Tool is a separate Job child. No refresh/automatic age increment found in the inspected exported state-writing code. |

### Precise Job-heading ledger

`J01`–`J15` are local citation aliases, not new requirements or benchmark IDs.
Headings below match the original JOB30 instruction string exactly.

| Ref / exact JOB30 heading | Rule or conflict used in this review |
|---|---|
| J01 / `FIXED LOB TIMELINES` | Exact qualified LOB approval/payout sentences; ends with unqualified age-only → open question/wait. Wording precedence is stated for the timeline sentence, not a complete conflict-resolution order. |
| J02 / `RECENT CANCELLED ORDER`; `GRABMART RECENT CANCELLED ORDER` | First valid within + `presentTimeline=true` → timeline, stage-specific photo reminder, anything-else; no automatic walkthrough. Conflicts with J01 for recent age-only input. |
| J03 / `FOLLOW-UP` | Answer current question; after-timeline nonreceipt question → conditional request-option explanation and offer/wait; timing answer includes approval and payout; evidence by LOB. OD-002's agreed approval-aware priority remains controlling for its subset. |
| J04 / `OLDER CANCELLED ORDER` | Older age-only clarification; timing answer/offer; distinct GF and GM open-question education priorities; upfront explicit guidance is direct. The explicit-intent paragraph is inside this older-order heading. |
| J05 / `STATUS AND SUBMISSION TOGETHER` | Dual intent is guidance consent except the named older open-question responses; no timeline/re-offer for direct requests; preserve both goals and status observation. Submit-only does not require status first. |
| J06 / `DIRECT GRABMART STATUS NAVIGATION — ISOLATED POC` | Existing age-independent status-navigation exception and its explicit precedence/exclusions, including the bypass of mandatory `start_guidance`. |
| J07 / `CANCELLATION DATE`; `SPEECH UNDERSTANDING` | Whole-number cancellation age, supported relative expressions, missing/invalid-age clarification; preserve facts and goal. |
| J08 / `MERCHANT CONTEXT`; `CURRENT ORDER LOB CORRECTION` | Same-order identity/LOB correction; reuse age and preferences; recompute routing. Newly-within result stops a prior beyond walkthrough under the documented correction rule. |
| J09 / `GUIDANCE`; `CLOSING` | Requested/accepted guidance, immediate respect for decline, separate finish handling; a new question is not automatically a finish signal. |
| J10 / `PLATFORM SCOPE`; `GUIDANCE PREFERENCES`; `GRABMART GUIDANCE RULES` | Supported routes, missing preferences, once-only GM notice and computer-Portal readiness; ordinary guidance setup is not an eligibility determination. |
| J11 / `REQUEST FOR COMPENSATION — GRABMERCHANT APP`; `PORTAL SUBMISSION — SEARCH BAR ROUTE` | Form visibility before completion; several form-completion instructions say to attach the LOB-specific photo without a no-photo condition. |
| J12 / `KNOWLEDGE`; `POST-SUBMISSION RESPONSE CONSTRAINTS` | Factual grounding, preparation/packing qualification, no-photo non-inference; conditional review outcome after merchant-reported submission. |
| J13 / `GUIDANCE TURN BEHAVIOR`; `ALL-AT-ONCE DECISION SEGMENTS`; `MANDATORY GUIDANCE CHECKPOINTS` | Current-step recovery, observations and retained progress remain separate from education and date classification. |
| J14 / `GRABFOOD APP — COMPENSATION STATUS`; `GRABMART PORTAL — COMPENSATION STATUS` | Supported status observations; date/History recovery is conditional on order visibility, not an automatic consequence of routing age. |
| J15 / `SAFETY ESCALATION`; `GREETING OWNERSHIP`; `CONTROLLED FLOW CONTENT`; `OUT OF SCOPE` | Existing priority, entry ownership and terminal/scope boundaries; the education review supplies no new transfer authority. |

### KB article, chunk and claim ledger

All 17 article metadata records and all 20 retained chunk/claim records were
authenticated against the export. The relevant claims are stated below, including
boundary controls. Article adoption remains `provisional_poc`, formal approval
`pending`; an exact extraction is not a new approval. The archive fingerprint
binds the full text and metadata; chunk IDs locate it independently of local IDs.

| Exact chunk / claim IDs | Source fact and limit used here |
|---|---|
| `UC4-MY-GF-TIMING-001-C01`; `UC4-MY-GF-CLAIM-007` | Usually 1–2 business days after order made for approval, then regular payout; not a guaranteed bank-credit date. |
| `UC4-MY-GM-TIMING-001-C01`; `UC4-MY-GM-CLAIM-006` | Usually 3–5 business days after order made for approval, then regular payout; distinct processing/receipt stages. |
| `UC4-MY-GF-THRESHOLD-001-C01`; `UC4-MY-GF-CLAIM-015`, `UC4-MY-GF-CLAIM-016` | Weekday elapsed-day cutoffs, inclusive recent boundary; not eligibility/deadline/payment math. Operating date/version conventions unconfirmed. |
| `UC4-MY-GM-THRESHOLD-001-C01`; `UC4-MY-GM-CLAIM-014` | GM weekday elapsed-day cutoffs with the same limits. |
| `UC4-MY-GF-EVIDENCE-001-C01`; `UC4-MY-GF-CLAIM-009`, `UC4-MY-GF-CLAIM-010` | Prepared-food photo reference; can continue request without photo using clear supporting information. No automatic denial, evidence exemption or approval; substitutes unconfirmed. |
| `UC4-MY-GF-EVIDENCE-001-C02`; `UC4-MY-GF-CLAIM-011` | Before-preparation exclusion is a provisional POC assumption pending formal applicability, not inferred from no photo. |
| `UC4-MY-GM-EVIDENCE-001-C01`; `UC4-MY-GM-CLAIM-008`, `UC4-MY-GM-CLAIM-009` | Packed-items photo reference; no-photo continuation and the same non-inference/substitution limits. |
| `UC4-MY-GM-EVIDENCE-001-C02`; `UC4-MY-GM-CLAIM-010` | Before-packing exclusion is a provisional POC assumption; missing photo does not establish unpacked items. |
| `UC4-MY-GF-STATUS-001-C01`; `UC4-MY-GF-CLAIM-005` | App status reference; approval is not bank receipt; missing order/link is not rejection. |
| `UC4-MY-GM-STATUS-001-C01`; `UC4-MY-GM-CLAIM-003`, `UC4-MY-GM-CLAIM-004` | Portal status reference; missing transaction is not rejection or bank receipt. No GM App status route supplied. |
| `UC4-MY-GF-SUBMIT-001-C01`; `UC4-MY-GF-CLAIM-012`, `UC4-MY-GF-CLAIM-013`, `UC4-MY-GF-CLAIM-014` | Documented App link and Portal alternative; early form acceptance/current screens untested; absent link is not ineligibility or wrong role. |
| `UC4-MY-GM-SUBMIT-001-C01`; `UC4-MY-GM-CLAIM-012`, `UC4-MY-GM-CLAIM-013` | Same submission-stage limits with GM evidence; no age-based acceptance assurance. |
| `UC4-MY-SHARED-DEADLINES-001-C01`; `UC4-MY-SHARED-CLAIM-008`, `UC4-MY-SHARED-CLAIM-010` | Routing thresholds do not reject older requests; public 90-day enquiry reference has unresolved UC4 applicability, including acceptance beyond it. |
| `UC4-MY-SHARED-DEADLINES-001-C02`; `UC4-MY-SHARED-CLAIM-008`, `UC4-MY-SHARED-CLAIM-009` | Five working days for investigation/response and at least three business days for bank credit before contact are separate source stages, with unconfirmed UC4 applicability. |
| `UC4-MY-GF-SPLIT-001-C01`; `UC4-MY-GF-CLAIM-001`, `UC4-MY-GF-CLAIM-002` | Eligible split-order automatic reimbursement/weekly App-record update; not every cancellation or a weekly payout promise. |
| `UC4-MY-GM-SPLIT-001-C01`; `UC4-MY-GM-CLAIM-001`, `UC4-MY-GM-CLAIM-002` | Same narrow split-order reference; not a new GM App status-navigation route. |
| `UC4-MY-SHARED-ELIGIBILITY-001-C01`; `UC4-MY-SHARED-CLAIM-006` | Illustrative cancellation reasons are not exhaustive eligibility or an individual award decision. |
| `UC4-MY-SHARED-REQUEST-001-C01`; `UC4-MY-SHARED-CLAIM-007` | Owner/Manager submission authorization and merchant self-submission; current authenticated access untested. |
| `UC4-MY-SHARED-PORTAL-001-C01`; `UC4-MY-SHARED-CLAIM-011`, `UC4-MY-SHARED-CLAIM-012`, `UC4-MY-SHARED-CLAIM-013` | Reference Portal destinations; standard POC route remains Search Bar; current menus untested. |
| `UC4-MY-GM-PERISHABLE-001-C01`; `UC4-MY-GM-CLAIM-011` | Existing partial-assessment notice, with amount/certainty limits; separate OD-006 decision. |

## 2. Intent, entry, age and LOB trigger table

**Reading rule:** “documented” describes source content, not complete Problem #2
acceptance. The final column records qualified **agreed internal** dispositions
and separately retained source/implementation conflicts. Q references mean Round 3
unless explicitly marked OD-002. Age-first applies only outside J06's existing
GM status-only exception. A factual timing/evidence question is not consent to a
walkthrough. “Check status” means requested supported navigation only where that
meaning is clear; generic status curiosity is kept separate.

| Row / input and entry context | Age / LOB | Source-backed response, offer and continuation | Agreed drafting disposition / remaining conflict / benchmark control |
|---|---|---|---|
| T01 — Only cancellation age, no clear goal; first recent classification | Within; GF or GM | J02 prescribes fixed LOB timeline → recent photo reminder → anything-else, no unsolicited walkthrough. J01 instead says unqualified age-only → open question/wait. | **Q1 AGREED:** deliver applicable recent education without an unnecessary extra goal question for this defined entry; do not infer preparation/packing. WB:S!C4:E5,C14:E15 / TC-001/025 remain the source targets. J01/J02's original conflict is retained, not implemented away. |
| T02 — Only cancellation age, no clear goal | Beyond; GF or GM | J04: one open question and wait; no menu, preferences or unsolicited timeline on that turn. | Documented; WB:S!E7,E8,E17,E18. DF-018's fix note cannot turn original TC-004 into within-threshold coverage. |
| T03 — Explicit “when/how long” timing question, including a later genuine timing question | Within; GF or GM | J01/J03 answer usual approval **and** regular payout. J02 adds the recent reminder/anything-else on its first-education path; subsequent replies answer the question without automatic full-bundle repetition. | Timing facts are established POC references; **Q5 AGREED** answers a new timing question after decline without automatically repeating the declined offer (T14). Known approval/nonreceipt uses protected T15. |
| T04 — Explicit timing question | Beyond; GF or GM | J04: fixed LOB timeline + status-check offer in the same response; wait for acceptance. No recent “take a photo” reminder. | Source rule retained; **Q5 AGREED** qualifies its repeat-offer applicability after decline. Do not apply the separate GF open-question existing-photo reminder to every timing-only reply. |
| T05 — Answers older open question with general status interest **or dual status/submission intent** | Beyond; GF | J04/J05: exact GF timeline + conditional existing-prepared-food-photo reminder + one status-guidance offer; wait. Accept → appropriate status or status-then-submission journey, retaining both goals. Decline → stop guidance. | Documented special entry, WB:S!E7/E8; TC-004/005 and relevant older GF inquiry segments. A dual reply here does not override the specific education/offer rule. |
| T06 — Answers older open question with general compensation/status inquiry | Beyond; GM | J04: exact GM timeline before preferences; one status-guidance offer is **optional** for general inquiry. If offered, wait; no mandatory older-GM photo reminder. Factual answer does not require platform access. | WB:S!E17 / TC-028 contrasts with its copied prepared-food reminder. A bare acknowledgement is not proof of resolution (OD-009). Clear where/how-only navigation still meets protected T12. |
| T07 — Answers older open question with status **and conditional submission** | Beyond; GM | J04/J05: fixed GM timeline + **required** one status-guidance offer, wait; accept → retain both goals, status first and submission only if still needed. | Documented priority, WB:S!E18 / TC-029; not optional merely because the preceding general-inquiry paragraph says “optionally.” |
| T08 — Upfront explicit status-only, submit-only or dual walkthrough request | Beyond; GF or GM, outside T12 | J04/J05: no unsolicited timeline, open-goal question or repeated offer; collect only missing required preferences, then supported route. Submit-only stays submit-only. | GF TC-003's scoped rule and TC-009 direct submission remain settled. **Q3 AGREED:** TC-027's clear upfront dual request proceeds without unsolicited timing/re-offer; retain GM partial notice, explicit computer-Portal transition, preferences and status observation before submission decisions. WB:S!E16's contrary text remains for formal review. |
| T09 — Upfront status interest whose requested assistance remains genuinely ambiguous in context | Beyond; GF or GM | J04 defines elicited inquiry (T05/T06) and explicit upfront navigation (T08); an isolated phrase does not establish which applies. J06 covers clear GM where/how-only intent. | **Q4 AGREED AS MODIFIED, CONDITIONAL:** clarify once only if assistance is genuinely ambiguous. A clear status-check request must not trigger redundant intent clarification; no phrase-based universal clarification rule. Preserve T12 and its absence of unnecessary age/loudspeaker intake. |
| T10 — Explicit direct navigation request, or acceptance of an offered walkthrough | Within; GF or GM, outside T12 | J05 broadly makes dual intent consent; J02 prescribes recent education; J04's explicit-intent paragraph is inside the older-order section; S06 admits standard guidance only when beyond. | **Q2 AGREED CONDITIONALLY:** requested/accepted navigation takes priority over unsolicited routine education, retaining mandatory disclosures and necessary intake. **Implementation conflict remains:** S06 is beyond-only; no runtime change is authorized and early form acceptance is not established. Detailed recent-entry contract/coverage remain pending. |
| T11 — After education: “what if compensation still does not arrive?” without already-established approval | Within/relevant follow-up; GF or GM | J03: conditional request-option explanation + offer to guide to cancelled order; wait. Do not infer eligibility from link presence/absence. J09 respects decline and asks further help. | WB:S!E5/E15 / TC-002/026 exercise **declined** offers. They do not demonstrate the accepted branch; that returns to T10/Q2. No GM App status route, payment deadline or remedy follows. |
| T12 — Clear current-order **GM status-navigation only**, where/how to view, without conflicting identity/LOB | Age not required; GM only | J06 explicitly overrides age-first/resolver-only lookup, recent/older routing, loudspeaker and mandatory guidance Tool. Answer supported location directly; guided steps collect only missing navigation preferences, preserve Portal readiness and once-only notice. | **Existing protected POC exception**, not a new approval question; `VAR-TC-027-F`. Excludes timing, eligibility, submission, dual intent and unresolved order/LOB conflicts. Changed intent exits it, reusing known facts. |
| T13 — Same-order LOB correction, or genuine age correction | Recomputed classification; GF or GM | J08/S01/S02 preserve intent/preferences and reuse known valid age for a LOB correction; discard incompatible route/status assumptions. Job says newly-within stops prior beyond walkthrough; beyond retains active intent. Age correction alone does not reset the Code's education marker. | **Q2 AGREED CONDITIONALLY**, explicitly including same-order age correction: retain requested/accepted navigation priority, necessary intake and mandatory disclosures. The corrected-route/state and beyond-only Tool contract still require reconciliation. J06 applies only with its nonconflicting GM-only status scope; different orders do not borrow age. |
| T14 — Guidance declined, then another timing/factual question on the same goal | Either age; GF or GM | J09 stops guidance; J03 answers the new question; J01 permits valid later timeline answers. J04 also attaches an offer to timing answers, leaving repeated-offer priority underspecified. | **Q5 AGREED:** answer the new timing question without automatically repeating the same declined offer. A new explicit guidance request may change the branch; its applicable entry contract still applies. The original Job-source conflict remains visible. |
| T15 — Reported approval with no bank receipt, or unclear displayed status during TC-003 handling | Existing OD-002 scope | Apply agreed C explanation/clarification priority or D observed-status clarification. Generic J03 must not restart unnecessary submission or infer paid/rejected from age. | **Settled OD-002**, referenced only. B/C behavior does not complete TC-003's submission target; D does only after establishing/exercising A. No new question here. |
| T16 — Evidence, preparation/packing or eligibility question | Either age; correct LOB required | J03/J12 and KB answer the actual factual question; explain provisional preparation/packing applicability when asked. Missing photo does not imply unprepared/unpacked, denial, exemption or approval. | **Q7 AGREED CONDITIONALLY:** no-photo supported-request continuation uses available evidence/information and preserves recommendations; no promise of eligibility, acceptance, completeness or approval. Flag separately established mandatory UI/business-policy conditions for review. Exact-text and final-policy conflicts remain. |
| T17 — Missing/invalid age, uncertain LOB/order, unsupported absolute-date interpretation | Age-dependent request; outside T12 | J07/J08/S01/S02 clarify genuinely missing facts, retain intent and valid facts; never default blank/invalid age to today or guess LOB. | **Q6 AGREED:** explicit cancellation-age fixtures with declared Asia/Kuala_Lumpur (UTC+8) test reference and reproducible same-session date assumptions; documented relative expressions allowed. Creation age remains distinct; unsupported absolute/midnight normalization remains unresolved. |
| T18 — Safety emergency, terminal state or genuinely unrelated topic | Either LOB/age | J15's existing priority/ownership applies; factual payment concern about this cancellation stays in scope. | Negative control TC-010; no new compensation intake, handoff trigger or safety rule is created by this review. |

The required evidence for an education judgment is the **actual entry context and
observable reply**, not merely `presentTimeline=true`. S02 marks
`educateDelivered=true` when it returns the suggestion, before any merchant-facing
speech; a suppressed or interrupted answer can leave that marker set. LOB changes
reset it; age-only changes do not. Treating it as proof of audible education would
confound OD-004 with OD-013. No state-machine correction is adopted here.

## 3. Timing and date conventions

### Routing cutoff reference

Exact source values: KB30 GF/GM THRESHOLD C01 and S02. These **internal elapsed-day
routing values** are not approval-business-day calculations or merchant deadlines.
Use the authoritative LOB; `age <= cutoff` is within/recent and `age > cutoff` is
beyond/older. Day zero is valid numeric routing input, not an approved approval-clock
day-zero rule.

| Weekday used for classification | GF maximum recent age | GM maximum recent age |
|---|---|---|
| Monday | 4 | 7 |
| Tuesday | 4 | 7 |
| Wednesday | 2 | 7 |
| Thursday | 2 | 7 |
| Friday | 2 | 7 |
| Saturday | 3 | 8 |
| Sunday | 4 | 9 |

For example, on a **declared Tuesday reference**, GF age 4 is within and 5 beyond;
GM age 7 is within and 8 beyond. On Sunday, GM 9 is within and 10 beyond. These are
static table illustrations, not runtime test results, due dates or eligibility.

### Date, clock and event sheet

| Topic | Authenticated source fact | Agreed fixture scope / unresolved interpretation |
|---|---|---|
| Routing event | S01/S02/J07 use **cancellation age**. WB:S!C3 says “Order age to give”; examples such as E4/E6/E14/E16 say order **made**. | Creation and cancellation cannot silently be equated. Use a clear cancellation-age fact; clarify when only creation age is known. Approval's different origin remains explicit. |
| Input representation | S01 requires whole-number **text**; S02 trims it and accepts nonnegative safe integers. Numeric JSON values, decimals, negative/blank/nonnumeric/unsafe values fail its valid-age check. | Validating an integer is not determining elapsed days from timestamps. Do not infer a 24-hour floor/ceiling or silently treat an invalid value as zero. |
| Relative expressions | J07/S01 map today → 0, yesterday/semalam → 1, two days ago/kelmarin → 2. J07 also recognizes clear natural speech such as “just now.” | Resolve clear relative wording into the supported whole-day representation; ambiguous dates need clarification. Job references to natural speech do not define arbitrary absolute-date normalization. |
| Reference date and timezone | S03 stores a fixed UTC+8 date/weekday; S04/S05/S09 place initialization under Initialize Once. S02 later reads the stored weekday. | **Q6 AGREED:** declare Asia/Kuala_Lumpur (UTC+8) as the test reference with reproducible same-session date assumptions. The export uses fixed-offset arithmetic, not an identified named-zone implementation; neither it nor the agreement certifies official operating policy or a refreshed clock. |
| Cross-midnight / long session | No weekday refresh or automatic `ageDays` increment found in the inspected exported state-writing code. The Tool exposes no injected `as_of`/`now` parameter. | A Tuesday→Wednesday session can retain Tuesday's cutoff and supplied age. New “yesterday” wording after midnight also needs a defined reference. These cases have no accepted cross-midnight convention here. |
| Absolute dates / timestamps | No absolute-date parser or timestamp-to-age calculation in S01/S02; Job's provided aliases are narrower. | Cancellation timestamp, locale, timezone, truncation/rounding and day boundary remain owner/spec dependencies. **Q6** settles only explicit cancellation-age fixtures/documented relative expressions; no fabricated conversion or Tool parameter. Absolute-date and midnight-boundary conventions remain unresolved. |
| Age and LOB changes | Valid age may be retained while LOB is unresolved; no successful classification until both exist. Same-order LOB correction recomputes with the supplied age and stored weekday. | Preserve current-order identity. A different order requires its own facts; an age change does not prove a fresh education delivery or refresh the reference clock. |
| Business calendar | J01/KB TIMING explicitly say business days. No authoritative holiday list, working-week calendar, daily cutoff, day-zero inclusion, service exception or effective-date schedule is supplied. | Keep usual qualified intervals; no exact approval date, lateness determination or holiday computation. Do not convert routing cutoffs into a business-day calendar. |
| Version and evidence | The October 30 export is a fingerprinted historical definition. WB examples are symbolic relative ages, not timestamped executions. | A future fixture should identify source version, LOB, same-order cancellation-age statement, initialization/reference date+weekday+UTC offset and entry context. Actual observed initialization must be distinguished from intended fixture metadata. |

**Q6 agreed internal fixture convention:** declare **Asia/Kuala_Lumpur (UTC+8)**
as the test reference, use explicit cancellation-age fixtures or documented
unambiguous relative expressions, and record reproducible same-session date
assumptions. Keep the initial fixture within its declared reference date; record
intended versus observed initialization separately. Cancellation-age routing is
distinct from approval timing after the order was made. Absolute-date, timestamp,
midnight-boundary and official business-calendar conventions remain unresolved.
The agreement supplies neither an injectable S01 clock nor a runtime change or
formal Grab timezone/calendar approval.

### Approval, payout, receipt and other intervals

| Stage / interval | Event origin, unit and authority | Permitted interpretation / limit |
|---|---|---|
| Usual GF approval: 1–2 business days | **After order was made**, J01 and GF TIMING C01. WB E4/E7 says “days” without “business.” | Use the documented qualified business-day approval reference, subject to policy; not days after inquiry/submission or a guaranteed bank payment. |
| Usual GM approval: 3–5 business days | **After order was made**, J01 and GM TIMING C01. WB E14/E17 says “days”; E16/E18 instead says credited to bank. | Bank-credit wording is a retained source conflict. The documented POC sentence concerns usual approval, followed by regular payout. |
| Payout cycle | Approved compensation then follows the next regular earnings payout cycle, J01/KB TIMING. | No exact frequency, cutoff, account schedule or maximum approval-to-bank duration is established. Approval, processing, payout and bank receipt remain separate stages. |
| Recent evidence reminder: GF >2 / GM >5 business days | J02's possible later support review language; original E4/E14 carries similar reminder thresholds. | This is reminder context, not a new form-acceptance gate or an additional SLA. No independently defined reminder clock/holiday calendar authorizes an exact-date computation. |
| Older-order enquiry: 90 days | SHARED DEADLINES C01 reports public wording measured from cancellation. | UC4 applicability unresolved; neither automatic rejection after 90 days nor indefinite acceptance is established. |
| Investigation/response: five working days | SHARED DEADLINES C02 describes a payment-dispute referral stage. | UC4 applicability and complete event/calendar conventions unconfirmed; not the LOB approval period. |
| Bank credit before contact: at least three business days | SHARED DEADLINES C02 describes separate bank-credit/contact wording. | Not an approved UC4 overdue trigger, fixed bank-credit promise or general escalation rule. Never add 90/5/3 into a total deadline. |
| Weekly record update for eligible split large orders | GF/GM SPLIT C01; eligible split-order automatic reimbursement reference. | “Weekly” describes the App **record**, not payouts or every cancellation; does not add a GM App status walkthrough. |

Known approval plus nonreceipt remains the agreed OD-002 C explanation/clarification
case. An approval interval cannot supply a remedy for an already-approved unpaid
order; authorized financial-resolution triggers remain OD-014 evidence needs.

### Stage-specific evidence reminders

| Stage | GF source content | GM source content | Boundary / review status |
|---|---|---|---|
| First recent education, when its trigger applies | J02: take a photo of the **prepared food**, in case of later support review after more than two business days. | J02 exact: “Please take a photo of the order as evidence, in case you would like to submit a request for our support team to review further after it has been more than five business days.” | Preserve stage distinction: GM recent says **order**, not GF “prepared food” and not a silent global replacement with “packed items.” Q1/Q2 settle scoped drafting priority, not the unchanged source/Tool conflict. Q1 does not confirm preparation/packing; Q7's conditional qualification applies. |
| Older open-question status/dual response | J04 exact: “If you still have a photo of the prepared food, keep it as evidence in case it needs review.” | J04 has **no equivalent mandatory older-GM reminder**. | GF concerns a photo already taken, not taking a new photo. WB E17's copied prepared-food/reminder text does not create a GM obligation. |
| Beyond timing-only answer | J01/J04: no recent take-new-photo instruction. | Same limit. | Do not automatically transplant the separate GF older-inquiry reminder into every timing-only answer. |
| Explicit evidence question or form completion after observed visibility | J03/J11/KB: photo of **prepared food**. | J03/J11/KB: photo of **packed items**. | Merchant fills/submits; then reports submission. Preparation/packing is not established merely by the instruction. Unconditional “attach” in J11 conflicts with known no-photo handling. |
| Merchant says photo absent/unavailable | KB GF EVIDENCE C01 permits continuing request with clear, complete supporting information. | KB GM EVIDENCE C01 permits the same. | **Q7 AGREED CONDITIONALLY:** continue the supported request process with available evidence/information; preserve evidence recommendations. Do not promise eligibility, acceptance, completeness or approval. Separately established mandatory UI/business-policy conditions must be flagged for review, not silently waived. No specific substitute or exemption is approved. |

WB:S!E14/E15/E17's GM prepared-food wording is preserved as source history;
E16/E18's submission segments instead use packed items. H1 §6 item 3 explicitly
calls for review of unconditional photo wording. Routine reminder text, a missing
photo, and a confirmed before-preparation/packing question are different facts;
only the latter invokes the separately qualified exclusion explanation.

## 4. Conflicts and dependencies

### Resolved drafting choices and retained conflicts

The requesting user's qualified Q1–Q7 approval settles the following internal
drafting choices. Source disagreements, implementation contracts and unavailable
policy/UI evidence remain separate dimensions; no complete OD or runtime path is
declared closed merely because its drafting choice is agreed.

| Choice / retained conflict | Evidence collision | Resolved drafting choice / remaining dependency |
|---|---|---|
| Recent age-only precedence | J01 open-question wording versus J02 and WB TC-001/025 first-recent education. | **Q1 agreed:** applicable recent education, no unnecessary extra goal question or inferred preparation/packing. Unchanged Job-source precedence and formal benchmark reconciliation remain. |
| Recent direct/accepted guidance admission | J05 direct-intent wording versus J02, J08 newly-within stop and S06 beyond-only gate; original TC-002/026 decline rather than accept. | **Q2 agreed conditionally:** intent priority, including same-order age correction, with mandatory disclosures/intake. Coherent admission/state contract and accepted-recent coverage remain open; Tool restriction is an implementation conflict, not a runtime-change authorization or evidence of early form support. |
| Older GM upfront dual education | WB TC-027 E16 inserts timeline/re-offer; J04/J05 say upfront explicit guidance is direct; TC-003 E6 illustrates direct intake. | **Q3 agreed:** no unsolicited timeline/redundant offer; GM notice, computer-Portal transition/preferences and status observation retained. Formal WB conflict and notice certainty remain; DF-014 closure is unchanged. |
| Upfront generic status curiosity | Elicited generic inquiry and explicit upfront navigation are specified; an isolated phrase does not establish ambiguity. | **Q4 agreed as modified:** clarify only genuinely ambiguous assistance, never redundantly clarify a clear status-check request. GM-only direct exception remains intact; no universal phrase-triggered question or unnecessary age/loudspeaker intake. |
| Repeated offer after decline | J04 timeline+offer and J01 valid later timeline requests versus J03 answer-first/J09 respect decline. | **Q5 agreed:** answer new timing question without automatic repeat offer. A new explicit request may change branch; final consent/finish fixtures remain OD-009 and recent admission remains the Q2 Tool-contract gap. |
| Reproducible date-fixture scope | KB “current weekday” versus S03–S05 stored initialization clock; WB order-made wording versus cancellation-age Tool; no arbitrary-date API. | **Q6 agreed:** explicit cancellation age, declared Asia/Kuala_Lumpur (UTC+8) test reference, reproducible same-session date assumptions and documented relative expressions. Absolute dates, midnight boundaries and official calendars remain unresolved; approval origin remains order made. |
| Known no-photo instruction precedence | KB EVIDENCE continuation versus J02/J11 take/attach wording; H1 §6 photo caveat. | **Q7 agreed conditionally:** supported-request continuation with available evidence/information; recommendations retained, no outcome/completeness promise. Any separately established mandatory UI/policy condition needs review. Exact wording is OD-011; formal evidence policy/substitutes remain OD-014. |

### Facts and owner gaps that are not approval questions

- The weekday values, inclusive comparison, Tool schema/gate and initialization
  clock are extraction facts. The user need not vote on what the artifacts contain.
- Approval/payout/bank-receipt distinctions, unsupported guaranteed dates,
  no-photo non-inference, the existing GM exception and OD-002 Q1–Q4 are retained
  inputs. Recording the new internal choices does not promote those inputs to
  formal policy or current execution evidence.
- **DF-018:** WB:D!D22 links **TC-004**; C7/D7 are beyond, N22 says within. G22's
  comparison with TC-003 does not create a direct DF–TC association. Blank retest
  result M22 stays blank; PLAN P012/P033 and PB §0/§7's owner resolution remains.
  DF-014's corresponding owner resolution also remains. A new assurance would
  need original-trigger evidence under OD-012, not another approval of old facts.
- **OD-014 owner evidence remains unavailable:** official operating calendar,
  timezone/effective dates and clock origins/cutoffs; current authenticated access
  and early form acceptance; evidence substitutes; formal status/duplicate policy
  and approved-but-unpaid remedy/triggers. No internal vote can create this evidence.
- **OD-006/011:** GM notice certainty and the broader exact-text register remain
  separate. Q3 preserves the notice; Q7 agrees only qualified supported-process
  continuation with the stated UI/policy limits. **OD-007/010/009:** navigation recovery, role reminders and explicit
  finish/transfer fixtures remain scoped later reviews. **OD-013/015:** audible
  evidence, named formal reviewers and acceptance sign-off remain outstanding.

## 5. Shared impact

**Direct** below means a source documents the shared segment or historical
finding. **Plausible** means a changed requirement could affect another applicable
journey. Neither establishes a current failure or a common implementation cause.
The existing BR/BP/TC/DF/DG/VAR identities and memberships are retained.

### Requirements and process boundaries

| Existing BRs | Relationship to this review | Acceptance boundary |
|---|---|---|
| BR-001/002/003 | **Direct core:** retained intent/LOB, age classification and education/timing applicability. | Distinguish an age-only opening, a factual question and requested navigation; identify the event/reference date and actual trigger before judging an omitted explanation. |
| BR-013 | **Direct content:** stage- and LOB-appropriate evidence reminders; merchant submission and conditional acknowledgement. | Preparation/packing and evidence availability remain separate facts. A reminder supplies neither eligibility nor backend approval. |
| BR-004/005 | **Plausible entry boundary:** opening ownership and collection of genuinely missing guidance preferences. | Education must not create a repeated greeting or unsupported preparation claim; a loudspeaker refusal does not decline guidance. Preserve the GM status-only intake exception. |
| BR-006/007/008/009/019 | **Direct downstream/negative controls:** navigation observations, routes, recovery and status-conditioned continuation. | An education decision does not waive pacing or observations. Preserve TC-003's agreed four-branch handling and TC-027's App-to-Portal readiness transition; do not infer status from age. |
| BR-010/011/012 | **Plausible downstream:** request entry, form observation and conditional role access. | Education can be answered without authenticated screen access; starting a walkthrough still requires the applicable route/observations. Preserve TC-009 submit-only and TC-006 declined-retry primary. |
| BR-014/015/016 | **Direct offer/finish and scope boundaries; plausible recovery impact.** | Declined guidance stops that guidance. Acknowledgement is not automatically finish or transfer consent. Missing money remains in scope; elapsed time supplies no handoff authority. |
| BR-018 | **Adjacent dependency:** GM once-only partial-compensation notice before applicable navigation. | Timing-only education does not automatically trigger the navigation notice. Its certainty remains OD-006; this review does not approve an individual amount. |
| BR-017/020 | **QA evidence/adjudication**, not additional merchant-facing instructions. | Distinguish spoken/displayed evidence and semantic acceptance from separately controlled text; OD-011/013 remain scoped dependencies. |

### Existing business-process families and TCs

| BP / existing family | Existing mapped TCs relevant here | Direct relationship / proposed impact control |
|---|---|---|
| BP-01 — Recent cancellation education | TC-001/025 | **Direct:** recent education and LOB-specific timing/evidence. Preserve the ordinary education/finish target; do not add unsolicited submission. |
| BP-02 — Recent follow-up and guidance declined | TC-002/026 | **Direct:** follow-up explanation, appropriate offer, explicit decline. Correct navigation after an accepted offer would be a different branch, not declined-guidance coverage. |
| BP-03 — Older-order inquiry and education | TC-004/028 | **Direct:** age-only entry followed by a factual/general inquiry. Preserve beyond-threshold education and an actual response/finish signal; DF-018's within-threshold fix note cannot redefine TC-004. |
| BP-04 — Compensation status and conditional submission decision | Primary TC-003/005/027/029; secondary TC-007 | **Direct shared intake segment; plausible trigger regression.** Contrast upfront dual navigation (TC-003/027) with goal supplied after the older-order question (TC-005/029). Keep status observations, applicable education, retained submission intent and branch coverage distinct. |
| BP-05 — Request/form submission and role access | Primary TC-006/009; existing secondary/conditional TC-003/005/007/008/027/029 | **Direct downstream segment; plausible reachability impact.** TC-009 is the agreed direct submit-only control. Role access is not an education prerequisite, and education does not establish form access or exercise retry coverage. |
| BP-06 — Navigation recovery, missing-link fallback and platform transition | Primary TC-007/008; conditional TC-003/006/027 | **Plausible conditional impact:** retain goal, age and preferences through recovery without restarting generic intake/education. Routing-date interpretation must not require gratuitous History/date recovery when the order is visible. |
| BP-07 — In-scope recovery boundary, out-of-scope handling and consented handoff | Primary TC-010; secondary TC-009; conditional TC-006/027 | **Negative/consent controls:** genuine unrelated TC-010 should not receive cancelled-order age/education intake; unpaid cancelled-order compensation is not automatically unrelated. No new transfer trigger follows from timing. |

This covers all 15 inventory TCs through their existing families; it does not
expand the other 12 journey specifications. The narrow direct-GM-status control
is existing `VAR-TC-027-F`; GM App submit-only is `VAR-TC-027-G`. TC-003's B/C/D
remain `VAR-TC-003-A/B/C` with their agreed behavioral/coverage distinction.
No GF or combined-journey bypass is inferred from the GM-only exception.

### Existing defect groups and direct historical evidence

| Group | Direct evidence relevant to OD-004/005 | Wider impact and limits |
|---|---|---|
| DG-003 — education/timing | DF-005/F01 (repetition); DF-006/F02, DF-007/F02, DF-009/F02, DF-010/F01, DF-014/F01, DF-015/F02–F03 (education/applicability); DF-018/F01–F02 (trigger/fix-fixture conflict). Direct TC union: TC-004/005/007/008/027/028. | **Core direct group.** Other timing/direct-navigation controls are plausible regression scope, not new DF associations. DF-014/018 remain owner-resolved; DF-010/F02's general positive feedback is not a complete pass. |
| DG-002 — context/intent | DF-006/F01, DF-007/F01, DF-009/F01 concern inquiry clarification; DF-011/F01 positively records collecting a missing cancellation date; DF-015/F01 positively records elicited intent. | **Direct intake evidence; plausible shared impact.** Reasking a known goal differs from clarifying an age-only opening. DF-002/F01 does not establish that ambiguous “food cancel” necessarily identifies GF. |
| DG-004 — status navigation/observations | DF-004/F01 and DF-007/F03 concern date-selector advice; DF-008/F02 and DF-009/F03 are positive missing-order recovery observations. | **Adjacent direct findings; plausible boundary impact.** Routing age is not the same as a History/date-selector recovery instruction. Actual missing-order preconditions and OD-007 remain necessary. |
| DG-005 — role/access | DF-003/F01, DF-004/F02, DF-007/F04, DF-009/F06 and DF-011/F03 concern role guidance/observations. | **Plausible downstream impact**, not evidence of a timing-policy defect. Successful-path reminder applicability remains OD-010; early education or date collection does not resolve it. |
| DG-006 — status-conditioned submission | DF-009/F04–F05 and DF-017/F01–F02 retain unresolved-goal/continuation and approval-aware adaptation evidence. | **Plausible priority interaction.** OD-002 already settles its bounded GF handling; generic follow-up must not reinstate automatic duplicate submission or imply original-target coverage. DF-016 remains a positive TC-029 control. |
| DG-007 — consent/finish/scope | DF-005/F02, DF-014/F04 and DF-015/F03–F04 report disconnect/access/ending concerns; other group members retain their separate transfer contexts. | **Plausible** premature finish or unnecessary handoff impact. A factual timing answer may be useful without screen access; the financial issue is not thereby resolved. Disconnect cause and exact consent remain unverified. |
| DG-008 — GM notice | DF-014/F02 directly reports a delayed notice, not wholly absent content. | **Adjacent OD-006 dependency:** preserve once-only timing before applicable navigation; a general education decision does not settle “will be partial” certainty. Parent historical closure is retained. |
| DG-001 / DG-009 | Opening and voice evidence remain separate. DG-009 includes direct silence/divergence reports on TC-026/003 and disconnect/cutoff contexts on TC-004/010. | **Boundary controls**, not demonstrated education/date common causes. Preserve entry ownership, audible evidence limits and OD-013; no voice-setting change or numerical SLA follows. |

Future review should select original trigger profiles, opposite-trigger negative
controls, applicable recovery/offer outcomes and boundary-date examples only where
their prerequisites are defined. Record source, exact condition, reviewer and
separate behavior/coverage criteria for each selection. This is impact analysis,
not an execution authorization, regrade or new defect/closure finding.

## 6. Human-review frontier

**Q1–Q7 are now agreed with the qualifications below.** They no longer require an
internal answer. Q numbers in this section are **Round 3** identifiers, distinct
from settled OD-002 Q1–Q4. The remaining frontier concerns dependent contracts,
policy/UI/timing evidence and formal acceptance, not a repeat of these choices.

### Recorded Q1–Q7 approval and provenance

- **Decision version/date:** `OD004-OD005-REVIEW-0.2`, recorded 2026-11-03.
- **Decision-maker/source:** the requesting project-side user's explicit message
  beginning “I have reviewed OD-004/005 Q1–Q7.” Personal name, official role and
  formal Grab/business/benchmark or QA authority were not supplied.
- **Status/scope:** **VERIFIED [POC] / ENGINEERING_AGREED_POC** for the seven
  qualified drafting choices only; all are provisional internal POC engineering
  agreements. Q2/Q7 are conditional; Q4 is approved as modified, not universally.
- **Authority limit:** no formal Grab approval, Cognigy/Knowledge modification,
  Python runner development, live test, evidence regrade or full Business
  Acceptance Baseline freeze. No runtime conformance or current UI acceptance is
  established. Earlier engineering decisions and original historical statuses
  retain their scope.

| Round 3 choice | Recorded disposition and qualification | Affected drafting scope / retained dependency |
|---|---|---|
| Q1 / OD-004 | **Approved:** defined recent age-only opening receives applicable recent education without an unnecessary goal question; no inference of preparation/packing. | T01; BR-001/003/004, TC-001/025 controls. Unchanged J01/J02 source conflict and formal certification retained. |
| Q2 / OD-004 | **Approved conditionally:** explicitly requested/accepted navigation takes priority over unsolicited routine education, including same-order age correction; preserve mandatory disclosures and necessary intake. | T10/T13; BR-001/002/003/005/009. Beyond-only S06 remains an implementation conflict. Detailed admission/state/coverage contract pending; no runtime authorization or official early-form support. |
| Q3 / OD-004 | **Approved:** clear upfront TC-027 dual request proceeds without unsolicited timing or redundant accepted-guidance offer; retain applicable GM partial notice, computer-Portal transition, preferences and status observation before submission decisions. | T08; JRN-TC-027 M02 applicability, BR-003/005/008/009/018. Original E16 conflict retained; OD-003 transition remains agreed; OD-006 notice certainty is not newly approved. |
| Q4 / OD-004 | **Approved as modified, conditional:** clarify once only for genuinely ambiguous assistance. Never redundantly clarify a clear status-check request. Preserve direct GM status-only exception and avoid unnecessary age/loudspeaker intake. | T09/T12; BR-001/005. Full context controls, not an isolated phrase. No new general age bypass or mandatory ambiguity question. |
| Q5 / OD-004 | **Approved:** answer new timing question after declined guidance without automatically repeating the same offer; new explicit guidance may change branch. | T03/T04/T14; BR-003/014. Entry/Tool contract and OD-009 finish/consent limits remain separate. |
| Q6 / OD-005 | **Approved:** explicit cancellation-age fixtures, declared **Asia/Kuala_Lumpur (UTC+8)** test reference and reproducible same-session date assumptions; documented relative expressions allowed. Routing cancellation age is distinct from approval after order made. | T17 / §3; BR-002/003. Absolute-date, midnight-boundary and official business-calendar conventions remain unresolved; export's fixed-offset clock is not a named-zone/runtime-policy certification. |
| Q7 / OD-005 | **Approved conditionally:** qualified KB continuation of the supported request process with available evidence/information when no photo; retain evidence recommendations. No promise of eligibility, acceptance, completeness or approval. Flag separately established mandatory UI/business-policy conditions for review. | T16 / §3; BR-013 with BR-010/011/012 boundaries. No condition is silently waived; exact wording/mandatory UI/final evidence policy remain OD-011/014. |

**Approval evidence — user's decision text, preserved verbatim:**

> I have reviewed OD-004/005 Q1–Q7.
>
> Approve the following as provisional internal POC engineering decisions, with these qualifications:
>
> **Q1 — YES.** For the defined recent age-only opening, deliver the applicable recent-order education response without an unnecessary additional goal question. Do not infer that food preparation or item packing has been confirmed.
>
> **Q2 — YES, CONDITIONAL.** Prioritize explicitly requested or accepted navigation over unsolicited routine education, including after a same-order age correction. Preserve applicable mandatory disclosures and necessary intake. Record the current older-order-only guidance Tool restriction as an implementation conflict; this decision does not authorize a runtime change or establish that early form acceptance is officially supported.
>
> **Q3 — YES.** For TC-027's clear upfront dual request, proceed without unsolicited timing education or repeating an already accepted guidance offer. Preserve the applicable GrabMart partial-compensation notice, explicit computer-Portal transition, merchant preferences, and status observation before submission decisions. Retain conflicting original benchmark text for review.
>
> **Q4 — MODIFY: CONDITIONAL YES, NOT UNIVERSAL.** Clarify once only when the merchant's requested assistance is genuinely ambiguous. A clear status-check request must not trigger redundant intent clarification. Preserve the existing direct GrabMart status-only POC exception and do not add unnecessary age/loudspeaker intake.
>
> **Q5 — YES.** Answer a new timing question even after the merchant declined previous guidance. Do not automatically repeat the same declined offer. A new explicit guidance request may change the applicable branch.
>
> **Q6 — YES.** Use explicit cancellation-age fixtures with a declared Asia/Kuala_Lumpur (UTC+8) test reference and reproducible same-session date assumptions. Allow documented relative expressions. Keep cancellation-age routing distinct from approval timing measured after the order was made. Absolute-date, midnight-boundary and official business-calendar conventions remain unresolved until specified.
>
> **Q7 — YES, CONDITIONAL.** When the merchant lacks a photo, follow the qualified KB guidance permitting continuation of the supported request process with available evidence and information. Do not promise eligibility, acceptance, completeness or compensation approval. Preserve evidence recommendations and flag any separately established mandatory UI or business-policy conditions for review.
>
> Record these as internal POC engineering agreements only, not formal Grab approval.
>
> Update the OD-004/005 review and relevant Problem #2 documents. Preserve the original benchmark, historical statuses, all earlier engineering decisions and version history.
>
> Explicitly distinguish resolved drafting choices from remaining policy, Tool-contract, UI and timing conflicts.
>
> No Cognigy modifications, Knowledge changes, Python runner development, live tests or full Business Acceptance Baseline freeze.
>
> After updating the documents, summarize the remaining blockers and propose the next focused review batch.

**Superseded interpretation:** v0.1's unanswered status and recommendations are
historical. Q4 must not be read as making the example status phrase automatically
ambiguous. Q6 now explicitly names the agreed test-reference zone. Q7's earlier
“no photo prerequisite” recommendation is qualified by supported-process scope
and review of any separately established mandatory UI/business-policy condition;
it does not waive such a condition or promise completeness. Q2 settles priority,
not a Tool contract or runtime change. The user's qualifications govern over any
broader reading of the historical questions below. No prior engineering agreement
is superseded by this recording.

### Original Round 3 questions — historical

The following v0.1 questions and recommendations are retained unchanged for
traceability. Their pending wording is historical; the recorded answers above
are the current internal decision state.

❓ **Q1** - **Recent age-only opening:** Shall the first recent, age-only response
use LOB-specific education, its recent evidence reminder and “anything else,”
rather than another open-goal question?

➡️ **Recommended: yes.** Prefer J02's specific rule and TC-001/025's target over
J01's unqualified age-only sentence, **only when no actual question or navigation
goal was supplied**. Consequence: preserves those benchmark education targets;
the contrary Job sentence needs an explicit precedence correction in later work.

---

❓ **Q2** - **Requested recent guidance:** Outside the existing GM-only exception,
shall a clear navigation request or accepted offer take priority over routine
recent education, including after a same-order correction makes the order recent?

➡️ **Recommended: yes, as a new internal direction.** Preserve the request and
allow only already-supported routes after necessary intake. Consequence: this
requires a later coherent recent-guidance admission contract because the current
standard Tool is beyond-only; current conformance remains unestablished. It grants
neither early form acceptance nor an age/LOB/preferences bypass. Declined guidance
in TC-002/026 remains declined. The detailed admission/fixture decision comes next.

---

❓ **Q3** - **Older GM upfront dual request:** Shall TC-027's explicit upfront
status-plus-submission request start guidance without an unsolicited timeline or
another offer of the guidance already requested?

➡️ **Recommended: yes.** Follow J04/J05's documented direct-intent rule, retaining
the GM notice, agreed App→computer-Portal readiness and status-before-submission
observation. Consequence: E16's education/re-offer becomes a retained benchmark
conflict; elicited older inquiries such as TC-029 still receive education/offer.

---

❓ **Q4** - **Ambiguous upfront status interest:** When an older-order opening only
says “I want to know about compensation status,” without a clear factual question
or request for steps, shall we clarify the help needed once?

➡️ **Recommended: yes.** Do not silently classify generic curiosity as either
timeline education or walkthrough consent. Consequence: this ambiguous entry adds
one clarification; clear factual questions, explicit navigation and J04's defined
older-open-question responses retain their own handling.

---

❓ **Q5** - **Another timing question after a decline:** Shall the Agent answer a
later factual/timing question without automatically re-offering the same declined
walkthrough when the order and goal have not changed?

➡️ **Recommended: yes.** Make J04's timeline-plus-offer rule conditional on this
decline history. Consequence: the new question still receives a useful answer,
but does not regenerate the same offer; a new explicit navigation request or
materially changed need is assessed under its applicable entry rules.

---

❓ **Q6** - **Internal date-fixture convention:** Shall this review's initial
fixtures use an explicit cancellation age and a declared, same-session-day UTC+8
reference, with only documented unambiguous relative aliases?

➡️ **Recommended: yes.** Match the inspectable initialization-clock model without
inventing calendar arithmetic. Consequence: arbitrary dates/timestamps and
cross-midnight fixtures remain unaccepted pending a defined convention; actual
initialization must later be evidenced rather than assumed injectable. This is
not approval of an official timezone, holiday calendar or payment clock.

---

❓ **Q7** - **Known unavailable photo:** When the merchant says they have no photo
to provide, shall qualified KB no-photo continuation take precedence over an
otherwise mandatory take/attach instruction?

➡️ **Recommended: yes, narrowly.** Preserve stage/LOB reminders when applicable,
but do not make producing a photo a prerequisite to continuing; explain clear
supporting information and conditional review without inventing substitutes. Consequence:
this adds a scoped semantic exception to current Job wording, to be captured in
OD-011's later text register. It grants no evidence exemption or eligibility/award.

### Remaining blockers and next focused review

| Remaining category | What is unresolved / effect on acceptance |
|---|---|
| **Tool-contract / implementation — OD-004 Q2** | Standard `start_guidance` remains beyond-only; Job recent/correction behavior and education-marker semantics have not been reconciled with agreed intent priority. Define recent admission, retained consent/preferences/location and corrected-route state before asserting an executable accepted-recent path. No current conformance is claimed. |
| **Timing — OD-005** | Absolute-date normalization, midnight boundaries/refresh, official calendar/holidays/cutoffs/effective dates and precise approval/payment clocks remain unspecified. The agreed Asia/Kuala_Lumpur same-session fixture reference resolves internal drafting only. |
| **UI / policy — OD-005/014** | Early form acceptance, authenticated routes/access, evidence substitutes and final eligibility/status/duplicate rules remain unconfirmed. Review the effect of any separately established mandatory UI/business-policy condition on no-photo continuation; Q7 does not waive it or guarantee acceptance/completeness. Approved-but-unpaid remedies and 90/5/3-day applicability remain unresolved. |
| **Controlled content — OD-006/011** | GM notice certainty and a versioned exact-text register remain open. Capture Q7's conditional semantic qualification without silently changing deployed text or inventing final evidence policy. |
| **Fixture/access/consent — OD-007/010/009** | Missing-order versus missing-control and first-stuck-step facts; universal role-reminder applicability and unavailable-access outcomes; explicit finish/transfer signals. Agreed TC-006/009/027 choices and Q5 are inputs, not reopened questions. |
| **Formal acceptance/evidence — OD-012/013/015** | Named business/benchmark and QA reviewers, original-source certification, current regression/closure evidence and voice/audibility evidence remain outstanding. Internal agreement supplies none of these or a baseline freeze. |

**Recommended next focused batch: OD-004 Q2 — recent-navigation entry and Tool
contract**, as a documentation review. Its prerequisites are now settled, while
the beyond-only gate directly conflicts with the agreed priority. Produce:

1. A bounded admission/continuation matrix for requested versus accepted recent
   status, submission and dual guidance, including same-order age correction;
   retain mandatory disclosures, genuinely needed intake and the protected GM-only
   exception. Do not fabricate an older age/threshold to pass the gate.
2. A proposed Tool/state contract distinguishing retained intent/consent/preferences,
   supported current location and education actually delivered from a marker merely
   set by the resolver. Identify changes requiring separate implementation approval.
3. Separate behavior/coverage criteria for the accepted-recent branch and existing
   declined-offer TC-002/026 controls; identify unsupported early-UI outcomes as
   specification gaps, without inventing a route, deadline or remedy.

This narrow dependency review precedes the previously suggested OD-007/010/009
fixture/access/consent batch; it does not restart OD-004/005 Q1–Q7. Obtain OD-014
owner evidence and OD-015 reviewer appointments alongside it; follow with
OD-006/011 content decisions. The recommendation is **PROPOSED**, not approval of
the future contract, new variants, implementation or execution.

## 7. History and verification

| Version / date | Preserved basis / change |
|---|---|
| `OD002-REVIEW-0.2` / 2026-11-02 | Completed internal OD-002 agreement remains the governing record for Q1–Q4; the Round 1 record and original source packs remain preserved. |
| `OD004-OD005-REVIEW-0.1` / 2026-11-03 | Coupled source-grounded trigger/timing review and shared impact; new human choices remain PROPOSED. No broader acceptance freeze or execution. |
| `OD004-OD005-REVIEW-0.2` / 2026-11-03 | User-approved qualified Q1–Q7 recorded as provisional internal POC agreements; current trigger/convention dispositions and dependent blockers synchronized. Q4 conditional modification, Q6 named test reference and Q2/Q7 limits explicit. No formal approval, runtime change or execution. |

**Pre-review snapshot:** [completed OD002-REVIEW-0.2 state](../../reference/UC4_Problem2_OD002_Review_v0.2_2026-11-03.zip),
SHA-256 `79f89595cdffd363504a5a54e4f5d1a0dab39681b8a1c0893443667f27f5c202`.
Created on 2026-11-03 before edits; ten repository-relative members preserve all
nine Problem #2 documents and the glossary byte-for-byte. It is local history,
not an externally supplied policy release. Earlier archives retain their hashes.

**Pre-approval v0.1 snapshot:** [exact reviewed documents](../../reference/UC4_Problem2_OD004_OD005_Review_v0.1_2026-11-03.zip),
SHA-256 `1194f6dcf1a230bd42ad925035c843943018196dd10688c0e00e554fdf850460`.
Created before this agreement update; eleven repository-relative members preserve
the ten Problem #2 documents plus glossary byte-for-byte, including all original
Round 3 questions, proposed interpretations and the v0.1 audit.

### Completed offline audit — 2026-11-03

**Historical v0.1 audit:** the following counts and zero-new-approvals statement
describe the pre-approval review, not this v0.2 agreement-recording update.

Executed from the repository root:

```powershell
.\.venv\Scripts\python.exe 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-od004-od005-review-2026-11-03\verify-review.py'
```

| Check | Actual result |
|---|---|
| Documentation integrity | **PASS:** 10 Problem #2 documents; 115 relative links/anchors; Markdown table widths, ID references and newly added whitespace checked; `git diff --check` passed. |
| Source authentication | **PASS:** 26 published artifact/member/text fingerprints, including nine new static-member fingerprints and the ten-member pre-review snapshot; 311 nonempty original workbook values authenticated without formula recalculation. |
| Review's source ledgers | **PASS:** 17 KB article metadata records, 20 chunk/claim rows, 15 exact Job-heading rows; all 14 routing cutoff values agree across the review, Code text and KB. Tool schema/gate and initialization wiring inspected as data. |
| Review structure and shared impact | **PASS:** 18 trigger rows, seven consecutively numbered unanswered questions, all seven BP and nine DG references checked against existing membership; all 18 original direct DF–TC associations checked against WB. |
| Preserved model/evidence identities | **PASS:** 15 TC inventory/mapping rows, 18 historical DF records, 49 atomic findings, seven BP rows, 15 TC-family rows, nine DG rows, 20 BR rows, three pilot bodies and 18 variant rows unchanged from the snapshot. |
| Preserved agreements/history | **PASS:** OD002-REVIEW-0.2 and the Round 1 agreement remain byte-identical; all snapshot members match pre-edit hashes; original glossary bytes remain a prefix. |
| Scope preservation | **PASS:** eight scoped pre-existing documentation files changed; the other 167 captured repository files, 467 report files and six external sources remain byte-identical. Two new repository files are this review and the preservation ZIP. Repository HEAD unchanged. |
| Execution/approval scope | Zero runtime Tool executions, runner tests, live requests, saved-evidence regrades or new approvals. Both verdicts remain `NOT_RUN`; baseline remains **NOT FROZEN**. |

Audit evidence is retained in
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-od004-od005-review-2026-11-03`:
`preservation-before.json`, `static-source-projection.json`,
`workbook-projection.json`, `kb30-source-projection.json`, `verify-review.py`,
`documentation-verification.json` and `review-documents.diff`. The linked original
archives/member locators and fingerprints remain the primary provenance. The
audit validates documentation and preservation, not Agent behavior or policy.

### Agreement-recording audit — 2026-11-03

Executed offline after recording the qualified approvals:

```powershell
.\.venv\Scripts\python.exe 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-od004-od005-agreement-2026-11-03\verify-agreement.py'
```

| Check | Actual v0.2 result |
|---|---|
| Approval/current-state consistency | **PASS:** seven qualified internal choices recorded; no unanswered Round 3 choices and no formal approval recorded. Q2/Q7 conditional, Q4 modified/conditional, Q6 named test reference and the user's quoted qualifications checked. |
| Documentation | **PASS:** 10 Problem #2 documents, 121 relative links/anchors, valid ID references/table widths and no new trailing whitespace; `git diff --check` passed. |
| Sources/history | **PASS:** 27 source/archive/member/text fingerprints, including the eleven-member pre-approval snapshot; 311 nonempty WB cells authenticated without recalculation. Nine static-member, 15 Job-heading and 20 KB claim rows preserved; 17 KB metadata records and 14 routing values checked. Original seven questions/recommendations and v0.1 audit preserved as history. |
| Identity/evidence preservation | **PASS:** 15 TC inventory/DF-mapping rows, 18 historical DF records, 49 atomic findings, seven BP rows, 15 TC-family rows, nine DG rows, 20 base BR rows and 18 variant rows unchanged. TC-027's milestone applicability is updated for Q3; source inventory and target/variant identities remain. |
| Prior agreements and protected cases | **PASS:** Round 1 and OD002-REVIEW-0.2 records plus glossary byte-identical; TC-003 status/coverage content and TC-006 pilot body preserved. GM-only exception and OD-002 protected trigger rows unchanged. TC-003 M02 only gains the current applicability reference. |
| Change boundary | **PASS:** eight Problem #2 documents updated; other 169 captured repository files, 467 report files and six external sources byte-identical. The only new repository file is the pre-approval snapshot. Repository HEAD unchanged. |
| Execution scope | Zero runtime changes, runner tests, live requests or saved-evidence regrades. Both verdicts remain `NOT_RUN`; full Business Acceptance Baseline remains **NOT FROZEN**. |

Evidence directory:
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-od004-od005-agreement-2026-11-03`;
files `preservation-before.json`, `capture-before.py`, `verify-agreement.py`,
`agreement-documents.diff` and `documentation-verification.json`. This audit
establishes approval-record/source preservation and documentation consistency,
not runtime conformance or formal policy/UI acceptance.
