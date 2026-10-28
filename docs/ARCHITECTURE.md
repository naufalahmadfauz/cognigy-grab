# Architecture — v0.1.1

## Components

```text
CLI (cli.py)
  ├─ environment + local .env (config.py)
  ├─ YAML/JSON validation + semantic scenario hash (scenario.py)
  └─ batch planning + bounded run scheduling (runner.py)
       └─ one sequential conversation per worker
            ├─ Cognigy REST POST (client.py)
            ├─ transcript normalization + trace extraction (normalize.py)
            └─ shared captured-run evaluation (assertions.py)
       └─ metrics + redaction + artifact writing (reports.py, redact.py)

CLI regrade (regrade.py)
  ├─ recorded aggregate JSON → compatibility validation → copied run evidence
  ├─ same captured-run evaluation (assertions.py)
  └─ grade comparison + same report writer → fresh REGRADE directory
```

`uc4_runner/scenarios/GM-CONTINUITY-001.yaml` is packaged with the application so
the default scenario also works after a wheel installation, outside the checkout.
`examples/STATUS-LOCATION-JSON.json` demonstrates the same schema in JSON.

The application needs no Cognigy plugin, OpenCode/Codex session, LLM grading API,
database, or external reporting service. Only a real `run` constructs an HTTP client.

## Data flow and identities

1. Validate all selected scenario files and environment settings before execution.
2. Generate a unique batch directory and one run UUID, synthetic user UUID, and
   synthetic session UUID for each repetition. IDs never derive from merchant PII.
3. Write a STARTED manifest and a redacted copy of the scenario definition.
4. In each run, send each merchant message with the same `userId` and `sessionId`.
   The body is exactly `{userId, sessionId, text, data: {}}`; local run identifiers
   are correlated in reports rather than injected into Flow data.
5. Capture response status, JSON or non-JSON body, timing, echoed identities, and
   trace IDs. Interpret only documented user-facing fields for assertions.
6. On transport/protocol error, stop that session and record subsequent turns as
   SKIPPED. Grade the captured run with `assertions.evaluate_run`, preserving
   chronological merchant/reply context. A behavioral failure does not suppress
   follow-up turns. Other independent runs continue.
7. Redact evidence before writing per-run checkpoints and transcripts. Finalize
   aggregate JSON, Markdown summary, and the COMPLETE manifest.

The default scheduler is sequential. With `--concurrency N`, a bounded thread pool
owns **whole runs**, so two turns of one session are never in flight simultaneously.
Run-delay spacing applies to submissions; request-delay spacing applies per
conversation, not as a global rate limiter. Each run has its own HTTP client and
cookie jar. Completed reports are ordered by run index regardless of finish order.

## REST behavior

- Test Mode inserts `/test/` immediately before the final token. Already transformed
  URLs are accepted; an explicit Test Mode false / `/test/` URL conflict is rejected.
- Optional authentication uses `x-cognigy-endpoint-key`; the legacy header can be
  selected explicitly. No authentication is sent when the key is blank.
- HTTPS certificate verification remains enabled. Redirects and automatic retries
  are disabled. Proxy environment variables are not inherited.
- Timeout is an HTTPX operation/inactivity timeout. A timeout or network exception
  cannot tell whether Cognigy consumed the message, so it is never replayed.
- HTTP failures, malformed JSON, unsupported response shapes, and empty/non-text
  replies are ERRORs. A 2xx response can therefore have a zero usable-reply rate.
- Cognigy request URLs, credentials, request headers, cookies, and exception strings
  are excluded from evidence metadata.

## Normalization

The raw response and normalized conversation are separate representations.

1. Prefer nonempty top-level `text`, Cognigy's documented combined reply. Do not
   append `outputStack` to it.
2. When combined text is absent/empty, read string `text` values of bot entries in
   `outputStack`, in order. Ignore internal `data` and non-bot entries.
3. Collapse adjacent increasing prefix snapshots and a final copy of a preceding
   multi-fragment suffix. Preserve earlier independent messages, such as a greeting.
4. If combined text exactly equals the stack's raw concatenation and that stack has
   redundant streaming fragments, use the collapsed stack instead. Otherwise
   preserve the combined text as authoritative.
5. Preserve unmarked identical utterances: deleting all duplicates would hide
   repeated-greeting defects. `normalizationNotes` explains any collapse.

These are conservative text heuristics for JSON REST responses, not an SSE client
or a guessed streaming metadata protocol. Arbitrary overlapping token streams,
custom transformer wrappers, and inconsistent top-level/stack content need an
adapter based on a reviewed response sample. Raw evidence preserves all fragments
subject to redaction. Assertions additionally normalize Unicode dash/apostrophe
variants, horizontal whitespace, and Markdown emphasis without rewriting transcripts.

Trace extraction visits JSON `traceId`/`traceIds` fields recursively and allowlisted
headers `x-trace-id`, `x-request-id`, and `traceparent`. Values are deduplicated in
first-seen order. No trace is invented when the Endpoint omits one.

## Assertion and result model

Scenario YAML declares the compensation policy; `assertions.py` evaluates it.
The HTTP client handles transport independently. When changing rule syntax or
semantics, use the [schema reference](TESTING_GUIDELINES.md#scenario-schema-v1).

An assertion records ID, type, turn, category, severity, outcome, reason, and supporting
evidence. For result meanings and precedence, use
[outcome interpretation](TESTING_GUIDELINES.md#outcomes-and-report-interpretation).

Identity checks validate requests against the planned run and compare response
echoes when present. Missing echoes produce a warning, not a claim of verified
server continuity. Business-context continuity is evaluated independently using
the follow-up navigation, product, and re-asking rules.

## Evidence and reliability

The aggregate includes all conversations, scenario ID/version/hash, runner/Python
version, credential-free configuration, defects, and separate metric denominators.
Per-run JSON retains full redacted raw responses only when opted in. Non-JSON error
bodies use `rawBody`; ordinary JSON uses `rawResponse` including `outputStack`.

- HTTP success: 2xx attempted turns / attempted turns.
- Usable replies: supported nonempty 2xx JSON replies / attempted turns.
- Complete conversations: runs without transport/protocol ERROR / executed runs.
- Behavioral pass: PASS or PASS_WITH_WARNINGS runs / complete runs.
- Strict behavioral pass: PASS runs / complete runs.
- End-to-end pass: PASS or PASS_WITH_WARNINGS runs / all executed runs.

ERROR runs are excluded from whole-conversation behavioral grading, but any prior
hard behavioral deviations remain in assertions, defects, and `observedHardFailures`.
Zero denominators yield null rates. Warnings, hard failures, and transport failures
are grouped independently by assertion ID and turn, with affected run indexes.

All artifact files use atomic replace within the batch directory. The manifest is
marked COMPLETE only after final reports exist. A process interruption can leave
STARTED batches with completed per-run evidence and temporary/incomplete files;
consumers should require the COMPLETE manifest for aggregate results.

## Offline regrading

### Regrade input contract

`regrade.py` accepts an EXECUTED or REGRADE aggregate with report schema version
`1.0` and completed run records. The selected scenario must match the recorded
scenario ID/business line and every turn ID/order/merchant message; expectations
may change. Completed ERROR runs remain regradable, including their skipped turns.
Supply the full aggregate: `transcripts.json` lacks execution and identity evidence
required by the validator.

Validation rejects dry-run plans and malformed or inconsistent captures before
output creation. The output root must be outside the source aggregate's directory.
Source files are read-only inputs.

### Regrade evaluation and provenance

Regrading copies runs in memory and calls the same `assertions.evaluate_run` as
`runner.py`, without constructing an HTTP client or requiring an Endpoint URL.
Evaluation uses saved `agentText` and merchant history. Saved text has already
passed through redaction; missing or redacted evidence cannot be reconstructed.
Raw responses are never normalized again, so this path cannot test normalization
changes.

The new batch has mode REGRADE, zero `requestsSent`, its own ID, source metadata and
aggregate hash, and a `comparison` containing old/new metrics and assertion outcome
changes. Run/user/session IDs, captured text, HTTP results, traces and capture times
remain historical; `evaluatedAt` records the new evaluation time. Per-run scenario
version/hash identify the new rubric. `source` identifies the immediate input batch,
including `source.aggregateSha256` for the exact bytes read, even when that input
is itself a regrade. Raw evidence is copied only when currently opted in and available,
through the [redaction boundary](#redaction-boundary).

Comparison entries list added, removed, or changed assertion outcomes. For changes
to reasons or evidence with unchanged outcomes, inspect the source and updated
per-run assertions.
For command execution and report review, follow the
[offline regrade workflow](TESTING_GUIDELINES.md#offline-regrade-workflow).

## Redaction boundary

Every persisted value goes through `Redactor`: exact configured credentials, URL
token (including encoded/decoded forms), extra configured redact values, URLs,
sensitive JSON keys, emails, and common phone formats are removed. Synthetic IDs
and trace identifiers remain useful for correlation; unfamiliar user/session IDs
from raw responses are masked. Computation happens before redaction so assertions
evaluate the actual Agent text.

Heuristics cannot recognize every name, address, identifier, or sensitive free-text
statement. Add known values through `UC4_REDACT_VALUES` and review evidence before
sharing. Raw retention is opt-in and does not promise byte-for-byte forensic fidelity.

## Public protocol references

Consulted during implementation, 2026-10-28:

- [Cognigy REST Endpoint](https://docs.cognigy.com/ai/deploy/endpoint-reference/rest/)
  (current page updated in 2026.16; version-specific authentication headers).
- [Cognigy Test Mode](https://docs.cognigy.com/ai/deploy/endpoints/test-mode/).
- [HTTPX transports](https://www.python-httpx.org/advanced/transports/), version 0.28.1.
- [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation), safe loader behavior.
- [python-dotenv](https://github.com/theskumar/python-dotenv), explicit local path and shell precedence.

No Cognigy administration API or resource mutation operation is used.
