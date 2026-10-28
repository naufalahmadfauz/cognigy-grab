# Runner workflow

To regrade saved evidence, follow the [offline regrade workflow](../TESTING_GUIDELINES.md#offline-regrade-workflow).
For implementation or documentation changes, use the steps below.

## 1. Load the affected contract

Read the sections for each affected behavior before editing:

| Change | Reference |
|---|---|
| Scenario syntax or grading | [Scenario schema and rules](../TESTING_GUIDELINES.md#scenario-schema-v1); the affected scenario definition holds its executable expectations |
| Run isolation or turn sequencing | [Data flow and identities](../ARCHITECTURE.md#data-flow-and-identities) |
| Endpoint transport or error handling | [REST behavior](../ARCHITECTURE.md#rest-behavior) |
| Transcript normalization or trace extraction | [Normalization](../ARCHITECTURE.md#normalization) |
| Regrade validation, evaluation, or provenance | [Offline regrading](../ARCHITECTURE.md#offline-regrading) |
| Report outcomes or rates | [Outcome interpretation](../TESTING_GUIDELINES.md#outcomes-and-report-interpretation) and [reliability denominators](../ARCHITECTURE.md#evidence-and-reliability) |
| Evidence storage or new output paths | [Redaction boundary](../ARCHITECTURE.md#redaction-boundary) |
| Installation, configuration, or CLI | [Operator guide](../../README.md); current options come from CLI help and dependency declarations from `pyproject.toml` |

When changing an existing tradeoff, read [decisions](../DECISIONS.md) and identify
which choice the change revises. Keep the contract's explanation in its linked
document so future edits have one authoritative location.

Proceed when every affected behavior has a contract reference and any revised
tradeoff is identified.

## 2. Verify the changed behavior

Use the [test command](../../README.md#tests) and
[offline test conventions](../TESTING_GUIDELINES.md#development-verification-and-future-regression-use).
Select checks for every affected boundary:

| Boundary | Completion evidence |
|---|---|
| Runtime logic | Relevant mocked tests pass; changed behavior has accepted and deviating examples |
| Scenarios or grading | Scenario validation and matching regression examples pass; changed expectations have a new scenario version |
| Regrade implementation | Mocked regression checks satisfy the [regrade completion criteria](../TESTING_GUIDELINES.md#offline-regrade-workflow); incompatible evidence is rejected before output creation |
| Scheduling or reports | Mocked multi-turn batch checks pass for isolation, turn order, and report metrics; inspect affected generated artifacts |
| CLI planning | Offline validation and dry-run succeed; planned outcomes remain unevaluated |
| Packaging | A non-editable installation can validate the packaged scenario from outside the checkout |
| Documentation only | Relative links and heading anchors in changed files resolve; examples agree with CLI help or their referenced sources; `git diff --check` passes |

Verification is complete when all applicable checks pass. Record a blocked check
as unverified, with the blocker and remaining check named.

## 3. Report the evidence

List the checks actually executed and their results, labeling mocked, dry-run,
offline regrade, and live evidence explicitly. [VERIFICATION.md](../VERIFICATION.md)
is a dated historical record; preserve its original scope when adding results for
a new change.
