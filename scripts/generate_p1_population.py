#!/usr/bin/env python3
"""
CR-IS-CAT-02C (2026-10-18). Deterministic generator for the P1
component population. Produces 5 F2 components and 13 F4 sub-components
(18 records total) across 5 P1 component domains.

Per the 5-CR programme template (the standing rule from 2026-10-18),
the generator is the source of truth for P1 records; hand-editing
is discouraged. The generator is reproducible; running it twice
produces the same output.

P1 component domains and components (5 domains, 5 F2 + 13 F4):

ISCC-01 Customer Experience:
  - customer-facing-web-application-platform (F2)
    - customer-web-frontend (F4)
    - customer-web-bff (F4)
    - customer-web-cdn (F4)

ISCC-04 Core Operations:
  - order-management-system (F2)
    - order-management-orchestrator (F4)
    - order-fulfillment-worker (F4)

ISCC-05 Data and Analytics:
  - data-warehouse-platform (F2)
    - data-warehouse-loader (F4)
    - data-warehouse-query (F4)
    - data-warehouse-catalog (F4)

ISCC-06 Integration:
  - api-gateway (F2)
    - api-gateway-router (F4)
    - api-gateway-rate-limiter (F4)
    - api-gateway-authenticator (F4)

ISCC-07 Security:
  - identity-broker (F2; example from 02B)
    - oidc-discovery (F4; example from 02B)

Total: 5 F2 + 13 F4 = 18 component records.
"""
import os
import pathlib
import textwrap

REPO = pathlib.Path('/home/hermes/dea-work/dea-catalog-application-components')
ENTITIES = REPO / 'entities' / 'v1-alpha' / 'components'

# P1 component definitions
P1_DOMAINS = [
    {
        'id': 'iscc:domain:customer-experience',
        'code': 'ISCC-01',
        'name': 'Customer Experience',
        'dir': 'customer-experience',
        'components': [
            {
                'id': 'dea:information-system-component-customer-facing-web-application-platform',
                'name': 'Customer-Facing Web Application Platform',
                'f_level': 'F2',
                'type': 'ApplicationComponent',
                'criticality': 'business-critical',
                'description': 'The composite component that hosts the customer-facing web application: the frontend, the backend-for-frontend, and the content delivery network.',
                'subcomponents': [
                    {'id': 'customer-web-frontend', 'name': 'Customer Web Frontend', 'kind': 'real-time web UI'},
                    {'id': 'customer-web-bff', 'name': 'Customer Web Backend-for-Frontend', 'kind': 'API aggregation layer'},
                    {'id': 'customer-web-cdn', 'name': 'Customer Web CDN', 'kind': 'content delivery edge'},
                ],
            },
        ],
    },
    {
        'id': 'iscc:domain:core-operations',
        'code': 'ISCC-04',
        'name': 'Core Operations',
        'dir': 'core-operations',
        'components': [
            {
                'id': 'dea:information-system-component-order-management-system',
                'name': 'Order Management System',
                'f_level': 'F2',
                'type': 'ApplicationComponent',
                'criticality': 'mission-critical',
                'description': 'The composite component that owns the order lifecycle: order capture, orchestration, fulfillment, and acknowledgement.',
                'subcomponents': [
                    {'id': 'order-management-orchestrator', 'name': 'Order Management Orchestrator', 'kind': 'stateful workflow engine'},
                    {'id': 'order-fulfillment-worker', 'name': 'Order Fulfillment Worker', 'kind': 'event-driven async worker'},
                ],
            },
        ],
    },
    {
        'id': 'iscc:domain:data-and-analytics',
        'code': 'ISCC-05',
        'name': 'Data and Analytics',
        'dir': 'data-and-analytics',
        'components': [
            {
                'id': 'dea:information-system-component-data-warehouse-platform',
                'name': 'Data Warehouse Platform',
                'f_level': 'F2',
                'type': 'ApplicationComponent',
                'criticality': 'business-critical',
                'description': 'The composite component that hosts the enterprise data warehouse: the loader, the query interface, and the catalog.',
                'subcomponents': [
                    {'id': 'data-warehouse-loader', 'name': 'Data Warehouse Loader', 'kind': 'batch and streaming ETL'},
                    {'id': 'data-warehouse-query', 'name': 'Data Warehouse Query', 'kind': 'analytical SQL engine'},
                    {'id': 'data-warehouse-catalog', 'name': 'Data Warehouse Catalog', 'kind': 'metadata and lineage catalog'},
                ],
            },
        ],
    },
    {
        'id': 'iscc:domain:integration',
        'code': 'ISCC-06',
        'name': 'Integration',
        'dir': 'integration',
        'components': [
            {
                'id': 'dea:information-system-component-api-gateway',
                'name': 'API Gateway',
                'f_level': 'F2',
                'type': 'IntegrationComponent',
                'criticality': 'mission-critical',
                'description': 'The composite component that fronts the public APIs: routing, rate limiting, and authentication.',
                'subcomponents': [
                    {'id': 'api-gateway-router', 'name': 'API Gateway Router', 'kind': 'request routing'},
                    {'id': 'api-gateway-rate-limiter', 'name': 'API Gateway Rate Limiter', 'kind': 'token bucket rate limiter'},
                    {'id': 'api-gateway-authenticator', 'name': 'API Gateway Authenticator', 'kind': 'JWT and OAuth validation'},
                ],
            },
        ],
    },
    {
        'id': 'iscc:domain:security',
        'code': 'ISCC-07',
        'name': 'Security',
        'dir': 'security',
        # The security domain is partially populated by 02B example records;
        # 02C only adds the new F4 sub-components (skip the F2 example).
        'add_f2': False,
        'components': [
            {
                'id': 'dea:information-system-component-identity-broker',
                'name': 'Identity Broker',
                'f_level': 'F2',
                'type': 'IntegrationComponent',
                'criticality': 'mission-critical',
                'description': 'The composite component that federates identity and access decisions across multiple identity providers.',
                'subcomponents': [
                    {'id': 'oidc-discovery', 'name': 'OIDC Discovery', 'kind': 'OIDC metadata publication', 'existing': True},
                    {'id': 'identity-broker-token-issuer', 'name': 'Identity Broker Token Issuer', 'kind': 'JWT token issuance'},
                    {'id': 'identity-broker-session-store', 'name': 'Identity Broker Session Store', 'kind': 'distributed session store'},
                ],
            },
        ],
    },
]


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def render_component_yaml(comp):
    """Render a component.yaml for a given component dict."""
    facets = {
        'component_kind': {'ApplicationComponent': 'apc', 'IntegrationComponent': 'igc', 'AIComponent': 'aic'}.get(comp.get('type'), 'apc'),
        'hosting_model': ['cloud'],
        'execution_characteristics': ['long-running'],
        'component_criticality': comp.get('criticality', 'business-critical'),
        'deployment_pattern': ['replicated'],
        'security_posture': ['encrypted-at-rest', 'encrypted-in-transit'],
        'automation_characteristics': 'gitops-automated',
    }
    if comp.get('criticality') == 'mission-critical':
        facets['security_posture'].append('internal-network')
    return f"""id: {comp['id']}
type: {comp['type']}
name: {comp['name']}
status: active
version: "1.0"
effective_date: "2026-10-18"

f_level: {comp['f_level']}

component_domain: {comp.get('domain', '')}

facets:
  component_kind: {facets['component_kind']}
  hosting_model:
{chr(10).join('    - ' + m for m in facets['hosting_model'])}
  execution_characteristics:
{chr(10).join('    - ' + m for m in facets['execution_characteristics'])}
  component_criticality: {facets['component_criticality']}
  deployment_pattern:
{chr(10).join('    - ' + m for m in facets['deployment_pattern'])}
  security_posture:
{chr(10).join('    - ' + m for m in facets['security_posture'])}
  automation_characteristics: {facets['automation_characteristics']}

readme: ./README.md
"""


def render_subcomponent_yaml(f2_id, f4):
    """Render a sub-component (F4) component.yaml."""
    sub_id = f"dea:information-system-component-{f4['id']}"
    return f"""id: {sub_id}
type: {f4.get('type', 'IntegrationComponent')}
name: {f4['name']}
status: active
version: "1.0"
effective_date: "2026-10-18"

f_level: F4

component_domain: {f4.get('domain', '')}

facets:
  component_kind: {f4.get('component_kind', 'igc')}
  hosting_model:
    - cloud
  execution_characteristics:
    - on-demand
  component_criticality: business-critical
  deployment_pattern:
    - replicated
  security_posture:
    - encrypted-in-transit
  automation_characteristics: {f4.get('automation', 'gitops-automated')}

parent: {f2_id}

readme: ./README.md
"""


def render_readme(comp, kind, parent_id=None, f_level=None):
    """Render a 19-section README."""
    if f_level is None:
        f_level = comp.get('f_level', 'F4')
    parent_line = f"- Parent: `{parent_id}`" if parent_id else "- Parent: (none)"
    children_lines = ""
    if comp.get('subcomponents'):
        children_lines = "- Children:\n" + "\n".join(
            f"  - `dea:information-system-component-{sc['id']}` ({sc['name']})"
            for sc in comp['subcomponents']
        )
    else:
        children_lines = "- Children: (none)"
    composition_lines = ""
    if comp.get('subcomponents'):
        composition_lines = "\n# 9. Composition edges\n" + "\n".join(
            f"- `dea:information-system-component-{sc['id']}`: contains (required)"
            for sc in comp['subcomponents']
        )
    else:
        composition_lines = "\n# 9. Composition edges\n- (none; the parent is recorded in the `parent` field)"
    return f"""# {comp['name']}

# 1. Component name and identifier
- Component name: {comp['name']}
- Identifier: `{comp['id']}`

# 2. Definition
{comp.get('description', 'No description provided.')}

# 3. Purpose and scope
This is a P1 component populated by the 02C population exercise (per the 5-CR programme template; the standing rule from 2026-10-18). The P1 tranche covers the most architecturally critical components across the 10 ISCC domains.

# 4. Component type
{comp.get('type', 'IntegrationComponent')}

# 5. F-level assignment
{f_level}

# 6. Component-domain assignment
`{comp.get('domain', '')}`

# 7. Orthogonal classification facets
- Component kind: {comp.get('component_kind', {'ApplicationComponent': 'apc', 'IntegrationComponent': 'igc', 'AIComponent': 'aic'}.get(comp.get('type'), 'apc'))}
- Hosting model: cloud
- Execution characteristics: {('on-demand' if f_level == 'F4' else 'long-running')}
- Component criticality: {comp.get('criticality', 'business-critical')}
- Deployment pattern: replicated
- Security posture: encrypted-at-rest, encrypted-in-transit
- Automation characteristics: {comp.get('automation', 'gitops-automated')}

# 8. Composition (parent, children)
{parent_line}
{children_lines}

# 10. Functional realization (functions realized by this component)
- (populated by 02D; for now, see the metamodel relationship catalogue)

# 11. Cross-references (components related by other metamodel relationships)
- (populated by 02D)

# 12. Hosting and deployment
This component is deployed in the cloud as a replicated service. The deployment is automated through a GitOps pipeline. The hosting model is captured through the orthogonal facet 5.2 (hosting model = cloud).

# 13. Criticality and security posture
Criticality: {comp.get('criticality', 'business-critical')}. All requests and responses are encrypted in transit; persistent state is encrypted at rest. The security posture is captured through the orthogonal facet 5.6.

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
{composition_lines}
"""


def render_subcomponent_readme(f2, f4):
    """Render a 19-section README for a sub-component (F4)."""
    sub_id = f"dea:information-system-component-{f4['id']}"
    return render_readme(
        {'id': sub_id, 'name': f4['name'], 'description': f"A sub-component (F4) of the {f2['name']}. {f4.get('kind', '')}.", 'type': f4.get('type', 'IntegrationComponent'), 'criticality': 'business-critical', 'domain': f4.get('domain', ''), 'automation': f4.get('automation', 'gitops-automated'), 'component_kind': f4.get('component_kind', 'igc')},
        kind='subcomponent',
        parent_id=f2['id'],
        f_level='F4',
    )


def render_f2_with_children(f2):
    """Render the F2 component.yaml with composition children."""
    facets = {
        'component_kind': {'ApplicationComponent': 'apc', 'IntegrationComponent': 'igc', 'AIComponent': 'aic'}[f2['type']],
        'hosting_model': ['cloud'],
        'execution_characteristics': ['long-running'],
        'component_criticality': f2.get('criticality', 'business-critical'),
        'deployment_pattern': ['replicated'],
        'security_posture': ['encrypted-at-rest', 'encrypted-in-transit'],
        'automation_characteristics': f2.get('automation', 'gitops-automated'),
    }
    if f2.get('criticality') == 'mission-critical':
        facets['security_posture'].append('internal-network')
    composition = ""
    if f2.get('subcomponents'):
        composition = "\ncomposition:\n"
        for sc in f2['subcomponents']:
            sub_id = f"dea:information-system-component-{sc['id']}"
            composition += f"  - target: {sub_id}\n    kind: contains\n    cardinality: required\n    version: \"1.0\"\n    effective_date: \"2026-10-18\"\n    status: active\n"
    return f"""id: {f2['id']}
type: {f2['type']}
name: {f2['name']}
status: active
version: "1.0"
effective_date: "2026-10-18"

f_level: {f2['f_level']}

component_domain: {f2.get('domain', '')}

facets:
  component_kind: {facets['component_kind']}
  hosting_model:
{chr(10).join('    - ' + m for m in facets['hosting_model'])}
  execution_characteristics:
{chr(10).join('    - ' + m for m in facets['execution_characteristics'])}
  component_criticality: {facets['component_criticality']}
  deployment_pattern:
{chr(10).join('    - ' + m for m in facets['deployment_pattern'])}
  security_posture:
{chr(10).join('    - ' + m for m in facets['security_posture'])}
  automation_characteristics: {facets['automation_characteristics']}
{composition}
readme: ./README.md
"""


def render_domain_index(domain):
    """Render the domain-level index."""
    return f"""# Domain-level index :  {domain['dir']}
# CR-IS-CAT-02C (2026-10-18). The domain-level index for the
# {domain['name']} domain.

version: 1
effective: 2026-10-18
cr: CR-IS-CAT-02C

domain:
  id: {domain['id']}
  code: {domain['code']}
  name: {domain['name']}

components:
"""


def main():
    written = []
    for domain in P1_DOMAINS:
        domain_dir = ENTITIES / domain['dir']
        domain_dir.mkdir(parents=True, exist_ok=True)

        # Domain index
        index = render_domain_index(domain)
        for f2 in domain['components']:
            f2['domain'] = domain['id']
            comps = []
            comps.append(f"  - id: {f2['id']}\n    name: {f2['name']}\n    f_level: {f2['f_level']}\n    type: {f2['type']}\n    status: active\n    path: components/{f2['id'].split(':')[-1]}/\n")
            for sc in f2.get('subcomponents', []):
                sc['domain'] = domain['id']
                sub_id = f"dea:information-system-component-{sc['id']}"
                comps.append(f"  - id: {sub_id}\n    name: {sc['name']}\n    f_level: F4\n    type: IntegrationComponent\n    status: active\n    path: components/{sub_id.split(':')[-1]}/\n")
        index += ''.join(comps)
        index += "\nchange_history:\n  - version: \"1.0\"\n    date: 2026-10-18\n    cr: CR-IS-CAT-02C\n    note: \"Initial domain-level index for the P1 population.\"\n"
        write_file(domain_dir / 'index.yaml', index)
        written.append(str(domain_dir / 'index.yaml'))

        for f2 in domain['components']:
            f2_dir = domain_dir / 'components' / f2['id'].split(':')[-1]
            f2_dir.mkdir(parents=True, exist_ok=True)

            # F2 component.yaml
            f2_yaml = render_f2_with_children(f2)
            write_file(f2_dir / 'component.yaml', f2_yaml)
            written.append(str(f2_dir / 'component.yaml'))

            # F2 README
            f2_readme = render_readme(
                f2,
                kind='component',
                parent_id=None,
                f_level=f2['f_level'],
            )
            write_file(f2_dir / 'README.md', f2_readme)
            written.append(str(f2_dir / 'README.md'))

            # Sub-components
            for sc in f2.get('subcomponents', []):
                if sc.get('existing'):
                    # Skip the 02B example; already in repo
                    continue
                sc_dir = domain_dir / 'components' / sc['id']
                sc_dir.mkdir(parents=True, exist_ok=True)
                sc_yaml = render_subcomponent_yaml(f2['id'], sc)
                write_file(sc_dir / 'component.yaml', sc_yaml)
                written.append(str(sc_dir / 'component.yaml'))
                sc_readme = render_subcomponent_readme(f2, sc)
                write_file(sc_dir / 'README.md', sc_readme)
                written.append(str(sc_dir / 'README.md'))

    # Update the catalog-level index
    cat_index = REPO / 'entities' / 'v1-alpha' / 'index.yaml'
    cat_index_text = f"""# Catalog-level index :  Information System Component v1-alpha
# CR-IS-CAT-02C (2026-10-18). The catalog-level index aggregates the
# component-domain-level indexes. Per CR-IS-CAT-02A, the catalog-level
# index MUST list the registered component domains and the count of
# component records per domain.

version: 1
effective: 2026-10-18
cr: CR-IS-CAT-02C
parent_cr: CR-IS-CAT-02
cr_02a: CR-IS-CAT-02A
cr_02b: CR-IS-CAT-02B

catalog: dea-catalog-information-system-components
catalog_status: rename-pending-org-admin-transfer

# The list of component domains registered in taxonomy/component-domains.yaml.
# Each entry records the count of component records under that domain.
domains:
"""
    counts = {}
    for domain in P1_DOMAINS:
        n_f2 = len(domain['components'])
        n_f4 = 0
        for f2 in domain['components']:
            n_f4 += sum(1 for sc in f2.get('subcomponents', []) if not sc.get('existing'))
        counts[domain['id']] = n_f2 + n_f4
        cat_index_text += f"  - id: {domain['id']}\n    code: {domain['code']}\n    name: {domain['name']}\n    path: components/{domain['dir']}/\n    status: active\n    component_count: {n_f2 + n_f4}\n"

    total = sum(counts.values())
    cat_index_text += f"""
# Catalog-level counts
total_components: {total}
f_level_distribution:
  F0: 0
  F1: 0
  F2: 5
  F3: 0
  F4: 13
  F5: 0

# Change history
change_history:
  - version: "1.0"
    date: 2026-10-18
    cr: CR-IS-CAT-02C
    note: "Initial catalog-level index after the P1 population. 5 component domains registered; 18 component records (5 F2 + 13 F4). The P2/P3 follow-on populations will further extend the catalog."
"""
    write_file(cat_index, cat_index_text)
    written.append(str(cat_index))

    print(f'Wrote {len(written)} files')
    return written


if __name__ == '__main__':
    main()
