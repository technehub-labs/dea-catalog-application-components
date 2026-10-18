# CR-IS-CAT-02C-P2: Information System Component P2 Follow-on Population

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-02C-P2 |
| **Title** | Information System Component P2 Follow-on Population (3 domains) |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue population (P2 follow-on) |
| **Repository** | technehub-labs/dea-catalog-information-system-components (legacy URL: technehub-labs/dea-catalog-application-components until org-admin transfer) |
| **Parent** | CR-IS-CAT-02 (merged 2026-10-18); CR-IS-CAT-02A (merged 2026-10-18); CR-IS-CAT-02B (merged 2026-10-18); CR-IS-CAT-02C (merged 2026-10-18); CR-IS-CAT-02D (merged 2026-10-18) |
| **Depends on** | CR-IS-CAT-02 (merged); CR-IS-CAT-02A (merged); CR-IS-CAT-02B (merged); CR-IS-CAT-02C (merged); CR-IS-CAT-02D (merged) |
| **Enables** | CR-IS-CAT-02C-P3 (P3 follow-on population; 2 remaining domains) |
| **Canonical entity** | `dea:InformationSystemComponent` (class alias `ISC`; OpenDEAM-local `dea:entity-information-system-component`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR is the P2 follow-on population of the ISC catalogue. It extends the P1 population (5 domains, 19 records per CR-IS-CAT-02C) with 3 additional domains (Employee Experience, Partner Integration, Observability). The P2 tranche adds 3 F2 composite components and 8 F4 sub-components (11 records total) and 6 new cross-catalogue relationships.

After this PR merges, the ISC catalogue covers 8 of 10 ISCC domains with 30 component records (8 F2 + 22 F4) and 22 cross-catalogue relationships. The remaining 2 domains (ISCC-09 Development Platform; ISCC-10 AI Native) are deferred to the P3 follow-on population.

## 2. P2 Selection Methodology

The 3 P2 domains were selected by the following criteria:

1. **Internal-facing**: the domain is internal-facing (not customer-facing).
2. **Operational**: the domain has cross-cutting operational concerns.
3. **P2 priority**: the domain is in the P2 priority band of the IS Semantic Architecture programme.

The 3 selected domains are:

| Code | Domain | Justification |
|---|---|---|
| ISCC-02 | Employee Experience | Internal-facing; the primary internal interface |
| ISCC-03 | Partner Integration | B2B; the cross-organization interface |
| ISCC-08 | Observability | Cross-cutting; required by every other domain for operational insight |

The remaining 2 domains (ISCC-09 Development Platform; ISCC-10 AI Native) are deferred to the P3 follow-on population.

## 3. P2 Component Inventory

The 3 P2 F2 composite components and their 8 F4 sub-components are:

| Domain | F2 Component | F4 Sub-components |
|---|---|---|
| ISCC-02 | Employee Portal Platform | employee-portal-frontend; employee-portal-bff |
| ISCC-03 | Partner Portal Platform | partner-portal-onboarding; partner-portal-data-exchange; partner-portal-settlement |
| ISCC-08 | Observability Platform | metrics-collector; log-aggregator; distributed-tracer |

Total: 3 F2 + 8 F4 = 11 component records. 8 composition edges (one per F2 to each F4 child). 6 new cross-catalogue relationships.

## 4. Doctrine on Overlapping Domains (Validation)

The 4 boundary doctrines from CR-IS-CAT-02A section 3.1 are validated by the P2 population:

1. **ISCC-08 vs ISCC-09 boundary**: the Observability Platform is correctly classified under ISCC-08 (observation). The Development Platform (ISCC-09) is the read-write operational platform for the build/dev lifecycle; the Observability Platform (ISCC-08) is the read-only telemetry aggregation. The boundary is observation vs creation.
2. **ISCC-02 vs ISCC-04 boundary**: the Employee Portal Platform is correctly classified under ISCC-02 (employee-facing). The Order Management System (ISCC-04 from P1) is back-office operations. The classification is by primary purpose, not by dependency.
3. **ISCC-03 vs ISCC-06 boundary**: the Partner Portal Platform is correctly classified under ISCC-03 (partner-facing B2B). The API Gateway (ISCC-06 from P1) is the internal integration component. The classification is by primary audience (partner vs internal), not by integration dependency.
4. **ISCC-10 vs all-other-domains boundary**: no P2 component is classified under ISCC-10 (AI Native). The AI-assisted components are deferred to the P3 follow-on population.

## 5. Cross-Catalogue Relationships (P2)

The 6 new cross-catalogue relationships added by the P2 population:

| ID | Source | Relationship | Target |
|---|---|---|---|
| isc-rel-101 | employee-portal-platform | depends-on | identity-broker |
| isc-rel-102 | employee-portal-platform | exposes | if:employee-portal-internal |
| isc-rel-103 | partner-portal-platform | depends-on | api-gateway |
| isc-rel-104 | partner-portal-data-exchange | consumes | data-entity:partner-transactions |
| isc-rel-105 | observability-platform | depends-on | data-warehouse-platform |
| isc-rel-106 | observability-platform | measured_by | metric:observability-data-freshness |

## 6. Repository Deliverables (this PR)

- `change-requests/CR-IS-CAT-02C-P2-population.md` (this file)
- `change-requests/README.md` (updated with P2 row)
- `docs/coverage-reports/p2-coverage-report.md` (new; the coverage report)
- `scripts/generate_p2_population.py` (new; deterministic generator)
- `entities/v1-alpha/index.yaml` (updated; catalog-level counts: 30 records)
- 3 new domain directories under `entities/v1-alpha/components/`
- 3 new domain index.yaml files
- 11 new component records (3 F2 + 8 F4)
- 11 new 19-section READMEs
- `relationships/v1-alpha/relationships.yaml` (updated; 22 cross-catalogue records)
- 5 `reports/*.yaml` files (regenerated)

## 7. CI Requirements

CI MUST validate (per the 14 rules from CR-IS-CAT-02B and the 14 steps from CR-IS-CAT-02D):
- v2 ISC schema validation (all 30 component records)
- README existence (all 30 records with 19-section README)
- Composition edges reference registered component identifiers
- Composition edges use a registered relationship kind
- Acyclic composition tree
- Composition depth <= 6
- Relationship registry validates against JSON Schema (22 records)
- Cross-reference resolution (all sources/targets resolve)
- OpenDEAM allocation check (the 2 `measured_by` records are metric declarations)
- Conformance reports generate deterministically

The existing 4 workflows (validate-allocation, validate-taxonomy, validate-entities, validate-catalogue) collectively enforce these checks.

## 8. Acceptance Criteria

1. The 3 P2 domains are populated with F2 composite components.
2. Each F2 has 2-3 F4 sub-components (8 F4 total).
3. All 30 component records validate against the v2 ISC schema.
4. All 30 component records have a 19-section README.
5. The 8 new composition edges are recorded in the v2 schema's `composition` array.
6. The 6 new cross-catalogue relationships are recorded in `relationships/v1-alpha/relationships.yaml`.
7. The 4 boundary doctrines are validated.
8. The catalog-level index reflects the new counts (30 records; 8 of 10 domains).
9. The deterministic generator is reproducible.
10. The coverage report is generated and committed.
11. CI passes.

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Incomplete coverage | The P2 tranche covers 3 more of 10 domains; the remaining 2 (ISCC-09, ISCC-10) are deferred to the P3 follow-on population |
| Doctrine violations | The 4 boundary doctrines are validated explicitly in section 4; the coverage report records the validation |
| Composition edge proliferation | The 4 relationship kinds (contains, depends-on, hosts, orchestrates) are the only authorized kinds |
| Vendor-specific leakage | Per G-12, no implementation-specific component becomes canonical |
| Documentation decay | Every active component MUST have a README (rule 3 from 02B); the README MUST include a change history (rule 13) |

## 10. Definition of Done

The P2 population is complete when the 3 P2 domains are populated, all 30 component records validate, the cross-catalogue relationships are recorded, the coverage report is generated, and CI passes.

## 11. Follow-on Population

The remaining 2 component domains are deferred to P3:

| Code | Domain | Priority | Target CR |
|---|---|---|---|
| ISCC-09 | Development Platform | P3 | CR-IS-CAT-02C-P3 |
| ISCC-10 | AI Native | P3 | CR-IS-CAT-02C-P3 |

## 12. References

- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02-information-system-components-rename.md` (parent; merged 2026-10-18 via PR #2, commit `15e49ef`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02A-taxonomy.md` (sibling; merged 2026-10-18 via PR #3, commit `a50a1b5`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02B-documentation.md` (sibling; merged 2026-10-18 via PR #4, commit `b73655a`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02C-population.md` (sibling P1; merged 2026-10-18 via PR #5, commit `2df0c5b`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02D-integration.md` (sibling; merged 2026-10-18 via PR #6, commit `b2eb7b8`)
- `technehub-labs/dea-catalog-application-components/taxonomy/` (the classification layer; 02A)
- `technehub-labs/dea-catalog-application-components/docs/decomposition-guide.md` (the F0-F5 model; 02B)
- `technehub-labs/dea-catalog-application-components/docs/coverage-reports/p1-coverage-report.md` (the P1 coverage report; 02C)
- `technehub-labs/dea-catalog-application-components/scripts/generate_p1_population.py` (the P1 generator; the template for P2)
- `technehub-labs/dea-catalog-application-components/scripts/generate_p2_population.py` (the P2 generator; this PR introduces it)
- `technehub-labs/dea-catalog-application-components/relationships/v1-alpha/relationships.yaml` (the relationship registry; 02D)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01C-population.md` (the ISF P1 population; the template)
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

End of CR-IS-CAT-02C-P2.
