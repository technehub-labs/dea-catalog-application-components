# Governance :  Information System Component catalogue

CR-IS-CAT-02 (2026-10-18). The governance model for the ISC catalogue.

## Authority hierarchy

1. **dea-metamodel**: normative semantic entity definitions, schemas and relationships.
2. **dea-architecture-framework**: OpenDEAM allocation and architecture-level relationships.
3. **dea-governance**: entity governance and identity continuity requirements.
4. **This repository** (`dea-catalog-information-system-components`): ISC taxonomy, catalogue instances, decomposition, documentation and catalogue-level relationships.

The catalogue MUST NOT:
- Redefine `dea:InformationSystemComponent`.
- Introduce competing metamodel entity types.
- Reclassify Business Capabilities as Information System Components.
- Reassign existing entity identifiers.
- Manually modify generated metamodel artefacts.

## Programme-wide governance (G-01..G-12)

| Rule | Requirement |
|---|---|
| G-01 | `dea:InformationSystemComponent` is the only canonical entity for new catalogue records. |
| G-02 | Legacy `dea:ApplicationComponent` identity remains traceable. |
| G-03 | Metamodel definitions remain authoritative in `dea-metamodel`. |
| G-04 | OpenDEAM allocation remains authoritative in `dea-architecture-framework`. |
| G-05 | Taxonomy nodes are catalogue classifications, not metamodel entities. |
| G-06 | Classification and functional decomposition are separate structures. |
| G-07 | Every active component has machine-readable content and individual documentation. |
| G-08 | Every relationship uses an authorized semantic contract. |
| G-09 | Catalogue completeness must be evidenced, not assumed. |
| G-10 | All generated artefacts must be reproducible and validated. |
| G-11 | Metric definitions remain owned by the Metric catalogue. |
| G-12 | No implementation-specific component becomes canonical merely because it exists in an application. |

## DRIFT-4 doctrine (per CR-019)

`dea:InfrastructureComponent` stays under `dea:SolutionComponent` (broader than the IS concern). The IFC records are migrated to a separate catalog (`dea-catalog-infrastructure-components`) in a follow-on CR-IS-CAT-02-IFC. This catalog (`dea-catalog-information-system-components`) covers APC + IGC (both IS-relevant).

## Change management

Changes to this catalog are governed by the 5-CR programme template (per the standing rule ratified 2026-10-18). The 5-CR cascade is:
- CR-IS-CAT-02 (this CR; the foundation)
- CR-IS-CAT-02A (taxonomy)
- CR-IS-CAT-02B (documentation)
- CR-IS-CAT-02C (population)
- CR-IS-CAT-02D (integration)

Each CR is a single PR. CR-MM-04 R2 (one CR per PR) is enforced.

## References

- `change-requests/CR-IS-CAT-02-information-system-components-rename.md` (the CR doc)
- `migrations/legacy-application-component-map.yaml` (the migration map)
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the canonical entity)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01*.md` (the 5-CR ISF programme; the template)
- `technehub-labs/dea-governance/change-requests/CR-012-*.md` (the entity governance standard)
