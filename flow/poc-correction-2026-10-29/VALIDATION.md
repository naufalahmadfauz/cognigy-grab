# Three-node correction — local validation

**Result: paste-ready artifacts validated; Cognigy application and fresh-export
verification are pending. No live tests were executed.**

Baseline: `Package-Naufal_2026-10-29_06-47-07.zip`

SHA-256: `015b714019081f458b2d8f28047b68761e47c7fe6e7ddab68670ecb0684be6af`.

## Exact edit set

Paths are beneath each node's `/localizedData/0/config`.

| Stable node reference | Manual field | Additional generated field |
|---|---|---|
| `e38e5029-d515-4002-ad03-dd99b0eb821e` | `instructions` | None |
| `3c8ee6d5-d094-41ec-b4e0-ab73161abbcf` | `code` | `transpiled` |
| `d438fa76-736e-4027-b6f4-86fbee9495c1` | `code` | `transpiled` |

The [manifest](manifest.json) records exact baseline member IDs and field hashes.
The two projected `transpiled` hashes describe a literal replacement in the
baseline compiler output. Cognigy's actual regenerated output will be inspected
from the fresh export; no actual compiler output has been claimed here.

## Executed checks

Artifact generation command, executed from the repository root:

```powershell
.\.venv\Scripts\python.exe "C:\Users\Nau\AppData\Local\Temp\opencode\prepare-uc4-poc-correction.py"
```

Observed output:

```text
PASS: approved baseline and all three source-field hashes match.
PASS: exact diagnosis A/B replacements generated as three complete paste-ready fields.
PASS: in-memory candidate differs only in 3 nodes / 5 export fields.
PASS: MAIN, shared resources, Tool conditions, and all other values unchanged in candidate.
PASS: candidate JSON round trip and known-credential exclusion.
```

An independent comparison of the generated Job field against the original also
passed:

```text
PASS: all artifact SHA-256 hashes match the manifest.
PASS: reversing precisely the approved edits restores the original Job instructions byte-for-byte.
PASS: 40 original instruction sections unchanged, including safety, policy, age/submission, Finance/Transactions segmentation and tool rules.
PASS: exactly one approved direct-status section inserted; no scenario-specific trigger or generated reply substituted.
```

Code-node probe command:

```powershell
node "C:\Users\Nau\AppData\Local\Temp\opencode\verify-uc4-poc-correction.cjs"
```

Observed results:

- Baseline exposes the native preparation claim and does not recognize the new
  shortened opening in its greeting recorder.
- Paste-ready Code passes native once-only greeting, merchant-text and timeout
  suppression, recognition of old/new openings and supported structured output,
  no false greeting match for a Finance-only reply, and retained offer recording.
- Projected compiler-output variants pass the same probes.

These probes execute reviewed JavaScript with stubbed `api.say`/`api.log` and
isolated input/context. They do not run a Cognigy conversation or an LLM.

Both supplied ZIP hashes and all 15 original batch-file hashes were also checked.
The original baseline/evidence remains intact.

## Remaining verification

The user must save the three node fields and provide a fresh export. At that point
compare the observed resource definitions against the baseline and these files,
including generated code and protected dependencies. A locally generated
candidate is not evidence of a Cognigy save or deployment.

Behavioral verification remains the existing five-run `GM-PORTAL-STEPS-001`
regression after separate authorization. Source preservation does not prove that
the LLM will follow the amended priority in every conversation.
