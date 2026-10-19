#!/usr/bin/env python3
"""
CR-IS-CAT-02C-P3 (2026-10-18). Deterministic generator for the P3
follow-on component population. Produces 2 F2 components and 6 F4
sub-components (8 records total) across the final 2 P3 component
domains.

Per the 5-CR programme template, this is a P3 follow-on to
CR-IS-CAT-02C (P1) and CR-IS-CAT-02C-P2 (P2). The P3 tranche covers
the last 2 priority domains; after it the ISC catalogue covers 10 of
10 ISCC domains.

P3 component domains and components (2 domains, 2 F2 + 6 F4):

ISCC-09 Development Platform:
  - development-platform (F2)
    - ci-cd-pipeline (F4)
    - artifact-repository (F4)
    - build-service (F4)

ISCC-10 AI Native:
  - ai-inference-platform (F2)
    - model-serving-runtime (F4)
    - model-registry (F4)
    - agent-orchestrator (F4)
"""
import importlib.util
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
ENTITIES = REPO / 'entities' / 'v1-alpha' / 'components'

spec = importlib.util.spec_from_file_location("p1gen", str(REPO / 'scripts' / 'generate_p1_population.py'))
p1gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p1gen)

# Add the P3 domains
P3_DOMAINS = [
    {
        'id': 'iscc:domain:development-platform',
        'code': 'ISCC-09',
        'name': 'Development Platform',
        'dir': 'development-platform',
        'add_f2': True,
        'components': [
            {
                'id': 'dea:information-system-component-development-platform',
                'name': 'Development Platform',
                'f_level': 'F2',
                'type': 'ApplicationComponent',
                'criticality': 'supporting',
                'description': 'The composite component that hosts the software delivery platform: the CI/CD pipeline, the artifact repository, and the build service.',
                'subcomponents': [
                    {'id': 'ci-cd-pipeline', 'name': 'CI/CD Pipeline', 'kind': 'build and deployment automation'},
                    {'id': 'artifact-repository', 'name': 'Artifact Repository', 'kind': 'binary and package storage'},
                    {'id': 'build-service', 'name': 'Build Service', 'kind': 'isolated build execution'},
                ],
            },
        ],
    },
    {
        'id': 'iscc:domain:ai-native',
        'code': 'ISCC-10',
        'name': 'AI Native',
        'dir': 'ai-native',
        'add_f2': True,
        'components': [
            {
                'id': 'dea:information-system-component-ai-inference-platform',
                'name': 'AI Inference Platform',
                'f_level': 'F2',
                'type': 'AIComponent',
                'criticality': 'business-critical',
                'automation': 'agent-orchestrated',
                'description': 'The composite component that hosts the AI-native runtime: model serving, model registry, and agent orchestration.',
                'subcomponents': [
                    {'id': 'model-serving-runtime', 'name': 'Model Serving Runtime', 'kind': 'model inference serving', 'automation': 'agent-orchestrated', 'type': 'AIComponent', 'component_kind': 'aic'},
                    {'id': 'model-registry', 'name': 'Model Registry', 'kind': 'model version and lineage management', 'automation': 'gitops-automated', 'type': 'AIComponent', 'component_kind': 'aic'},
                    {'id': 'agent-orchestrator', 'name': 'Agent Orchestrator', 'kind': 'agentic execution coordination', 'automation': 'agent-orchestrated', 'type': 'AIComponent', 'component_kind': 'aic'},
                ],
            },
        ],
    },
]


def main():
    written = []
    for domain in P3_DOMAINS:
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
        index += "\nchange_history:\n  - version: \"1.0\"\n    date: 2026-10-18\n    cr: CR-IS-CAT-02C-P3\n    note: \"Initial P3 domain-level index. 1 F2 + 3 F4 per domain.\"\n"
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

    # Update the catalog-level index
    cat_index = REPO / 'entities' / 'v1-alpha' / 'index.yaml'
    text = cat_index.read_text()
    insert_before = "# Catalog-level counts"
    p3_entries = []
    p3_f2 = 0
    p3_f4 = 0
    for domain in P3_DOMAINS:
        n_f2 = len(domain['components'])
        n_f4 = sum(len(f2.get('subcomponents', [])) for f2 in domain['components'])
        p3_f2 += n_f2
        p3_f4 += n_f4
        p3_entries.append(f"  - id: {domain['id']}\n    code: {domain['code']}\n    name: {domain['name']}\n    path: components/{domain['dir']}/\n    status: active\n    component_count: {n_f2 + n_f4}\n")
    p3_block = ''.join(p3_entries)
    text = text.replace(insert_before, p3_block + "\n" + insert_before)
    # P1 (19) + P2 (11) + P3 (8) = 38 records; F2: 5+3+2 = 10; F4: 14+8+6 = 28
    text = re.sub(r'total_components: \d+', 'total_components: 38', text)
    text = re.sub(r"  F2: \d+", "  F2: 10", text)
    text = re.sub(r"  F4: \d+", "  F4: 28", text)
    text = text.rstrip() + "\n  - version: \"1.2\"\n    date: 2026-10-18\n    cr: CR-IS-CAT-02C-P3\n    note: \"P3 follow-on population. 2 component domains added (ISCC-09, ISCC-10); 8 new component records (2 F2 + 6 F4). Total catalog: 38 records (10 F2 + 28 F4) across 10 of 10 ISCC domains. The ISC catalogue domain coverage is COMPLETE.\"\n"
    cat_index.write_text(text)
    written.append(str(cat_index))

    print(f'Wrote {len(written)} files for P3 population')
    return written


if __name__ == '__main__':
    main()
