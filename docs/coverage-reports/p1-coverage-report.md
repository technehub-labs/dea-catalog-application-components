# P1 Coverage Report :  Information System Component
# CR-IS-CAT-02C (2026-10-18). The P1 population coverage report.

date: 2026-10-18
cr: CR-IS-CAT-02C
parent_cr: CR-IS-CAT-02

## 1. Scope

This report covers the P1 priority population of the Information System Component (ISC) catalogue. The P1 tranche covers 5 architecturally foundational component domains (out of the 10 ISCC domains in the taxonomy). For each domain, 1 F2 composite component and 2-3 F4 sub-components are populated. Total: 5 F2 + 14 F4 = 19 component records.

The P1 population is the validation step for the 10-domain taxonomy established in CR-IS-CAT-02A. The P2 and P3 follow-on populations extend the catalog to the remaining 5 domains.

## 2. Population methodology

The 5 P1 domains were selected by the following criteria:

1. **Foundational**: the domain is architecturally foundational to any information system.
2. **Cross-cutting**: the domain has cross-cutting concerns that affect multiple other domains.
3. **P1 priority**: the domain is in the P1 priority band of the IS Semantic Architecture programme (per the 5-CR programme template; the standing rule from 2026-10-18).

The 5 selected domains are:

| Code | Domain | Justification |
|---|---|---|
| ISCC-01 | Customer Experience | Foundational; the primary external interface |
| ISCC-04 | Core Operations | Foundational; the back-office substrate |
| ISCC-05 | Data and Analytics | Cross-cutting; powers all other domains |
| ISCC-06 | Integration | Cross-cutting; enables the other domains to interact |
| ISCC-07 | Security | Foundational; required by every other domain |

The remaining 5 domains (ISCC-02 Employee Experience; ISCC-03 Partner Integration; ISCC-08 Observability; ISCC-09 Development Platform; ISCC-10 AI Native) are deferred to P2 and P3 follow-on populations.

## 3. P1 component inventory

### 3.1 ISCC-01 Customer Experience (4 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Customer-Facing Web Application Platform | customer-web-frontend (F4); customer-web-bff (F4); customer-web-cdn (F4) | active |
| F4 | Customer Web Frontend | (none) | active |
| F4 | Customer Web Backend-for-Frontend | (none) | active |
| F4 | Customer Web CDN | (none) | active |

### 3.2 ISCC-04 Core Operations (3 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Order Management System | order-management-orchestrator (F4); order-fulfillment-worker (F4) | active |
| F4 | Order Management Orchestrator | (none) | active |
| F4 | Order Fulfillment Worker | (none) | active |

### 3.3 ISCC-05 Data and Analytics (4 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Data Warehouse Platform | data-warehouse-loader (F4); data-warehouse-query (F4); data-warehouse-catalog (F4) | active |
| F4 | Data Warehouse Loader | (none) | active |
| F4 | Data Warehouse Query | (none) | active |
| F4 | Data Warehouse Catalog | (none) | active |

### 3.4 ISCC-06 Integration (4 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | API Gateway | api-gateway-router (F4); api-gateway-rate-limiter (F4); api-gateway-authenticator (F4) | active |
| F4 | API Gateway Router | (none) | active |
| F4 | API Gateway Rate Limiter | (none) | active |
| F4 | API Gateway Authenticator | (none) | active |

### 3.5 ISCC-07 Security (4 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Identity Broker | oidc-discovery (F4); identity-broker-token-issuer (F4); identity-broker-session-store (F4) | active |
| F4 | OIDC Discovery | (none) | active |
| F4 | Identity Broker Token Issuer | (none) | active |
| F4 | Identity Broker Session Store | (none) | active |

## 4. Total counts

| Metric | Count |
|---|---|
| Component domains covered | 5 of 10 (50%) |
| F2 composite components | 5 |
| F3 atomic components | 0 |
| F4 sub-components | 14 |
| F5 leaf components | 0 |
| Total component records | 19 |
| Composition edges | 14 (one per F2 to each F4 child) |
| Validation rules enforced | 14 (from 02B) |

## 5. Doctrine on overlapping domains (validation)

The 4 boundary doctrines from CR-IS-CAT-02A section 3.1 are validated by the P1 population:

1. **ISCC-07 vs ISCC-04 boundary**: the Identity Broker is correctly classified under ISCC-07 (security infrastructure); the Order Management System is correctly classified under ISCC-04 (back-office). The Identity Broker depends on the Order Management System at runtime (recorded in the metamodel `dea:executes` relationship in 02D); the classification is by primary purpose, not by dependency.
2. **ISCC-05 vs ISCC-04 boundary**: the Data Warehouse Platform is correctly classified under ISCC-05 (data platform); the Order Management System is correctly classified under ISCC-04 (operations). The Order Management System produces data that the Data Warehouse Platform ingests; the classification is by primary purpose, not by data flow.
3. **ISCC-06 vs other-domain boundary**: the API Gateway is correctly classified under ISCC-06 (integration); none of the other P1 components duplicate this. The API Gateway is the only IGC (Integration Component) in the P1 population that is the primary integration component; the Identity Broker is a secondary IGC.
4. **ISCC-10 vs all-other-domains boundary**: no P1 component is classified under ISCC-10 (AI Native). The AI-assisted components are deferred to the P3 follow-on population.

## 6. Deferred components (P2 and P3)

The remaining 5 component domains are deferred:

| Code | Domain | Priority | Target CR |
|---|---|---|---|
| ISCC-02 | Employee Experience | P2 | CR-IS-CAT-02C-P2 |
| ISCC-03 | Partner Integration | P2 | CR-IS-CAT-02C-P2 |
| ISCC-08 | Observability | P2 | CR-IS-CAT-02C-P2 |
| ISCC-09 | Development Platform | P3 | CR-IS-CAT-02C-P3 |
| ISCC-10 | AI Native | P3 | CR-IS-CAT-02C-P3 |

## 7. Exclusions

The following component kinds are explicitly excluded from the P1 population:

- **IFC (Infrastructure Component)**: not in scope of this catalogue; the IFC records are migrated to a separate catalog (`dea-catalog-infrastructure-components`) in a follow-on CR-IS-CAT-02-IFC.
- **Vendor-specific component instances**: per G-12, no implementation-specific component becomes canonical merely because it exists in an application. Vendor-specific components are referenced through the metamodel `dea:executes` relationship in 02D; they do not appear as catalogue records.
- **Test components and ephemeral components**: not in scope of the canonical catalogue.

## 8. Conclusion

The P1 population validates the 10-domain taxonomy established in CR-IS-CAT-02A. The 5 selected domains cover the most architecturally critical components. The 4 boundary doctrines are validated by the P1 population. The remaining 5 domains are deferred to P2 and P3 follow-on populations.
