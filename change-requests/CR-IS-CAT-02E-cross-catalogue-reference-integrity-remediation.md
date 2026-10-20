# CR-IS-CAT-02E: Cross-Catalogue Reference Integrity Remediation (ISC)

## Status

Authoritative governance correction to the cross-catalogue references in
`dea-catalog-information-system-components`, mirroring `CR-IS-CAT-01R` in the
function catalogue (ISF).

## 1. Audit finding

The ISC relationship registry (27 records) and its conformance report had the
same false-assurance pattern that `CR-IS-CAT-01R` remediated in the ISF catalogue:

- 5 ISF refs pointed at synthetic ids that did not exist in the ISF catalogue.
  Of those: 4 rebased to canonical ISF ids; 1 declared as forward (to ISF P3).
- 12 forward refs (1 ISS, 4 II, 4 DataEntity, 3 Metric) declared with named
  owning CRs.
- 10 internal ISC refs unchanged.

The pre-existing `reference-integrity.yaml` reported `27/27 sources resolved,
27/27 targets resolved` under prefix-match only; it did not resolve against
the actual target catalogues.

## 2. Rebasing map (4 entries)

| Legacy synthetic id | Canonical ISF id | Rationale |
|---|---|---|
| `dea:information-system-function-data-ingestion` | `dea:information-system-function-data-acquisition` | data-ingestion (verb) = data-acquisition (function). ISF catalogue @ `9faff32`. |
| `dea:information-system-function-data-query` | `dea:information-system-function-data-retrieval` | data-query (verb) = data-retrieval (function). ISF catalogue @ `9faff32`. |
| `dea:information-system-function-order-capture` | `dea:information-system-function-transaction-initiation` | The canonical ISF function for transaction lifecycle entry. ISF catalogue @ `9faff32`. |
| `dea:information-system-function-order-fulfillment` | `dea:information-system-function-transaction-execution` | The canonical ISF function for executing the transaction. ISF catalogue @ `9faff32`. |

## 3. Forward references (13)

| Legacy id | Target repo | Owning CR |
|---|---|---|
| `dea:information-system-function-customer-experience-management` | `dea-catalog-system-functions` | CR-IS-CAT-01C-P3 (ISF P3 population) |
| `dea:information-system-service-api-gateway-service` | `dea-catalog-information-system-services` | CR-IS-CAT-03 (ISS 5-CR programme) |
| `dea:integration-interface-agent-orchestrator-internal` | `dea-catalog-integration-interfaces` | CR-IS-CAT-04 (II 5-CR programme) |
| `dea:integration-interface-api-gateway-public` | `dea-catalog-integration-interfaces` | CR-IS-CAT-04 (II 5-CR programme) |
| `dea:integration-interface-employee-portal-internal` | `dea-catalog-integration-interfaces` | CR-IS-CAT-04 (II 5-CR programme) |
| `dea:integration-interface-identity-broker-public` | `dea-catalog-integration-interfaces` | CR-IS-CAT-04 (II 5-CR programme) |
| `dea:data-entity-order-events` | `dea-catalog-business-objects` | data-entity CR (deferred) |
| `dea:data-entity-partner-transactions` | `dea-catalog-business-objects` | data-entity CR (deferred) |
| `dea:data-entity-model-artifacts` | `dea-catalog-business-objects` | data-entity CR (deferred) |
| `dea:metric-api-gateway-p99-latency` | `dea-catalog-metrics` | metric catalogue CR (deferred) |
| `dea:metric-inference-latency-p99` | `dea-catalog-metrics` | metric catalogue CR (deferred) |
| `dea:metric-observability-data-freshness` | `dea-catalog-metrics` | metric catalogue CR (deferred) |
| (one duplicate `dea:data-entity-order-events` reference in `isc-rel-012`) | (same as above) | (same as above) |

## 4. Hardened validator behaviour

`report_reference_integrity` upgraded to resolve against vendored
target-id snapshots. Three buckets:

- **resolved**: target id exists in a vendored target-id snapshot pinned to
  a specific commit. Includes internal (ISC-local) and external (resolved
  in target repo) refs.
- **forward**: target repo named, target repo exists, target record admitted
  by a named future CR. NOT a failure.
- **unresolved**: target id absent from both local and resolved-target
  snapshots and not declared as forward. Hard-fail in CI.

The vendored snapshot comes from
`docs/is-semantic-architecture/target-id-snapshots.yaml`. CI does not fetch;
deterministic + offline-safe.

## 5. Files

- **Added**: `docs/is-semantic-architecture/cross-catalogue-reference-map.yaml`,
  `docs/is-semantic-architecture/target-id-snapshots.yaml`,
  `change-requests/CR-IS-CAT-02E-cross-catalogue-reference-integrity-remediation.md`
- **Patched**: `relationships/v1-alpha/relationships.yaml` (4 rebases + 13 forward declarations),
  `scripts/generate_conformance_reports.py` (real resolution; 3-bucket report),
  `.github/workflows/validate-catalogue.yml` (Step 3 hard-fail on unresolved)
- **Regenerated**: `reports/reference-integrity.yaml` and the other 4 conformance reports.

## 6. Reference-integrity report (post-PR)

| Bucket | Count |
|---|---:|
| total | 27 |
| resolved | 14 |
| forward | 13 |
| unresolved | 0 |

## 7. Governance basis

- EGV-006 (references resolve to valid entities within the declared identity scope).
- CR-012 (cross-catalogue references resolve to authoritative entities).
- Programme-wide control: evidence before assertion.

## 8. Companion slices (next, not in this CR)

- `CR-IS-CAT-01C-P2` (ISF P2 population) - unblocked by `CR-IS-CAT-01R`. Its 4 of the
  5 ISF forward refs (data-acquisition, data-retrieval, transaction-initiation,
  transaction-execution) are now real records; P2 itself creates the 5th (customer-experience-management).
- `CR-IS-CAT-01C-P3` (ISF P3).
- `CR-IS-CAT-03` (ISS 5-CR programme; resolves 1 remaining forward ref).
- `CR-IS-CAT-04` (II 5-CR programme; resolves 4 forward refs).
- `CR-013 (dea-governance)` - portfolio-level reference-resolution policy.
