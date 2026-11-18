# UC4 handoff — stopped eight-run collection

Prepared 2026-11-16. Workspace: `%USERPROFILE%\cognigy-grab`; paths below are
workspace-relative unless marked `%TEMP%`.

## Execution gate

**STOPPED; nothing is running.** The latest collection stopped at slot 1 on HTTP
500; seven slots are deferred. Its result and review ZIP were delivered to the user.
Remain offline pending a new request: deferred slots and earlier risk acceptance
are **not continuing authorization** for execution or remediation.

## Continue in order

1. **Load scope.** Read `AGENTS.md`, `docs/agents/domain.md`, `GLOSSARY.md` and the
   applicable `docs/agents/runner.md` pointers. Done when the next user request is
   classified as evidence review, document work, implementation or live execution.
2. **Establish state.** In the latest evidence root below, read
   `REVIEW_MANIFEST.md` and `STOP_ENTIRE_COLLECTION.json`. Done when consumed versus
   deferred slots and pending assessments are accounted for; use original artifacts
   for exact identities/times rather than reconstructing them.
3. **Apply the gate.** Perform only the newly requested, authorized work. Live
   execution, replay, probes, configuration changes and remediation require fresh
   explicit scope. With no new task, stop after acknowledging the handoff.

Preserve historical evidence, original grades, stop markers and DF-001–DF-018.
Existing working-tree changes are user work, not cleanup targets. No commit/push,
baseline freeze or Excel update was performed by this work.

## Latest evidence

Root: `reports/problem2-pilots/eight-run-consistency/20261107T063633Z/`

| Reach when | Source under that root |
|---|---|
| Reporting slots, original grades, identities or timestamps | `collection-manifest.json` |
| Checking authorization, fixture hashes or local configuration provenance | `preflight.json`, `slot-plan.json` |
| Inspecting the failed request or actual replies | `slot-01-TC-001-run-01/`; original artifacts are inside its `original-runner/` directory |
| Sharing evidence or verifying preservation/integrity | `package-verification.json` and `UC4-EightRun-Consistency-20261107T063633Z-sanitized-review.zip` |

Original ERROR is technical, not a business verdict. Business and coverage
assessments for this collection remain pending. Local provenance does not prove
the served revision or effective model; GPT-5.6 remains owner-reported only.

## Branch references

**Findings or progression:** open only the relevant file under
`docs/problem2/follow-up-2026-11-07/`:

- `P2-AGENT-001.md`, `P2-AGENT-002.md`, `P2-AGENT-003.md`: evidence, qualifications
  and retest criteria. Keep P2-AGENT-001's source/acceptance conflict explicit.
- `TC-005-TRIAGE.md`: matcher diagnosis versus unverified UI behavior.
- `NEXT-CONSISTENCY-COLLECTION.md`: preparation choices. Its historical NO-GO
  preceded the later authorization and mandatory stop; it is not current permission.

TC-003/005 remain excluded from repeated live sampling pending separately
authorized progression work. TC-003's unopened-article fixture choice is settled.
The claimed updated Excel was unavailable locally; its update is user-reported.

**Business assessment:** consult `docs/problem2/JOURNEY_PILOT.md`,
`docs/problem2/BASELINE_MODEL.md` and
`reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md`.
Assess behavior separately from coverage; REST text does not prove terminal,
audio, authenticated UI or backend outcomes.

**Historical comparison:** these are separate collections, not resumed Batch 01:

| Evidence | Directory under `reports/problem2-pilots/` |
|---|---|
| Ten-run observations and independent assessments | `two-tries/20261106T212938Z/`: start with `summary.md`, `independent-review.json`, `collection-complete.json` |
| Original HTTP 502 incident | `batch-01/20261106T120439Z/` |
| Earlier separate HTTP 500 diagnostic | `TC-001/diagnostic-20261106T211407Z/` |
| First successful TC-001 observation | `TC-001/20261106T081600497108Z-55d027739384/` |

**Incident diagnosis:** causes remain unestablished. Private Cognigy/provider logs
were not accessed. Use saved correlation windows/IDs to request an owner-provided
sanitized log timeline; if logs are unavailable/expired, report that limit.
Repeated local reads cannot recover missing server evidence.

**Preservation tooling:** `%TEMP%\opencode\uc4-eight-run-20261107T063633Z.json`
is private snapshot data. Keep it and configuration contents out of shared evidence.
The `preflight-uc4-eight-runs.py`, `execute-uc4-eight-runs.py` and
`package-uc4-eight-runs.py` helpers in that directory are historical references,
**not commands to rerun**. Share only sanitized artifacts; exclude Endpoint
URLs/tokens, credentials and private configuration hashes.

## Suggested skills

Call the Skill tool when the next request matches:

- `diagnosing-bugs`: incident diagnosis; reproduction/instrumentation remains
  subject to the execution gate.
- `context7-mcp`: current Cognigy/HTTPX/API documentation.
- `grilling`: stress-testing decisions; `domain-modeling`: resolving terminology.
- `tdd`: separately authorized test-first implementation.
