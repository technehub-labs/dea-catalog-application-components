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
