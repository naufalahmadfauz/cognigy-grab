# Problem #2 — complete Business Journey Specification catalog

**Catalog:** `P2-JOURNEYS-0.4` · **2026-11-04** · **15 full specifications for review**.
Included in `P2-BASELINE-CANDIDATE-0.1`, **NOT FROZEN**. The established filename is
retained for link continuity. The pre-Phase-4 three-pilot document is archived in
the [completed Q1–Q13 snapshot](../../reference/UC4_Problem2_OD007_OD010_OD009_Review_v0.2_2026-11-04.zip).
All JRN/TC/VAR identities and existing pilot milestone IDs are retained. A complete
specification describes blocked branches as well as assessable ones; it does not
approve every criterion or establish observed behavior.

## Catalog index and version scope

Every JRN below has candidate version `P2-JOURNEYS-0.4`; fixture inputs are proposed
documentation inputs within the named prior agreements. See the [candidate manifest](BASELINE_MODEL.md#phase-4-scoped-acceptance-baseline-review-candidate)
for BR/VAR inclusion, controlled text, dependencies and exclusions. Source keys
retain their definitions in BASELINE_MODEL. R means the qualified recovery review
`OD007-OD010-OD009-REVIEW-0.2`; T means the trigger review
`OD004-OD005-REVIEW-0.2`; their local profile aliases are not global variant IDs.

| Original TC / full specification | Intended target | BP membership |
|---|---|---|
| [TC-001](#jrn-tc-001) | GF recent education and explicit finish | BP-01 |
| [TC-002](#jrn-tc-002) | GF recent follow-up, guidance declined and finish | BP-02; BP-01 prerequisite |
| [TC-003](#jrn-tc-003) | Visible blank GF status → retained review request → full App submission | BP-04; BP-05; BP-06 conditional |
| [TC-004](#jrn-tc-004) | GF older inquiry → education → explicit guidance decline/finish | BP-03 |
| [TC-005](#jrn-tc-005) | GF elicited dual goal → grouped status then App submission | BP-04; BP-05 |
| [TC-006](#jrn-tc-006) | Missing form → authorized access → retry declined → finish | BP-05; BP-06; BP-07 conditional |
| [TC-007](#jrn-tc-007) | GF Date-selector first failure → one repeat → success → submission | BP-06; BP-04; BP-05 conditional |
| [TC-008](#jrn-tc-008) | Missing App link → accepted Portal fallback → submission | BP-06; BP-05 |
| [TC-009](#jrn-tc-009) | Portal submit-only → accepted retry fails → separately consented mock handoff | BP-05; BP-07 |
| [TC-010](#jrn-tc-010) | Clearly unrelated menu-update request → consented mock handoff | BP-07 |
| [TC-025](#jrn-tc-025) | GM recent education and explicit finish | BP-01 |
| [TC-026](#jrn-tc-026) | GM recent follow-up, guidance declined and finish | BP-02; BP-01 prerequisite |
| [TC-027](#jrn-tc-027) | GM upfront dual goal → explicit App-to-Portal transition → submission | BP-04; BP-06; BP-05; BP-07 conditional |
| [TC-028](#jrn-tc-028) | GM older general inquiry → optional-offer/no-offer explicit finish | BP-03 |
| [TC-029](#jrn-tc-029) | GM elicited dual goal → grouped Portal status then submission | BP-04; BP-05 |

**P2-DRAFT-0.2 + P2-ENG-DECISIONS-0.3 / OD002-REVIEW-0.2 / OD004-OD005-REVIEW-0.2 / OD004-RECENT-GUIDANCE-REVIEW-0.2 / OD007-OD010-OD009-REVIEW-0.2 overlays (2026-11-04). Bounded internal choices agreed; dependent pilot acceptance PROPOSED; formal reviewer/approval date unassigned.**

**Limited fixture agreement:** TC-006 declined-retry target (OD-001) and TC-027 explicit App→Portal transition (OD-003) have project-side **internal POC engineering agreement**. TC-009 submission-only target (OD-008) is carried into its full specification below. They **do not resolve the original benchmark conflicts**; read [decision record](ENGINEERING_DECISIONS_2026-11-02.md).

**Round 2:** [OD-002 Q1–Q4](OD002_STATUS_DECISION_REVIEW.md#recorded-q1q4-approval-and-provenance)
are **VERIFIED [POC] / ENGINEERING_AGREED_POC**, approved by the requesting
project-side user on 2026-11-02. Branch A is the original internal target; B/C/D
retain `VAR-TC-003-A/B/C`. Q2/Q3 are explicitly provisional; all four are internal
POC decisions. Formal policy, payment remedies and dependent acceptance remain
pending; the Round 1 agreements remain in force.

**Round 3 agreement:** [qualified OD-004/005 Q1–Q7](OD004_OD005_TRIGGER_TIMING_REVIEW.md#recorded-q1q7-approval-and-provenance)
are **VERIFIED [POC] / ENGINEERING_AGREED_POC**, requesting project-side user,
2026-11-03. Q3 settles TC-027's upfront education applicability below; Q4 permits
clarification only for genuinely ambiguous assistance. The common fixture and
evidence qualifications incorporate Q6/Q7. Q2's intent priority is conditional,
with implementation conflicts and exact recent-entry fixtures still unresolved.
Original target/variant identities, OD-002 verdict distinctions and the GM-only
status exception remain unchanged; these approvals do not certify all pilots.

**Qualified Q8 design overlay:** [Option B approved with seven qualifications](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#recorded-q8-approval-and-provenance),
requesting project-side user, 2026-11-03; **VERIFIED [POC] /
ENGINEERING_AGREED_POC** for documentation/design direction only. The common
contract below incorporates compatible-progress retention, selective invalidation
and actual-output-based education accounting within the Agent-first/minimal-change
boundary. References in retained pilot rows to residual OD-004 now concern exact
implementation/fixture acceptance, not an unanswered Q8. All three pilot targets,
18 registered variant rows, prior agreements and their approval scopes are retained.

**Qualified Q9–Q13 applicability:** the requesting project-side user's [2026-11-04
approval](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#recorded-q9q13-approval-and-provenance)
is **VERIFIED [POC] / ENGINEERING_AGREED_POC**, provisional internal specification/
test-fixture criteria only; Q12 is explicitly provisional. Personal name, official
role and formal business/QA authority were not supplied. The overlay below governs
the retained pilot/variant rows; it does not approve every full variant or regrade
historical evidence. Q1–Q8 and their Agent-first/minimal-change boundary remain.

**Preparer:** AI-assisted analysis. **Business/benchmark and QA reviewers:** to assign.

[Sources and BR register](BASELINE_MODEL.md) · [TC inventory](TC_CLASSIFICATION_MATRIX.md) ·
[Decisions](OPEN_DECISIONS.md) · [Defect impact](DEFECT_GROUP_IMPACT_MATRIX.md)

These specifications use PB §§2–5's **JRN / business requirement BR / VAR** model.
Milestones are business checkpoints, not literal speeches. A composite route below
still requires separate action/wait turns when one-by-one guidance applies.
Beyond the bounded internal agreements, new fixtures, branch interpretations and
mappings are **PROPOSED**; explicit
**CONFLICT** and **UNKNOWN** labels take precedence. Existing approved POC rules
are cited as POC-scoped support, never formal Grab approval.

All fifteen journeys have `behavior_verdict=NOT_RUN`, `coverage_verdict=NOT_RUN`,
`configuration_id=null`, and no new execution evidence. The dialogues in WB are
illustrations, not recordings assessed here. A hypothetical acceptable branch is
not a recorded PASS.

## Common contract

**Applies to every JRN below, including the retained pilots:**

- **Fixture version:** `P2-JOURNEYS-0.4`. Proposed common reference: **2026-11-04,
  Wednesday, Asia/Kuala_Lumpur (UTC+8), same-date conversation**. Recent = explicit
  cancellation age **1 day**; older = **14 days**. These select within/beyond for
  both LOBs under T §3; they do not calculate eligibility or an approval/payment
  date. TC-010 has no age prerequisite. Record intended versus actually observed
  reference/initialization separately in any future execution. No injectable clock
  or absolute-date parser is assumed. Alternate reference fixtures require versioning.
- **Shared fixture facts:** English benchmark context; normal non-safety entry,
  current-order identity and explicit authoritative LOB; no prior education unless
  stated. Record opening already emitted versus outstanding, actual channel and
  later served configuration. Submission fixtures supply authorized access,
  present/absent controls and each merchant observation as declared inputs, not
  authenticated UI facts. Preparation/packing and evidence availability remain
  unknown unless supplied; no fixture asserts individual eligibility.
  Declared inputs become observations only when communicated or recorded at the
  required stage; hidden fixture facts prove no completed action or consent.
- **Shared assessment:** judge applicable requirements on the observed branch,
  then intended target coverage independently. A supported behavior violation may
  coexist with fully traversed coverage; correct alternate handling may leave
  coverage incomplete. Unsupported dependent judgments remain blocked; preserve
  the observed prefix and independently assessable violations. All current verdicts
  are `NOT_RUN`, including any case containing a blocked outcome.
- **Language:** all journeys allow semantic paraphrase, genuine clarification and
  variable turn counts while preserving conditional ordering and observations.
  The [controlled-language register](BASELINE_MODEL.md#controlled-language-applicability-register)
  specifies source-controlled candidates and their OD-006/011 limits. Only an
  applicable, scoped accepted control may become a literal criterion; workbook
  dialogue never supplies one by itself. BR-017/020 govern evidence/assessment.
- **Review ownership:** preparer AI-assisted; internal authority is the requesting
  project-side user's recorded qualified agreements. Formal business/benchmark and
  QA reviewers, accepted versions, date, channel and sampling remain unassigned.
  Full specifications and the candidate are for review, not fresh approvals.

- Record English/voice as the benchmark context; actual channel, execution date,
   business timezone and served revision belong to a future run. “About two weeks”
   denotes the workbook's beyond-threshold fixture, not verified runtime math.
- **Agreed Q6 drafting convention:** explicit cancellation-age fixtures, declared
  Asia/Kuala_Lumpur (UTC+8) test reference and reproducible same-session date
  assumptions; documented relative expressions allowed. Keep cancellation routing
  distinct from approval after order made. Absolute-date, midnight-boundary and
  official business-calendar conventions remain unresolved; actual initialization
  is future evidence, not an assumed injectable clock.
- Preserve clear current-order business line, age, goal, preferences and observed
  location. Ask only for genuinely missing facts. No preparation/packing fact is
  established merely by the sample greeting.
- **Agreed Q8 continuity:** coordinate existing admission/checkpoint validation/
  age-correction handling; a start-gate-only change is insufficient. After a
  same-order age correction, retain compatible intent, consent, preferences,
  location and completed actions. Revisit only actions/observations invalidated by
  corrected facts, such as an incompatible selected date and dependent visibility;
  preserve unrelated completed navigation and applicable observation gates.
  A correction does not replenish retry allowance or imply fallback/transfer consent.
- **Agreed Q8 architecture/delivery boundary:** preserve Agent-first ownership and
  prefer minimal existing instruction/contract changes; no new controller protocol,
  unnecessary persistent walkthrough state or additional Flow infrastructure.
  Education selected internally is not evidence of merchant-facing delivery; use
  actual output and keep audibility evidence separate. Q8 does not authorize early
  eligibility, guaranteed compensation, unsupported submission or policy/UI override.
- Apply the relevant opening/disclosure once (BR-004), semantic/controlled-text
  boundary (BR-020), safety priority and terminal ownership. Exactness must cite
  the applicable source/version in the controlled-language register, subject to
  OD-011; sample wording alone supplies no literal requirement. Retained JOB29
  citations preserve their historical source scope; the new register binds JOB30
  and its Flow Say members.
- Read status from merchant observations; distinguish order visibility, status,
  request-link visibility and form visibility. A navigation acknowledgement proves
  only the immediately requested action. Merchant-reported submission is not
  backend confirmation or approval.
- Allow natural paraphrase, supported clarifications and different turn counts.
   One-by-one pacing and business observation/consent boundaries remain mandatory
   within the proposed accepted profile. Unknown outcomes never imply automatic
   transfer. See BR-001–020 for sources and applicability.
- **Agreed Q7 conditional evidence handling:** when no photo, use qualified KB
  continuation of the supported request process with available evidence/information;
  retain evidence recommendations. Promise neither eligibility, acceptance,
  completeness nor approval. Flag any separately established mandatory UI/business
  conditions for review; do not silently waive them or infer preparation/packing.
- **Agreed Q4/Q5 applicability:** a clear status-check request needs no redundant
  intent question; the GM status-only exception adds no age/loudspeaker intake.
  Answer new timing questions after decline without automatically repeating the
  declined offer. A new explicit guidance request may change branch, subject to its
   actual supported-entry contract and separate observations/consent.

**Coverage protection:** recent education TC-001/025 and declined guidance
TC-002/026 remain distinct controls alongside affected navigation variants and
same-order corrections. [N01–N08/correction profiles](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#proposed-regression-selection)
need reviewed fixture versions/identities; they do not replace existing beyond
targets or any of the 18 variants. Accepted navigation does not cover decline;
starting recent does not cover an active beyond→within correction. Qualified Q9–Q13
now settle scoped recovery/access/consent criteria. The
[completed catalog and candidate](OPEN_DECISIONS.md#phase-4-completion-and-remaining-review)
are ready for criterion-level review, retaining unresolved outcomes explicitly.

### Qualified Q9–Q13 pilot and variant applicability

The pilot bodies, milestone tables, 18 variant rows and target identities below
retain their source/version history. Pending OD-007/010/009 references there now
mean residual full-fixture, unsupported-remedy or formal acceptance gaps. The
retained VAR-TC-006-D universal-reminder question is answered internally by Q11:
authorization stays required; conditional explanations and actual role questions
apply, without a universal successful-path spoken reminder unless separately approved.

| Pilot / existing variants | Agreed criteria carried forward | Coverage / acceptance boundary |
|---|---|---|
| JRN-TC-003 target and VAR-TC-003-D | Q9 conditional History only for missing order, one-by-one action/wait and actual visibility/status observations. Preserve OD-002's visible-blank target and separate A/B/C alternatives; Q8 governs correction-invalidated progress. | No unconditional Date selector for the visible-order target. Recovery success still needs the remaining submission milestones; unsupported further recovery stays UNKNOWN. |
| JRN-TC-003 request path; VAR-TC-003-E/F; JRN-TC-006 and VAR-TC-006-A–E | Q10 separate link/article/scroll/form/authorization/retry consent/result/submission. TC-006's declined-retry primary and successful-retry variant stay distinct. Q11 conditional access explanation, no missing-form-to-wrong-role inference. | Visible form does not prove submission or remove authorization. A successful retry does not cover the declined target; unavailable authorization and post-visibility failure retain their own unresolved outcomes. |
| VAR-TC-006-B/C and supported handoff in applicable pilots | Q13 supported trigger → separate person offer → later explicit acceptance → one Flow-owned mock transfer; retry consent/acknowledgement/silence cannot transfer. | Accepted versus declined person offer are separate outcomes. No generic transfer for an unsupported failure; ordinary closing cannot replace the mock terminal or prove audible completion. |
| JRN-TC-027 and VAR-TC-027-C/D/E | Q9 action/wait and correction distinctions apply to the supported GM route; Q10/Q11 to form access. Q13 preserves the supported GM Portal-unavailable offer and separate acceptance. | Preserve App→computer-Portal readiness, pending submission, style and notice; do not import GF History or turn GM-specific support into a generic GF remedy. Full GM alternative semantics and policy/wording acceptance remain open. |
| Ordinary pilot endings; TC-004/028 controls | Q12 preserves explicit finish and required-offer triggers; acknowledgement, silence or submission does not establish resolution. TC-004 decline/finish and TC-028 optional-offer/no-offer repairs are provisional internal fixtures. | Benchmark fixture changes require reviewer approval. Finish handling is independent of status, form, submission and transfer observations; no new VAR identity is allocated. |

TC-007's agreed Date-selector first failure/repeat/success, TC-008 fallback,
TC-009 submission-only handoff and TC-010's proposed unrelated menu-update fixture
are carried into the full specifications below with their original TC identities.
All fifteen now have review-candidate records. Both verdicts remain `NOT_RUN` and
baseline **NOT FROZEN**.

## JRN-TC-003

### Identity, goal and fixture

- **Source:** `WB:S!A6:F6`; PB §4; PLAN §5/P079–098. **LOB:** GrabFood.
- **Goal:** check cancelled-order compensation status, then submit a review request
  if still appropriate. **Original target:** full App submission happy path.
- **Starting facts:** beyond threshold; App; one-by-one; no loudspeaker; dual goal
  supplied upfront in E6. Existing location and actual status must be observed.
- **Agreed internal branch-driving fixture (Q1):** relevant order visible,
  compensation status explicitly blank/not shown, merchant still wants review;
  request link present, article reached/scrolled, form observed, merchant reports
  submitting. Preserve the supplied in-scope prepared-food and authorized
  Owner/Manager access prerequisites without inferring eligibility. These are
  controlled merchant facts, not authenticated validation or new universal intake
  questions. They make the target testable;
  E6 does **not** explicitly supply a not-compensated status or establish individual
  eligibility. Any eligibility prerequisite beyond the documented request process
  is **UNKNOWN** (OD-002/014). “Not compensated” meaning only unpaid funds does
  not substitute for the explicitly blank-status fixture.
- **Scoped version/authority:** `OD002-REVIEW-0.2` overlays JRN-TC-003's target,
  M05/M06 interpretation and VAR-TC-003-A/B/C handling/coverage. Requesting
  project-side user's 2026-11-02 agreement; formal business/benchmark and QA
  sign-off pending. Dependent BRs and recovery variants retain their prior status.
- **Source conflicts:** E6 uses Date selector even after order visibility;
  JOB30 retains conditional History/date recovery (OD-007). E6's upfront direct
  dual request has an existing POC no-unsolicited-education exception; the older
  open-question response has a different education/offer trigger (scoped OD-004
  disposition in review §5). DF-017's quoted Auto approved reply is absent in E6.

### Milestones and dependency edges

| ID | Applicability / required outcome | BRs; provenance |
|---|---|---|
| M01 | Always: establish/reuse the current GF order, age-dependent context and both goals. | BR-001/002; WB:S!C6:E6; H1 §1 |
| M02 | Conditional education: E6's upfront dual guidance does not receive an unsolicited timeline/re-offer. If dual/status intent instead answers the older-order open question, give the fixed GF timeline, existing-photo reminder and guidance offer, then wait. Apply the qualified Round 3 trigger overlay; residual Tool/policy/timing conflicts remain. | BR-003; JOB30 “OLDER CANCELLED ORDER” / “STATUS AND SUBMISSION TOGETHER”; [OD-002 §5](OD002_STATUS_DECISION_REVIEW.md#5-limited-dependency-disposition); OD004-OD005-REVIEW-0.2 |
| M03 | Before guidance: collect only missing App/style/loudspeaker preferences and continue from known location. | BR-005; WB:S!E6 |
| M04 | Always on status path: App → Orders → Cancelled; observe whether the relevant order is visible. If missing, use the conditional recovery below. | BR-006/007; KB GF-STATUS-C01; JOB29 “GRABFOOD APP — COMPENSATION STATUS” |
| M05 | Once order visible: inspect/read the reported compensation status; distinguish visible blank from unread status, missing order or only missing money. Clarify ambiguity rather than substitute order visibility for status. | BR-007/009; PB §4; KB30 GF-STATUS-C01; JOB30 GF status |
| M06 | After M05: choose using status **and** remaining intent. Under agreed Q1–Q4: visible blank + retained review request → supported request guidance without an eligibility/award claim; reported approved/status-only → explanation without unnecessary duplicate; approved/unpaid → stage explanation/clarification priority; unclear → clarify before status-dependent submission. | BR-009; PB D-05/D-10; [four-branch decision table](OD002_STATUS_DECISION_REVIEW.md#source-backed-decision-table), OD002-REVIEW-0.2; formal policy/remedy limits remain |
| M07 | Target submission: open relevant order details if needed → present Request for compensation link → Report a payment dispute → scroll → observe form visibility. Apply supported access recovery if necessary. | BR-010/012; KB GF-SUBMIT-C01, SHARED-REQUEST-C01; H1 §5 |
| M08 | Only after form visible: order details, GF prepared-food evidence guidance with no-photo qualification, merchant self-submission. | BR-013; KB GF-EVIDENCE-C01/C02; JOB29 request route |
| M09 | After merchant reports submission: acknowledge their action; compensation remains conditional on approval, with no invented result/payment date. | BR-013; JOB29 “POST-SUBMISSION RESPONSE CONSTRAINTS” |
| M10 | At an appropriate branch endpoint: further help/finish handling; do not call the payment issue resolved merely because a request was reported submitted. | BR-014; WB:S!D6:E6; JOB29 “CLOSING” |

Dependencies: `M01 → M03 → M04 → M05 → M06`; `M02 → M03` **only when
M02 applies**; target `M06 → M07 → M08 → M09 → M10`.
For a missing order within M04: `History → wait → Date selector/date → wait →
Confirm → wait → order-visibility observation → wait`; resume opening/status only
after visibility. Each arrow is a dependency, not permission to merge steps.

### Branch and variant register

| Branch / internal variant | Type; merchant-observed condition | Handling and boundary (approval scope in next column) | Label / provenance | Original target coverage |
|---|---|---|---|---|
| `target-submit` / original TC | Normal; relevant order visible with explicitly blank compensation status, review requested, supported form available | M01–M10 as applicable; retain intent/prerequisites and obtain each observation. No eligibility, automatic approval or guaranteed compensation inferred. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q1)** fixture, OD002-REVIEW-0.2; WB:S!D6:F6, PB §4; dependent acceptance and OD-007 remain pending | Potentially complete only after actual full-App target milestones and applicable accepted requirements; current verdict NOT_RUN. |
| VAR-TC-003-A | Alternate; Auto approved, merchant only wants status confirmation | Explain merchant-reported approval and distinguish bank receipt; avoid unnecessary duplicate request, address unresolved concerns and finish only when appropriate. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q2, provisional)**, OD002-REVIEW-0.2; PB §4, WB:D!G21; formal status/duplicate semantics **UNKNOWN**, OD-002/014 | Incomplete submission coverage even if behavior is later judged correct. |
| VAR-TC-003-B | Alternate; Auto approved, money not received | Preserve unpaid concern; distinguish approval/payout/bank receipt. Prioritize explanation and relevant clarification over generic request guidance. No invented remedy, payout date, payment guarantee or automatic transfer. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q3, provisional)**, OD002-REVIEW-0.2; PB §4, KB GF-TIMING/GF-STATUS; Job-source conflict retained, remedy **UNKNOWN**, OD-005/014 | Does not exercise target submission. Bounded explanation can be acceptable; unsupported end-to-end payment resolution remains BLOCKED_SPEC. |
| VAR-TC-003-C | Conditional; unclear/conflicting status | Clarify observed status before choosing a status-dependent submission branch; no invented approval, rejection or forced submission. Continue only once the branch can be supported. | **VERIFIED [POC] / ENGINEERING_AGREED_POC (Q4)**, OD002-REVIEW-0.2; PB §4, PLAN §5; unsupported status meanings/recovery **UNKNOWN** | Incomplete/needs review unless later clarification establishes A and all target stages are actually exercised. |
| VAR-TC-003-D | Recovery; order missing from Cancelled | Conditional History/date/Confirm/visibility sequence, one action at a time; then observed status decision. Repeated unresolved UI failure is **UNKNOWN** beyond supported recovery. | **PROPOSED**; JOB29 GF status; OD-007 | Can complete submission only after recovery plus the remaining target; cannot substitute for a no-recovery fixture comparison. |
| VAR-TC-003-E | Recovery; request link absent in open App order details | Offer Portal and wait; on acceptance use the supported Portal form route with retained preferences. On decline stop that fallback and handle remaining help. | **PROPOSED**; KB GF-SUBMIT, JOB29 missing-link fallback; BR-010/011 | Alternate route: not the intended full App-submission coverage. |
| VAR-TC-003-F | Recovery; article reached/scrolled but form absent | Use JRN-TC-006's conditional role/retry stages. Role access alone does not establish visibility or retry consent. | **PROPOSED**; KB SHARED-REQUEST; JOB29 form recovery; WB:D!G7:G8 | Access recovery and any submission assessed separately; not proof of the normal fixture. |

**Prohibited:** blind duplicate claim, approval = bank receipt, date recovery when
its precondition is absent, merging one-by-one actions, invented screen controls,
missing-photo denial, lost pending submission, or premature successful close.

**Traceability:** direct reports DF-003/004/017; groups DG-002/004/005/006/007/009.
DF-017's adaptive-guidance feedback is not automatically a behavioral failure.
OD-002's bounded choices are agreed; formal semantics and OD-004/007/010/014
dependencies still require their separately scoped review.

**OD002-REVIEW-0.2 applicability:** Q1 adopts A's visible-blank request-for-review
fixture; Q2 adopts B's narrow no-unnecessary-request response; Q3 settles C's
explanation/clarification priority over generic non-arrival guidance; Q4 adopts
clarification before D's status-dependent submission. C's end-to-end payout remedy
remains UNKNOWN, and the unchanged Job-source conflict is retained. See review §4
for independent behavior and original-target coverage criteria. Both verdicts
remain `NOT_RUN`; approval supplies neither evidence nor a completed target.

### Phase 4 reconciliation — TC-003

**BP/BR:** BP-04 primary, BP-05 target, BP-06 conditional; BR-001/002/003/004/005/
006/007/009/010/011/012/013/014/015/019 by branch, with BR-017/020 assessment.
**Fixture inputs:** common older GF reference; clear upfront dual request; App,
one-by-one, loudspeaker=no; relevant order visible in Cancelled, explicitly blank
status, retained review request; link/article/scroll/form individually confirmed;
authorized Owner/Manager access available; merchant reports submission and later
explicitly finishes. Evidence availability is supplied separately, applying Q7 if
no photo. No automatic History/date recovery or unsolicited timeline/re-offer.

**Observations/pauses:** M04 visibility is not M05 status; M07 link, article,
scroll and form reports are distinct. Every one-by-one action waits for its result;
details/evidence/self-submission and M09's report cannot be inferred from entry.
Q9/Q10/Q11 now govern conditional recovery/access; Q12/Q13 govern finish/handoff.
**Language:** common semantic rule; opening/terminal controls, and timeline only
if a new actual timing trigger applies. No universal role-reminder speech.

**Independent criteria:** behavior requires retained intent, correct observed-status
decision and applicable supported route/access/finish. Target coverage requires
M01/M03–M10 and M02 only if its trigger actually applies. OD-002 situation B/C
(`VAR-TC-003-A/B`) cannot cover the App submission target; situation D
(`VAR-TC-003-C`) can only after A's conditions and remaining stages occur. Portal
fallback has alternate-route coverage, not full App coverage. A visible form or
submission report alone cannot complete the normal terminal.

**Trace/regression:** retain direct DF-003/F01–F03, DF-004/F01–F02 and
DF-017/F01–F03, their original memberships DG-002/004/005/006/007/009, and all six
registered variants. Pair TC-005 grouped pacing, TC-007 actual failure, TC-008
fallback and TC-006 form recovery as plausible shared-BR controls, not new direct
DF links. **Authority/dependencies:** OD-002 Q1–Q4, qualified Q1–Q13 and the common
contract; formal status/payment rules, unsupported recovery, OD-011/013/014/015
remain scoped. Retained pilot rows' pending OD-007/010 references mean residual
acceptance, not unanswered Q9–Q11. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-006

### Identity, goal and fixture

- **Source:** `WB:S!A9:F9`; PB §5; PLAN §6/P101. **LOB:** GrabFood.
- **Goal:** obtain a compensation request form through authorized access; respect
  the merchant's retry decision. **Original source conflict retained:** D9 says
  retry declined/soft close; E9 says re-login succeeds and the merchant submits.
  **Internal primary choice agreed under OD-001:** declined retry.
- **Agreed provisional internal primary fixture:** beyond threshold; App, one-by-one,
  no loudspeaker; supported status/submission observations; request link present;
  article open and scrolled, form absent; authorized role available/confirmed;
  merchant explicitly declines the separate retry offer and then finishes.
- E9's contradictory order-visibility replies and role inference are not mandatory
  facts. The primary fixture needs explicit, internally consistent observations
  (OD-007/010). Age, preparation, eligibility and authenticated access are not
  independently verified by this specification.
- DF-008 is directly filed against TC-006, but describes a **missing App link and
  unavailable Portal** deviation. It is not evidence that either conflicting role
  retry target was fully executed.

### Milestones and dependency edges

| ID | Applicability / required outcome | BRs; provenance |
|---|---|---|
| M01 | Establish/reuse order, goal, conditional education and preferences; complete applicable status decision before this submission continuation. | BR-001/002/003/005/009; WB:S!D9:E9; OD-004 |
| M02 | Establish relevant App request link/article navigation. Missing link uses BR-010 fallback, not a premature form-role diagnosis. | BR-010; KB GF-SUBMIT; JOB29 missing-link fallback |
| M03 | Article open → scroll instructed/completed → explicit form-absent observation. | BR-006/012; WB:S!F9/E9; JOB29 form recovery |
| M04 | Explain Owner/Manager submission requirement; if access is unknown, ask and wait. Reuse already confirmed access. Do not assert the missing form proves an incorrect role. | BR-012; KB SHARED-REQUEST-C01; OD-010 |
| M05 | Once authorized access is established, offer one form retry as a distinct question, then wait. Role confirmation is not consent to retry. | BR-012; JOB29 “FORM NOT VISIBLE — ROLE ACCESS AND ONE RETRY” |
| M06 | If retry accepted: instruct one retry of the same supported form route with authorized access; await its observed result. | BR-012; same source; WB:S!E9 |
| M07 | If form becomes visible: resume details/GF evidence/self-submission in selected style; obtain submission report and conditional acknowledgement. | BR-013; KB GF-EVIDENCE, SHARED-REQUEST; WB:S!E9 |
| M08 | If accepted retry fails: speak the supported person offer and wait. The failed retry report is not transfer consent or a finish signal. | BR-015; JOB29 “CONNECTION AFTER FAILED FORM RETRY”; neighboring WB:S!E12 |
| M09 | If person offer accepted on later input: one mock transfer, Flow-owned closing; if declined: no transfer, handle further help/finish. | BR-014/015; JOB29 controlled flow content |
| M10 | If retry declined: no retry/automatic transfer; supported later-attempt/soft-close advice and further-help handling, closing only when finished. | BR-012/014; WB:S!D9; JOB29 form recovery; OD-001 |

Dependencies: `M01 → M02 → M03 → M04 → M05`; unknown role requires a separate
answer before M05. `M05/yes → M06 → visible:M07` or `not-visible:M08 → M09`.
`M05/no → M10`. Initial unsuccessful form access plus **one** accepted retry
is two attempts total, not permission for two additional retries.

### Branch and variant register

| Branch / internal variant | Type; condition | Proposed handling and boundary | Label / provenance | Original target coverage |
|---|---|---|---|---|
| `retry-declined` / agreed internal primary TC | Form absent, access confirmed, retry explicitly declined | M01–M05 then M10; no invented successful form or consented transfer. | **VERIFIED [POC] fixture choice** under OD-001; dependent acceptance remains PROPOSED, original D9/E9 **CONFLICT** retained | Internal target is decline; formal benchmark attribution remains pending. No run/coverage pass claimed. |
| VAR-TC-006-A | Alternate; retry accepted, form becomes visible | M06 → M07, actual merchant-reported submission, appropriate finish. | **PROPOSED**; E9, JOB29 role recovery | Covers successful-retry variant, not a declined-retry target. |
| VAR-TC-006-B | Recovery; retry accepted, form remains absent, later person offer explicitly accepted | M06 → M08 → M09; separate retry and handoff consent, one mock transfer. | **PROPOSED**; JOB29 failed retry; WB:S!E12 supports neighboring behavior | Covers failed-retry/handoff variant, not the agreed internal primary decline. |
| VAR-TC-006-C | Alternate; accepted retry fails, merchant declines person offer | M08 → no transfer → further-help/finish handling; do not renew retry/connection offers. | **PROPOSED**; JOB29 failed-retry decline behavior | Distinct consent-decline coverage. |
| VAR-TC-006-D | Conditional; form visible after initial article/scroll | Skip role-recovery/retry milestones, proceed with supported submission. Whether a universal spoken role reminder is mandatory remains OD-010. | **PROPOSED**; KB request route; JOB29 form boundary | Correct normal access does not test TC-006's missing-form/retry branch. |
| VAR-TC-006-E | Conditional recovery; authorized access unavailable or cannot be established | Clarify access without requesting credentials; do not promise role acquisition, guaranteed form visibility or automatic handoff. Required next disposition remains **UNKNOWN** pending owner review. | **UNKNOWN**; KB documents required role, not every unavailable-role outcome; OD-010/014 | Block the unsupported outcome; do not mark the retry branch covered. |

**Prohibited:** choosing a source outcome silently; conflating absent link with
absent form; assuming role from UI failure; requesting credentials; unconsented
retry/transfer; unlimited retries; or claiming backend submission from “form visible.”

**Traceability:** direct report DF-008; groups DG-006/007, with positive inquiry and
Date selector observations retained as DG-002/004 controls. DF-003/004/007/009/011 are
requirement-related reports on **other** TCs, not direct TC-006 reports. Their
potential impact is explicit in DG-005/007. OD-001 settles the internal target;
formal target adjudication and the applicable role/recovery acceptance remain open.

### Phase 4 reconciliation — TC-006

**BP/BR:** BP-05 primary, BP-06 missing-form recovery, BP-07 only on supported
handoff; BR-001/002/003/004/005/006/007/009/010/012/013/014/015/019 by branch,
BR-017/020 assessment. **Fixture inputs:** common older GF reference; consistent
visible-order/blank-status prefix and retained submission request; App, one-by-one,
loudspeaker=no; request link present, article opened and scrolled, form absent;
authorized access known or explicitly established; separate retry offer expressly
declined; further-help question followed by explicit finish. When intent is elicited
from the older open question, T05's education/reminder/offer and acceptance precede
navigation. This is distinct from TC-003's upfront-dual entry.

**Observations/pauses:** preserve M03 article/scroll/form boundaries and M04 unknown
role answer before M05's separate retry question. The primary executes no retry;
accepted variants observe one additional attempt and its result, then separate
submission or person-offer/acceptance stages. **Language:** conditional role
explanation, no wrong-role diagnosis; common register governs applicable timeline,
older GF reminder, person offer and terminal. Q11 supersedes the historical
universal-reminder question in VAR-TC-006-D.

**Independent criteria:** primary behavior respects refusal and unresolved concern,
offers supported further help and closes only on finish. Coverage requires
M01–M05 and M10 with actual absence, authorization, retry refusal and finish; an
initially visible form or successful/failed accepted retry is not this target.
VAR-TC-006-A needs observed form and merchant submission; B needs supported failed
retry, person offer, later acceptance and one mock terminal; C needs person refusal
and no transfer; D is normal access; E leaves unsupported authorization disposition
blocked. Each retains independent behavior/coverage and its approval state.

**Trace/regression:** direct DF-008/F01–F04 and DG-002/004 positive controls plus
DG-006/007; its missing-link/unavailable-Portal report does not prove primary
role-retry coverage. DG-005 impacts are plausible via shared BR-012, not new direct
DF-003/004/007/009/011 links. Pair TC-008 missing-link, TC-009 failed-retry transfer
and TC-027 shared form access. **Authority/dependencies:** OD-001 primary agreement,
Q9–Q13 boundaries; formal D9/E9 attribution, unavailable authorization/GF Portal,
post-visible submission failure and OD-011/013/014/015 remain scoped. No historical
status is regraded. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-027

### Identity, goal and fixture

- **Source:** `WB:S!A16:F16`; PB §5; PLAN §6/P103. **LOB:** GrabMart.
- **Goal:** status review followed by a request if still needed. **Pilot target:**
  App-selected → explicit computer-Portal transition → one-by-one Portal status →
  conditional Portal submission. D16's broader “App or Portal” allowance remains
  visible; Portal-first does not demonstrate this pilot's App-transition coverage.
- **Starting facts:** beyond/about two weeks; clear upfront dual goal; App selected; one-by-one;
  no loudspeaker. **Proposed target observations:** merchant can access computer
  Portal; relevant order visible but not compensated/no status; form later visible;
  merchant reports submission. E16's “No” alone does not distinguish a missing
  order from a visible order with no compensation status.
- **CONFLICT:** E16 opens App then gives Portal controls, promises bank credit
  within 3–5 business days and allows full-or-partial compensation. F16 says
  Portal-only status. OD-003's explicit transition is agreed internally; its formal
  benchmark conflict remains. **Round 3 Q3 now agrees internal upfront entry
  without unsolicited timing education or redundant guidance offer**; preserve
  E16's contrary text for formal review. Q6 supplies only the internal test-reference
  convention; formal timing, GM status/amount policy and UI limits remain open.
- **Scoped version/authority:** `OD004-OD005-REVIEW-0.2`, requesting user's
  qualified Q3 approval, 2026-11-03, governs M02 applicability alongside OD-003's
  earlier transition agreement. It does not approve GM alternative status semantics
  or remove the mandatory notice, preference retention or status observation.

### Milestones and dependency edges

| ID | Applicability / required outcome | BRs; provenance |
|---|---|---|
| M01 | Establish/reuse GM order, age-dependent combined goal and preferences. Combined status/submission is not the POC status-only intake exception. | BR-001/002/005; WB:S!C16:E16; POC approved policy |
| M02 | **Agreed Q3:** for this clear upfront dual-request target, omit unsolicited timing education and redundant accepted-guidance offer. A different applicable education/timing inquiry follows its own trigger; never recite E16's bank-credit promise. Preserve M03 disclosures/readiness and M05 status observation. | BR-003; JOB30 “OLDER CANCELLED ORDER” / “STATUS AND SUBMISSION TOGETHER”; KB GM-TIMING; OD004-OD005-REVIEW-0.2 Q3; formal WB conflict retained |
| M03 | Before first applicable navigation: existing POC partial notice once; explain that this status check uses computer Portal, then establish readiness/location before Portal controls. Preserve selected style/loudspeaker. | BR-005/008/018; JOB29 “GRABMART GUIDANCE RULES”; OD-003/006 |
| M04 | Once Portal accessible: Finance → wait → Transactions → wait → relevant time period/store → wait → Category / Compensation for cancelled orders → wait. Period/store is one action; Category is separate. | BR-006/008; KB GM-STATUS; JOB29 one-by-one segmentation |
| M05 | Separately ask/read the observed compensation result; distinguish missing order from visible-but-not-compensated and clarify ambiguous “No.” | BR-008/009; JOB29 GM Portal status; WB:S!E16,E18 |
| M06 | Only after M05: choose the supported outcome. If submission remains appropriate/requested, retain that goal and continue on Portal without recollecting preferences. Approval/payout alternatives need their own review. | BR-009; PB D-05; JOB29 “STATUS AND SUBMISSION TOGETHER”; OD-002 |
| M07 | Submission: from current Portal location, Help Centre → wait → Search Bar/search dispute → wait → Report a payment dispute → wait → scroll/form-visibility observation → wait. | BR-006/011/012; KB SHARED-PORTAL/REQUEST; JOB29 Portal route |
| M08 | Form visible: order details, packed-items evidence with applicable no-photo qualification, merchant self-submission; each action separated for one-by-one guidance. | BR-013; KB GM-EVIDENCE-C01/C02; WB:S!E16 |
| M09 | Obtain merchant submission report; acknowledge conditionally, preserve unconfirmed approval/payment; finish only when appropriate. | BR-013/014; JOB29 post-submission/closing |

Dependencies: `M01 → M03`; `M02 → M03` only if M02 applies;
`M03/readiness → M04 → M05 → M06`; target `M06 → M07 → M08 → M09`.
No request-entry actions belong in the status segment before M05. No Portal
controls belong before the platform transition. Missing-order recovery returns
to an observation, not directly to submission.

### Branch and variant register

| Branch / internal variant | Type; condition | Proposed handling and boundary | Label / provenance | Pilot target coverage |
|---|---|---|---|---|
| `app-to-portal-submit` / original TC pilot | Normal; App preference, Portal available, visible order without compensation, submission needed | Agreed upfront entry without unsolicited timeline/re-offer; applicable notice and explicit transition/readiness, M04/M05 status observation, then supported Portal submission. | **VERIFIED [POC]** OD-003 transition and qualified Round 3 Q3 entry; remaining acceptance **PROPOSED**, original benchmark **CONFLICT** retained | Complete only with the agreed App transition and all applicable target stages observed under reviewed requirements. |
| VAR-TC-027-A | Alternate; merchant starts in Portal | Begin at confirmed Portal location; same status/conditional submission dependencies, no redundant reopening or platform question. | **PROPOSED**; D16 allows Portal; JOB29 GM Portal route | Does not prove the internally agreed App-transition target; formal benchmark adjudication remains pending. |
| VAR-TC-027-B | Alternate; order already compensated/approved | Clarify whether the concern is status only or unpaid funds; use supported explanation, avoid unnecessary duplicate request and premature close. | **PROPOSED**; KB GM-STATUS/TIMING, PB §4 reasoning adapted to GM; exact status semantics **UNKNOWN**, OD-002 | Alternate behavior, not original submission coverage. |
| VAR-TC-027-C | Recovery; no computer-Portal access | Supported POC access-assistance offer, then wait. Explicit later acceptance → one mock transfer; decline → further-help handling; gained access → resume known route. Never invent App status or close solely for missing access. | **PROPOSED** for acceptance; JOB29 “GRABMART PORTAL UNAVAILABLE — SUPPORT OFFER”; direct historical report WB:D!G18, owner-resolved per PLAN P012 | Does not complete status/submission unless access is recovered and the target then finishes. Each consent outcome must be recorded separately. |
| VAR-TC-027-D | Recovery; order absent from selected report | Recheck period to cover cancellation date, retaining store/Category; wait for a new observation. No GF History route or inferred rejection. | **PROPOSED**; JOB29 GM Portal status; KB GM-STATUS limitation | Can reach later target only after supported recovery; preserve different fixture identity. |
| VAR-TC-027-E | Conditional recovery; submission article scrolled, form absent | Apply role/access → one offered/accepted retry → observed result, as JRN-TC-006. Any failed-retry handoff still needs separate consent. | **PROPOSED**; KB SHARED-REQUEST; JOB29 form recovery | Records recovery variant; normal form-available coverage remains distinct. |
| VAR-TC-027-F | Conditional negative control; explicit GM status-only navigation, age/loudspeaker not supplied | Apply the **VERIFIED [POC]** navigation exception: no age/loudspeaker intake solely to enable status navigation; collect only necessary navigation facts. | **PROPOSED variant** supported by POC approved policy; outside combined target | Does not exercise age-dependent combined status/submission. |
| VAR-TC-027-G | Alternate negative control; GM submission-only, App chosen | Keep supported App submission path; no forced status detour or universal Portal redirect. | **PROPOSED**; KB GM-SUBMIT; JOB29 GM guidance/platform rules | Does not exercise the Portal status/transition target. |

**Prohibited:** Portal controls on an unestablished platform, GM App status,
unconditional Portal routing for App submission-only, bank-credit guarantees,
fixed award claims, repeated notice/preferences, skipped status/form observations,
unconsented handoff, or closing an unresolved access concern as successful.

**Traceability:** direct report DF-014; groups DG-003/004/007/008. Its October 23
owner-reported resolution is retained; drafting a recovery variant does not reopen
it. TC-029/DF-016 are neighboring all-at-once control evidence, not proof this
pilot or any new variant passed.

### Phase 4 reconciliation — TC-027

**BP/BR:** BP-04 primary; BP-06 transition, BP-05 conditional request, BP-07 only
supported unavailable-Portal handoff; BR-001/002/003/004/005/006/008/009/011/012/
013/014/015/018/019 by branch, BR-017/020 assessment.
**Fixture inputs:** common older GM reference; clear upfront dual request; App
selected, one-by-one, loudspeaker=no; computer Portal becomes accessible and ready;
relevant order visible with compensation status absent, retained review request;
authorized access, article/scroll/form confirmations; merchant submission then
explicit finish. Packed-items evidence availability is an explicit fixture input,
not inferred packing or eligibility. Amount/alternative-status semantics remain
qualified; absent status is not proof of rejection or entitlement.

**Observations/pauses:** M03 readiness precedes Portal controls. M04 period/store,
Category and M05 result remain separate actions/observations. M07 article, scroll
and form are separately established before M08/M09. Q3 suppresses unsolicited
timing/re-offer for this upfront dual target; applicable notice remains once.
**Language:** common controls include GM notice/redirect, qualified against OD-006/
011; never substitute E16's bank-credit or full-award statements.

**Independent criteria:** behavior preserves known goal/preferences, explicit
transition and supported status/conditional submission; target coverage requires
App-selected→Portal-ready plus M04–M09 and applicable M01/M03, not a Portal-first
or access-blocked ending. M02 applies only on a separate actual education trigger.
VAR-TC-027-C transfer is not full status/submission coverage; D requires a new
visibility observation before continuation; E needs its own access/consent evidence.
Protect F's clear GM status-only exception: no unnecessary age/loudspeaker intake;
its new dual/submission intent exits the exception. G preserves App submit-only.

**Trace/regression:** direct DF-014/F01–F04, DG-003/004/007/008; historical owner
resolution remains. TC-029/DF-016 is a neighboring grouped positive control, not
another direct DF-014 link. Include all seven existing variants and Q8 correction
controls by applicability. **Authority/dependencies:** OD-003 transition, Round 3
Q3 entry and qualified Q8–Q13; GM alternative policy, notice certainty/exactness,
unsupported recovery and formal attribution/sign-off remain scoped. Verdicts:
`NOT_RUN / NOT_RUN`.

### Process-family alignment and pilot review gates (proposed)

| Pilot | Primary / conditional BP mapping | Decision gating target coverage | What reviewers must inspect first |
|---|---|---|---|
| JRN-TC-003 | BP-04 primary; BP-05 submission; BP-06 if order/link/form unavailable | OD-002 Q1–Q4 and applicable qualified Round 3 drafting choices agreed; formal policy/remedy and residual OD-004/005/007/010/014 dependencies retained | Agreed visible-blank review-request target and retained intent/prerequisites; correct B/C is **not** original submission coverage, D needs an actual A continuation. |
| JRN-TC-006 | BP-05 primary; BP-06 form-recovery; BP-07 only if later consented transfer | OD-001 internal decline choice agreed; formal attribution pending; OD-010 | Preserve decline primary and distinct accepted-retry variants; inspect role/consent conditions, not a reopened primary choice. |
| JRN-TC-027 | BP-04 primary; BP-06 Portal redirection; BP-05 request after observed status | OD-003 transition and qualified Round 3 Q3 upfront entry agreed; formal source conflict, OD-006 and GM status/conditional-submission semantics remain | No unsolicited timing/redundant offer for clear upfront dual request; preserve GM notice, App → computer Portal readiness/preferences and observed status before submission decisions. |

The original benchmark and all old defects remain as reported. No primary fixture, business rule, or draft variant receives approval merely from inclusion here. See [Round 1 review worksheet](REVIEW_DECISION_WORKSHEET.md) for selectable review outcomes and named reviewer fields.

## Pilot acceptance and review action

For each run, assess applicable BRs against actual observations and the approved
requirement version, then assess the **target fixture independently**. A supported
alternate may be behaviorally correct while target coverage is incomplete. A
disputed rule yields BLOCKED_SPEC/NEEDS_REVIEW for the affected judgment; retain
independent established violations rather than hiding them behind the conflict.

Before baseline evaluation, reviewers should agree on the fixture, conditional
milestones, controlled-language scope and prohibited outcomes for each pilot.
Record decisions in OPEN_DECISIONS, version the affected JRN/BR/VAR records, and
have business/benchmark and QA reviewers independently annotate the same evidence.
This draft supplies no new transcript, trace, deployment verification or pass.

## JRN-TC-001

### Goal, identity and fixture

**Source:** WB:S!A4:F4; T T01/T03 and §3; KB GF-TIMING-C01/GF-EVIDENCE-C01.
**Goal/target:** understand recent GF cancellation compensation and finish without
navigation. **BP:** BP-01. **BR:** BR-001/002/003/004/013/014; BR-017/020 assessment.
**Inputs:** common recent GF fixture; cancellation age 1 explicitly supplied,
age-only entry, no clear navigation request, no earlier education; preparation and
eligibility unknown. Merchant gives an explicit no-further-help answer. Platform,
style, loudspeaker, status, form and authorization are not needed for this target.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Normal entry: apply once-only opening ownership; establish/reuse GF and supported cancellation age. Clarify only genuinely missing facts. | BR-001/002/004 |
| M02 | First recent age-only education: qualified usual GF approval after order made, then regular payout; recent prepared-food evidence reminder, without asserting preparation. | BR-003/013 |
| M03 | Ask further help; wait for the merchant's actual answer. A new question continues the conversation. | BR-014 |
| M04 | Clear finish: ordinary Flow-owned goodbye and terminal; no duplicate Agent close. | BR-014 |

**Edges:** applicable opening/context → M02 → M03 → explicit finish → M04.
Actual education output is required; an age-resolver selection is not delivery.

### Decisions, variation and forbidden outcomes

A new timing question receives a grounded answer; a nonreceipt follow-up activates
TC-002's distinct offer path; requested/accepted recent navigation is a Q2/Q8
supplemental branch, not this education-only target. Missing/invalid age or unknown
LOB requires clarification. Allow common semantic variation; GF timeline is a
source-controlled candidate, recent GF reminder is semantic, normal terminal is
Flow-owned. Forbid automatic walkthrough/preferences, eligibility/payment guarantees,
bank-credit deadlines, inferred preparation or closing on silence.

### Independent criteria, traceability and review

**Behavior:** correct recent trigger, qualified GF facts/reminder, no unnecessary
goal question and finish handling. **Coverage:** actual M02 content, M03 answer and
M04; recent routing alone or accepted navigation does not complete this target.
**Direct findings:** DF-001/F01 and DF-002/F01, DG-001/002; preserve Closed/Pass
versus Fixed (retest) history. **Regression:** TC-025 LOB comparator; TC-002
follow-up; Q8 N01–N08 requested/accepted navigation and output-delivery controls;
native-empty versus utterance-first opening. No VAR-TC-001 ID is allocated.
**Authority/blockers:** qualified Q1/Q6/Q7/Q8/Q12; BR source authority as registered;
OD-005 official dates/calendar, OD-011 literal register, OD-013 voice and OD-015
sign-off remain scoped. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-002

### Goal, identity and fixture

**Source:** WB:S!A5:F5; T T01/T11/T14; JOB30 FOLLOW-UP/GUIDANCE/CLOSING;
KB GF-TIMING/SUBMIT/SHARED-REQUEST. **Goal/target:** understand possible nonreceipt
after recent education, decline offered guidance, then finish. **BP:** BP-02;
BP-01 prerequisite. **BR:** BR-001/002/003/004/005/010/013/014; BR-017/020 assessment.
**Inputs:** common recent GF fixture; M02 education actually presented; merchant
asks what happens if compensation does not arrive, with no established approval
or present overdue condition; explicitly declines the distinct guidance offer,
then answers further help with clear finish. No platform/access fact is assumed.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Establish/reuse GF and recent cancellation context; applicable opening once. | BR-001/002/004 |
| M02 | Deliver qualified GF recent education/evidence reminder, ask further help and wait. | BR-003/013/014 |
| M03 | Actual nonreceipt follow-up: conditional supported review-request information, without linking eligibility to menu visibility; offer relevant guidance and wait. | BR-003/010/014 |
| M04 | Explicit guidance decline: stop that guidance; ask further help and wait. | BR-005/014 |
| M05 | Explicit finish after M04: ordinary Flow-owned terminal. | BR-014 |

**Edges:** M01 → M02 → actual follow-up → M03 → decline → M04 → finish → M05.
The answer to an offer is distinct from the answer to a further-help question.

### Decisions, variation and forbidden outcomes

Acceptance instead activates Q2/Q8's supported recent-navigation scope and its
UI/implementation limits; it does not cover decline. After decline, answer a new
timing question without automatically repeating the declined offer (Q5). A new
explicit request may change branch; actual reported approval/nonreceipt uses the
protected status/goal distinction, not an invented remedy. Common semantic wording
applies except scoped source controls. Forbid eligibility inference from a link,
unrequested navigation, repeated declined offers, automatic transfer or payout dates.

### Independent criteria, traceability and review

**Behavior:** answer the actual concern conditionally, respect refusal and preserve
unresolved intent until finish. **Coverage:** education, distinct follow-up, offer,
explicit decline and later finish/terminal must all occur; a simple education-only
run covers TC-001, not this target. **Direct findings:** none recorded. **Plausible
regression:** DG-003/006/007, shared trigger/fallback/finish requirements; DG-009
only channel-dependent. Compare TC-026; TC-004 older decline; Q8 N07 accepted-offer
scope as a separate control, with no new VAR allocated. **Authority/blockers:**
Q1/Q5/Q6/Q7/Q8/Q10/Q12; formal financial remedies, early UI access, OD-005/011/013/
014/015 remain scoped. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-004

### Goal, identity and fixture

**Source:** WB:S!A7:F7; PLAN P105; PB §5; T T02/T05/T14; R C1/C6.
**Goal/target:** older GF compensation information without walkthrough.
**BP:** BP-03. **BR:** BR-001/002/003/004/013/014; BR-017/020 assessment.
**Inputs:** common older GF fixture; age-only opening, then general status inquiry
in answer to the open question, not upfront navigation; explicit guidance decline
and a separate finish answer. The added responses repair E7's missing turn under
provisional Q12; the original workbook remains unchanged.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Reuse known GF/older age; applicable opening once; ask the missing goal and wait. | BR-001/002/004 |
| M02 | Elicited general status inquiry: qualified GF timeline, existing-prepared-food-photo reminder, one required status-guidance offer; wait. | BR-003/013/014 |
| M03 | Explicit decline: stop guidance; ask further help and wait. | BR-014 |
| M04 | Later explicit finish: ordinary Flow-owned close/terminal. | BR-014 |

**Edges:** M01 → actual general inquiry → M02 → decline → M03 → finish → M04.
Do not supply preferences or navigation between the offer and its reply.

### Decisions, variation and forbidden outcomes

If guidance is accepted, assess the supported navigation branch separately; it is
not this no-walkthrough target. Genuine timing after decline follows Q5. Common
semantic variation applies around fixed GF timeline and exact existing-photo
source control; preparation is not established by the reminder. Forbid treating
the omitted workbook turn as consent/refusal, silent closing, repeated education
without need, or using DF-018's within-threshold fix note to change this older target.

### Independent criteria, traceability and review

**Behavior:** correct elicited-entry education/offer, honored refusal and explicit
finish. **Coverage:** older fixture plus M01–M04, including both merchant replies;
recent education or accepted navigation does not cover it. **Direct findings:**
DF-005/F01–F02, DF-006/F01–F02, DF-018/F01–F02; DG-002/003/007/009. Preserve
DF-018 owner resolution and its source discrepancy. **Regression:** TC-028's
different offer trigger; TC-001/002 recent controls; TC-005 accepted elicited dual
path; R C1/C6 and Q5 later question. No new VAR allocated. **Authority/blockers:**
Q12 explicitly provisional; benchmark fixture review still required; OD-005/011/
013/015 and any unsupported later outcome remain scoped. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-005

### Goal, identity and fixture

**Source:** WB:S!A8:F8; T T02/T05; JOB30 ALL-AT-ONCE DECISION SEGMENTS;
KB GF-STATUS/SUBMIT/EVIDENCE and SHARED-REQUEST. **Goal/target:** status then
requested App review submission using grouped guidance. **BP:** BP-04; BP-05.
**BR:** BR-001/002/003/004/005/006/007/009/010/012/013/014/019 by applicability;
BR-017/020 assessment. **Inputs:** common older GF fixture; dual goal elicited
after age-only opening, guidance accepted; App, all-at-once, loudspeaker=no;
visible order and explicit blank status, retained submission request, present
link, article reached/scrolled, form visible, authorized access, merchant submission
and later finish. These observations make E8's abbreviated actions testable.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Establish/reuse GF/older context; clarify missing goal and wait; opening once. | BR-001/002/004 |
| M02 | Elicited dual goal: GF timeline/existing-photo reminder and guidance offer; wait for acceptance. | BR-003/013/014 |
| M03 | Reuse or separately collect App/style/loudspeaker preferences; retain both goals. | BR-005/009 |
| M04 | Group supported App status actions only to the next required observation; establish order visibility and actual status. Stop for missing-order recovery if needed. | BR-006/007 |
| M05 | Observed blank status and retained request: choose supported review guidance without asserting eligibility. | BR-009 |
| M06 | Group supported request entry within known conditions: present link → article → scroll; obtain actual form visibility before completion instructions. | BR-006/010/012 |
| M07 | Visible form/authorized access: grouped details, GF evidence and self-submission; wait for merchant submission report. | BR-012/013 |
| M08 | Conditional acknowledgement/further-help question; wait for explicit finish, then ordinary terminal. | BR-014 |

**Edges:** M01 → M02/accept → M03 → M04/status → M05 → M06/form → M07/report → M08.
Grouping never crosses unknown link, status, access, form, consent or submission facts.

### Decisions, variation and forbidden outcomes

Missing order uses conditional History; missing link uses offered/accepted Portal
fallback; absent post-scroll form uses role/one-retry criteria. Already-approved or
unclear status needs its own supported goal/status decision; no mandatory duplicate.
Natural grouped instructions are allowed, with source timeline/reminder/terminal
controls as applicable. Forbid completing request entry on an ambiguous “okay,”
submitting before status, or requiring unsolicited role speech on every successful path.

### Independent criteria, traceability and review

**Behavior:** conditional ordered segments, factual guidance and separate observations.
**Coverage:** elicited dual/accepted offer, grouped App status and full App submission
plus finish; Portal fallback or an already-approved ending is alternate coverage.
**Direct:** DF-007/F01–F04, DG-002/003/004/005. **Regression:** TC-003 one-by-one,
TC-029 GM grouped, TC-007 stuck and TC-008 fallback; existing VAR-TC-003-A–F are
related controls, not TC-005 variants. DG-006/007 additionally plausible via BRs.
**Authority/blockers:** existing POC source rules and qualified Q1–Q13 applicability;
full fixture/BR review, formal policy/UI and OD-005/011/013/014/015 remain scoped.
Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-007

### Goal, identity and fixture

**Source:** WB:S!A10:F10; R A2/A3/A4/A5; JOB30 GF status/GUIDANCE TURN BEHAVIOR.
**Goal/target:** recover an actual failed Date-selector action and finish the GF
status-to-App-request journey. **BP:** BP-06; BP-04; BP-05 when request continues.
**BR:** BR-001/002/003/004/005/006/007/009/010/012/013/014/019; BR-017/020 assessment.
**Inputs:** common older GF entry, status interest elicited after open question,
guidance accepted, retained later submission request; App/one-by-one/loudspeaker=no;
order missing in Cancelled; History successfully opened; first Date selection
fails, one supported repeat succeeds; Confirm succeeds, order visible, status
explicitly blank; link/form later present with authorized access, submission and
finish reported. The failed action is Q9's internal selection of unspecified Step 4,
not a recorded failure in E10 or a correction-invalidated prior success.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Context/opening, elicited GF education/reminder/offer, acceptance and missing preferences, each with required wait. | BR-001/002/003/004/005 |
| M02 | Orders then Cancelled, separately; obtain explicit order-absent observation. | BR-006/007 |
| M03 | Missing order: direct History action and wait for confirmed opening. | BR-006/007 |
| M04 | Date-selector action; wait for actual failure. Repeat that same supported action once with useful context; wait for observed success. | BR-006/019 |
| M05 | Separate Confirm action and result; then separately establish order visibility before opening the order. | BR-006/007 |
| M06 | Observe actual status; retain/request submission intent before the status-dependent continuation. | BR-009 |
| M07 | Link, article, scroll and form observations; supported access conditions before details/evidence/self-submission, one action/wait at a time. | BR-006/010/012/013 |
| M08 | Obtain submission report; conditional acknowledgement/further help; explicit finish and normal terminal. | BR-013/014 |

**Edges:** M01 → M02/absent → M03 → M04/fail → repeat/success → M05/visible → M06
→ supported request → M07/form/submission → M08. Failed action never advances.

### Decisions, variation and forbidden outcomes

If order is already visible, skip History but record incomplete stuck-target
coverage. If repeat fails, order remains missing or no applicable checkpoint
recovery exists, retain observed prefix and block unsupported next disposition.
Q8 correction revisits only invalidated work; it does not consume a fictional
ordinary failure or renew a spent form retry. Common language rules apply; useful
supported action wording may vary. Forbid grouped one-by-one steps, premature
handoff, invented recovery ladder or interpreting E10's success-only script as a repeat.

### Independent criteria, traceability and review

**Behavior:** correct conditional recovery/pacing, one actual repeat and supported
continuation. **Coverage:** all stated failure/repeat/success observations plus
remaining target stages; ordinary success, an age correction or History alone
does not exercise the target. **Direct:** DF-009/F01–F06; DG-002/003/004/005/006/007,
including positive F03/F05. **Regression:** TC-003 visible-order negative control,
VAR-TC-003-D recovery, TC-005 grouping, R A4 unsupported boundaries/A5 correction,
TC-006 form retry distinction. No new VAR allocated. **Authority/blockers:** Q9
internal fixture, Q8 continuity, Q10–Q13 boundaries; formal fixture attribution,
unsupported recovery and OD-005/011/013/014/015 remain. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-008

### Goal, identity and fixture

**Source:** WB:S!A11:F11; R B1/B2; T T05; KB GF-SUBMIT/SHARED-PORTAL/REQUEST.
**Goal/target:** submit through Portal after a genuinely missing App request link.
**BP:** BP-06; BP-05. **BR:** BR-001/002/003/004/005/006/007/009/010/011/012/013/014;
BR-017/020 assessment. **Inputs:** common older GF elicited-status entry and accepted
guidance; App/one-by-one/loudspeaker=yes; order visible, explicitly blank status,
retained request; open order details but request link absent; separate Portal
fallback offered/accepted, Portal accessible; article/scroll/form visible with
authorized access; merchant submission report then explicit finish.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Applicable context, GF education/reminder/offer and acceptance; preferences once. | BR-001/002/003/004/005 |
| M02 | Supported App status actions and actual visible-order/blank-status report. | BR-006/007/009 |
| M03 | Retained request: open order details and obtain explicit absent-link observation. | BR-009/010 |
| M04 | Offer supported Portal fallback; wait for acceptance and actual accessible Portal/readiness. | BR-005/010/011 |
| M05 | Help Centre, Search Bar/search dispute, article opening, scroll and form observation: one action/wait per turn. | BR-006/011/012 |
| M06 | Visible form/authorization: order details, GF evidence and merchant self-submission; each action/result distinct. | BR-012/013 |
| M07 | Merchant submission report; conditional acknowledgement/further help; explicit finish and ordinary terminal. | BR-013/014 |

**Edges:** M01 → M02 → M03/absent → M04/accepted/ready → M05/form → M06 → M07.
Fallback acceptance is neither role-retry consent nor submission completion.

### Decisions, variation and forbidden outcomes

Declined Portal fallback stops that route and retains further-help/finish handling;
unavailable GF Portal has no inherited GM access-transfer entitlement. If Portal
form is absent, use distinct authorized-role/one-retry conditions; a missing App
link alone does not trigger those stages. Reuse known preferences/location and
allow semantic wording around scoped controls. Forbid repeated absent-link clicks,
invented alternate App controls, Portal request-link controls, role inference,
eligibility inference or automatic transfer on access difficulty.

### Independent criteria, traceability and review

**Behavior:** supported conditional fallback and independent access/submission/finish.
**Coverage:** actual absent App link, separate accepted switch, full Portal target
and finish; an App success, declined fallback or unavailable Portal does not cover it.
**Direct:** DF-010/F01–F02, DG-003 (education concern/general positive context).
**Plausible:** DG-004/005/006/007 through route/access/consent BRs; no extra direct
DF links. **Regression:** VAR-TC-003-E, TC-006 absent-form contrast, TC-009 retry
failure, GM Portal-unavailable negative control. No new VAR allocated.
**Authority/blockers:** Q10 target retained, Q9/Q11–Q13 boundaries; GF unavailable
Portal, authenticated UI, final evidence/wording and formal review remain scoped.
Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-009

### Goal, identity and fixture

**Source:** WB:S!A12:F12; agreed OD-008; R B6/C3; KB SHARED-PORTAL/REQUEST;
JOB30 CONNECTION AFTER FAILED FORM RETRY. **Goal/target:** Portal submission-only,
then consented mock handoff after one accepted authorized retry fails.
**BP:** BP-05; BP-07. **BR:** BR-001/002/003/004/005/006/011/012/014/015;
BR-017/020 assessment. **Inputs:** common older GF fixture; older status inquiry
may receive its applicable education/offer, then merchant explicitly declines
status guidance and requests submission only, as E12. Portal/one-by-one/loudspeaker=yes;
article opened/scrolled, form absent; authorized access established; distinct retry
accepted, one further attempt still has no form; person offer separately accepted
on later input. No actual form submission or successful resolution is asserted.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Reuse GF/older context and actual entry; apply education only when triggered; honor submit-only correction, preferences and opening ownership. | BR-001/002/003/004/005 |
| M02 | Portal Help Centre → Search Bar/search → article → scroll; separate actions/results, then explicit form absence. | BR-006/011/012 |
| M03 | Conditional Owner/Manager explanation; establish unknown access with a separate answer or reuse known authorization. | BR-012 |
| M04 | Separate one-retry offer; wait for explicit acceptance; instruct one supported attempt and await still-absent result. | BR-012 |
| M05 | Supported failed-retry person offer as required by the current POC control; wait for a separate later response. | BR-015 |
| M06 | Explicit acceptance of M05: one Flow-owned mock transfer/terminal, no additional ordinary close. | BR-015 |

**Edges:** M01 → M02/absent → M03/authorized → M04/accepted/failed → M05 → later
explicit acceptance → M06. Initial attempt plus one retry = two attempts total.

### Decisions, variation and forbidden outcomes

Retry decline follows the separate soft-close/finish path; retry success permits
supported details/evidence/self-submission with BR-013 but is not this failed-retry
target. Person refusal means no transfer; unclear actual reply uses supported
re-offer/wait, silence grants no consent. Role unavailable remains a distinct
blocked disposition. Natural navigation wording is allowed; the failed-retry offer
and mock terminal have scoped source controls. Forbid GF Portal status detours,
wrong-role inference, a third attempt, transfer on retry yes, claimed real CXone
connection or an ordinary “issue solved” ending.

### Independent criteria, traceability and review

**Behavior:** correct submit-only route, access/retry discipline and supported
separate consent/terminal ownership. **Coverage:** all M01–M06 conditions and actual
failure/offer/later-acceptance/mock-terminal evidence; declined consent or successful
submission does not cover the intended handoff. **Direct:** DF-011/F01–F05,
DG-002/005/007 with positive intake/role observations retained. **Regression:**
TC-006 and VAR-TC-006-A/B/C/E; TC-010 unrelated reason and VAR-TC-027-C GM access
reason as distinct controls; R C3 no-response/unclear/post-terminal controls.
**Authority/blockers:** OD-008 and Q10/Q11/Q13; original D12/E12 conflict, unsupported
access/silence disposition, OD-011/013/014/015 acceptance. No new VAR allocated.
Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-010

### Goal, identity and fixture

**Source:** WB:S!A13:F13; R C3/C4/C5; JOB30 OUT OF SCOPE and Flow terminal ledger.
**Goal/target:** reach supported mock handoff for a clearly unrelated menu-update
request. **BP:** BP-07. **BR:** BR-001/004/014/015/016; BR-017/020 assessment.
**Inputs:** original GF-labeled merchant; unrelated request such as updating
restaurant menu prices, followed by separate explicit acceptance of the actual
person offer. Age/platform/style/loudspeaker and compensation status are not
prerequisites. This is Q13's **proposed internal fixture**, not a workbook edit;
E13's ambiguous payout example is retained as a negative/scope-clarification control.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Apply normal opening ownership and determine actual scope; clarify only genuine ambiguity and wait. | BR-001/004/016 |
| M02 | Clearly unrelated request: applicable scope statement/person offer; wait. | BR-015/016 |
| M03 | Separate later explicit acceptance of that offer: one matching Flow-owned mock terminal. | BR-015 |

**Edges:** established unrelated intent → M02 → later explicit acceptance → M03.
An initial request for a person or a yes answering scope clarification is not M03 consent.

### Decisions, variation and forbidden outcomes

Confirmed cancellation-related payout stays in scope with its supported explanation
and unresolved financial remedies. An in-scope correction cancels the unrelated
offer; a new supported offer needs its own answer. Refusal means no transfer and
further-help/finish; unclear response requires supported clarification/re-offer.
Merchant phrasing may vary while unrelated scope remains clear; scope/person and
terminal text have separate source controls. Forbid unrelated menu advice, irrelevant
age intake, transfer on ambiguity/acknowledgement/silence, duplicate transfer,
actual-contact-center claims or appending the normal goodbye merely for DF-012.

### Independent criteria, traceability and review

**Behavior:** grounded scope handling and separate offer/consent/terminal evidence.
**Coverage:** genuine unrelated request plus M02 and consented M03; in-scope payout,
person refusal or a generated offer alone does not cover the target. **Direct:**
DF-012/F01–F02, DG-007/009; ordinary-wording complaint stays separate from possible
truncation. **Regression:** TC-009 supported retry reason, VAR-TC-027-C GM access,
R C3/C5 consent and corrected-scope controls, ordinary-close TC-001/025 contrast.
**Authority/blockers:** Q13 criterion agreed internally; menu-update fixture and
formal benchmark attribution still proposed/reviewable; OD-011/013/015 text/voice/
sign-off and unspecified silence disposition remain scoped. No new VAR allocated.
Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-025

### Goal, identity and fixture

**Source:** WB:S!A14:F14; T T01 and §3; KB GM-TIMING/GM-EVIDENCE.
**Goal/target:** understand recent GM compensation and finish without navigation.
**BP:** BP-01. **BR:** BR-001/002/003/004/013/014; BR-018 negative applicability;
BR-017/020 assessment. **Inputs:** common recent GM age-only fixture, no prior
education or clear navigation goal; preparation/packing unknown; explicit finish
after further-help question. Platform, access and status are not needed.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Establish/reuse GM and supported recent cancellation context; opening once. | BR-001/002/004 |
| M02 | Actual recent education: usual 3–5 business-day approval after order made, then regular payout; stage-specific photo-of-the-order reminder. | BR-003/013 |
| M03 | Ask further help and wait; distinguish new question from finish. | BR-014 |
| M04 | Explicit finish: ordinary Flow-owned terminal. | BR-014 |

**Edges:** M01 → M02 → M03 → actual finish → M04. A resolver marker is not education.

### Decisions, variation and forbidden outcomes

Nonreceipt follow-up activates TC-026; actual navigation request follows its own
supported route/exception and Q8 boundaries. Missing photo applies Q7 without
inferring unpacked goods or guaranteed evidence completeness. Timeline and the
recent GM photo-of-the-order reminder are source-controlled candidates; surrounding
wording is semantic. Forbid copied GF prepared-food reminder, unsolicited platform
intake/walkthrough/GM navigation notice, guaranteed bank credit or inferred packing.

### Independent criteria, traceability and review

**Behavior:** correct GM recent education trigger, stage-specific evidence meaning
and finish. **Coverage:** actual M02 education/reminder plus M03 finish and M04;
navigation or routing classification alone does not complete the target.
**Direct findings:** none recorded. **Plausible regression:** DG-001/002/003/007;
DG-008 notice-absence control, DG-009 by channel. Pair TC-001 GF timing/evidence,
TC-026 follow-up and VAR-TC-027-F navigation-only bypass. No new VAR allocated.
**Authority/blockers:** Q1/Q6/Q7/Q8/Q12 and source POC content; original E14's copied
prepared-food text preserved as conflict; OD-005/011/013/015 formal acceptance
remains scoped. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-026

### Goal, identity and fixture

**Source:** WB:S!A15:F15; T T01/T11/T14; JOB30 FOLLOW-UP/GUIDANCE; KB GM-TIMING/
SUBMIT/STATUS. **Goal/target:** recent GM follow-up with guidance expressly declined
and later finish. **BP:** BP-02, BP-01 prerequisite. **BR:** BR-001/002/003/004/005/
008/010/013/014; BR-018 negative applicability, BR-017/020 assessment.
**Inputs:** common recent GM fixture; actual first education; merchant asks about
possible future compensation nonreceipt, with no established approval/overdue
condition; guidance offer declined, further-help question explicitly finished.
No App/Portal accessibility or future successful submission is assumed.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Known GM/recent context and opening once; deliver applicable recent timeline/order-photo reminder and further-help question. | BR-001/002/003/004/013 |
| M02 | Actual nonreceipt follow-up: conditional supported review-option explanation and appropriate guidance offer; wait. | BR-003/008/010/014 |
| M03 | Explicit decline: stop guidance, ask further help and wait. | BR-005/014 |
| M04 | Actual finish: ordinary Flow-owned terminal. | BR-014 |

**Edges:** M01 → actual follow-up → M02 → decline → M03 → finish → M04.
No acceptance of navigation, platform transition or transfer is inferred from follow-up.

### Decisions, variation and forbidden outcomes

An accepted offer requires its actual scope: GM status uses computer Portal; GM
submission-only can use its supported chosen platform. Genuine ambiguity may be
clarified, but clear status-only intent retains the no-age/no-loudspeaker exception.
A later timing question after refusal is answered without automatic re-offer.
Use common semantic rule plus applicable GM timeline/recent reminder/terminal
controls. Forbid a GM App status promise, treating every App submission reference
as wrong, automatic navigation notice, continuation after decline or unsupported
payout remedy. Silence grants neither decline nor finish.

### Independent criteria, traceability and review

**Behavior:** grounded follow-up, scoped offer, honored decline and real finish.
**Coverage:** recent education, actual follow-up and distinct decline/finish/terminal;
accepted navigation or a TC-025 education-only path is incomplete target coverage.
**Direct:** DF-013/F01, DG-009; silence report does not establish ASR cause or SLA
violation. **Plausible regression:** DG-003/007 and DG-008 negative notice control;
TC-002 GF, TC-025 no follow-up, Q8 N07 accepted-offer scope, VAR-TC-027-F/G route
contrast. No new VAR allocated. **Authority/blockers:** qualified Q1/Q5–Q8/Q10/Q12,
POC source content; original copied evidence wording, unsupported financial/UI
outcomes and OD-005/011/013/014/015 remain scoped. Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-028

### Goal, identity and fixture

**Source:** WB:S!A17:F17; T T02/T06; R C2/C6; JOB30 OLDER CANCELLED ORDER/CLOSING.
**Goal/target:** general older GM compensation explanation, no walkthrough, explicit
finish. **BP:** BP-03. **BR:** BR-001/002/003/004/014; BR-013/018 applicability
controls; BR-017/020 assessment. **Inputs:** common older GM age-only entry; general
compensation/status inquiry after the open question—not clear where/how navigation,
dual intent or a substituted timing-only query. Choose/record one permitted local
ending: optional offer explicitly declined, or no offer with acknowledgement;
both then require a further-help question and explicit finish. No new VAR ID or
universal offer duty is created. Platform access need not be available for education.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Establish/reuse older GM context; opening once; ask unknown goal and wait. | BR-001/002/004 |
| M02 | General inquiry: qualified GM approval/payout education before any preferences. | BR-003 |
| M03 | If optional guidance offer is made, wait for explicit decline; otherwise record the merchant acknowledgement after education. | BR-014 |
| M04 | Ask further help and wait for actual explicit finish. | BR-014 |
| M05 | Finish established: ordinary Flow-owned terminal. | BR-014 |

**Edges:** M01/general inquiry → M02 → M03/decline-or-acknowledgement → M04/finish
→ M05. Acknowledgement is not itself a finish signal.

### Decisions, variation and forbidden outcomes

Timing-only and elicited dual goals retain their required offers under T04/T07;
clear GM status-only navigation retains the protected exception. An accepted
walkthrough exercises a separate branch. Common semantic flexibility applies
around the GM timeline/terminal source controls; no mandatory older-GM evidence
reminder follows from E17's copied prepared-food wording. Forbid platform intake
before answering this informational goal, inability-to-educate claims based on
access, unwarranted GM navigation notice, automatic transfer or close on “okay.”

### Independent criteria, traceability and review

**Behavior:** correct general-inquiry trigger, actual applicable offer response and
explicit finish. **Coverage:** either permitted M03 ending plus M01/M02/M04/M05
covers the no-walkthrough target; only offered-and-declined M03 covers guidance
decline. Neither bare acknowledgement nor accepted navigation supplies target finish.
**Direct:** DF-015/F01–F04; DG-002/003/007, positive inquiry and later N19 fix note
preserved without inventing a retest pass. **Regression:** TC-004 required GF offer,
TC-029 required GM dual offer, TC-025 recent evidence, R C2/C6; DG-008 only plausible
notice applicability. **Authority/blockers:** Q12 **YES, PROVISIONALLY**; benchmark
fixture changes require reviewer approval; OD-005/011/013/015 remain scoped.
Verdicts: `NOT_RUN / NOT_RUN`.

## JRN-TC-029

### Goal, identity and fixture

**Source:** WB:S!A18:F18; T T02/T07; R A6; KB GM-STATUS/GM-EVIDENCE/SHARED-PORTAL;
JOB30 GM guidance and grouped segments. **Goal/target:** elicited older GM dual
goal, grouped computer-Portal status and conditional Portal submission.
**BP:** BP-04; BP-05. **BR:** BR-001/002/003/004/005/006/008/009/011/012/013/014/
018/019 by applicability; BR-017/020 assessment. **Inputs:** common older GM fixture;
dual goal supplied after open question, education/required guidance offer accepted;
App selected, all-at-once, loudspeaker=no; computer Portal accessible/ready;
visible order with status absent, retained request; authorized access, article/
scroll/form visible, merchant submission and finish reports. Evidence availability
is declared; no individual eligibility or payment outcome is implied.

### Conditional milestones and observation dependencies

| ID | Condition / action and required observation or pause | BR |
|---|---|---|
| M01 | Context/opening; older age-only goal question and wait. | BR-001/002/004 |
| M02 | Elicited dual intent: qualified GM timeline and required guidance offer; wait for acceptance. | BR-003/014 |
| M03 | Preferences once; applicable GM notice once; explicit App→computer-Portal redirect and observed readiness before controls. | BR-005/008/018 |
| M04 | Group Finance, Transactions, period/store and Category selection only within supported status segment; obtain actual order visibility/status. | BR-006/008 |
| M05 | Decide using observed status and retained request; no automatic eligibility/rejection conclusion. | BR-009 |
| M06 | Group supported Portal entry/search/article/scroll to form observation; stop for access recovery if absent. | BR-006/011/012 |
| M07 | Visible form/authorized access: grouped details, packed-items evidence and self-submission; wait for merchant report. | BR-012/013 |
| M08 | Conditional acknowledgement/further help; explicit finish and ordinary terminal. | BR-014 |

**Edges:** M01 → M02/accept → M03/ready → M04/status → M05 → M06/form → M07/report
→ M08. Status and submission segments cannot be combined across the status answer.

### Decisions, variation and forbidden outcomes

Missing order uses supported period correction and a new observation, not GF
History; still-missing recovery remains blocked beyond known steps. Unavailable
computer Portal uses the supported GM offer with separate later consent, not
successful close. Already-approved/unclear GM outcomes retain formal semantics
limits; missing form uses separate role/one-retry conditions. Common semantic
variation applies around source GM timeline/notice/redirect/terminal controls.
Forbid bank-credit-in-3–5-days promises, full-award guarantees, repeated notice,
GM App status, skipped readiness/form observations or forced duplicate submission.

### Independent criteria, traceability and review

**Behavior:** correct elicited-dual education/offer, once-only notice/transition,
observed grouped segments, retained request and supported completion. **Coverage:**
all target entry/readiness/status/form/submission/finish conditions; access handoff,
Portal-first or missing-order-only recovery does not complete this selected fixture.
**Direct:** DF-016/F01, DG-004/006 positive control; “most steps” is not full PASS.
**Plausible regression:** DG-002/003/005/007/008; TC-027 one-by-one/upfront entry and
VAR-TC-027-A–G, TC-005 GF grouped, R A6/C7 and Q8 corrections. Memberships are not
expanded by this plausible list. **Authority/blockers:** supported POC route and
qualified Q1–Q13 applicability; GM notice certainty OD-006, exactness OD-011, status/
evidence/UI outcomes OD-014, timing/voice/review OD-005/013/015 remain scoped.
No new VAR allocated. Verdicts: `NOT_RUN / NOT_RUN`.
