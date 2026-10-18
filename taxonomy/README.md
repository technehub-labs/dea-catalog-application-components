# Taxonomy :  Information System Component Classification

This directory holds the catalogue-level classification architecture for the Information System Component (ISC) catalogue.

The taxonomy is NOT a new metamodel entity hierarchy. It is a catalogue-level classification system that classifies instances of `dea:InformationSystemComponent` (and its concrete specializations APC, IGC, AIC) across component domains, categories, subcategories and orthogonal classification facets. Per G-05 (programme-wide governance), taxonomy nodes are catalogue classifications, not metamodel entities. Per G-06, classification (this directory) and component decomposition (CR-IS-CAT-02B) are separate structures.

## Files

| File | Purpose |
|---|---|
| `component-domains.yaml` | The 10 initial top-level component domains (ISCC-01..ISCC-10) with normative definitions, scope, inclusion criteria and exclusion criteria |
| `orthogonal-facets.yaml` | The 7 orthogonal classification facets (5.1-5.7) |
| `classification-rules.yaml` | The 11 classification rules that govern how components are classified |

## The 10 component domains

| Code | Domain | Scope summary |
|---|---|---|
| ISCC-01 | Customer Experience | Public-facing, customer-facing web/mobile/desktop components |
| ISCC-02 | Employee Experience | Internal-facing, employee-facing components |
| ISCC-03 | Partner Integration | Partner-facing, B2B components |
| ISCC-04 | Core Operations | Back-office components (ERP, CRM, finance, supply chain) |
| ISCC-05 | Data and Analytics | Data platform components (warehouse, lake, BI, analytics, ML training) |
| ISCC-06 | Integration | API gateway, message broker, ESB, integration endpoints (IGC specializations) |
| ISCC-07 | Security | Identity broker, policy decision point, vault, secrets management |
| ISCC-08 | Observability | Monitoring, logging, tracing, alerting, metrics |
| ISCC-09 | Development Platform | CI/CD, dev tools, build infrastructure, artifact repositories |
| ISCC-10 | AI Native | AI inference, training, model serving, agentic components (AIC specializations) |

## Doctrine on overlapping domains

The 10 domains are NOT strictly MECE. Known overlaps and the boundaries that resolve them:

1. **ISCC-07 vs ISCC-04**: security infrastructure vs business operations.
2. **ISCC-08 vs ISCC-09**: observation vs creation.
3. **ISCC-10 vs all**: AI-native primary vs AI-assisted orthogonal facet 5.7.
4. **ISCC-05 vs ISCC-04**: data storage/analytics vs business operations.

The 02C population exercise is the validation step. G-09 governs: catalogue completeness must be evidenced, not assumed.

## Cross-cutting concerns and orthogonal facets

Cross-cutting concerns (technology, AI assistance, hosting model, criticality, deployment pattern, security posture, automation mode) are NOT component domains. They are orthogonal facets. A component MAY have multiple orthogonal facet values; a component MUST have exactly one primary component-domain assignment.

## Identifier convention

Taxonomy identifiers follow `iscc:<type>:<slug>` where `<type>` is `domain`, `category`, `subcategory`, or `facet`, and `<slug>` is the kebab-case name. Example: `iscc:domain:customer-experience`.

## Validation

CI validates the taxonomy at `.github/workflows/validate-taxonomy.yml`. The validation checks:
- YAML syntax
- Unique identifiers
- Valid parent references
- No circular hierarchy
- Valid status and lifecycle values
- Valid component-domain assignments
- No orphaned references
- Stable identifier and migration rules
- Valid inclusion/exclusion metadata

## References

- `change-requests/CR-IS-CAT-02A-taxonomy.md` (the CR doc that establishes this standard)
- `change-requests/CR-IS-CAT-02-information-system-components-rename.md` (parent; CR-IS-CAT-02)
- `technehub-labs/dea-catalog-system-functions/taxonomy/` (the ISF taxonomy; the template)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01A-taxonomy.md` (the ISF taxonomy CR; the template)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; the template)
- `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md` (snapshot)
