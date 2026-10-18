# Decomposition Guide :  Information System Component

This guide documents the F0-F5 component decomposition model and the 14 validation rules for the Information System Component (ISC) catalogue. The decomposition standard is the catalogue-level content that governs how component records are structured and how compositions are expressed.

## F0-F5 Decomposition Model

The F0-F5 model establishes 6 levels of component decomposition. A component MUST be assigned exactly one F-level at any given time.

| Level | Name | Description |
|---|---|---|
| F0 | System | A complete application system composed of one or more F1 groups |
| F1 | Component Group | A coherent group of related F2 composite components |
| F2 | Composite Component | A composite component that contains F3 atomic components and F4 sub-components |
| F3 | Atomic Component | An atomic component that is not decomposed further in the catalogue |
| F4 | Sub-Component | A sub-component of an F2 or F3 |
| F5 | Leaf | A leaf-level implementation unit |

## Composition rules

A composition is expressed through the `composed_of` field. The composition rules are:

- An F0 contains one or more F1.
- An F1 contains one or more F2.
- An F2 contains one or more F3 and F4.
- An F3 may contain one or more F4.
- An F4 may contain one or more F5.
- An F0 MUST contain at least one F1.
- An F1 MUST contain at least one F2.
- An F2 MAY contain F3 and F4.
- The composition depth MUST NOT exceed 6 (F0..F5).
- A component MUST NOT be its own ancestor.
- The composition tree MUST be acyclic.

## Composition edge kinds

A composition edge carries the relationship kind. The 4 authorized kinds are:

- `contains` (the parent contains the child structurally)
- `depends-on` (the parent depends on the child for runtime execution)
- `hosts` (the parent hosts the child for deployment purposes)
- `orchestrates` (the parent orchestrates the child; reserved for orchestration frameworks)

## 14 Validation Rules

The 14 validation rules governing component records and the decomposition structure:

1. Every active component MUST have exactly one F-level assignment.
2. Every active component MUST have exactly one primary component-domain assignment.
3. Every active component MUST have a README that follows the 19-section template.
4. Composition edges MUST reference registered component identifiers.
5. Composition edges MUST use a registered relationship kind.
6. An F2 component MAY contain F3 and F4 components.
7. An F1 component MUST contain at least one F2 component.
8. An F0 component MUST contain at least one F1 component.
9. A component MUST NOT be its own ancestor (no self-ancestor).
10. The composition tree MUST be acyclic.
11. The composition depth MUST NOT exceed 6 (F0..F5).
12. Cross-component composition edges MUST use the v2 schema's `composition` array.
13. The README MUST include a change history.
14. The README MUST reference the parent and child components.

## README Standard

Each component record MUST have an associated README. The README MUST follow the 19-section template in `templates/README-template.md`. The 19 sections are:

1. Component name and identifier
2. Definition
3. Purpose and scope
4. Component type
5. F-level assignment
6. Component-domain assignment
7. Orthogonal classification facets
8. Composition (parent, children)
9. Composition edges
10. Functional realization (functions realized by this component)
11. Cross-references (components related by other metamodel relationships)
12. Hosting and deployment
13. Criticality and security posture
14. Performance characteristics
15. Disaster recovery posture
16. Compliance posture
17. Owner
18. Change history
19. References

## Schema versioning

The v1 schema (introduced in CR-IS-CAT-02) is a minimal schema with the entity ID, name, definition, and primary component-domain assignment. The v2 schema extends v1 with the F-level assignment, composition edges, orthogonal facets, and the 19-section README reference.

Existing v1 records continue to be valid. New records MUST use the v2 schema. The 02C population exercise may supersede v1 records with v2 records; the supersession is a documented change with a `supersedes: [...]` field in the v2 record.

## Cross-references

- `taxonomy/` (the classification layer; orthogonal to the decomposition layer per G-06)
- `change-requests/CR-IS-CAT-02B-documentation.md` (the CR doc that establishes this standard)
- `templates/component-template.yaml` (the machine-readable component template)
- `templates/README-template.md` (the 19-section README template)
- `schemas/entities/information-system-component.v2.json` (the v2 schema)
- `entities/v1-alpha/` (the catalogue records; populated by 02C)
- `.github/workflows/validate-entities.yml` (the CI validator)
