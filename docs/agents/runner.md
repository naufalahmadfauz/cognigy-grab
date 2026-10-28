# Runner workflow

## 1. Load the affected contract

Read the sections for each affected behavior before editing:

| Change | Reference |
|---|---|
| Scenario syntax or grading | [Scenario schema and rules](../TESTING_GUIDELINES.md#scenario-schema-v1); the affected scenario definition holds its executable expectations |
| Run isolation or turn sequencing | [Data flow and identities](../ARCHITECTURE.md#data-flow-and-identities) |
| Endpoint transport or error handling | [REST behavior](../ARCHITECTURE.md#rest-behavior) |
| Transcript normalization or trace extraction | [Normalization](../ARCHITECTURE.md#normalization) |
| Report outcomes or rates | [Outcome interpretation](../TESTING_GUIDELINES.md#outcomes-and-report-interpretation) and [reliability denominators](../ARCHITECTURE.md#evidence-and-reliability) |
| Evidence storage or new output paths | [Redaction boundary](../ARCHITECTURE.md#redaction-boundary) |
| Installation, configuration, or CLI | [Operator guide](../../README.md); current options come from CLI help and dependency declarations from `pyproject.toml` |

When changing an existing tradeoff, read [decisions](../DECISIONS.md) and identify
which choice the change revises. Keep the contract's explanation in its linked
document so future edits have one authoritative location.

## 2. Verify the changed behavior

Use the [test command](../../README.md#tests) and
[offline test conventions](../TESTING_GUIDELINES.md#development-verification-and-future-regression-use).
Select checks for every affected boundary:

| Boundary | Completion evidence |
|---|---|
| Runtime logic | Relevant mocked tests pass; changed behavior has accepted and deviating examples |
| Scenarios or grading | Scenario validation and matching regression examples pass; changed expectations have a new scenario version |
| Scheduling or reports | Mocked multi-turn batch checks pass for isolation, turn order, and report metrics; inspect affected generated artifacts |
| CLI planning | Offline validation and dry-run succeed; planned outcomes remain unevaluated |
| Packaging | A non-editable installation can validate the packaged scenario from outside the checkout |
| Documentation only | Changed relative links resolve and examples agree with their referenced sources |

Verification is complete when all applicable checks pass. Record a blocked check
as unverified, with the blocker and remaining check named.

## 3. Report the evidence

List the checks actually executed and their results, labeling mocked, dry-run, and
live evidence explicitly. [VERIFICATION.md](../VERIFICATION.md) is a dated historical
record; preserve its original scope when adding results for a new change.
