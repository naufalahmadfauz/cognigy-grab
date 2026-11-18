# UC4 Knowledge Base coverage suite

## Purpose and evidence

Test answer content and business-policy boundaries using runner v0.2 against
`UC4_KB_AGENT_POC_v03`, with intended Knowledge Store `UC4_KB_POC_v03_TEST`.
New scenarios are in [scenarios/kb-coverage](../scenarios/kb-coverage/). The user
makes the final semantic PASS/FAIL assessment from captured conversations.

Three different claims must stay separate:

- **Planned article coverage:** a scenario asks about supported article content.
- **Correct answer content:** the recorded reply answers the merchant correctly,
  with the applicable business line, qualifications, and supported next action.
- **Verified retrieval:** same-conversation execution evidence shows Knowledge
  Search ran and identifies returned source/chunk content. Matching an article's
  answer alone does not establish retrieval; Job instructions may supply it.

The user's earlier **20/20 isolated retrieval result** is historical context,
not a new end-to-end result from this suite. For live review, record retrieval as
**verified**, **not observed**, or **not assessable from available evidence**,
separately from the semantic verdict. A trace ID is a correlation pointer, not
proof of a search or of the particular article used.

Existing reports retain normalized reply text, assertions, and available trace
IDs. Raw-response retention, when already enabled, may expose additional search
evidence but cannot guarantee it exists; inspect only the evidence actually
captured. This suite adds no retrieval instrumentation.

Cognigy documentation consulted through Context7 distinguishes Job Instructions
and Context from knowledge querying, and describes retrieved chunks with source
metadata:

- [AI Agent configuration](https://docs.cognigy.com/ai/build/node-reference/ai/ai-agent/)
- [Knowledge Search result metadata](https://docs.cognigy.com/ai/empower/knowledge-ai/knowledge-source/knowledge-source-tags/)

## Source inventory and authority

Reviewed the complete text of **17 articles / 20 chunks** in
[the latest local export](../flow/Package-Naufal_2026-10-29_06-47-07.zip).
Archive SHA-256:
`015b714019081f458b2d8f28047b68761e47c7fe6e7ddab68670ecb0684be6af`.
Store reference: `786b7a11-913c-4ec0-8a4e-e48352921d78`;
archive member: `knowledgeStore/6ae2ebf02f2c7932c4cad948`.

Article identity/title/version are in `knowledgeSource/*` → `data`; actual text
is in `knowledgeChunk/*` → `text`. Join chunks by `sourceReference` to source
`_id`, and sources by `storeReference` to the store `_id`. Chunk provenance is
`data.chunk_ref` and `data.claim_ids`; `order` gives chunk order. The logical chunk
IDs are the article ID plus `-C01`, and `-C02` for the three two-chunk articles.
These `.ctxt` names are source metadata, not standalone files in this checkout.

Every article is **v0.3.0**, market **MY**, language **en-MY**, with
`adoption=provisional_poc` and `formal_approval=pending`. All sources are ready and
all 20 chunks enabled in the export. Source text refers to project material and
indexed official information but provides no original policy URLs. Thus this is
coverage of the supplied provisional KB, not independent confirmation of public
Grab policy or current authenticated screens.

The export predates the approved direct GrabMart status-navigation exception.
For conversation constraints, also reviewed the
[approved POC decision](../flow/UC4-PORTAL-DIAGNOSIS-2026-10-29.md) and
[prepared Job instructions](../flow/poc-correction-2026-10-29/01-job-instructions.txt).
The user subsequently reported 5/5 live passes for the earlier two-turn Portal
scenario; a fresh post-correction configuration export is not present here.

### Article coverage matrix

Question examples below summarise the executable merchant scripts. The linked
YAML files hold the full messages and actual deterministic expectations.
All limitations/prohibited claims also belong to the final semantic review,
including those too subtle for the regex checks.

| Article ID — exact title | Scope / chunks | Supported facts and expected guidance | Limitations and prohibited claims | Representative question → planned test |
|---|---|---|---|---|
| **UC4-MY-GF-TIMING-001** — GrabFood usual approval and payout reference | GrabFood / 1 | Usually approved in **1–2 business days after the order was made**, then next regular payout cycle; subject to cancellation policy. | Approval, processing, payout and bank receipt differ. No guaranteed payment date or total-payment SLA; do not substitute 3–5 days. | “How long until approval and payment?” → [KB-GF-TIMING-AGE-001](../scenarios/kb-coverage/KB-GF-TIMING-AGE-001.yaml); bank-receipt distinction also in [KB-GF-STATUS-001](../scenarios/kb-coverage/KB-GF-STATUS-001.yaml). |
| **UC4-MY-GM-TIMING-001** — GrabMart usual approval and payout reference | GrabMart / 1 | Usually approved in **3–5 business days after the order was made**, then next regular payout cycle; subject to cancellation policy. | No guaranteed bank-credit date or total-payment SLA; do not substitute 1–2 days. | “How long until approval and payment?” → [KB-GM-TIMING-AGE-001](../scenarios/kb-coverage/KB-GM-TIMING-AGE-001.yaml). |
| **UC4-MY-GF-THRESHOLD-001** — GrabFood order age reference table | GrabFood / 1 | Mon–Sun elapsed-day cutoffs: **4, 4, 2, 2, 2, 3, 4**. At/below is recent; above is older. Older orders retain review/request guidance. | Internal journey selection, not eligibility, deadline or payment date. Timezone, time-of-day and effective version unconfirmed. Test covers recent/older extremes, not every weekday boundary. | “Cancelled today” then “Does 14 days old mean automatically ineligible?” → [KB-GF-TIMING-AGE-001](../scenarios/kb-coverage/KB-GF-TIMING-AGE-001.yaml). |
| **UC4-MY-GM-THRESHOLD-001** — GrabMart order age reference table | GrabMart / 1 | Mon–Sun elapsed-day cutoffs: **7, 7, 7, 7, 7, 8, 9**. Same recent/older interpretation and review path. | Calendar elapsed days, not a new business-day calculation; same unresolved conventions. Test covers extremes only. | “Cancelled today” then “Does 14 days old mean automatically ineligible?” → [KB-GM-TIMING-AGE-001](../scenarios/kb-coverage/KB-GM-TIMING-AGE-001.yaml). |
| **UC4-MY-GF-STATUS-001** — GrabFood compensation status in the app | GrabFood / 1 | GrabMerchant App → Orders → Cancelled → relevant order's displayed compensation status. Indexed guidance concerns current-month cancellations and auto-approved status. | Approved does not prove bank receipt. Missing order/link does not prove rejection. Authenticated screens untested; avoid substituting the GrabMart route. | “Show the status steps; does Approved mean my bank received payment?” → [KB-GF-STATUS-001](../scenarios/kb-coverage/KB-GF-STATUS-001.yaml). |
| **UC4-MY-GM-STATUS-001** — GrabMart compensation status in the portal | GrabMart / 1 | Portal → Finance → Transactions → relevant period/store → Category → Compensation for cancelled orders → observe whether compensated. | GrabFood's App status route does not apply. Missing transaction proves neither rejection nor bank receipt; screens untested. POC missing-order recovery rechecks period. | “Show all status steps; does a missing entry mean rejection?” → [KB-GM-STATUS-001](../scenarios/kb-coverage/KB-GM-STATUS-001.yaml). |
| **UC4-MY-GF-SUBMIT-001** — GrabFood compensation request route | GrabFood / 1 | Open cancelled order → Request for compensation when present → Report a payment dispute → scroll for form → order details/evidence → merchant submits. Missing link permits Portal alternative. | Missing link proves neither ineligibility nor wrong role. Current screens and early acceptance untested. Respect form-visibility and platform-switch observations. | “Guide me to the form” → [KB-GF-SUBMIT-001](../scenarios/kb-coverage/KB-GF-SUBMIT-001.yaml); “The App link is missing” → [KB-GF-MISSING-LINK-001](../scenarios/kb-coverage/KB-GF-MISSING-LINK-001.yaml). |
| **UC4-MY-GM-SUBMIT-001** — GrabMart compensation request route | GrabMart / 1 | Same supported App submission path with packed-items evidence; Portal-first submission starts at Help Centre. | App submission is allowed even though App status is not. No forced status detour; missing link and early acceptance limitations as above. | “Submit only, in the App” → [KB-GM-SUBMIT-001](../scenarios/kb-coverage/KB-GM-SUBMIT-001.yaml); Portal-first → [KB-PORTAL-SUBMIT-001](../scenarios/kb-coverage/KB-PORTAL-SUBMIT-001.yaml). |
| **UC4-MY-GF-EVIDENCE-001** — GrabFood evidence and no photo guidance | GrabFood / 2 | **C01:** prepared-food photo requested; may continue submission without already having it, with clear/complete supporting information. **C02:** adopted isolated-POC rule places cancellation before preparation outside compensation; missing photo does not prove unprepared food. | No automatic photo-based denial, exemption or approval. Substitutes/final evidence policy unconfirmed. Before-preparation applicability awaits formal confirmation, not an individual determination. | “Can I submit without a photo?” then “Does that prove no preparation; is the before-preparation rule confirmed?” → [KB-GF-EVIDENCE-001](../scenarios/kb-coverage/KB-GF-EVIDENCE-001.yaml); form evidence also [KB-GF-SUBMIT-001](../scenarios/kb-coverage/KB-GF-SUBMIT-001.yaml). |
| **UC4-MY-GM-EVIDENCE-001** — GrabMart evidence and no photo guidance | GrabMart / 2 | **C01:** packed-items photo requested; same no-photo continuation. **C02:** adopted isolated-POC rule places cancellation before packing outside compensation; missing photo proves no packing fact. | Same evidence uncertainty. Do not substitute prepared-food evidence or turn the provisional rule into confirmed final policy. | “Can I submit without a photo?” then packing-boundary follow-up → [KB-GM-EVIDENCE-001](../scenarios/kb-coverage/KB-GM-EVIDENCE-001.yaml); form evidence also [KB-GM-SUBMIT-001](../scenarios/kb-coverage/KB-GM-SUBMIT-001.yaml). |
| **UC4-MY-GF-SPLIT-001** — GrabFood eligible split large order cancellations | GrabFood / 1 | Eligible split large-order cancellations: automatic reimbursement, no merchant action, weekly GrabMerchant App record updates under policy. | Not every cancelled order. FAQ establishes no individual eligibility, amount, approval date or bank-credit date. Weekly record update is not weekly guaranteed payout. | “If eligible, must I claim, when does the record update, and is this for every cancellation?” → [KB-GF-SPLIT-001](../scenarios/kb-coverage/KB-GF-SPLIT-001.yaml). |
| **UC4-MY-GM-SPLIT-001** — GrabMart eligible split large order cancellations | GrabMart / 1 | Same conditional automatic reimbursement and weekly **App record** update. | Same guarantee limits. An App-record statement does not authorise substituting an App status-navigation route. | Same split-order question for GrabMart → [KB-GM-SPLIT-001](../scenarios/kb-coverage/KB-GM-SPLIT-001.yaml). |
| **UC4-MY-GM-PERISHABLE-001** — GrabMart partial compensation for perishable items | GrabMart / 1 | Partial compensation is based on assessment of perishable items; article also contains the existing “compensation will be partial” notice. | No percentage, formula, exhaustive perishable definition, full-value reimbursement or guaranteed award. Keep notice as observed wording with a separate certainty-review warning. | “Fixed percentage or guaranteed full value; what determines it?” → [KB-GM-PARTIAL-001](../scenarios/kb-coverage/KB-GM-PARTIAL-001.yaml). |
| **UC4-MY-SHARED-DEADLINES-001** — Order age and enquiry applicability | Shared / 2 | **C01:** internal age selects journey; older orders retain review. Public wording mentions enquiry within 90 days. **C02:** five working days investigation/response and at least three business days bank credit before contact describe separate stages. | UC4 applicability of these public periods unresolved. No automatic rejection beyond 90 days, indefinite submission rights, combined eight-day SLA, or replacement of product approval timing. | “Does 91 days mean rejected or unlimited rights?” then “Is five plus three an eight-day promise?” → [KB-DEADLINES-001](../scenarios/kb-coverage/KB-DEADLINES-001.yaml); older-order semantics in both timing/age scenarios. |
| **UC4-MY-SHARED-ELIGIBILITY-001** — Malaysia cancelled order eligibility examples | Shared / 1 | Examples: customer changes mind; incorrect address/location; no available delivery partner. Subject to cancellation policy/guidelines. | Non-exhaustive; an example does not determine individual eligibility, payable amount or date. | “Which reasons are examples; does a match guarantee approval?” → [KB-ELIGIBILITY-001](../scenarios/kb-coverage/KB-ELIGIBILITY-001.yaml). |
| **UC4-MY-SHARED-PORTAL-001** — Portal routes to the payment dispute form | Shared / 1 | Help Centre → (1) Search Bar, search dispute; (2) Common Problems → Payouts & Reports → Payout issues; (3) Browse by Services → Payment Services → Payment issues. All reach Report a payment dispute; scroll for form. | Menus untested. Failure is not wrong role/ineligibility. Only Search Bar is permitted by the current standard POC Job; alternate routes are deferred, not treated as required Agent behavior. | “Start my submission in Portal” → [KB-PORTAL-SUBMIT-001](../scenarios/kb-coverage/KB-PORTAL-SUBMIT-001.yaml); accepted App fallback → [KB-GF-MISSING-LINK-001](../scenarios/kb-coverage/KB-GF-MISSING-LINK-001.yaml). |
| **UC4-MY-SHARED-REQUEST-001** — Payment dispute form and submission role | Shared / 1 | Report a payment dispute; authorised **Owner or Manager** login to submit; merchant completes/submits the form. | Missing link/navigation failure is not proof of wrong role. Actual authenticated access/form visibility untested. Agent must not claim to have submitted for the merchant. | “Form still missing; which role may submit?” → [KB-PORTAL-SUBMIT-001](../scenarios/kb-coverage/KB-PORTAL-SUBMIT-001.yaml); self-submission in both App submission scenarios. |

## Suite design and POC decisions

**15 new scenarios / 26 scripted turns**, each initially run once. Files use schema
v1; individual versions are recorded with the offline results below. This separate
directory is selected with the existing `--scenarios-dir` flag. The three existing
packaged scenarios remain separate.

| Scenarios | Turns each | Why multiple turns / gate placement | Likely answer source, not a retrieval claim |
|---|---:|---|---|
| KB-GF-TIMING-AGE-001; KB-GM-TIMING-AGE-001 | 2 | Compare recent and older orders while retaining business line; independent factual follow-up, no gate. | Timing is fixed Job content; age is also Tool/Job routing. |
| KB-GF-STATUS-001; KB-GM-STATUS-001 | 2 | Gate complete status guidance before a scripted screen observation; then test interpretation. | Standard navigation is in the Job; factual boundary may also be in KB. |
| KB-GF-SUBMIT-001; KB-GM-SUBMIT-001 | 2 | Gate request entry and form-visibility question before claiming the form is visible. | Job directly provides request route, evidence and self-submission. |
| KB-PORTAL-SUBMIT-001 | 2 | Gate article/scroll guidance before reporting a missing form; test role requirements next. | Job prescribes Search Bar route and role handling. |
| KB-GF-MISSING-LINK-001 | 2 | Gate the Portal offer before accepting it; preserve preferences on the switch. | Job directly supplies the recovery sequence. |
| KB-GF-EVIDENCE-001; KB-GM-EVIDENCE-001 | 2 | Follow evidence advice with a challenge to inferred preparation/packing; no scripted navigation acknowledgment, no gate. | Evidence type is in the Job; no-photo/provisional-policy detail is a KB candidate. |
| KB-GF-SPLIT-001; KB-GM-SPLIT-001 | 1 | One conditional FAQ question each. | KB candidate for automatic reimbursement and record-update details. |
| KB-GM-PARTIAL-001 | 1 | Ask for unsupported amount certainty and the supported assessment basis. | Notice is in Job and KB; formula/award limitations are a KB candidate. |
| KB-ELIGIBILITY-001 | 1 | One examples-versus-entitlement question. | KB candidate. |
| KB-DEADLINES-001 | 2 | Follow the same enquiry's age uncertainty with response-versus-payment interpretation; no gate. | KB candidate; actual retrieval still needs evidence. |

Scenario prompts supply business line and, except for direct GrabMart status,
cancellation age. Guided requests also supply App/Portal, all-at-once style and
loudspeaker preference to minimise intake-only turns. “Today” is within all
listed cutoffs; 14 elapsed days is beyond all of them. There is no mocked weekday
or new clock control. The status-only GrabMart exception bypasses age and
loudspeaker intake for both voice and REST/text; it does not extend to submission
or eligibility questions.

The Job requires exact timing wording, but the suite checks the essential facts
rather than that entire literal sentence. For form evidence, use prepared food
for GrabFood and packed items for GrabMart. The Job's **recent GrabMart timing
reminder** says “photo of the order”; this suite does not wrongly fail that timing
reply for lacking the separate form-evidence wording.

Portal submission uses the Job's Search Bar route. The KB's other two Portal
routes remain inventoried as deferred branch coverage. Form filling follows a
merchant visibility observation; App-to-Portal switching follows acceptance.
None of the scripts claims that an actual form was submitted or accepts a
transfer. All screen observations are synthetic merchant messages, not browser
interactions.

## Interpretation

Deterministic assertions are screening checks. They tolerate configured wording
variants but can misread negation, attribution, implicit qualifications, and
novel paraphrases. UI labels and business-day ranges are intentional anchors.
Use [matching rules](TESTING_GUIDELINES.md#concept-matching) when investigating a
grade. The semantic reviewer should cite the reply, article, and any applicable
POC limitation rather than accept a regex verdict automatically.

For every live run, review all executed replies, mark unsent turns as untested,
and retain the original automated grade alongside the independent semantic
assessment. A stopped run does not demonstrate downstream coverage. Preserve
historical batches; capture any authorized rerun as a fresh conversation.

### Known coverage limits and policy review

- **No wholly unmapped article:** all 17 articles have executable planned coverage;
  both chunks of each two-chunk article have explicit prompts. Article mapping
  does not mean every claim, route branch or paraphrase has been exercised.
- **Threshold tables:** weekday cutoffs, equality boundaries, timezone and
  time-of-day behavior are not exhaustively tested. The Job keeps threshold
  values internal. This suite tests recent/older routing implications without
  demanding their disclosure or claiming to validate the resolver.
- **Portal alternatives:** Common Problems and Browse by Services branches are
  not executable expectations for the current standard Job. Current menu/form
  availability and actual authenticated Owner/Manager access remain unverified.
- **Scope sampling:** shared eligibility examples are exercised in a GrabFood
  conversation; shared deadlines in GrabMart; shared self-submission in both
  business lines; Owner/Manager access in the GrabMart Portal path. This is not
  every shared article crossed with both lines.
- **Unconfirmed policy:** percentages, evidence substitutes, final
  preparation/packing applicability, exact perishable definitions, real awards,
  approval/payment dates, early form acceptance and the UC4 applicability of the
  90/5/3-day statements cannot be established. Tests assess whether the Agent
  preserves those limits instead of inventing certainty.
- **Partial notice:** preserve its emitted wording. `partial-policy-review`
  records the potentially overconfident “will be partial” as WARN, not a gate
  failure. The no-fixed-amount/no-guaranteed-award expectations remain separate.
- **Regex limits:** keywords can occur in incorrect, quoted or negated claims;
  local exclusions can miss indirect or multi-clause claims. Ordered labels do
  not prove real screen actions. Amount/guarantee patterns catch selected forms,
  not every invented percentage or promise. These are reasons to read all replies,
  not to keep expanding the frozen engine.
- **Retrieval:** no new article/chunk retrieval coverage is claimed by this suite.
  Source citations without corresponding search evidence may be generated text.
  The previous 20/20 isolated result does not prove the Agent will retrieve those
  chunks in these conversations.

### Scenario-specific screening limits

| Scenario(s) | What the semantic reviewer must still check |
|---|---|
| KB-GF-TIMING-AGE-001; KB-GM-TIMING-AGE-001 | Approval range, order-made origin, payout and policy qualification must apply to the merchant's business line. A correct range mentioned only as a comparison is insufficient. Older-order review must actually remain available; weekday cutoffs are not checked. |
| KB-GF-STATUS-001; KB-GM-STATUS-001 | Action/label matches do not prove usable screens or an order's outcome. Read the full explanation of approval versus bank receipt, or missing entry versus rejection. Known negated instructions and bare-label routes are rejected, but other paraphrases can be misgraded. |
| KB-GF-SUBMIT-001; KB-GM-SUBMIT-001 | Check that the form really is the next scripted observation, the evidence is for the correct business line, and the merchant is the submitting actor. Keyword presence alone does not settle actor, permission or outcome. |
| KB-PORTAL-SUBMIT-001 | Search Bar guidance must search for dispute and wait at form visibility. Owner/Manager words must describe authorised access, without claiming the merchant's role is known. Other KB Portal branches are deliberately outside this walkthrough. |
| KB-GF-MISSING-LINK-001 | The question must genuinely offer a Portal switch; label/question matching cannot establish that by itself. The accepted-switch turn must use Portal controls, not retry the absent App link. |
| KB-GF-EVIDENCE-001; KB-GM-EVIDENCE-001 | No-photo continuation is neither an evidence waiver nor guaranteed approval. Uncertainty must qualify the preparation/packing rule itself; a qualification elsewhere in the answer is insufficient. No substitute evidence is confirmed. |
| KB-GF-SPLIT-001; KB-GM-SPLIT-001 | “Eligible” must qualify the automatic reimbursement rule. “Weekly” refers to the App record, not guaranteed weekly payout. The patterns cannot fully establish those relationships. |
| KB-GM-PARTIAL-001 | Read amount and award claims in full, including spelled-out percentages and indirect promises. Preserve the source notice as a separate certainty warning. |
| KB-ELIGIBILITY-001 | The three reasons must be non-exhaustive examples subject to policy, not an exhaustive entitlement test. A “policy” keyword alone is insufficient. |
| KB-DEADLINES-001 | Uncertainty must concern UC4 applicability, not an unrelated date. Investigation/response, bank credit and product approval are different stages; the cited periods establish no total-payment SLA. |

Identity assertions check request/echo continuity, not semantic understanding.
Factual follow-ups remain ungated so a wording failure does not unnecessarily
prevent the next independent question. Six procedural gates protect the scripted
observations or Portal-switch acceptance.

## Execution plan

1. Validate the suite offline. Dry-run each command below with `--dry-run` appended
   to inspect its script; this sends no requests and produces null grades.
2. After explicit live authorization, run each listed command **once** against the
   existing POC Endpoint configuration. Each command makes an independent
   conversation. Use the existing CLI repeatedly; there is no new batch executor.
3. Record the batch ID alongside its scenario. Read the COMPLETE manifest,
   `transcripts/run-001.md` and `runs/run-001.json`, then assess every executed
   reply against the matrix. Record semantic PASS/FAIL, article/chunk references,
   supporting text, untested turns, policy caveats and retrieval evidence status.
4. Reserve repetitions for an observed defect or high-risk inconsistency after
   review. A false regex failure remains visible alongside the semantic verdict;
   preserve all source evidence.

Offline validation from the repository root in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m uc4_runner validate --scenarios-dir scenarios/kb-coverage
```

### Initial live commands — prepared, not executed

Use these only after live authorization. Start with timing/age and factual
boundaries, then exercise the guided paths. Every command specifies `--repeat 1`.

```powershell
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-TIMING-AGE-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-TIMING-AGE-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-EVIDENCE-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-EVIDENCE-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-SPLIT-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-SPLIT-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-PARTIAL-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-ELIGIBILITY-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-DEADLINES-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-STATUS-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-STATUS-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-SUBMIT-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-SUBMIT-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-PORTAL-SUBMIT-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-MISSING-LINK-001 --repeat 1
```

Each command creates its own `reports/<batch-id>/` containing `manifest.json`,
`scenario.json`, `aggregate.json`, `summary.md`, `transcripts.json`,
`runs/run-001.json` and `transcripts/run-001.md`. All 15 completed first-pass
conversations would contain **26 executed turns**; gate or transport stops reduce
that count. See [report interpretation](../README.md#reports) for outcomes and exit
codes. A valid dry-run is a plan, not a behavioral pass.

## Offline verification results

Completed **2026-10-30**. Report IDs and report timestamps use UTC.

| Check | Result |
|---|---|
| Scenario validation | **15/15 valid** using the existing CLI and schema. |
| Existing mocked regression tests | **173 passed in 6.02 s**: scenario loading, assertions, advancement, and the existing full Portal status scenario. |
| New-scenario wording checks | **104/104 checks passed**, including a supported reply for every one of the 26 turns, numeric/quoted-label variants, policy qualifiers, negation, and deliberately incorrect replies. This tests the rubric, not the live Agent. |
| New-scenario mocked execution checks | **40/40 checks passed**: 15 complete scripted conversations; 17 expected gate stops covering all six gates; six empty-reply ERROR cases with unevaluated gates; non-blocking policy-warning progression; ungated factual continuation after a failure. Real sockets were blocked. |
| Article/chunk accounting | **17/17 article IDs** match the canonical export and map to executable scenarios. All **20 source chunks** are accounted for; the three C02 chunks have explicit follow-up prompts. Titles, source projection and archive hash matched. |
| Policy fidelity | Compared questions and expectations with the 20 source texts and prepared Job. Timing/business lines, evidence types, eligible-only split rules, provisional preparation/packing, unresolved 90/5/3-day applicability and Search Bar-only standard guidance agree with those sources. Formal policy remains pending. |
| Dry-runs | **15 current-version plans**, one per scenario: **26 planned turns**, **zero request attempts**, null run/turn grades and pass rates, and **six unevaluated gates**. All manifests COMPLETE; all seven expected report files present per batch. Saved scenario definitions, hashes, scripted messages and per-run/aggregate evidence agreed. |
| Commands and documentation | All **15 live commands parsed** with `--repeat 1` and each scenario selected exactly once. Relative links/heading anchors and whitespace checks passed; `git diff --check` passed. |
| Preservation | SHA-256 checks confirmed **134 pre-existing repository files** and **220 historical report files** unchanged, including the export. Source additions are exactly this document plus the 15 new YAML scenarios. |
| Live execution | **0 Cognigy conversation requests**. No new live answer-quality or retrieval result is claimed. |

The existing mocked-test command used during preparation was:

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_scenario.py tests/test_assertions.py tests/test_advancement.py tests/test_portal_status_full.py -p no:cacheprovider --basetemp 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-kb-coverage-ucnf_dge\existing-tests'
```

One-off verification inputs and results are retained locally in
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-kb-coverage-ucnf_dge`:
`check_wording.py` / `wording-results.json`,
`check_mocked_gates.py` / `mocked-results.json`, and
`check_artifacts.py` / `artifact-results.json`.
The preservation baseline is `before-files.json`; `kb-source.json` is the KB-only
projection used for policy review. The new suite itself needs only the existing
runner and the YAML files.

Offline counterexamples prompted narrower review-denial matching and action-aware
navigation gates; quoted UI labels remain accepted. Report inspection also found
that the draft eligibility concept named `address` was redacted as a sensitive
field. Its v0.1.1 definition uses `incorrect_location`, preserving the same
business expectation and a complete saved scenario. The earlier v0.1.0 dry-run
`20261029T213110972991Z-552eb7623ce1` remains intact; its corrected plan is below.
Thus there are **16 retained dry-run batches**, of which these 15 match the final
scenario versions. None sent requests.

### Current-version dry-run evidence

Each batch is under `reports/<batch-id>/`; open its `summary.md`,
`transcripts/run-001.md` and `runs/run-001.json`.

| Scenario | Version | Batch ID |
|---|---|---|
| KB-GF-TIMING-AGE-001 | 0.1.1 | `20261029T213058440837Z-4dcec7c2df8d` |
| KB-GM-TIMING-AGE-001 | 0.1.1 | `20261029T213058489048Z-665aa950670b` |
| KB-GF-EVIDENCE-001 | 0.1.0 | `20261029T213058509406Z-8b06da70733c` |
| KB-GM-EVIDENCE-001 | 0.1.0 | `20261029T213058518057Z-32f20ce4b938` |
| KB-GF-SPLIT-001 | 0.1.0 | `20261029T213058515060Z-22d4c2fc9925` |
| KB-GM-SPLIT-001 | 0.1.0 | `20261029T213110967086Z-b23428bec897` |
| KB-GM-PARTIAL-001 | 0.1.0 | `20261029T213110968456Z-1dac1760fe97` |
| KB-ELIGIBILITY-001 | 0.1.1 | `20261029T213614407787Z-d79fa7a545bb` |
| KB-DEADLINES-001 | 0.1.0 | `20261029T213111031404Z-f5bd9ce2e099` |
| KB-GF-STATUS-001 | 0.1.1 | `20261029T213111027058Z-a188cff01653` |
| KB-GM-STATUS-001 | 0.1.1 | `20261029T213118784571Z-61975ce52817` |
| KB-GF-SUBMIT-001 | 0.1.1 | `20261029T213118826009Z-54aaff831644` |
| KB-GM-SUBMIT-001 | 0.1.1 | `20261029T213118846831Z-6a08c4799b64` |
| KB-PORTAL-SUBMIT-001 | 0.1.1 | `20261029T213118822330Z-81a1a2e32bad` |
| KB-GF-MISSING-LINK-001 | 0.1.1 | `20261029T213118821000Z-fcf1af8ce83c` |
