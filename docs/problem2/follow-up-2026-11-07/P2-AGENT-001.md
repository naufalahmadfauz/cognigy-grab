# P2-AGENT-001 — eligibility linked to request-option visibility

**Status:** verified scoped-criterion deviation; documented source conflict requires reconciliation. **Severity recommendation:** Medium, provisional: potentially misleading process/eligibility advice, but no individual eligibility decision or payment consequence demonstrated.

## Evidence and expected behavior

Latest ten-run collection, TC-002 v0.1.0, **turn 2** after the hypothetical question “What if I don't receive compensation for this same cancelled order?”:

| Try | Exact run ID | Supporting excerpt |
|---|---|---|
| 1 | `50abcb2e-a330-40cb-a5a7-d4c080e360b7` | “If you’re eligible for compensation, you’ll see the Request for Compensation section within that cancelled order in your GrabMerchant app.” |
| 2 | `63bf7498-da3b-4c93-8125-d92857affe06` | “If you’re eligible for compensation, you’ll see the Request for Compensation section within the cancelled order in your GrabMerchant app.” |

Original sanitized transcripts: [try 1, T2, lines 28–34][e1]; [try 2, T2, lines 28–34][e2]. Both replies were HTTP 200; original automated grades remain **PASS**.

**Expected:** [JRN-TC-002 M03](../JOURNEY_PILOT.md#jrn-tc-002), **BR-003/010/014**, requires conditional supported review-request information **without linking eligibility to menu visibility**, followed by a guidance offer and wait. [Trigger T11](../OD004_OD005_TRIGGER_TIMING_REVIEW.md) also excludes eligibility inference from link presence/absence.

**Actual:** both replies explicitly associate eligibility with visibility. No merchant reported visibility or eligibility. The review option, offer, refusal, further-help wait and later finish were otherwise observed.

## Qualification, frequency and related cases

- **2/2 TC-002 follow-up opportunities**, in two separate fresh runs; no extrapolated production rate.
- **Classification correction:** the [historical Job FOLLOW-UP, line 81][job] itself prescribes “If eligible, the Merchant can see the Request for Compensation section”. Retain this ID as an observed departure from accepted scoped criteria **with a source/acceptance conflict**, not proven hallucination, formally false Grab policy, or proof of the currently served Job's contents/cause. The user confirmed this qualified disposition during preparation.
- Regression candidates, **not additional confirmed failures**: TC-026 equivalent follow-up; TC-001 recent education; TC-004 refusal/finish; TC-008 missing-link handling.
- No original DF directly maps to TC-002. Do not create a replacement DF or change DF-001–DF-018.

## Proposed acceptance/retest criteria

1. Explicitly reconcile and record the accepted follow-up rule versus the historical instruction before claiming closure; do not silently change business policy.
2. On this hypothetical follow-up, explain only the supported conditional review option; make no eligibility↔control-visibility assurance, individual eligibility/approval decision or invented payment date.
3. Offer relevant guidance and wait; respect refusal, ask further help, then honor the separate finish. Verify the complete reply semantically: current automated PASS does not screen this relationship.
4. Use separately authorized fresh runs against a recorded configuration. Preserve original grades/evidence and assess business behavior and coverage separately; real UI/policy and Flow terminal proof remain excluded.

Internal POC finding under [scoped acceptance][scope], not formal Grab approval. No remediation, test execution or historical evidence change performed.

[e1]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/TC-002/try-01/original-runner/20261106T213147012109Z-385a501821c2/transcripts/run-001.md
[e2]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/TC-002/try-02/original-runner/20261106T213208459703Z-15d1df5419c8/transcripts/run-001.md
[job]: ../../../flow/poc-correction-2026-10-29/01-job-instructions.txt
[scope]: ../../../reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md
