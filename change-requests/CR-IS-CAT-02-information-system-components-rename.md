# CR-IS-CAT-02: Information System Components catalog rename and extension

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-02 |
| **Title** | Information System Components catalog rename and extension |
| **Status** | Proposed (this PR) |
| **Type** | Repository migration and catalogue establishment |
| **Repository** | technehub-labs/dea-catalog-information-system-components (legacy URL: technehub-labs/dea-catalog-application-components until org-admin transfer) |
| **Canonical entity** | `dea:InformationSystemComponent` (class alias `ISC`; OpenDEAM-local `dea:entity-information-system-component`) |
| **Layer** | L5 |
| **Building block** | L5-systems |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR is the second catalog-rename slice of Path Y, landing in `technehub-labs/dea-catalog-application-components`. The GitHub repository rename to `dea-catalog-information-system-components` is performed by an org admin via GitHub repository transfer; this CR records the rename in the canonical metamodel pointer, the README, and the artifacts.

The catalog is the rename target for the legacy `dea:entity-application-component` (class alias `APC`) and `dea:entity-integration-component` (class alias `IGC`) identities, which specialise the new canonical abstract kind `dea:InformationSystemComponent` (class alias `ISC`), introduced in dea-metamodel CR-019 (D-2 disposition). The `dea:entity-infrastructure-component` (class alias `IFC`) identity stays under `dea:SolutionComponent` per DRIFT-4 (broader than the IS concern); the IFC records are migrated to a separate catalog (`dea-catalog-infrastructure-components`) in a follow-on CR-IS-CAT-02-IFC.

The 5-CR programme template (per the standing rule ratified 2026-10-18) is applied: CR-IS-CAT-02 is the foundation; CR-IS-CAT-02A..02D are the siblings (taxonomy, documentation, population, integration). The 5-CR programme for the ISC catalog follows the same A/B/C/D sub-cascade shape as CR-IS-CAT-01..01D for the ISF catalog.

## 2. Background

The existing repository was established as a scaffold for `dea:entity-application-component` (class alias `APC`), hosted with 2 sibling entities (`IFC` and `IGC`) under a shared catalog_repo (per ADR-0002 D6). The original definition described a deployable unit of an application system. This was superseded by dea-metamodel CR-019 (2026-10-16), which introduced `dea:InformationSystemComponent` as a Digital Profile abstract kind under `dea:SolutionComponent` (now abstract).

The existing repository currently has:
- Legacy README documentation.
- Legacy APC identity references.
- metamodel-pointer.yaml referring to `dea:entity-application-component`.
- An allocation-validation workflow (pinned to v0.2.1).
- A shared catalog_repo with IFC and IGC (per ADR-0002 D6).

OpenDEAM v0.7.0 (post-CR-AR-FMWK-04) declares:
- Entity: `dea:entity-information-system-component` (class alias `ISC`)
- Repository: `dea-catalog-information-system-components`
- Layer: L5
- Building block: L5-systems
- Abstract: true
- Specialises: `dea:SolutionComponent` (the parent abstract kind per ADR-0002 D3)
- Specialised by: APC, IGC
- Migration path: APC and IGC specialise ISC; IFC stays under SolutionComponent (DRIFT-4)

## 3. Objectives

1. Establish the canonical repository identity (`dea-catalog-information-system-components`).
2. Preserve historical repository continuity (the GitHub rename preserves commit history).
3. Adopt the Information System Component semantic definition (abstract kind; APC/IGC specialise ISC).
4. Establish a maintainable repository structure (per the 5-CR programme template).
5. Establish the repository's governance and contribution model (G-01..G-12).
6. Retain and extend existing allocation-validation mechanisms (pin to v0.7.0).
7. Prepare the repository for taxonomy, decomposition, population and cross-catalogue integration (CR-IS-CAT-02A..02D).
8. Establish a clear boundary between metamodel authority and catalogue authority (G-03, G-04).

## 4. Repository Migration

### 4.1 Rename

Rename `dea-catalog-application-components` to `dea-catalog-information-system-components`. The migration MUST use GitHub's repository rename mechanism rather than creating an unrelated replacement repository. This preserves commit history and allows GitHub to maintain redirects from the old repository URL.

### 4.2 Identity reconciliation

The following mapping is normative:

| Legacy | Canonical |
|---|---|
| `dea:ApplicationComponent` (metamodel) | `dea:InformationSystemComponent` (abstract parent) |
| `dea:entity-application-component` (OpenDEAM-local) | `dea:entity-information-system-component` (abstract parent) |
| `APC` (class alias) | `ISC` (class alias) |
| Application Component | Information System Component |
| `dea-catalog-application-components` | `dea-catalog-information-system-components` |

The same pattern applies to the IGC identity (Integration Component). The IFC identity (Infrastructure Component) is NOT in scope of this CR; it is migrated to `dea-catalog-infrastructure-components` in a follow-on CR.

Historical identifiers MUST remain discoverable. New records MUST use the canonical identity (ISC). The legacy identifier MUST NOT be silently reassigned to an unrelated concept.

### 4.3 Metamodel pointer

Update `metamodel-pointer.yaml` to reflect the canonical OpenDEAM v0.7.0 allocation.

Required fields:
- Metamodel version (v0.7.0) and canonical entity ID (`dea:entity-information-system-component`)
- Class alias (`ISC`)
- Layer (L5) and building block (L5-systems)
- Viewer URL
- Catalogue name and repository
- Catalogue status (planned)
- Canonical definition
- Metamodel and OpenDEAM links
- Supersession/migration reference (the 3-way mapping: APC/IGC -> ISC; IFC -> separate catalog)

The pointer MUST agree with the authoritative root model. It MUST NOT introduce an independent allocation or redefine the metamodel entity.

## 5. Repository Structure (5-CR programme template)

Establish the following target structure (per the 5-CR ISF programme template; standing rule for the IS catalog cascade):

```
dea-catalog-information-system-components/
├── README.md
├── CONTRIBUTING.md (added in this CR)
├── CHANGELOG.md (added in this CR)
├── LICENSE
├── NOTICE
├── metamodel-pointer.yaml
├── taxonomy/ (added in CR-IS-CAT-02A)
│   ├── README.md
│   ├── component-domains.yaml
│   ├── component-categories.yaml
│   └── classification-rules.yaml
├── schemas/
│   ├── information-system-component.schema.json
│   ├── application-component.schema.json
│   ├── integration-component.schema.json
│   └── taxonomy.schema.json (added in CR-IS-CAT-02A)
├── entities/
│   └── v1-alpha/
│       ├── README.md
│       ├── index.yaml
│       ├── components/ (added in CR-IS-CAT-02C)
│       └── ...
├── relationships/ (added in CR-IS-CAT-02D)
│   └── v1-alpha/
│       └── relationships.yaml
├── migrations/
│   ├── README.md (added in this CR)
│   └── legacy-application-component-map.yaml (added in this CR)
├── examples/ (added in CR-IS-CAT-02B)
├── docs/
│   ├── architecture.md (added in CR-IS-CAT-02B)
│   ├── taxonomy-guide.md (added in CR-IS-CAT-02A)
│   ├── decomposition-guide.md (added in CR-IS-CAT-02B)
│   ├── governance.md (added in this CR)
│   └── is-semantic-architecture/
│       └── opendeam-identifier-map.yaml (added in this CR)
├── .github/
│   └── workflows/
│       ├── validate-allocation.yml (updated in this CR; pinned to v0.7.0)
│       ├── validate-taxonomy.yml (added in CR-IS-CAT-02A)
│       ├── validate-entities.yml (added in CR-IS-CAT-02B)
│       └── validate-catalogue.yml (added in CR-IS-CAT-02D)
└── templates/ (added in CR-IS-CAT-02B)
    ├── component-template.yaml
    └── README-template.md
```

This structure is the target established through the 5-CR ISC programme. The detailed taxonomy, entity templates and validation implementation are owned by the sibling CRs (02A, 02B, 02C, 02D).

## 6. Governance and Authority

The following authority hierarchy applies (per the source doc section 6 of CR-IS-CAT-01):

1. dea-metamodel: normative semantic entity definitions, schemas and relationships.
2. dea-architecture-framework: OpenDEAM allocation and architecture-level relationships.
3. dea-governance: entity governance and identity continuity requirements.
4. This repository: ISC taxonomy, catalogue instances, decomposition, documentation and catalogue-level relationships.

The catalogue MUST NOT:
- Redefine `dea:InformationSystemComponent`.
- Introduce competing metamodel entity types.
- Reclassify Business Capabilities as Information System Components.
- Reassign existing entity identifiers.
- Manually modify generated metamodel artefacts.

Per G-01..G-12 (programme-wide governance, source doc section 7).

## 7. CI/CD

Retain the existing reusable allocation-validation workflow (`validate-allocation.yml`), pinned to v0.7.0. The taxonomy validator (`validate-taxonomy.yml`) is added in CR-IS-CAT-02A; the entity validator (`validate-entities.yml`) is added in CR-IS-CAT-02B; the cross-catalogue conformance validator (`validate-catalogue.yml`) is added in CR-IS-CAT-02D.

The 4 workflows operate in dependency order: allocation -> taxonomy -> entities -> catalogue.

## 8. Dependencies

- CR-019 (Information System Component introduction; merged 2026-10-16)
- CR-022 (metamodel closure; merged 2026-10-16)
- CR-AR-FMWK-04 (OpenDEAM extension; merged 2026-10-16; v0.7.0 tag)
- CR-IS-CAT-01..01D (the 5-CR ISF programme; merged 2026-10-18; the template)
- DRIFT-4 (Infrastructure Component placement; recorded in CR-019)
- EGV-004 (Identity Continuity)
- EGV-011 (Generated artefact authority)
- EGV-012 (Migration and compatibility governance, where applicable)

## 9. Acceptance Criteria

1. The existing repository is renamed without losing its history.
2. The canonical repository URL resolves.
3. The README identifies Information System Component as the catalogue subject.
4. The metamodel pointer uses the canonical ISC identity.
5. The pointer agrees with OpenDEAM v0.7.0.
6. Legacy identity mapping is documented and machine-readable (`migrations/legacy-application-component-map.yaml`).
7. Repository structure is established (this PR adds the skeleton; the detailed taxonomy, entity templates and validation are added by 02A, 02B, 02C, 02D).
8. Existing allocation-validation workflow remains operational (pinned to v0.7.0).
9. Governance and contribution model is established (`docs/governance.md`, `CONTRIBUTING.md`).
10. No new catalogue entity uses the deprecated APC identity without specialising ISC.
11. CI passes.
12. Repository documentation identifies the ownership boundary between metamodel, framework and catalogue.

## 10. Risks

| Risk | Mitigation |
|---|---|
| Repository renamed before allocation is aligned | Verify OpenDEAM v0.7.0 first; the pointer is pinned to v0.7.0 |
| Legacy links break | Use GitHub rename and maintain migration map (`migrations/legacy-application-component-map.yaml`) |
| Duplicate catalogue identity | Canonical ID validation (in 02A's taxonomy validator) |
| Metamodel/catalogue semantic divergence | Explicit authority hierarchy (section 6) |
| CI coverage overstated | Separate allocation validation (this CR) from taxonomy (02A), entities (02B), catalogue (02D) validation |
| Premature content population | Depend on 02A, 02B and 02C |
| IFC migration scope | The IFC identity is migrated to `dea-catalog-infrastructure-components` in a follow-on CR-IS-CAT-02-IFC (separate catalog) |

## 11. Definition of Done

CR-IS-CAT-02 is complete when the existing repository has been migrated to the canonical identity, its governance and structural foundation are in place, and the catalogue is ready to receive the taxonomy, documentation standards and content delivered by the sibling CRs (02A, 02B, 02C, 02D).

## 12. References

- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the canonical entity)
- `technehub-labs/dea-metamodel/change-requests/CR-022-metamodel-artifact-and-conformance-closure.md` (the artifact closure)
- `technehub-labs/dea-architecture-framework/change-requests/CR-AR-FMWK-04-information-system-entity-allocation.md` (the OpenDEAM extension)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01*.md` (the 5-CR ISF programme; the template)
- `technehub-labs/dea-governance/change-requests/CR-012-*.md` (the entity governance standard)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme source)
- `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md` (snapshot)

## 13. Standing Rules Acknowledged

The following programme-wide governance rules apply to CR-IS-CAT-02 and are acknowledged in this PR:

- G-01: `dea:InformationSystemComponent` is the only canonical entity for new catalogue records.
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification and functional decomposition are separate structures.
- G-07: Every active component has machine-readable content and individual documentation.
- G-08: Every relationship uses an authorized semantic contract.
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-10: All generated artefacts must be reproducible and validated.
- G-11: Metric definitions remain owned by the Metric catalogue.
- G-12: No implementation-specific component becomes canonical merely because it exists in an application.

The DRIFT-4 doctrine applies: `dea:InfrastructureComponent` stays under `dea:SolutionComponent` (broader than the IS concern); the IFC records are migrated to a separate catalog (`dea-catalog-infrastructure-components`) in a follow-on CR-IS-CAT-02-IFC.

---

End of CR-IS-CAT-02.
