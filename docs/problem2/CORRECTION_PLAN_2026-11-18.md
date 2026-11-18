# UC4 Problem #2 — correction plan

**Date:** 2026-11-18

**Status:** PROPOSED — owner review pending.

**Scope:** Saved evidence only. No Cognigy changes, live requests, regrade,
workbook edits or defect closures.

## Recommendation

Prepare small corrections to the observed Agent behavior. Start with the
outstanding opening, then protect required observations and apply the correct
education triggers. Use focused retests after separate approval.

This plan groups observations by business requirement. A group does not establish
a shared technical cause. The 10 failed runs are not 10 confirmed engineering bugs.
No technical root cause has been established.

## Current position

- One run was attempted for each of the 15 primary benchmark cases on November
  16/17: **5 scoped PASS and 10 FAIL**.
- Text-target coverage was **9 COMPLETE and 6 PARTIAL**. COMPLETE means traversal
  of the text target, not correct behavior, backend success or terminal execution.
- These 15 runs contain **127 POSTs, all HTTP 200, with zero HTTP retries**.
  This excludes older stopped collections. It is not a reliability rate or proof
  that all runs used the same served configuration.
- The cumulative [workbook][workbook], [summary][summary] and original assessments
  remain the result records. This plan does not change their verdicts.
- The [scoped internal POC acceptance][acceptance] remains in place. Preserve the
  23-fixture selection and the separate 21-fixture smoke subset. The selected
  scenario variants have not been executed in these 15 runs.

Agent replies are captured REST/text evidence. Merchant screen, access, evidence
and submission statements are declared simulations. Served revision, effective
model and Knowledge binding remain unverified. Actual UI/backend actions, audio,
human connection and Tool/Flow-owned terminal execution remain unverified.

## Proposed behavior corrections

The order below is a review recommendation, not a severity rating or an approved
implementation. Each retest list is a candidate pool, not an execution instruction.
Business requirements come from the [requirement register][requirements]; trigger
references come from the [education trigger review][triggers].

### 1. Deliver the outstanding opening once

- **Evidence:** [TC-004][e004] T1–T3, [TC-010][e010] T1–T2 and [TC-026][e026]
  T1 omit the outstanding opening/identity/recording-purpose disclosure.
- **Requirement:** BR-004; [common opening contract][common].
- **Proposed correction:** For normal utterance-first entry with no prior
  opening, deliver the applicable opening before substantive education or
  guidance. Do not repeat it later. Preserve known merchant facts, already-emitted
  openings, native-empty entry ownership and existing safety priority.
- **Retest:** TC-004/010/026. Use TC-001/025 as previously passing normal-entry
  controls. Check the whole reply order, not only whether opening words occur.
- **Existing finding:** TC-004 re-observes [P2-AGENT-002][f002]. TC-010/026 concern
  the same requirement; a shared technical cause is not established. The earlier
  TC-003 late-opening observation was not reproduced and is not closed.

### 2. Ask the missing goal before older-order education

- **Evidence:** [TC-004][e004] T1 and [TC-028][e028] T1 give education and a guidance
  offer on an older age-only entry. The goal question never occurs. TC-004 also
  has no existing-photo reminder in its captured replies.
- **Requirement:** BR-001/003, T02 followed by the applicable T05/T06.
- **Proposed correction:** Ask the genuinely missing goal and wait. Then apply
  the correct business-line and entry-context rule. For TC-004's elicited general
  inquiry, give qualified GF education, the conditional existing-prepared-food-photo
  reminder and the required offer. Do not add that GF reminder to older GM inquiry.
  TC-028's general-inquiry offer remains optional; a finish signal is still required.
- **Retest:** TC-004/028. Protect recent age-only education with TC-001/025 and
  elicited dual-goal handling with TC-005/029. These triggers must not be made universal.
- **Existing finding:** TC-004 re-observes the early-education/missing-goal prefix
  of [P2-AGENT-003][f003]. Its historical later premature preference intake was
  not reproduced. TC-028 is a requirement analogy. Q12 fixture limits remain provisional.

### 3. Do not repeat an offer after a clear direct navigation request

- **Evidence:** [TC-008][e008] T1 and [TC-027][e027] T1 give unsolicited timing
  education and another guidance offer despite clear upfront dual intent.
- **Requirement:** BR-003/005, T08 and qualified Q3.
- **Proposed correction:** Retain the direct request as guidance consent. Collect
  only missing required facts/preferences, then use the supported route. Preserve
  the opening, applicable GM notice and Portal-readiness requirements. Do not
  suppress education or offers when a different entry context requires them.
- **Retest:** TC-008/027. Contrast TC-003's direct entry with TC-005/029's elicited
  dual goal. Protect TC-009's submit-only goal. These are run-local observations,
  not a demonstrated common cause of P2-AGENT-003.

### 4. Observe compensation status before conditional request navigation

- **Evidence:** [TC-003][e003] T8 directs “Request for compensation” after the
  merchant reports only that order details are open. No compensation-status
  question or report occurs.
- **Requirement:** BR-007/009/010; [JRN-TC-003][j003] M05/M06.
- **Proposed correction:** Obtain the merchant-observed compensation status and
  retain the pending review goal before choosing status-dependent submission.
  Order visibility is not status. Unread status is not blank status.
- **Retest:** TC-003's visible-blank target, with TC-005 as a status-before-request
  control and TC-009 as a submit-only control. Do not add a status prerequisite to
  submit-only navigation. VAR-TC-003-A/B/C require separate fresh runs if selected;
  correct alternative handling does not complete the primary submission target.

### 5. Pause for computer-Portal readiness before its controls

- **Evidence:** [TC-029][e029] T6 explains the computer Portal, then gives Finance,
  Transactions, period/store and Category instructions while the merchant is still
  App-selected. There is no Portal-readiness exchange.
- **Requirement:** BR-005/008/009; [JRN-TC-029][j029] M03 before M04.
- **Proposed correction:** Explain the App-to-computer-Portal transition and wait
  for readiness. Only then give the supported status segment. All-at-once pacing
  does not remove this prerequisite. Preserve known preferences.
- **Retest:** TC-029, using TC-027's observed readiness segment as a contrast,
  not an overall PASS control. If the change affects broader GM intake, consider
  separately approved VAR-TC-027-F/G controls for the narrow status-only exception
  and App submission-only route.
- **Limit:** This is a readiness failure, not a ban on grouped guidance.
  Historical DF-016 “Not a defect” remains unchanged.

### 6. Wait for date-selection completion before Confirm

- **Evidence:** [TC-007][e007] T10 directs Confirm after the merchant reports
  only that the Date selector opened. Date selection is reported later at T11.
- **Requirement:** BR-006/007/019; [JRN-TC-007][j007] M04/M05.
- **Proposed correction:** Distinguish opening the selector from selecting a
  date. Wait for the pending selection to complete before Confirm. Preserve the
  one supported repeat after the first declared stuck action; do not invent
  another retry or transfer.
- **Retest:** TC-007's first-failure/repeat/success path. Protect TC-003/005's
  visible-order paths from unnecessary History/date recovery.

### 7. Keep details and evidence separate in one-by-one guidance

- **Evidence:** [TC-008][e008] T16 bundles filling order details and attaching a
  prepared-food photo after one-by-one pacing was selected.
- **Requirement:** BR-006/013; [JRN-TC-008][j008] M06.
- **Proposed correction:** Give the current details action and wait. Then give
  the applicable evidence instruction, with the existing qualified no-photo
  handling. Obtain the merchant's submission report before acknowledging submission.
- **Retest:** TC-008 after its evidence fixture is reviewed. Use TC-005's grouped
  path as a contrast: supported grouping is not itself a defect. Do not use this
  pacing correction to impose a new evidence policy.

### 8. Reuse clear order-visibility reports

- **Evidence:** [TC-003][e003] T6 and [TC-007][e007] T12 ask whether the order is
  visible immediately after the merchant explicitly reports visibility.
- **Requirement:** BR-001/005 and the [common context-retention contract][common].
- **Proposed correction:** Use the supplied same-order observation and continue
  to the next valid action. Clarify only if the report is ambiguous, contradicted
  or made invalid by corrected facts. Do not remove necessary status questions.
- **Retest:** TC-003/007. Check that clear visibility is retained while actual
  status, form and submission observations remain separate.

## Keep these decisions and gaps separate

| Item | Evidence and current classification | Required next action / later check |
|---|---|---|
| Eligibility linked to request-control visibility | [TC-002][e002] T2 and [TC-026][e026] T2. Recorded scoped failures with a source/criterion conflict, not proven false Grab policy. TC-002 re-observes [P2-AGENT-001][f001]; TC-026 is the GM requirement analogy. | Owner/implementer must reconcile the historical FOLLOW-UP wording with the already accepted scoped criterion before claiming correction. Proposed behavior: explain the supported conditional review option without an eligibility↔visibility assurance. Retest TC-002/026 through offer, refusal, further help and explicit finish. Do not invent an eligibility or payment decision. |
| GM notice certainty | [TC-027][e027] T5 and [TC-029][e029] T6 each emit the notice once before navigation. “Will be partial” remains an OD-006 conversation-quality warning/conflict, not a new literal failure rule. | Business/content review must resolve certainty and wording authority under [OD-006/011][decisions]. Do not change contested wording in an unrelated correction or promise an individual award. Preserve the current scoped once-only placement; later check TC-027/029 and timing-only negative controls TC-001/025. |
| Unspecified photo availability | [TC-007 assessment][a007], especially T19/T20, and [TC-008 assessment][a008]. Generic supporting evidence proves neither photo availability nor absence. TC-007's repeated photo request is not registered as an Agent evidence-policy defect. Submission/finish remain unobserved. | Before retesting through this stage, the test preparer and reviewer must record explicit evidence availability and conditional responses in a reviewed fixture version. A no-photo alternative needs its own defined fresh run if selected. Preserve Q7's qualified continuation; do not invent a photo, substitute equivalence, acceptance or approval. Do not edit old transcripts or grades. |
| Completion-plus-submit phrasing | [TC-027][e027] T17/T18. Separate review note, not another confirmed pacing defect. The actual information acknowledgement and later submission instruction were separate. | Reviewer checks the conditional wording and action boundaries. Do not add a hard failure or a correction merely by analogy with TC-008 T16. |

These gaps do not block review of unrelated observed deviations. The
[qualified recovery/access/finish decisions][recovery] and existing internal
acceptance are settled inputs, not questions to restart.

## Focused retest proposal

**Suggested first slice, after an opening-only correction is approved and
implemented:** TC-004/010/026, plus TC-001/025 as normal-entry controls. Review the
opening requirement independently: TC-004 or TC-026 can still FAIL for another
requirement even if the opening is corrected.

For later corrections, select only the affected candidate pools above. Preserve
the five previously passing controls: [TC-001][e001], [TC-005][e005],
[TC-006][e006], [TC-009][e009] and [TC-025][e025]. TC-006 protects retry refusal;
TC-009 protects submit-only handling and separate transfer consent. A past PASS
does not guarantee a future PASS.

Before any live retest:

1. Identify the served Flow/Job, relevant Tool/Code, effective model and Knowledge
   binding through owner-supplied or read-only configuration evidence. Record
   versions/fingerprints before and after the approved change. The November 13
   static export does not prove what served the November 16/17 runs.
2. Review the exact proposed change and its affected boundaries. Prefer minimal
   existing instructions/contracts and preserve Agent-first ownership. Do not
   introduce a new controller, persistent walkthrough model or broad runner rewrite.
3. Review scenario versions, declared date/UTC+8 assumptions, evidence availability,
   conditional merchant responses and advancement gates. Keep business behavior
   and target-branch coverage independent. Do not supply hidden fixture facts
   before their actual trigger or treat Agent instructions as completed actions.
4. Obtain explicit approval for the exact change and, separately, the named live
   runs and per-run request limits. Use fresh conversations, sequential execution,
   no HTTP retries/replacements/probes, and a collection-wide stop on technical
   error. Stop an affected run when a required progression condition is missing.
   Do not resume the consumed November 16/17 conversations.
5. Save new evidence separately. Assess semantic business behavior and coverage,
   retaining applicable controlled-language limits. Do not close a finding from
   HTTP 200, text-target COMPLETE, or a successful different business branch.

No repetition count, request budget, variant execution or live permission is
created by this plan.

## Owner review and preservation

- **Decision now:** review the proposed correction order and select the first
  change scope. Recommendation: start with the outstanding opening.
- **Still needed:** the implementer and test reviewer, configuration evidence,
  the exact change proposal, and separate implementation/execution approvals.
  Independent QA and formal Grab approval are not established by this plan.
- Preserve the original benchmark, source workbook, cumulative result workbooks,
  saved transcripts, assessments and DF history. In particular, do not reopen
  DF-001 Closed/Pass, DF-014/018 owner-resolved, or DF-016 Not a defect.
- Do not infer resolution of earlier HTTP 500/502 causes, voice/ASR/barge-in
  reports, authenticated UI/access, backend payment or exactly-once terminal
  behavior. No baseline freeze or release recommendation is made.

## Offline verification

All **334 file hashes listed in the five existing verification manifests**
matched. All **339 files** in those five evidence directories, including their
manifests, matched the before/after inventory. The five cumulative workbooks
passed ZIP integrity checks. Documentation checks cover 32 relative link targets,
six heading anchors and whitespace. No live requests were sent for this plan.
This is evidence organisation, not a regrade or new Agent execution.

[requirements]: BASELINE_MODEL.md
[triggers]: OD004_OD005_TRIGGER_TIMING_REVIEW.md
[recovery]: OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md
[decisions]: OPEN_DECISIONS.md#decision-register
[common]: JOURNEY_PILOT.md#common-contract
[j003]: JOURNEY_PILOT.md#jrn-tc-003
[j007]: JOURNEY_PILOT.md#jrn-tc-007
[j008]: JOURNEY_PILOT.md#jrn-tc-008
[j029]: JOURNEY_PILOT.md#jrn-tc-029
[f001]: follow-up-2026-11-07/P2-AGENT-001.md
[f002]: follow-up-2026-11-07/P2-AGENT-002.md
[f003]: follow-up-2026-11-07/P2-AGENT-003.md
[acceptance]: ../../reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md
[workbook]: ../../reports/problem2-pilots/rest-restart/20261117T064316Z-TC025-029-6b209e6a/UC4_Adaptive_REST_Testing_v0.3_results.xlsx
[summary]: ../../reports/problem2-pilots/rest-restart/20261117T064316Z-TC025-029-6b209e6a/summary.md
[e001]: ../../reports/problem2-pilots/rest-restart/20261116T074523Z-3e0f6787/transcript.md
[e002]: ../../reports/problem2-pilots/rest-restart/20261116T080116Z-TC002-6b05f0e8/transcript.md
[e003]: ../../reports/problem2-pilots/rest-restart/20261116T081952Z-TC003-005-356d79b8/TC-003/transcript.md
[e004]: ../../reports/problem2-pilots/rest-restart/20261116T081952Z-TC003-005-356d79b8/TC-004/transcript.md
[e005]: ../../reports/problem2-pilots/rest-restart/20261116T081952Z-TC003-005-356d79b8/TC-005/transcript.md
[e006]: ../../reports/problem2-pilots/rest-restart/20261116T090542Z-TC006-010-f17330c4/TC-006/transcript.md
[e007]: ../../reports/problem2-pilots/rest-restart/20261116T090542Z-TC006-010-f17330c4/TC-007/transcript.md
[e008]: ../../reports/problem2-pilots/rest-restart/20261116T090542Z-TC006-010-f17330c4/TC-008/transcript.md
[e009]: ../../reports/problem2-pilots/rest-restart/20261116T090542Z-TC006-010-f17330c4/TC-009/transcript.md
[e010]: ../../reports/problem2-pilots/rest-restart/20261116T090542Z-TC006-010-f17330c4/TC-010/transcript.md
[e025]: ../../reports/problem2-pilots/rest-restart/20261117T064316Z-TC025-029-6b209e6a/TC-025/transcript.md
[e026]: ../../reports/problem2-pilots/rest-restart/20261117T064316Z-TC025-029-6b209e6a/TC-026/transcript.md
[e027]: ../../reports/problem2-pilots/rest-restart/20261117T064316Z-TC025-029-6b209e6a/TC-027/transcript.md
[e028]: ../../reports/problem2-pilots/rest-restart/20261117T064316Z-TC025-029-6b209e6a/TC-028/transcript.md
[e029]: ../../reports/problem2-pilots/rest-restart/20261117T064316Z-TC025-029-6b209e6a/TC-029/transcript.md
[a007]: ../../reports/problem2-pilots/rest-restart/20261116T090542Z-TC006-010-f17330c4/TC-007/assessment.json
[a008]: ../../reports/problem2-pilots/rest-restart/20261116T090542Z-TC006-010-f17330c4/TC-008/assessment.json
