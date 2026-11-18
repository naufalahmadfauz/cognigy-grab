# P2-AGENT-002 — outstanding opening/disclosure late or omitted

**Status:** verified captured REST/text deviation; two distinct manifestations, not a proven common technical cause. **Severity recommendation:** Medium, provisional: required identity/recording disclosure is affected, not merely cosmetic greeting style. No legal breach or audible-delivery conclusion is established.

## Exact observations

| TC / try | Run ID | Turn and original transcript evidence |
|---|---|---|
| TC-003 v0.1.3 / 2 | `c5614385-805b-41ec-ba3f-ce5ca285df60` | [T1, line 14][e3]: “Please tap the Orders tile and tell me when it opens.” Opening first appears at **T2**, line 40: “Hi, I'm your Grab AI Assistant, and I'll be assisting you today. Please note that this call will be recorded for quality assurance and training purposes.” |
| TC-004 v0.1.0 / 2 | `1e4d799b-d9e9-4cca-b357-7d010151dedf` | [T1–T4 Agent replies, lines 14–16, 35, 54, 73][e4]: T1 begins “Compensation for a cancelled order is usually approved within one to two business days…”; no greeting, identity or recording/purpose disclosure appears in any of the four captured replies. |

**Expected:** **BR-004**, [common journey opening contract](../JOURNEY_PILOT.md#common-contract) and [CT01](../BASELINE_MODEL.md) require the applicable outstanding opening once on normal utterance-first entry. TC-004 **M01** explicitly includes it; TC-003 uses the common opening contract, **not** its conditional M02 education. [Historical greeting-ownership instructions, lines 14–17][job], place the outstanding opening at the beginning of the first normal response.

**Actual:** TC-003 delivers it **late**, after navigation starts; it is not wholly absent or duplicated. TC-004 omits it throughout the observed run. This conclusion uses the declared fresh, normal, utterance-first fixture; internal greeting state and output ownership are unverified.

## Frequency, scope and related cases

- TC-003: **1/2 late**; TC-004: **1/2 omitted**. Combined **2/4 runs of those cases**, or **2/10 normal-entry opportunities** in the collection. Other first replies contain opening/disclosure.
- TC-003 try 1 and TC-004 try 1 are observed positive controls. TC-001/002, TC-005's observed prefix, and TC-025/026/028/029 are useful regression candidates—not newly confirmed failures. TC-003/005 are not authorized for another live run by this record.
- Related historical requirement: **DF-001/F01 / DG-001**. Preserve DF-001's original TC-001 Closed/Pass history and severity; do not reopen, renumber or overwrite it.
- TC-004's same run also supports [P2-AGENT-003](P2-AGENT-003.md); these are different requirements, **not two unique affected runs**. TC-003's later gate false positive is independent of this opening finding.

## Proposed acceptance/retest criteria

1. For normal utterance-first entry with no prior opening, deliver the applicable identity and recording/purpose disclosure before substantive journey guidance/education, once only. Preserve known merchant facts and the relevant next question/action.
2. On subsequent inputs, do not introduce a delayed new opening or repeat one already emitted. Check full response order manually; TC-003's selected gates do not screen this issue.
3. Retain separate already-emitted/native-empty and existing safety-precedence controls under their own reviewed fixtures and authorization; do not widen normal-entry rules into those cases.
4. Record fresh per-run configuration and business-versus-coverage verdicts. Closing text, `end_call`, ownership, exactly-once terminal and audio need separate evidence.

Internal POC finding under [scoped acceptance][scope]. No runtime change or retest performed.

[e3]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/TC-003/try-02/original-runner/20261106T213311533911Z-b3291c78df68/transcripts/run-001.md
[e4]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/TC-004/try-02/original-runner/20261106T213358896676Z-fd418102bfae/transcripts/run-001.md
[job]: ../../../flow/poc-correction-2026-10-29/01-job-instructions.txt
[scope]: ../../../reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md
