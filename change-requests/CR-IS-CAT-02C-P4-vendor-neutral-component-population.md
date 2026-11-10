# CR-IS-CAT-02C-P4: Information System Component P4 Vendor-Neutral Population

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-02C-P4 |
| **Title** | Information System Component P4 Vendor-Neutral Population (generic system classes) |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue population (P4 follow-on; vendor-neutral tranche) |
| **Repository** | technehub-labs/dea-catalog-information-system-components (legacy URL: technehub-labs/dea-catalog-application-components until org-admin transfer) |
| **Parent** | CR-IS-CAT-02 (merged); CR-IS-CAT-02A (merged); CR-IS-CAT-02B (merged); CR-IS-CAT-02C (merged); CR-IS-CAT-02D (merged) |
| **Depends on** | CR-IS-CAT-02 (merged); CR-IS-CAT-02A..02D (merged) |
| **Canonical entity** | `dea:InformationSystemComponent` (class alias `ISC`; OpenDEAM-local `dea:entity-information-system-component`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-10 |

## 1. Executive Summary

This CR is the P4 follow-on population of the ISC catalogue: a vendor-neutral tranche of generic
system classes grounded in commonly stated industry terminology. It adds
34 F0 system classes, 63 F1 component groups and 141 F2 composite components
(238 records total) across 8 of 10 ISCC domains. After
this PR merges the ISC catalogue holds 276 component records.

Every generic class in the tranche is corroborated by commercial and open-source products from at
least three distinct vendors. Per G-12 no implementation-specific component becomes canonical:
vendor products appear as evidence in the ISF catalogue records (CR-IS-CAT-01C-P4), never as component
names, identifiers or facets in this catalogue. The F0-F5 model from docs/decomposition-guide.md
is applied in full: F0 (system) contains F1 (component groups); F1 contains F2 (composite
components); composition edges use kind=contains, cardinality=required.

## 2. Selection Methodology

The P4 tranche is selected from a vendor-neutral reference catalog of information system
functions built on the OpenDEAM metamodel (system to sub-system to component to service crawl
with the ISC executes ISF relationship grammar). Selection criteria:

1. **Generic**: the class is stated in commonly used industry terms (ERP System, EHR, Core
   Banking System, MES, BSS, OSS, mobile core, RAN and so on), not a vendor product name.
2. **Corroborated**: at least 3 distinct vendors realize the class in the market.
3. **Crawlable**: the class decomposes to sub-systems and components that execute functions
   allocated in the ISF catalogue (CR-IS-CAT-01C-P4).

## 3. P4 Component Inventory

| Domain | F0 classes | F1 groups | F2 components | Total |
|---|---|---|---|---|
| Customer Experience | 3 | 7 | 19 | 29 |
| Employee Experience | 2 | 2 | 12 | 16 |
| Partner Integration | 2 | 2 | 2 | 6 |
| Core Operations | 14 | 39 | 83 | 136 |
| Data and Analytics | 3 | 3 | 3 | 9 |
| Integration | 4 | 4 | 5 | 13 |
| Security | 1 | 1 | 6 | 8 |
| Development Platform | 5 | 5 | 11 | 21 |

Component kinds across the 34 system classes: apc 21,
igc 10, data 2,
security 1.

## 4. Doctrine and Classification

Per G-05 and G-06, classification (component domain) and decomposition (F-level) are separate.
The P4 classes map one system class to exactly one primary ISCC domain by the component purpose
doctrine from CR-IS-CAT-02A. The full class to domain mapping:

| Identifier | Generic system class | ISCC domain | Kind | F1 groups | F2 components |
|---|---|---|---|---|---|
| `dea:information-system-component-card-payment-network` | Card Payment Network | Core Operations | apc | 1 | 1 |
| `dea:information-system-component-claims-management-system` | Claims Management System | Core Operations | apc | 1 | 1 |
| `dea:information-system-component-core-banking-system` | Core Banking System | Core Operations | apc | 5 | 11 |
| `dea:information-system-component-electronic-health-record-ehr-system` | Electronic Health Record (EHR) System | Core Operations | apc | 3 | 11 |
| `dea:information-system-component-enterprise-resource-planning-erp-system` | Enterprise Resource Planning (ERP) System | Core Operations | apc | 7 | 37 |
| `dea:information-system-component-manufacturing-execution-system-mes` | Manufacturing Execution System (MES) | Core Operations | apc | 1 | 1 |
| `dea:information-system-component-mobile-core-network-epc-5gc` | Mobile Core Network (EPC/5GC) | Core Operations | apc | 4 | 4 |
| `dea:information-system-component-payment-processing-platform` | Payment Processing Platform | Core Operations | apc | 3 | 3 |
| `dea:information-system-component-policy-administration-system` | Policy Administration System | Core Operations | apc | 1 | 1 |
| `dea:information-system-component-radio-access-network-ran` | Radio Access Network (RAN) | Core Operations | apc | 3 | 3 |
| `dea:information-system-component-telecom-business-support-system-bss` | Telecom Business Support System (BSS) | Core Operations | apc | 4 | 4 |
| `dea:information-system-component-telecom-operations-support-system-oss` | Telecom Operations Support System (OSS) | Core Operations | apc | 4 | 4 |
| `dea:information-system-component-transportation-management-system-tms` | Transportation Management System (TMS) | Core Operations | apc | 1 | 1 |
| `dea:information-system-component-warehouse-management-system-wms` | Warehouse Management System (WMS) | Core Operations | apc | 1 | 1 |
| `dea:information-system-component-customer-relationship-management-crm-system` | Customer Relationship Management (CRM) System | Customer Experience | apc | 4 | 16 |
| `dea:information-system-component-customer-service-ticketing-platform` | Customer Service Ticketing Platform | Customer Experience | apc | 1 | 1 |
| `dea:information-system-component-e-commerce-platform` | E-Commerce Platform | Customer Experience | apc | 2 | 2 |
| `dea:information-system-component-cloud-data-warehouse` | Cloud Data Warehouse | Data and Analytics | data | 1 | 1 |
| `dea:information-system-component-data-lakehouse-platform` | Data Lakehouse Platform | Data and Analytics | data | 1 | 1 |
| `dea:information-system-component-workflow-orchestration-platform` | Workflow Orchestration Platform | Data and Analytics | apc | 1 | 1 |
| `dea:information-system-component-cloud-infrastructure-platform` | Cloud Infrastructure Platform | Development Platform | igc | 1 | 4 |
| `dea:information-system-component-container-orchestration-platform` | Container Orchestration Platform | Development Platform | igc | 1 | 4 |
| `dea:information-system-component-continuous-integration-continuous-delivery-ci-cd-platform` | Continuous Integration / Continuous Delivery (CI/CD) Platform | Development Platform | igc | 1 | 1 |
| `dea:information-system-component-infrastructure-as-code-iac-platform` | Infrastructure as Code (IaC) Platform | Development Platform | igc | 1 | 1 |
| `dea:information-system-component-issue-tracking-platform` | Issue Tracking Platform | Development Platform | igc | 1 | 1 |
| `dea:information-system-component-human-capital-management-hcm-system` | Human Capital Management (HCM) System | Employee Experience | apc | 1 | 8 |
| `dea:information-system-component-it-service-management-itsm-platform` | IT Service Management (ITSM) Platform | Employee Experience | apc | 1 | 4 |
| `dea:information-system-component-communications-platform-cpaas` | Communications Platform (CPaaS) | Integration | igc | 1 | 1 |
| `dea:information-system-component-email-delivery-platform` | Email Delivery Platform | Integration | igc | 1 | 1 |
| `dea:information-system-component-event-streaming-platform` | Event Streaming Platform | Integration | igc | 1 | 1 |
| `dea:information-system-component-iot-device-management-platform` | IoT Device Management Platform | Integration | igc | 1 | 2 |
| `dea:information-system-component-financial-messaging-network` | Financial Messaging Network | Partner Integration | igc | 1 | 1 |
| `dea:information-system-component-supply-chain-visibility-platform` | Supply Chain Visibility Platform | Partner Integration | apc | 1 | 1 |
| `dea:information-system-component-identity-and-access-management-iam-platform` | Identity and Access Management (IAM) Platform | Security | security | 1 | 6 |

Doctrine notes:

1. **ISCC-04 vs other domains**: business-operation systems (ERP, core banking, insurance, EHR,
   payments, telecom BSS/OSS/core/RAN, commerce-adjacent operations) classify under Core
   Operations by purpose; customer-facing channel platforms (CRM, e-commerce, ticketing) under
   Customer Experience; employee-facing platforms (HCM, ITSM) under Employee Experience.
2. **ISCC-03**: network platforms that integrate with partners (financial messaging, supply chain
   visibility) classify under Partner Integration.
3. **ISCC-09 vs ISCC-06**: the delivery substrate (container orchestration, IaC, CI/CD, cloud
   infrastructure, issue tracking) classifies under Development Platform; message-transport
   platforms (event streaming, CPaaS, email, device connectivity) under Integration.
4. **F-level legacy**: the P1-P3 records retain their F2/F4 assignments (composite + sub-
   component) pending a rebasing CR; the P4 tranche applies the full F0/F1/F2 model per the
   decomposition guide. Both decompositions validate under the CI rules (composition kinds,
   acyclicity, README conformance).
5. **Facets**: only the component_kind facet is asserted by the vendor-neutral records;
   hosting, execution, criticality, deployment, security and automation facets vary across the
   corroborating vendor implementations and are deferred to per-deployment CRs (documented in
   each README section 7).

## 5. Executing-Function Crawl

The CR-IS-CAT-01C-P4 population in technehub-labs/dea-catalog-system-functions references these
component records via `executing_components` (the ISC executes ISF relationship grammar). The
ISF target-id snapshot pin for dea-catalog-application-components is advanced to the head commit
of this PR; the ISF CI hard check (unresolved_count = 0) resolves all 594 new references against
that snapshot.

## 6. Repository Deliverables (this PR)

- `change-requests/CR-IS-CAT-02C-P4-vendor-neutral-component-population.md` (this file)
- `change-requests/README.md` (updated with the P4 row)
- `docs/coverage-reports/p4-coverage-report.md` (new; the coverage report)
- `scripts/generate_p4_population.py` (new; deterministic idempotent generator)
- `scripts/p4_component_data.json` (new; the P4 inventory)
- `entities/v1-alpha/index.yaml` (updated; catalog counts and change history)
- 8 domain index.yaml files (updated)
- 238 component.yaml records + 238
  19-section READMEs under `entities/v1-alpha/components/`
- `reports/catalogue-conformance.yaml`, `reports/taxonomy-coverage.yaml`,
  `reports/documentation-coverage.yaml` (refreshed committed copies; CI regenerates)

## 7. CI Requirements

CI MUST validate (validate-entities, validate-catalogue, validate-taxonomy,
validate-allocation): v2 ISC schema validation for all
276 records; README existence and 19-section conformance; F-level
assignment; composition edge kinds; component_domain registered in the taxonomy; relationship
registry authorization (unchanged); reference-integrity (unchanged relationships; 0 unresolved);
conformance report determinism.

## 8. Acceptance Criteria

1. 34 F0 system classes, 63 F1 component groups and 141 F2 composite
   components are admitted with vendor-neutral identifiers and names.
2. Every F0 contains at least one F1; every F1 contains at least one F2 (decomposition guide
   rules 7 and 8).
3. All records validate against schemas/entities/information-system-component.v2.json.
4. All records have a 19-section README with the composition and change-history sections.
5. No vendor product name appears in any canonical field (per G-12).
6. The domain indexes and catalog index reflect the new counts.
7. The deterministic generator reproduces the P4 artifacts byte-identically (G-10).
8. CI passes.

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Vendor-specific leakage | Generic names and identifiers only; vendor products appear as evidence in the ISF catalogue, never in this catalogue (per G-12); a vendor-token assertion runs in the P4 generator pipeline |
| Over-broad generic classes | Every class is corroborated by at least 3 distinct vendors in the market before admission |
| Facet under-assertion | Only vendor-invariant facets are asserted; deployment-specific facets are explicitly deferred and documented in README section 7 |
| Legacy F-level mismatch with P1-P3 | Documented in section 4 note 4; a rebasing CR is queued as remaining work |
| Telecommunications terminology | Embargo-clean generic terminology only (BSS, OSS, mobile core, RAN); no standards-body vocabulary is used |

## 10. Definition of Done

The P4 population is complete when all 238 records validate, the
executing-function crawl from CR-IS-CAT-01C-P4 resolves, the coverage report is committed and CI passes.

## 11. Remaining ISC Work

- CR-IS-CAT-02-IFC: infrastructure component migration (requires an org-admin repo create).
- Per-deployment facet population CR (hosting, criticality, security posture).
- F-level rebasing CR for the P1-P3 records onto the full F0/F1/F2 model.
- ISS and IF catalogue populations (CR-IS-CAT-03/04) so the provides/exposes crawl completes.
