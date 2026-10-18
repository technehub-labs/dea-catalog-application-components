# README Template :  Information System Component v2
# CR-IS-CAT-02B (2026-10-18). The 19-section README template for an
# Information System Component record. New records MUST follow this template.

# 1. Component name and identifier
# Component name: <Name>
# Identifier: dea:information-system-component-<slug>

# 2. Definition
<one-paragraph definition>

# 3. Purpose and scope
<one-paragraph purpose and scope>

# 4. Component type
<Type: InformationSystemComponent (abstract) | ApplicationComponent | IntegrationComponent | AIComponent>

# 5. F-level assignment
<F0 | F1 | F2 | F3 | F4 | F5>

# 6. Component-domain assignment
<iscc:domain:<slug>>

# 7. Orthogonal classification facets
- Component kind: <value>
- Hosting model: <values>
- Execution characteristics: <values>
- Component criticality: <value>
- Deployment pattern: <values>
- Security posture: <values>
- Automation characteristics: <value>

# 8. Composition (parent, children)
- Parent: <dea:information-system-component-<parent-slug>> (if any)
- Children: <list of dea:information-system-component-<child-slug>>

# 9. Composition edges
- <target>: <contains | depends-on | hosts | orchestrates> (<cardinality>)

# 10. Functional realization (functions realized by this component)
- <dea:information-system-function-<slug>>: <relationship kind>

# 11. Cross-references (components related by other metamodel relationships)
- <dea:information-system-component-<slug>>: <relationship kind>

# 12. Hosting and deployment
<hosting model and deployment pattern summary>

# 13. Criticality and security posture
<criticality and security posture summary>

# 14. Performance characteristics
<performance summary>

# 15. Disaster recovery posture
<DR summary>

# 16. Compliance posture
<compliance summary>

# 17. Owner
<owner (team or organization)>

# 18. Change history
- <version>: <date>: <change summary>

# 19. References
- <list of references>
