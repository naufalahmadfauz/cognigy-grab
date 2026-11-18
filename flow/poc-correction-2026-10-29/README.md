# Apply the approved three-node POC correction

**Status: prepared for manual application.** The user has confirmed the live
Endpoint's Flow reference, Snapshot/current-Project selection, and runner
destination. Cognigy administration remains read-only for this agent.

Target Flow: **UC4_KB_AGENT_POC_v03**

Flow reference: `17f129de-69b3-4828-bc4f-0c7d19ef41ce`

## Apply

Open the verified POC Flow in Cognigy. Replace the **complete contents of the one
specified field** in each row with its linked UTF-8 file, then save that node.
The files contain full field values, including all preserved instructions/code.

| Node | Stable node reference | Field to replace | Exact content |
|---|---|---|---|
| Grab Cancelled Order Compensation | `e38e5029-d515-4002-ad03-dd99b0eb821e` | Job **Instructions and Context** (`config.instructions`) | [01-job-instructions.txt](01-job-instructions.txt) |
| Code: Proactive greeting once | `3c8ee6d5-d094-41ec-b4e0-ab73161abbcf` | Code (`config.code`) | [02-proactive-greeting.js](02-proactive-greeting.js) |
| Code: Record greeting emission | `d438fa76-736e-4027-b6f4-86fbee9495c1` | Code (`config.code`) | [03-record-greeting.js](03-record-greeting.js) |

For the first row, edit the **Job node**, not the shared AI Agent's configuration.
For the Code nodes, let Cognigy regenerate `config.transpiled` when saving.
Use the existing nodes and references. Apply these field edits only; importing or
replacing the full package is outside this correction.

The source is the 06:47 export. [manifest.json](manifest.json) records its SHA-256,
the baseline member IDs, and the before/after field hashes. If a field has changed
since that export, compare the difference before overwriting it.

Review [changes.diff](changes.diff) for the precise edits. Their authoritative
specification is sections A and B of the
[diagnosis report](../UC4-PORTAL-DIAGNOSIS-2026-10-29.md#smallest-proposed-correction).

## Return a fresh export for verification

1. After saving all three nodes, export the edited POC Flow with its dependencies
   using **⋮ → Export as Package**. Save the new ZIP in `flow/` with a fresh name.
2. To verify `[MAIN]` as well, include it in the read-only audit export alongside
   the POC and shared dependencies, matching the scope of the 06:47 baseline.
   A POC-only export can verify the POC fields and included dependencies, but
   cannot prove that an omitted `[MAIN]` is unchanged.
3. Provide that ZIP and confirm whether the edited revision is the revision served
   by the already-verified Endpoint. If the Endpoint serves a Snapshot, identify
   the Snapshot; saving a source Flow alone does not update a Snapshot. Endpoint
   or Snapshot deployment changes are outside this three-node edit set.

The comparison will match resources by stable references, account for regenerated
package-local IDs, and report metadata changes separately. Expected content changes:

- One Job `instructions` field, exactly matching file 01.
- Two Code `code` fields, exactly matching files 02 and 03.
- The corresponding two generated `transpiled` fields, reviewed against that code.

All other POC fields, `[MAIN]`, shared AI Agent/Knowledge Store content, Tool
conditions, and chart structure must match the baseline for a full-scope result.

**Do not run live tests yet.** The existing `GM-PORTAL-STEPS-001` five-run regression
remains reserved for separate authorization after application verification.

See [VALIDATION.md](VALIDATION.md) for the checks completed on these local artifacts.
