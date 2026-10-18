# CR-IS-CAT-02D: Information System Component Cross-Catalogue Integration and Conformance

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-02D |
| **Title** | Information System Component Cross-Catalogue Integration and Conformance |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue integration and conformance |
| **Repository** | technehub-labs/dea-catalog-information-system-components (legacy URL: technehub-labs/dea-catalog-application-components until org-admin transfer) |
| **Parent** | CR-IS-CAT-02 (merged 2026-10-18); CR-IS-CAT-02A (merged 2026-10-18); CR-IS-CAT-02B (merged 2026-10-18); CR-IS-CAT-02C (merged 2026-10-18) |
| **Depends on** | CR-IS-CAT-02 (merged); CR-IS-CAT-02A (merged); CR-IS-CAT-02B (merged); CR-IS-CAT-02C (merged) |
| **Canonical entity** | `dea:InformationSystemComponent` (class alias `ISC`; OpenDEAM-local `dea:entity-information-system-component`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR is the **fourth and final sibling** in the 5-CR ISC catalogue programme. It establishes cross-catalogue integration, relationship validation and conformance requirements for the Information System Component catalogue. The catalogue consumes the established metamodel and OpenDEAM relationship definitions rather than independently inventing relationship semantics.

After this CR merges, the 5-CR ISC programme is complete. The remaining Path Y work in the IS catalogue cascade is CR-IS-CAT-03 (ISS new), CR-IS-CAT-04 (II new), and the governance closure (CR-013).

## 2. Cross-Catalogue Relationship Matrix

The cross-catalogue relationship matrix (per the source doc section 4 from CR-IS-CAT-01; the standing 5-CR programme template) establishes the relationship kinds the ISC catalogue participates in. Each row in the matrix is a relationship kind; each kind is anchored in a metamodel relationship (CR-017..021) or an OpenDEAM allocation declaration (CR-AR-FMWK-04).

| Source | Relationship | Target | Authority |
|---|---|---|---|
| InformationSystemComponent | executes | InformationSystemFunction | CR-018/019 |
| InformationSystemComponent | provides | InformationSystemService | CR-019/020 |
| InformationSystemComponent | depends-on | InformationSystemComponent | CR-019 |
| InformationSystemComponent | hosts | InformationSystemComponent | CR-019 (deployment) |
| InformationSystemComponent | consumes | DataEntity | CR-017/018 |
| InformationSystemComponent | produces | DataEntity | CR-017/018 |
| InformationSystemComponent | exposes | IntegrationInterface | CR-021 |
| InformationSystemComponent | measured_by | Metric | OpenDEAM v0.7.0 (allocation declaration) |

The last row is an OpenDEAM allocation declaration, NOT a metamodel relationship claim. Per G-11, metric definitions remain owned by the Metric catalogue; the ISC catalogue references them through the established OpenDEAM v0.7.0 `measured_by:[MTR]` allocation. No new `dea:has-metric` or similar relationship is invented.

## 3. Relationship Registry (P1 Tranche)

The P1 population (from CR-IS-CAT-02C) provides 19 component records. The P1 relationship registry records 16 cross-catalogue relationships:

| ID | Source | Relationship | Target |
|---|---|---|---|
| isc-rel-001 | customer-facing-web-application-platform | executes | isf:customer-experience-management |
| isc-rel-002 | order-management-system | executes | isf:order-capture |
| isc-rel-003 | order-management-system | executes | isf:order-fulfillment |
| isc-rel-004 | data-warehouse-platform | executes | isf:data-ingestion |
| isc-rel-005 | data-warehouse-platform | executes | isf:data-query |
| isc-rel-006 | api-gateway | provides | iss:api-gateway-service |
| isc-rel-007 | api-gateway | exposes | if:api-gateway-public |
| isc-rel-008 | api-gateway | depends-on | identity-broker |
| isc-rel-009 | api-gateway | measured-by | metric:api-gateway-p99-latency |
| isc-rel-010 | order-management-system | depends-on | identity-broker |
| isc-rel-011 | data-warehouse-platform | consumes | data-entity:order-events |
| isc-rel-012 | order-management-system | produces | data-entity:order-events |
| isc-rel-013 | customer-facing-web-application-platform | depends-on | api-gateway |
| isc-rel-014 | identity-broker | exposes | if:identity-broker-public |
| isc-rel-015 | order-management-orchestrator | hosts | order-fulfillment-worker |
| isc-rel-016 | api-gateway-router | hosts | api-gateway-rate-limiter |

The 16 relationships cover 6 of the 8 relationship kinds from the matrix. The two relationship kinds not yet exercised by the P1 population (ISC consumes/produces Event) are deferred to the P2/P3 follow-on populations.

## 4. 4-Level Conformance Architecture

Per the source doc section 7, the conformance architecture is structured in 4 levels:

1. **Structural conformance**: every record MUST satisfy the v2 ISC schema (rule 1, rule 2, rule 3 from 02B). The 02B validate-entities.yml workflow enforces this level.

2. **Semantic conformance**: every record MUST be semantically consistent with the metamodel (CR-019, CR-022) and the OpenDEAM allocation (CR-AR-FMWK-04). The validate-against-model.yml reusable workflow enforces this level (from CR-IS-CAT-02).

3. **Cross-catalogue conformance**: every cross-catalogue relationship MUST be a valid instance of a registered metamodel relationship or OpenDEAM allocation declaration. The 02D validate-catalogue.yml workflow enforces this level.

4. **Governance conformance**: every record MUST be consistent with the governance model (G-01..G-12 from CR-IS-CAT-01 section 7). The governance model is captured in docs/governance.md. The governance conformance is enforced by code review and CR process; the 02D coverage reports provide the evidence.

## 5. 14-Step CI Validator

The new `validate-catalogue.yml` workflow runs 14 validation steps:

1. YAML/JSON parse
2. Relationship-type authorization check (the 8 kinds from section 2)
3. Cross-reference resolution (every source/target exists in the catalogue)
4. OpenDEAM allocation check (the `measured_by` kind is a declaration)
5. Conformance report generation (catalogue-conformance)
6. Conformance report generation (relationship-coverage)
7. Conformance report generation (reference-integrity)
8. Conformance report generation (taxonomy-coverage)
9. Conformance report generation (documentation-coverage)
10. Schema validation (relationship-record.schema.json)
11. Idempotency check (running the script twice produces the same reports)
12. Composition edge validation (rule 5 from 02B: registered relationship kind)
13. README template conformance (19 sections from 02B; check the section count)
14. Cardinality validation (per the source doc section 4 matrix; the source and target cardinality)

The validator distinguishes unavailable external validation from invalid local records (G-10).

## 6. 5 Conformance Reports

The deterministic generator at `scripts/generate_conformance_reports.py` produces 5 conformance reports:

1. **catalogue-conformance.yaml**: per-record conformance summary (records that pass all 4 levels)
2. **relationship-coverage.yaml**: per-relationship-kind coverage (which kinds are exercised by which records)
3. **reference-integrity.yaml**: cross-reference resolution (every target registered)
4. **taxonomy-coverage.yaml**: per-domain coverage (which ISCC domains are exercised by the P1 population)
5. **documentation-coverage.yaml**: per-record README coverage (which records have 19-section READMEs)

Each report is generated deterministically (G-10): running the script twice produces the same report.

## 7. Repository Deliverables (this PR; 9 files)

- `change-requests/CR-IS-CAT-02D-integration.md` (this file)
- `change-requests/README.md` (updated with 02D row)
- `relationships/v1-alpha/relationships.yaml` (new; 16 relationship records)
- `schemas/relationships/relationship-record.schema.json` (new; JSON Schema)
- `.github/workflows/validate-catalogue.yml` (new; 14-step CI validator)
- `scripts/generate_conformance_reports.py` (new; deterministic generator)
- 5 `reports/*.yaml` files (generated)

## 8. Acceptance Criteria

1. The 8 relationship kinds from the cross-catalogue matrix are documented.
2. 16 relationship records are registered in `relationships/v1-alpha/relationships.yaml`.
3. The relationship records validate against the JSON Schema.
4. The 14-step CI validator passes.
5. The 5 conformance reports are generated deterministically.
6. All 4 levels of the conformance architecture are exercised.
7. D-004 / D-005 / embargo clean across all 9 changed files.
8. Cardinal rule compliance: Author: Emmanuel A. Otchere (allowlist).
9. CI passes.

## 9. Definition of Done

The 5-CR ISC programme is complete when CR-IS-CAT-02D merges. After 02D, the remaining Path Y work in the IS catalogue cascade is:

- `CR-IS-CAT-03` (Information System Service; new; same 5-CR template)
- `CR-IS-CAT-04` (Integration Interface; new; same 5-CR template)
- `CR-IS-CAT-02-IFC` (IFC migration to `dea-catalog-infrastructure-components`; separate catalog)
- `CR-IS-CAT-01C-P2` (P2 population: 6 records)
- `CR-IS-CAT-01C-P3` (P3 population: 4 records)
- `CR-IS-CAT-02C-P2` (P2 follow-on population: 3 domains)
- `CR-IS-CAT-02C-P3` (P3 follow-on population: 2 domains)
- `CR-013 (dea-governance)` (portfolio adoption; the closure gate)

## 10. References

- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02-information-system-components-rename.md` (parent; merged 2026-10-18 via PR #2, commit `15e49ef`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02A-taxonomy.md` (sibling; merged 2026-10-18 via PR #3, commit `a50a1b5`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02B-documentation.md` (sibling; merged 2026-10-18 via PR #4, commit `b73655a`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02C-population.md` (sibling; merged 2026-10-18 via PR #5, commit `2df0c5b`)
- `technehub-labs/dea-catalog-application-components/taxonomy/` (the classification layer; 02A)
- `technehub-labs/dea-catalog-application-components/docs/decomposition-guide.md` (the F0-F5 model; 02B)
- `technehub-labs/dea-catalog-application-components/docs/coverage-reports/p1-coverage-report.md` (the P1 coverage report; 02C)
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the canonical entity)
- `technehub-labs/dea-architecture-framework/change-requests/CR-AR-FMWK-04-information-system-entity-allocation.md` (OpenDEAM extension)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01D-integration.md` (the ISF integration; the template)
- `technehub-labs/dea-catalog-system-functions/relationships/v1-alpha/relationships.yaml` (the ISF relationship registry; the template)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; the template)

## 11. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to 02D and are acknowledged in this PR:

- G-01: `dea:InformationSystemComponent` is the only canonical entity for new catalogue records.
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification (02A) and functional decomposition (02B) are separate structures.
- G-08: Every relationship uses an authorized semantic contract.
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-10: All generated artefacts must be reproducible and validated.
- G-11: Metric definitions remain owned by the Metric catalogue.
- G-12: No implementation-specific component becomes canonical merely because it exists in an application.

---

End of CR-IS-CAT-02D.
