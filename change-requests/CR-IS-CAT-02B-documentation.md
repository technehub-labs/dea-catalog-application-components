# CR-IS-CAT-02B: Information System Component Documentation and Decomposition Standard

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-02B |
| **Title** | Information System Component Documentation and Decomposition Standard |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue documentation and decomposition standard |
| **Repository** | technehub-labs/dea-catalog-information-system-components (legacy URL: technehub-labs/dea-catalog-application-components until org-admin transfer) |
| **Parent** | CR-IS-CAT-02 (merged 2026-10-18); CR-IS-CAT-02A (merged 2026-10-18) |
| **Depends on** | CR-IS-CAT-02 (merged); CR-IS-CAT-02A (merged) |
| **Enables** | CR-IS-CAT-02C (population); CR-IS-CAT-02D (integration) |
| **Canonical entity** | `dea:InformationSystemComponent` (class alias `ISC`; OpenDEAM-local `dea:entity-information-system-component`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR establishes the documentation and decomposition standard for the Information System Component catalogue. The standard is the catalogue-level content that governs how `dea:InformationSystemComponent` records (and its concrete specializations APC, IGC, AIC) are documented, decomposed and structurally related. The decomposition standard is the catalogue-level content that supports the metamodel relationships from CR-018/019.

The standard is NOT a new metamodel entity hierarchy. It is a catalogue-level structural standard. Per G-05, taxonomy nodes are catalogue classifications, not metamodel entities. Per G-06, classification (02A) and functional decomposition (02B) are separate structures. The classification layer is a taxonomy of component domains; the decomposition layer is a structural model of component composition.

## 2. Decomposition Principles

### 2.1 Component vs composition

A component is a deployable unit. A composition is a structured arrangement of one or more components. The decomposition standard governs how compositions are expressed through component records. The component is a single node; the composition is a graph of nodes.

### 2.2 Functional decomposition vs structural decomposition

A component is decomposed for structural reasons (deployment, ownership, reuse), not for functional reasons (a function is decomposed separately in the ISF catalogue). A component may realize multiple functions; a function may be realized by multiple components. The decomposition is at the component layer only.

### 2.3 Component atomicity is contextual

A component is atomic relative to its deployment context. A service is a component, a service mesh is a composition of services, a microservice is a component, a process orchestrating microservices is a composition. The same artefact may be atomic in one context and part of a composition in another.

### 2.4 Composition vs orchestration

Composition is the structural relationship; orchestration is the runtime relationship. The decomposition standard records composition only. Orchestration is recorded in the metamodel (CR-017/018: `dea:executes` is a runtime relationship).

### 2.5 Multi-level composition is permitted

A composition may contain other compositions; the F0-F5 model supports up to 6 levels of nesting. The F0 level is the system (e.g., the customer-facing web application system); F5 is the leaf (e.g., a single authentication routine). The intermediate levels are contextual.

## 3. F0-F5 Decomposition Model

The F0-F5 model establishes 6 levels of component decomposition. The model is the same as the ISF F0-F5 model (per CR-IS-CAT-01B) but applied to components.

| Level | Name | Description | Example |
|---|---|---|---|
| F0 | System | A complete application system composed of one or more F1 groups | Customer-facing web application |
| F1 | Component Group | A coherent group of related F2 composite components | Identity and access group |
| F2 | Composite Component | A composite component that contains F3 atomic components and F4 sub-components | Identity broker |
| F3 | Atomic Component | An atomic component that is not decomposed further in the catalogue | OIDC server |
| F4 | Sub-Component | A sub-component of an F2 or F3 | OIDC discovery endpoint |
| F5 | Leaf | A leaf-level implementation unit | A specific function call within a sub-component |

A component MUST be assigned exactly one F-level at any given time. A component MAY be reclassified as the catalogue evolves; the reclassification is a documented change, not a silent move.

### 3.1 Composition rule

A composition is expressed through the `composed_of` field. An F0 contains one or more F1; an F1 contains one or more F2; an F2 contains one or more F3 and F4; an F3 may contain one or more F4; an F4 may contain one or more F5. Compositions are recorded at each level independently.

A component MUST NOT be its own ancestor in the decomposition tree. The validator rejects cycles (rule 9, 10, 11 from CR-IS-CAT-02A).

### 3.2 Composition edges

A composition edge carries the relationship kind: `contains`, `depends-on`, `hosts`, `orchestrates`. The relationship kind is recorded in the `composition_edge_kind` field. Per G-08 (every relationship uses an authorized semantic contract), the kinds are:

- `contains` (the parent contains the child structurally)
- `depends-on` (the parent depends on the child for runtime execution)
- `hosts` (the parent hosts the child for deployment purposes)
- `orchestrates` (the parent orchestrates the child; the parent is the orchestrator)

The `orchestrates` kind is reserved for orchestration frameworks; per the doctrine (section 2.4), orchestration is a runtime concept and is captured in the metamodel `dea:executes` relationship. The `orchestrates` composition edge is a structural label only.

## 4. Component Record Schema

### 4.1 Required fields per record

Each component record MUST include:
- Stable identifier (e.g., `dea:information-system-component-identity-broker`)
- Name
- Definition
- F-level assignment (F0, F1, F2, F3, F4, or F5)
- Component type (`InformationSystemComponent` abstract; or a concrete specialization like `ApplicationComponent`, `IntegrationComponent`, `AIComponent`)
- Primary component-domain assignment (from `taxonomy/component-domains.yaml`)
- Composition edges (where applicable)
- Status (proposed, active, deprecated, retired)
- Version
- Effective date
- Documentation reference (link to the README)

### 4.2 Optional fields

- Orthogonal classification facets (from `taxonomy/orthogonal-facets.yaml`)
- Owner (the team or organization responsible)
- Hosting model (also captured via the orthogonal facet 5.2)
- Criticality (also captured via the orthogonal facet 5.4)
- Security posture (also captured via the orthogonal facet 5.6)
- Performance characteristics
- Disaster recovery posture
- Compliance posture

## 5. README Standard

Each component record MUST have an associated README. The README MUST follow the 19-section template in `templates/README-template.md`.

The 19 sections are:

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

## 6. Composition Edge Schema

Each composition edge MUST include:
- Source component identifier
- Target component identifier
- Relationship kind (contains, depends-on, hosts, orchestrates)
- Cardinality (one, many, optional, required)
- Version
- Effective date
- Status

Composition edges are recorded inline in the component record's `composition` field. Cross-component composition edges (where source and target live in different F-levels) are recorded in the v2 schema's `composition` array.

## 7. Repository Deliverables (this PR)

- `change-requests/CR-IS-CAT-02B-documentation.md` (this file)
- `change-requests/README.md` (updated with 02B row)
- `docs/decomposition-guide.md` (new; F0-F5 model + 14 validation rules)
- `templates/component-template.yaml` (new; machine-readable)
- `templates/README-template.md` (new; 19-section template)
- `schemas/entities/information-system-component.v2.json` (new; v2 schema)
- `entities/v1-alpha/README.md` (new; directory structure)
- `entities/v1-alpha/index.yaml` (new; catalog-level index)
- `entities/v1-alpha/components/index.yaml` (new; component-level index)
- `entities/v1-alpha/components/identity-and-access/index.yaml` (new; domain-level index)
- `entities/v1-alpha/components/identity-and-access/components/dea-isc-identity-broker/component.yaml` (new; F2 example)
- `entities/v1-alpha/components/identity-and-access/components/dea-isc-identity-broker/README.md` (new; F2 README)
- `entities/v1-alpha/components/identity-and-access/components/dea-isc-oidc-discovery/component.yaml` (new; F4 example)
- `entities/v1-alpha/components/identity-and-access/components/dea-isc-oidc-discovery/README.md` (new; F4 README)
- `.github/workflows/validate-entities.yml` (new; CI validator)

## 8. CI Requirements

CI MUST validate:
- Component record YAML syntax
- Required fields (section 4.1)
- F-level assignment is one of F0..F5
- Primary component-domain assignment exists in taxonomy
- Orthogonal facets reference registered taxonomy identifiers
- Composition edges reference registered component identifiers
- No cycles in the composition tree
- README exists for every active component
- 19-section README template conformance
- Composition edge kind is one of `contains`, `depends-on`, `hosts`, `orchestrates`

The validation is implemented at `.github/workflows/validate-entities.yml`. The workflow is a local step (no external reusable workflow).

## 9. 14 Validation Rules

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

## 10. Acceptance Criteria

1. The F0-F5 decomposition model is documented.
2. The v2 ISC schema is registered.
3. The 19-section README template is registered.
4. The component template is registered.
5. Two example records (F2 + F4) are registered.
6. The catalog-level index is registered.
7. The component-level index is registered.
8. The domain-level index is registered.
9. The 14 validation rules are enforceable through CI.
10. The 19-section README template conformance is enforceable through CI.
11. CR-02C can use the standard to populate the initial component inventory.
12. CI passes.

## 11. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Overly nested compositions | Composition depth limited to 6 levels (F0..F5); the 02C population exercise validates the boundaries |
| Confusing composition with classification | Per G-06, classification (02A) and decomposition (02B) are separate structures; the README template section 6 distinguishes them |
| Implementation technology leaking into decomposition | The decomposition is structural; implementation technology is captured through the orthogonal facet 5.3 (execution characteristics) |
| Documentation decay | Every active component MUST have a README (rule 3); README MUST include a change history (rule 13) |
| Composition edge proliferation | The 4 relationship kinds (contains, depends-on, hosts, orchestrates) are the only authorized kinds; rule 5 enforces this |
| Schema versioning | The v2 schema is additive; v1 records continue to be valid until 02C supersedes them; the migration is documented in section 13 |

## 12. Definition of Done

The documentation and decomposition standard is complete when the F0-F5 model, the v2 schema, the README template, the component template, the example records, and the CI validator are all in place and CI passes.

## 13. Migration from v1

The v1 schema (introduced in CR-IS-CAT-02) is a minimal schema with the entity ID, name, definition, and primary component-domain assignment. The v2 schema extends v1 with the F-level assignment, composition edges, orthogonal facets, and the 19-section README reference.

Existing v1 records continue to be valid. New records MUST use the v2 schema. The 02C population exercise may supersede v1 records with v2 records; the supersession is a documented change with a `supersedes: [...]` field in the v2 record.

## 14. References

- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02-information-system-components-rename.md` (parent; merged 2026-10-18 via PR #2, commit `15e49ef`)
- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02A-taxonomy.md` (sibling; merged 2026-10-18 via PR #3, commit `a50a1b5`)
- `technehub-labs/dea-catalog-application-components/taxonomy/` (the taxonomy; the upstream of this CR)
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the canonical entity)
- `technehub-labs/dea-metamodel/change-requests/CR-022-metamodel-artifact-and-conformance-closure.md` (artifact closure)
- `technehub-labs/dea-architecture-framework/change-requests/CR-AR-FMWK-04-information-system-entity-allocation.md` (OpenDEAM extension)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01B-decomposition.md` (the ISF decomposition; the template)
- `technehub-labs/dea-catalog-system-functions/docs/decomposition-guide.md` (the ISF decomposition guide; the template)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; the template)
- `~/.hermes/profiles/coder/kanban/cr-is-cat-01-programme-plan-2026-10-18.md` (reconciliation plan)
- `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md` (snapshot)

## 15. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to 02B and are acknowledged in this PR:

- G-01: `dea:InformationSystemComponent` is the only canonical entity for new catalogue records.
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification (02A) and functional decomposition (02B) are separate structures.
- G-07: Every active component has machine-readable content and individual documentation.
- G-08: Every relationship uses an authorized semantic contract.
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-12: No implementation-specific component becomes canonical merely because it exists in an application.

---

End of CR-IS-CAT-02B.
