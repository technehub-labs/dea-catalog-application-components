# Changelog

## [Unreleased]

## [v1.0.0] :  2026-10-18 (CR-IS-CAT-02)

### Changed
- Renamed from `dea-catalog-application-components` to `dea-catalog-information-system-components` (org-admin transfer pending).
- Updated `metamodel-pointer.yaml` to reference `dea:entity-information-system-component` (class alias `ISC`) instead of `dea:entity-application-component` (class alias `APC`).
- Updated the allocation workflow pin from v0.2.1 to v0.7.0 (post-CR-AR-FMWK-04).

### Added
- `change-requests/CR-IS-CAT-02-information-system-components-rename.md` (the CR doc).
- `migrations/legacy-application-component-map.yaml` (the legacy APC/IGC/IFC to ISC migration map).
- `docs/governance.md` (the governance model).
- `docs/is-semantic-architecture/opendeam-identifier-map.yaml` (the local copy of the OpenDEAM-to-metamodel identifier map).
- `CONTRIBUTING.md` (the contributing guide).
- `CHANGELOG.md` (this file).

### Notes
- The legacy APC (Application Component) and IGC (Integration Component) identities are preserved under the legacy identity (EGV-004).
- The IFC (Infrastructure Component) identity stays under `dea:SolutionComponent` per DRIFT-4; the IFC records are migrated to `dea-catalog-infrastructure-components` in a follow-on CR-IS-CAT-02-IFC.
- The 5-CR programme template is the standing rule for the IS catalog cascade (per the user ratification on 2026-10-18).


## CR-IS-CAT-02E (2026-10-19)

- Cross-catalogue reference integrity remediation (ISC).
- 4 synthetic ISF refs rebased (data-ingestion, data-query, order-capture, order-fulfillment).
- 13 forward refs declared (1 ISF-P3, 1 ISS, 4 II, 4 DataEntity, 3 Metric).
- Reference-integrity report upgraded to real resolution: 14 resolved + 13 forward + 0 unresolved.
- CI step 3 hardened: hard-fail on unresolved_count > 0.


## CR-IS-CAT-02F (2026-10-20)

- ISC forward-reference resolution against the completed ISF catalogue.
- `isc-rel-001` rebased: `dea:information-system-function-customer-experience-management` (never admitted, not canonical) to `dea:information-system-function-experience-and-interaction` (canonical ISF-14 F2). Provenance now `resolved`.
- Conformance: 15 resolved / 12 forward / 0 unresolved (was 14 / 13 / 0).
- Re-verified all 12 remaining forward refs against live target repos at pinned commits; all correctly remain forward.
- Corrected two incorrect `declared-empty` snapshot claims: `dea-catalog-metrics` admits 5 metric records, `dea-catalog-business-objects` is scaffolded. Neither contains any declared ISC-side target.
- ISF target snapshot pin advanced `9faff32aefae` to `635f1cae2582`; snapshot expanded from 4 hand-listed ids to all 50 canonical ISF ids.

## CR-IS-CAT-02C-P4 (2026-11-10)

- ISC P4 population: 238 vendor-neutral component records (34 F0 system classes + 63 F1 component groups + 141 F2 composite components) across 8 of 10 ISCC domains.
- F0-F5 model applied per docs/decomposition-guide.md: F0 contains F1, F1 contains F2; composition edges kind=contains, cardinality=required.
- Vendor products are evidence only per G-12; the component_kind facet is asserted (apc/igc/data/security); deployment-specific facets are deferred to per-deployment CRs.
- New scripts/generate_p4_population.py + scripts/p4_component_data.json (deterministic and idempotent; per G-10).
- Total catalog: 276 records. Executed-function crawl: CR-IS-CAT-01C-P4 in the ISF catalogue.


## CR-IS-CAT-02C-P5 (2026-11-12)

- ISC P5 atomic population: 459 F3 atomic component records via the canonical verb-cluster decomposition of the 141 P4 F2 composite components.
- Method: the 594 CR-IS-CAT-01C-P4 function names (157 distinct leading verbs) are mapped into a 15-cluster canonical taxonomy; one atom per (F2, cluster) pair present in the evidence. All 594 functions allocated to exactly one atom.
- The 141 P4 F2 records gain their first composition edges (kind=contains, cardinality=required); the F2 ids and records are otherwise unchanged. The 10 legacy F2s and 28 legacy F4s are untouched.
- New scripts/generate_p5_population.py + scripts/p5_component_data.json (deterministic and idempotent; per G-10).
- The relationship registry is unchanged: composition is not a registry kind (per CR-IS-CAT-02D).
- Total catalog: 735 records (34 F0 + 63 F1 + 151 F2 + 459 F3 + 28 F4). Reference integrity: 15 resolved / 12 forward / 0 unresolved.
