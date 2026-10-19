# CR-IS-CAT-02C-P3: Information System Component P3 Follow-on Population

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-02C-P3 |
| **Title** | Information System Component P3 Follow-on Population (2 final domains) |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue population (P3 follow-on) |
| **Repository** | technehub-labs/dea-catalog-information-system-components (legacy URL: technehub-labs/dea-catalog-application-components until org-admin transfer) |
| **Parent** | CR-IS-CAT-02 (merged 2026-10-18); CR-IS-CAT-02A (merged 2026-10-18); CR-IS-CAT-02B (merged 2026-10-18); CR-IS-CAT-02C (merged 2026-10-18); CR-IS-CAT-02C-P2 (merged 2026-10-18); CR-IS-CAT-02D (merged 2026-10-18) |
| **Depends on** | CR-IS-CAT-02 (merged); CR-IS-CAT-02A (merged); CR-IS-CAT-02B (merged); CR-IS-CAT-02C (merged); CR-IS-CAT-02C-P2 (merged); CR-IS-CAT-02D (merged) |
| **Canonical entity** | `dea:InformationSystemComponent` (class alias `ISC`; OpenDEAM-local `dea:entity-information-system-component`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR is the P3 follow-on population of the ISC catalogue, and the final population slice. It extends the P1 population (5 domains, 19 records per CR-IS-CAT-02C) and the P2 population (3 domains, 11 records per CR-IS-CAT-02C-P2) with the final 2 component domains: Development Platform (ISCC-09) and AI Native (ISCC-10). The P3 tranche adds 2 F2 composite components and 6 F4 sub-components (8 records total) and 5 new cross-catalogue relationships.

After this PR merges, the ISC catalogue covers **10 of 10 ISCC domains** with 38 component records (10 F2 + 28 F4) and 27 cross-catalogue relationships. The ISC catalogue's domain coverage is complete.

## 2. P3 Selection Methodology

The 2 P3 domains were selected by the following criteria:

1. **Enabling**: the domain enables the delivery of the other 9 domains.
2. **Emerging**: the domain represents an emerging architectural pattern whose boundary needed the most careful doctrine application.
3. **P3 priority**: the domain is in the P3 priority band of the IS Semantic Architecture programme.

The 2 selected domains are:

| Code | Domain | Justification |
|---|---|---|
| ISCC-09 | Development Platform | Enabling; the delivery substrate for every other domain |
| ISCC-10 | AI Native | Emerging; the AI-native vs AI-assisted boundary is the most heavily scrutinised doctrine in the taxonomy |

## 3. P3 Component Inventory

The 2 P3 F2 composite components and their 6 F4 sub-components are:

| Domain | F2 Component | Type | F4 Sub-components |
|---|---|---|---|
| ISCC-09 | Development Platform | ApplicationComponent (APC) | ci-cd-pipeline; artifact-repository; build-service |
| ISCC-10 | AI Inference Platform | AIComponent (AIC) | model-serving-runtime; model-registry; agent-orchestrator |

Total: 2 F2 + 6 F4 = 8 component records. 6 composition edges (one per F2 to each F4 child). 5 new cross-catalogue relationships.

The AI Inference Platform and its 3 sub-components are the catalogue's first `AIComponent` (AIC) records. The AIComponent type is the concrete AI-native specialization of ISC, allocated alongside APC and IGC.

## 4. Doctrine on Overlapping Domains (Validation)

The 4 boundary doctrines from CR-IS-CAT-02A section 3.1 are validated by the P3 population:

1. **ISCC-08 vs ISCC-09 boundary (observation vs creation)**: the Observability Platform (P2) is correctly classified under ISCC-08 (read-only telemetry aggregation). The Development Platform (P3) is correctly classified under ISCC-09 (the read-write operational platform for the build and delivery lifecycle). The Development Platform depends on the Observability Platform at runtime for build telemetry; the classification is by read-write character, not by dependency. This is the boundary the P3 population was specifically selected to test.
2. **ISCC-10 vs all-other-domains boundary (AI-native vs AI-assisted)**: the AI Inference Platform and its 3 sub-components are correctly classified under ISCC-10. Their primary behaviour is AI-native: model inference, model lineage, and agentic execution. The orthogonal facet 5.7 (automation characteristics) is set to `agent-orchestrated` for the AI Inference Platform, the Model Serving Runtime, and the Agent Orchestrator. The Model Registry is set to `gitops-automated` because its primary behaviour is deterministic lifecycle management, not agentic execution. This is the first use of the `agent-orchestrated` facet value in the catalogue, and it demonstrates the doctrine in practice.
3. **ISCC-09 vs ISCC-10 boundary**: the CI/CD Pipeline is correctly classified under ISCC-09, not ISCC-10, even though an AI-assisted build pipeline is a plausible future state. An AI-assisted build pipeline is a CI/CD Pipeline with the orthogonal facet 5.7 set to `ai-assisted-deployment`; it does not become an AI-native component.
4. **ISCC-04 vs ISCC-09 boundary**: the Development Platform is correctly classified under ISCC-09 (delivery substrate), not ISCC-04 (business operations). The classification is by the component's purpose, not by the business capability it ultimately serves.

## 5. Cross-Catalogue Relationships (P3)

The 5 new cross-catalogue relationships added by the P3 population:

| ID | Source | Relationship | Target |
|---|---|---|---|
| isc-rel-201 | development-platform | depends-on | data-warehouse-platform |
| isc-rel-202 | ai-inference-platform | depends-on | observability-platform |
| isc-rel-203 | agent-orchestrator | exposes | if:agent-orchestrator-internal |
| isc-rel-204 | ai-inference-platform | measured_by | metric:inference-latency-p99 |
| isc-rel-205 | ai-inference-platform | consumes | data-entity:model-artifacts |

## 6. Repository Deliverables (this PR)

- `change-requests/CR-IS-CAT-02C-P3-population.md` (this file)
- `change-requests/README.md` (updated with P3 row)
- `docs/coverage-reports/p3-coverage-report.md` (new; the coverage report)
- `scripts/generate_p3_population.py` (new; deterministic generator)
- `scripts/generate_p1_population.py` (updated; the shared renderer now supports the AIComponent type, the `automation` facet override, and the `component_kind` override)
- `entities/v1-alpha/index.yaml` (updated; catalog-level counts: 38 records; 10 of 10 domains)
- 2 new domain directories under `entities/v1-alpha/components/`
- 2 new domain index.yaml files
- 8 new component records (2 F2 + 6 F4)
- 8 new 19-section READMEs
- `relationships/v1-alpha/relationships.yaml` (updated; 27 cross-catalogue records)
- 5 `reports/*.yaml` files (regenerated)

## 7. CI Requirements

CI MUST validate (per the 14 rules from CR-IS-CAT-02B and the 14 steps from CR-IS-CAT-02D):
- v2 ISC schema validation (all 38 component records; the AIComponent type is a valid `type` enum value in the v2 schema)
- README existence (all 38 records with 19-section README)
- Composition edges reference registered component identifiers
- Composition edges use a registered relationship kind
- Acyclic composition tree
- Composition depth <= 6
- Relationship registry validates against JSON Schema (27 records)
- Cross-reference resolution (all sources/targets resolve)
- OpenDEAM allocation check (the 3 `measured_by` records are metric declarations)
- Conformance reports generate deterministically

The existing 4 workflows (validate-allocation, validate-taxonomy, validate-entities, validate-catalogue) collectively enforce these checks.

## 8. Acceptance Criteria

1. The 2 P3 domains are populated with F2 composite components.
2. Each F2 has 3 F4 sub-components (6 F4 total).
3. All 38 component records validate against the v2 ISC schema.
4. All 38 component records have a 19-section README.
5. The 6 new composition edges are recorded in the v2 schema's `composition` array.
6. The 5 new cross-catalogue relationships are recorded in `relationships/v1-alpha/relationships.yaml`.
7. The 4 boundary doctrines are validated, including the first use of the `agent-orchestrated` facet value.
8. The catalog-level index reflects 38 records across 10 of 10 domains.
9. The deterministic generator is reproducible.
10. The coverage report is generated and committed.
11. CI passes.

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| AI-native over-classification | The ISCC-10 vs all doctrine is validated in section 4; the `agent-orchestrated` facet value is applied only to components whose primary behaviour is agentic |
| AI-assisted components misrouted into ISCC-10 | The orthogonal facet 5.7 is the routing mechanism; the CI/CD Pipeline example demonstrates an AI-capable component that is NOT classified under ISCC-10 |
| Incomplete coverage | The P3 tranche completes the domain coverage at 10 of 10; the coverage report records the completion |
| Vendor-specific leakage | Per G-12, no implementation-specific component becomes canonical |
| Documentation decay | Every active component MUST have a README (rule 3 from 02B); the README MUST include a change history (rule 13) |

## 10. Definition of Done

The P3 population is complete when the 2 P3 domains are populated, all 38 component records validate, the cross-catalogue relationships are recorded, the coverage report is generated, and CI passes. The ISC catalogue's domain coverage is complete at 10 of 10 ISCC domains.

## 11. Remaining ISC Work

The ISC catalogue's structural and content work is complete after this PR. The remaining ISC work is:

| CR | Scope | Blocker |
|---|---|---|
| CR-IS-CAT-02-IFC | Migrate the Infrastructure Component records to `dea-catalog-infrastructure-components` | Requires an org-admin repo create |

The IFC identity stays under `dea:SolutionComponent` per DRIFT-4 (broader than the IS concern); this is a catalogue-separation decision, not a metamodel change.

## 12. References

- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02-information-system-components-rename.md` (parent; merged 2026-10-18 via PR #2, commit `15e49ef`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02A-taxonomy.md` (sibling; merged 2026-10-18 via PR #3, commit `a50a1b5`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02B-documentation.md` (sibling; merged 2026-10-18 via PR #4, commit `b73655a`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02C-population.md` (sibling P1; merged 2026-10-18 via PR #5, commit `2df0c5b`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02C-P2-population.md` (sibling P2; merged 2026-10-18 via PR #7, commit `47dfc74`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02D-integration.md` (sibling; merged 2026-10-18 via PR #6, commit `b2eb7b8`)
- `technehub-labs/dea-catalog-application-components/taxonomy/orthogonal-facets.yaml` (facet 5.7; the automation characteristics facet)
- `technehub-labs/dea-catalog-application-components/docs/coverage-reports/p1-coverage-report.md` (the P1 coverage report)
- `technehub-labs/dea-catalog-application-components/docs/coverage-reports/p2-coverage-report.md` (the P2 coverage report)
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the canonical entity)
- `technehub-labs/dea-metamodel/change-requests/CR-022-metamodel-artifact-and-conformance-closure.md` (artifact closure)
- `technehub-labs/dea-architecture-framework/change-requests/CR-AR-FMWK-04-information-system-entity-allocation.md` (OpenDEAM extension)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; the template)

## 13. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to this CR and are acknowledged in this PR:

- G-01: `dea:InformationSystemComponent` is the only canonical entity for new catalogue records.
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification (02A) and functional decomposition (02B) are separate structures.
- G-07: Every active component has machine-readable content and individual documentation.
- G-08: Every relationship uses an authorized semantic contract.
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-10: All generated artefacts must be reproducible and validated.
- G-12: No implementation-specific component becomes canonical merely because it exists in an application.

---

End of CR-IS-CAT-02C-P3.
