# Domain Docs

## Layout

This repository is single-context:

- `GLOSSARY.md` at the repository root defines domain vocabulary.
- `docs/adr/` holds architecture decision records.

## Before exploring

Read `GLOSSARY.md` and the ADRs relevant to the area you are about to work in.

If these files or directories are absent, proceed silently. The `/domain-modeling` skill creates them lazily when terms or decisions are resolved.

## Use the glossary's vocabulary

Use the glossary's terms when naming domain concepts in issues, proposals, hypotheses, and tests. Follow its guidance on synonyms.

If a needed concept is missing, reconsider whether it belongs to the domain; note genuine vocabulary gaps for `/domain-modeling`.

## Flag ADR conflicts

If a proposal contradicts an existing ADR, identify the ADR and explain why the decision should be reopened.
