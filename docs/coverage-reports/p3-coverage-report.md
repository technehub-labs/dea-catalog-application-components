# P3 Coverage Report :  Information System Component
# CR-IS-CAT-02C-P3 (2026-10-18). The P3 follow-on population coverage report.

date: 2026-10-18
cr: CR-IS-CAT-02C-P3
parent_cr: CR-IS-CAT-02
sibling_crs: CR-IS-CAT-02C (P1); CR-IS-CAT-02C-P2 (P2)

## 1. Scope

This report covers the P3 follow-on population of the Information System Component (ISC) catalogue. The P3 tranche covers the final 2 component domains (out of the 10 ISCC domains in the taxonomy; 5 were covered by P1 per CR-IS-CAT-02C and 3 by P2 per CR-IS-CAT-02C-P2). For each domain, 1 F2 composite component and 3 F4 sub-components are populated. Total P3: 2 F2 + 6 F4 = 8 component records.

After the P3 population, the ISC catalogue covers **10 of 10 ISCC domains** with 38 component records. The domain coverage of the ISC catalogue is COMPLETE.

## 2. P3 Selection Methodology

The 2 P3 domains were selected by the following criteria:

1. **Enabling**: the domain enables the delivery of the other 9 domains.
2. **Emerging**: the domain represents an emerging architectural pattern whose boundary needed the most careful doctrine application.
3. **P3 priority**: the domain is in the P3 priority band of the IS Semantic Architecture programme (per the 5-CR programme template; the standing rule from 2026-10-18).

The 2 selected domains are:

| Code | Domain | Justification |
|---|---|---|
| ISCC-09 | Development Platform | Enabling; the delivery substrate for every other domain |
| ISCC-10 | AI Native | Emerging; the AI-native vs AI-assisted boundary is the most heavily scrutinised doctrine in the taxonomy |

## 3. P3 Component Inventory

### 3.1 ISCC-09 Development Platform (4 components)

| F-level | Component | Sub-components | Status |
|---|---|---|---|
| F2 | Development Platform | ci-cd-pipeline (F4); artifact-repository (F4); build-service (F4) | active |
| F4 | CI/CD Pipeline | (none) | active |
| F4 | Artifact Repository | (none) | active |
| F4 | Build Service | (none) | active |

### 3.2 ISCC-10 AI Native (4 components)

| F-level | Component | Type | Sub-components | Status |
|---|---|---|---|---|
| F2 | AI Inference Platform | AIComponent (AIC) | model-serving-runtime (F4); model-registry (F4); agent-orchestrator (F4) | active |
| F4 | Model Serving Runtime | AIComponent (AIC) | (none) | active |
| F4 | Model Registry | AIComponent (AIC) | (none) | active |
| F4 | Agent Orchestrator | AIComponent (AIC) | (none) | active |

## 4. Total counts

| Metric | P1 | P2 | P3 | Total |
|---|---|---|---|---|
| Component domains covered | 5 | 3 | 2 | **10 of 10 (100%)** |
| F2 composite components | 5 | 3 | 2 | 10 |
| F4 sub-components | 14 | 8 | 6 | 28 |
| Total component records | 19 | 11 | 8 | **38** |
| Composition edges | 14 | 8 | 6 | 28 |
| Cross-catalogue relationships | 16 | 6 | 5 | **27** |
| AIComponent (AIC) records | 0 | 0 | 4 | 4 |

## 5. Doctrine on Overlapping Domains (Validation)

The 4 boundary doctrines from CR-IS-CAT-02A section 3.1 are validated by the P3 population:

1. **ISCC-08 vs ISCC-09 boundary (observation vs creation)**: the Observability Platform (P2) is correctly classified under ISCC-08 (read-only telemetry aggregation). The Development Platform (P3) is correctly classified under ISCC-09 (the read-write operational platform for the build and delivery lifecycle). The Development Platform depends on the Observability Platform at runtime for build telemetry; the classification is by read-write character, not by dependency. **This is the boundary the P3 population was specifically selected to test.**

2. **ISCC-10 vs all-other-domains boundary (AI-native vs AI-assisted)**: the AI Inference Platform and its 3 sub-components are correctly classified under ISCC-10. Their primary behaviour is AI-native: model inference, model lineage, and agentic execution. The orthogonal facet 5.7 (automation characteristics) is set to `agent-orchestrated` for the AI Inference Platform, the Model Serving Runtime, and the Agent Orchestrator. The Model Registry is set to `gitops-automated` because its primary behaviour is deterministic lifecycle management, not agentic execution. This is the first use of the `agent-orchestrated` facet value in the catalogue, and it demonstrates the doctrine in practice: an AI-native component is classified by its primary behaviour, while the automation facet records the agentic mode independently.

3. **ISCC-09 vs ISCC-10 boundary**: the CI/CD Pipeline is correctly classified under ISCC-09, not ISCC-10, even though an AI-assisted build pipeline is a plausible future state. An AI-assisted build pipeline is a CI/CD Pipeline with the orthogonal facet 5.7 set to `ai-assisted-deployment`; it does not become an AI-native component.

4. **ISCC-04 vs ISCC-09 boundary**: the Development Platform is correctly classified under ISCC-09 (delivery substrate), not ISCC-04 (business operations). The classification is by the component's purpose, not by the business capability it ultimately serves.

## 6. Cross-Catalogue Relationships (P3)

The 5 new cross-catalogue relationships added by the P3 population:

| ID | Source | Relationship | Target |
|---|---|---|---|
| isc-rel-201 | development-platform | depends-on | data-warehouse-platform |
| isc-rel-202 | ai-inference-platform | depends-on | observability-platform |
| isc-rel-203 | agent-orchestrator | exposes | if:agent-orchestrator-internal |
| isc-rel-204 | ai-inference-platform | measured_by | metric:inference-latency-p99 |
| isc-rel-205 | ai-inference-platform | consumes | data-entity:model-artifacts |

Total: 27 cross-catalogue relationships (16 P1 + 6 P2 + 5 P3).

## 7. Exclusions

The following component kinds remain excluded from the ISC catalogue:

- **IFC (Infrastructure Component)**: not in scope of this catalogue; the IFC records are migrated to a separate catalog (`dea-catalog-infrastructure-components`) in a follow-on CR-IS-CAT-02-IFC.
- **Vendor-specific component instances**: per G-12, no implementation-specific component becomes canonical merely because it exists in an application. Vendor-specific components are referenced through the metamodel `dea:executes` relationship in 02D; they do not appear as catalogue records.
- **Test components and ephemeral components**: not in scope of the canonical catalogue.

## 8. Conclusion

The P3 follow-on population completes the ISC catalogue's domain coverage: **10 of 10 ISCC domains** are populated with 38 component records (10 F2 + 28 F4) and 27 cross-catalogue relationships. The ISCC-08 vs ISCC-09 boundary (observation vs creation) and the ISCC-10 vs all-other-domains boundary (AI-native vs AI-assisted) are validated by the P3 population, and the orthogonal facet 5.7 (automation characteristics) is exercised with the `agent-orchestrated` value for the first time.

The ISC catalogue's structural and content work is complete. The remaining ISC work is the IFC migration (CR-IS-CAT-02-IFC), which requires a separate catalog repository.
