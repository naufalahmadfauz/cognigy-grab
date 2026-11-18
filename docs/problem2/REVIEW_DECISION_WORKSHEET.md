# UC4 Problem #2 — business/benchmark worksheet and internal agreement log

**Current acceptance:** [Scoped internal POC acceptance recorded](#recorded-scoped-internal-poc-acceptance),
declaration dated 2026-11-04; recorded here 2026-11-05. The pending decision form
below is preserved as the pre-acceptance record. [Execution readiness](EXECUTION_READINESS.md):
**NO-GO**; execution not authorized, baseline **NOT FROZEN**, both verdicts **NOT_RUN**.

**Current sign-off sheet:** [Final internal POC acceptance sign-off sheet](#final-internal-poc-acceptance-sign-off-sheet).
Project owner confirmed in both internal POC engineering acceptance and QA roles
(temporary self-review); 23-fixture baseline proposed, 21-fixture smoke/regression
subset retained; consolidated acceptance decision pending.

**Phase 5:** [Acceptance review summary](#phase-5-acceptance-review-summary),
2026-11-04 — recommendations and prioritized regression selection; sign-off pending.

**Phase 4 review packet:** `P2-BASELINE-CANDIDATE-0.1` / `P2-JOURNEYS-0.4` /
`P2-CONTROLLED-TEXT-0.1`, **NOT FROZEN**. All 15 full specifications are prepared;
the [candidate checklist](#phase-4-candidate-review-checklist) records outstanding
review without reopening existing internal approvals. Both verdicts remain `NOT_RUN`.

**Package:** P2-DRAFT-0.2 + P2-ENG-DECISIONS-0.3 / OD002-REVIEW-0.2 / OD004-OD005-REVIEW-0.2 / OD004-RECENT-GUIDANCE-REVIEW-0.2 / OD007-OD010-OD009-REVIEW-0.2 internal agreements

**Status:** Four Round 1 internal agreements plus **OD-002 Q1–Q4** (2026-11-02), **qualified OD-004/005 Q1–Q7**, **qualified Q8 Option B design direction** (2026-11-03) and **qualified Q9–Q13 criteria** (2026-11-04) agreed internally; **no formal benchmark or Grab policy approvals recorded**. See [Round 1 record](ENGINEERING_DECISIONS_2026-11-02.md) and [OD-002 approval provenance](OD002_STATUS_DECISION_REVIEW.md#recorded-q1q4-approval-and-provenance).

**Input authority:** October 23 Problem #2 PLAN/PB; Grab benchmark workbook (immutable); KB v0.3 POC source decisions; existing `OPEN_DECISIONS.md`.  
**Use:** Record selections from named benchmark/business and QA reviewers. An LLM recommendation cannot approve or change a business rule.

**Current agreement, 2026-11-04:** `OD007-OD010-OD009-REVIEW-0.2`; Q9–Q13 are
**answered with qualifications**, Q12 explicitly provisional. Earlier agreements
and formal authority limits persist.

## Historical options for formal benchmark review

The next table retains the pre-agreement source options and formal acceptance
blockers. The internal choices are already recorded in the following agreement
log; they are not reopened by unfilled formal fields. OD-002 Q1–Q4 have explicit
answers in [the Round 2 record](OD002_STATUS_DECISION_REVIEW.md#7-review-frontier-and-adoption-limits).
Formal business/benchmark and QA sign-off remains pending for both rounds.

**Round 3, OD-004/005:** the [qualified approval record](OD004_OD005_TRIGGER_TIMING_REVIEW.md#recorded-q1q7-approval-and-provenance)
contains the user's actual answers, full qualifications and superseded proposals.
All seven internal choices are recorded below; formal policy-owner and QA sign-off
remain separate. Q4 is conditional on genuine ambiguity, not a universal question.

| OD | Issue and source evidence | Candidate option A (historical proposal; formal approval pending) | Alternative / why it matters | Historical / formal state |
|---|---|---|---|---|
| OD-001 | TC-006 `WB:S!D9` expects retry declined, while `E9` accepts re-login and successful form submission | Keep D9 declined retry/soft close as **proposed** original fixture; keep accepted/success as `VAR-TC-006-A`; failed retry separately | Stakeholder could choose E9 as original target. Either way preserve both and specify fixture; don't fabricate consensus. | CONFLICT; original TC coverage BLOCKED_SPEC |
| OD-008 | TC-009 `WB:S!D12` says Portal *status*, `E12` explicitly declines status and requests submission only | Use E12 Portal submission + failed retry + separate consented mock transfer as **proposed** original fixture | If D12 is required, confirm supported GF Portal status route before requiring it; current KB supports GF App status. | CONFLICT; original TC coverage BLOCKED_SPEC |
| OD-003 | TC-027 `WB:S!E16` selects App, then shifts into Portal Finance/Transactions; `F16` says Portal-only for GM status | Keep App selection; explicitly explain computer Portal status route, confirm Portal readiness and preserve style | Portal unavailable needs separate supported recovery/consent; don't silently treat App as Portal. | CONFLICT; target fixture review pending |
| OD-015 | Reviewer ownership/acceptance scope/sample count not assigned | Assign business/benchmark owner and QA reviewer; sign off only on chosen fixture/BR applicability with version and date | Without reviewer authority, mark draft and don't convert proposed instructions into Grab policy. | PROPOSED; no approvals |

## Project-side engineering agreement log (recorded 2026-11-02)

| OD | Selected internal POC direction | Scope | Formal reviewer sign-off |
|---|---|---|---|
| OD-001 | Declined retry = provisional original TC-006; success = VAR-TC-006-A; failed retry separate | Engineering fixture agreed; original workbook contradiction retained | Pending |
| OD-008 | Portal **submission-only**; failed retry → person offer → separate explicit consent → mock transfer | Engineering fixture agreed; original workbook contradiction retained | Pending |
| OD-003 | App selection → explain computer Portal requirement → verify readiness → Portal status guidance; preserve preferences | Engineering transition agreed; benchmark conflict retained | Pending |
| OD-015 | Appoint business/benchmark and QA reviewers; review and freeze scoped accepted requirements before baseline execution | Review governance agreed; appointments and sign-off not performed | Pending |
| OD-002 | Q1 Approved: visible-blank review-request target with intent/prerequisites, no eligibility/award claim. Q2 Approved provisionally: reported approval/status-only explanation without unnecessary duplicate. Q3 Approved provisionally: approval/payout/bank-receipt explanation and clarification priority, no invented remedy/date/guarantee. Q4 Approved: clarify observed status before status-dependent submission. | **VERIFIED [POC] / ENGINEERING_AGREED_POC**, OD002-REVIEW-0.2; all four provisional internal POC decisions. Behavior and original TC-003 coverage remain independent; dependent requirements, formal semantics and remedies remain open | Pending |

**Recorded authority:** the requesting project-side user's explicit conversation
agreement, 2026-11-02. Personal name, official role and formal business/benchmark
or QA authority were not supplied. OD-002's source quotation, rationale, affected
versions and superseded wording are in its linked record. These entries do not
create formal Grab policy approval or authorize runtime changes.

## Qualified Round 3 agreement log (recorded 2026-11-03)

All entries below are **VERIFIED [POC] / ENGINEERING_AGREED_POC**, provisional
internal engineering scope only. Source: requesting project-side user's explicit
qualified approval message; personal name/official role/formal Grab or QA authority
not supplied. The linked full approval text governs any abbreviated row.

| Choice / OD | Recorded answer and scope | Remaining conflict / formal sign-off |
|---|---|---|
| Q1 / OD-004 | Approved: defined recent age-only education without unnecessary goal question; no inferred preparation/packing. | Job-source conflict retained; formal sign-off pending. |
| Q2 / OD-004 | Approved conditionally: requested/accepted navigation priority, including same-order age correction; preserve mandatory disclosures and necessary intake. | Implementation conflict retained; qualified Q8 below now settles design direction. Exact implementation/fixtures remain open; no runtime authorization or official early-form support. |
| Q3 / OD-004 | Approved: TC-027 clear upfront dual request omits unsolicited timing/redundant accepted-guidance offer; preserve GM notice, computer-Portal transition, preferences and status observation before submission. | Original benchmark conflict and final GM policy retained; formal sign-off pending. |
| Q4 / OD-004 | Approved as modified, conditional: clarify once only for genuine ambiguity; no redundant clear-status clarification or unnecessary age/loudspeaker intake under the direct GM-only exception. | No universal phrase-triggered clarification; formal acceptance pending. |
| Q5 / OD-004 | Approved: answer new timing question after decline without automatic repeat offer; new explicit guidance request may change branch. | Applicable entry/Tool and finish/consent boundaries remain. |
| Q6 / OD-005 | Approved: explicit cancellation-age fixtures, declared Asia/Kuala_Lumpur (UTC+8) reference, reproducible same-session dates and documented relative expressions; approval after order made stays distinct. | Absolute dates, midnight boundaries and official business-calendar conventions unresolved. |
| Q7 / OD-005 | Approved conditionally: KB-supported no-photo continuation with available evidence/information; retain recommendations, no eligibility/acceptance/completeness/approval promise; flag separately established mandatory UI/business conditions for review. | Exact text, UI acceptance/conditions, final evidence policy and substitutes unresolved. |

No execution or regrade result accompanies these agreements. Formal fields below
remain unfilled; their pending status does not reopen internal Q1–Q7.

## Qualified Q8 design agreement log (recorded 2026-11-03)

Source: [OD004-RECENT-GUIDANCE-REVIEW-0.2 — full approval/provenance](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#recorded-q8-approval-and-provenance).
The requesting project-side user explicitly agreed to Option B with seven
qualifications. Personal name, official role and formal Grab business/benchmark
or QA authority were not supplied. The full quoted approval governs this summary.

| Choice | Selected design direction and qualifications | Recorded answer / authority |
|---|---|---|
| [Q8 — Option B](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#recorded-q8-approval-and-provenance), OD-004 Q2 dependency | (1) Coordinate existing admission/checkpoint validation/age correction; (2) retain compatible intent, consent, preferences, location and actions, invalidate only changed-fact-dependent progress; (3) actual education/disclosure delivery differs from resolver selection; (4) Agent-first, smallest instruction/contract changes, no new controller protocol, unnecessary persistent walkthrough state or additional Flow infrastructure; (5) retain Q1–Q7 and GM direct status-only exception; (6) no early eligibility, compensation guarantee, unsupported submission or policy/UI override; (7) protect TC-001/025, TC-002/026, navigation variants and same-order corrections. | **Approved with seven qualifications — VERIFIED [POC] / ENGINEERING_AGREED_POC**, requesting project-side user, 2026-11-03. **Documentation/design direction only**; formal sign-off pending. |

Q8 is answered; the original question, alternative options and v0.1 audit are
preserved in the [twelve-member pre-approval snapshot](../../reference/UC4_Problem2_OD004_Recent_Guidance_Review_v0.1_2026-11-03.zip).
Qualification 4 constrains prior representation/API suggestions; no exact mechanism
or new fixture acceptance is selected. No Cognigy/Job/Tool/Code/KB/runner change,
live test or baseline freeze is authorized. Formal sign-off below remains separate.

## Qualified Q9–Q13 agreement log (recorded 2026-11-04)

Source: [full qualified approval and provenance](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#recorded-q9q13-approval-and-provenance).
All five answers are **VERIFIED [POC] / ENGINEERING_AGREED_POC** for provisional
internal POC specification/test-fixture design only. **Decision-maker:** requesting
project-side user, **2026-11-04**; personal name, official role and formal Grab
business/benchmark or QA authority were not supplied. The full quotation governs.
All behavior/coverage verdicts remain `NOT_RUN`.

| Question / OD | Recorded criterion and scope | Actual answer / authority / date |
|---|---|---|
| Q9 / OD-007 | History only for the relevant order missing from Cancelled; TC-007 Date-selector first failure → one supported repeat → observed success. Preserve one-by-one action/wait boundaries; actual failure is distinct from Q8 correction-invalidated progress. No unsupported recovery steps. | **YES, qualified**; requesting project-side user; 2026-11-04 |
| Q10 / OD-010 | Separate App request-link availability, article opening, scroll, form visibility, authorization, retry consent, retry outcome and merchant-reported submission. Preserve TC-006 decline, VAR-TC-006-A success, TC-008 fallback and TC-009 submit-only. Missing form never proves wrong role. | **YES, qualified**; requesting project-side user; 2026-11-04 |
| Q11 / OD-010 | Owner/Manager submission authorization remains required; explain conditionally during access recovery and actual role questions. No universal successful-path spoken reminder unless separately approved. | **YES, qualified**; requesting project-side user; 2026-11-04 |
| Q12 / OD-009 | TC-004 explicit guidance decline and finish; TC-028 reviewed optional-offer/no-offer endings with explicit finish. Required offers retain their triggers; acknowledgement, silence or submission does not establish resolution. **Benchmark fixture changes require reviewer approval.** | **YES, PROVISIONALLY**, qualified; requesting project-side user; 2026-11-04 |
| Q13 / OD-009 | Supported trigger → separate person offer → later explicit acceptance → one Flow-owned mock transfer. Retry consent/acknowledgement/silence cannot transfer. TC-010 menu-update request is the proposed internal out-of-scope fixture; ordinary closing and transfer terminals stay separate. | **YES, qualified**; requesting project-side user; 2026-11-04 |

The old unanswered frontier is preserved in the [pre-approval snapshot](../../reference/UC4_Problem2_OD007_OD010_OD009_Review_v0.1_2026-11-04.zip)
and the report's historical questions. Q1–Q8 remain controlling. Approval covers
the stated criteria, not every detailed profile, whole variant or unknown remedy.
Owner evidence for [unsupported outcomes](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#outcomes-still-needing-an-authorized-disposition)
and formal benchmark/business/QA acceptance remain pending. Q11's conditional
criterion no longer awaits an internal universal-reminder decision. The A/B/C
aliases allocate no new VARs; the [12-specification phase](OPEN_DECISIONS.md#proposed-next-phase--12-specifications-and-scoped-baseline-review)
was proposed by that approval-recording update and is now completed as a review
candidate under Phase 4; no additional policy approval follows.

## Formal human review record — leave unfilled until named authorized reviewer signs off

| OD | Selected option / alternative | Business or benchmark reviewer | QA reviewer | Date | Approval scope and rationale | Impacted BR/JRN/VAR version | Decision state |
|---|---|---|---|---|---|---|---|
| OD-001 | _pending_ | _unassigned_ | _unassigned_ | — | _not decided_ | BR-012/014/015; JRN-TC-006; VAR-TC-006-A/B | CONFLICT |
| OD-008 | _pending_ | _unassigned_ | _unassigned_ | — | _not decided_ | BR-009/011/012/015; JRN-TC-009 | CONFLICT |
| OD-003 | _pending_ | _unassigned_ | _unassigned_ | — | _not decided_ | BR-005/008; JRN-TC-027; TC-029 comparison | CONFLICT |
| OD-015 | _pending_ | _unassigned_ | _unassigned_ | — | _not decided_ | Review framework and high-risk sampling | PROPOSED |
| OD-002 | _pending formal confirmation_ | _unassigned_ | _unassigned_ | — | _formal scope pending; internal Q1–Q4 recorded above_ | OD002-REVIEW-0.2: BR-009; JRN-TC-003; VAR-TC-003-A/B/C | UNKNOWN formal policy; sign-off pending |
| OD-004 | _pending formal confirmation_ | _unassigned_ | _unassigned_ | — | _qualified internal Q1–Q5 and Q8 recorded; exact implementation/fixtures and formal source acceptance open_ | OD004-OD005-REVIEW-0.2 and OD004-RECENT-GUIDANCE-REVIEW-0.2: BR-001/002/003/005/009/014 and conditional §6 impacts; JRN-TC-027 entry | Internal design agreement; formal/implementation CONFLICT retained |
| OD-005 | _pending formal confirmation_ | _unassigned_ | _unassigned_ | — | _qualified internal Q6–Q7 recorded; official timing/UI/evidence conditions unresolved_ | OD004-OD005-REVIEW-0.2: BR-002/003/013; shared fixture/evidence scope | Internal agreement; formal policy/UI/timing UNKNOWN/CONFLICT |
| OD-007 | _pending formal confirmation_ | _unassigned_ | _unassigned_ | — | _qualified internal Q9 recorded; formal fixture attribution and further remedies pending_ | OD007-OD010-OD009-REVIEW-0.2: BR-006/007/019; TC-007 and conditional recovery | Internal agreement; formal CONFLICT / unsupported outcomes UNKNOWN |
| OD-010 | _pending formal confirmation_ | _unassigned_ | _unassigned_ | — | _qualified internal Q10–Q11 recorded; conditional reminder criterion settled internally_ | OD007-OD010-OD009-REVIEW-0.2: BR-010/011/012/013/014 and applicable variants | Internal agreement; formal policy/UI and unsupported remedies pending |
| OD-009 | _pending formal confirmation_ | _unassigned_ | _unassigned_ | — | _Q12 provisional fixture repairs and qualified Q13 recorded; benchmark fixture approval required_ | OD007-OD010-OD009-REVIEW-0.2: BR-014/015/016/020; TC-004/028/010 and supported handoff paths | Internal agreement; formal fixture/wording/evidence acceptance pending |

## Reviewer checklist

- [ ] Confirm the two separate questions for each fixture: Agent behavior on observed branch and coverage of intended original TC.
- [ ] Confirm the proposed target and any distinct test variant, without overwriting Grab's workbook.
- [ ] Check BR source authority and its **POC adoption** vs **formal business approval** boundary.
- [ ] Identify which requirements are business obligations versus QA/evidence rules.
- [x] Record qualified OD-004/005 Q1–Q7 as provisional internal decisions with authority limits and preserved source conflicts.
- [x] Record [qualified Q8 Option B approval](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#recorded-q8-approval-and-provenance), all seven qualifications, Agent-first boundary and documentation/design-only authority.
- [x] Record [qualified Q9–Q13](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#recorded-q9q13-approval-and-provenance), including Q12's provisional fixture-review limit, TC-010's proposed fixture and actual authority/date; preserve Q1–Q8.
- [x] Draft the 12 remaining specifications, reconcile the three pilots and prepare the versioned scoped baseline review candidate with explicit blockers and exclusions.
- [ ] Obtain formal OD-002/014 status, duplicate/dispute, unpaid-remedy and access evidence; retain answered internal choices. Follow this review with scoped OD-006/011 wording review.
- [ ] Record an owner, date, rationale, changed versions, evidence and dissent/unresolved status.
- [ ] After applicable decisions and named sign-off, consider a scoped baseline version and separate execution authorization. Full Business Acceptance Baseline v1.0 remains **NOT FROZEN** under this update.

**Current next action:** submit the completed journey catalog and scoped candidate
for named review. Seek additional contract evidence only for a genuine acceptance blocker.
Later execution/evidence assessment requires separate authorization. Retain
independent historical/new verdicts; KB coverage is not 15 benchmark passes.

## Phase 4 candidate review checklist

**Review object:** [P2-BASELINE-CANDIDATE-0.1](BASELINE_MODEL.md#phase-4-scoped-acceptance-baseline-review-candidate),
complete [P2-JOURNEYS-0.4 catalog](JOURNEY_PILOT.md#catalog-index-and-version-scope)
and [P2-CONTROLLED-TEXT-0.1](BASELINE_MODEL.md#controlled-language-applicability-register).
Preparation was confirmed by the requesting project-side user on 2026-11-04;
this is scope confirmation, not a new numbered engineering or formal-policy approval.

### Preparation and quality checklist

- [x] All 15 original TCs have full source-traceable JRN records covering the eleven requested content areas, with a shared contract explicitly included.
- [x] Twelve new records supplement the reconciled TC-003/006/027 pilots; existing milestone/VAR identities and prior approval scopes are retained.
- [x] TC-006 decline, TC-009 submit-only, TC-027 transition/upfront dual, TC-003 separate status/coverage alternatives and direct GM status-only exception are explicit.
- [x] Q9 recovery, Q10 observation boundaries, Q11 conditional role speech, Q12 provisional explicit endings and Q13 separate supported transfer consent are carried forward.
- [x] Candidate manifests include 20 BRs and 18 existing VARs; Q8 and R profiles remain source-qualified local aliases.
- [x] Controlled source text, semantic instructions, triggers/channel/owners and pending literal/formal approval are distinguished.
- [x] Original 18 DF/49 atomic/nine-DG history and direct-versus-plausible associations remain preserved; conditional regression and negative controls are documented.
- [x] Unknown outcomes, formal policy/UI/wording gaps, unverified current configuration and later evidence requirements remain visible; both current verdicts are NOT_RUN.

Static verification evidence and preservation counts are recorded in the
[Phase 4 change report](README.md#phase-4-static-verification-and-change-report).
Preparation checks are not reviewer acceptance or execution results.

### Consolidated outstanding reviewer decisions

In each row, record **accept / amend / exclude / defer**, exact criterion and
JRN/BR/VAR/CT version, rationale/source, dissent or remaining blocker, reviewer
identity/authority and date. Do not use a whole-journey acceptance checkbox to
silently settle a blocked outcome. All owner fields below remain **unassigned**.

| Review scope / affected criteria | Decision or evidence required | Responsible review role | Named reviewer / authority / date | Disposition |
|---|---|---|---|---|
| Candidate scope and 15 JRN fixtures | Accept/amend/exclude precise versions/conditions; retain 18 VAR meanings and two independent verdicts. | Business/benchmark + QA | _unassigned / not supplied / —_ | Pending |
| Formal fixture attribution; TC-006/009/027, TC-007, TC-004/028 and proposed TC-010 | Confirm formal benchmark interpretation/refinement; Q12 changes remain provisional. Original workbook preserved. | Benchmark owner + QA | _unassigned / not supplied / —_ | Pending; internal choices stand |
| BR-002/003/013; OD-005 | Official clock/calendar, absolute/midnight cases and timing/evidence wording outside Q6/Q7's agreed scope. | Policy/timing owner + QA | _unassigned / not supplied / —_ | Block dependent criteria |
| BR-009; OD-002/014 | Canonical GF/GM status, duplicate/dispute policy and approved-but-unpaid remedy/trigger. | Business/policy owner | _unassigned / not supplied / —_ | Block unsupported meanings/remedies |
| BR-010/011/012/013; OD-014 | Authenticated supported screens, early acceptance, mandatory evidence/substitutes/authorization conditions. | Policy/UI owner + QA | _unassigned / not supplied / —_ | Block unsupported UI/policy assurance |
| BR-006/007/008/019 and access/finish boundaries | Supported next outcomes after repeated failure, still-missing order, unusable recovery, unavailable GF Portal/role, post-visible submission error and unspecified silence disposition. | Applicable policy/UI/POC contract owner + QA | _unassigned / not supplied / —_ | Unknown outcome; prefix retained |
| BR-018/020; CT06; OD-006 | GM partial-compensation certainty and applicable policy wording. | Business/content owner + QA | _unassigned / not supplied / —_ | Source conflict retained |
| CT01–CT14; OD-011 | Accept exact versus semantic mode, version, trigger, exceptions, owner and channel; no blanket literal workbook. | Content/business owner + QA | _unassigned / not supplied / —_ | Literal register adoption pending |
| BR-017, terminal output; OD-013 | Audibility/response expectations and synchronized capture requirements; no unsupported SLA or causal inference. | Voice/environment owner + QA | _unassigned / not supplied / —_ | Evidence scope pending |
| Regression selection/channel/sampling; OD-015 | Approve applicable target/variant/negative controls and count; PB five-run proposal remains unadopted. | QA + business/benchmark | _unassigned / not supplied / —_ | Pending |
| Current served configuration/Q8 conformance; new closure assurance OD-012 | Future authorized configuration/binding evidence, known implementation reconciliation and traceable current regression where new assurance is requested. | POC/configuration/defect owner + QA | _unassigned / not supplied / —_ | Later work; no current assurance |

### Sign-off record — unfilled

| Candidate | Accepted criterion/version scope and exclusions | Business/benchmark reviewer and authority | QA reviewer | Date | Evidence/channel/sampling scope | Freeze authorization |
|---|---|---|---|---|---|---|
| P2-BASELINE-CANDIDATE-0.1 | _pending_ | _unassigned_ | _unassigned_ | — | _pending_ | **None — NOT FROZEN** |

Recording future acceptance does not silently authorize implementation or tests.
Where owner evidence remains unavailable, reviewers may preserve a blocked outcome
or explicitly exclude its judgment with rationale while assessing supported criteria.

## Phase 5 acceptance review summary

**Review object:** unchanged `P2-JOURNEYS-0.4`, `P2-BASELINE-CANDIDATE-0.1` and
`P2-CONTROLLED-TEXT-0.1`. **Recommendation only; no criterion accepted or frozen
by this summary.** Q1–Q13 and earlier internal agreements retain their exact scope.
The user's Phase 5 scope confirmation authorizes this documentation preparation.
All named reviewers/authority/date fields above remain **unassigned / pending**.
Current verdicts: **behavior NOT_RUN; coverage NOT_RUN**; baseline **NOT FROZEN**.

**Readiness labels apply to the stated subcriterion, not its entire BR/JRN:**
**Ready** = source-supported and ready for an authorized internal POC acceptance
decision; **Conditional** = accept only an explicitly bounded fixture/interpretation
with recorded conditions; **Blocked** = the named missing evidence prevents that
dependent decision; **Excluded** = outside this candidate's assessment scope.
Neither readiness nor later satisfaction of a condition supplies automatic approval.
Acceptance of conversational criteria does not certify implementation conformance.

**Sources:** [candidate manifest and exclusions](BASELINE_MODEL.md#included-requirement-manifest)
govern all applicability. **ENG** = [earlier internal agreements](ENGINEERING_DECISIONS_2026-11-02.md);
**S** = [OD-002 status decisions](OD002_STATUS_DECISION_REVIEW.md#recorded-q1q4-approval-and-provenance);
**T** = [qualified Q1–Q7 / T01–T18](OD004_OD005_TRIGGER_TIMING_REVIEW.md#2-intent-entry-age-and-lob-trigger-table);
**G** = [Q8 design agreement](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#recorded-q8-approval-and-provenance);
**R** = [qualified Q9–Q13](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#recorded-q9q13-approval-and-provenance).
JOB30, KB30 and PB retain the candidate's source identities/hashes. **POC + QA**
below means an explicitly authorized internal business/benchmark reviewer plus QA,
not an inferred appointment or formal Grab policy authority. Additional owner roles
apply only to their named dependent decisions.

### Criterion-level acceptance recommendations

All references inherit the candidate's preconditions and versions. Shared rules
apply to VARs conditionally. Authenticated CT wording is **Conditional** for internal
literal adoption under OD-011: an explicit content/QA decision is still needed,
not another quotation investigation. CT06's policy certainty remains **Blocked**
under OD-006; CT13 is UI-identity mode, CT14 semantic mode. Voice claims need BR-017
evidence. No literal grading is authorized before its applicable adoption decision.

| Criterion | Recommendation / precise boundary | Affected TC / VAR | Reviewer and remaining decision | Source |
|---|---|---|---|---|
| BR-001 | **Ready:** reuse known order/LOB/intent; clarify genuine ambiguity only. | All 15; applicable correction/scope variants. | POC + QA: accept conditional context rule, not guessed facts. | JOB30; T Q1/Q4; G |
| BR-002 | **Ready:** declared cancellation ages and same-date UTC+8 fixture. **Blocked:** official calendar, absolute dates or midnight interpretation. | Age-dependent TCs except TC-010; VAR-TC-027-F bypass. | POC + QA: accept fixture convention; timing owner: supply authority for broader date judgments (OD-005). | T §3/Q6 |
| BR-003 | **Ready:** entry-specific education/offer/suppression and actual output evidence; approval differs from payout. **Conditional:** fixed-text adoption. **Blocked:** official-date claims. | TC-001–009/025–029 by trigger; TC-003/027 suppression; VAR-TC-027-F exception. | POC + QA: accept T01–T18; content/timing owners: OD-011/005 scope. | T Q1–Q5; G; JOB30 |
| BR-004 | **Ready:** once-only normal opening/ownership. **Conditional:** entry/channel fixture and CT01 adoption. **Blocked:** audible certification without capture. | All 15 normal-entry targets. | POC + QA: select native-empty/utterance-first controls; content/voice owners: OD-011/013 scope. | JOB30; CT01 |
| BR-005 | **Ready:** necessary preferences once; retain compatible intent/progress; preserve narrow GM bypass. | TC-003/005–009/027/029; VAR-TC-027-F/G; G correction profiles. | POC + QA: accept conditional reuse and exception; current Q8 conformance remains an execution dependency. | ENG OD-003; T Q3/Q4; G |
| BR-006 | **Ready:** one action/wait or grouped decision segments; distinct observations and consent. | Navigation targets; TC-005/029 grouped controls. | POC + QA: accept observation boundaries and per-fixture pacing. | JOB30 segmentation; R Q9/Q10 |
| BR-007 | **Ready:** GF App status; History only for missing order. **Conditional:** TC-007's selected failure fixture. **Blocked:** further unsupported recovery. | TC-003/005–008; VAR-TC-003-D. | POC + QA: sign exact internal fixture; benchmark owner: formal attribution; UI/contract owner: missing next remedy. | R Q9; KB30 GF-STATUS |
| BR-008 | **Ready:** GM computer-Portal status/readiness; status-only bypass and App submit-only distinction. **Conditional:** transition/recovery fixture attribution. **Blocked:** authenticated UI and still-missing remedy. | TC-027/029; VAR-TC-027-A/C/D/F/G. | POC + QA: accept bounded route; benchmark/UI owners: attribution/screens/remedy (OD-003/014). | ENG; T Q3; G; JOB30 |
| BR-009 | **Ready:** actual status plus remaining goal, clarify before continuation. **Conditional:** S's provisional approval/status-only and unpaid explanations. **Blocked:** canonical/GM alternative meanings, duplicate exceptions and financial remedy. | TC-003/005–008/027/029; VAR-TC-003-A/B/C; VAR-TC-027-B; TC-009 submit-only control. | POC + QA: accept bounded S branches; policy owner: OD-002/014 meanings/remedy. | S Q1–Q4; PB; KB30 |
| BR-010 | **Ready:** distinguish link/article/scroll/form; separately accepted Portal fallback; no eligibility/role inference. **Blocked:** real screens/early form acceptance. | GF request targets; TC-008; VAR-TC-003-E/F; VAR-TC-027-G. | POC + QA: accept merchant-observation criteria; UI/policy owner: OD-014 assurance. | R Q10; KB30 SUBMIT |
| BR-011 | **Ready:** Portal Search Bar route and observation boundaries. **Excluded:** other reference Portal routes as standard fixtures. | TC-008/009/027/029; accepted Portal alternatives. | POC + QA: accept source-scoped route; no actual-menu guarantee. | JOB30; KB30 SHARED-PORTAL; R Q10 |
| BR-012 | **Ready:** required authorization, conditional role explanation, separate one-retry choice/attempt/result. **Blocked:** unavailable authorization and unsupported post-visible errors. | Submission/access targets; VAR-TC-003-F; VAR-TC-006-A–E; VAR-TC-027-E. | POC + QA: accept Q10/Q11 boundaries; policy/UI owner: missing dispositions, especially VAR-TC-006-E. | R Q10/Q11; KB30 SHARED-REQUEST |
| BR-013 | **Ready:** LOB/stage-specific evidence, qualified no-photo continuation and merchant submission report. **Blocked:** evidence substitutes/completeness, individual eligibility or mandatory-condition waiver. | Applicable TC-001–009/025–029 reminders/submission variants. | POC + QA: accept Q7 bounds; policy/UI owner: final mandatory evidence conditions (OD-014). | T Q7; R Q10; KB30 EVIDENCE |
| BR-014 | **Ready:** respect refusal; distinguish task completion from finish. **Conditional:** Q12's TC-004/028 fixture repairs. **Blocked:** unspecified silence disposition. | Ordinary endings; TC-004/028; TC-006; VAR-TC-006-C. | POC + QA and benchmark reviewer: exact Q12 fixture approval; contract owner: silence rule if included. | R Q12; T Q5; JOB30 CLOSING |
| BR-015 | **Ready:** supported offer → later acceptance → one mock terminal; refusal means no transfer. **Conditional:** reason-specific fixture, supported consent form and CT adoption. **Blocked:** broader Tool/semantic compatibility and audio evidence. **Excluded:** real connection assurance. | TC-009/010; VAR-TC-006-B/C; VAR-TC-027-C; supported form-recovery variants. | POC + QA: accept consent/ownership; configuration/content/voice owners: compatibility and CT08–CT11 scope. | R Q13 and terminal ledger; JOB30 |
| BR-016 | **Ready:** genuine scope clarification; cancellation payout remains in scope. **Conditional:** proposed TC-010 menu-update fixture. | TC-010; R C4/C5 corrected-scope controls. | POC + QA/benchmark reviewer: approve exact internal fixture attribution, not a new financial remedy. | R Q13; JOB30 OUT OF SCOPE |
| BR-017 | **Ready:** separate generated/displayed from audible evidence. **Blocked:** voice/terminal judgments without synchronized capture and agreed expectations. | All voice claims; especially TC-003/004/010/026. | Voice/environment owner + QA: OD-013 capture/assessment scope. | Candidate evidence rules; R terminal ledger |
| BR-018 | **Ready:** once-only applicable GM notice, with GF/informational negatives. **Blocked:** certainty policy. **Conditional:** any source-text use must explicitly retain that conflict; no individual award guarantee. | TC-027/029 and GM navigation variants; TC-025/026/028/GF negatives. | POC + QA: accept trigger/order separately; content/policy owner: OD-006 and CT06/OD-011 decision. | JOB30; G; CT06 |
| BR-019 | **Ready:** one actual ordinary failed-action repeat, success observed before continuation. **Blocked:** second-failure/unusable-recovery disposition. | TC-007; VAR-TC-003-D; VAR-TC-027-D by actual failure, distinct from G corrections. | POC + QA: accept Q9 boundary; UI/contract owner: supported further remedy. | R Q9/A2–A5; JOB30 |
| BR-020 | **Ready:** semantic assessment, separate behavior/coverage and preserved historical severity. **Conditional:** controlled-register adoption; no literal oracle until accepted. | All 15 and 18 VARs; CT01–CT14 modes. | POC + QA: accept assessment discipline; content + QA: adopt CT scope/version/channel under OD-011. | PB/PLAN; candidate verdict model/register |

**Cross-cutting exclusions:** real contact-center connection, backend submission/
approval/payment, production reliability, numerical latency SLA and asserted ASR
cause are outside this mock conversational candidate. Exact calendar/payment
computations, unsupported recovery outcomes and alternative Portal routes are not
required outcomes in the initial regression selection. Their supported prefixes
and non-inference prohibitions remain assessable. POC + QA must record these
[candidate exclusions](BASELINE_MODEL.md#outstanding-outcomes-and-explicit-exclusions)
against the affected BR-002/003/009/011/013/015/017 targets; exclusion supplies no remedy.

### Prioritized minimal regression selection

**Proposed lean core: 21 distinct fixtures — 13 original targets plus eight existing
VARs, from the 33 registered TC/VAR entries.** Priority 1 protects access/consent;
2 protects route/status decisions; 3 protects education/decline/finish distinctions.
These are coverage selections, not executed runs or an adopted repetition count.
Use the full existing JRN/VAR definitions, common fixture and source qualifications.
DG references mean existing direct or plausible regression relevance as recorded
in the [impact matrix](DEFECT_GROUP_IMPACT_MATRIX.md#phase-4-cross-tc-regression-reconciliation);
they do not create new DF associations or close a group.

| Priority | Existing targets / variants | Fixtures | BP / BR focus | DG relevance and required discrimination |
|---|---|---:|---|---|
| 1 | TC-006; VAR-TC-006-A | 2 | BP-05/06; BR-012/013/014 | DG-005/007: retry declined versus retry succeeds; normal access is covered separately by TC-003. |
| 1 | TC-009/010 | 2 | BP-05/07; BR-011/012/014/015/016 | DG-002/005/007/009: submit-only failed retry versus unrelated reason; separate later consent and one mock terminal. |
| 1 | VAR-TC-027-C | 1 | BP-06/07; BR-008/014/015 | DG-007/008: GM Portal-unavailable offer explicitly declined; no transfer, then further-help/finish. Never reused as GF access policy. |
| 2 | TC-003/029 | 2 | BP-04/05; BR-005–014/018 | DG-003/004/005/006/008: GF upfront one-by-one versus GM elicited/grouped; status before form/submission; GM transition/notice. |
| 2 | TC-007/008 | 2 | BP-04/05/06; BR-006/007/010/011/012/019 | DG-003/004/005/006/007: actual Date failure/repeat/success versus absent-link accepted Portal fallback. |
| 2 | VAR-TC-003-A/B/C | 3 | BP-04; BR-009/014 | DG-006/007: approved/status-only, approved/unpaid, unclear then clarified. VAR-TC-003-A/B cannot cover TC-003; C needs clarification then the full target. S situation letters differ from VAR suffixes. |
| 2 | VAR-TC-027-D/F/G | 3 | BP-04/05/06; BR-002/005/006/008/010/012/013/018 | DG-002/004/005/006/008: period recheck/new visibility, GM status-only bypass, GM App submit-only negative control. |
| 3 | TC-001/025 | 2 | BP-01; BR-001/002/003/004/013/014 | DG-001/002/003/007/008: GF/GM recent education without navigation, actual delivery and ordinary finish. |
| 3 | TC-002/026 | 2 | BP-02; BP-01 prerequisite; BR-003/005/010/014 | DG-003/006/007/009: separate follow-up, guidance refusal and finish; not accepted-navigation coverage. |
| 3 | TC-004/028 | 2 | BP-03; BR-001/003/013/014 | DG-002/003/007/009: required GF offer/decline versus GM no-offer/acknowledgement; both explicit finish. Q12 fixture approval required. |

**Binding controls for QA review:** retain TC-001/025 as education-only controls,
separate from TC-002/026. Allocate native-empty versus utterance-first entry across
the former pair. Include known versus initially unknown authorized access across
TC-009/006; normal visible-form/no-recovery control in TC-003. Exercise Q7 no-photo
handling for GF and GM in compatible submission fixtures, with no eligibility or
evidence-waiver claim. Use R C3's unclear-offer response then later acceptance in
TC-009, and TC-028's no-offer acknowledgement then explicit finish. These selections
need exact versioned scenario bindings; they allocate no new TC/VAR identities.
TC-028's offered-and-declined ending remains separate unselected local coverage.

**Executable status — held:** no reviewed Phase 4 executable TC/VAR bindings or
current served-configuration identity were found in the existing inventories.
Known Q8 conformance conflicts remain. Existing YAMLs are limited reuse candidates:

- [GM-PORTAL-STATUS-FULL-001 v0.2.1](../../uc4_runner/scenarios/GM-PORTAL-STATUS-FULL-001.yaml)
  supplies the one-by-one status-action slice of VAR-TC-027-F; it ends at the status
  question, not a merchant result, TC-027 transition, submission or finish.
- [KB-GF-MISSING-LINK-001 v0.1.1](../../scenarios/kb-coverage/KB-GF-MISSING-LINK-001.yaml)
  supplies grouped fallback/consent content, not TC-008's one-by-one full target.
- The [existing KB suite](../KB_TEST_COVERAGE.md#suite-design-and-poc-decisions)
  supplies timing, status, form-entry and evidence slices. Its scripts do not report
  actual form submission or accept transfer; its direct timing questions do not
  replace age-only education/decline targets. No current runnable/pass claim follows.

**Explicit omissions and holds:**

- **Deferred combinations:** TC-005 GF elicited-dual/grouped and TC-027 GM upfront-
  dual/one-by-one. Their component criteria have selected controls, but their full
  interactions and original target coverage remain untested. Add TC-005 for changes
  affecting its elicited/grouped combination or DF-007 closure assurance; add TC-027
  for its entry/transition/notice/pacing changes or DF-014 closure assurance.
- **Deferred overlapping variants:** VAR-TC-003-D/E/F, VAR-TC-006-B/C/D and
  VAR-TC-027-A/E. Selected recovery, fallback, handoff and normal-access fixtures
  exercise shared requirements; none earns these omitted variants a coverage pass.
  Person refusal is sampled in VAR-TC-027-C; its accepted-handoff/access-gained
  outcomes are deferred. Add VAR-TC-006-C for changed failed-retry refusal handling,
  and the accepted GM access outcome for GM handoff assurance. Add other omitted
  fixtures when parent/platform effects or a new closure claim require them.
- **Blocked outcomes:** VAR-TC-006-E's final access remedy and VAR-TC-027-B's
  unsupported GM status-policy conclusions; retain assessable clarification/non-
  inference. Other unknown remedies follow the criterion table, not invented steps.
- **Q8 execution hold:** N01–N08 recent-entry profiles and R A5 correction coverage
  need exact fixtures and the documented admission/checkpoint/correction/delivery
  conformance work. The core does not certify Q8 runtime regression or replace it.
- **DG-009 evidence hold:** selected TC-003/004/010/026 require synchronized voice/
  terminal capture for the reported observations. Text runs cannot establish audible
  completion, silence causation or closure. Historical resolutions remain intact.

**Independent assessment:** current axes stay `NOT_RUN / NOT_RUN`. Later, record
behavior against applicable accepted criteria and coverage against the specific
selected target separately. Correct alternate handling may be
`PASS / INCOMPLETE_COVERAGE`; fully traversed incorrect behavior may be `FAIL / PASS`.
Missing specification or environment evidence blocks only its dependent judgment;
retain known violations and the observed prefix. No omitted target is a pass.

### Exact remaining sign-off requirements

1. **Authorized internal POC/business or benchmark reviewer + QA:** supply names,
   authority and date; record accept/amend/exclude/defer for exact BR subcriteria,
   TC/VAR fixtures and candidate/register versions, with rationale and conditions.
   Internal acceptance must not be described as formal Grab approval. All existing
   sign-off fields remain unfilled until this occurs.
2. **Benchmark reviewer + QA:** record precise internal fixture scope and outstanding
   formal attribution for TC-006/007/009/027; approve Q12's TC-004/028 fixture changes
   and the proposed TC-010 menu-update fixture. Record selected VAR outcomes and
   any deliberately omitted combinations; do not re-decide Q1–Q13.
3. **Relevant policy/UI/timing owners:** provide evidence for any included blocked
   status/duplicate/payment remedy, eligibility/evidence/access, authenticated UI,
   further recovery or date/calendar judgment (OD-002/005/007/010/014). Otherwise
   record its exact exclusion/deferment while accepting supported criteria separately.
4. **Content/policy owner + QA:** decide OD-006 certainty and OD-011's exact CT row,
   mode, version, trigger, exception, owner and channel. Source authentication alone
   cannot adopt a literal oracle or settle the GM notice's policy conflict.
5. **QA + authorized POC reviewer:** approve the 21-fixture selection or a documented
   amendment, omissions/addition triggers, executable scenario IDs/versions and
   observation/consent gates, channel and repetition/sampling count (OD-015).
   The historical five-run proposal remains unadopted; full 15-TC/18-VAR coverage
   and group-wide closure are not granted by this reduced selection.
6. **Configuration and voice/environment owners + QA, before later execution or
   conformance claims:** bind the served configuration, resolve applicable known Q8
   conflicts, and establish capture/terminal evidence requirements (OD-013; OD-012
   for new closure assurance). Obtain separate execution authorization. These are
   later execution/evidence prerequisites, not reasons to withhold a ready criterion's
   bounded internal acceptance. **No freeze authorization is requested or recorded.**

## Final internal POC acceptance sign-off sheet

**Review object:** `P2-BASELINE-CANDIDATE-0.1` / `P2-JOURNEYS-0.4` /
`P2-CONTROLLED-TEXT-0.1`. **NOT FROZEN.**
**Behavior verdict: NOT_RUN. Coverage verdict: NOT_RUN.**

**Confirmed reviewer ownership:** the project owner will temporarily serve as both
**Internal POC Engineering Acceptance Reviewer** and **Internal POC QA Reviewer**.
This is a **dual-role, self-review arrangement for the isolated POC**.
**Independent QA review remains deferred; no independent QA validation is claimed.**
**Formal Grab business-policy approval remains pending.** Personal name, approval
date and completed sign-off have not been supplied. Ownership confirmation is not
acceptance sign-off or formal business/benchmark authority.

For internal POC decisions below, “reviewer and QA” / “Project owner + QA” denote
the same project owner acting in both capacities. Formal benchmark/QA review and
the separately required policy/UI/timing/content/voice/configuration authority or
evidence retain their stated limits; dual-role ownership supplies none of them.

This sheet records the current roles and prepares one consolidated decision. Earlier
unassigned-role statements retain their historical scope; the original agreements,
qualified Q1–Q13 and separately namespaced OD-002 Q1–Q4 remain controlling.
All decisions below are **pending**. Readiness labels apply to **subcriteria**;
a BR can occur in several groups. The [20-BR matrix](#criterion-level-acceptance-recommendations)
supplies detailed applicability, affected TC/VAR identities and sources.

### Proposed fixture scope

| Selection | Exact existing identities | Count |
|---|---|---:|
| Original benchmark targets | TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-025, TC-026, TC-027, TC-028, TC-029 | 15 |
| Selected variants | VAR-TC-003-A, VAR-TC-003-B, VAR-TC-003-C, VAR-TC-006-A, VAR-TC-027-C, VAR-TC-027-D, VAR-TC-027-F, VAR-TC-027-G | 8 |
| Proposed initial baseline | All original targets above plus the eight selected variants | **23** |
| Separate smoke/regression subset | The [Phase 5 core](#prioritized-minimal-regression-selection): 13 original targets above, excluding TC-005 and TC-027, plus the same eight variants | **21** |

**23 = 21 + TC-005 + TC-027.** Their Phase 5 deferral now applies only to the
smoke subset; both full original targets are proposed for the initial baseline.
The 21-fixture core retains its priorities, binding controls and promotion triggers;
it does **not** cover all 15 original targets. Counts are proposed fixtures, not
runs, repetitions or achieved coverage. `VAR-TC-027-C` selects **person offer
declined**; accepted handoff/access-gained outcomes remain unselected. The other
ten registered variants and Q8 supplemental-profile/voice holds remain as recorded
in Phase 5. Selecting all original TCs does not settle their fixture conflicts.

### Ready — proposed for provisional internal POC acceptance

The reviewer and QA may accept these bounded criteria explicitly; no whole BR or
fixture is accepted by this recommendation. All existing applicability limits apply.

| BR | Source-supported subcriterion |
|---|---|
| BR-001 | Reuse known order/LOB/goal; clarify genuinely missing or ambiguous facts. |
| BR-002 | Declared cancellation-age routing and Q6 same-date UTC+8 fixture; no eligibility/payment inference. |
| BR-003 | Entry-specific education, offers and suppression; actual delivery; distinguish approval, payout and bank receipt. |
| BR-004 | Applicable normal opening/disclosure once, with correct ownership. |
| BR-005 | Ask necessary preferences once; preserve compatible progress and the narrow GM status-only exception. |
| BR-006 | One-action/wait or grouped decision segments; distinct status, form and submission observations. |
| BR-007 | GF App status route; History only when the relevant order is missing. |
| BR-008 | GM computer-Portal status/readiness; preserve transition and App submit-only distinction. |
| BR-009 | Observe/clarify actual status and remaining goal before status-dependent submission. |
| BR-010 | Separate link/article/scroll/form observations; separately accepted Portal fallback; no role/eligibility inference. |
| BR-011 | Supported Portal Search Bar submission route and observation boundaries. |
| BR-012 | Required authorization, conditional role explanation and separate retry choice, attempt and result. |
| BR-013 | LOB/stage-specific evidence, qualified Q7 no-photo continuation and merchant-reported self-submission. |
| BR-014 | Respect refusal; distinguish task completion, unresolved concern and explicit finish. |
| BR-015 | Supported person offer, later explicit acceptance, one Flow-owned mock terminal; refusal means no transfer. |
| BR-016 | Clarify genuine scope ambiguity; cancellation payout remains in scope. |
| BR-017 | Separate generated/displayed evidence from audible evidence; an assessment discipline. |
| BR-018 | Applicable GM notice once before navigation, with GF/informational negative controls; timing independent of certainty. |
| BR-019 | One repeat of an actual ordinary failed action; observe success before advancing; distinguish Q8 corrections. |
| BR-020 | Semantic/process assessment, separate behavior/coverage and preserved historical severity; an assessment discipline. |

### Conditional — accept only with recorded bounds

| BR / scope | Exact condition for internal acceptance |
|---|---|
| BR-004 | Select native-empty/utterance-first entry and channel fixtures explicitly. |
| BR-007/008/012/014/015/016; fixture-dependent criteria | Project owner + QA must record exact internal TC-006/007/009/027 fixtures, Q12 TC-004/028 repairs, proposed TC-010 menu-update fixture, and reason/response-specific handoff outcomes. Role confirmation accepts none of them; formal benchmark attribution still needs authorized benchmark/QA review. |
| BR-009 | Retain OD-002's provisional GF reported-approval/status-only and unpaid explanations with their qualifications; no automatic GM extension or financial remedy. |
| BR-003/004/008/013/014/015/016/018/020; controlled text | Content reviewer + QA must adopt exact applicable CT row, mode, version, trigger, exception, owner and channel under OD-011. Authenticated quotations alone do not authorize literal grading. CT13 retains UI-identity mode; CT14 semantic mode. CT06 source-text use must retain the separate OD-006 certainty conflict. |

### Blocked — dependent judgment awaits evidence

| BR / judgment | Reason and required disposition |
|---|---|
| BR-002/003/013: official calendar, absolute/midnight dates and deadline applicability | OD-005/014 timing/policy authority absent; declared Q6 fixture remains reviewable. |
| BR-009: canonical/GM alternative status meanings, duplicate exceptions and unpaid remedy | OD-002/014 policy/financial evidence absent; bounded GF explanations remain reviewable. |
| BR-006/007/008/019: repeated failure, still-missing order or unusable recovery | Supported next remedy absent; policy/UI/contract owner must supply it. Preserve observed prefix and non-advancement rules. |
| BR-008/010/011/012/013: real UI, early form acceptance, eligibility, evidence substitutes/completeness | Authenticated screens and final policy/mandatory conditions absent under OD-014; no waiver or acceptance guarantee. |
| BR-010/011/012/013/014/015: unavailable GF Portal/authorization or post-visible submission error | No established next disposition under OD-010/014; do not transplant the GM access offer or infer transfer entitlement. |
| BR-014/015: unspecified silence disposition or broader consent/Tool compatibility | Supported contract absent; silence is not finish or transfer consent. |
| BR-018: CT06 compensation-policy certainty | OD-006 source conflict unresolved; policy owner decision required independently of notice timing and OD-011 wording adoption. |
| BR-004/014/015/017: audible opening/closing/transfer and voice-defect assurance | OD-013 expectations and synchronized audio/terminal evidence absent; text cannot certify playback or DG-009 closure. |

Current served-configuration and applicable Q8 admission/checkpoint/correction/
delivery conformance are also unverified. This blocks runtime assurance, separately
from accepting a supported criterion. Preserve known violations and assessable
prefixes when only a dependent outcome is blocked.

### Excluded — outside the proposed assessment

| Affected BRs | Proposed exclusion and reason |
|---|---|
| BR-002/003/009/013/015 | Exact calendar/payment computation and real backend submission, approval, payment or contact-center connection: beyond declared fixtures/mock conversational evidence. |
| BR-006/007/008/010/011/012/014/015/019 | Alternative Portal routes as standard fixtures, invented further remedies and unspecified silence-timeout outcomes: unsupported/unselected in this candidate; supported prefixes remain in scope. |
| BR-017/020 | Production reliability, numerical latency SLA and asserted ASR/barge-in cause: no adopted threshold, sampling authority or causal evidence. |

These exclusions require explicit recorded dispositions; they neither settle a
blocked policy question nor remove original TC/DF history or unselected VAR identities.

### Exact versions and pre-test evidence

The linked manifests supply the **exact archive/member locators and full SHA-256
fingerprints**, incorporated by reference rather than replaced by this sheet.

| Binding | Required reference / present limit |
|---|---|
| Acceptance sources | [P2-BASELINE-CANDIDATE-0.1](BASELINE_MODEL.md#phase-4-scoped-acceptance-baseline-review-candidate), [P2-JOURNEYS-0.4](JOURNEY_PILOT.md#catalog-index-and-version-scope), [P2-CONTROLLED-TEXT-0.1](BASELINE_MODEL.md#controlled-language-applicability-register); 20 BRs plus qualified applicability, 18 retained VAR definitions. |
| Governing agreements | `P2-ENG-DECISIONS-0.3`; `OD002-REVIEW-0.2`; `OD004-OD005-REVIEW-0.2`; `OD004-RECENT-GUIDANCE-REVIEW-0.2`; `OD007-OD010-OD009-REVIEW-0.2`. Exact records and historical snapshot are in [source/configuration references](BASELINE_MODEL.md#source-and-configuration-references). |
| Original benchmark/process sources | WB `Grab_UC4_Benchmark_Test_Scenarios_Feedback (3).xlsx`, Scenarios rows 4–18 / Defect Log rows 5–22; October 23 PLAN/PB bundle, PB v1.0. Use [source locators](BASELINE_MODEL.md#sources-and-authority) and [fingerprints](BASELINE_MODEL.md#fingerprints). |
| Historical configuration reference | `Package-Naufal_2026-10-30_06-38-33.zip`; JOB30 `nodeData/6ae43b6f90878ce305636d97`, `/localizedData/0/config/instructions`; KB30 17 v0.3.0 articles / 20 chunks, formal approval pending. Export/Job hashes are in the fingerprint table; exact Flow/Tool/Code members in the [static ledger](OD004_OD005_TRIGGER_TIMING_REVIEW.md#static-tool-code-and-wiring-ledger) and [terminal ledger](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#terminal-member-ledger-and-wiring). Historical export is not current deployment. |
| Current executable/configuration binding | `configuration_id=null`; current served revision/model/settings/Endpoint binding and reviewed TC/VAR executable bindings remain unverified. [Runner metadata](../../pyproject.toml) is `uc4-runner` v`0.2.0`, not an executed revision. Existing YAMLs retain only their [documented partial reuse](#prioritized-minimal-regression-selection). |

Before separately authorized testing, establish:

1. **Reviewed scope and executable fixtures:** exact scenario IDs/versions/hashes and
   runner revision/content hash for each selected TC/JRN/VAR outcome; observation/
   consent gates and Phase 5 controls. Record channel/language and OD-015 sampling
   separately for the 23-fixture baseline and 21-fixture subset; five runs remains
   an unadopted proposal. Retain Q8 N01–N08/correction holds until exact bindings
   and applicable conformance evidence exist.
2. **Reproducible context:** [common fixture](JOURNEY_PILOT.md#common-contract)
   `2026-11-04`, Wednesday, Asia/Kuala_Lumpur UTC+8, same-date conversation;
   recent age 1 day / older 14 days, with TC-010 and direct GM status-only exceptions.
   Version any changed reference; record intended versus actual initialization,
   order/LOB/goal, opening state, access and merchant observations separately.
3. **Served configuration evidence:** captured timestamp; Flow/Job/Agent/KB/Tool/Code
   revisions or stable IDs plus hashes; model/settings; effective Endpoint-to-revision
   binding and observed initialization. Resolve applicable known Q8 conflicts for
   conformance claims; historical member hashes cannot fill current fields.
4. **Capture plan before execution; records from each later run:** execution/batch/
   fresh-conversation IDs, target and configuration binding, timestamp/timezone,
   transcript/trace paths and hashes, attempted/skipped turns, action/observation/
   consent/terminal events and source-linked separate assessments. Voice claims
   require synchronized recognized input, generated/displayed output, audible
   playback/interruption timing and terminal trace. Current execution/evidence IDs
   remain `null`; QA/voice owners must agree OD-013 expectations and capture first.
5. **QA and authorization:** complete the decision record below, required scoped
   acceptance and later baseline-freeze decision under existing OD-015 governance
   before baseline execution. Obtain separate execution authorization specifying
   fixtures, environment, channel and sampling; real conversations, including
   Cognigy Test Mode, require explicit user authorization. No such authorization or
   freeze is recorded here.

### Decision record — pending

**One consolidated internal POC decision, one signature in both capacities.**
The proposed approval below is **not yet adopted**. An acceptance would:

1. Provisionally accept the **Ready subcriteria** for isolated POC evaluation under
   `P2-BASELINE-CANDIDATE-0.1`, `P2-JOURNEYS-0.4` and `P2-CONTROLLED-TEXT-0.1`,
   with their existing applicability and source qualifications.
2. Approve the **23-fixture assessment selection** (15 original TCs plus eight
   selected variants), retaining the **21-fixture smoke/regression subset** and
   its separate purpose. Selection does not certify fixtures or achieved coverage.
3. Record the existing **Conditional bounds, blocked judgments and exclusions**
   with their stated reasons. Unresolved conditional fixture/text choices remain
   pending unless explicitly resolved in this decision with the required authority
   and evidence; an overall acceptance does not silently adopt them.

Record **accept / amend / exclude / defer**, precise BR/JRN/VAR/CT versions,
exceptions, rationale/source and any explicit conditional resolutions. Detailed
executable bindings, channel, capture, sampling and controlled-text adoption remain
pending unless specifically recorded; all pre-test prerequisites above still apply.

| Required entry | Current record |
|---|---|
| Decision-maker and capacities | **Project owner — Internal POC Engineering Acceptance Reviewer and Internal POC QA Reviewer**; temporary isolated-POC dual-role self-review; ownership confirmed only. |
| Consolidated acceptance decision | _Pending_ for the proposed approval above; no acceptance sign-off recorded. |
| Personal name / single signature / decision date | _Not supplied / not supplied / not supplied_. |
| Conditions, amendments and explicit conditional resolutions | _No new decisions recorded_; existing bounds and unresolved choices remain. Record exact scope, rationale, authority and evidence for any resolution. |
| Independent QA / formal approval | Independent QA review **deferred**; no independent QA validation claimed. Formal Grab business-policy approval **pending**; formal benchmark attribution remains separately pending. |
| Execution authorization | _Not granted_; authorizer, scope and date: _not supplied_. |

**Preparation only. Baseline NOT FROZEN; behavior NOT_RUN / coverage NOT_RUN.**

## Recorded scoped internal POC acceptance

**Decision: ACCEPTED — scoped internal POC criteria and fixture selection only.**
The [supplied acceptance decision record](../../reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md)
is preserved byte-for-byte from
`C:\Users\Nau\Downloads\UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md`;
SHA-256 `8ee7d8e978b437553935f628e263b0ef20f3380727e3cdef92380556d2586a81`.
Its declaration is reproduced exactly:

> I approve the scoped internal POC acceptance: Ready subcriteria of the 20 BRs, the 23-fixture selection while retaining the 21-fixture smoke subset, and the documented conditions, blocked judgments and exclusions. This is self-reviewed internal POC acceptance only. No baseline freeze or test execution authorization.

| Decision field | Recorded scope / evidence |
|---|---|
| Decision-maker and review capacities | Project owner; temporary **Internal POC Engineering Acceptance Reviewer and Internal POC QA Reviewer**. **Self-review**, not independent QA validation. |
| Declaration date / signature | **2026-11-04**, as stated in the supplied record; conversation date, not an authenticated signing timestamp. Personal name and handwritten/digital signature **not supplied**. |
| Review objects | `P2-BASELINE-CANDIDATE-0.1`, `P2-JOURNEYS-0.4`, `P2-CONTROLLED-TEXT-0.1`; existing BR classifications, source qualifications and qualified Q1–Q13 retained. |
| Accepted criteria | The [Ready subcriteria](#ready--proposed-for-provisional-internal-poc-acceptance) of all 20 BRs for provisional isolated-POC evaluation; not whole-BR or implementation acceptance. |
| Accepted selection | The [23 fixture identities](#proposed-fixture-scope): all 15 original targets and eight selected variants. Separate **21-fixture smoke/regression subset** retained; TC-005/027 included only in the full selection. VAR-TC-027-C remains person-offer declined. |
| Conditions and dispositions | Documented Conditional bounds, Blocked judgments, Excluded outcomes and reasons retained. No unresolved fixture conflict, controlled wording or unsupported outcome is silently approved. |
| Remaining authority and execution limits | Independent QA deferred; formal Grab business-policy/benchmark approval pending. Configuration, executable bindings, evidence/channel/sampling and exact conditional choices remain outstanding. **No execution, runtime change, regrade or freeze authorized.** |

**Provenance limit:** the supplied record names `problem2(6).zip`; that exact archive
was not located. The available local `docs/problem2/problem2.zip` contains a worksheet
member byte-identical to the pre-update worksheet (SHA-256
`e658f4ee6e3e83b16e3dbc0eec7c0a4e03a550c57133a2175168e96d04d33f28`).
Archive identity/renaming is not inferred. The supplied declaration and the owner's
current explicit confirmation establish the stated scope; historical records remain
intact. The new [readiness assessment](EXECUTION_READINESS.md) records the next gate.

**Baseline NOT FROZEN; execution NOT AUTHORIZED; behavior NOT_RUN / coverage NOT_RUN.**
