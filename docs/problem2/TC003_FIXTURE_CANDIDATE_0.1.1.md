# TC-003 fixture correction — v0.1.1 candidate

**Prepared 2026-11-06; offline validation PASS; candidate only, NOT authorized for live execution.**

## Candidate and exact change

- [Candidate YAML](../../scenarios/problem2-pilots/candidates/tc-003-v0.1.1/P2-TC-003-001.yaml):
  same scenario ID `P2-TC-003-001`, new version **0.1.1**, **14 turns / 13 gates**.
- [Exact unified diff](TC003_FIXTURE_CANDIDATE_0.1.1.diff) against the unchanged
  [v0.1.0 YAML](../../scenarios/problem2-pilots/P2-TC-003-001.yaml).
- The separate version directory preserves the original catalog's v0.1.0 selection;
  it does not add another fixture identity to the accepted 23 or smoke 21 selection.
  Select this candidate explicitly by file for offline review; it is not promoted.

1. Recognize `open the relevant cancelled order`, existing open/tap/select/choose
   forms, tap/click with optional `on`, and canceled/cancelled spelling. Retain
   action-verb, selected-order and existing negation-exclusion requirements.
2. Disambiguate the `Cancelled` tab from a `cancelled order`: the tab regex's new
   negative lookahead prevents a valid `open the cancelled order` instruction
   triggering a false repeat-tab/pacing failure. Tab instructions still match.
3. T04 now requires only opening the visible order and waits; it no longer requires
   a same-reply status question. For this requested fixed-script profile, combining
   the two stages stops progression rather than silently skipping the opening wait.
4. New T05 `order-opened`: merchant confirms opening/details visibility **without
   supplying status**; Agent must obtain the compensation-status observation and
   wait, with no request navigation or repeated opening.
5. T06 supplies the explicit blank status, retained review intent and present link;
   only then does the unchanged conditional review-request continuation begin.
   Old T05–T13 map to new T06–T14. The redundant opening clause moves out of the
   old blank-status input into the new confirmation checkpoint.

All common assertions, concept exclusions, first-three-turn definitions, known
authorized Owner input, no-handoff/no-guarantee/merchant-owned submission controls,
qualified no-photo handling and explicit-finish/closing assertions are preserved.
Only the two listed concept patterns and the opening/status checkpoint binding change.

## Exact hashes

| Artifact | SHA-256 |
|---|---|
| Candidate YAML bytes | `e15a084a45e57e02ddfd3a37c701eb7f7f96cc855c939b68b8fd359caf7730d6` |
| Candidate canonical `scenarioSha256` | `922e0f9adb7ad01ee4a8e8b75591719f272d285f694a610c475d8e13e866fb1c` |
| Preserved v0.1.0 YAML bytes | `cb37ccac813fbd4844950d8fe33f501b0c010941511fa96efb640ab19251db13` |
| Preserved v0.1.0 canonical hash | `1ec66c5a61b8f39314c6d69f4074dbc314465b4c03a946610fe70c90b2d2056b` |

Canonical hash uses the unchanged parser's default-separator
`json.dumps(validated_definition, sort_keys=True, ensure_ascii=False)` UTF-8 bytes.

## Offline checks actually performed

The existing schema, CLI validation entry point, evaluator and guarded mock
progression were used, following [advancement verification](../TESTING_GUIDELINES.md#advancement-verification)
and the previous pilot helper's approach. **No pytest/test-suite command or live
benchmark execution was performed.** Temporary checks used HTTPX 0.28.1 MockTransport,
dummy `.invalid` configuration, blocked sockets/DNS and an isolated working directory
with Cognigy/UC4 environment removed; repository `.env` was not loaded or changed.

- Existing CLI validation: **1 candidate accepted**; **5 ineligible gate forms rejected**.
- **65 wording checks**, including all four saved replies, 15 passing open-order
  forms, negatives/negation, premature status/request actions and retained safety rules.
- **34 single-run mocked batches**: complete synthetic progression, all **13 gate
  stops**, complete paths for every passing opening variant, missing replies,
  textless terminal, final closing failure and non-gating identity failure.
- Verified exact mock message prefixes, no later messages or pacing after a stop,
  preserved stopping text/reasons, zero-attempt unsent turns, finalized reports and
  matching per-run/aggregate evidence. One dry plan remained unevaluated.
- **192 pre-existing repository files and 503 historical report files unchanged**;
  original YAML, live batch, review ZIP, runner source and acceptance documents retained.

[Detailed verification](../../reports/problem2-pilots/TC-003/fixture-candidate-v0.1.1-2026-11-06/verification.json)
and [preservation record](../../reports/problem2-pilots/TC-003/fixture-candidate-v0.1.1-2026-11-06/preservation-verification.json)
are local development evidence, **not new observed Agent behavior**. Reproducible
temporary helper and mock reports are under
`C:\Users\Nau\AppData\Local\Temp\opencode\uc4-tc003-fixture-candidate-2026-11-06`.
Do not rerun the older three-pilot helper for this isolated candidate: it targets the
old bindings and its companion validation helper includes pytest.

## Previous run and review boundary

Original batch `20261105T213635803637Z-42167a454825` remains an immutable
four-turn capture with its original automated **FAIL**, nine unsent turns and
[transcript](../../reports/problem2-pilots/TC-003/20261105T213635803637Z-42167a454825/transcripts/run-001.md).
The project owner's current message reports independent ChatGPT review: **no
confirmed business-process defect in the four observed replies; full TC-003
INCONCLUSIVE; target coverage PARTIAL**. This is recorded as an owner-relayed
review finding, not a newly performed independent assessment or a rewritten grade.

Saved replies were used only for wording calibration. No historical regrade,
session continuation or invented post-T04 live replies occurred. The changed
turn count/progression cannot be retroactively applied as a completed old journey.
The new candidate itself remains **NOT_RUN / NOT_RUN**.

## Remaining limitations and next action

- Regexes recognize bounded wording, not unrestricted semantic equivalents. Other
  valid paraphrases, turn segmentations, clarifications or branches can still stop
  a fixed script and need manual assessment rather than automatic defect attribution.
- Existing [E1–E5 evidence limitations](PILOT_EXECUTION_PREPARATION.md#3-manual-and-external-evidence-requirements)
  remain: synthetic UI/access/submission inputs, text-only capture, no backend or
  audio proof, separate terminal ownership/exactly-once evidence and textless ERROR handling.
- Cancellation age stays **14 days**; catalog reference stays November 4. The
  runner injects no clock. Any future run must record actual MYT reference/init evidence.
- This correction does not resolve controlled-text adoption, broader policy gaps,
  configuration provenance or acceptance of every later wording gate.

**Next: review this exact candidate/hash. A new live run needs separate authorization.**
No Cognigy/Knowledge/Flow/Job/Tool/Code/runner changes, Endpoint requests, original
evidence overwrite, other pilot changes or baseline freeze occurred.
