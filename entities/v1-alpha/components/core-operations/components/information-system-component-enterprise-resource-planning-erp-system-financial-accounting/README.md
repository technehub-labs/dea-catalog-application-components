# Financial Accounting (Enterprise Resource Planning (ERP) System)

# 1. Component name and identifier
- Component name: Financial Accounting (Enterprise Resource Planning (ERP) System)
- Identifier: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting`

# 2. Definition
The Financial Accounting component group of the Enterprise Resource Planning (ERP) System: groups the composite components that realize the Financial Accounting behaviour of the vendor-neutral Enterprise Resource Planning (ERP) System class. The group is canonical; vendor module evidence is recorded in the ISF catalogue records (CR-IS-CAT-01C-P4).

# 3. Purpose and scope
This is a P4 vendor-neutral population record (CR-IS-CAT-02C-P4; the 5-CR programme population series). The P4 tranche admits generic component classes realized by commercial and open-source products from at least three distinct vendors; per G-12 no implementation-specific component is canonical. The record follows the F0-F5 decomposition model in docs/decomposition-guide.md.

# 4. Component type
ApplicationComponent

# 5. F-level assignment
F1

# 6. Component-domain assignment
`iscc:domain:core-operations`

# 7. Orthogonal classification facets
- Component kind: apc
- Hosting model / execution characteristics / criticality / deployment pattern / security posture / automation characteristics: not asserted by the vendor-neutral record; these facets vary across the corroborating vendor implementations and are populated per-deployment in a follow-on CR.

# 8. Composition (parent, children)
- Parent: `dea:information-system-component-enterprise-resource-planning-erp-system`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-billing-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-collections-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-cost-center-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-invoice-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-invoice-processing-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-journal-entry-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-journal-import-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-ledger-accounting-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-payment-engine-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-payment-format-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-payment-proposal-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-reconciliation-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-requisition-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-settlement-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-tax-component`
- Child: `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-voucher-component`

# 9. Composition edges
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-billing-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-collections-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-cost-center-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-invoice-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-invoice-processing-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-journal-entry-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-journal-import-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-ledger-accounting-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-payment-engine-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-payment-format-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-payment-proposal-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-reconciliation-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-requisition-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-settlement-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-tax-component`: contains (required)
- `dea:information-system-component-enterprise-resource-planning-erp-system-financial-accounting-voucher-component`: contains (required)

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
