# P2 Coverage Report :  Information System Component
# CR-IS-CAT-02C-P2 (2026-10-18). The P2 follow-on population coverage report.

date: 2026-10-18
cr: CR-IS-CAT-02C-P2
parent_cr: CR-IS-CAT-02
sibling_cr: CR-IS-CAT-02C (P1)

## 1. Scope

This report covers the P2 follow-on population of the Information System Component (ISC) catalogue. The P2 tranche covers 3 additional component domains (out of the 10 ISCC domains in the taxonomy; 5 were covered by the P1 tranche per CR-IS-CAT-02C). For each domain, 1 F2 composite component and 2-3 F4 sub-components are populated. Total P2: 3 F2 + 8 F4 = 11 component records. Total catalog after P2: 8 F2 + 22 F4 = 30 component records across 8 of 10 domains.

The P2 population is the second validation step for the 10-domain taxonomy established in CR-IS-CAT-02A. The P3 follow-on population (2 domains) further extends the catalog to 10 of 10 domains.

## 2. P2 Selection Methodology

The 3 P2 domains were selected by the following criteria:

1. **Internal-facing**: the domain is internal-facing (not customer-facing).
2. **Operational**: the domain has cross-cutting operational concerns.
3. **P2 priority**: the domain is in the P2 priority band of the IS Semantic Architecture programme (per the 5-CR programme template; the standing rule from 2026-10-18).

The 3 selected domains are:

| Code | Domain | Justification |
|---|---|---|
| ISCC-02 | Employee Experience | Internal-facing; the primary internal interface |
| ISCC-03 | Partner Integration | B2B; the cross-organization interface |
| ISCC-08 | Observability | Cross-cutting; required by every other domain for operational insight |

The remaining 2 domains (ISCC-09 Development Platform; ISCC-10 AI Native) are deferred to the P3 follow-on population.

## 3. P2 Component Inventory

### 3.1 ISCC-02 Employee Experience (3 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Employee Portal Platform | employee-portal-frontend (F4); employee-portal-bff (F4) | active |
| F4 | Employee Portal Frontend | (none) | active |
| F4 | Employee Portal Backend-for-Frontend | (none) | active |

### 3.2 ISCC-03 Partner Integration (4 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Partner Portal Platform | partner-portal-onboarding (F4); partner-portal-data-exchange (F4); partner-portal-settlement (F4) | active |
| F4 | Partner Portal Onboarding | (none) | active |
| F4 | Partner Portal Data Exchange | (none) | active |
| F4 | Partner Portal Settlement | (none) | active |

### 3.3 ISCC-08 Observability (4 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Observability Platform | metrics-collector (F4); log-aggregator (F4); distributed-tracer (F4) | active |
| F4 | Metrics Collector | (none) | active |
| F4 | Log Aggregator | (none) | active |
| F4 | Distributed Tracer | (none) | active |

## 4. Total counts

| Metric | P1 | P2 | Total |
|---|---|---|---|
| Component domains covered | 5 | 3 | 8 of 10 (80%) |
| F2 composite components | 5 | 3 | 8 |
| F4 sub-components | 14 | 8 | 22 |
| Total component records | 19 | 11 | 30 |
| Composition edges | 14 | 8 | 22 |
| Cross-catalogue relationships | 16 | 6 | 22 |

## 5. Doctrine on Overlapping Domains (Validation)

The 4 boundary doctrines from CR-IS-CAT-02A section 3.1 are validated by the P2 population:

1. **ISCC-08 vs ISCC-09 boundary**: the Observability Platform is correctly classified under ISCC-08 (observation). The Development Platform (ISCC-09) is the read-write operational platform for the build/dev lifecycle; the Observability Platform (ISCC-08) is the read-only telemetry aggregation. The boundary is observation vs creation.
2. **ISCC-02 vs ISCC-04 boundary**: the Employee Portal Platform is correctly classified under ISCC-02 (employee-facing). The Order Management System (ISCC-04 from P1) is back-office operations. The Employee Portal depends on the Order Management System at runtime (recorded in the metamodel `dea:executes` relationship in 02D); the classification is by primary purpose, not by dependency.
3. **ISCC-03 vs ISCC-06 boundary**: the Partner Portal Platform is correctly classified under ISCC-03 (partner-facing B2B). The API Gateway (ISCC-06 from P1) is the internal integration component. The Partner Portal depends on the API Gateway at runtime; the classification is by primary audience (partner vs internal), not by integration dependency.
4. **ISCC-10 vs all-other-domains boundary**: no P2 component is classified under ISCC-10 (AI Native). The AI-assisted components are deferred to the P3 follow-on population.

## 6. Cross-Catalogue Relationships (P2)

The 6 new cross-catalogue relationships added by the P2 population:

| ID | Source | Relationship | Target |
|---|---|---|---|
| isc-rel-101 | employee-portal-platform | depends-on | identity-broker |
| isc-rel-102 | employee-portal-platform | exposes | if:employee-portal-internal |
| isc-rel-103 | partner-portal-platform | depends-on | api-gateway |
| isc-rel-104 | partner-portal-data-exchange | consumes | data-entity:partner-transactions |
| isc-rel-105 | observability-platform | depends-on | data-warehouse-platform |
| isc-rel-106 | observability-platform | measured_by | metric:observability-data-freshness |

Total: 22 cross-catalogue relationships (16 from P1 + 6 from P2).

## 7. Deferred Components (P3)

The remaining 2 component domains are deferred to the P3 follow-on population:

| Code | Domain | Priority | Target CR |
|---|---|---|---|
| ISCC-09 | Development Platform | P3 | CR-IS-CAT-02C-P3 |
| ISCC-10 | AI Native | P3 | CR-IS-CAT-02C-P3 |

## 8. Conclusion

The P2 follow-on population extends the catalog from 19 to 30 component records across 8 of 10 component domains. The 4 boundary doctrines from CR-IS-CAT-02A are further validated. The remaining 2 domains (ISCC-09 Development Platform; ISCC-10 AI Native) are deferred to the P3 follow-on population.
