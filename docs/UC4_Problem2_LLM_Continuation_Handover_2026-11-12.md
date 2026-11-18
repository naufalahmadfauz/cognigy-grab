# UC4 / Problem #2 — LLM Continuation Handover

**Project:** Malaysia GrabFood / GrabMart — Cancelled-Order Compensation AI Agent (Cognigy.AI)  
**Handover date:** 12 November 2026 (Asia/Jakarta)  
**Handover type:** State-preserving context for the next LLM / developer  
**Primary focus:** Problem #2 — Benchmark, Business Journeys, Semantic Acceptance, Defect Traceability and Manual Testing  
**Status:** **DOCUMENTATION / SCOPED POC TEST DESIGN READY · NEW v0.3 MANUAL EXECUTION NOT STARTED · FORMAL GRAB ACCEPTANCE PENDING**  
**IMPORTANT:** This is a continuation record, **not** a new audit, implementation plan, approval, request to change Cognigy, or claim that the Agent passes the benchmark.

---

## 0. READ THIS FIRST — instructions for the successor LLM

You are continuing **UC4 Problem #2**. **Do not restart the journey architecture, classify the 15 benchmark cases again from scratch, or propose a fresh generic testing strategy.** A substantial documented baseline already exists. Use the following sequence:

1. **Read this handover completely.** Treat dates and status labels as material: newer records supersede older *status narratives*, but do not erase historical evidence.
2. Read `UC4_Adaptive_Manual_Playbook_v0.3.md` and `UC4_Adaptive_Manual_Testing_v0.3.xlsx` (9 Nov 2026) before proposing any new benchmark execution. The manual pack is **adaptive, condition-triggered and not yet executed**.
3. Read `UC4_Problem2_Current_Progress_and_REST_ExitPlan_2026-11-07.docx` for the historical REST evidence and paused-automation decision.
4. Read `UC4_Problem2_Business_Journeys_Human_Review_Report_2026-11-02.docx`, `README(4).md`, `BASELINE_MODEL(1).md`, `OPEN_DECISIONS.md`, and the 23 Oct playbook for design provenance. Check for later review overlays before interpreting an older “open” label as current.
5. Use the **original Grab benchmark workbook** as an immutable stakeholder reference; distinguish its example transcript from an approved business policy. The user supplied a direct Google Drive link, recorded in §2.
6. Use the **12 Nov Cognigy Flow ZIP** as the most recently supplied **static export snapshot**, not automatically the effective running Endpoint/Agent/Knowledge configuration. Do not confuse resource-reference equality or static integrity with deployment proof.
7. On the user's next request, **continue the concrete work they ask for** (e.g. executing manual tests, documenting results, reviewing a particular decision, or preparing a focused patch). Do not invent a new task or silently perform Flow fixes.
8. Preserve all pre-existing benchmark test IDs, defect IDs, prior verdicts, traces, project-side decisions and approval qualifications. When evidence is missing, use `UNKNOWN`, `CONFLICT`, `BLOCKED_SPEC`, `BLOCKED_ENV`, `NOT_RUN` or `NEEDS_REVIEW` rather than fabricating closure.

### Handover in one paragraph

Problem #2 changes UC4 evaluation from **verbatim scripted conversation matching** to **correct merchant business process, necessary milestones, grounded facts, sequencing, consent and outcomes**, with **behavior correctness scored separately from target test-branch coverage**. Fifteen official Grab TCs and eighteen historical DF entries have been inventoried; seven candidate business-process families, a BR-001–BR-020 register, nine proposed defect groups, atomic findings and high-risk pilot journeys have been documented. Several *bounded internal POC* decisions were recorded on 2 Nov, but formal Grab policy approval and a fully frozen acceptance baseline were not obtained. Historical REST/text trials produced useful but mixed evidence; recurrent 500/502 failures led to a **REST pause**. The latest operational output is a **9 Nov adaptive manual test package**, covering 15 TCs with 128 core checkpoints and 23 separate alternate branches; it explicitly records **zero new v0.3 executions**. On 12 Nov the user supplied the original Excel URL and a current Flow export ZIP. The handover goal is to enable the next LLM to pick up this work **without redoing completed design or assuming tests have passed**.

---

## 1. Scope, task boundaries and authority

**Project / product:** Malaysia merchant-facing voice AI Agent for cancelled GrabFood / GrabMart orders, their usual compensation timelines, status checks, supported request-submission guidance, navigation recovery, and handoff as allowed.

**Problem #2 question:** “How do we evaluate whether the Agent did the **correct business process** for the merchant, especially when the Agent legitimately takes a different path from Grab's sample dialogue?”

**In scope:** benchmark normalization; merchant goals and status-dependent routes; internal business-requirement catalog; conditional journeys/variants; source-and-decision governance; historical defect decomposition and impact mapping; acceptance and coverage scoring; manual test playbook; evidence and next-step continuity.

**Not automatically in scope:** editing Cognigy Flow/Agent/Knowledge, changing original stakeholder workbook or DF log, inventing Grab business policy, treating a simulated UI as an authenticated real UI, claiming backend compensation/payment/transfer execution, restarting failed REST batches without separate authorization.

**Other workstreams:** Problem #1 Knowledge Base v0.3 reached its documented **isolated POC** article-level retrieval/functional review closeout (not full formal policy or all real-world behavior certification). Problem #2 must use the appropriate KB provenance; it must not erase Problem #1's bounded conclusion or claim that Problem #1 proves all benchmark paths. Changes to Flow/Code/Tool contracts have Problem #3/#4/#5 change-control and regression dependencies; they are not a prerequisite for writing this handover.

### Authority hierarchy

1. Applicable, **actually approved** Grab/project business policy and verified official sources for the relevant claim, when provided.
2. Explicit project-side **internal POC** decisions, scoped and labeled; do not represent them as formal Grab approval.
3. Versioned Business Requirements (BR) and approved Journey/Variant acceptance fixtures with provenance and review status.
4. Original Grab workbook: **official benchmark/test and historical feedback**, not independent authority for every eligibility/payment/UI assertion embedded in an illustrative dialogue.
5. Historical Agent Job, Knowledge Store, previous tests and test harness: implementation/evidence, not independent policy authority.

The original official workbook and defect history are **read-only sources**. Proposed changes belong in separate internal normalized records and, if approved, in a separately versioned implementation change.

---

## 2. Exact input baselines and where to find them

### A. Original stakeholder benchmark (provided by the user)

- **Exact file title:** `Grab_UC4_Benchmark_Test_Scenarios_Feedback (3).xlsx`
- **Direct URL:** https://docs.google.com/spreadsheets/d/1-DMoct1N20xJA5QkgPDz_uMzwrkwLf3G/edit
- **Provider type:** Drive-hosted `.xlsx`, **not necessarily a native Google Sheet**. The Google Drive connector successfully identified this exact file on 12 Nov.
- **Recorded original XLSX SHA-256 in the prior source ledger:** `12e17ad51b6ee2053a4e2c56d3ae8b5ff56f544a6f9a1487dd274c05af5c797e`. Treat as a **recorded historical content fingerprint**; recompute from actual bytes if verification against a new download is needed.
- **Source structure:** `Scenarios` (15 official TC rows) and `Defect Log` (18 historical DF rows); source row/cell citations are documented in `BASELINE_MODEL(1).md`.
- **Scenario IDs:** TC-001–TC-010 and TC-025–TC-029.
- **Historical defect IDs:** DF-001–DF-018. Historical severity/status columns must be preserved, with any *new internal* triage separate.

### B. Most recently supplied Cognigy Flow snapshot

- **Exact uploaded name:** `Flow-UC4_KB_AGENT_POC_v03_2026-11-12_14-47-26.zip`
- **ZIP SHA-256, independently recomputed from this upload:** `fb47b07d9b1c77bb07a0f04bb48a8fd8a950bbfa7cdaa893b16c53e5f971c2e2`
- **Package metadata:** Cognigy `2026.23.0`; package `createdAt=2026-11-12T14:47:32.697Z`; `partial=false`; `skippedResources=[]`.
- **Flow:** `UC4_KB_AGENT_POC_v03`; stable Flow `referenceId=17f129de-69b3-4828-bc4f-0c7d19ef41ce`; package member `flow/6af5d1840cd638c60a6bc906`; package chart member `chart/6af5d1840cd638c60a6bc907`.
- **Resource inventory in this ZIP:** 1 Flow, 1 Chart, 31 `nodeData` members, one locale (`en-US`) and Flow metadata/settings. Within 31 nodes: 1 Agent Job, 6 Agent Tool nodes, 8 Code, 3 Say, 3 Resolve Tool Answer, 3 Hang Up and remaining start/once/other structure. The static chart has no identified dangling relations; this says nothing about runtime pass rates.
- **Agent Job name:** `Grab Cancelled Order Compensation`; stable Job `referenceId=e38e5029-d515-4002-ad03-dd99b0eb821e`; package member `nodeData/6af5d1840cd638c60a6bc91e`, configuration under `/localizedData/0/config/`.
- **Agent reference:** `3c1b0294-6016-4b52-8478-afd6cc05a434`; provider `default`, API version `latest`; neither is evidence of the effective deployed model.
- **Job instructions SHA-256 (UTF-8):** `d89731bb49f09959e0c9c35550cb0b9fa71fa03a88295916887672c20390d860` (~91,233 characters). **This matches the October 30 historical Job-instruction hash in the 5 Nov readiness ledger.** That match concerns this instruction text only; do not infer a complete package or live-Endpoint match.
- **Knowledge:** Job on-demand Knowledge search enabled, Job Knowledge Store reference `786b7a11-913c-4ec0-8a4e-e48352921d78` (historically `UC4_KB_POC_v03_TEST`), top-K `3`. **This Flow-only ZIP does not contain Knowledge Source/Chunk/Store contents or the AI Agent resource.** No live retrieval or KB freshness assertion follows from the reference alone.
- **Six local Tool IDs:** `resolve_order_age`, `start_guidance`, `update_guidance_checkpoint`, `end_call`, `transfer_to_live_agent`, `escalate_safety`.
- **Notable configuration facts:** `Set Session Config (EN)` node is disabled; voice settings may be supplied elsewhere. Stateful guidance/checkpoint validation exists; this is not by itself a finding that the Flow is wrong. End-call, mock-transfer and safety terminal branches are represented.
- **Explicit caveat:** Export does **not** prove the currently served Endpoint binding, Snapshot, enabled voice settings, provider/model resolution, real UI, actual Knowledge content, or successful behavior. No Flow change was made while preparing this handover.

### C. Historical configuration reference (not the new snapshot)

`UC4_P2_Execution_Readiness_2026-11-05.md` documents the earlier October 30 full package `Package-Naufal_2026-10-30_06-38-33.zip`, Cognigy `2026.22.2`, SHA-256 `e92afdf8d41c5a348e65e18e0a1cad77f827d26dab5c6d3fe136d3439c1a8a1f`, including Flow/Agent/Knowledge Store/17 sources/20 chunks. Do **not** mistakenly attribute those older Knowledge members to the **new 12 Nov Flow-only ZIP**. A current full export/Endpoint capture remains a separate task only if required for later live testing or change control.

---

## 3. Problem #2 methodology — decisions that must survive context transfer

1. **Business journey, not screenplay.** Grab evaluates whether the Agent gets the merchant through the appropriate process; line-by-line transcript reproduction is not the default oracle.
2. **Meaning over wording.** Semantically equivalent phrasing is acceptable unless a specifically sourced, applicable controlled sentence or UI label requires exactness. A historical “missing verbatim line” category alone does not establish a genuine failure.
3. **Dependency order matters.** A correct set of individual instructions can still be wrong if delivered before consent, before the relevant screen exists, or before the Agent observes the required status.
4. **Behavior and coverage are independent.** An Agent that correctly responds to `Auto approved` without redundant submission may be behaviorally correct but not cover the benchmark's **submit-request** target. Preserve both axes.
5. **Merchant observations are not implied facts.** Visible order ≠ status known; visible link ≠ article opened; article opened ≠ form visible; reported submission ≠ backend accepted; approval ≠ payout ≠ bank receipt.
6. **Alternative paths require provenance.** Classify material interpretations as `VERIFIED [POC]`, `PROPOSED`, `UNKNOWN` or `CONFLICT`. A proposed alternative does not silently become stakeholder-approved behavior.
7. **Traceability is many-to-many.** One BR can apply across different TCs/LOBs; one DF can contain several atomic findings; a change should select all related journeys and nearby variants for regression. A defect grouping does **not** prove a common technical root cause.
8. **No fabricated eligibility/transfer/payment.** Do not infer approval or eligibility from menu availability. A request or compensation claim is not proven just because a mock script says “Done.” Do not invent transfer rules or payout dates.
9. **Preserve original historical records.** Never overwrite prior REST findings, Grab's original DF statuses, or verdicts because a newer manual target was defined.

### Identifiers and modeling layers

| ID family | Meaning | Current status / caution |
|---|---|---|
| `BP-01`…`BP-07` | Shared business-process families | Seven candidate families; useful for grouping, not blanket PASS labels |
| `BR-001`…`BR-020` | Requirements, dependencies and evidence/acceptance rules | Twenty drafted BR IDs; substantive acceptance varies by decision and scope |
| `JRN-TC-###` | Per-TC business journey, milestones, preconditions and target | Three original high-risk detailed pilots; broader catalog/fixture overlays exist |
| `VAR-TC-###-X` | Material conditional alternative | Proposed/selected variants; keep meanings and parent TC stable |
| `TC-###` | Grab's official benchmark case | 15 immutable original TC identifiers |
| `DF-###` | Grab's historical defect/feedback record | 18 original external records; do not silently edit or reopen |
| `DF-###/F##` | Atomic finding from a compound DF | 49 extracted atomic records in engineering review; not 49 proven bugs |
| `DG-###` | Proposed defect-behavior group | Nine candidate groups; not nine confirmed shared causes |
| `OD-###` | Internal open-decision/review item | 15 enumerated decision slots; overlays supersede older pending labels |
| `RUN` | Specific immutable observed session/run evidence | Requires date, exact baseline, channel, transcript, scope and verdicts |

**Requirement categories:** `BR-001`–`BR-016` and `BR-018`–`BR-019` are primarily Agent behavior; `BR-017` governs QA voice/display evidence; `BR-020` governs semantic acceptance methodology. Do not turn BR-017/020 directly into script lines the Agent must say.

### Seven business-process families

| ID | Primary cases | Principal outcome |
|---|---|---|
| BP-01: Recent compensation education | TC-001, TC-025 | Correct LOB timing/evidence reminder; suitable closing |
| BP-02: Follow-up / declined guidance | TC-002, TC-026 | Address hypothetical nonreceipt; offer guidance, respect decline |
| BP-03: Older-order inquiry / education | TC-004, TC-028 | Clarify actual goal; educate as applicable; don't force walkthrough |
| BP-04: Status → conditional submission | TC-003, TC-005, TC-027, TC-029 | Observe status first; choose review/submission only if still needed |
| BP-05: Request form / authorization access | TC-006, TC-009 | Link/article/form/Owner–Manager role; retry and consent boundaries |
| BP-06: Navigation recovery / fallback | TC-007, TC-008 | Stuck step repeat, History, missing App link → Portal support |
| BP-07: Consent / appropriate handoff | TC-010 | Out-of-scope response and separately consented mock handoff |

Secondary cross-family links must be preserved: e.g. TC-009 also exercises handoff, TC-003/027 also exercise submission access, and TC-007 can continue into submission.

---

## 4. Business decisions — which are actually agreed, and what remains open

### Recorded **internal POC** directions (not formal Grab approval)

- **OD-001 / TC-006:** The *declined-retry* route is the proposed main target; the sample dialogue's *accepted and successful retry* remains a separately testable alternative. The original `Expected flow path` and sample transcript **conflict**, so do not erase either.
- **OD-003 / TC-027:** A GrabMart merchant selecting App for a status journey must receive an **explicit computer-Portal status redirect** with readiness/acceptance and preserved preferences before Finance → Transactions. The benchmark's App-then-Portal jump is not a justified invisible transition.
- **OD-008 / TC-009:** Treat the target as **Portal submission-only**, then appropriate role/access recovery, failed agreed retry, a **separate** person offer, **explicit consent**, mock transfer and Flow terminal handling. A retry agreement is not transfer consent; the benchmark path text is not entirely consistent.
- **OD-015:** A staged internal POC review approach was agreed, without assigning formal Grab/business/QA approval authority.
- **OD-002 Q1–Q4 (2 Nov user-approved POC overlay):** (Q1) On **visible blank** status, conditional review-request guidance is allowed **without** an eligibility/award promise; (Q2) on a reported `Auto approved` state, explain it and avoid redundant submission when the merchant's remaining goal is status-only; (Q3) distinguish **approval**, **payout** and **bank receipt**, clarify what remains unresolved; (Q4) **clarify uncertain status before** any status-dependent submission decision. This is `ENGINEERING_AGREED_POC / VERIFIED [POC]` only; payment remedies, broader triggers and formal policy remain subject to further review.

### Unresolved/high-impact decision frontier

- **OD-004 / OD-005:** Applicable education vs direct intent, goal/intake trigger ordering, threshold/reference-date conventions and timing/evidence statements. Review with later overlays; avoid an age-based forced walkthrough.
- **OD-006:** GrabMart partial-compensation wording and its approval/exactness.
- **OD-007:** Navigation recovery, History/date-selector behavior, one-retry boundaries, unknown next steps after repeat failure.
- **OD-009 / OD-010:** Closing and handoff consent, unknown roles, authorized retry, unresolved form access and recovery terminal.
- **OD-011:** A sourced, trigger-scoped controlled-language inventory (not verbatim matching of every sample line).
- **OD-012 / OD-013:** Historical DF closure and independent voice/ASR/latency evidence.
- **OD-014:** Real policy and UI source authority, payout/status remedies, bank-receipt rules and remaining unsupported outcomes.
- **OD-015:** Named owner/reviewer/governance and formal sign-off. A provisional owner self-review is not independent QA or Grab sign-off.

**Current policy conflict `P2-AGENT-001`:** The original TC-002 benchmark and both an earlier/historical Agent Job and the 12 Nov Job instructions link eligibility to visibility of a Request for Compensation control, while the scoped internal acceptance excludes treating control visibility as eligibility proof. This is a **source/criterion conflict**, not independently proven false Grab policy, and is **not a reason to stop or rewrite the handover**. Record it, don't silently “fix” either document or the ZIP. Its source/approval reconciliation remains open.

---

## 5. Test strategy and latest manual package (9 November)

### The operational package

1. `UC4_Adaptive_Manual_Playbook_v0.3.md` — full tester instructions and official case-by-case conditional response bank.
2. `UC4_Adaptive_Manual_Testing_v0.3.xlsx` — **10 tabs**: `READ FIRST`, `CASE CARDS`, `IF THEN ROUTES`, `ALTERNATE BRANCHES`, `CHECKPOINT LOG`, `NEW MANUAL RUNS`, `PAST REST RUNS`, `PAST TRANSCRIPTS`, `FINDINGS`, `SPEC WARNINGS`.
3. `UC4_Adaptive_Manual_Testing_v0.3_Package.zip` — archival package containing the manual testing deliverable.

**Crucial numbers:** 15 official cases, **128 core checkpoints** and **23 separate alternate branches** in v0.3; **0 new v0.3 manual attempts** at release. A different, older 5 Nov execution-readiness catalog lists **23 selected assessment fixtures** (15 official + 8 selected variants) and **21-fixture smoke subset**. These counts mean **different things**. Do not conflate 23 manual alternatives with 23 approved runner fixtures.

### The selected primary target per official TC

| Case | LOB | Primary target | Core checkpoints | Separate alternatives |
|---|---|---|---:|---:|
| TC-001 | GrabFood | Recent order; timeline/evidence → finish | 2 | 1 |
| TC-002 | GrabFood | Hypothetical nonreceipt → offer → decline → finish | 4 | 1 |
| TC-003 | GrabFood | Upfront dual goal → App status → conditional request | 13 | 3 |
| TC-004 | GrabFood | Older age-only → clarify missing goal → educate/decline | 4 | 1 |
| TC-005 | GrabFood | Elicited dual goal → grouped App status → request | 10 | 2 |
| TC-006 | GrabFood | Missing form; authorized Owner; decline offered retry | 12 | 3 |
| TC-007 | GrabFood | Missing order; Date selector stuck; repeat once | 17 | 1 |
| TC-008 | GrabFood | Missing App request link → accept Portal fallback | 14 | 1 |
| TC-009 | GrabFood | Portal submit-only; failed retry; explicit mock-transfer consent | 12 | 2 |
| TC-010 | GrabFood-labeled | Out-of-scope concern; separate person offer/consent | 2 | 1 |
| TC-025 | GrabMart | Recent order education → finish | 2 | 1 |
| TC-026 | GrabMart | Hypothetical nonreceipt → decline guidance | 4 | 1 |
| TC-027 | GrabMart | App preference → explicit computer Portal redirect; one-by-one status → request | 17 | 2 |
| TC-028 | GrabMart | Older age-only → elicited inquiry → educate/optional offer | 4 | 1 |
| TC-029 | GrabMart | Elicited dual goal → grouped Portal status → grouped request | 11 | 2 |
| **Total** | | | **128** | **23** |

### How to execute (mandatory protocol)

1. Pick **one** TC and selected target, **start a fresh Agent conversation** and record channel, timestamp (include Asia/Kuala_Lumpur/MYT if used), exact configuration ID/hash where available, testcase/fixture version and tester.
2. Send **only the initial `START/O1` merchant utterance**. **Do not pre-supply** held preferences (platform, pacing, loudspeaker, role) when the fixture exists to test whether the Agent elicits them.
3. Wait for the **actual Agent trigger** and choose the corresponding `IF THEN ROUTES` response. The checkpoint IDs are **not fixed turns**. Adapt to valid orderings; never read the next row just because the previous row number ended.
4. Report real UI screen states **only if actually observed** in an authenticated UI. Otherwise mark synthetic role-play `DECLARED SIMULATION`. Never claim submitted/approved/paid/connected because the tester needs the script to progress.
5. At each step record Agent input/output and evidence in `CHECKPOINT LOG`; use `NEW MANUAL RUNS` for the summary. If a mandatory checkpoint is missing, record `NOT OBSERVED` / `FAIL` / `NEEDS REVIEW`; do not fabricate intermediate success.
6. Separate **behavior verdict** (`PASS`, `FAIL`, `INCONCLUSIVE`, `BLOCKED_SPEC`, `BLOCKED_ENV`) and **target coverage** (`COMPLETE`, `PARTIAL`, `NOT COVERED`, `ALTERNATE`, `NOT OBSERVABLE`). Do not turn a good alternative response into full original-path coverage.
7. An alternative outcome needs a **separate fresh session**, its own VAR/ALT identity and run record. No mixing mutually exclusive target and alternate scenarios.
8. Text closes cannot prove actual Flow Hang Up, successful real transfer, TTS audibility, or ASR transcription fidelity. Capture voice and terminal evidence separately, or use the appropriate not-observable/blocked verdict.
9. Never ask testers for passwords, bank records or real merchant private details. Role/authorization inputs may be explicitly declared synthetic fixtures.

### Example of the coverage distinction

TC-003 has a selected target where the status is **blank** and the merchant still wants conditional submission. If the merchant instead reports **Auto approved**, the Agent may be correct to explain approval and not make a duplicate request; score the observed behavior separately and mark the **original submission-target coverage incomplete**, then run the target fixture anew if still required.

---

## 6. Historical execution evidence — do not transpose to new v0.3 runs

**7 Nov report:** prior REST/text testing exists but is incomplete and affected by Endpoint/runner reliability. Its case-level summary is:

| Original TC | Historical evidence status | Interpretation / caveat |
|---|---|---|
| TC-001 | PASS in REST/text evidence | Recent-order education and closing text observed; real terminal/audio not verified |
| TC-002 | FAIL against scoped internal POC criterion | Two complete follow-up runs linked eligibility with request-control visibility; source/criterion conflict remains |
| TC-003 | Observed FAIL in a run / incomplete across attempted runs | One late identity/recording disclosure; separate matcher/progression truncation in others |
| TC-004 | FAIL in one of two runs | Missing/late opening or goal/consent sequencing; other run was positive control |
| TC-005 | NEEDS REVIEW | Two partial runs stopped at article-route matcher; not proof of Agent navigation failure |
| Other 10 TCs | Not executed in this 7 Nov official benchmark evaluation | Do not mark PASS/FAIL based on historical DF labels or the new manual case definition |

Named findings: **P2-AGENT-001** (TC-002 rule/source conflict), **P2-AGENT-002** (opening/disclosure timing, TC-003/004), **P2-AGENT-003** (goal and guidance-consent ordering, TC-004), and **P2-HARNESS-001/002** (TC-003/005 regex/progression false negatives; not confirmed Agent defects). Later workbook also tracks environment/technical issues separately. A 9 Nov workbook retained historical REST artifacts/transcripts in `PAST REST RUNS` and `PAST TRANSCRIPTS`; those do **not** become fresh v0.3 execution evidence.

**Automation pause:** Recurrent **HTTP 500/502** made REST Endpoint testing unreliable. The 7 Nov eight-slot attempt stopped at the first technical failure; the other seven slots were **not** run. Do not interpret HTTP failures as business-rule failures, retry quietly, or run the deferred slots under the old authorization. To restore automation, first establish Endpoint/Flow/Agent/Knowledge/LLM bindings, investigate transport/provider failures, verify the runner/fixture baseline, then request **fresh explicit authorization for each named batch/smoke run**. The former fixed-turn runner cannot fully express adaptive conditional conversations or native-empty entry without approved redesign; manual testing is the current recommended channel.

**5 Nov readiness record:** `UC4_P2_Execution_Readiness_2026-11-05.md` said **NO-GO** for executable automation: scope was provisionally selected, but current deployment configuration unverified and **0/23** selected fixtures had a complete reviewed executable binding. This predates the manual v0.3 design and the 12 Nov static Flow export; it has **not** been superseded by a successful live evaluation.

---

## 7. Known specification conflicts and evidence gaps — keep these OPEN, not “fixed”

### A. Benchmark contradictions / source qualification

- **TC-006:** “Expected flow path” says retry **declined** but sample merchant agrees to re-login and succeeds. Main target chosen internally; successful retry remains VAR. Official benchmark owner has not adjudicated the contradiction.
- **TC-027:** Merchant initially says App, sample jumps into Finance/Transactions computer-Portal status. POC interpretation requires explicit App → Portal explanation and readiness; verify actual UI/role state in later tests.
- **TC-003 / DF-017:** Reported `Auto approved` adaptation does not necessarily satisfy the selected submission test; status/approval/payout/bank distinctions matter. Original feedback is evidence, not standalone policy authority.
- **TC-002 / P2-AGENT-001:** Eligibility/visible request control wording conflict between original sample/historical Job and internal scoped criterion. Mark source conflict, not known false policy, and do not modify the ZIP or benchmark merely to make documents agree.
- **Exact-wording disputes:** Some historical DFs use “Missing or changed verbatim line”; review actual merchant outcome and any source-approved mandatory sentence rather than failing harmless paraphrases.

### B. Runtime/environment boundaries

- The current **12 Nov Flow-only export** cannot prove live Endpoint binding or complete AI Agent/Knowledge Store resources. Record exact Endpoint target, locale, Snapshot/revision, overrides, effective LLM provider/model, shared dependencies and current Knowledge content **when authorized and needed**.
- Disabled Flow session-voice node does not prove that voice is globally disabled; external settings may own TTS/ASR.
- A chart/static ZIP check cannot prove actual tool-call ordering, speaker interruptions, run reliability, real App/Portal UI, payment logic, Owner/Manager authorization, mock transfer event, or Flow hang-up.
- Do not turn a speculative transfer-condition weakness into a confirmed merchant-facing failure without an applicable trace.
- Internal approval labels must never be promoted to “Grab policy approved.” No formal Grab sign-off is recorded in the reviewed sources.

---

## 8. What to do next — ordered continuation plan, **not** a request to do everything now

### Immediate: preserve/locate authoritative sources

1. Keep source benchmark and 12 Nov ZIP unmodified. Record fingerprints and the documented Knowledge/Flow/Job scope. Do not create replacement files over originals.
2. On another LLM/chat, retrieve the exact named Library documents in §9 and the Google Drive workbook. **Do not ask the user to re-upload all files by default.** If a specific file is inaccessible, identify it explicitly.
3. Before any actual new execution, check for test runs or changes **after 9 Nov** and record them as newer evidence only if provided; the 12 Nov ZIP alone is not a run.

### Next active Problem #2 workstream: manual evidence collection

4. Use **adaptive v0.3** (not the superseded fixed-turn v0.2) to execute fresh, explicitly chosen primary targets and separate alternatives in a functioning Cognigy test channel. Record exact system baseline, actual Agent replies, observed branch, process verdict and coverage verdict.
5. Reasonable risk-first candidates are **TC-002** (policy-source conflict), **TC-003/004** (opening/intake/branch decisions), **TC-006/007/008/009** (role, retry, recovery and consent), **TC-010** (out-of-scope consent), and **TC-027/029** (GrabMart Portal step boundaries). This is a **proposed prioritization**, not authorization or a new official test selection.
6. For each failure, verify requirement applicability and evidence. Create/link a *new internal finding* without erasing historical DF. Group regression impact by BR and BP as appropriate; diagnose Flow/Agent/Knowledge/tool/endpoint only if a defect is reproducible and a fix is actually requested.

### Decision and acceptance governance

7. Track `OD-004/005` plus unresolved role/status/voice/controlled-language policy issues. Record owner, evidence, approved POC scope and future review date; keep formal Grab sign-off distinct.
8. When sufficient source and reviewer authority exist, version/freeze the relevant **accepted** BR/JRN/VAR fixtures. Do not claim a frozen acceptance baseline retroactively.
9. If automation becomes viable again, separately authorize a safe technical smoke only after 500/502 root-cause and live configuration checks, and **do not automatically resume** all deferred runs.
10. If a Flow patch is requested later, work from an authenticated current baseline, hash input, minimal diff, no overwrite, explicit constraints, deterministic validation and focused + neighboring regression. That is a **new task**; this handover does not authorize a patch.

### Minimal run/evidence record (conceptual, not runner schema)

```yaml
run_id: "<fresh-unique-id>"
run_timestamp_myt: "<YYYY-MM-DDTHH:MM:SS+08:00>"
tester: "<person-or-test-role>"
channel: "<Cognigy UI / voice / approved REST>"
configuration:
  flow_name: UC4_KB_AGENT_POC_v03
  flow_export_sha256: "<recorded-if-relevant>"
  endpoint_binding: "VERIFIED | UNVERIFIED"
  agent_job_revision: "<if-known>"
  knowledge_revision: "<if-known>"
  effective_model: "<if-known>"
benchmark_source: "Grab_UC4_Benchmark_Test_Scenarios_Feedback (3).xlsx"
manual_pack: "UC4_Adaptive_Manual_Testing_v0.3"
tc_id: "TC-003"
variant_id: null
selected_target: "<selected-primary-goal>"
observed_branch: "<actual-outcome>"
evidence_mode: "DECLARED SIMULATION | VERIFIED REAL UI"
checkpoint_ids_observed: []
checkpoint_ids_missing: []
source_transcript_or_recording: "<link-or-reference>"
behavior_verdict: "PASS | FAIL | INCONCLUSIVE | BLOCKED_SPEC | BLOCKED_ENV"
target_coverage: "COMPLETE | PARTIAL | NOT COVERED | ALTERNATE | NOT OBSERVABLE"
reviewer: "<if-different>"
notes: "Do not infer server-side submission, payment, actual transfer or Hang Up from text."
```

---

## 9. Source index — specific names, purposes and reading order

The following were found in **ChatGPT Library** during prior source retrieval; for a new chat, search by **exact title**. File titles and timestamps help distinguish older and newer overlays. The original workbook is in Google Drive; the 12 Nov ZIP is an attachment to this conversation and may need to be carried or uploaded to a new one if the next LLM cannot access it.

### Essential Problem #2 continuity files

1. **`UC4_Adaptive_Manual_Playbook_v0.3.md` (9 Nov)** — latest condition-triggered per-TC manual scripts, assumptions, 128 checkpoints/23 alternatives, no new executions.
2. **`UC4_Adaptive_Manual_Testing_v0.3.xlsx` (9 Nov)** — active operational workbook with the 10 named tabs, separate history/new runs and test warnings.
3. **`UC4_Adaptive_Manual_Testing_v0.3_Package.zip`** — optional bundled transfer of the 9 Nov manual deliverables.
4. **`UC4_Problem2_Current_Progress_and_REST_ExitPlan_2026-11-07.docx`** — historical 7 Nov case status, defect findings, failed Endpoint and manual transition.
5. **`UC4_Manual_Testing_and_Progress_ExitPlan_2026-11-07.xlsx`** — earlier 5-tab manual workbook; historical/operational predecessor, **not** the latest v0.3 runner.
6. **`UC4_P2_Execution_Readiness_2026-11-05.md`** — 23 selected assessment fixtures/21 smoke subset, 0/23 reviewed executable bindings, historical configuration ledger and no-go decision.
7. **`UC4_Problem2_Business_Journeys_Human_Review_Report_2026-11-02.docx`** — human-facing process families, pilots, four core POC directions, sign-off gaps.
8. **`README(4).md`** — engineering review package v0.3 **plus OD-002 Q1–Q4 acceptance overlay**, version history and formal-policy boundaries.
9. **`BASELINE_MODEL(1).md`** — candidate BR-001–BR-020, source/cell provenance, 49 atomic findings, type distinctions, decision authority.
10. **`OPEN_DECISIONS.md`** — OD-001–OD-015 decision registry; **some front matter is older than later approval overlays**, so read with README and OD-002 record.
11. **`UC4_Problem2_Benchmark_Journey_Implementation_Playbook_2026-10-23.md`** — original LLM/developer methodology and explicitly agreed process direction.
12. **`UC4_Problem2_Benchmark_Journey_Decision_and_Action_Plan_2026-10-23.docx`** — initial rationale and decision/action package.
13. **`Grab_UC4_Benchmark_Test_Scenarios_Feedback (3).xlsx`** — immutable official benchmark; direct Drive URL in §2.
14. **`Flow-UC4_KB_AGENT_POC_v03_2026-11-12_14-47-26.zip`** — current user-supplied **Flow-only static snapshot**, SHA and limits above.

### Specialist source files (if available inside the engineering review package)

- `TC_CLASSIFICATION_MATRIX.md` — all TC-to-BP/BR relations and candidate process-family assignments.
- `JOURNEY_PILOT.md` — TC-003/006/027 high-risk journey milestones and variants.
- `DEFECT_GROUP_IMPACT_MATRIX.md` — historical DF-001–018 decomposition and proposed DG groups.
- `OD002_STATUS_DECISION_REVIEW.md` — Q1–Q4 internal POC user approval and source limits.
- `OD004_OD005_TRIGGER_TIMING_REVIEW.md`, `OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md`, `OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md` — targeted decision/contract evaluations if those matters are reopened.
- `REVIEW_DECISION_WORKSHEET.md` — scoped review/fixture decision work and approval qualifications.
- `P2-AGENT-001.md` — the qualified TC-002 source/acceptance conflict. Preserve it instead of flattening it to a generic “Flow broken” claim.
- Problem #1 `UC4_Problem1_KB_v03_LLM_Handover_2026-10-30.md` and `UC4_KB_v03_Retrieval_Validation_Closeout_2026-10-30.md` — isolated KB POC scope/background, if policy article provenance becomes necessary.

**Source caveat:** Some specialist files are inside historical archived packages or Library and were not individually re-opened during this handover. The recorded references identify where to continue; they do not claim that the newer Flow ZIP embeds them.

---

## 10. What the next LLM must NOT infer or do

- **Do not say the user asked for a new Flow audit or repair.** The user's present goal is an **LLM continuation handover**. A prior optional static ZIP audit is separate contextual evidence.
- Do not claim the ZIP is wrong merely because an internal acceptance rule differs from an illustrative original benchmark sentence; preserve the difference as a documented source conflict.
- Do not claim that receiving the 12 Nov ZIP means the live Endpoint, Knowledge Store, effective model and voice settings were verified.
- Do not claim that v0.3 manual tests were performed or passed. **They were designed, not executed**, as of the available evidence.
- Do not collapse original TC target completeness and alternate branch correctness into a single verdict.
- Do not map every historical DF to an active reproducible Agent bug or overwrite its recorded Grab status.
- Do not conflate **23 manual v0.3 alternative branches** with **23 earlier selected assessment fixtures**.
- Do not demand exact benchmark wording except where a supported scoped controlled sentence actually applies.
- Do not force an App/Portal handoff, a request form, a retry, a transfer or payout remedy when source and consent are missing.
- Do not run REST batches, edit Cognigy, alter a user file or initiate external actions without a new explicit scoped request and proper authorization.
- Do not re-ask for materials already supplied and accessible; search by exact names first.

---

## 11. Ready-to-paste continuation prompt

> You are continuing our existing **UC4 Malaysia GrabFood/GrabMart cancelled-order compensation — Problem #2** project. Read the attached `UC4_Problem2_LLM_Continuation_Handover_2026-11-12.md` **fully**, then retrieve/read its exact named sources, prioritizing the 9 Nov **Adaptive Manual Playbook v0.3**, 9 Nov testing workbook, 7 Nov REST exit report, 2 Nov business-journey review/OD-002 overlay and the original Grab benchmark. A 12 Nov Cognigy Flow-only ZIP is our latest supplied static snapshot; **do not assume live deployment bindings or Knowledge Store contents are verified**. Our approach is **business-process/semantic acceptance, not line-by-line scripted matching**, with independent **behavior** and **target coverage** verdicts. Preserve all decisions, source conflicts, historical test evidence and open approvals. The latest v0.3 manual pack has **15 TCs, 128 core checkpoints, 23 alternate branches, and zero new v0.3 executions**. REST automation remains paused due to 500/502. **Do not restart design, silently fix the Flow, overwrite Grab's Excel or claim formal Grab approval.** First summarize current state briefly, then continue the specific next task I give you from this checkpoint.

---

## 12. Final handover status

**Ready to transfer:** project objective, agreed methodology, original benchmark locator, current static Flow export identity/hash, business-process model, bounded POC decisions, exact continuity documents, prior REST results, adaptive manual test protocol and execution frontier.

**Not yet achieved:** 15 new v0.3 manual executions; verified live Endpoint/Agent/Knowledge/model/voice deployment baseline; independently signed/frozen acceptance for every BR/JRN/variant; formal Grab policy sign-off; real merchant App/Portal/backend payment validation; a proven fully passing benchmark; resolution of all source conflicts.

**Precise continuation point:** **Use the 9 Nov adaptive manual package to collect real fresh evidence against the versioned Problem #2 process requirements (or perform another explicitly requested scoped task), while preserving the 12 Nov Flow ZIP as the newest supplied export snapshot.**

**Preparation integrity:** This handover has not modified the original Google Drive workbook, the user's attached Flow ZIP, Cognigy resources, REST runner, or historical evidence.
