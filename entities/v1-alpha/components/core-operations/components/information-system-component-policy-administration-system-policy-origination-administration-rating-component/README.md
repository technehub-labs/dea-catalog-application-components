# Rating Component (Policy Origination & Administration, Policy Administration System)

# 1. Component name and identifier
- Component name: Rating Component (Policy Origination & Administration, Policy Administration System)
- Identifier: `dea:information-system-component-policy-administration-system-policy-origination-administration-rating-component`

# 2. Definition
The Rating Component of the Policy Origination & Administration group of the Policy Administration System: a vendor-neutral composite component executing the functions allocated to the Rating Component in the Policy Origination & Administration behaviour of the Policy Administration System class.

# 3. Purpose and scope
This is a P4 vendor-neutral population record (CR-IS-CAT-02C-P4; the 5-CR programme population series). The P4 tranche admits generic component classes realized by commercial and open-source products from at least three distinct vendors; per G-12 no implementation-specific component is canonical. The record follows the F0-F5 decomposition model in docs/decomposition-guide.md.

# 4. Component type
ApplicationComponent

# 5. F-level assignment
F2

# 6. Component-domain assignment
`iscc:domain:core-operations`

# 7. Orthogonal classification facets
- Component kind: apc
- Hosting model / execution characteristics / criticality / deployment pattern / security posture / automation characteristics: not asserted by the vendor-neutral record; these facets vary across the corroborating vendor implementations and are populated per-deployment in a follow-on CR.

# 8. Composition (parent, children)
- Parent: `dea:information-system-component-policy-administration-system-policy-origination-administration`
- Children: (none)

# 9. Composition edges
- (none; the parent is recorded in the `parent` field)

# 10. Functional realization (functions realized by this component)
- Executes 8 vendor-neutral function record(s) of the P4 population (CR-IS-CAT-01C-P4 in technehub-labs/dea-catalog-system-functions); each function record lists this component in `executing_components`.

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
