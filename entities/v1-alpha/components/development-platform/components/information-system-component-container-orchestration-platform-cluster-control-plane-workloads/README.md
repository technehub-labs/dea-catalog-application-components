# Cluster Control Plane & Workloads (Container Orchestration Platform)

# 1. Component name and identifier
- Component name: Cluster Control Plane & Workloads (Container Orchestration Platform)
- Identifier: `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads`

# 2. Definition
The Cluster Control Plane & Workloads component group of the Container Orchestration Platform: groups the composite components that realize the Cluster Control Plane & Workloads behaviour of the vendor-neutral Container Orchestration Platform class. The group is canonical; vendor module evidence is recorded in the ISF catalogue records (CR-IS-CAT-01C-P4).

# 3. Purpose and scope
This is a P4 vendor-neutral population record (CR-IS-CAT-02C-P4; the 5-CR programme population series). The P4 tranche admits generic component classes realized by commercial and open-source products from at least three distinct vendors; per G-12 no implementation-specific component is canonical. The record follows the F0-F5 decomposition model in docs/decomposition-guide.md.

# 4. Component type
IntegrationComponent

# 5. F-level assignment
F1

# 6. Component-domain assignment
`iscc:domain:development-platform`

# 7. Orthogonal classification facets
- Component kind: igc
- Hosting model / execution characteristics / criticality / deployment pattern / security posture / automation characteristics: not asserted by the vendor-neutral record; these facets vary across the corroborating vendor implementations and are populated per-deployment in a follow-on CR.

# 8. Composition (parent, children)
- Parent: `dea:information-system-component-container-orchestration-platform`
- Child: `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-controller-component`
- Child: `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-node-agent-component`
- Child: `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-scheduler-component`
- Child: `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-state-store-component`

# 9. Composition edges
- `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-controller-component`: contains (required)
- `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-node-agent-component`: contains (required)
- `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-scheduler-component`: contains (required)
- `dea:information-system-component-container-orchestration-platform-cluster-control-plane-workloads-state-store-component`: contains (required)

# 10. Functional realization (functions realized by this component)
- The functions realized by this component group are recorded on its descendant components; see the descendant records and the ISF catalogue (CR-IS-CAT-01C-P4 executing_components crawl).

# 11. Cross-references (components related by other metamodel relationships)
- (none in this CR; cross-catalogue relationships remain owned by CR-IS-CAT-02D)

# 12. Hosting and deployment
The hosting model is not asserted by the vendor-neutral record; the generic class is commonly offered as cloud, on-premises or hybrid deployments across the corroborating vendors. The hosting facet is populated per-deployment.

# 13. Criticality and security posture
Criticality and security posture facets are not asserted by the vendor-neutral record; they are populated per-deployment once the criticality class is asserted.

# 14. Performance characteristics
Performance characteristics are vendor-deployment-specific and are not asserted by the vendor-neutral record.

# 15. Disaster recovery posture
The disaster recovery posture is captured by the standard RTO/RPO values per criticality class once the criticality facet is asserted per-deployment: mission-critical RTO 15 minutes / RPO 5 minutes; business-critical RTO 4 hours / RPO 1 hour; supporting RTO 24 hours / RPO 24 hours.

# 16. Compliance posture
Compliance posture is context-specific and is populated per-record in subsequent CRs.

# 17. Owner
Enterprise Architecture team (DEA-Architecture@example.com)

# 18. Change history
- 1.0: 2026-11-10: Initial P4 vendor-neutral record (CR-IS-CAT-02C-P4).

# 19. References
- `change-requests/CR-IS-CAT-02C-P4-vendor-neutral-component-population.md` (the CR doc)
- `docs/coverage-reports/p4-coverage-report.md` (the P4 coverage report)
- `docs/decomposition-guide.md` (the F0-F5 model)
- `taxonomy/` (the classification layer)
- `schemas/entities/information-system-component.v2.json` (the v2 schema)
- `technehub-labs/dea-catalog-system-functions` (the executing-function catalogue; CR-IS-CAT-01C-P4)
