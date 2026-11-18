# Minimal UC4 KB correction candidate

**Status: proposed, not applied. No live requests made.**

[Focused diagnosis](DIAGNOSIS.md) · [Three-hunk diff](changes.diff) ·
[Hashes and edit locations](manifest.json) · [Offline verification](verification.json)

The supplied handoff supports a preliminary correction against its verified
October 29 baseline. Live root cause remains unverified. This kit contains three
additions to **one isolated POC Job field**, preserving the existing instructions.

## Application instructions

After approval to apply the candidate:

1. Open Flow **UC4_KB_AGENT_POC_v03**, stable reference
   `17f129de-69b3-4828-bc4f-0c7d19ef41ce`.
2. Select its **Grab Cancelled Order Compensation Job**, stable node reference
   `e38e5029-d515-4002-ad03-dd99b0eb821e`. The editable field is **Instructions and
   Context** (`config.instructions`; baseline JSON pointer in the manifest).
   Identify it by ownership/reference, since `[MAIN]` has a similarly named Job.
3. Capture the current field/revision before editing. Compare it with the supplied
   approved text or the manifest's normalized baseline hash. If there are substantive
   intervening changes, review and rebase these insertions onto that current field
   rather than replacing it with the old full Job. A current export is optional
   for this preliminary proposal, but is needed for verified deployment comparison.
4. Append each linked paragraph to the specified section, once, preserving the
   existing text and a blank line between paragraphs:

| Exact paragraph | Append to section | Immediately before next heading |
|---|---|---|
| [01-explicit-lob.txt](01-explicit-lob.txt) | `MERCHANT CONTEXT` | `CURRENT ORDER LOB CORRECTION` |
| [02-provisional-evidence.txt](02-provisional-evidence.txt) | `KNOWLEDGE` | `SPEECH UNDERSTANDING` |
| [03-form-visibility.txt](03-form-visibility.txt) | `REQUEST FOR COMPENSATION — GRABMERCHANT APP` | `PORTAL SUBMISSION — SEARCH BAR ROUTE` |

5. Save that Job field. Export the edited POC and dependencies under a fresh name
   for comparison. Confirm that the Endpoint serves the edited revision; the
   supplied reference package includes no Endpoint/Snapshot binding. If it serves
   a Snapshot, use the existing operator deployment process after confirming the
   revision. Saving a source Flow alone does not prove what the Endpoint serves.

`changes.diff` is an additions-only unified diff of a normalized text projection
named `poc-job-instructions.txt`, with zero context to avoid reproducing long
unchanged paragraphs. Use the section locations above for the manual edit; this
is not a full-package import or a replacement Job. The two evidence scenarios
share one completeness clarification; the factual exclusion remains KB-grounded.

### Configuration-diff verification after application

Compare pre/post exports by stable resource references, resolving package-local
ID remapping before comparing content. The only intended content difference is
the three paragraphs in the specified POC Job `instructions` field. Treat export
timestamps, package-local IDs and any editor-generated preview differences as
metadata to inspect separately, not extra business changes to approve silently.

Verify all remaining Job fields, Code nodes, Tool conditions/parameters/answers,
chart edges, Flow settings and all 39 included shared Agent/Store/source/chunk
entries are unchanged. Compare the normalized field hash with the candidate hash
when the baseline matched exactly; a rebased candidate needs its own reviewed
diff and hash. Include `[MAIN]` in a pre/post read-only audit export if independent
confirmation of its deployed state is required: it is absent from the supplied
13:33 package, so that package cannot prove its current state.

For rollback, remove only the three exact inserted paragraphs from this field.
Preserve unrelated intervening edits. Offline removal restores the original
baseline field byte-for-byte.

## Verification completed

| Check | Observed result |
|---|---|
| Evidence integrity | **35/35** supplied live files match the originals. |
| Job baseline | Approved text and exported field match after line-ending/final-newline normalization. |
| Deterministic baseline replay | **5/5** supplied openings use the unresolved-LOB fallback; the modeled existing canonical follow-up resolves each correctly. Includes the working GM submission control. |
| KB baseline | All **17 sources / 20 chunks** enabled; relevant facts present. All KB content and shared Agent unchanged between the two reference exports after ID remapping. |
| Candidate configuration diff | **76 members compared; one changed leaf field**, three added paragraphs, zero deleted original characters. Other **30 POC nodes** and **39 shared entries** unchanged. |
| Patch consistency | The three-hunk diff reconstructs the candidate exactly. Removing insertions restores the original raw field. File and field SHA-256 values match the manifest. |
| Preservation | **151 pre-existing source files / 442 historical report files** unchanged. |
| Agent correction verification | **Not executed.** Static checks do not replay the LLM or establish live recovery. |

The verified candidate adds **1,921 characters** using the exported CRLF line
endings. No full Job replacement is distributed. Supporting one-off checks and
results are retained in
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-kb-diagnosis-ey4dwjbt`:

```powershell
node 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-kb-diagnosis-ey4dwjbt\check-resolver-baseline.cjs'
.\.venv\Scripts\python.exe 'C:\Users\Nau\AppData\Local\Temp\opencode\uc4-kb-diagnosis-ey4dwjbt\verify-candidate.py'
```

These checks are offline diagnostic artifacts; they add no runner/test-framework
feature. The Node check models resolver calls, not the unobserved live call chain.

## Focused regression plan

After application/diff verification and **separate live-request authorization**,
run only these four existing scenarios **once each**. Their full scripts contain
**seven turns**; the existing GF submission gate may suppress its second turn.

```powershell
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-SPLIT-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-SUBMIT-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GF-EVIDENCE-001 --repeat 1
.\.venv\Scripts\python.exe -m uc4_runner run --scenarios-dir scenarios/kb-coverage --scenario KB-GM-EVIDENCE-001 --repeat 1
```

| Scenario | Independent semantic acceptance |
|---|---|
| KB-GM-SPLIT-001 | Retain explicit GrabMart context without re-asking LOB. Answer conditional eligible split-order automatic reimbursement, no merchant action and weekly **App record** updates. Do not generalize to every cancellation or promise an amount/date. |
| KB-GF-SUBMIT-001 | Turn 1 ends at the form-visibility question after article/scroll, without details/evidence/submission instructions. Only after the scripted visibility confirmation does turn 2 give order details, prepared-food evidence and merchant self-submission. Both turns must execute for complete coverage. |
| KB-GF-EVIDENCE-001 | Preserve correct photo/no-photo continuation. Follow-up explains the provisional before-preparation exclusion **and** pending formal applicability; missing photo proves neither unprepared food nor ineligibility. |
| KB-GM-EVIDENCE-001 | Same, using packed items/before-packing. Answer the rule's formal status rather than substituting uncertainty about an individual award. |

Record each new batch ID and retain original Python outcomes, transcripts,
HTTP/errors, traces and any unsent turns. Continue to the other authorized
scenarios after FAIL, without automatic fixes or repetitions. Read the replies
independently: the known GF no-photo regex false negative may still occur, and
correct content alone does not establish KB retrieval. If execution/search
evidence is available, correlate it with the new run instead of assuming a tool
call or C02 retrieval from the reply. Existing approved behavior outside these
four scenarios is preserved statically; no broader live regression is claimed.
