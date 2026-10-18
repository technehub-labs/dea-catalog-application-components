# Contributing to the Information System Component catalogue

This catalogue is the canonical home for `dea:InformationSystemComponent` (class alias `ISC`) and its concrete specializations (APC = Application Component, IGC = Integration Component). The catalogue is owned by the IS Semantic Architecture programme.

## How to contribute

1. Read the governance model at `docs/governance.md`.
2. Read the migration map at `migrations/legacy-application-component-map.yaml` (the legacy APC/IGC records are preserved; new records use ISC).
3. Use the machine-readable template at `templates/component-template.yaml` (added in CR-IS-CAT-02B).
4. Use the README template at `templates/README-template.md` (added in CR-IS-CAT-02B).
5. Submit a PR against `origin/main`.
6. CI validates: allocation (validate-allocation.yml), taxonomy (validate-taxonomy.yml in CR-IS-CAT-02A), entities (validate-entities.yml in CR-IS-CAT-02B), catalogue (validate-catalogue.yml in CR-IS-CAT-02D).

## Cardinal rules

- **CR-MM-04 R1**: the Author field on any CR doc carries `Emmanuel A. Otchere` (the allowlist value).
- **CR-MM-04 R2**: one CR per PR.
- **D-004**: no en-dash (U+2013), em-dash (U+2014), three-dot pause (U+2E3B), or ellipsis (U+2026) in any artifact.
- **D-005**: no three-semicolon run in prose.
- **D-006**: no emojis in formal artifact content.
- **Standardization-body embargo**: no legacy telecom standards body vocabulary in any artifact.

## Governance

The catalogue is governed by the 5-CR programme template (per the standing rule ratified 2026-10-18). The 5-CR cascade is: CR-IS-CAT-02 (foundation) -> CR-IS-CAT-02A (taxonomy) -> CR-IS-CAT-02B (documentation) -> CR-IS-CAT-02C (population) -> CR-IS-CAT-02D (integration). Each CR is a single PR. Each PR has its own acceptance criteria in the CR doc.

## References

- `change-requests/CR-IS-CAT-02-information-system-components-rename.md` (the CR doc)
- `docs/governance.md` (the governance model)
- `migrations/legacy-application-component-map.yaml` (the migration map)
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the canonical entity)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01*.md` (the 5-CR ISF programme; the template)
