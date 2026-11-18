# UC4 Problem #2 — execution readiness

**P2-EXECUTION-READINESS-0.1 · assessed 2026-11-05 · NO-GO**

Scoped internal POC acceptance is [recorded](REVIEW_DECISION_WORKSHEET.md#recorded-scoped-internal-poc-acceptance):
Ready subcriteria, **23 assessment fixtures**, separate **21-fixture smoke subset**,
and retained conditions/blockers/exclusions. This is project-owner engineering/QA
**self-review**; independent QA is deferred and formal Grab approval remains pending.
**Execution NOT AUTHORIZED; baseline NOT FROZEN; behavior NOT_RUN / coverage NOT_RUN.**

| Readiness gate | Finding |
|---|---|
| Scoped criteria and selection | Accepted; outstanding conditional fixture/text choices are not silently resolved. |
| Currently served isolated POC configuration | **Unverified.** No current administration capture/binding available; `configuration_id=null`. |
| Complete reviewed executable bindings | **0/23.** Existing scenarios provide partial content/navigation only. |
| Opening, terminal and voice evidence | Native-empty entry unsupported by the runner; terminal ownership and synchronized audio need external capture. |
| Channel, reference date and sampling | Proposals below; exact bindings and decisions remain outstanding. |

The owner confirmed completion of this report with missing current evidence made
explicit. **NO-GO reflects missing technical/evidence prerequisites as well as
separate execution authorization; it does not rescind scoped acceptance.**

## 1. Configuration verification and comparison

### Verified historical reference; current deployment unverified

Recomputed the October 30 export SHA-256 and **22 documented node/chart member
fingerprints**, plus the Job instruction hash, against the [existing source ledger](BASELINE_MODEL.md#fingerprints),
[Tool/Code ledger](OD004_OD005_TRIGGER_TIMING_REVIEW.md#static-tool-code-and-wiring-ledger)
and [terminal ledger](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md#terminal-member-ledger-and-wiring).
All match. This verifies historical source integrity, not the served configuration.

Source: `C:\Users\Nau\Downloads\Package-Naufal_2026-10-30_06-38-33.zip`,
created `2026-10-30T06:38:40.267Z`, package Cognigy version **2026.22.2**;
SHA-256 `e92afdf8d41c5a348e65e18e0a1cad77f827d26dab5c6d3fe136d3439c1a8a1f`.
Its 77 members include one Flow, 31 nodes, one Agent, one Knowledge Store, 17 sources
and 20 chunks. **No Endpoint, Snapshot or LLM-provider definition is included.**

| Resource | Verified October 30 identity/settings | Current-versus-historical result |
|---|---|---|
| Flow / chart | `UC4_KB_AGENT_POC_v03`; stable ref `17f129de-69b3-4828-bc4f-0c7d19ef41ce`; Flow member `flow/6ae43b6f90878ce305636d7f`; chart `chart/6ae43b6f90878ce305636d80`. | Current Flow/revision/entry and isolation unverified. |
| Agent Job | `Grab Cancelled Order Compensation`; stable ref `e38e5029-d515-4002-ad03-dd99b0eb821e`; `nodeData/6ae43b6f90878ce305636d97`; instructions `/localizedData/0/config/instructions`. | Current Job/instructions unverified. |
| Six local Tools | `resolve_order_age`, `start_guidance`, `update_guidance_checkpoint`, `end_call`, `transfer_to_live_agent`, `escalate_safety`; stored definitions and associated Code/Resolve wiring. | Current definitions/conditions/wiring unverified; no Tool invoked. |
| Relevant Code | Initialize session; Capture first-input LOB; Proactive greeting once; Record greeting emission; resolve_order_age; Validate guidance checkpoints; Mock Transfer; Safety Mock Transfer. | Current Code and terminal path unverified; no Code executed. |
| AI Agent | `Grab AI Assistant`, ref `3c1b0294-6016-4b52-8478-afd6cc05a434`; `aiAgent/6ae43b7090878ce305636e12`; points to the store below. | Current Agent, voice settings and shared callers unverified. Historical October 29 evidence shows this Agent/store were shared with `[MAIN]`. |
| Knowledge | `UC4_KB_POC_v03_TEST`, ref `786b7a11-913c-4ec0-8a4e-e48352921d78`; `knowledgeStore/6ae43b7090878ce305636de3`; 17 v0.3.0 articles / 20 chunks. Job knowledge enabled; Agent knowledge disabled for this Job; on-demand search, generated search prompt, top-K 3. | Current store/content/index/model bindings and retrieval unverified. Static content match is not retrieval evidence. |
| Model/settings | Job provider ref `default`, API `latest`, temperature `0.3`, max tokens `500`, timeout `8000` ms; memory inherited. | Neither `default` nor `latest` identifies an effective model/version. Current provider/model, overrides and inherited settings missing. |
| Endpoint | October 30 has none. [October 29 export/history](../../flow/UC4-PORTAL-DIAGNOSIS-2026-10-29.md#exported-target-and-isolation-verification) recorded REST `Test` targeting the POC Flow, active, mocking off; its operator confirmation is historical. | Current Endpoint-to-Flow/revision/Snapshot, entry, transformer/mocking and connection-override settings unverified. |

Additional exact historical member hashes (whole member bytes, not live IDs):

| Member | SHA-256 |
|---|---|
| `flow/6ae43b6f90878ce305636d7f` | `6026decafbbc3a62492be127e5f291dfa47232a87b391b1f59476db2178494c9` |
| `aiAgent/6ae43b7090878ce305636e12` | `ea93c9813b85860f35b5ab2922b1991f4974e623499202d82610529e12bcca99` |
| `knowledgeStore/6ae43b7090878ce305636de3` | `ba5880ea0b80c1dbcf13d6ba7f519dc97a44745ac9a03e98278250a0447ce5d3` |
| Job instructions, original UTF-8 | `d89731bb49f09959e0c9c35550cb0b9fa71fa03a88295916887672c20390d860` |

**Historical comparison only:** joining the October 29 06:47 export and October 30
by stable node references finds 3/31 POC node configurations changed: Job
`instructions`, proactive-greeting `code`/`transpiled`, greeting-recorder
`code`/`transpiled`. The other 28 match. All 17 source references and compared
name/metadata/data/chunk-count fields match; all 20 chunk references and compared
text/data/disabled/order fields match. This comparison does not certify embeddings
or any current deployment. **Current-versus-baseline differences cannot be computed.**

**Known historical Q8 discrepancies remain:** beyond-only `start_guidance`,
beyond-only GF checkpoint validation, correction-driven deletion of otherwise
compatible progress, and `educateDelivered` set on selection rather than actual
output. The [qualified Q8 review](OD004_RECENT_GUIDANCE_CONTRACT_REVIEW.md#2-source-grounded-static-trace)
governs their scope; a current capture must show whether they remain. No fix is
inferred from acceptance or from these older-target fixtures.

### Evidence needed to establish the current binding

No Cognigy administration tool/resource or authenticated management connection was
available. Local configuration has a conversation URL; variable presence was
checked without recording its value. No conversation Endpoint was contacted.

Obtain a timestamped, sanitized current export/configuration capture and Endpoint
settings showing tenant/project and stable resource IDs; selected Flow, explicit
current-project revision or Snapshot, entry point, locale, enabled/mocking status,
transformers, connection overrides and effective model/settings. Include linked
Agent/Job/Tools/Code/Knowledge and shared-dependency references; hash the exact
captured bytes and compare by stable ref, not package-local ID. Record missing
dependencies rather than inventing a complete isolation claim. Source configuration
evidence can be inspected read-only; actual initialization/behavior remains future
run evidence. Do not include Endpoint tokens, API keys or connection credentials.

Current [Endpoint documentation](https://docs.cognigy.com/ai/agents/deploy/endpoints/overview)
distinguishes Flow, Snapshot and connection overrides; [Packages](https://docs.cognigy.com/ai/platform-features/packages.md)
contain selected resources/dependencies. [Test Mode](https://docs.cognigy.com/ai/agents/deploy/endpoints/test-mode.md)
processes real messages; it is neither an offline check nor proof of isolation or
revision selection. Public docs explain the required evidence, not this tenant's state.

## 2. Mapping all 23 selected fixtures

**Every row has no complete reviewed executable binding.** The paths below supply
reuse candidates only; concatenating separate runs cannot make one journey.
Original target and selected variant meanings remain in [P2-JOURNEYS-0.4](JOURNEY_PILOT.md#catalog-index-and-version-scope).
`F` marks unresolved exact fixture/refinement acceptance; `U` marks an unsupported
dependent outcome; `E` marks native-empty entry outside runner support. All rows
also need current configuration, executable bindings and external terminal/voice
evidence where claimed. Other supported prefixes are **conditionally testable after
those prerequisites**, not runnable or passed now.

| Reuse alias | Existing scenario and version |
|---|---|
| TF / TM | [KB-GF-TIMING-AGE-001](../../scenarios/kb-coverage/KB-GF-TIMING-AGE-001.yaml) / [KB-GM-TIMING-AGE-001](../../scenarios/kb-coverage/KB-GM-TIMING-AGE-001.yaml), both v0.1.1; direct timing questions, then a different order. |
| SF / SM | [KB-GF-STATUS-001](../../scenarios/kb-coverage/KB-GF-STATUS-001.yaml) / [KB-GM-STATUS-001](../../scenarios/kb-coverage/KB-GM-STATUS-001.yaml), both v0.1.1; grouped status content. |
| PF | [GM-PORTAL-STATUS-FULL-001](../../uc4_runner/scenarios/GM-PORTAL-STATUS-FULL-001.yaml) v0.2.1; one-by-one Portal instructions ending at the status question. |
| AF / AM | [KB-GF-SUBMIT-001](../../scenarios/kb-coverage/KB-GF-SUBMIT-001.yaml) / [KB-GM-SUBMIT-001](../../scenarios/kb-coverage/KB-GM-SUBMIT-001.yaml), both v0.1.1; grouped entry/completion advice, no submission report/finish. |
| P / L | [KB-PORTAL-SUBMIT-001](../../scenarios/kb-coverage/KB-PORTAL-SUBMIT-001.yaml) / [KB-GF-MISSING-LINK-001](../../scenarios/kb-coverage/KB-GF-MISSING-LINK-001.yaml), both v0.1.1; GM grouped access question / GF grouped accepted fallback. |
| EF / EM | [KB-GF-EVIDENCE-001](../../scenarios/kb-coverage/KB-GF-EVIDENCE-001.yaml) / [KB-GM-EVIDENCE-001](../../scenarios/kb-coverage/KB-GM-EVIDENCE-001.yaml), both v0.1.0; factual no-photo handling only. |

Below, inputs/checkpoints are required drafting specifications, **not adopted scripts**.
“Finish” is a separate explicit no-further-help response after applicable further-help
handling. “Submission” is the merchant's report, not verified backend acceptance.

| Fixture | Partial reuse | Required merchant inputs / observation sequence | Principal missing binding or conditional hold |
|---|---|---|---|
| TC-001 | TF facts | GF, cancelled 1 day ago, age-only entry → actual education/reminder → further help → finish. | TF instead asks timing directly; **E** for proposed native-empty opening allocation. |
| TC-002 | TF facts | Recent GF education → nonreceipt follow-up → guidance offer → explicit decline → finish. | Entire follow-up/refusal/ending chain absent. |
| TC-003 | SF/AF/EF | Older GF upfront dual goal; App/one-by-one → visible order, blank status, retained review goal → link/article/scroll/form → authorized submission → finish. | Existing grouped/approved-status slices omit full blank-status target and completion. |
| TC-004 | TF facts | Older GF age-only → elicited general status inquiry → education/photo reminder/required offer → decline → finish. | **F:** Q12 explicit decline/finish repair; no full elicited-entry script. |
| TC-005 | TF/SF/AF | Older GF age-only → elicited dual goal → education/offer/acceptance → App/grouped → blank status → form/submission → finish. | Full elicited/grouped combination absent; included in 23, outside smoke 21. |
| TC-006 | SF/AF; P wording only | Elicited older GF/App/one-by-one → blank status/request → scrolled article, absent form → unknown access clarified → retry declined → finish. | **F:** exact declined-retry fixture; existing P has wrong LOB/platform and no retry decision. |
| TC-007 | SF/AF fragments | GF status → order absent → History → Date-selector actual failure → one repeat → success/Confirm → newly visible order/status → submission/finish. | **F:** exact failure fixture; no History/repeat script. **U:** still-missing or second-failure remedy. |
| TC-008 | L/SF | GF/App/one-by-one/loudspeaker yes → visible blank status → missing link → fallback offer accepted → Portal ready → form/submission/finish. | L is grouped and ends before downstream observations. **U:** GF Portal unavailable. |
| TC-009 | P/L wording | Older GF → explicitly decline status, request Portal submission only; one-by-one/loudspeaker yes; known access → retry accepted/fails → person offer → unclear “okay”/supported re-offer → later explicit acceptance → mock terminal. | **F:** exact submit-only/retry/consent fixture; no executable chain or typed terminal assertion. |
| TC-010 | None | Unrelated menu-update request, no age prerequisite → scope/person offer → later explicit acceptance → mock terminal. | **F:** menu-update refinement; no scope/handoff script or terminal capture binding. |
| TC-025 | TM facts | GM, cancelled 1 day ago, age-only → education/order-photo reminder → further help → finish. | Timing question is not this trigger; utterance-first opening proposed; voice evidence separate. |
| TC-026 | TM facts | Recent GM education → nonreceipt follow-up → guidance offer → decline → finish. | No refusal chain; text cannot assess reported voice silence. |
| TC-027 | PF/P/EM | Older GM upfront dual/App/one-by-one → notice/computer-Portal explanation/readiness → actions/status → retained request → form/evidence/submission/finish. | **F:** exact transition fixture; PF starts Portal-ready and stops before status answer. Outside smoke 21. |
| TC-028 | TM facts | Older GM age-only → elicited general inquiry → education → selected no-offer acknowledgement → further help/explicit finish. | **F:** Q12 ending; acknowledgement is not finish; offered-and-declined alternative unselected. |
| TC-029 | TM/SM/P/EM | Older GM elicited dual → education/offer/acceptance → App/grouped → notice/Portal readiness → blank status → form/submission/finish. | No joined elicited/grouped interaction; grouped segments stop at observations. |
| VAR-TC-003-A | SF | Parent route → Auto approved, remaining goal status-only → bounded explanation/no duplicate → finish. | Exact status/remaining-goal control absent; does not cover original App submission. |
| VAR-TC-003-B | SF/TF | Auto approved but funds not received → approval/payout/bank distinction and relevant clarification. | Unpaid concern binding absent; **U:** payment remedy/date/financial resolution. |
| VAR-TC-003-C | SF/AF | Unclear status → actual clarification → visible blank plus retained review goal → full App target continuation. | Clarification/continuation script absent; clarification alone cannot cover TC-003. |
| VAR-TC-006-A | AF; P wording | Parent access prefix → retry separately accepted → one attempt → form visible → submission/finish. | No retry-success script; never covers primary retry-declined target. |
| VAR-TC-027-C | None | Computer Portal unavailable → supported person offer → explicit refusal → no transfer → further help/finish. | **Only refusal selected**; no accepted-handoff/access-gained coverage. |
| VAR-TC-027-D | SM/PF | Order absent → period recheck retaining compatible store/Category → new visibility/status → supported continuation. | SM stops at advice; **U:** still-missing remedy; define successful recheck branch. |
| VAR-TC-027-F | PF/SM | Explicit GM status-only, no age/loudspeaker → necessary navigation facts → actions → actual result; no submission scope. | PF ends at status question; no full result/ending or reviewed bypass binding. |
| VAR-TC-027-G | AM/EM | Older GM App submission-only → link/article/scroll/form → authorized evidence/completion → submission/finish; no forced status or Portal detour. | Grouped content slice lacks full parent-preference-preserving target. |

## 3. Inputs, checkpoints and evidence with the unchanged runner

**Inspected source:** `uc4-runner` **0.2.0**, Git HEAD
`59faa616dc36dd96a0df6f6884de1cc77198b15a`; working tree includes uncommitted scenario/
documentation work. HEAD alone does not reproduce this inventory. Source-content
manifest hash: `ba293100e4fe6fe2f9f0a9af4541f011495d8c165bdbb412cd4560db6f79e4ef`
(SHA-256 of sorted `sha256  repo-relative-path\n` lines for `pyproject.toml` and the
12 immediate `uc4_runner/*.py` files). This is not an executed/installed revision.
Nineteen standalone scenario definitions exist: three packaged YAMLs, fifteen KB
YAMLs and one JSON example; none supplies a full selected-fixture binding.

The [schema](../TESTING_GUIDELINES.md#scenario-schema-v1) / [parser](../../uc4_runner/scenario.py)
supports versioned YAML/JSON, `product`, regex concepts/assertions and fixed ordered
turns with **nonempty** `merchant` text and optional `advance_when`. Each
[request](../../uc4_runner/client.py) sends fresh-run identities, `text`, `data: {}`.
No schema field injects channel, clock, context, previous education, branch state
or UI observations. Product metadata does not tell the Agent the business line.

- **Communicate facts when due:** English/Malaysia, synthetic current-order identity,
  explicit GF/GM, cancellation age 1 or 14 days (except TC-010/direct status-only
  bypass), entry goal and stated platform/style/loudspeaker preferences. Supply
  authorization/evidence availability only as the selected fixture permits.
- **Preserve observation boundaries:** one action/wait versus grouped TC-005/029
  segments; missing order differs from visible blank/unread/approved status; missing
  link, opened article, scroll, form visibility, access, retry consent/attempt/result,
  submission report, person-offer consent and finish are separate checkpoints.
  Guard the preceding instruction/offer before sending its scripted acknowledgement.
- **Gates are screening, not semantic adjudication:** [eligible gates](../TESTING_GUIDELINES.md#gate-eligibility)
  can advance one fixed script or stop it. They cannot branch, loop or adapt to
  lawful clarifications. Preserve alternate replies/skipped turns; do not force a
  target or treat a narrow regex failure as definitive BR failure. Unsupported
  adaptive paths require a separately agreed manual protocol, not invented fields.
- **Native-empty entry is a hard representation gap:** empty/whitespace merchant
  text is rejected. A greeting/sentinel is a different fixture; no pre-start/resume
  facility recreates the missing opening. External manual/channel capture is needed
  for that control; no runner extension is proposed here.
- **Reference date is not injectable:** catalog fixture `2026-11-04` Wednesday,
  Asia/Kuala_Lumpur UTC+8 remains its documented version. Assessment is now November 5;
  any later run needs an explicitly versioned reference-date binding and actual
  initialization evidence. Do not pretend the old date is the live date or cross
  midnight under an unapproved convention.

### Separate assessments and capture

The runner's aggregate PASS/PASS_WITH_WARNINGS/FAIL/ERROR is **not** the two-axis
Problem #2 assessment. Keep it unchanged and add a separate record per run with
acceptance/JRN/BR/VAR versions, observed branch, milestone evidence and compliance,
reviewer/date, **behavior verdict** and **target-coverage verdict**. Correct alternate
handling can be `PASS / INCOMPLETE_COVERAGE`; incorrect but fully traversed handling
can be `FAIL / PASS`. Unsupported dependent judgments retain `BLOCKED_SPEC`,
`BLOCKED_ENV` or `NEEDS_REVIEW` as applicable; preserve known violations/prefixes.
Current axes remain `NOT_RUN / NOT_RUN`. A COMPLETE manifest or transport success
does not establish coverage, a terminal event or business resolution.

Required evidence: scenario ID/version, byte hash and runner canonical parsed hash;
configuration/source bindings; run/batch/fresh-conversation IDs; channel/language;
intended/actual reference and capture times; merchant/Agent transcript, attempted/
skipped turns and gates; trace locators; matched Tool/Flow terminal events; artifact
paths/hashes. Runner [normalization](../ARCHITECTURE.md#normalization) captures text,
not arbitrary internal data/asynchronous output. Empty/nontext replies become ERROR,
including a potentially legitimate textless terminal: preserve the result and seek
external evidence rather than infer success or an Agent defect.

Propose redacted raw-response retention plus restricted external trace capture;
review storage/access/retention and redaction before authorization. Raw retention
is opt-in and not byte-exact forensic evidence. A trace ID alone proves no Tool,
retrieval or terminal. Voice claims require synchronized recognized input, generated/
displayed content, audible playback, interruption timing and terminal trace; the
runner captures none of those audio channels. REST “loudspeaker=yes” tests a stated
preference, not voice. Real UI/backend/payment/connection assurance stays excluded.

## 4. Reproducible execution plan — proposed, not authorized

1. **Bind a manifest before any run:** one row per the 23 identities above with exact
   outcome, scenario path/ID/version/hashes, BR/JRN/CT scope, entry and merchant script,
   gates, applicable unresolved limits, current configuration fingerprint, actual
   reference-date version, channel/capture, repetitions and output root. Preserve
   the 21-fixture membership flag (all except TC-005/027). Missing scenario paths/
   versions are explicit blockers, not aliases to partial YAMLs. Future scenario
   authoring/review and offline verification remain separate work; none occurred here.
2. **Primary channel proposal:** English REST/text, sequential fresh conversations,
   concurrency 1; synthetic observations only. Propose TC-001 native-empty and TC-025
   utterance-first as the opening contrast: TC-001 then requires a separately
   verified, authorized manual/channel route. Do not silently substitute text-first
   for native-empty. Record this exception in the manifest; the full selection is
   not currently one runnable REST suite.
3. **Sampling proposal, OD-015 decision still needed:** first pass 1 fresh conversation
   per selected identity (23 across approved channel bindings). For status/recovery/
   consent/transition risk, increase **TC-003/005/006/007/008/009/010/027/029 and all
   eight selected VARs** to 5 total each after capture review: 17 high-risk targets,
   68 additional conversations, **91 primary-cohort conversations** if completed.
   Do not discard failed or alternate branches or reset the denominator after fixes.
   Same-version smoke membership would identify 81 of those conversations; the
   TC-005/027 ten remain full-selection coverage, not smoke. A separate later smoke
   run is its own cohort, not double-counted evidence.
4. **Separate voice proposal:** 5 fresh voice conversations each for TC-003/004/010/026
   plus one each for the TC-001/025 opening contrast, with synchronized capture and
   reviewed terminal expectations. These 22 supplemental conversations are a distinct
   cohort, not substitutes for primary runs or full 23-fixture voice coverage.
   Other audible claims stay held without corresponding voice evidence. No sampling
   count establishes production reliability, DG-009 closure or Q8 conformance.
5. **Record transport/capture settings:** installed Python/dependency versions,
   source-content hash, Endpoint binding and Test Mode choice, timeout/delays, raw
   retention/redaction, output root and all relevant environment values without secrets.
   Proposed single-session pacing must also fit documented Test Mode message limits;
   a repeat count is not a rate limit. Retain every batch and original automated grade.

The existing [CLI source](../../uc4_runner/cli.py) supports the following command
shape **only after bindings, required decisions and separate execution authorization**.
It is not a runnable plan yet; no values are supplied for the missing bindings:

```powershell
& 'C:\Users\Nau\cognigy-grab\.venv\Scripts\python.exe' -m uc4_runner run --scenario-file $scenarioFile --repeat $repeat --concurrency 1 --output-dir $outputDir
```

Use reviewed absolute scenario/output paths; one invocation selects one scenario.
For staged sampling, record the initial `--repeat 1` and later `--repeat 4` batches
against the same unchanged binding. Manual/native-empty/voice captures do not use
this text-only command. No scenario validation, dry-run or execution was performed.

## 5. Outstanding prerequisites and decision

| Prerequisite / responsible capacity | Required before changing NO-GO for its scope |
|---|---|
| Current configuration — configuration owner | Fresh authenticated resource capture, effective Endpoint/revision/Snapshot/entry and model/Knowledge binding, hashes and current-versus-historical diff; verify POC/shared dependency boundaries. |
| Executable fixtures — project owner in engineering + QA capacities | Complete reviewed bindings for all 23; precise merchant scripts/gates and versioned reference date. Resolve exact TC-006/007/009/027 fixtures, Q12 TC-004/028 repairs and TC-010 refinement explicitly; scoped selection approval did not resolve them. |
| Q8 — configuration owner + internal reviewers | Determine current admission/checkpoint/correction/delivery conformance; retain N01–N08/same-order correction holds. Existing timing scripts use a different order. Do not claim full Q8 regression from the 23 selected targets or invent additional accepted VARs. |
| Conditional policy/text — relevant authorized owners + internal QA | Exact OD-011 CT adoption where literal grading is proposed; OD-006 certainty stays blocked. Canonical status/payment/UI/evidence/calendar/recovery unknowns remain bounded; do not require excluded judgments for supported-prefix assessment. |
| Channel/evidence — voice/configuration owner + internal QA | Native-empty route, terminal ownership/exactly-once capture and synchronized audio; dispositions for textless terminal/alternate branch/gate stops; storage and evidence bindings. |
| Sampling and readiness scope — project owner in both capacities | Explicitly decide the proposed sampling/channel manifest and any scoped deferments. Independent QA remains deferred; no independent validation claim. |
| Execution governance — separately authorized decision-maker | Required later scoped baseline-freeze decision under existing OD-015 governance before baseline execution, plus explicit execution authorization for exact configuration, fixtures, channel and counts. Neither is requested as an approval by this report or granted here. |

**Final: NO-GO for execution of the accepted 23-fixture selection.** Supported text
paths can become conditionally testable after binding/capture decisions; unsupported
outcomes remain held or excluded. A future scoped readiness change must name its
exact coverage and cannot silently shrink the 23 selection to the 21 subset.
**Stop here and await separate execution authorization.**

## 6. Assessment provenance and static checks

- Acceptance evidence: immutable [supplied record](../../reference/UC4_P2_Scoped_Internal_POC_Acceptance_Decision_2026-11-04.md),
  SHA-256 `8ee7d8e978b437553935f628e263b0ef20f3380727e3cdef92380556d2586a81`;
  declaration date November 4 is not an authenticated signature timestamp.
- Preservation baseline, complete historical member hashes/comparison,
  documentation diffs and link/table/identity/whitespace verification are retained
  in `C:\Users\Nau\AppData\Local\Temp\opencode\uc4-execution-readiness-2026-11-05`
  (`audit-readiness.py`, `preservation-before.json`,
  `historical-configuration-verification.json`, `documentation-verification.json`).
- Checks are static source/documentation checks only. Catalog/candidate, qualified
  agreements, existing scenario/runner files and historical reports are preserved.
  No current deployment verification, Cognigy mutation, runner development, live
  conversation, test, scenario validation/dry-run, regrade or freeze is claimed.
