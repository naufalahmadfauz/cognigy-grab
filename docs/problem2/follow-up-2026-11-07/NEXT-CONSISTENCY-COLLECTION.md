# Proposed next consistency collection — eight runs

**PROPOSED / NO-GO FOR EXECUTION.** User-confirmed preparation choices, 2026-11-07: **unchanged-configuration characterization**, not post-fix acceptance retesting; shared-runtime fail-fast. Findings remain open. No execution, changes, probes or freeze authorized.

## Evidence and scope corrections

The [latest ten-run collection][latest] did not resume/replace original Batch 01. This proposal contains three per-scenario **batches**, consistent with the [glossary](../../../GLOSSARY.md).

| Scenario | Existing observations | Proposed fresh runs |
|---|---|---:|
| TC-001 | 3 successful scoped text observations; **also HTTP 502 and separate HTTP 500 technical-error attempts**, neither a business verdict | 2 |
| TC-002 | 2 script-complete observations; both automated PASS, both with [P2-AGENT-001](P2-AGENT-001.md)'s qualified scoped deviation | 3 |
| TC-004 | 2 script-complete observations; one scoped business failure supports [P2-AGENT-002](P2-AGENT-002.md) and [003](P2-AGENT-003.md), not two failed runs | 3 |

**Eight fresh runs; maximum 28 merchant requests.** Order: TC-001 ×2 → TC-002 ×3 → TC-004 ×3, sequentially, reviewing each before the next slot. The first run counts—no extra health probe. An errored slot is consumed, never replaced.

All-complete arithmetic gives five historical complete observations per TC, **not five business passes or proven same-revision observations**. Keep configuration cohorts separate; never pool pre/post-fix results as acceptance evidence.

**Exclude TC-003/005:** prefixes are 13/14 and 9/14, and 4/7 twice. Resolve progression interpretation and separately authorized versioned corrections/offline verification first. See [TC-005 triage](TC-005-TRIAGE.md); TC-003's unopened-link choice stays settled.

## Existing fixture bindings

All are v0.1.0, **ungated**; read-only byte hashes match the [saved preflight][preflight]. No validation, dry-run or tests were rerun.

| TC / turns | Exact unchanged fixture | YAML SHA-256 |
|---|---|---|
| TC-001 / 2 | [P2-TC-001-001.yaml][f1] | `7f6df486cb31fa462519b08d1a36b06659503677e9e20a7b991a7b228e5f8cca` |
| TC-002 / 4 | [P2-TC-002-001.yaml][f2] | `0b9acd70b8e52dc9e511a808d0a6acda0557fc395264aba662747adadca3f342` |
| TC-004 / 4 | [P2-TC-004-001.yaml][f4] | `548b0c3ff71cce8763eaf31e20b24751736915b8d7764a7e2fd15051b25a99f2` |

## Readiness conditions still requiring review

- Confirm **Test → UC4_KB_AGENT_POC_v03** and currently served resource/model identity from owner evidence. Local settings do not prove unchanged deployment; GPT-5.6 remains owner-reported. No administration requests made here.
- Review unresolved 502 **and 500** disposition. Latest 50/50 HTTP 200 replies do not prove recovery. Preserve [original stop][stop] and [500 capture][http500].
- Reconfirm fixture/channel/reference scope: actual UTC/MYT initialization, ages 1/14 days, no injected clock; retain TC-004's provisional Q12 qualification and manual TC-002 review.
- Reconfirm saved settings/provenance: Test Mode on, concurrency 1, 60s **operation/inactivity** timeout, 0.5s turn/1s run pacing, retries 0, raw retention off. No implicit logging/capture changes.
- Obtain fresh authorization for **eight runs plus this stop policy**; older permissions do not carry forward. Updated Excel is user-reported, not available locally; no workbook changed.

## Confirmed proposed shared-runtime stop rule

**First technical error stops the entire collection:** non-2xx HTTP (including 5xx/429/redirect), timeout/network failure, invalid/empty/unsupported reply, identity/security/configuration mismatch, incomplete evidence or interruption. Preserve the prefix/stop reason; defer remaining slots. **No retries, replay, session continuation, replacement, probes or automatic resume.** Require review and new authorization.

Business deviations alone may continue within authorized slots; healthy ungated scripts retain their refusal/finish sequence. The [runner](../../ARCHITECTURE.md#rest-behavior) stops only the affected conversation: enforce the global rule by dispatching/reviewing **one fresh slot at a time**, not all repetitions blindly.

## Per-run evidence and assessment

Each slot: fresh run/user/session identities/client, separate artifacts, fixture/runner/configuration provenance, UTC/MYT times, complete sanitized inputs/replies, HTTP status/timing, trace IDs, attempted/skipped turns and finalized status. No credentials; raw retention off limits diagnosis.

Preserve grades; independently record **business** and **target-branch coverage** verdicts against each journey. Sent scripts do not establish milestones. REST goodbye does not prove Flow ownership, `end_call`/hangup, exactly-once terminal or audio. Native-empty/UI/backend/payment claims remain excluded. No automatic Excel update or defect clearance.

**Await review and separate execution authorization.** Historical evidence/DFs, requirements, fixtures, runner and Cognigy remain unchanged. [Scoped acceptance][scope] is not formal approval or execution permission.

[latest]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/summary.md
[preflight]: ../../../reports/problem2-pilots/two-tries/20261106T212938Z/preflight.json
[stop]: ../../../reports/problem2-pilots/batch-01/20261106T120439Z/STOP_ENTIRE_BATCH.json
[http500]: ../../../reports/problem2-pilots/TC-001/diagnostic-20261106T211407Z/execution-capture.json
[f1]: ../../../scenarios/problem2-pilots/candidates/tc-001-v0.1.0/P2-TC-001-001.yaml
[f2]: ../../../scenarios/problem2-pilots/candidates/tc-002-v0.1.0/P2-TC-002-001.yaml
[f4]: ../../../scenarios/problem2-pilots/candidates/tc-004-v0.1.0/P2-TC-004-001.yaml
[scope]: ../../../reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md
