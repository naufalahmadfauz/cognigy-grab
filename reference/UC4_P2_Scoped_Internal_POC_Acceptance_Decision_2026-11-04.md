# UC4 Problem #2 — Scoped Internal POC Acceptance Decision

**Decision status:** ACCEPTED — scoped internal POC criteria and fixture selection only  
**Declaration date:** 2026-11-04 (conversation date; exact signing timestamp not asserted)  
**Decision evidence:** Project owner’s explicit statement in this conversation, reproduced below.  
**Decision-maker:** Project owner (personal name and handwritten/digital signature not supplied).  
**Review capacities:** Internal POC Engineering Acceptance Reviewer **and** Internal POC QA Reviewer; temporary **self-review**, not independent QA.

## Explicit declaration

> I approve the scoped internal POC acceptance: Ready subcriteria of the 20 BRs, the 23-fixture selection while retaining the 21-fixture smoke subset, and the documented conditions, blocked judgments and exclusions. This is self-reviewed internal POC acceptance only. No baseline freeze or test execution authorization.

## Accepted scope

1. **Ready subcriteria** of the 20 business requirements for provisional evaluation in the isolated UC4 POC, with existing source, applicability and version qualifications. This is **not** blanket acceptance of all subcriteria of all 20 BRs.
2. **23 proposed assessment fixtures**: the 15 official benchmark targets (`TC-001`–`TC-010`, `TC-025`–`TC-029`) plus eight selected variants: `VAR-TC-003-A`, `VAR-TC-003-B`, `VAR-TC-003-C`, `VAR-TC-006-A`, `VAR-TC-027-C`, `VAR-TC-027-D`, `VAR-TC-027-F`, `VAR-TC-027-G`.
3. Preserve the **separate 21-fixture smoke/regression subset** (13 original targets, excluding `TC-005` and `TC-027`, plus those eight variants). The 21-fixture subset is not a replacement for the 23-fixture assessment selection.
4. Preserve all previously documented **Conditional** bounds, **Blocked** judgments, **Excluded** outcomes and their rationale. No outstanding conditional decision, fixture conflict, controlled wording or unsupported business-policy outcome is silently approved.

## Referenced review objects

- `P2-BASELINE-CANDIDATE-0.1`
- `P2-JOURNEYS-0.4`
- `P2-CONTROLLED-TEXT-0.1`
- `REVIEW_DECISION_WORKSHEET.md` in user-provided `problem2(6).zip` — source sign-off sheet before this explicit acceptance.

## Not authorized or established

- **Baseline remains NOT FROZEN.** No freeze approval is given by this decision.
- **Test execution remains NOT AUTHORIZED.** No live Cognigy/Endpoint requests are authorized by this decision.
- **Behavior = NOT_RUN; coverage = NOT_RUN.** No outcome has been measured or certified.
- No Cognigy Flow, Agent Job, Tool, Code, Knowledge Store or Python runner change is authorized.
- Formal Grab business-policy and benchmark approval remain pending.
- Independent QA validation remains deferred; dual-role self-review must be disclosed in downstream reports.
- Exact authenticated UI behavior, incomplete executable fixture bindings, configuration identity, recording/channel and sampling requirements, controlled-text adoption and unsupported recovery/payout outcomes require separate resolution or explicit exclusion.
- A personal signature was not supplied; the explicit chat declaration is decision evidence, not a fabricated signature.

## Next gate: execution-readiness only

1. Propagate this decision and its exact limited scope into the project’s existing sign-off sheet and version history; do not overwrite historical source records.
2. Establish a read-only fingerprint of the **currently served** isolated POC Cognigy Flow / Agent Job / relevant Tool and Code configuration and compare it with the documented historical export; record differences.
3. Map the approved **23 fixture identities** to executable test inputs, making unsupported bindings and unresolved fixture preconditions visible. Preserve the distinct 21-fixture subset.
4. Propose a test channel, evidence capture requirements, sampling/repetition plan and observation/checkpoint graders. Do not change the existing runner without separate authorization.
5. Return a clear **GO / NO-GO execution-readiness report** with blockers. Obtain a separate explicit user authorization before any live run, prompt patch or baseline freeze.

**Scope-control statement:** This record authorizes acceptance of scoped *evaluation criteria and fixture selection*, not evaluation results, implementation changes, execution or release.
