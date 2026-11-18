# Four UC4 KB findings — focused diagnosis

**2026-10-30 · Preliminary diagnosis; candidate prepared, not applied.**

The four behavioral findings are confirmed by the recorded conversations. The
smallest supported proposal is **three clarifying paragraphs in the isolated POC
Job's existing instructions**. The supplied baseline already contains the correct
business-line recovery and form-visibility rules, and the KB already contains the
missing provisional facts. Live root cause and corrected behavior remain unverified.

## Evidence and authority

Source: [diagnosis evidence ZIP](../UC4_KB_v03_Codex_Diagnosis_Evidence_2026-10-30.zip).
Relevant members:

- `analysis/UC4_KB_v03_Live_Test_Review_2026-10-30.md`: independent assessment,
  **11 PASS / 2 PARTIAL / 2 FAIL** across the first 15-scenario pass.
- `reference_baseline/Package-Naufal_2026-10-29_13-33-26.zip`: verified October 29
  reference configuration, not proof of October 30 deployed state.
- `reference_baseline/01-job-instructions.txt`: approved October 29 instructions.
- `live_evidence/<scenario>/`: the four target conversations and supplied working
  `KB-GM-SUBMIT-001` comparison. All **35 files** match the corresponding original
  local live reports byte-for-byte.

The exported Job and approved text are identical after CRLF/LF and final-newline
normalization. The raw field hashes differ only for those formatting reasons.
[manifest.json](manifest.json) records the archive, field and normalized hashes.

The 17 KB sources and 20 enabled chunks have unchanged content, metadata, tags,
claim IDs and enabled state between the 06:47 and supplied 13:33 exports. Their
approval status remains `provisional_poc` / `formal_approval=pending`.

## Findings and proposed response

| Scenario | Confirmed observation | Baseline contract and candidate |
|---|---|---|
| **KB-GM-SPLIT-001** | Merchant explicitly names GrabMart. Agent says “I'll check the applicable GrabMart compensation guidance” and then asks whether it is GrabFood or GrabMart, leaving the FAQ unanswered. | `MERCHANT CONTEXT` and `CANCELLATION DATE` already require reuse of the stated LOB and a silent canonical-LOB follow-up when saved state is unresolved. Clarify that question-bearing/multi-sentence input still supplies the current-order LOB, and retain the pending factual question after resolution. |
| **KB-GF-SUBMIT-001** | Turn 1 navigates to the article/scroll step, then immediately directs details, prepared-food photo and submission. It never asks whether the form is visible. The runner correctly skips turn 2. | `REQUEST FOR COMPENSATION — GRABMERCHANT APP` already separates request entry and form completion, including `all_at_once`. Clarify that a visible request link or order details is not a visible form; stop after the form-visibility question. |
| **KB-GF-EVIDENCE-001** | Correct prepared-food/no-photo advice in turn 1; its Python `continue_request` failure is the review's known wording false negative. Turn 2 preserves uncertainty but omits the provisional before-preparation exclusion. | `UC4-MY-GF-EVIDENCE-001-C02` says the adopted isolated-POC assumption places cancellation before preparation outside compensation, with exact applicability pending formal Grab confirmation. Clarify that the rule and its formal status are both parts of the question. |
| **KB-GM-EVIDENCE-001** | Correct packed-items/no-photo advice. Turn 2 shifts from formal status of the before-packing rule to whether an individual award is confirmed, omitting the provisional exclusion. | `UC4-MY-GM-EVIDENCE-001-C02` contains the corresponding packing assumption and pending-confirmation qualifier. The same narrow completeness clarification covers both business lines without changing their KB content. |

The evidence-answer target is the paired meaning: **current provisional guidance
places before-preparation/before-packing cancellation outside compensation, while
exact applicability awaits formal Grab confirmation**. Missing photos prove
neither condition and establish no individual eligibility decision. Internal
article IDs or literal “POC” wording need not be spoken to the merchant.

## Hypotheses checked against available evidence

### 1. Business-line capture or resolver handoff

The baseline's `Code: Capture first-input LOB` deliberately accepts a bounded
grammar. Question marks and the supplied openings leave its saved LOB unresolved.
This is an intentional fallback boundary, not proof of the live defect's cause.

An offline Node.js VM replay executed the **unmodified exported initialization,
capture and resolver code**, using the five supplied first messages, empty request
data and a fixed October 30 clock:

```text
5/5: first-input capture leaves LOB unresolved
5/5: resolve_order_age(days_ago="14", lob="use_session") returns lobRequired=true
5/5: modeled canonical-LOB follow-up resolves the correct LOB and older-order route
```

Crucially, the working GrabMart submission conversation has the **same** initial
fallback. The deterministic code can recover using the already-approved second
call. This does not support broadening the parser or changing resolver state.
The missing live evidence is whether that call occurred, which arguments/results
were used, and what context reached the next LLM invocation.

**Candidate prediction:** an explicit current-order LOB guard reduces redundant
intake after an unresolved lookup. A trace showing the canonical follow-up already
succeeded would instead point to later prompt/context or answer handling.

### 2. Form visibility versus link visibility

The merchant says **Request for compensation is visible**, not that the form is
visible. The approved Job already demands an observation after article/scroll.
The working GrabMart comparison stops at “Is the form visible?” and completes
only on the later confirmation. GF and GM submission KB chunks are identical
after substituting the business-line name; the KB does not establish a different
GrabFood checkpoint.

**Candidate prediction:** distinguishing these observations explicitly prevents
all-at-once grouping across the existing decision boundary. The live trace is
needed to distinguish this interpretation error from an older effective prompt
or an answer composed from the unsplit KB route.

### 3. Retrieval omission versus incomplete answer composition

Both C02 chunks already contain the provisional exclusion and pending formal
confirmation. The evidence proves missing answer content, not missing retrieval.
The supplied Job uses on-demand knowledge, context-aware search prompt generation
and topK=3; none establishes which chunks were returned in these runs.

**Candidate prediction:** retaining the preparation/packing condition and its
formal-status question together improves completeness when that guidance is
available. If C02 was absent, targeted query/results evidence is needed; if it was
present, omission occurred in answer composition. The candidate preserves the
existing unknown-information fallback instead of inventing an unavailable rule.

## Trace correlation register

These are the original executed turns, all HTTP 200. Their reports have
`rawEvidenceRetained=false` and `rawResponse=null`; no Cognigy internal trace bodies
are included. A correlation ID is not proof of a resolver call or KB retrieval.

| Scenario / turn | UTC input time, 2026-10-30 | Trace ID |
|---|---|---|
| GF evidence / 1 | 04:12:24.653 | `endpoint-httpIncomingMessage-544afce2-3fde-41f2-bf47-5a2ff07cfbf0` |
| GF evidence / 2 | 04:12:36.429 | `endpoint-httpIncomingMessage-16f6e859-e7a5-439f-ac2f-fe9305a6a1fd` |
| GM evidence / 1 | 04:12:43.719 | `endpoint-httpIncomingMessage-2224a40a-5c0d-4dd8-b267-f0688f5258c5` |
| GM evidence / 2 | 04:12:51.381 | `endpoint-httpIncomingMessage-e08c16da-ef37-42a5-a147-1bc3b8548a79` |
| GM split / 1 | 04:13:03.820 | `endpoint-httpIncomingMessage-6a20f1e6-cf0b-42a2-993e-fb156faee3ed` |
| GF submit / 1 | 04:14:09.339 | `endpoint-httpIncomingMessage-0297e381-1542-45dd-a47a-8fbdf508fe87` |

Optional evidence to refine the preliminary diagnosis: a current served-revision
export; the GM split resolver arguments/results and effective conversational
context; the GF submission effective Job/guidance settings; and the evidence
follow-ups' knowledge queries, returned C02/source metadata and LLM prompt.
Cognigy's [AI Agent documentation](https://docs.cognigy.com/ai/build/node-reference/ai/ai-agent/)
describes Job, knowledge-result, system-prompt and tool-definition logging. Their
availability is not evidence that historical logs were enabled. No logging or
other configuration was changed for this investigation.

## Correction scope

The candidate targets only POC Job reference
`e38e5029-d515-4002-ad03-dd99b0eb821e`, owned by POC Flow
`17f129de-69b3-4828-bc4f-0c7d19ef41ce`.

The 06:47 audit export shows separate 31-node POC and 31-node `[MAIN]` sets with
zero shared node references. The 13:33 package retains all POC references but
omits `[MAIN]`. Both use shared AI Agent
`3c1b0294-6016-4b52-8478-afd6cc05a434`; its Knowledge Store is
`786b7a11-913c-4ec0-8a4e-e48352921d78`. POC naming does not make those shared
resources safe correction targets.

The three insertions retain every original Job character, including approved
status exceptions, safety/greeting/terminal priorities, one-by-one checkpoints,
role retry, Search Bar navigation, timelines and partial-compensation wording.
No Code node, Tool definition, memory injection, retrieval setting, shared
resource, Python file, scenario or historical report is edited.

See [application and regression plan](README.md) and the
[offline configuration-diff result](verification.json). They establish candidate
scope and provenance, not a deployed fix or a new semantic PASS.
