# TC-005 — offline article-navigation triage

**Conclusion:** confirmed **regex/wording mismatch at the recorded stop**; not a demonstrated Agent navigation violation or ambiguous-merchant-observation failure. **Actual UI transition remains unverified.** This sharpens the prior blanket “inconclusive route” assessment without changing historical automated FAILs or claiming end-to-end PASS.

## Original evidence

TC-005 v0.1.0, **T4 in both runs**:

| Try | Exact run ID | Original sanitized transcript |
|---|---|---|
| 1 | `de767e1b-ef7f-4316-8c57-a68d67efb6c2` | [T4, lines 67–86][e1] |
| 2 | `55912210-1bd9-446c-9c31-77073951824c` | [T4][e2] |

Identical reply:

> Tap Request for compensation inside the order. This will open the Help Centre article Report a payment dispute. Scroll down until you find the form. Is the form visible?

Only `article` was missing from `request-entry-segment`; `wait-for-visible-form` passed. Both runs stopped at **4/7 turns**; T5–T7 were **SKIPPED, zero attempts**.

## Contract and matcher diagnosis

- [JRN-TC-005 M04–M07](../JOURNEY_PILOT.md#jrn-tc-005), **BR-006/009/010/012/013**, permit grouped request entry after observed blank status and retained intent: present link → article → scroll → ask form visibility; completion must await its actual confirmation. The reply describes that segment without premature details/evidence/submission instructions.
- The [unchanged fixture, line 37][fixture] permits `open [the] [article/result/link] Report a payment dispute`, but not the intervening **“Help Centre”**. [Matching code][matching] searches unanchored regex spans; normalization does not delete these words. By static inspection, descriptive “This will open the article Report…” could match while imperative “Open the Help Centre article Report…” could fail. **The mismatch is not simply descriptive versus imperative wording.** No test was executed here.
- T4's merchant report is clear: relevant order visible/details open, explicitly blank status, retained review intent, request link visible. It does **not** establish the post-tap landing screen. The future T5 “opened…” statement was never sent and proves no navigation completion.
- [Historical App request instructions, lines 131–132][job], describe the tap as opening the named Help Centre article. That supports the destination description, not authenticated current UI behavior. Whether another article-opening click is required remains unknown. TC-003's settled unopened-article fixture is a separate declared state, not a TC-005 UI fact.

## Disposition and readiness

High confidence in the matcher diagnosis and clear T4; no verified real UI transition. **No confirmed Agent defect is registered from these stops.** Preserve both original FAILs and partial-coverage verdicts; do not fabricate form visibility, submission or finish through regrading.

Keep TC-005 out of repeated live sampling. Next step is offline review of acceptable TC-005 route descriptions plus omitted-article and premature-completion counterexamples. Any versioned matcher/fixture correction, its offline verification and a fresh execution require **separate authorization**; none was performed. Business requirements remain unchanged.

[e1]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/TC-005/try-01/original-runner/20261106T213413761440Z-08950a31a2b3/transcripts/run-001.md
[e2]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/TC-005/try-02/original-runner/20261106T213429702985Z-8dec08991b4a/transcripts/run-001.md
[fixture]: ../../../scenarios/problem2-pilots/candidates/tc-005-v0.1.0/P2-TC-005-001.yaml
[matching]: ../../../uc4_runner/assertions.py
[job]: ../../../flow/poc-correction-2026-10-29/01-job-instructions.txt
