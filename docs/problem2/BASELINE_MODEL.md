# Problem #2 — acceptance and baseline model

**Current candidate:** `P2-BASELINE-CANDIDATE-0.1` · **2026-11-04** · **REVIEW CANDIDATE / NOT FROZEN**.
Includes the complete `P2-JOURNEYS-0.4` catalog, scoped BR/VAR manifest and
`P2-CONTROLLED-TEXT-0.1` applicability register [below](#phase-4-scoped-acceptance-baseline-review-candidate).
This adds a reviewable acceptance scope to the preserved source model; it supplies
no new policy approval. Both current verdicts are `NOT_RUN`.

**Version:** `P2-DRAFT-0.2` with `P2-ENG-DECISIONS-0.3` / `OD002-REVIEW-0.2` / `OD004-OD005-REVIEW-0.2` / `OD004-RECENT-GUIDANCE-REVIEW-0.2` / `OD007-OD010-OD009-REVIEW-0.2` overlays · **2026-11-04** · **State:** bounded internal engineering agreements, remaining acceptance PROPOSED; baseline NOT FROZEN.

**No executed baseline:** OD-001/003/008/015 now have bounded project-side POC agreement, documented in [ENGINEERING_DECISIONS_2026-11-02.md](ENGINEERING_DECISIONS_2026-11-02.md). This does not approve all BRs/variants, appoint reviewers, resolve formal benchmark conflicts, or authorize tests.

**Round 2 agreement:** [OD-002 Q1–Q4](OD002_STATUS_DECISION_REVIEW.md#recorded-q1q4-approval-and-provenance)
are **VERIFIED [POC] / ENGINEERING_AGREED_POC** following the requesting project-side
user's 2026-11-02 approval. They distinguish observed blank status, reported
approval, unpaid funds and unclear status for the scoped GF fixture/alternatives.
Formal status/duplicate policy, payment remedies and dependent requirements remain
open. See [version history](README.md#version-history-and-preservation) for the
preserved source packs and exact pre-approval nine-document snapshot.

**Round 3 agreement (2026-11-03):** the requesting project-side user's
[qualified OD-004/005 Q1–Q7 approval](OD004_OD005_TRIGGER_TIMING_REVIEW.md#recorded-q1q7-approval-and-provenance)
is **VERIFIED [POC] / ENGINEERING_AGREED_POC** for scoped drafting choices only.
The applicability overlay below governs those subsets of the retained BR rows;
complete BR acceptance, formal policy/UI, Tool-contract and timing conflicts
remain open. OD-002's GF status/coverage agreement is preserved.

**Qualified Q8 agreement (2026-11-03):** [Option B and seven qualifications](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#recorded-q8-approval-and-provenance)
are **VERIFIED [POC] / ENGINEERING_AGREED_POC** for documentation/design direction.
Coordinated existing-path adjustment, compatible-progress retention/selective
invalidation and actual-output-based education accounting are agreed under the
**Agent-first/minimal existing-instruction-and-contract boundary**. No new
controller protocol, unnecessary persistent walkthrough state or additional Flow
infrastructure is authorized. Q1–Q7 and the GM-only exception remain intact; exact
implementation and dependent fixture/BR acceptance remain open.

**Qualified Q9–Q13 agreement (2026-11-04):** [full approval and provenance](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#recorded-q9q13-approval-and-provenance)
record **YES** to Q9/Q10/Q11/Q13 and **YES, PROVISIONALLY** to Q12, **VERIFIED [POC] /
ENGINEERING_AGREED_POC** for internal specification/test-fixture design. The scoped
overlay below governs current applicability while original BR/source rows remain
preserved. Q1–Q8 retain their authority and qualifications; no formal Grab approval,
whole-variant certification or execution evidence is supplied.

[Classification](TC_CLASSIFICATION_MATRIX.md) · [Pilots](JOURNEY_PILOT.md) ·
[Defect impact](DEFECT_GROUP_IMPACT_MATRIX.md) · [Decisions](OPEN_DECISIONS.md)

This is a documentation model, not a runner schema change or an executed Agent
baseline. All 15 official TCs and proposed variants are **NOT_RUN in this work**.
Existing KB tests remain separate evidence with their original identifiers.

## Sources and authority

Locators below are the citation keys used throughout this review pack.
`WB:S!D9` means the workbook's **Scenarios** sheet, cell D9;
`WB:D!G12` means **Defect Log**, cell G12. A range includes both endpoints.
`PLAN §6/P101` identifies the DOCX section and the 101st `word/document.xml`
paragraph, counting paragraphs inside tables. `PB §4` identifies a Markdown section.

| Key | Original source and precise location | Authority / limits |
|---|---|---|
| PLAN | [Original decision bundle](../../reference/UC4_Problem2_Original_Decision_Documents_2026-10-23.zip), member `UC4_Problem2_Benchmark_Journey_Decision_and_Action_Plan_2026-10-23.docx` | October 23 agreed process direction; individual conversions/approvals remain outstanding. §§3–9 and §§10–13 govern this draft. |
| PB | Same bundle, member `UC4_Problem2_Benchmark_Journey_Implementation_Playbook_2026-10-23.md` | v1.0; existing BR/JRN/VAR definitions, approval labels, templates and pilot proposals. |
| WB | `C:\Users\Nau\Downloads\UC4_Knowledge_Implementation_2026-10-24.zip` → `UC4_Knowledge_Implementation/Provenance/Originals/03_Business_and_Test_Context/Grab_UC4_Benchmark_Test_Scenarios_Feedback (3).xlsx` | Immutable official test reference, not independent policy authority. Scenarios rows 4–18; Defect Log rows 5–22. IDs include original cached formula results; no recalculation. |
| H1 | `C:\Users\Nau\Downloads\UC4_Problem1_KB_v03_LLM_Handover_2026-10-30.md` | §§0, 4–6: closed isolated-POC scope, 17 article-level retrieval checks; 15 functional scenarios, one completed manually. §§3, 8: authority and next workstream. |
| KBC | `C:\Users\Nau\Downloads\UC4_KB_v03_Retrieval_Validation_Closeout_2026-10-30.md` | “Executive conclusion,” “Article-level evidence ledger,” “Remaining limits and sign-off conditions”: article-level smoke coverage, not all chunks, UI validation or formal Grab approval. |
| KB | [October 29 export](../../flow/Package-Naufal_2026-10-29_06-47-07.zip), `knowledgeSource/*` metadata and joined `knowledgeChunk/*` text | All 17 v0.3.0 articles / 20 chunks read. Cite logical article/chunk/claim IDs below. All have `adoption=provisional_poc`, `formal_approval=pending`; H1 §2 reports KB content unchanged in its October 30 audit. |
| KC | [KB coverage and decisions](../KB_TEST_COVERAGE.md), “Source inventory and authority,” “Suite design and POC decisions,” “Known coverage limits” | Supporting article inventory and POC constraints. Its earlier execution narrative is historical; H1 supplies the later closure scope. |
| POC | [Approved October 29 POC policy](../../flow/UC4-PORTAL-DIAGNOSIS-2026-10-29.md#approved-poc-policy) | Explicit GrabMart status-only navigation bypasses age/loudspeaker intake in voice and text; excludes combined status/submission, eligibility and timing. Internal POC decision, not Grab policy approval. |
| JOB29 | [Approved October 29 Job text](../../flow/poc-correction-2026-10-29/01-job-instructions.txt), cited by heading | Historical controlled-language/procedural reference. H1 §§2, 5 reports later application of three scoped additions. It is not proof of the currently served configuration. |
| P2V03 | [Engineering Review Pack v0.3](../../reference/UC4_Problem2_Engineering_Review_Pack_v0.3.zip); eight root Markdown members | Actual Round 2 input, `P2-DRAFT-0.2` plus `P2-ENG-DECISIONS-0.3` overlay. Engineering record governs four internal choices; classifications/other acceptance remain proposed. |
| JOB30 / KB30 | `C:\Users\Nau\Downloads\Package-Naufal_2026-10-30_06-38-33.zip`; Job `nodeData/6ae43b6f90878ce305636d97`, `/localizedData/0/config/instructions`; KB `knowledgeSource/*`, `knowledgeChunk/*` | Matches H1's last verified static export. Round 2 comparison: 17 article metadata / 20 chunk text/claim records match KB29; 39/42 Job sections match after whitespace normalization, three contain H1's approved additions. Historical POC scope; no present Endpoint binding or authenticated UI proof. |
| OD2 | [OD002-REVIEW-0.2 approval record](OD002_STATUS_DECISION_REVIEW.md#recorded-q1q4-approval-and-provenance); user's explicit Q1–Q4 approval message, 2026-11-02 | Requesting project-side user agrees to provisional internal POC decisions; personal name/official role and formal Grab or QA authority not supplied. Supersedes v0.1's pending internal choices only, preserving factual source limits and formal-policy unknowns. |
| STATIC30 | Same authenticated October 30 export: age Tool/Code/Resolve, initializer, Initialize Once/On First Time nodes, first-input LOB capture and chart wiring. Exact members and hashes in the [OD-004/005 static-source ledger](OD004_OD005_TRIGGER_TIMING_REVIEW.md#static-tool-code-and-wiring-ledger). | Read-only definitions establish a stored UTC+8 initialization date, integer cancellation-age classification and a beyond-only standard guidance gate. They do not establish runtime behavior, official operating-date policy, absolute-date normalization or current Endpoint binding. |
| OD45 | [OD004-OD005-REVIEW-0.2 approval/provenance](OD004_OD005_TRIGGER_TIMING_REVIEW.md#recorded-q1q7-approval-and-provenance); requesting user's explicit qualified Q1–Q7 message, 2026-11-03 | Provisional internal POC engineering agreements only. Q2/Q7 conditional; Q4 modified to genuinely ambiguous assistance only; Q6 declares Asia/Kuala_Lumpur (UTC+8) test reference. Formal authority not supplied; no runtime authorization, official calendar, early-form acceptance or guaranteed evidence completeness. |
| Q8 | [OD004-RECENT-GUIDANCE-REVIEW-0.2 approval/provenance](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#recorded-q8-approval-and-provenance); requesting user's explicit seven-qualified Option B approval, 2026-11-03 | Provisional internal POC documentation/design direction only. Agent-first/minimal adjustment governs prior representation/API suggestions. Personal name/official role/formal business or QA authority not supplied; no implementation, policy/UI override, early eligibility, guaranteed compensation, unsupported submission or freeze authorized. |
| Q9–Q13 | [OD007-OD010-OD009-REVIEW-0.2 approval/provenance](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#recorded-q9q13-approval-and-provenance); requesting project-side user's qualified approval, 2026-11-04 | Provisional internal POC specification/test-fixture criteria only; Q12 explicitly provisional and benchmark fixture changes require reviewer approval. Personal name/official role/formal business or QA authority not supplied. TC-010 menu-update fixture remains proposed; unsupported outcomes and formal-policy limits remain. |

### Fingerprints

| Artifact | SHA-256 |
|---|---|
| Decision bundle | `5fc1ac6e177af2706fa6deb694fa11bb892a7bbee0b13778feeb1aa640802349` |
| PLAN DOCX member | `0fce8536941c45bcae7bae7a65ac1ec1a2959c805c53c2b4f3af674e272d1326` |
| PB Markdown member | `067d1f8680bb5de9f55dcb6ecf57c74bfb0f8ccc3724bc7db7f6dd9f354cc940` |
| WB containing ZIP | `70af7a87677a5e4b0dd9a794513fa1640eb21eb2ef8fe9748a05b1500b2c5f4b` |
| WB XLSX member | `12e17ad51b6ee2053a4e2c56d3ae8b5ff56f544a6f9a1487dd274c05af5c797e` |
| H1 | `42d47a69d9f0d392e17dea60d033f60c0ae6e10e616f129fd8c091b9a67408a1` |
| KBC | `6907060c34d3d9207efbbf306d4974f0479a4dcd4e2c74795f8fed203b1b2c47` |
| KB export | `015b714019081f458b2d8f28047b68761e47c7fe6e7ddab68670ecb0684be6af` |
| JOB29 | `9136fd79342f9053b545a64619d666f29ffd0fa95f6f75e02a875fca9e5ac535` |
| P2V03 ZIP | `3244e5ec8ae7cdd28a76dd3f4aec144ebbf34fa56a83b5b23b24be5080463606` |
| JOB30 / KB30 ZIP | `e92afdf8d41c5a348e65e18e0a1cad77f827d26dab5c6d3fe136d3439c1a8a1f` |
| JOB30 node member | `71d62956ae2b91db64deef08dcd0aaab37ba1a38f16d43c292f916a622f756c0` |
| JOB30 instructions (UTF-8, original whitespace) | `d89731bb49f09959e0c9c35550cb0b9fa71fa03a88295916887672c20390d860` |
| OD002-REVIEW-0.1 pre-approval nine-document ZIP | `9e34da889adf7847a6d519bf75dd60a7a6e900767876a3a9d8c53da298dd595e` |

Round 3's [member-level fingerprints, exact Job headings and KB claim ledger](OD004_OD005_TRIGGER_TIMING_REVIEW.md#1-sources-and-authority)
extend this manifest without replacing its earlier source identities or BR rows.
The [pre-Round-3 snapshot](../../reference/UC4_Problem2_OD002_Review_v0.2_2026-11-03.zip)
has SHA-256 `79f89595cdffd363504a5a54e4f5d1a0dab39681b8a1c0893443667f27f5c202`.
The [pre-approval OD004-OD005-REVIEW-0.1 snapshot](../../reference/UC4_Problem2_OD004_OD005_Review_v0.1_2026-11-03.zip)
has SHA-256 `1194f6dcf1a230bd42ad925035c843943018196dd10688c0e00e554fdf850460`;
its eleven members preserve all ten Problem #2 documents and the glossary.

PB §0's hierarchy is adopted as **VERIFIED process direction**: applicable
approved Grab project policy; validated supplementary official sources for gaps;
explicitly reviewed project rules. WB examples are test evidence. The supplied KB
has POC adoption, not formal Grab approval. No higher-authority policy is invented
to settle a conflict. PLAN and PB reuse `D-*` numbers differently: always cite
`PLAN D-05` or `PB D-05`, never a bare decision number.

## Interpretation labels and identity rules

Use PB §9 exactly:

- **VERIFIED:** source-backed and reviewed/approved for the stated UC4 scope.
  `VERIFIED [POC]` does not mean formally approved Grab policy.
- **PROPOSED:** candidate interpretation/mapping awaiting review; not binding.
- **UNKNOWN:** necessary policy, UI, evidence or permitted recovery not established.
- **CONFLICT:** incompatible source statements retained together for resolution.

Reading a cell accurately is an **extraction fact**, not a VERIFIED business
interpretation. All new requirement formulations, classifications, groups and
journey mappings below are **PROPOSED** unless explicitly labeled otherwise.
Existing POC adoption and formal approval are separate fields.

Preserve `TC-###`, `DF-###`, `JRN-TC-###`, `BR-###` and `VAR-TC-###-A/B` from PB §2.
**BR means business requirement.** A branch uses its JRN-local name and, where
materially different, a VAR ID. Keep PB's `VAR-TC-003-A/B/C` meanings unchanged.
Internal groups use `DG-###`; atomic findings use `DF-###/F01`. New group and
decision IDs (`OD-###`) are proposed internal identifiers, not Grab-issued IDs.
Definitions are in the [glossary](../../GLOSSARY.md#benchmark-journey-analysis).

## Candidate business requirement register

Each row remains **PROPOSED for complete Problem #2 acceptance**, except explicitly
agreed internal subsets. BR-009's scoped GF A/B/C/D interpretation now carries the
`OD002-REVIEW-0.2` **ENGINEERING_AGREED_POC** overlay; this does not approve every
related requirement or GM alternative. Linked conflicts remain open. No row grants
formal policy approval. Citations to JOB29 describe the existing POC contract.

**Qualified Round 3 applicability overlay:** the following approved subsets govern
current internal drafting of the retained source-based BR rows. They do not make
every requirement or mapped variant accepted. Scope and qualifications are
authoritative in OD45; the original rows retain their provenance.

| Round 3 decision / affected requirements | Agreed internal applicability | Remaining acceptance boundary |
|---|---|---|
| Q1/Q4 — BR-001/003/004/005 | Defined recent age-only entry receives education without an unnecessary goal question or inferred preparation/packing. Clarify assistance only when genuinely ambiguous; clear status requests are not re-clarified. Preserve GM status-only intake exception. | Source/implementation discrepancies remain; this does not create a phrase-based ambiguity rule or expand the GM exception. |
| Q2/Q3 — BR-001/002/003/005/008/009/018 | Requested/accepted navigation takes priority over unsolicited routine education, including same-order age correction; preserve necessary intake/disclosures. TC-027 upfront dual entry skips unsolicited timing/re-offer while retaining GM notice, computer-Portal readiness, preferences and status observation. | Beyond-only guidance/checkpoint rules remain implementation conflicts; qualified Q8 below settles coordinated design direction, with exact implementation/fixtures pending. No runtime change, early-form acceptance or final GM amount/status policy approved. |
| Q5 — BR-003/014 | Answer new timing question after decline without automatically repeating that offer; a new explicit request may change branch. | Applicable entry/Tool rules and separate finish/transfer consent still apply. |
| Q6 — BR-002/003 | Explicit cancellation-age fixtures with declared Asia/Kuala_Lumpur (UTC+8) test reference, reproducible same-session assumptions and documented relative expressions. Approval remains measured after order made. | Absolute-date, midnight-boundary and official business-calendar/clock conventions unresolved; no payment date inferred. |
| Q7 — BR-013, with BR-010/011/012 boundaries | Qualified KB-supported continuation with available evidence/information when no photo; retain evidence recommendations and flag separately established mandatory UI/policy conditions for review. | No eligibility, acceptance, completeness or approval promise, no condition silently waived; exact text, authenticated UI and final evidence policy remain open. |

**Qualified Q8 applicability overlay:** the following design obligations govern the
retained register; they do not change its original source rows or grant full BR
acceptance. [Contract-review §6](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#6-affected-requirements-cases-variants-and-findings)
retains the complete conditional impact selection.

| Q8 scope / affected requirements | Agreed design obligation | Remaining acceptance boundary |
|---|---|---|
| Admission/continuity — BR-001/002/005/006/007/008/009/014/019 | Coordinate existing admission, checkpoint validation and age correction. Retain compatible intent/consent/preferences/location/completed actions; invalidate only progress made invalid by corrected facts. Preserve truthful classification, observations and separate retry/fallback/transfer consent. | Minimal Agent-first implementation representation and exact correction/recovery fixtures remain pending; no new controller or broad walkthrough-state model is approved. |
| Education/disclosure accounting — BR-003, with BR-004/018 and evidence BR-017/020 boundaries | Internally selected education is not delivered education/disclosure. Use actual output evidence for the relevant context; preserve applicable once-only disclosures and Q1–Q7 triggers. | Transcript/displayed content does not certify audible receipt; OD-013 evidence and OD-006/011 controlled content remain separate. |
| Submission/access and consent boundaries — BR-010/011/012/013/015/016 | Preserve supported routes, actual access/form/submission observations and unresolved intent through correction. | No early eligibility, compensation guarantee, unsupported form submission or override of policy/UI restrictions; OD-007/010/009 fixture decisions and OD-014 owner evidence remain open. |

Regression protection is agreed for TC-001/025 education, TC-002/026 decline,
affected navigation variants and same-order corrections. Detailed recent requested/
accepted/correction identities and milestone acceptance remain proposed. Neither
navigation coverage nor a resolver marker substitutes for the original education
or declined-guidance target; both verdicts remain `NOT_RUN`.

**Qualified Q9–Q13 applicability overlay:** the criteria below are agreed internally,
subject to the full approval. References in the retained source/BR rows and prior
overlays to pending OD-007/010/009 now mean **residual fixture, unsupported-outcome
or formal acceptance**, not unanswered Q9–Q13. In particular, BR-012's retained
“universal spoken-role reminder remains undecided” is historical: Q11 settles
conditional applicability internally, with a broader reminder requiring separate
approval. It does not waive Owner/Manager authorization.

| Decision / affected requirements | Agreed internal criterion | Remaining acceptance boundary |
|---|---|---|
| Q9 — BR-006/007/019, with BR-002/005 continuity | History only for the relevant order missing from Cancelled; TC-007 Date-selector first failure → one supported repeat → observed success. Preserve action/wait and distinguish actual failure from correction-invalidated progress under Q8. | No invented recovery beyond supported steps; repeated failure, still-missing order and unusable checkpoint recovery retain scoped UNKNOWN outcomes. Complete fixture versions and formal benchmark attribution remain review work. |
| Q10 — BR-010/011/012/013/014 | Separate link/article/scroll/form/authorization/retry-consent/retry-result/submission observations; missing form does not prove wrong role. Preserve TC-006 declined primary and successful variant, TC-008 fallback, TC-009 submit-only. | Observations do not guarantee access, backend receipt or approval. Unavailable authorization/GF Portal and post-visibility submission failure remain unsupported-remedy boundaries. |
| Q11 — BR-012 | Owner/Manager authorization remains required for submission. Explain during access recovery and answer actual merchant role questions; no universal successful-path spoken reminder unless separately approved. | Applies by observed context, not from a role-omission label alone; historical findings are not regraded. Authenticated UI and formal policy approval remain separate. |
| Q12 — BR-014/020, with BR-003 offer triggers | **YES, PROVISIONALLY:** explicit TC-004 guidance decline and finish; reviewed TC-028 optional-offer/no-offer general-inquiry endings with explicit finish. Preserve required offers; acknowledgement, silence or submission does not resolve concern. | Benchmark fixture changes require reviewer approval. No silent waiver of a required offer or invented silence-timeout disposition; formal wording acceptance remains OD-011. |
| Q13 — BR-015/016, with BR-017/020 evidence boundaries | Supported trigger → separate person offer → later explicit acceptance → one Flow-owned mock transfer. Retry consent/acknowledgement/silence cannot transfer. TC-010's proposed unrelated menu-update fixture is distinct from ambiguous payout; normal closing stays separate. | No new handoff entitlement, real-contact-center assurance, literal-text acceptance or audible-completion proof. Terminal and voice evidence retain their separate requirements. |

This overlay changes applicability only; it retains 20 BR identities, all source
rows and independent verdict definitions. [Phase 4](OPEN_DECISIONS.md#phase-4-completion-and-remaining-review)
now supplies twelve full specifications and three reconciled pilots in the scoped
review candidate. Both verdicts stay `NOT_RUN`; baseline **NOT FROZEN**.

| ID | Applicable requirement / prohibition | Provenance and unresolved dependency |
|---|---|---|
| BR-001 | Establish and retain the current order's business line and merchant goal. Clarify genuinely missing/ambiguous facts; do not repeat clear answers or infer GrabFood merely from “food.” | PB D-02/D-03; JOB29 “MERCHANT CONTEXT,” “CURRENT ORDER LOB CORRECTION,” “OLDER CANCELLED ORDER”; WB:S!D5:D12. OD-004. |
| BR-002 | For age-dependent journeys, use deterministic age/weekday classification; a threshold selects guidance, not eligibility, rejection or a payment deadline. Record age origin/date assumptions. | H1 §§1,3,6; KB `UC4-MY-GF-THRESHOLD-001-C01` claims GF-015/016; `UC4-MY-GM-THRESHOLD-001-C01` claim GM-014. POC status-only exception; OD-004/005. |
| BR-003 | Give applicable education when its trigger applies: usual approval 1–2 business days GF / 3–5 GM after order made, then next regular payout, subject to policy. Distinguish approval from bank receipt. Do not universally insert education before every direct request. | KB `UC4-MY-GF-TIMING-001-C01` claim GF-007; GM equivalent claim GM-006; JOB29 “FIXED LOB TIMELINES,” “OLDER CANCELLED ORDER”; WB:S!E7,E16,E18; OD-004/005. |
| BR-004 | Deliver the applicable opening/recording disclosure once; respond to supplied intent without claiming unestablished preparation/packing. Entry/channel and safety priority determine applicability. | POC approved policy; JOB29 “GREETING OWNERSHIP”; WB:S!E4:E18; OD-011. |
| BR-005 | Collect only missing supported platform, guidance-style and loudspeaker preferences; retain them across recovery and platform changes. A loudspeaker refusal is not refusal of guidance. | WB:S!D6:F6,D8:F12,D16:F18; JOB29 “GUIDANCE PREFERENCES”; POC exception; OD-003/004. |
| BR-006 | One-by-one: one current navigation action and a wait; all-at-once: group actions only until the next required business observation. Status, form visibility and reported submission are separate observations. | PB §§3,6; JOB29 “ALL-AT-ONCE DECISION SEGMENTS,” “GRABMART PORTAL STATUS — ONE-BY-ONE SEGMENTATION”; H1 §5. OD-007. |
| BR-007 | GF status: App → Orders → Cancelled → relevant order/status. Use History → Date selector → Confirm only for an order missing from the Cancelled list; observe visibility before opening it. | KB `UC4-MY-GF-STATUS-001-C01` claim GF-005; JOB29 “GRABFOOD APP — COMPENSATION STATUS”; WB:S!E6,E9,E10; OD-007. History detail is a POC procedural reference, not independently validated UI. |
| BR-008 | GM status: computer Portal → Finance → Transactions → period/store → Category → Compensation for cancelled orders → observed result. Distinguish missing order from visible order with no compensation status; explain App-to-Portal transition. | KB `UC4-MY-GM-STATUS-001-C01` claims GM-003/004; JOB29 “GRABMART GUIDANCE RULES,” “GRABMART PORTAL — COMPENSATION STATUS”; WB:S!E16,F16,E18,F18; OD-003. |
| BR-009 | For a status-and-submission goal, observe status before deciding whether submission remains needed; retain the pending request. Never fabricate status or equate approval with bank receipt. Distinguish visible blank from unread/missing-order state. **Agreed GF subset:** A visible-blank review-request fixture without eligibility/award claims; B reported Auto approved/status-only explanation without unnecessary duplicate submission; C approval/payout/bank-receipt explanation and clarification priority; D clarify before status-dependent submission. Preserve unresolved intent and independent target coverage. | PB §4/D-05/D-10; PLAN §5; WB:D!G21; KB30 GF/GM status articles; JOB30 “STATUS AND SUBMISSION TOGETHER” / GF status; [OD-002 A/B/C/D](OD002_STATUS_DECISION_REVIEW.md#4-four-branch-decision-and-acceptance-model). **OD2 / OD002-REVIEW-0.2: VERIFIED [POC]**, requesting user, 2026-11-02; formal policy/payment remedies remain OD-002/014, broader triggers OD-004. Generic FOLLOW-UP source conflict persists; internal Q3 priority is settled. Submit-only remains distinct under OD-008; GM-specific interpretations remain proposed. |
| BR-010 | App request entry: relevant order → present Request for compensation link → Report a payment dispute → scroll → observe form. Established missing App link permits offering Portal fallback; wait for acceptance, preserve preferences. Missing link proves neither ineligibility nor wrong role. | KB `UC4-MY-GF-SUBMIT-001-C01` claims GF-012/013/014; GM equivalent claims GM-012/013; JOB29 “APP REQUEST LINK MISSING — PORTAL FALLBACK”; WB:S!D11:E11; OD-010. |
| BR-011 | Supported POC Portal submission starts at Help Centre → Search Bar/search dispute → Report a payment dispute → scroll → observe form. No fabricated Portal Request for compensation control. | KB `UC4-MY-SHARED-PORTAL-001-C01` claims SHARED-011/012/013; KC “Suite design”; JOB29 “PORTAL SUBMISSION — SEARCH BAR ROUTE.” Other KB routes are references, not accepted standard POC variants; OD-014. |
| BR-012 | Form access: article/scroll observation precedes role recovery. Owner/Manager authorization is required to submit; missing form is not proof of wrong role. Confirm unknown access, offer one retry, wait for acceptance, attempt once, then observe success/failure. | KB `UC4-MY-SHARED-REQUEST-001-C01` claim SHARED-007; WB:S!D9:F9,D12:F12; JOB29 “FORM NOT VISIBLE — ROLE ACCESS AND ONE RETRY”; OD-001/010. Universal spoken-role reminder remains undecided. |
| BR-013 | After observed form visibility, guide order details, LOB-appropriate evidence and merchant self-submission; obtain the merchant's submission report before acknowledgement. No photo does not prove no preparation/packing or deny access. Approval remains conditional; backend receipt is unverified. | KB GF/GM evidence C01/C02 (GF-009/010/011; GM-008/009/010), SHARED-REQUEST; JOB29 “POST-SUBMISSION RESPONSE CONSTRAINTS”; H1 §6; OD-005/014. |
| BR-014 | Respect declined guidance/retry, retain unresolved intent, offer further help as applicable and close only on an appropriate finish signal. A missing screen/access issue is not a resolved claim; avoid repeated education/offers without a new need. | WB:S!D5,D7,D9,D15,D17; PB §§3,9; JOB29 “GUIDANCE,” “CLOSING”; OD-009. Transport disconnection cannot be attributed to the Agent without evidence. |
| BR-015 | Authorized recovery handoff requires a spoken offer and separate explicit consent; retry consent is not transfer consent. Preserve correct mock-transfer/terminal ownership and avoid repeated offers or false real-connection claims. | WB:S!D12:F13; JOB29 “CONTROLLED FLOW CONTENT,” “CONNECTION AFTER FAILED FORM RETRY,” “GRABMART PORTAL UNAVAILABLE — SUPPORT OFFER”; OD-009/010. |
| BR-016 | Clarify genuinely ambiguous scope; for clearly unrelated issues explain scope and offer supported handoff, then wait for consent. “Payout” alone is not out of scope. | WB:S!D13:F13; JOB29 “OUT OF SCOPE”; OD-009. |
| BR-017 | Assess audible and displayed responses separately in voice tests; record missing response, interruption and timing evidence. Do not infer ASR loss, barge-in cause or a response-time SLA without evidence. | PB §6; PLAN §4/P075; WB:D!G17,G21; OD-013. A numeric latency acceptance threshold is UNKNOWN. |
| BR-018 | Preserve the currently adopted GM partial-compensation notice once before applicable navigation; do not promise a fixed amount/full award. Its certainty and disagreement with sample full-or-partial wording require business review. | KB `UC4-MY-GM-PERISHABLE-001-C01` claim GM-011; JOB29 “GRABMART GUIDANCE RULES”; H1 §6 item 2; WB:S!E16,E18; OD-006. |
| BR-019 | On a first ordinary stuck navigation action, repeat that current action once with supported context, wait and continue only after success. Specific missing-link, missing-order and missing-form recovery takes precedence; no premature transfer. | WB:S!D10,F10; JOB29 “GUIDANCE TURN BEHAVIOR”; OD-007/010. Further unsupported recovery is UNKNOWN. |
| BR-020 | Assess semantic meaning/process rather than sample wording. Apply literal matching only to a separately identified, applicable controlled-language requirement; preserve original severity separately from internal assessment. | VERIFIED process direction: PB D-03/D-06, §§3,6; PLAN §§1,4. The concrete wording register still needs OD-011 review. |

Claim suffixes above are abbreviated only in prose: e.g. GF-007 is
`UC4-MY-GF-CLAIM-007`, and SHARED-007 is `UC4-MY-SHARED-CLAIM-007`.
Elsewhere, `KB GF-STATUS` means article `UC4-MY-GF-STATUS-001`, and
`KB GF-STATUS-C01` means chunk `UC4-MY-GF-STATUS-001-C01`; the same expansion
applies to GM and SHARED article/chunk names. Slash-separated IDs retain the
prefix, e.g. `BR-001/002` means BR-001 and BR-002.

### Requirement kind and assessment ownership (proposed metadata; IDs unchanged)

The BR register combines two different types of normative statements. Keep the existing IDs and mappings, but record `requirement_kind` so that **changing evaluation methodology is not mistaken for changing merchant-facing Agent behavior**.

| IDs | `requirement_kind` | Ownership and acceptance rule |
|---|---|---|
| BR-001–BR-016, BR-018–BR-019 | `AGENT_BEHAVIOR` | Conditional merchant-facing facts, workflow, consent, navigation or recovery. Grade only when their preconditions apply, against the relevant POC-authority/approval scope. |
| BR-017 | `QA_EVIDENCE` | Audio/display/timing capture discipline. A missing evidence channel may yield BLOCKED_ENV or NEEDS_REVIEW, not automatically an Agent behavior defect. No invented SLA. |
| BR-020 | `QA_SEMANTIC_ACCEPTANCE` | Review discipline for paraphrases versus source-controlled exact text. It governs grading; it is not a line the Agent must speak. Exact-language obligations, if approved, remain part of their substantive applicable BRs and OD-011. |

`BP-##` process families in [classification](TC_CLASSIFICATION_MATRIX.md#candidate-shared-business-process-families-bp) group the **business processes**; `DG-###` groups reported and plausible **defect findings**; `BR-###` describes an applicable requirement. No one of these identifiers proves a technical shared cause. New type labels remain PROPOSED until reviewers accept the taxonomy.

### Controlled language boundary

JOB29 explicitly designates exact opening/recording text, LOB timeline sentences,
GM partial notice/Portal redirect, and particular scope/person-offer text;
“CONTROLLED FLOW CONTENT” assigns terminal utterances to the Flow. These are
**source-backed POC controls**, not permission to make every WB sentence literal.
The inventory must record exact source section/text/hash, trigger and approval
scope under OD-011 before becoming a Problem #2 literal oracle. Official UI labels
retain their identity; natural instructional phrasing remains flexible. WB's
generic greeting preparation claim and “Glad your issue is solved” are not
independent evidence of preparation or resolution.

## Minimal records

These are proposed documentation records, implementable later in any suitable
format. Preserve source values and allow nulls; do not fill gaps with inferred facts.

| Record | Minimum fields |
|---|---|
| Source | `source_id`, original path/archive/member, SHA-256, version/date, locator, authority, adoption/formal-approval scope, supersedes link where explicit |
| Requirement | `requirement_id`, version, conditional rule/prohibition, semantic or controlled-text mode, source refs, interpretation label, approval scope, reviewer/date, open decision IDs |
| Journey / variant | JRN and original TC; version/state; goal; initial facts including unknowns; target branch; VAR and parent JRN; M01… milestones with conditions/BRs; dependency edges; branch decisions; permitted variation; prohibitions; source refs and reviewer |
| Defect / finding / group | Original DF and immutable cells/status/severity; child finding and observation; proposed triage; group memberships with BR rationale; directly reported TC separately from plausible impacts; confidence, status history, root-cause evidence, closure coverage |
| Configuration baseline | `configuration_id`, captured timestamp; Flow/Job/Agent/KB/Tool/Code versions or stable refs plus content hashes; model/settings; runner/scenario versions; effective Endpoint-to-revision binding evidence and gaps; no credentials |
| Execution evidence | `execution_id`, actual run/batch IDs, TC/VAR target, fresh-conversation identity, channel/language, fixture/version, capture time/timezone, configuration ID, transcript/audio/trace paths and hashes, attempted/skipped turns, merchant-reported versus system-confirmed observations |
| Assessment | `assessment_id`, execution ID, acceptance/JRN/BR versions, reviewer/date, observed branch, milestone observation and compliance separately, **behavior_verdict**, **coverage_verdict**, reasons/BR/finding links, evidence locators; original automated result retained separately |
| Change / comparison | `change_id`, approved diff/baseline IDs, changed BRs/dependencies; before/after executions and assessment IDs, comparable conditions and confounders; added/removed requirements; regression selection with inclusion reasons and outcomes |

Required relationships are many-to-many: `BR ↔ JRN/VAR ↔ TC ↔ finding ↔ DG`,
then `finding/BR ↔ change ↔ evidence/assessment`. A group can contain findings
with different historical statuses. Group membership never supplies a direct
DF–TC association, a common cause, remediation or a pass.

### Two independent verdicts

Use PB's vocabulary with an explicit axis:

| Verdict | Agent behavior axis | Intended-branch coverage axis |
|---|---|---|
| PASS | Applicable approved requirements satisfied on the observed branch. | Target conditions and required stages were actually exercised with evidence; not a claim that every answer was correct. |
| FAIL | Supported violation of an applicable requirement. | Use INCOMPLETE_COVERAGE for an uncompleted target, rather than conflating it with behavioral failure. |
| INCOMPLETE_COVERAGE | Not used as a substitute for a behavioral judgment. | Another branch reached, or intended stages remain unobserved. |
| BLOCKED_SPEC | Unresolved rule prevents the relevant judgment. Independently established failures remain recorded. | Contradictory/undefined fixture prevents deciding what the target is. |
| BLOCKED_ENV | Environment/evidence failure prevents the relevant judgment; preserve earlier observations. | Environment prevents establishing target coverage. |
| NEEDS_REVIEW | Evidence or interpretation needs adjudication. | Branch/coverage evidence is insufficient or disputed. |
| NOT_RUN | No execution assessed under this work. | No target execution under this work. |

Illustrative combinations, **not executed results**: under OD-002's agreed internal
Q2/Q3 scope, correctly handled B/C can be `PASS / INCOMPLETE_COVERAGE` for TC-003
when applicable dependent requirements are settled; a fully traversed A target
with incorrect timing facts can be `FAIL / PASS`. D's clarification alone cannot
supply submission coverage; a later continuation must establish and exercise A's
target stages. Unknown policy or unsupported payment-resolution outcomes still
yield `BLOCKED_SPEC`/`NEEDS_REVIEW` for that judgment, not a payment-resolution PASS.
Current verdicts remain `NOT_RUN`. TC-006's internal declined-retry target follows
agreed OD-001; external target certification remains pending. Neither a
successful-retry variant nor a convenient source column supplies decline coverage.

The following v0.2 record is a **historical example before the v0.3 fixture
agreement**, not TC-006's current internal decision status:

```yaml
acceptance_version: P2-DRAFT-0.2
journey_id: JRN-TC-006
tc_id: TC-006
specification_label: CONFLICT
open_decisions: [OD-001]
execution_id: null
configuration_id: null
observed_branch: null
behavior_verdict: NOT_RUN
coverage_verdict: NOT_RUN
evidence_links: []
reviewer: null
```

## Versioning, comparison and regression selection

1. After review, freeze a named acceptance version with source hashes, scope,
   reviewers and unresolved blockers. Configuration identity and acceptance
   identity are separate; H1's verified October 30 export is historical context,
   not a fresh Problem #2 served-revision baseline.
2. Preserve each actual conversation and original automated grade. Add a new
   assessment when a rubric changes. A **regrade** compares the same capture
   under different requirements; it does not demonstrate a deployed correction
   or supply skipped turns. A fresh run compares runtime behavior.
3. Compare before/after only with explicit configuration, requirement, fixture,
   branch, age/timezone and channel versions. Mark confounding differences and
   sample sizes; do not silently drop failed or alternate-path runs.
4. For changed BRs, select every mapped TC/JRN/VAR, all linked atomic findings,
   and prerequisite/downstream boundaries affected by the change. Add plausible
   group impacts for review; record why each is included or excluded. Recompute
   selection if a shared policy or requirement version changes.
5. Examples: BR-012 selects TC-003/005/006/007/008/009/027/029 at applicable form
   boundaries, including the TC-006 retry variants and TC-009 failed retry;
   BR-008 selects TC-027/029 plus GM direct-status/recovery variants; BR-003
   selects relevant education paths and direct-navigation negative controls.
   These are proposed regression selections, **not newly reported DF links**.
6. Require original target fixture, relevant alternatives, neighboring shared
   requirements and voice evidence where implicated. PB §7 proposes five fresh
   independent runs for high-risk paths; sampling/any external requirement needs
   OD-015 review. Neither a single pass nor five passes proves reliability.

Keep `DF_REMEDIATED`, `TC_PASS`, `VAR_PASS`, `STAKEHOLDER_ACCEPTED` and `RELEASED`
independent (PB §7; PLAN §7/P123). The current deliverable is a **reviewable draft**,
not completion of PB's full implementation/approval/execution definition of done.

## Documentation verification

Historical **v0.1** documentation audit, completed offline on **2026-11-02**;
counts below describe that original five-file delivery. Round 2 checks are recorded
in [the OD-002 addendum](OD002_STATUS_DECISION_REVIEW.md#8-version-and-verification-record).

- All **15 TC inventory rows and direct DF mappings** match the original workbook;
  all **18 DF status/TC/date/category/severity/retest records** match its cells.
- **49 atomic records** account for the 18 reports, including positive observations
  and documentary conflicts; they are not 49 confirmed defects. **Nine proposed
  groups** have consistent child membership and direct-TC unions.
- **Three pilots, 18 proposed variants, 20 BRs and 15 open decisions** have valid
  internal ID references. Relative links/heading anchors and Markdown table
  structure were checked. Nine source/archive fingerprints match their originals.
- **159 pre-existing repository files and 467 historical report files** are
  byte-identical to the task's preservation baseline. The original glossary bytes
  remain an unchanged prefix, followed by the new benchmark-analysis definitions.
  The newly supplied decision bundle and original workbook are unchanged.
- **Zero live requests and zero official-baseline executions.** These checks
  validate documentation/source accounting, not Agent behavior or policy approval.

Read-only source extracts and the audit result are retained at
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-problem2-sources-62rzemtm`:
`benchmark-source-extract.json`, `decision-plan.txt`, `playbook.md`,
`preservation-before.json`, `verify-documents.py` and
`documentation-verification.json`. Original paths, archive members and hashes
above remain the primary provenance.

## Phase 4 scoped acceptance baseline review candidate

**Identity:** `P2-BASELINE-CANDIDATE-0.1`, prepared 2026-11-04, **NOT FROZEN**.
**Catalog:** [P2-JOURNEYS-0.4](JOURNEY_PILOT.md#catalog-index-and-version-scope), all
15 original TCs and corresponding `JRN-TC-###` records. **Requirement version:**
the retained 20 BR source rows plus qualified Q1–Q13 applicability in this candidate.
**Variant version:** the 18 existing rows in `P2-JOURNEYS-0.4`, each retaining its
own authority and blocked outcomes. **Controlled text:** `P2-CONTROLLED-TEXT-0.1`.
**Configuration ID:** `null` (current served revision unverified).
**Execution/evidence IDs:** `null`; `behavior_verdict=NOT_RUN`;
`coverage_verdict=NOT_RUN`. No candidate inclusion is a pass or whole-rule approval.

The project-side user confirmed this Phase 4 drafting scope after the requested
shared-understanding check on 2026-11-04. That confirmation authorizes preparation
of these documents only; it adds no business rule, reviewer appointment or freeze.
The five prior engineering approval records remain authoritative and byte-identical.

### Journey inclusion and assessment scope

Included exactly: **TC-001/002/003/004/005/006/007/008/009/010/025/026/027/028/029**,
with corresponding `JRN-TC-###` IDs and version `P2-JOURNEYS-0.4`. The catalog
index is the inclusion manifest for their targets/BPs; its common contract is an
explicit part of every JRN. All seven BP family definitions and existing membership
rows remain as recorded. The twelve new records and three reconciled pilots are
structurally complete for review; formal/full criterion acceptance is separate.

Review each conditional criterion using three independent fields:

1. **Source/interpretation:** VERIFIED [POC], PROPOSED, UNKNOWN or CONFLICT,
   with exact source and qualified agreement. Source-controlled wording is not
   automatically a formally approved policy or a new literal assessment rule.
2. **Candidate disposition:** included for review, included with scoped blocker,
   or excluded outcome with rationale. An included JRN can contain all three.
3. **Execution axes:** future behavior and target coverage assessed independently;
   current values remain NOT_RUN even when a future judgment would be BLOCKED_SPEC.

### Included requirement manifest

All rows below are scoped to actual preconditions; existing source/BR definitions
above remain the detailed authority. **Complete BR acceptance remains reviewable.**
Q1–Q7 mean the qualified OD-004/005 round; OD-002 Q1–Q4 remain separately namespaced.

| BR / kind | Included criterion and TC/variant applicability | Authority and dependent review boundary |
|---|---|---|
| BR-001 / AGENT_BEHAVIOR | Reuse actual order/LOB/goal; clarify only missing or genuinely ambiguous facts; all 15 by context. | POC Job/KB; qualified Q1/Q4/Q8; TC-010 scope clarification. No default GF from ambiguous “food.” |
| BR-002 / AGENT_BEHAVIOR | Declared cancellation-age routing for age-dependent targets; all except TC-010; VAR-TC-027-F retains narrow bypass. | Q6 explicit same-session UTC+8 convention; official calendar/absolute/midnight handling excluded pending OD-005. No eligibility/late-payment inference. |
| BR-003 / AGENT_BEHAVIOR | Actual education on applicable entry; TC-001/002/004/005/007/008/025/026/028/029 and TC-006/009 prefix by fixture; TC-003/027 direct-request suppression controls. | Qualified Q1–Q5/Q8 and T01–T18; usual approval differs from payout/receipt. Literal acceptance OD-011; official timing OD-005. |
| BR-004 / AGENT_BEHAVIOR | Once-only applicable normal opening/disclosure, all 15; preserve native-empty/utterance-first and existing safety precedence. | Historical POC owner/source reference; OD-011/013 exact/channel acceptance. No greeting-based preparation fact or new safety-policy scope. |
| BR-005 / AGENT_BEHAVIOR | Necessary preferences once; TC-003/005/006/007/008/009/027/029, applicable alternatives; preserve on transition/correction and honor refusal. | OD-003, qualified Q3/Q4/Q8; VAR-TC-027-F no unnecessary age/loudspeaker intake. Education-only cases are negative controls. |
| BR-006 / AGENT_BEHAVIOR | One action/wait or grouped decision segments on navigation TCs; status/form/submission observations distinct. | Q9/Q10 plus source segmentation; TC-005/029 grouped versus one-by-one controls. No inferred action completion. |
| BR-007 / AGENT_BEHAVIOR | GF App status, conditional missing-order History; TC-003/005/006/007/008 and VAR-TC-003-D. | Q9; TC-007 actual Date failure/repeat/success selected internally. Formal source attribution and further missing-order remedy remain pending. |
| BR-008 / AGENT_BEHAVIOR | GM computer-Portal status and readiness; TC-027/029, VAR-TC-027-A/C/D/F; protect App submit-only G. | OD-003/Q3/Q8, existing direct-status-only exception. Authenticated UI and unsupported missing-order outcomes remain scoped. |
| BR-009 / AGENT_BEHAVIOR | Observed status plus remaining goal before conditional request; TC-003/005/006/007/008/027/029; TC-009 submit-only negative control. | OD-002 GF A/B/C/D agreed subsets; no automatic GM alternative-policy approval. Canonical status/duplicate/unpaid-remedy judgments remain OD-002/014. |
| BR-010 / AGENT_BEHAVIOR | App link/article/scroll/form distinctions and offered/accepted fallback; applicable GF request paths, VAR-TC-027-G App submission. | Q10; TC-008 fallback retained. Missing link/form does not establish role, eligibility or rejection; authenticated UI/early acceptance OD-014. |
| BR-011 / AGENT_BEHAVIOR | Supported Portal Search Bar submission; TC-008/009/027/029 and accepted Portal alternatives. | POC SHARED-PORTAL/JOB30, Q10; no fabricated request-link control. Other reference routes excluded as standard fixtures pending review. |
| BR-012 / AGENT_BEHAVIOR | Authorization, separate one-retry offer/acceptance/attempt/result; applicable submission/access TCs and variants. | Q10/Q11; conditional role explanation, not universal successful-path speech. Unavailable access and post-visible errors retain distinct blocked dispositions. |
| BR-013 / AGENT_BEHAVIOR | Stage-specific evidence and observed self-submission/report; education reminders and applicable request paths. | Q7/Q10; no-photo continuation qualified, no waiver of known mandatory UI/business conditions. Final substitutes/eligibility/evidence completeness OD-014. |
| BR-014 / AGENT_BEHAVIOR | Respect refusal, retain unresolved goal, separate completion from finish; all applicable ordinary endings. | Q5/Q10/Q12; TC-004/028 fixture repairs provisional, benchmark review required. Unspecified silence timeout excluded. |
| BR-015 / AGENT_BEHAVIOR | Supported person offer, later explicit acceptance, one Flow-owned mock terminal; TC-009/010, VAR-TC-006-B/C and VAR-TC-027-C. | Q13; consent declined is no transfer. No generic handoff entitlement or real CXone assurance; OD-011/013 terminal exactness/audibility review. |
| BR-016 / AGENT_BEHAVIOR | Clarify ambiguous scope; TC-010 clearly unrelated menu-update target and in-scope payout controls. | Q13; menu fixture remains proposed internal benchmark refinement. Financial remedy not supplied by scope clarification. |
| BR-017 / QA_EVIDENCE | Separate displayed/generated and audible evidence; all cases where voice judgment is claimed, especially TC-003/004/010/026. | Established evidence discipline; OD-013 expectations/capture pending. No numerical latency SLA or ASR/barge-in cause inferred. |
| BR-018 / AGENT_BEHAVIOR | Existing GM notice once before applicable navigation; TC-027/029 and GM navigation/submission variants; timing-only/GF negative controls. | POC source control, Q3/Q8 continuity. OD-006 certainty and OD-011 literal adoption remain explicit conflicts; no individual award guarantee. |
| BR-019 / AGENT_BEHAVIOR | First ordinary stuck action repeated once, observed success before continuation; TC-007 and conditionally other navigation paths. | Q9; distinct from missing link/order/form or Q8-invalidated progress. Further unsupported failure disposition blocked. |
| BR-020 / QA_SEMANTIC_ACCEPTANCE | Meaning/process rather than sample transcript; all 15 and included variants; literal comparison only with applicable accepted control. | PB/PLAN process direction, qualified agreements; controlled register adoption needs OD-011 review. Original severity remains independent. |

### Existing variant manifest

The rows below preserve **18 existing VAR identities**, not 18 newly accepted tests.
Sources and detailed observations remain in the parent JRN registers. All have
current `NOT_RUN / NOT_RUN`. Approval of a criterion does not approve an entire VAR.

| VAR | Included branch / relation to original target | Authority / remaining boundary |
|---|---|---|
| VAR-TC-003-A | Reported Auto approved/status-only; original App submission coverage incomplete. | OD-002 Q2 provisional internal explanation; formal meanings/duplicate policy pending. |
| VAR-TC-003-B | Reported approval/no bank receipt; original submission coverage incomplete. | OD-002 Q3 provisional explanation/clarification; payment remedy blocked. |
| VAR-TC-003-C | Unclear status; coverage only if clarification establishes and exercises original A target. | OD-002 Q4 agreed internal clarification; unknown statuses retain review boundary. |
| VAR-TC-003-D | Missing order; conditional History and later observations. | Q9 criteria agreed; full variant/formal attribution and unsupported further recovery pending. |
| VAR-TC-003-E | Absent App link, offered Portal fallback; not full App-route coverage. | Q10 boundaries; accepted/declined fallback distinct, GF Portal-unavailable remedy blocked. |
| VAR-TC-003-F | Article scrolled/form absent; access recovery independent of submission. | Q10/Q11/Q13 criteria; complete variant and unsupported outcomes reviewable. |
| VAR-TC-006-A | Retry accepted/form visible/submission; not declined primary coverage. | OD-001 preserves identity; Q10 criteria agreed, full variant acceptance pending. |
| VAR-TC-006-B | Accepted retry fails, later person offer accepted, mock transfer. | Q10/Q13 supported criteria; full variant/terminal evidence acceptance pending. |
| VAR-TC-006-C | Accepted retry fails, person offer declined, no transfer. | Q13 consent boundary, Q12 finish; full variant acceptance pending. |
| VAR-TC-006-D | Initial form visible; skip recovery/retry. | Q11 conditional reminder criterion settled internally; authorization remains required. |
| VAR-TC-006-E | Authorized access unavailable/unestablished. | Clarification/non-inference assessable; unsupported final access remedy UNKNOWN. |
| VAR-TC-027-A | Portal-first status/conditional request; not App-transition coverage. | Supported POC route; full variant and GM conditional semantics reviewable. |
| VAR-TC-027-B | GM compensated/approved alternative; not original submission coverage. | PROPOSED GM-specific semantics; no automatic extension of all OD-002 GF conclusions. |
| VAR-TC-027-C | Computer Portal unavailable; separate offer/accept/decline/access-gained branches. | Existing GM support source, Q13 consent; transfer does not cover status/submission. |
| VAR-TC-027-D | Order absent; period recheck, retained store/Category and new visibility. | Source-supported recovery; still-missing remedy UNKNOWN. |
| VAR-TC-027-E | Portal form absent; role/access and one separate retry/result. | Q10/Q11/Q13 boundaries; full variant acceptance and unavailable authorization pending. |
| VAR-TC-027-F | Direct GM status-only with no age/loudspeaker supplied. | Protected isolated-POC exception; excludes timing, eligibility, submission, dual intent and unresolved order/LOB conflict. |
| VAR-TC-027-G | GM App submission-only; no forced Portal status. | Supported POC route; form/evidence/UI acceptance remains qualified. |

**Supplemental profile index, without new VAR allocation:**

| Source-qualified aliases | Included review coverage | Limit |
|---|---|---|
| Q8 report N01–N06 | Recent requested/accepted status, submission and dual tasks, supported GF/GM routes and entry-specific consent. | Detailed fixture identities/versions need review before execution; no unsupported route cross-product. |
| Q8 report N07/N08 | Accepted generic-offer scope; no request/acceptance, declined or withdrawn guidance; preserve education/decline controls. | N07 acceptance cannot replace TC-002/026 decline; N08 is not a new journey. |
| Recovery review A1–A6 | Navigation observations, missing order, ordinary failure, unsupported next outcomes, correction and GM comparison. | Q9/Q8 approve stated criteria, not every detailed profile or unknown remedy. |
| Recovery review B1–B8 | Link/form/access distinctions, retry outcomes and unsupported access/submission errors. | Q10/Q11 conditional scope; no form/role guarantees. |
| Recovery review C1–C7 | Explicit finishes, consent responses, unrelated/corrected scope, task-versus-finish and GM access comparator. | Q12 provisional fixtures and Q13 supported handoff only. |

TC-028's two permitted endings are local branches of its single informational
target. Either may cover that target; the no-offer branch never counts as guidance
decline. Q8 and R profile letters remain namespaced; OD-002 situation A/B/C/D are
not VAR suffixes. No additional benchmark/BR/VAR/DG identity is introduced.

### Controlled-language applicability register

**Register:** `P2-CONTROLLED-TEXT-0.1`, part of this candidate. CT01–CT14 are local
row locators, not additional BRs. **Source version for Job rows:** JOB30, October 30
export `e92afdf8d41c5a348e65e18e0a1cad77f827d26dab5c6d3fe136d3439c1a8a1f`, Job
`nodeData/6ae43b6f90878ce305636d97`, instruction SHA-256
`d89731bb49f09959e0c9c35550cb0b9fa71fa03a88295916887672c20390d860`.
These are **whole-source hashes**, not phrase hashes. Quotations below preserve
the words with source wrapping whitespace normalized; semantic rows are labeled.
Flow rows use the same export and exact member/owner recorded below and in R §2.

**Approval/channel rule for every row:** existing POC control/source content is
recorded with its actual authority; **Problem #2 literal-register adoption and
formal business/QA approval remain pending under OD-011**. Q1–Q13 settle only
their qualified applicability. English source text is not a multilingual control;
displayed text can support text assessment, while voice claims require audible
evidence under OD-013. The register does not certify current served configuration.

| Row / BR | Source heading or member; owner | Wording / mode | Trigger, exception and specific approval boundary |
|---|---|---|---|
| CT01 / BR-004 | JOB30 `GREETING OWNERSHIP`; Flow native empty entry, Agent exceptional utterance-first fallback | “Hi, I'm your Grab AI Assistant, and I'll be assisting you today. Please note that this call will be recorded for quality assurance and training purposes.” | Once when normal opening is outstanding; existing safety priority, prior output and terminal ownership govern. No inferred preparation/packing sentence. Exact source control; literal/channel adoption pending. |
| CT02 / BR-003 | JOB30 `FIXED LOB TIMELINES`; Agent | “Compensation for a cancelled order is usually approved within one to two business days after the order was made, and it is then paid in your next payout cycle, the same cycle as your regular order earnings, subject to Grab's cancellation policy and guidelines.” | GF actual education/timing trigger under T01–T18 and qualified Q1–Q5/Q8; no automatic timeline for upfront requested guidance. Fixed source sentence; official calendar/payment guarantee not established. |
| CT03 / BR-003 | JOB30 `FIXED LOB TIMELINES`; Agent | “Compensation for a cancelled order is usually approved within three to five business days after the order was made, and it is then paid in your next payout cycle, the same cycle as your regular order earnings, subject to Grab's cancellation policy and guidelines.” | GM applicable education/timing trigger; TC-027 upfront dual suppresses unsolicited education. Approval is not bank credit; no exact payment date or substituted “Once approved” wording accepted by the source. |
| CT04 / BR-013 | JOB30 `GRABMART RECENT CANCELLED ORDER`; Agent | “Please take a photo of the order as evidence, in case you would like to submit a request for our support team to review further after it has been more than five business days.” | First applicable recent GM education after CT03 and before further help. Source exact reminder; not packed-items form wording or a submission deadline. Q7 qualification and final evidence policy limits persist. |
| CT05 / BR-013 | JOB30 `OLDER CANCELLED ORDER`; Agent | “If you still have a photo of the prepared food, keep it as evidence in case it needs review.” | GF older elicited status/dual inquiry after timeline and before offer. Not a universal older timing-only or GM requirement; no preparation fact inferred. Source exact reminder, Q7/OD-014 limits. |
| CT06 / BR-018 | JOB30 `GRABMART GUIDANCE RULES`; Agent | “Please note that compensation will be partial, based on the assessment of the perishable items.” | Once before first applicable GM status/submission navigation, retained across transitions/corrections. Never GF or routine timing-only education. Existing POC control; **OD-006 certainty CONFLICT** remains, literal adoption pending; no individual award guarantee. |
| CT07 / BR-008 | JOB30 `GRABMART GUIDANCE RULES`; Agent | “This particular check has to be done on the GrabMerchant portal on a computer.” | App-selected GM journey containing status, before first Portal-status action; establish readiness and preserve preferences. Not universal for GM App submission-only. Existing POC exact redirect, OD-003 transition/Q3 retained. |
| CT08 / BR-015 | JOB30 `CONNECTION AFTER FAILED FORM RETRY`; Agent | “Would you like me to connect you with someone who can help further?” | Supported accepted authorized retry actually failed: first response is this offer alone, then wait for later response; Q13 consent boundary. No inferred trigger from arbitrary failure. Source exact offer; register adoption pending. |
| CT09 / BR-015/016 | JOB30 `OUT OF SCOPE`; Agent | “I only handle issues about cancelled orders. Would you like me to connect you with someone who can help further?” | Clearly unrelated topic, then wait; ambiguous payout needs clarification and corrected in-scope intent cancels the unrelated offer. Q13; TC-010 menu-update fixture remains proposed. |
| CT10 / BR-015 | JOB30 `GRABMART PORTAL UNAVAILABLE — SUPPORT OFFER`; Agent | “Would you like me to connect you with someone who can help with your GrabMerchant portal access?” | Actual GM computer-Portal status access block: brief requirement acknowledgement, then this final question; later explicit acceptance. Not GF fallback or generic role failure; Q13 applies. |
| CT11 / BR-015 | Flow Say `nodeData/6ae43b6f90878ce305636db3`, R S06; Flow | “Please hold while I transfer you to a customer service officer. You might have to repeat some of our conversation. Thank you for your patience and understanding.” | Supported person offer accepted later, one matching mock terminal; Agent adds no ordinary goodbye/end_call. Mock-only, no real CXone proof. Source fixed Say, full playback unverified. |
| CT12 / BR-014 | Flow Say `nodeData/6ae43b6f90878ce305636da9`, R S09; Flow | “Thank you for calling Grab. If there's anything else you need help with, please contact us again. Have a nice day.” | Clear finish after appropriate further-help question; distinct from transfer. No close inferred from form/submission, refusal alone, acknowledgement or silence. Source fixed Say; audible completion needs separate evidence. |
| CT13 / BR-006/007/008/010/011 | JOB30 route headings; KB GF-STATUS/GM-STATUS/GF-SUBMIT/GM-SUBMIT/SHARED-PORTAL; Agent guidance | **UI identity mode:** Orders; Cancelled; History; Date selector; Confirm; Request for compensation; Help Centre; Search Bar; Report a payment dispute; Finance; Transactions; Category; Compensation for cancelled orders. | Preserve supported label identity and LOB/platform/observation applicability; ordinary instruction phrasing is semantic. No invented controls, translations or authenticated-screen guarantee; OD-014 remains. |
| CT14 / BR-013/014 | JOB30 `RECENT CANCELLED ORDER` and `CLOSING`; Agent | **Semantic mode:** recent GF prepared-food reminder with possible later review after more than two business days; appropriate further-help question. | GF recent source expressly allows natural example wording outside fixed timeline. Distinguish GM exact order-photo reminder and later packed-items form evidence. Q7/Q12 apply; this row is not a literal oracle. |

Role authorization/recovery explanations and form-completion instructions remain
semantic unless separately designated and accepted. Q11 requires conditional
explanation/actual role answers, not universal scripted speech. Q7's qualified
no-photo continuation governs over an unqualified reading of “attach” instructions;
it supplies no invented substitute, exemption or approved replacement exact text.

### Outstanding outcomes and explicit exclusions

Each row blocks only its dependent criterion/outcome. **Current verdicts stay
NOT_RUN**; the assessment consequence below describes later judgment, not a run.
Known supported prefixes, explanations, refusals and consent rules remain reviewable.

| Boundary / affected requirements and journeys | Candidate treatment / missing authority | Later assessment consequence |
|---|---|---|
| Repeated ordinary failure, order still missing, or unusable applicable checkpoint recovery; BR-006/007/008/019; TC-007, VAR-TC-003-D, VAR-TC-027-D and Q8 correction controls | Include observed prefix and non-advancement rules; exclude invented extra attempts/escalation. POC contract/policy/UI owner must supply the specific next remedy. Existing rejection with a valid next stage remains supported. | BLOCKED_SPEC/NEEDS_REVIEW only for unsupported continuation; known violations still assessable. |
| GF Portal unavailable, authorization unavailable, post-visible submission failure; BR-010/011/012/013/014/015; TC-008 and applicable request variants including VAR-TC-006-E | Distinguish access, form and submission errors; do not transplant GM Portal offer authority or failed-form-retry entitlement. Missing remedy remains UNKNOWN. | Dependent outcome blocked; no claim of target submission or automatic transfer. |
| Canonical status/duplicate/dispute/approved-but-unpaid remedies; BR-009; TC-003 alternatives and GM alternatives | Retain agreed OD-002 bounded GF explanations; GM-specific alternatives remain proposed. Formal policy and financial remedy/trigger need OD-002/014 owner evidence. | Bounded explanation may be assessed; end-to-end financial resolution blocked; original submission coverage independent. |
| Eligibility, early form acceptance, mandatory evidence/substitutes, authenticated screens; BR-010/011/012/013; all applicable submissions | Fixture observations are merchant/test inputs, not verified real UI. Q7 supports qualified continuation without guaranteeing acceptance/completeness; retain any separately established mandatory condition. | Block only unsupported policy/UI assurance; evaluate supported conversational prefix separately. |
| Official clock/calendar, absolute dates, midnight, 90/5/3-day applicability; BR-002/003/013; age/timing-dependent cases | Include Q6's explicit same-session cancellation-age fixtures; exclude exact calendar/payment computations and invented deadlines pending OD-005/014. | Such alternate judgment BLOCKED_SPEC; ordinary declared fixture remains reviewable. |
| GM notice certainty and literal control adoption; BR-018/020 and CT rows; TC-027/029, GM variants and controls | Preserve source-controlled POC text/trigger and OD-006 conflict; OD-011 must accept literal scope/version/channel. No wholesale wording approval or individual award guarantee. | Block unresolved certainty/literal judgments; preserve independently assessable once-only/order facts. |
| Formal benchmark fixture attribution; TC-006/009/027, TC-007, TC-004/028 and proposed TC-010 fixture | Use stated internal definitions; preserve original source discrepancies. Q12 repairs remain provisional and benchmark changes require reviewer approval; no workbook edit. | Internal fixture review possible; formal original-case certification pending named benchmark/QA review. |
| Broader semantic-consent/Tool compatibility or unspecified silence timeout; BR-014/015; supported handoff/ending profiles | Include separate semantic offer/answer evidence, existing supported re-offer behavior and no-consent-from-silence. Exclude invented timeout/disposition or repeated unavailable Tool calls. | Unsupported final disposition blocked; consent violations independently assessable. |
| Current served configuration and Q8 implementation conformance | Historical October 30 source reference only; known admission/checkpoint/correction/delivery conflicts retained. No runtime change, deployment identity or active-conversation result supplied. | Current conformance unverified; future missing environment evidence may be BLOCKED_ENV. |
| Real contact-center connection, backend submission/approval/payment, production reliability, numerical latency SLA or ASR cause | Outside this mock conversational candidate. Sampling, channel evidence and actual system outcomes need separate authority/evidence. | No assurance or causal claim from this package; current verdicts NOT_RUN. |

### Regression and evidence requirements for review

Use the existing [nine-group regression selection](DEFECT_GROUP_IMPACT_MATRIX.md#required-regression-evidence-for-any-new-closure-assurance)
and [Phase 4 cross-TC reconciliation](DEFECT_GROUP_IMPACT_MATRIX.md#phase-4-cross-tc-regression-reconciliation).
For each candidate assessment select the actual TC/VAR/qualified local profile,
applicable BR conditions, original DF findings, plausible impacts and negative
controls with an inclusion/exclusion reason. No group membership implies a failure
or a common technical cause; no family-level pass closes all cases.

Minimum future evidence: versioned target/fixture, actual entry/order/LOB/age and
reference context, channel, served configuration, merchant inputs and observed
responses, each required action/observation/consent, applicable terminal events,
source-linked assessment reasons, reviewer/date, and separate behavior/coverage.
For voice claims add synchronized recognized input, displayed/generated content,
audible playback/interruption timing and terminal trace. Sampling remains OD-015;
PB's five fresh high-risk runs is a proposal, not an adopted count or reliability
guarantee. No execution or evidence regrading occurs in this phase.

### Source and configuration references

| Reference | Candidate binding and limitation |
|---|---|
| Original workbook | Original containing ZIP and XLSX hashes in the preserved fingerprint table; XLSX `12e17ad51b6ee2053a4e2c56d3ae8b5ff56f544a6f9a1487dd274c05af5c797e`. Original 15 TC/18 DF cached records unchanged. |
| PLAN/PB | October 23 bundle and member fingerprints above; process/identity/semantic acceptance source, not approval of every new criterion. |
| Historical KB/Job/Flow/Tool/Code reference | October 30 export hash above, 17 POC-adopted articles/20 chunks and cited member ledgers in the immutable reviews. Formal KB approval pending; current Endpoint/revision binding unverified. No new broad contract investigation. |
| Internal engineering agreements | P2-ENG-DECISIONS-0.3; OD002-REVIEW-0.2; OD004-OD005-REVIEW-0.2; OD004-RECENT-GUIDANCE-REVIEW-0.2; OD007-OD010-OD009-REVIEW-0.2. Exact qualification/provenance records govern. |
| Pre-Phase-4 package | [Thirteen-member completed Q1–Q13 snapshot](../../reference/UC4_Problem2_OD007_OD010_OD009_Review_v0.2_2026-11-04.zip), SHA-256 `e1f354795a884368e396908b9cc11fc0eb594994e90e844a00de44444afb4546`. Prior histories/archives retained. |
| Current runtime/configuration | `configuration_id=null`, model/settings/current binding not captured for this candidate; no observed initialization, test execution or new closure evidence. |

### Reviewer ownership and candidate exit

Use the [consolidated worksheet](REVIEW_DECISION_WORKSHEET.md#phase-4-candidate-review-checklist)
to record reviewer name, authority, date, accepted/amended/excluded exact criterion
and JRN/BR/VAR/register version, rationale, residual blockers, channel and sampling.
Business/benchmark, QA, policy/UI, content/timing and voice/configuration ownership
are **unassigned**; roles identify needed review, not appointments.

**Readiness for review:** all 15 structural specifications; consistent conditional
BRs; preserved Q1–Q13 and original identities/history; explicit manifest/controls/
exclusions and two verdict axes. **Readiness for acceptance or execution:** requires
the applicable reviewer decisions and separately authorized configuration/evidence
work. This candidate never freezes Business Acceptance Baseline v1.0 automatically.
