# P2-AGENT-003 — TC-004 premature education and guidance setup

**Status:** verified scoped intent/dependency deviation. **Severity recommendation:** Medium, provisional: information-only entry advances toward guidance without clear acceptance; subsequent refusal is respected. No actual transfer, submitted request or payment impact demonstrated.

## Exact reproduction evidence

TC-004 v0.1.0, **try 2**, run `1e4d799b-d9e9-4cca-b357-7d010151dedf`; [original sanitized transcript][e4]:

- **T1, lines 11–16:** merchant supplies only “I'm a GrabFood merchant in Malaysia. The order was cancelled 14 days ago.” Agent immediately gives the qualified compensation timeline, then asks: “Would you like me to show you how to check the compensation status for that order?” The missing-goal question never occurs.
- **T2, lines 32–35:** merchant: “I want to know about the compensation status for that order.” Agent: “Are you on the GrabMerchant app, or the GrabMerchant portal on a computer?”
- **T3/T4, lines 51–73:** explicit refusal is respected, further help is asked, and the separate finish receives goodbye text.

**Expected:** [JRN-TC-004 M01 → actual inquiry → M02 → offer response → M03](../JOURNEY_PILOT.md#jrn-tc-004), [T02/T05](../OD004_OD005_TRIGGER_TIMING_REVIEW.md), and **BR-001/002/003/005/013/014**: establish the genuinely missing goal and wait; then applicable qualified GF education, existing-prepared-food-photo reminder, one guidance offer and wait. Collect walkthrough preferences only after a supported request/clear acceptance. The TC-004 decline/finish fixture remains Q12-provisional within scoped acceptance.

**Actual/correction:** timeline and offer are **early**, not absent from the whole conversation. The existing-photo reminder is absent throughout. T2 is **premature preference intake without clear guidance acceptance**—not proof of an internal consent flag, an actual walkthrough, or an unconsented transfer. Opening omission is recorded separately in [P2-AGENT-002](P2-AGENT-002.md).

## Frequency and regression scope

- **1/2 TC-004 runs**; try 1 supplies the correct entry/education/offer sequence. Four sent messages do not establish required M01/M02 coverage in try 2.
- Regression candidates, **not additional confirmed failures**: TC-005/029 older elicited dual goal; TC-028's different optional-offer trigger; TC-003/027 upfront direct intent; TC-001/025 recent education; TC-002/026 declined guidance. These are not extra authorized executions.
- Historical overlap: **DF-006/F01–F02** and **DF-018/F01**. Preserve DF-018's owner-resolved status and beyond/within source discrepancy. DF-005 repetition/disconnection was not reproduced. No DF is replaced or reopened.

## Proposed acceptance/retest criteria

1. With the unchanged older age-only entry, ask the missing goal and wait; do not prematurely educate, offer guidance or collect preferences.
2. After the actual general status inquiry, deliver the qualified GF education and conditional existing-photo reminder, offer relevant guidance, then wait. Fix sequencing rather than prescribing redundant timeline repetition after an already-bad prefix.
3. Do not interpret this information-only reply as guidance acceptance. After explicit refusal, stop guidance, ask further help and wait; close only on the later finish.
4. Assess both process correctness and actual milestone coverage from complete fresh transcripts, preserving original grades and separate [opening finding](P2-AGENT-002.md). Any post-fix closure requires separately authorized configuration-scoped retesting.

Internal POC finding under [scoped acceptance][scope], not a formal policy decision or proven shared root cause. No change/retest performed.

[e4]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/TC-004/try-02/original-runner/20261106T213358896676Z-fd418102bfae/transcripts/run-001.md
[scope]: ../../../reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md
