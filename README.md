# Information System Component

> An identifiable architectural constituent of an information system that encapsulates a defined responsibility, structure or execution boundary.

**Layer:** L5 :  **Entity:** `dea:InformationSystemComponent` (class alias `ISC`) :  **Metamodel:** [v1.0.0](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=ISC)

> **CR-IS-CAT-02 status (2026-10-18)**: This catalog is the rename target of the legacy `dea-catalog-application-components` (per CR-IS-CAT-02). The GitHub repository rename to `dea-catalog-information-system-components` is performed by an org admin via GitHub repository transfer. Until the rename is complete, the legacy URL continues to resolve. The canonical reference in the OpenDEAM root model (v0.7.0) is `dea-catalog-information-system-components`.

## Status

This is a **scaffold** repository that is being renamed and extended to cover the canonical Information System Component (ISC) entity introduced in the IS Semantic Architecture programme (dea-metamodel CR-019 D-2). The ISC is the abstract parent; the concrete APC (Application Component) and IGC (Integration Component) specialise ISC. The IFC (Infrastructure Component) stays under SolutionComponent per DRIFT-4 (broader than the IS concern).

Content population is planned for a subsequent phase; existing APC scaffold records are preserved under the legacy identity.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:InformationSystemComponent` |
| Class Alias | `ISC` |
| Layer | L5 |
| Building Block | L5-systems |
| Profile | dea:digital |
| Metamodel Version | v1.0.0 |
| Status | planned |
| Abstract | true |
| Specialises | `dea:SolutionComponent` (the parent abstract kind per ADR-0002 D3) |
| Specialised by | `dea:ApplicationComponent` (APC); `dea:IntegrationComponent` (IGC) |

## Catalog Structure

```
dea-catalog-information-system-components/
├── metamodel-pointer.yaml   :  entity mapping (do not edit manually)
├── change-requests/
│   └── CR-IS-CAT-02-information-system-components-rename.md
├── entities/
│   └── v1-alpha/          :  catalog entries go here
│       └── README.md
├── schemas/                :  JSON Schema for this entity type
│   └── entity.schema.json
├── taxonomy/               :  ISC classification (added in CR-IS-CAT-02A)
├── relationships/          :  cross-catalogue relationships (added in CR-IS-CAT-02D)
├── migrations/             :  legacy identity mapping (added in CR-IS-CAT-02)
├── examples/               :  example records (added in CR-IS-CAT-02B)
├── docs/
│   ├── architecture.md     :  ISC architecture (added in CR-IS-CAT-02B)
│   ├── taxonomy-guide.md   :  ISC taxonomy (added in CR-IS-CAT-02A)
│   ├── decomposition-guide.md (added in CR-IS-CAT-02B)
│   └── governance.md       :  ISC governance (added in CR-IS-CAT-02)
├── .github/
│   └── workflows/
│       ├── validate-allocation.yml  :  pins the pointer against OpenDEAM
│       ├── validate-taxonomy.yml    :  taxonomy validation (added in CR-IS-CAT-02A)
│       ├── validate-entities.yml    :  entity validation (added in CR-IS-CAT-02B)
│       └── validate-catalogue.yml   :  cross-catalogue conformance (added in CR-IS-CAT-02D)
└── templates/              :  templates for new records (added in CR-IS-CAT-02B)
```

## Migration

The legacy `dea:entity-application-component` identity (class alias `APC`) and `dea:entity-integration-component` identity (class alias `IGC`) are retained in OpenDEAM for EGV-004 identity continuity. The `dea:entity-infrastructure-component` identity (class alias `IFC`) stays under `dea:SolutionComponent` per DRIFT-4. New records should use the canonical `dea:InformationSystemComponent` (class alias `ISC`) as the abstract kind; concrete records are APC (application) or IGC (integration) specializations.

The catalog supports both identities conditionally:
- `dea:entity-application-component` (legacy; class alias `APC`; specialises ISC per CR-019)
- `dea:entity-integration-component` (legacy; class alias `IGC`; specialises ISC per CR-019)
- `dea:InformationSystemComponent` (canonical abstract; class alias `ISC`)

The conditional merge is documented in the metamodel pointer's `migration.disposition` field. The IFC records are migrated to a separate catalog (`dea-catalog-infrastructure-components`) in a follow-on CR-IS-CAT-02-IFC.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.
