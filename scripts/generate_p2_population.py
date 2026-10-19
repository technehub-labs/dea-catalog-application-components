#!/usr/bin/env python3
"""
CR-IS-CAT-02C-P2 (2026-10-18). Deterministic generator for the P2
follow-on component population. Produces 3 F2 components and 8 F4
sub-components (11 records total) across 3 P2 component domains.

Per the 5-CR programme template, this is a P2 follow-on to CR-IS-CAT-02C
(P1). The P2 tranche covers the next 3 priority domains after the P1
tranche (5 domains; 19 records).

P2 component domains and components (3 domains, 3 F2 + 8 F4):

ISCC-02 Employee Experience:
  - employee-portal-platform (F2)
    - employee-portal-frontend (F4)
    - employee-portal-bff (F4)

ISCC-03 Partner Integration:
  - partner-portal-platform (F2)
    - partner-portal-onboarding (F4)
    - partner-portal-data-exchange (F4)
    - partner-portal-settlement (F4)

ISCC-08 Observability:
  - observability-platform (F2)
    - metrics-collector (F4)
    - log-aggregator (F4)
    - distributed-tracer (F4)
"""
import os
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
ENTITIES = REPO / 'entities' / 'v1-alpha' / 'components'

# Patch the P1 generator to also generate P2 records
# by appending to the P1_DOMAINS list
import importlib.util
spec = importlib.util.spec_from_file_location("p1gen", str(REPO / 'scripts' / 'generate_p1_population.py'))
p1gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p1gen)

# Add the P2 domains
P2_DOMAINS = [
    {
        'id': 'iscc:domain:employee-experience',
        'code': 'ISCC-02',
        'name': 'Employee Experience',
        'dir': 'employee-experience',
        'add_f2': True,
        'components': [
            {
                'id': 'dea:information-system-component-employee-portal-platform',
                'name': 'Employee Portal Platform',
                'f_level': 'F2',
                'type': 'ApplicationComponent',
                'criticality': 'business-critical',
                'description': 'The composite component that hosts the employee-facing portal: the frontend, the backend-for-frontend, and the single sign-on integration.',
                'subcomponents': [
                    {'id': 'employee-portal-frontend', 'name': 'Employee Portal Frontend', 'kind': 'internal web UI'},
                    {'id': 'employee-portal-bff', 'name': 'Employee Portal Backend-for-Frontend', 'kind': 'API aggregation layer'},
                ],
            },
        ],
    },
    {
        'id': 'iscc:domain:partner-integration',
        'code': 'ISCC-03',
        'name': 'Partner Integration',
        'dir': 'partner-integration',
        'add_f2': True,
        'components': [
            {
                'id': 'dea:information-system-component-partner-portal-platform',
                'name': 'Partner Portal Platform',
                'f_level': 'F2',
                'type': 'ApplicationComponent',
                'criticality': 'business-critical',
                'description': 'The composite component that hosts the B2B partner portal: onboarding, data exchange, and settlement.',
                'subcomponents': [
                    {'id': 'partner-portal-onboarding', 'name': 'Partner Portal Onboarding', 'kind': 'partner self-service onboarding'},
                    {'id': 'partner-portal-data-exchange', 'name': 'Partner Portal Data Exchange', 'kind': 'EDI and B2B gateway'},
                    {'id': 'partner-portal-settlement', 'name': 'Partner Portal Settlement', 'kind': 'partner financial settlement'},
                ],
            },
        ],
    },
    {
        'id': 'iscc:domain:observability',
        'code': 'ISCC-08',
        'name': 'Observability',
        'dir': 'observability',
        'add_f2': True,
        'components': [
            {
                'id': 'dea:information-system-component-observability-platform',
                'name': 'Observability Platform',
                'f_level': 'F2',
                'type': 'ApplicationComponent',
                'criticality': 'operationally-significant',
                'description': 'The composite component that hosts the observability stack: metrics, logs, and traces.',
                'subcomponents': [
                    {'id': 'metrics-collector', 'name': 'Metrics Collector', 'kind': 'time-series metrics aggregation'},
                    {'id': 'log-aggregator', 'name': 'Log Aggregator', 'kind': 'centralized log aggregation'},
                    {'id': 'distributed-tracer', 'name': 'Distributed Tracer', 'kind': 'distributed tracing collector'},
                ],
            },
        ],
    },
]


def main():
    written = []
    for domain in P2_DOMAINS:
        domain_dir = ENTITIES / domain['dir']
        domain_dir.mkdir(parents=True, exist_ok=True)

        # Domain index
        index = p1gen.render_domain_index(domain)
        for f2 in domain['components']:
            f2['domain'] = domain['id']
            comps = []
            comps.append(f"  - id: {f2['id']}\n    name: {f2['name']}\n    f_level: {f2['f_level']}\n    type: {f2['type']}\n    status: active\n    path: components/{f2['id'].split(':')[-1]}/\n")
            for sc in f2.get('subcomponents', []):
                sc['domain'] = domain['id']
                sub_id = f"dea:information-system-component-{sc['id']}"
                comps.append(f"  - id: {sub_id}\n    name: {sc['name']}\n    f_level: F4\n    type: IntegrationComponent\n    status: active\n    path: components/{sub_id.split(':')[-1]}/\n")
        index += ''.join(comps)
        index += "\nchange_history:\n  - version: \"1.0\"\n    date: 2026-10-18\n    cr: CR-IS-CAT-02C-P2\n    note: \"Initial P2 domain-level index. 3 components (1 F2 + 2-3 F4) per domain.\"\n"
        p1gen.write_file(domain_dir / 'index.yaml', index)
        written.append(str(domain_dir / 'index.yaml'))

        for f2 in domain['components']:
            f2_dir = domain_dir / 'components' / f2['id'].split(':')[-1]
            f2_dir.mkdir(parents=True, exist_ok=True)

            f2_yaml = p1gen.render_f2_with_children(f2)
            p1gen.write_file(f2_dir / 'component.yaml', f2_yaml)
            written.append(str(f2_dir / 'component.yaml'))

            f2_readme = p1gen.render_readme(
                f2,
                kind='component',
                parent_id=None,
                f_level=f2['f_level'],
            )
            p1gen.write_file(f2_dir / 'README.md', f2_readme)
            written.append(str(f2_dir / 'README.md'))

            for sc in f2.get('subcomponents', []):
                sc_dir = domain_dir / 'components' / sc['id']
                sc_dir.mkdir(parents=True, exist_ok=True)
                sc_yaml = p1gen.render_subcomponent_yaml(f2['id'], sc)
                p1gen.write_file(sc_dir / 'component.yaml', sc_yaml)
                written.append(str(sc_dir / 'component.yaml'))
                sc_readme = p1gen.render_subcomponent_readme(f2, sc)
                p1gen.write_file(sc_dir / 'README.md', sc_readme)
                written.append(str(sc_dir / 'README.md'))

    # Update the catalog-level index (extend it with the P2 entries)
    cat_index = REPO / 'entities' / 'v1-alpha' / 'index.yaml'
    text = cat_index.read_text()
    # Add the 3 P2 domains to the domains list
    insert_before = "# Catalog-level counts"
    p2_entries = []
    p2_f2 = 0
    p2_f4 = 0
    for domain in P2_DOMAINS:
        n_f2 = len(domain['components'])
        n_f4 = sum(len(f2.get('subcomponents', [])) for f2 in domain['components'])
        p2_f2 += n_f2
        p2_f4 += n_f4
        p2_entries.append(f"  - id: {domain['id']}\n    code: {domain['code']}\n    name: {domain['name']}\n    path: components/{domain['dir']}/\n    status: active\n    component_count: {n_f2 + n_f4}\n")
    p2_block = ''.join(p2_entries)
    text = text.replace(insert_before, p2_block + "\n" + insert_before)
    # Update totals: P1 had 5 F2 + 14 F4 = 19 records; P2 adds 3 F2 + 8 F4 = 11 records; total 30 records
    text = re.sub(r'total_components: \d+', 'total_components: 30', text)
    text = re.sub(r"  F2: \d+", "  F2: 8", text)
    text = re.sub(r"  F4: \d+", "  F4: 22", text)
    # Add a P2 entry to change_history
    text = text.rstrip() + "\n  - version: \"1.1\"\n    date: 2026-10-18\n    cr: CR-IS-CAT-02C-P2\n    note: \"P2 follow-on population. 3 component domains added (ISCC-02, ISCC-03, ISCC-08); 11 new component records (3 F2 + 8 F4). Total catalog: 30 records (8 F2 + 22 F4) across 8 of 10 domains.\"\n"
    cat_index.write_text(text)
    written.append(str(cat_index))

    print(f'Wrote {len(written)} files for P2 population')
    return written


if __name__ == '__main__':
    main()
