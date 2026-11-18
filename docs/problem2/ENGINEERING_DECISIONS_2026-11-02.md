# UC4 Problem #2 — Round 1 Engineering Decision Record

**Record version:** `P2-ENG-DECISIONS-0.3`  
**Recorded:** 2026-11-02 (Asia/Jakarta)  
**Authority:** Explicit project-side user agreement in the conversation, **internal POC test-design direction only**. Named decision-maker's official role and sign-off authority are not recorded here.  
**Formal Grab benchmark/policy approval:** **NOT obtained**.  
**Agent tests / flow modifications:** **NONE**.  
**Acceptance baseline:** **NOT FROZEN**.  

This file captures the four agreements reached sequentially in the conversation after the `P2-DRAFT-0.2` review. It is a **decision overlay**, not a change to Grab's original Excel, defect history, or a claim that every criterion in the pilot journeys is approved. Preserve earlier contradictions and their source locations as historical specification evidence.

## Engineering agreements

| ID | Internal POC decision agreed | Scope and unresolved authority |
|---|---|---|
| **OD-001** | For **TC-006**, use the **merchant declines the retry** as the provisional original target, leading to supported non-retry/soft-close handling. Keep **merchant accepts retry and succeeds** as `VAR-TC-006-A`; keep an accepted-but-failed retry as a separate proposed variant. Role confirmation is not retry consent; retry consent is not transfer consent. | **Engineering-agreed test fixture**. The original `WB:S!D9` versus `E9` contradiction remains; a named benchmark owner must approve which branch formally defines the official TC. Linked BR-012/014/015, JRN-TC-006. |
| **OD-008** | For **TC-009**, use **Portal submission-only** as provisional target: form absent → authorized access / one offered-and-accepted retry → observed retry failure → separate offer of a person → explicit consent → mock transfer. Do not implement a fabricated GrabFood Portal status route. | **Engineering-agreed test fixture**. Preserve conflicting `WB:S!D12` Portal-status path versus `E12` submission-only dialogue. Named benchmark review still required. Linked BR-009/011/012/015, JRN-TC-009. |
| **OD-003** | For **TC-027**, preserve merchant's App selection, explicitly explain that GrabMart compensation-status review uses a computer Portal, **confirm Portal readiness**, and only then give Finance → Transactions status navigation. Keep established guidance style/preferences; handle unavailable Portal through only supported recovery, with required consent. Continue to submission only as appropriate to observed status and intent. | **Engineering-agreed POC transition behavior**; original `WB:S!E16/F16` mismatch remains for formal benchmark review. Linked BR-005/008/015, JRN-TC-027; compare TC-029. |
| **OD-015** | Adopt **staged review governance**: engineers draft BR/JRN/DG; project-side owner reviews provisional POC interpretations; named benchmark/business and QA reviewers decide applicable acceptance requirements; unresolved formal Grab policy stays flagged; freeze only a scoped reviewed version; authorize baseline execution separately. | **Review process agreed**, **reviewer names and QA owner still unassigned**. This does not appoint the user as Grab policy approver or make unsigned criteria authoritative. No automatic live-test approval. |

## Status semantics

- `ENGINEERING_AGREED_POC`: a test-design direction has user agreement for internal planning, **not** independent Grab policy authority.
- `BENCHMARK_CONFLICT_RETAINS`: a conflicting original workbook entry is kept unchanged and requires named review for external TC certification.
- `BUSINESS_POLICY_UNKNOWN`: policy/UI/role wording issues linked to the journey remain unresolved.
- `NOT_RUN`: no new Agent execution or pass is implied by recording these decisions.

For the purpose of drafting **internal** fixtures, OD-001, OD-008 and OD-003 can guide the next review pass. Their original TC benchmark acceptance remains **pending authorized stakeholder adjudication**. OD-015's governance is agreed as a process, while named owners and baseline sign-off remain outstanding.

## Next gate — do not skip

1. **Identify reviewers**: benchmark/business owner and QA reviewer; log identity, role, decision date and scope. The user agreed to the process, not to an unprovided roster of approvers.
2. **Review three pilots** `JRN-TC-003/006/027` and the related `TC-009` fixture under the four engineering directions, checking source-backed branch conditions and unresolved decision IDs.
3. **Resolve high-impact remaining decisions** before locking their corresponding requirements: in particular `OD-002` (Auto approved semantics), `OD-004` (education triggers), `OD-005` (date/timing), `OD-006` (partial-compensation wording), `OD-007` (conditional History recovery), `OD-010` (role reminder/retry), `OD-011` (controlled text), `OD-014` (policy/UI).
4. Publish a **scoped, reviewed Business Acceptance Baseline** once its applicable BR and JRN fixtures have owner decisions. **Only then** snapshot the served isolated POC Agent and compare baseline behavior. Keep behavior correctness and targeted branch coverage as separate verdicts.
5. Before implementing any Agent change, determine a **BR-led regression set** from the defect impact matrix. Preserve directly reported versus plausible TC effects. No auto-declaration that nine DGs are proven root causes or that 18 historical DFs are currently open.

## Relationship to source drafts

- [OPEN_DECISIONS.md](OPEN_DECISIONS.md) retains the **source conflicts** and remaining external review frontier.
- [REVIEW_DECISION_WORKSHEET.md](REVIEW_DECISION_WORKSHEET.md) includes an internal-agreement snapshot and still reserves a blank sign-off register for authorized reviewers.
- [JOURNEY_PILOT.md](JOURNEY_PILOT.md) remains a proposed normative draft; only the bounded fixture choices above have internal agreement.
- [BASELINE_MODEL.md](BASELINE_MODEL.md) remains a **model**, not executed Agent baseline.
