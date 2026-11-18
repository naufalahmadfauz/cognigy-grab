# UC4 Problem #2 — offline pilot preparation

**P2-PILOT-PREP-0.1 · 2026-11-05 · all three pilots NO-GO for real execution**

Three complete fixed-script drafts are authored and validated offline. **Binding
and evidence review remains pending: 0/3 pilots and 0/23 selected fixtures have
complete reviewed executable bindings.** Current configuration is unverified;
`configuration_id=null`. Behavior **NOT_RUN** / target coverage **NOT_RUN**.

The [scoped internal POC acceptance](REVIEW_DECISION_WORKSHEET.md#recorded-scoped-internal-poc-acceptance)
stands. The approved **23-fixture selection** and separate **21-fixture smoke subset**
are unchanged; TC-003/006 are in both, TC-027 is in the 23 only. The owner retains
the accepted engineering/QA self-review roles; independent QA remains deferred and
formal Grab approval pending. No baseline freeze or execution authorization occurs here.
This preparation supplements [P2-EXECUTION-READINESS-0.1](EXECUTION_READINESS.md).

## 1. Readiness manifest

All files use the existing runner schema v1; scenario ID equals filename stem.
“Validated” means schema/regex/reference validation plus the offline checks below,
not approved binding, current deployment verification or observed Agent performance.

| Pilot / scenario file | Version | Turns / gates | Supported original target | Missing review/evidence; real-run status |
|---|---|---|---|---|
| TC-003 — [P2-TC-003-001.yaml](../../scenarios/problem2-pilots/P2-TC-003-001.yaml) | 0.1.0 | 13 / 12 | GF upfront dual goal → visible blank status → full App review request → reported submission → explicit finish | Exact known-access/initial-form/no-photo allocation; E1–E5 and current configuration below. **NO-GO** |
| TC-006 — [P2-TC-006-001.yaml](../../scenarios/problem2-pilots/P2-TC-006-001.yaml) | 0.1.0 | 13 / 12 | GF older elicited goal → education/offer/acceptance → absent form → access clarification → retry declined → explicit finish | Exact unknown-access/refusal script; E1–E5 and current configuration below. **NO-GO** |
| TC-027 — [P2-TC-027-001.yaml](../../scenarios/problem2-pilots/P2-TC-027-001.yaml) | 0.1.0 | 16 / 15 | GM App-selected → computer-Portal ready → status → Portal review request → reported submission → explicit finish | Exact transition/access/no-photo allocation; once-only notice review; E1–E5 and current configuration below. **NO-GO** |

| Scenario | YAML-byte SHA-256 | Validated canonical `scenarioSha256` |
|---|---|---|
| P2-TC-003-001 | `cb37ccac813fbd4844950d8fe33f501b0c010941511fa96efb640ab19251db13` | `1ec66c5a61b8f39314c6d69f4074dbc314465b4c03a946610fe70c90b2d2056b` |
| P2-TC-006-001 | `66c63483c067fc85e764e29467ea99c60831bc43f7784331ac12c4962aaa0fa9` | `623976dfa3531db0ddd15d5608e75a21a045206d68e550ecb4adb6044704812e` |
| P2-TC-027-001 | `e539a0a12c9ead1f899dc1e0e2ea023d692a434da7fba9ef9f5dbba9dd932bcc` | `db182c73d9a94e70c529df0a677091de42a74172bb1e91334e7c87e071a70a0e` |

Canonical hashes use the unchanged parser's
`sha256(json.dumps(validated_definition, sort_keys=True, ensure_ascii=False).encode("utf-8"))`
with default JSON separators. YAML comments/formatting affect only the byte hash.
Any subsequent script/rubric change needs a new scenario version and fresh hashes/checks.

## 2. Bound inputs and checkpoint map

**Preparation scope confirmed by the user:** fixed, utterance-first English REST/text
scripts with semantic screening gates for these three original targets. That
confirmation did not approve the exact scripts or their evidence arrangements.

- Governing specifications: [P2-JOURNEYS-0.4 common contract](JOURNEY_PILOT.md#common-contract),
  the three linked journeys below, qualified Q1–Q13 and the accepted review scope.
  All start fresh, with ordinary opening **outstanding**, no prior education or
  pre-started conversation; first input is nonempty merchant text.
- All communicate Malaysia, explicit business line, **cancellation age 14 days**,
  one-by-one guidance and **loudspeaker=no**. Catalog reference remains
  **2026-11-04, Wednesday, Asia/Kuala_Lumpur UTC+8**. It is external fixture metadata,
  not an injected runtime clock. A future run needs a versioned reference-date
  binding and evidence of actual initialization/date; the old date is not assumed current.
- Proposed exact allocation: TC-003 supplies prepared-food context and authorized
  Owner access at T01, with an initially visible form. TC-006 leaves access unknown
  to the Agent until its separate T11 answer after T10 form absence; availability
  does not assert a login change or retry. TC-027 starts **App-selected**, then
  reports computer-Portal home/readiness and authorized Owner access at T02.
- TC-003/027 allocate the qualified GF/GM no-photo controls respectively. Evidence
  recommendations remain; available information does not guarantee sufficiency,
  eligibility, acceptance or approval. These allocations still need binding review.

`Tnn` denotes the YAML turn index. Each action/offer receives its own Agent reply;
the next merchant observation is sent only after the preceding gate passes.

| Source milestones | Script checkpoints and preserved waits |
|---|---|
| [JRN-TC-003](JOURNEY_PILOT.md#jrn-tc-003) M01/M03–M10 | T01 direct dual goal/preferences → Orders; T02 Cancelled; T03 order-visibility question → T04 visible-order report/open-order/status question → T05 explicit blank status, retained request and present link. T05–T08 link action → article opening → scroll/form question → visible form. T08–T12 details → prepared-food evidence → no-photo continuation → information completion → merchant self-submission/report and further help. T13 explicit finish/ordinary closing. M02 has no trigger here. |
| [JRN-TC-006](JOURNEY_PILOT.md#jrn-tc-006) M01–M05/M10 | T01 age-only/open goal question → T02 elicited dual goal, qualified GF approval/payout education, existing-photo reminder and offered guidance → T03 acceptance/preferences. T03–T07 Orders/Cancelled/visible-order/explicit blank status and retained request. T07–T10 present link/article/scroll/form-absence observation. T10 access explanation/question → T11 authorized-access answer/separate retry offer → T12 explicit refusal/later-attempt advice/further help → T13 explicit finish. **M06–M09 do not execute.** |
| [JRN-TC-027](JOURNEY_PILOT.md#jrn-tc-027) M01/M03–M09 | T01 App-selected dual goal/computer-Portal explanation/readiness question → T02 Portal-ready report/Finance. T03 Transactions → T04 period **and** store → T05 Category → T06 separate result question → T07 visible blank status/retained request. T07–T11 Help Centre → Search Bar “dispute” → article → scroll/form question → visible form. T11–T15 details → packed-items evidence → no-photo continuation → information completion → merchant self-submission/report/further help. T16 explicit finish. M02 has no trigger; M03 notice is manually assessed below. |

TC-003 follows [OD-002 situation A](OD002_STATUS_DECISION_REVIEW.md) and the normal
visible-form profile. TC-006 preserves the agreed primary **declined retry**, not
`VAR-TC-006-A` success. Its unknown-access prefix follows the later readiness
allocation; older local profile B4 already knew access, while B5's accepted-retry
success remains a separate outcome.
The [Q9–Q13 access/consent contract](OD007_OD010_OD009_RECOVERY_ACCESS_CONSENT_REVIEW.md)
governs observations and endings; [Q3/Q7](OD004_OD005_TRIGGER_TIMING_REVIEW.md)
govern GM direct entry and qualified no-photo continuation.

## 3. Manual and external evidence requirements

The [existing gates](../TESTING_GUIDELINES.md#advancement-conditions) screen the
**current Agent reply** before sending the next fixed message. They cannot adapt
to a different lawful branch, clarification or turn segmentation. Preserve the
stopping reply and skipped turns; manually assess a wording mismatch before calling
it a BR violation. Schema validity and synthetic gate passes do not approve these bindings.

| ID | Required review/capture or explicit scope disposition |
|---|---|
| E1 — semantic transcript review | Review all milestone meanings, waits, context retention, actual education order/qualifications, guidance versus retry versus transfer consent, no-photo limits, premature closure and unsupported guarantees/remedies. TC-027 specifically needs the GM notice **once before the first applicable navigation**, including order across replies and no repetition on submission entry. This is not a hard regex gate. Its certainty wording produces only a review warning. [Controlled-text adoption](BASELINE_MODEL.md#controlled-language-applicability-register) remains pending; no literal CT01/02/05/06/07/12 oracle is adopted. |
| E2 — initialization and ordinary terminal | Bind timestamped external Flow/Tool trace to each run/session and reply: actual initial context/entry, applicable greeting emission, explicit finish, `end_call`/Flow-owned goodbye and terminal exactly once, with no duplicate Agent closing or transfer. Text alone proves neither ownership nor completion. Empty/textless terminal remains runner **ERROR** until separately assessed; never overwrite it as a pass. |
| E3 — UI, role and backend facts | Here all visibility, authorized access, evidence availability and submission reports are **synthetic merchant inputs**. Review that scope explicitly. Authentic UI/access/backend claims need separately authorized screenshots/audit/transaction evidence tied to the order and time; none is supplied by these fixtures. Submission report does not establish backend acceptance, approval, payment or resolved compensation. |
| E4 — opening and audio scope | These scripts cover utterance-first text only. Native-empty entry needs a separate reviewed manual/channel capture; no empty/sentinel substitution. Audible greeting/education/goodbye, playback completion and interruption need synchronized recognized input, generated text, audio and terminal trace. Keep these claims outside the REST pilot's evidence scope; TC-003 does not close DG-009. Review any scoped deferral rather than infer voice coverage from loudspeaker=no. |
| E5 — reproducibility and assessment | Record exact scenario/version/both hashes, configuration fingerprint, acceptance/JRN/BR/CT scope, intended and actual reference date/time, channel, fresh run/batch/session IDs, transcript/gates/unsent turns, external trace locators and artifact hashes. Name capture/review owner, storage/access/retention/redaction, textless-terminal/alternate-branch handling, and separate behavior/target-coverage verdicts. Raw retention is opt-in; redacted raw responses and trace IDs alone are not terminal/retrieval evidence. |

## 4. Owner checklist — current configuration, read-only and secret-free

**Every item is currently unverified.** Supply timestamped, sanitized captures with
stable resource references, capture origin and SHA-256 of the shared bytes; record
redaction scope. Never include Endpoint URLs/tokens, API keys, passwords, cookies,
connection credentials or merchant data. Do not change settings or send messages
to obtain this static evidence.

- [ ] **Capture identity:** tenant/project, Cognigy version, owner, capture time/timezone,
  isolated POC purpose and resource/dependency inventory, including shared callers.
- [ ] **Endpoint → Flow:** Endpoint reference/name/type, active/mocking state, selected
  Flow stable reference, locale/entry point, selected current-project revision or
  Snapshot ID/version, transformers, connection references and Snapshot-connection
  override flags. Record intended Test Mode choice separately; it is not offline mode.
- [ ] **Served revision:** establish which captured Flow/resources the Endpoint will
  serve; record revision identifiers or timestamped content fingerprints where a
  revision ID is unavailable. A package alone does not prove this binding. Capture
  current Flow/chart and Agent references, plus shared-dependency/isolation boundaries.
- [ ] **Job:** exact `Grab Cancelled Order Compensation` instructions, node/Agent
  references, entry/exit wiring, enabled options and their effective source/overrides.
- [ ] **Tools:** definitions, parameters/conditions and wiring for `resolve_order_age`,
  `start_guidance`, `update_guidance_checkpoint`, `end_call`, `transfer_to_live_agent`
  and `escalate_safety`; record renamed/added/removed Tools and dependencies.
- [ ] **Code:** session initialization, first-input LOB, greeting emission/recording,
  age resolution, checkpoint validation and ordinary/transfer/safety terminal paths;
  exact source/transpiled content hashes where applicable. Identify current Q8
  admission/checkpoint/correction/delivery differences; these older pilots do not
  establish full Q8 conformance.
- [ ] **Knowledge:** Agent versus Job store selection/overrides, enabled/injection/search
  settings, search prompt, top-K/filters, source versions and chunk/disabled inventory,
  embedding model and indexing status. Compare content hashes; retrieval behavior
  requires later run trace, not merely matching stored text.
- [ ] **Effective models/settings:** resolve `default` through project Generative AI
  settings and all applicable overrides; record provider, model/deployment and
  resolvable version, API version, custom options, temperature, token limit, timeout,
  inherited memory/history and relevant voice/channel settings. `default`/`latest`
  alone is insufficient. Record connection references only.
- [ ] **Comparison and review:** compare stable refs and sanitized configuration fields
  with the [historical October 30 ledger](EXECUTION_READINESS.md#verified-historical-reference-current-deployment-unverified),
  recording same/changed/missing and reviewed impact. Historical member hashes prove
  historical integrity only. Assign a current configuration fingerprint and reviewer
  only after the capture, effective resolution and differences are accounted for.

Documentation consulted through Context7: [Cognigy Endpoints](https://docs.cognigy.com/ai/agents/deploy/endpoints/overview)
(Flow/Snapshot/connection overrides) and [AI Agent Node](https://github.com/cognigy/documentation/blob/main/docs/ai/build/node-reference/ai/ai-agent.md)
(project-default LLM and Knowledge injection). Use the captured tenant version's
available fields; public documentation is not evidence of this deployment's state.

## 5. Offline verification and preservation

- Existing CLI: **3 scenarios validated**, from an isolated cwd without repository
  `.env`, with Cognigy/UC4 environment removed. Command:
  `python -B -m uc4_runner validate --scenarios-dir C:\Users\Nau\cognigy-grab\scenarios\problem2-pilots`.
- Existing schema/gate-eligibility tests: **47 passed**. No runner or permanent test
  implementation was changed.
- Final synthetic verification pass: **110 wording checks**, **55 single-run mocked
  batches**, one **five-run mixed mocked batch**, and **3 dry-run plans** passed.
  All **39 non-final gates** have a compliant full-chain path and a deviating stop
  check. Verified exact sent prefixes, no later messages/delays after a stop,
  retained replies/reasons/zero-attempt skipped turns, persisted reports/metrics,
  distinct identities, nonblocking warnings/unselected failures, final-turn failure
  and empty-reply/textless-terminal ERROR. Dry-run outcomes remain unevaluated.
- Mock checks used HTTPX **0.28.1**, Python **3.15.2**, dummy `.invalid` configuration,
  blocked real sockets/DNS and temporary outputs. **Zero live Endpoint requests**;
  no Cognigy modification, historical regrade, commit, push or freeze.
- Preservation checks cover **186 unchanged existing repository files**, the original
  README content, **467 historical report files**, **94 prior audit files** and
  **seven external sources**. Only the README pointer and these four new files
  belong to this preparation; existing uncommitted work is preserved.

Audit directory: `C:\Users\Nau\AppData\Local\Temp\opencode\uc4-pilot-offline-2026-11-05`.
Retained: `preservation-before.json`, `validate-pilots.py`, `validation-latest.json`,
`verify-pilots.py`, `offline-verification-latest.json`, `audit-pilots.py`,
`documentation-verification.json` and fresh temporary outputs. The final successful
mock pass is under `mocked-check-nwus7ad5`; earlier draft-calibration outputs remain
separate. These are offline development evidence, not Cognigy behavior/coverage results.

## 6. Exactly what remains before the first real run

1. **Current configuration evidence and comparison:** complete the owner checklist
   and bind the exact served Endpoint/revision/Snapshot/Job/Tools/Code/Knowledge/model.
2. **Binding and evidence review:** owner records engineering + QA review of the
   selected pilot's exact script/hashes, proposed access/no-photo/transition choices,
   reference-date version and E1–E5 capture arrangements/dispositions. Resolve
   applicable conditional requirements within the accepted scope; keep excluded
   UI/backend/audio/native-empty claims explicit.
3. **Exact run scope/settings:** decide which pilot(s), repetitions/staging, English
   REST/channel scope, sequential pacing/concurrency, Test Mode choice, capture/output
   location and settings. A pilot authorization must name its limited scope while
   retaining the approved 23/21 selections; the prior sampling proposal remains undecided.
4. **Separate governance and authorization:** obtain the later scoped freeze decision
   required by existing OD-015 governance before baseline execution, and explicit
   authorization for the exact configuration, fixtures, channel and counts. Neither
   is granted by business acceptance, this manifest or offline validation.

**Stop: offline preparation complete; all three real-run statuses remain NO-GO.**
