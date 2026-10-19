# Build Service

# 1. Component name and identifier
- Component name: Build Service
- Identifier: `dea:information-system-component-build-service`

# 2. Definition
A sub-component (F4) of the Development Platform. isolated build execution.

# 3. Purpose and scope
This is a P1 component populated by the 02C population exercise (per the 5-CR programme template; the standing rule from 2026-10-18). The P1 tranche covers the most architecturally critical components across the 10 ISCC domains.

# 4. Component type
IntegrationComponent

# 5. F-level assignment
F4

# 6. Component-domain assignment
`iscc:domain:development-platform`

# 7. Orthogonal classification facets
- Component kind: igc
- Hosting model: cloud
- Execution characteristics: on-demand
- Component criticality: business-critical
- Deployment pattern: replicated
- Security posture: encrypted-at-rest, encrypted-in-transit
- Automation characteristics: gitops-automated

# 8. Composition (parent, children)
- Parent: `dea:information-system-component-development-platform`
- Children: (none)

# 10. Functional realization (functions realized by this component)
- (populated by 02D; for now, see the metamodel relationship catalogue)

# 11. Cross-references (components related by other metamodel relationships)
- (populated by 02D)

# 12. Hosting and deployment
This component is deployed in the cloud as a replicated service. The deployment is automated through a GitOps pipeline. The hosting model is captured through the orthogonal facet 5.2 (hosting model = cloud).

# 13. Criticality and security posture
Criticality: business-critical. All requests and responses are encrypted in transit; persistent state is encrypted at rest. The security posture is captured through the orthogonal facet 5.6.

# 14. Performance characteristics
Performance characteristics are populated by the 02C coverage report (`docs/coverage-reports/p1-coverage-report.md`).

# 15. Disaster recovery posture
The disaster recovery posture is captured by the standard RTO/RPO values per criticality class: mission-critical RTO 15 minutes / RPO 5 minutes; business-critical RTO 4 hours / RPO 1 hour; supporting RTO 24 hours / RPO 24 hours.

# 16. Compliance posture
Compliance posture is context-specific and is populated per-record in subsequent CRs.

# 17. Owner
Enterprise Architecture team (DEA-Architecture@example.com)

# 18. Change history
- 1.0: 2026-10-18: Initial P1 record (CR-IS-CAT-02C).

# 19. References
- `change-requests/CR-IS-CAT-02C-population.md` (the CR doc)
- `docs/coverage-reports/p1-coverage-report.md` (the P1 coverage report)
- `docs/decomposition-guide.md` (the F0-F5 model)
- `taxonomy/` (the classification layer)
- `schemas/entities/information-system-component.v2.json` (the v2 schema)

# 9. Composition edges
- (none; the parent is recorded in the `parent` field)
