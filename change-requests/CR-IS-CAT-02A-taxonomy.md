# CR-IS-CAT-02A: Information System Component Taxonomy and Classification Architecture

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-02A |
| **Title** | Information System Component Taxonomy and Classification Architecture |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue taxonomy and classification |
| **Repository** | technehub-labs/dea-catalog-information-system-components (legacy URL: technehub-labs/dea-catalog-application-components until org-admin transfer) |
| **Parent** | CR-IS-CAT-02 (merged 2026-10-18) |
| **Depends on** | CR-IS-CAT-02 (merged) |
| **Enables** | CR-IS-CAT-02B (documentation); CR-IS-CAT-02C (population); CR-IS-CAT-02D (integration) |
| **Canonical entity** | `dea:InformationSystemComponent` (class alias `ISC`; OpenDEAM-local `dea:entity-information-system-component`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR establishes the component taxonomy and classification architecture for the Information System Component (ISC) catalogue. The taxonomy is the catalogue-level content that classifies `dea:InformationSystemComponent` records (and its concrete specializations APC, IGC, and the new AIC = AI Component) across component domains, categories, subcategories and orthogonal classification facets.

The taxonomy is NOT a new metamodel entity hierarchy. It is a catalogue-level classification system. Per G-05, taxonomy nodes are catalogue classifications, not metamodel entities. Per G-06, classification (02A) and functional decomposition (02B) are separate structures. Per G-09, catalogue completeness must be evidenced, not assumed; the 02C population exercise is the validation step.

The 10 component domains are a starting baseline. The 02C population exercise validates the boundaries; gaps and overlaps discovered during 02C are recorded in the coverage report and trigger a taxonomy refinement CR.

## 2. Classification Principles

### 2.1 Component vs function

A component is a deployable architectural constituent. A function is the behaviour performed by a component. The taxonomy classifies the former, not the latter. Per the metamodel relationship (CR-018/019), the component executes the function; the taxonomy and the ISF taxonomy (CR-IS-CAT-01A) are separate classification systems.

### 2.2 Component vs application

A component is a deployable unit. An application is a system composed of one or more components. The taxonomy classifies the constituent, not the composite. Per the metamodel relationship (CR-017/018), a business process is enabled by functions, which are executed by components; the application is the composite that owns the components.

### 2.3 Functional classification vs technology classification

A component MUST NOT be classified primarily by its implementation technology. For example, a web application component remains a customer-experience component whether implemented in Java, Python, Node.js or Go. Implementation technology is captured through the orthogonal facet "execution characteristics" (5.3).

### 2.4 Multi-dimensional classification

A component MUST have exactly one primary component-domain assignment. It MAY have multiple additional classifications where justified. The primary classification supports catalogue navigation; orthogonal facets support analysis and discovery.

### 2.5 Taxonomy stability

The component-domain structure SHOULD remain relatively stable. New technology patterns, implementation methods and emerging practices SHOULD normally be expressed through orthogonal classification facets rather than constant restructuring of the component taxonomy.

## 3. Component Domain Taxonomy

The initial top-level component domains are:

| Code | Component domain | Scope |
|---|---|---|
| ISCC-01 | Customer Experience | Public-facing, customer-facing web/mobile/desktop components |
| ISCC-02 | Employee Experience | Internal-facing, employee-facing components (intranet, HR portal, productivity tools) |
| ISCC-03 | Partner Integration | Partner-facing, B2B components (EDI, partner portals, supplier interfaces) |
| ISCC-04 | Core Operations | Back-office components (ERP, CRM, finance, supply chain) |
| ISCC-05 | Data and Analytics | Data platform components (warehouse, lake, BI, analytics, ML training) |
| ISCC-06 | Integration | API gateway, message broker, ESB, integration endpoints (the IGC specializations) |
| ISCC-07 | Security | Identity broker, policy decision point, vault, secrets management |
| ISCC-08 | Observability | Monitoring, logging, tracing, alerting, metrics |
| ISCC-09 | Development Platform | CI/CD, dev tools, build infrastructure, artifact repositories |
| ISCC-10 | AI Native | AI inference, training, model serving, agentic components (the AIC specializations) |

These domains establish the initial taxonomy baseline. They MUST be reviewed against the population exercise in CR-IS-CAT-02C before being declared stable.

### 3.1 Doctrine on overlapping domains

The 10 domains are NOT strictly MECE. Known overlaps and the boundaries that resolve them (per the 5-CR programme template; analogous to the ISF 7 DOCTRINE-MECE boundaries from card #463):

1. **ISCC-07 (Security) vs ISCC-04 (Core Operations)**: ISCC-07 is the security infrastructure (identity broker, vault, PDP); ISCC-04 is the back-office systems. The boundary is security infrastructure vs business operations.
2. **ISCC-08 (Observability) vs ISCC-09 (Development Platform)**: ISCC-08 is the read-only monitoring infrastructure; ISCC-09 is the build/dev tools. The boundary is observation vs creation.
3. **ISCC-10 (AI Native) vs all other domains**: ISCC-10 is AI-native (model inference, training, agentic); AI-assisted versions of other components route through the orthogonal facet "automation characteristics" (5.7) with values `AI-assisted` or `agent-orchestrated`. The boundary is the primary behaviour is AI-native.
4. **ISCC-05 (Data and Analytics) vs ISCC-04 (Core Operations)**: ISCC-05 is the data platform (warehouse, lake, BI); ISCC-04 is the operational systems. The boundary is data storage/analytics vs business operations.

The 02C population exercise validates these boundaries. G-09 governs: catalogue completeness must be evidenced, not assumed.

## 4. Classification Hierarchy

Each component domain MAY contain:
- Component categories
- Component subcategories
- More specific component classifications

The hierarchy is:

```
Component Domain
  -> Component Category
  -> Component Subcategory
  -> Information System Component (instance)
```

A taxonomy node is a classification value, NOT an `dea:InformationSystemComponent` entity. The hierarchy MUST NOT be mistaken for component decomposition. Classification groups concepts; decomposition (CR-IS-CAT-02B) establishes behavioural composition.

## 5. Orthogonal Classification Facets

Every catalogue record SHOULD support the following facets where applicable.

### 5.1 Component kind

Examples: application (APC), integration (IGC), AI (AIC), security, observability, data, workflow.

### 5.2 Hosting model

Examples: cloud, on-premises, hybrid, edge, serverless, container, virtual-machine.

### 5.3 Execution characteristics

Examples: long-running, batch, event-driven, streaming, real-time, scheduled, on-demand.

### 5.4 Component criticality

Examples: mission-critical, business-critical, operationally-significant, supporting, convenience.

Criticality is contextual and MUST NOT be treated as an intrinsic universal characteristic of the component.

### 5.5 Deployment pattern

Examples: singleton, replicated, sharded, serverless, blue-green, canary, rolling.

### 5.6 Security posture

Examples: public-internet, internal-network, restricted-network, isolated-network, air-gapped, encrypted-at-rest, encrypted-in-transit.

### 5.7 Automation characteristics

Examples: manual-deployment, scripted-deployment, ci-cd-automated, gitops-automated, ai-assisted-deployment, agent-orchestrated.

This facet is the answer to the ISCC-10 vs all-other-domains overlap: an AI-assisted component is classified under its primary domain with this facet set to `AI-assisted` or `agent-orchestrated`; it is NOT classified under ISCC-10 unless the primary behaviour is AI-native.

## 6. Taxonomy Data Model

### 6.1 Files created

- `taxonomy/README.md` (this directory's purpose)
- `taxonomy/component-domains.yaml` (the 10 component domains)
- `taxonomy/orthogonal-facets.yaml` (the 7 orthogonal facets)
- `taxonomy/classification-rules.yaml` (the 11 classification rules)
- `schemas/taxonomy.schema.json` (JSON Schema for taxonomy records)

### 6.2 Required fields per taxonomy record

Each taxonomy record MUST include:
- Stable identifier (e.g., `iscc:domain:customer-experience` for ISCC-01)
- Name
- Definition
- Parent identifier (where applicable)
- Status (proposed, active, deprecated)
- Version
- Effective date
- Synonyms (where applicable)
- Inclusion criteria
- Exclusion criteria
- Related taxonomy references
- Change history

Taxonomy identifiers MUST remain stable across definition refinements. Renaming or restructuring MUST use a documented migration rather than identifier reuse.

## 7. Classification Rules

1. Every active component MUST have exactly one primary component-domain assignment.
2. Additional domain associations MUST be explicitly justified.
3. Classification MUST be based on the component's purpose.
4. Implementation technology MUST NOT determine component identity.
5. Application ownership MUST NOT determine component classification.
6. A component MUST NOT be classified as an application system (the application is a composite).
7. Classification nodes MUST NOT be registered as metamodel entities (G-05).
8. Deprecated taxonomy values MUST remain traceable.
9. No taxonomy node may have itself as an ancestor.
10. Circular taxonomy hierarchies MUST be rejected.
11. Classification assignments MUST reference registered taxonomy identifiers.

## 8. Repository Deliverables (this PR)

- `taxonomy/README.md` (new; classification architecture overview)
- `taxonomy/component-domains.yaml` (new; 10 component domains)
- `taxonomy/orthogonal-facets.yaml` (new; 7 orthogonal facets)
- `taxonomy/classification-rules.yaml` (new; 11 rules)
- `schemas/taxonomy.schema.json` (new; JSON Schema for taxonomy records)
- `.github/workflows/validate-taxonomy.yml` (new; CI validator)
- `change-requests/CR-IS-CAT-02A-taxonomy.md` (this file)
- `change-requests/README.md` (updated with 02A row)

## 9. CI Requirements

CI MUST validate:
- Taxonomy YAML syntax
- Unique taxonomy identifiers
- Valid parent references
- No circular hierarchy
- Valid status and lifecycle values
- Valid component-domain assignments
- No orphaned taxonomy references
- Stable identifier and migration rules
- Valid inclusion/exclusion metadata

The validation is implemented via a new workflow at `.github/workflows/validate-taxonomy.yml`. The workflow uses the existing reusable `validate-against-model.yml@v0.7.0` for the allocation check (from CR-IS-CAT-02); the new taxonomy validation is a local step in the same workflow.

## 10. Acceptance Criteria

1. All 10 initial component domains are represented.
2. Each domain has a normative definition.
3. Classification hierarchy is implemented.
4. Orthogonal facets are defined.
5. Primary and secondary classification rules are enforceable.
6. Taxonomy schemas validate.
7. Duplicate and circular identifiers are rejected by the CI validator.
8. Taxonomy is independent of the metamodel entity hierarchy.
9. CR-02C can use the taxonomy to classify initial catalogue records.
10. CI passes.

## 11. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Overly broad domains | Inclusion and exclusion criteria for each domain; per-record criticality; per-record technology neutralization |
| Overly granular taxonomy | Keep fine-grained classification at subcategory level; subcategories are populated in 02B |
| Technology-driven classification | Classification is based on component purpose; technology is captured through the orthogonal facet "execution characteristics" (5.3) |
| Artificial MECE claims | The 10-domain baseline is explicitly NOT MECE; cross-cutting concerns route through orthogonal facets; 02C population exercise validates boundaries |
| Taxonomy proliferation | Governance of additions and changes is recorded in section 7; per-rule change requires a documented migration |
| Confusion with decomposition | Per G-06, classification and decomposition are separate structures; 02A establishes classification, 02B establishes decomposition |

## 12. Definition of Done

The taxonomy is complete when component domains and classification facets are documented, machine-readable, validated and usable for consistent classification of the initial Information System Component catalogue. Per G-09, completeness is evidenced by the 02C population exercise; a populated domain is NOT automatically considered complete.

## 13. References

- `technehub-labs/dea-catalog-application-components/change-requests/CR-IS-CAT-02-information-system-components-rename.md` (parent; merged 2026-10-18 via PR #2, commit `15e49ef`)
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the canonical entity)
- `technehub-labs/dea-metamodel/change-requests/CR-022-metamodel-artifact-and-conformance-closure.md` (artifact closure)
- `technehub-labs/dea-architecture-framework/change-requests/CR-AR-FMWK-04-information-system-entity-allocation.md` (OpenDEAM extension; v0.6.0 -> v0.7.0)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01A-taxonomy.md` (the ISF taxonomy; the template)
- `technehub-labs/dea-catalog-system-functions/taxonomy/` (the ISF taxonomy files; the template)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; the template)
- `~/.hermes/profiles/coder/kanban/cr-is-cat-01-programme-plan-2026-10-18.md` (reconciliation plan)
- `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md` (snapshot)
- DOCTRINE-MECE card #463 on board 23 (the 7 boundary doctrines from 01A; the analog for 02A is the 4 doctrine in section 3.1)

## 14. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to 02A and are acknowledged in this PR:

- G-01: `dea:InformationSystemComponent` is the only canonical entity for new catalogue records.
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification and functional decomposition are separate structures.
- G-08: Every relationship uses an authorized semantic contract.
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-12: No implementation-specific component becomes canonical merely because it exists in an application.

---

End of CR-IS-CAT-02A.
