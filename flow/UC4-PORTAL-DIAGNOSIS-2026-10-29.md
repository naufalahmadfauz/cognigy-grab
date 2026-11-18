# UC4 Portal batch diagnosis — 2026-10-29

## Conclusion

The exported Flow explicitly requires cancellation age before guidance. The Agent's
observed age question follows that configuration. The export does **not** establish
that age is a business prerequisite for viewing GrabMart compensation status:
the knowledge material calls the age threshold a conversation-routing rule, and
its status article starts at Finance without an age prerequisite.

The preparation statement and redundant help question are both literal, required
greeting text in the AI Agent Job. They are defects in the opening for this
merchant request, rather than evidence that the model invented that wording.

A second configured prerequisite matters: the Job requires a loudspeaker question
before navigation. The approved POC exception removes both prerequisites for
explicit status-only navigation in voice and REST/text conversations.

**Status:** diagnosis completed and POC policy approved. The new package confirms
the exported Endpoint's POC target and separate POC/`[MAIN]` Job/Tool identities.
The user has manually confirmed the live target and correct revision selection.
Exact three-node edits are prepared in the
[manual application kit](poc-correction-2026-10-29/README.md). Application and a
fresh-export comparison are pending operator action; no live tests are authorized.

## Approved POC policy

The user confirmed these boundaries after the initial diagnosis:

- Explicit GrabMart cancelled-order compensation-status navigation bypasses age
  intake and pre-navigation loudspeaker setup in **both voice and REST/text**.
- Missing platform or guidance-style preferences do not disable the exception.
  Answer a status-location question directly, or ask only for navigation
  information genuinely needed to continue.
- Already inside GrabMerchant Portal plus requested one-by-one guidance means
  Finance immediately, then Transactions only after acknowledgment.
- [Status navigation](../GLOSSARY.md) does not establish compensation eligibility,
  approval, payment, preparation, or packing. Applicable age requirements for
  eligibility/submission decisions and other journeys remain in force.
- Safety escalation, recording disclosures, greeting ownership, compensation
  policy, and terminal-state handling retain their existing priority.
- The existing v0.2 scenario remains the five-run regression after application
  and separate live-request authorization.

These decisions supersede the initial draft's text-only restriction and its
requirement that Portal and guidance style already be known. They authorize a
behavioral exception within the POC, not a change to shared resources or `[MAIN]`.

## Evidence and limits

- Batch: `20261029T002241049421Z-c93afb1a711d`.
- Scenario: [GM-PORTAL-STEPS-001](../uc4_runner/scenarios/GM-PORTAL-STEPS-001.yaml),
  version `0.2.0`, captured hash
  `6fc54e58eb2eab896f4a5989489d2b493148373a725cc3b89150df0fbb85e69c`.
- All five runs: Turn 1 HTTP 200; `finance-step` failed; Turn 2 skipped with zero
  attempts. All five opening paragraphs exactly match the Job's greeting literal.
- Export: [Package-Naufal_2026-10-29_00-56-08.zip](Package-Naufal_2026-10-29_00-56-08.zip).
  SHA-256: `056835f451b84541e025feff0f5c4cac12dd963cc2858445ef174434a42bfb35`.
- Package version `2026.22.1`, created `2026-10-29T00:56:15.186Z`; 76 members,
  including one Flow, 31 nodes, one AI Agent, one Knowledge Store, 17 sources,
  and 20 chunks. No Endpoint resource is included.
- Flow name: `UC4_KB_AGENT_POC_v03`. Knowledge Store: `UC4_KB_POC_v03_TEST`.
  The Job belongs to that Flow in the export. POC names and ownership do not prove
  which live Endpoint, Snapshot, entry node, or other callers use these resources.
- This export postdates the batch. The AI Agent metadata has a last-change time of
  `2026-10-29T00:55:57Z`; the nodes carry no individual revision timestamps.
  Historical deployment equivalence cannot be established from this package.
- Saved evidence contains normalized replies and one trace ID per executed turn,
  but no raw responses or node-level execution/knowledge-retrieval traces.
  The literal sources are confirmed; attribution of each live output fragment to
  a particular node remains conditional on the actual Endpoint entry path.

### Follow-up screenshot and 06:47 export

The supplied screenshot shows the REST Endpoint named `Test`, with
`UC4_KB_AGENT_POC_v03` selected, Endpoint enabled, and mocking disabled. The
Endpoint URL/token is omitted from these notes. The displayed Flow name is
supporting evidence; its stable ID and effective revision require reference
verification against the configuration.

New package:
[Package-Naufal_2026-10-29_06-47-07.zip](Package-Naufal_2026-10-29_06-47-07.zip).
SHA-256: `015b714019081f458b2d8f28047b68761e47c7fe6e7ddab68670ecb0684be6af`.

All 31 original POC node configurations match the new package when joined by
stable `referenceId`. The three proposed edit targets also retain their enabled,
entry-point, and mocking flags. Their field hashes in section A still match.
Package-local member IDs differ between exports; use the stable references to
identify corresponding resources.

| Proposed target | Stable reference | Member in 06:47 export |
|---|---|---|
| Job instructions | `e38e5029-d515-4002-ad03-dd99b0eb821e` | `nodeData/6ae2ebf02f2c7932c4cad8f7` |
| Proactive greeting Code | `3c8ee6d5-d094-41ec-b4e0-ab73161abbcf` | `nodeData/6ae2ebf02f2c7932c4cad8f5` |
| Greeting recorder Code | `d438fa76-736e-4027-b6f4-86fbee9495c1` | `nodeData/6ae2ebf02f2c7932c4cad901` |

### Exported target and isolation verification

The new package was created at `2026-10-29T06:47:13.068Z` on Cognigy `2026.22.1`.
Its 112 JSON members include two Flows, 62 nodes, one Endpoint, one AI Agent, and
one Knowledge Store with 17 sources and 20 chunks. No Snapshot is included.

Endpoint member `endpoint/6ae2ebf02f2c7932c4cad93d` contains:

```text
name = Test
channel = rest
targetType = flow
flowId = 17f129de-69b3-4828-bc4f-0c7d19ef41ce
entrypoint = null
active = true
enableMocking = false
overrideSnapshotConnections = false
```

All five Endpoint transformer enable flags are false. The exported target Flow ID
matches the POC stable reference exactly. The screenshot agrees on Endpoint name,
Flow name, enabled state, and mocking state.

| Resource | POC stable reference | `[MAIN]` stable reference |
|---|---|---|
| Flow | `17f129de-69b3-4828-bc4f-0c7d19ef41ce` | `1e2d8901-ede6-43a8-8f18-a2537d439051` |
| Local Job | `e38e5029-d515-4002-ad03-dd99b0eb821e` | `f29ddf5c-b903-5785-8979-f5d8af37bda7` |
| `resolve_order_age` Tool | `af154209-7c67-42a0-b84f-c999ac7ede6c` | `771f8a95-55ad-53af-ab17-ba74b8a6634d` |
| `start_guidance` Tool | `7769b22f-7870-48bb-a3e6-9ba5a50271b6` | `f8475d63-ed1c-4bee-9d1b-a38a5e76f374` |

Each Flow owns 31 nodes. Their node `_id` and stable `referenceId` sets have no
intersection. Each Job has its own six Tool definitions and local downstream
Code/Resolve nodes. Chart edges resolve within their owning Flow. Both Flows have
empty attached-Flow lists; the inspected nodes/strings contain no cross-Flow
invocation between POC and `[MAIN]`. All 62 nodes are enabled with node mocking off.
These are package-scoped facts, not a project-wide reverse-reference inventory.

**Shared dependencies are confirmed:** both Jobs reference AI Agent
`3c1b0294-6016-4b52-8478-afd6cc05a434` (`Grab AI Assistant`). That Agent points to
Knowledge Store `786b7a11-913c-4ec0-8a4e-e48352921d78`
(`UC4_KB_POC_v03_TEST`). The POC enables Job knowledge for this store. `[MAIN]`
enables AI Agent knowledge, so it also has a configured path to this POC-named
store. Its separate enabled Job-store reference,
`96ffeec0-739c-49ed-aae5-478370cb47af`, has no definition in the package. Manifest
`partial=false` and empty missing-resource lists therefore do not prove all
project dependencies are included.

The smallest proposed edit set uses only the independent POC Job instructions and
the two independent POC greeting Code nodes. No shared Job/Tool node needs copying
on the evidence supplied. The shared AI Agent and Knowledge Store are outside that
edit set; their contents and references are protected. A full-package replacement
would include `[MAIN]` and shared dependencies, so it is outside the approved scope.

### Live-target verification history and operator confirmation

The screenshot's browser-editor Endpoint ID is `6ae1c67bbc3cfbe2fe5b68e5`. The
package-local Endpoint `_id` is different and has no stable `referenceId` or
original browser-ID mapping. Package-local IDs also differ for all three known
POC edit targets across the two exports. A name match supports the correspondence
but does not independently establish the live Endpoint's stable Flow binding.

The exported `entrypoint=null` does not explicitly select a named Snapshot or
prove a live current-Project selection. Neither `overrideSnapshotConnections=false`,
the manifest's Cognigy version, nor Job `apiVersion="latest"` supplies that evidence.

A private comparison found the local runner destination token differs from the
exported Endpoint token. That export-only comparison did not establish the live
destination. No URL or token is reproduced in this report.

The user subsequently completed the manual deployment check and confirmed:

- The live REST Endpoint selects `UC4_KB_AGENT_POC_v03`.
- Its Flow reference is `17f129de-69b3-4828-bc4f-0c7d19ef41ce`.
- Its Snapshot/current-Project selection is correct.
- The runner's configured destination matches that Endpoint.

This is accepted operator confirmation, distinct from an administration read by
the agent. The exact Snapshot name/ID or current-Project selection value was not
recorded here. The target-verification stage is complete for this manual handoff;
the fresh export after application is the next required deployment evidence.

## Entry path

The exported chart gives this normal Start path:

```text
Start
  -> Initialize Once
       On First Time -> Code: Initialize session
                     -> Set Session Config (EN)
                     -> Code: Proactive greeting once
       Afterwards    -> no bootstrap actions
  -> Code: Capture first-input LOB
  -> Grab Cancelled Order Compensation [AI Agent Job]
       Default -> Code: Record greeting emission
       resolve_order_age -> Code: resolve_order_age -> Resolve Tool Action
       start_guidance -> Resolve Tool Action: guidance settings
  -> End
```

Both Start and the AI Agent Job have `isEntryPoint=true`, making them possible
targets for node-level routing such as Go To or AI Agent Handover. That flag alone
does not prove that an Endpoint selects an individual node. Endpoint configuration
selects a Flow and optionally a Snapshot; the documented `input.entrypoint`
identifies the Project or Snapshot, not the Job node. The Flow has no attached
Flows in the original export. Effective routing must be checked from the Endpoint
configuration and any routing/transformer references.

On the normal Start path, initialization sets `ageDays=-1`, `threshold=""`, and
`greetingDelivered=false`. The proactive Code speaks only when `input.text` is
empty and the event is empty, `CALL_CREATED`, or `CALL_IN_PROGRESS`.

With the captured nonempty first merchant message, that Code does not speak.
The Job's **Exceptional utterance-first fallback** then requires the full greeting
when none was emitted earlier. This is the matching source path for the recorded
first-text request, assuming the Endpoint passed that text through normally.

The bounded first-input business-line parser does not recognize the scenario's
multi-sentence opening when no `input.data.lob` is supplied. The Job nevertheless
explicitly retains the merchant's clear conversational GrabMart statement. This
is not a reason to broaden that parser for this task: the age-first instruction
and tool gate still apply even when the saved business line is already GrabMart.

## Exact sources

Paths below are ZIP member names. Configuration fields are under
`/localizedData/0/config`.

| Source | Member / stable reference | Relevant content |
|---|---|---|
| AI Agent Job | `nodeData/6ae299aeb2804e59b88dfb9d`; `e38e5029-d515-4002-ad03-dd99b0eb821e` | `instructions`, sections GREETING OWNERSHIP, MERCHANT CONTEXT, CANCELLATION DATE, GUIDANCE PREFERENCES, and GRABMART PORTAL — COMPENSATION STATUS |
| Proactive opening | `nodeData/6ae299aeb2804e59b88dfb9b`; `3c8ee6d5-d094-41ec-b4e0-ab73161abbcf` | `code` and `transpiled`: `api.say(...)` contains the same full greeting, guarded by absent merchant text |
| Opening recorder | `nodeData/6ae299aeb2804e59b88dfba7`; `d438fa76-736e-4027-b6f4-86fbee9495c1` | `code` and `transpiled`: detects the full greeting using `generatedText.includes(...)`; it does not emit it |
| Guidance availability | `nodeData/6ae299aeb2804e59b88dfba0`; `7769b22f-7870-48bb-a3e6-9ba5a50271b6` | `condition`: `context.shortTermMemory.uc4.threshold === "beyond"` |
| Age resolver | `nodeData/6ae299aeb2804e59b88dfbaa`; `10d6ac7d-0451-41b7-9404-b1c68da8caff` | Whole-number age validation and weekday routing; no merchant-facing text |
| Flow | `flow/6ae299aeb2804e59b88dfb85`; `17f129de-69b3-4828-bc4f-0c7d19ef41ce` | Owner of the inspected nodes |

### Preparation assumption and redundant question

GREETING OWNERSHIP orders the Agent to use the **entire approved greeting**, without
shortening it or adapting it to the business line:

> Hi, I'm your Grab AI Assistant, and I'll be assisting you today. Please note that this call will be recorded for quality assurance and training purposes. I understand that you're contacting us about an order that was cancelled after it had already been prepared. How may I help you today?

The next paragraph explicitly calls the final question fixed opening wording,
even when the request is already known. Therefore the redundant question is an
instruction-level behavior. The merchant did not establish preparation or packing.
The Job's role description and adopted preparation/packing scope do not establish
that fact about this particular order.

The exact preparation phrase appears in only those three nodes: the Job literal,
the proactive emitter, and the recorder. Neither the resolver nor a knowledge
article is needed to produce it.

### Age-first routing

CANCELLATION DATE says:

> If the cancellation age is not yet known, ask one short cancellation-age question first and wait, retaining any LOB answer or intent already given.

MERCHANT CONTEXT routes authoritative business-line resolution through
`resolve_order_age`; that tool requires both `days_ago` and `lob`. Unknown age
therefore blocks that lookup even if the merchant already said GrabMart.

The resolver sets GrabMart `within` at up to 7 elapsed days Monday–Friday, 8 on
Saturday, and 9 on Sunday, inclusive. Above the cutoff it returns `beyond`.
`start_guidance` is enabled only for `beyond`. The recent-order rules instead
require timeline education. The direct-guidance wording in OLDER CANCELLED ORDER
sits inside that older-order routing context; it is not a clear age-free exception.

GUIDANCE PREFERENCES also says:

> Never give a navigation step before the platform and style questions have been answered and the loudspeaker question has been asked.

The scenario supplies Portal and one-by-one preferences, but no loudspeaker answer.
These are deliberate configured intake rules. They conflict with the scenario's
immediate Finance-step expectation; the runner correctly reports that conflict.

## Knowledge configuration and policy evidence

The Job selects `UC4_KB_POC_v03_TEST`, reference
`786b7a11-913c-4ec0-8a4e-e48352921d78`, with:

```text
knowledgeSearchBehavior = onDemand
knowledgeSearchJobKnowledge = true
knowledgeSearchAiAgentKnowledge = false
knowledgeSearchGenerateSearchPrompt = true
knowledgeSearchTopK = 3
knowledgeSearchTags = ""
```

The shared AI Agent `Grab AI Assistant` also points to that store, but the Job's
Agent-knowledge switch is false. The Job instructs the Agent to answer the standard
journey from its instructions and use knowledge only for additional factual gaps.
No retrieved chunks for these five runs are available.

All 17 sources are version `0.3.0`, `adoption=provisional_poc`,
`formal_approval=pending`. Relevant source/chunk evidence:

| Source | Chunk | Finding |
|---|---|---|
| `UC4-MY-GM-STATUS-001.ctxt` | `6ae299afb2804e59b88dfc03` | Finance → Transactions → time period/store → Category → Compensation for cancelled orders. No age prerequisite stated. |
| `UC4-MY-GM-THRESHOLD-001.ctxt` | `6ae299afb2804e59b88dfc0c` | The threshold “selects a conversation journey and does not establish eligibility, a submission deadline or a payment date.” |
| `UC4-MY-SHARED-DEADLINES-001.ctxt` | `6ae299afb2804e59b88dfc0e` | Older orders retain review/request guidance; threshold alone is not a rejection rule. |
| `UC4-MY-GM-EVIDENCE-001.ctxt` | `6ae299afb2804e59b88dfc07` | Packing condition is an adopted POC assumption, explicitly not a verified decision about an individual order. |
| `UC4-MY-SHARED-ELIGIBILITY-001.ctxt` | `6ae299afb2804e59b88dfc09` | Eligibility examples do not establish an individual order's qualification or payment. |

**Decision supported by the export:** age is mandatory in the current configured
journey, but a genuine age prerequisite for status navigation is not established.
Approved POC policy: let an explicit status-only navigation request proceed without
age-based intake or loudspeaker setup in either channel. Keep eligibility and
timing decisions distinct from viewing a status screen. This approval changes the
POC's conversation priority; it does not establish formal Grab policy.

## Smallest proposed correction

### A. Correct the opening and its emission tracking

Apply these exact text edits to the independent POC nodes listed
above. Each old string must occur exactly once in each specified field.
Use the Cognigy Code editor for Code fields and verify its regenerated `transpiled`
output in a fresh export. The supplied archive remains the source baseline.

Define the new introductory text as:

```text
Hi, I'm your Grab AI Assistant, and I'll be assisting you today. Please note that this call will be recorded for quality assurance and training purposes.
```

1. **Job `instructions`, GREETING OWNERSHIP:** replace the full quoted greeting
   with the quoted introductory text above. Replace this exact sentence:

   ```text
   The final question in the approved greeting is fixed opening wording, not a request to repeat already-known facts.
   ```

   with:

   ```text
   The Merchant has already supplied a request, so do not append a generic help question. Do not infer that food was prepared or items were packed from the compensation topic alone.
   ```

2. **Code: Proactive greeting once, `code`:** replace only the greeting string
   inside `api.say` with the introductory text followed by
   ` How may I help you today?`. Its existing no-merchant-text guard makes that
   question appropriate for native empty entry. The preparation claim is removed.

3. **Code: Record greeting emission, `code`:** replace only the full greeting
   string inside `generatedText.includes(...)` with the introductory text. This
   recognizes the new fallback, the new native opening, and an old opening already
   present in conversation history. Updating this matcher prevents repeat greetings
   after the shorter opening. Preserve the rest of the offer-recording code.

Original field SHA-256 preconditions (UTF-8 field value, without JSON escaping):

| Field | SHA-256 |
|---|---|
| Job `instructions` | `cebfb6ca586f258605b07722712670e622fbca3ee80208a1bf9c6ac3494bee92` |
| Proactive `code` | `70066fd77df4462228cc2ec75e323770121fb195b49c237acda170f629509869` |
| Proactive `transpiled` | `2cfe729b39253247b5efe078a7fdc4cabbbfe53fb2e505bac1431ae7278c956e` |
| Recorder `code` and `transpiled` | `6a797f7b3cd53ee4e003981a6e2dafbcd925c856f3e6447abcf80d748271ae9a` |

If the current fields differ, compare the current revision before applying these
edits. Opening correction A alone does not fix the age-first gate failure.

### B. Approved channel-independent POC navigation exception

The business scope is approved for both voice and REST/text. Apply this candidate
only after the effective POC target and mutable-resource isolation are verified.

In the POC Job's `instructions`, insert the following section immediately before
the unique `# CANCELLATION DATE` heading, after applying A:

```text
# DIRECT GRABMART STATUS NAVIGATION — ISOLATED POC
This exception applies in this isolated POC to both voice and text conversations when the Merchant clearly identifies the current journey as GrabMart and explicitly asks only where or how to view cancelled-order compensation status. Platform and guidance style do not have to be known for this exception to apply. Retain the established intent, preferences, and confirmed location across follow-up messages such as Done. Do not activate this exception for an ambiguous or conflicting business line, an unresolved change of order, a request for eligibility or timing, a submission request, or a combined status-and-submission request.

Within this scope, this section takes precedence over the age-first intake, resolver-only business-line lookup, recent/older-order routing, loudspeaker setup, and mandatory start_guidance instructions. Safety, terminal-state handling, and greeting ownership still take precedence over this exception. Use the Merchant's explicit GrabMart statement for navigation only; do not infer it from screen labels or override a conflicting resolved business line.

Cancellation age and loudspeaker setup are not prerequisites for viewing the status screen. Do not ask for either before this navigation. Do not call resolve_order_age or start_guidance solely to enable this navigation-only path. Do not manufacture days_ago, threshold, a loudspeaker answer, or a resolved tool result. Use the supplied preferences and conversation history directly for this path.

Answer a direct status-location question from the supported GrabMerchant Portal route without first collecting walkthrough preferences. For requested guided steps, use preferences already supplied. If information is genuinely missing, ask only one necessary navigation question at a time and wait; missing platform or style must never return the Merchant to cancellation-age or loudspeaker intake. GrabMart status uses the Portal on a computer. Apply the existing app-to-Portal redirect or Portal-unavailable recovery when relevant. Do not re-ask known preferences or ask whether the Merchant wants guidance they already requested.

Follow GRABMART PORTAL — COMPENSATION STATUS and its ONE-BY-ONE SEGMENTATION. If the Merchant is already signed into the Portal and has requested one step at a time, instruct them to open Finance on the left sidebar and wait for confirmation. After they confirm Finance is open, instruct them to click the Transactions tab and wait. Continue from each confirmed location, with one route action per turn and the existing separate status-observation point. Preserve the existing once-only GrabMart partial-compensation notice before the first navigation action; it must accompany rather than replace that action.

This navigation does not establish preparation, packing, eligibility, approval, payment, or the status of an individual order. If the Merchant changes to an age-dependent question or submission journey, leave this exception and apply the existing rules using facts already supplied; ask only for facts that are genuinely missing for that new request.
```

This is an unapplied prompt candidate. The Job has `toolChoice="auto"`, which allows
a direct response when `start_guidance` is unavailable. The exception explicitly
uses that direct path. The tool's Resolve node only returns the selected arguments;
it performs no navigation or persistent guidance setup. Therefore this candidate
requires no fabricated age and no global relaxation of the tool condition. Actual
Agent behavior still requires verification after application.

The existing preparation/packing scope, threshold table, and voice preferences
are intentional project rules. This candidate changes their application to the
specified status-navigation path; it does not establish formal Grab policy.

### Static scope review

These are review expectations for the draft, not observed corrected replies:

| Situation | Required behavior |
|---|---|
| Explicit GrabMart status navigation, Portal open, one-by-one requested | Finance action immediately; Transactions only after acknowledgment; no age or loudspeaker intake |
| Status-location question with no preferences supplied | Answer the supported Portal location directly; missing preferences do not disable the exception |
| Requested walkthrough with genuinely missing navigation information | Ask only the necessary navigation question; retain the age/loudspeaker bypass |
| GrabMart status requested from the app or Portal unavailable | Preserve the existing Portal redirect or access-recovery behavior |
| Eligibility, timeline, submission, or combined status/submission request | Existing applicable intake and decision rules; this exception does not establish eligibility or approval |
| Status navigation followed by an age-dependent request | Leave the exception, reuse supplied facts, and collect genuinely required missing facts |
| Active emergency, including during navigation | Existing mandatory safety escalation takes priority |
| First clear merchant request | Required introductory disclosure once, then address the request; no preparation assumption or generic help question |
| Native empty entry or subsequent reply | Natural opening ownership; no unsupported preparation claim; no repeated greeting/disclosure |

## Isolation and verification

The package establishes local-node independence from the included `[MAIN]`, and
the user has confirmed the live Endpoint binding. Apply only the three identified
POC node fields using the [manual kit](poc-correction-2026-10-29/README.md).
The shared AI Agent, Knowledge Store, Tools, other nodes, and full-package import
are outside this edit set. Cognigy administration remains read-only under the
workspace guide, so saving these fields and producing the fresh export requires
the operator. No workspace access rule was changed.

After verified POC application:

1. Export the POC again. Check A's three fields and the inserted B section; check
   that the Endpoint selects that exact POC revision. Review the resulting diff.
2. Use fresh conversations with the existing, unmodified v0.2 scenario. Only after
   explicit authorization for five live runs, execute from the repository root
   with the verified POC URL configured locally:

   ```powershell
   .\.venv\Scripts\python.exe -m uc4_runner run --scenario GM-PORTAL-STEPS-001 --repeat 5
   ```

   This sends up to ten conversation requests. Test Mode still sends real requests.
3. Require all five runs to execute both turns: Turn 1 gives only the Finance
   navigation action; after the scripted confirmation, Turn 2 gives only the
   Transactions action. Require passing advancement gates, no App substitution,
   and consistent conversation identities. Review any warnings separately.
4. Inspect both replies for unsupported preparation/packing claims, redundant help,
   age diversion, loudspeaker intake, and repeated openings. The Portal scenario
   itself does not assert all these conversation-quality checks. The existing
   local symptom oracle checks the reported phrases alongside the real evaluator:

   ```powershell
   .\.venv\Scripts\python.exe "C:\Users\Nau\AppData\Local\Temp\opencode\uc4-portal-live-feedback.py" "reports/NEW_BATCH_ID"
   ```

   Phrase checks are targeted diagnostics; inspect paraphrases manually. A new
   captured batch is required to verify changed behavior. Regrading the stopped
   original batch cannot supply its unsent Turn 2 or verify a deployed correction.
5. Inspect a redacted execution trace for at least one new run: selected Flow/route,
   greeting emitter, Job revision, and tools used. Retest native empty entry and
   a later greeting-free reply if that entry will remain part of the POC. The
   five-run REST scenario does not verify voice behavior, missing-preference
   handling, or preserved eligibility/submission behavior; those checks need
   separately authorized conversations before broader behavioral validation is
   claimed.

## Checks actually executed

- Offline captured-evidence feedback: **RED in 5/5 runs**, and RED for minimized
  run 1. This reproduces the saved symptoms without sending requests.
- Read-only archive inspection and exact-string comparison: **5/5 recorded opening
  paragraphs match the required Job literal**.
- Offline Node probes against reviewed exported `code` and `transpiled` fields:
  captured first text suppresses proactive output; no-metadata business-line
  capture remains unresolved; unknown/recent ages leave guidance unavailable;
  Thursday GrabMart ages 0/7 are `within`, age 8 is `beyond`.
- In-memory candidate A probes: neutral native opening remains once-only; the
  updated recorder recognizes old/new openings and does not mark a Finance-only
  reply as a greeting. These probes do not execute the Cognigy runtime or an LLM.
- Original batch and ZIP integrity, replacement preconditions, local links,
  CLI example syntax, and whitespace were checked before handoff.
- Follow-up export: all 31 POC node configurations are identical to the original.
  In-memory application of the updated draft changes exactly five fields across
  three identified nodes: Job `instructions`, and `code`/`transpiled` for each of
  the two greeting nodes. All other resource values remain equal in that static
  comparison; JSON round-trip and exact replacement preconditions pass. The draft
  explicitly covers both channels and missing navigation preferences.
- Both supplied ZIP hashes and all 15 original batch-file hashes remain intact.
- Endpoint/ownership audit: the new exported Endpoint's `flowId` matches the POC;
  the two Flows have disjoint local node identities and local chart edges. Shared
  AI Agent/Knowledge Store dependencies were identified and excluded from the
  proposed edit set. The user subsequently confirmed the live revision selection.
- Manual application artifacts: exact complete field values, review diff, and
  before/after hashes were generated from sections A/B. Independent inverse-patch
  comparison restores the original Job instructions byte-for-byte; 40 original
  instruction sections are unchanged. The actual paste-ready Code files pass the
  once-only greeting and emission-recognition probes. See the
  [validation record](poc-correction-2026-10-29/VALIDATION.md).

Probe location:
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-export-probe.js`.
Original batch fingerprints:
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-portal-live-evidence-hashes.json`.
Deployment correction and live regression: **unverified**. No new conversation
requests or Cognigy administration writes were performed during this inspection.

## Platform references

Current Cognigy documentation was retrieved through Context7:

- [AI Agent Node](https://docs.cognigy.com/ai/agents/develop/node-reference/ai/ai-agent.md):
  Job-specific Instructions and Context, knowledge injection modes, and streaming
  result handling. Its Tool child-node documentation confirms that a false
  condition prevents the AI Agent from accessing the tool for that execution.
- [Packages](https://docs.cognigy.com/ai/platform-features/packages.md): exported
  resources, dependencies, and import conflict handling.
- [Endpoint settings](https://docs.cognigy.com/ai/agents/deploy/endpoints/overview.md):
  Flow reference selection, optional Snapshot, and Endpoint mocking.
- [Input object](https://docs.cognigy.com/ai/agents/develop/ai-agent-memory/input.md):
  `entrypoint` is the Project ID without a Snapshot, or the Snapshot ID when used.

Live documentation was also checked because the indexed source paths had moved.

These references explain platform behavior. The supplied configuration and
knowledge chunks are the evidence for this POC's business rules.
