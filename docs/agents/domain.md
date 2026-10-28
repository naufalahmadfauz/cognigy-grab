# Domain guidance

1. Before exploration, read the root [glossary](../../GLOSSARY.md) and relevant
   records in `docs/adr/`, when present. Proceed with available sources if one is absent.
2. Use canonical glossary terms across code, scenarios, tests, documentation, and
   issues. For missing or conflicting domain meanings, use `/domain-modeling` to
   resolve them and capture the definitions in the glossary.
3. If a proposed change conflicts with an ADR, identify the record and explain why
   its decision should be reopened before implementing the conflicting change.

Terminology work is complete when every introduced or changed domain term has a
canonical glossary definition. Keep implementation rationale in
[decisions](../DECISIONS.md) or an applicable ADR.
