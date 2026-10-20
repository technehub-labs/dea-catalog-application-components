# CR-IS-CAT-02F: ISC Forward-Reference Resolution Against the Completed ISF Catalogue

## Status

Forward-reference reconciliation slice for `dea-catalog-application-components`.
Resolves the ISC-side forward declarations that CR-IS-CAT-02E parked against
ISF slices that have since landed, and re-verifies every remaining forward
declaration against its live target repository at a pinned commit.

Companion to `CR-IS-CAT-01C-P3` (ISF P3, PR #10, `2f8685e`) and
`CR-IS-CAT-01C-P1H` (ISF P1 authoring hygiene, PR #11, `635f1ca`).

## 1. Starting state

CR-IS-CAT-02E hardened the ISC conformance validator from prefix-match to
real snapshot-based resolution and declared 13 forward references across 12
distinct legacy ids:

| Target catalogue | Forward refs |
|---|---:|
| `dea-catalog-system-functions` | 1 |
| `dea-catalog-information-system-services` (ISS) | 1 |
| `dea-catalog-integration-interfaces` (II) | 4 |
| `dea-catalog-business-objects` (data entities) | 4 |
| `dea-catalog-metrics` | 3 |
| **Total** | **13** |

Conformance result at CR-IS-CAT-02E: 14 resolved, 13 forward, 0 unresolved.

## 2. What this slice resolves

`isc-rel-001` declared:

```
source: dea:information-system-component-customer-facing-web-application-platform
target: dea:information-system-function-customer-experience-management
owning_cr: CR-IS-CAT-01C-P3 (ISF P3 population)
rationale: "Forward: customer-experience-management lives in ISF-14 Experience
            and Interaction (P3). ISF P3 will admit this record."
```

The declaration predicted that ISF P3 would admit a function with the id
`customer-experience-management`. **It did not.** ISF P3 admitted the ISF-14
Experience and Interaction domain under a different canonical id:

| Level | Canonical ISF id |
|---|---|
| F2 parent | `dea:information-system-function-experience-and-interaction` |
| F4 atomic | `dea:information-system-function-experience-delivery` |
| F4 atomic | `dea:information-system-function-interaction-management` |

`dea:information-system-function-customer-experience-management` was never
admitted and is not a canonical ISF id. Left untouched it would have remained
a permanently unsatisfiable forward reference pointing at an id that does not
exist and never will.

### Resolution

`isc-rel-001` is rebased to `dea:information-system-function-experience-and-interaction`,
the canonical ISF-14 F2 parent.

### Corroboration, not assertion

The rebase is not a unilateral ISC-side assertion. The ISF-14 F2 record lists
`dea:information-system-component-customer-facing-web-application-platform` in
its own `executing_components` field, so the ISF catalogue independently
asserts the same binding. The ISC-side relationship now corroborates a fact the
ISF record already carries.

### Why the F2 parent rather than an F4 atomic

The four pre-existing ISC-side `executes` relationships all target F4 atomics
(`transaction-initiation`, `transaction-execution`, `data-acquisition`,
`data-retrieval`). Targeting an F4 here was considered and rejected:

The legacy id was `customer-experience-management` -- a **domain-scoped
management** concept, not an atomic operation. CR-IS-CAT-02E's own rationale
placed it in ISF-14 as a whole. ISF-14 admits two F4 atomics that both list
this component (`experience-delivery`, `interaction-management`); picking one
would silently narrow the original assertion and drop the other binding. The F2
parent is the record that corresponds to the original domain-scoped intent.

The F4 targets of the other four relationships reflect that those legacy ids
were themselves atomic verbs (`order-capture`, `order-fulfillment`,
`data-ingestion`, `data-query`). Different legacy semantics, correct different
targets.

## 3. Re-verification of the remaining 12 forward references

Every remaining forward declaration was checked against its **live** target
repository at a pinned commit, not assumed.

| Target catalogue | Pinned commit | Live state | Effect |
|---|---|---|---|
| `dea-catalog-information-system-services` | (empty) | repo exists, empty | 1 ref stays forward |
| `dea-catalog-integration-interfaces` | (empty) | repo exists, empty | 4 refs stay forward |
| `dea-catalog-business-objects` | `b752a211a9c1` | scaffold only; 0 data-entity records | 4 refs stay forward |
| `dea-catalog-metrics` | `3e4c72a87785` | **5 metric records admitted**; 0 match the declared targets | 3 refs stay forward |

Two findings worth recording, because both contradict the CR-IS-CAT-02E
snapshot's "empty" claim:

1. **`dea-catalog-metrics` is no longer empty.** It admits 5 metric records:
   `control-effectiveness-rate`, `customer-retention-rate`, `data-completeness`,
   `mean-time-to-recovery`, `operating-margin`. None of the 3 declared ISC-side
   targets (`api-gateway-p99-latency`, `observability-data-freshness`,
   `inference-latency-p99`) matches an admitted id, so all 3 correctly remain
   forward. The snapshot's `declared-empty: true` was factually wrong and is
   corrected.
2. **`dea-catalog-business-objects` is no longer empty.** It exists as a
   scaffold carrying only the catalogue self-id. No data-entity records are
   admitted, so all 4 declared targets correctly remain forward.

Correcting these matters: a snapshot that claims "empty" when a catalogue has
content will mislead the next reviewer into assuming the forward refs are
still trivially pending. The snapshot now records the actual admitted ids so a
future slice can detect the moment a declared target appears.

## 4. Conformance result

| Metric | CR-IS-CAT-02E | CR-IS-CAT-02F |
|---|---:|---:|
| resolved | 14 | **15** |
| forward | 13 | **12** |
| unresolved | 0 | 0 |

Zero unresolved. The ISC catalogue has no unclassified reference.

Reference map counts: 4 rebased, 1 newly resolved, 11 forward (12 distinct
ids across 13 relationships; `isc-rel-011` and `isc-rel-012` share the target
`dea:data-entity-order-events`).

## 5. Files

- **Modified** `relationships/v1-alpha/relationships.yaml`: `isc-rel-001`
  rebased to the canonical ISF-14 F2; provenance `reference_status: forward`
  to `resolved`; `rebased_to`, `resolved_by`, and `target_pinned_commit`
  recorded; note rewritten; CR attribution and change-history updated.
- **Modified** `docs/is-semantic-architecture/cross-catalogue-reference-map.yaml`:
  new `resolved_references` block; the resolved entry removed from
  `forward_references`; new `forward_references_verification` block recording
  the pinned-commit re-verification of all 12 remaining refs; repo pins
  refreshed; counts updated.
- **Modified** `docs/is-semantic-architecture/target-id-snapshots.yaml`: ISF
  pin advanced `9faff32aefae` to `635f1cae2582`; snapshot expanded from 4
  hand-listed ISF ids to all **50** canonical ISF ids (every F2 and F4, with
  decomposition level and source file); the two incorrect `declared-empty`
  claims replaced with the actual admitted id sets.
- **Modified** `scripts/generate_conformance_reports.py`: report version
  2.0 to 2.1, CR attribution to CR-IS-CAT-02F, `supersedes` note.
- **Regenerated** `reports/reference-integrity.yaml` and the other 4 reports.

## 6. Why the snapshot expansion matters

The CR-IS-CAT-02E snapshot hand-listed the 4 ISF ids that ISC happened to
reference at the time. That is a snapshot of *ISC's needs*, not of *ISF's
population*, and it could not detect a new ISF record that satisfied a
forward-declared reference. This slice replaces the hand-list with the full
50-id ISF population, so the next slice that declares a forward reference can
be checked automatically rather than by hand.

## 7. Governance basis

- **EGV-006** references resolve to valid entities within the declared
  identity scope. `isc-rel-001` now resolves against a real ISF record.
- **CR-012** cross-catalogue references resolve to authoritative entities. The
  resolved target is canonical, admitted, and pinned.
- **Evidence before assertion.** The resolution is corroborated by the ISF-14
  F2 record's own `executing_components`, not asserted on the ISC side alone.
  The 12 remaining forward refs were re-verified against live repositories at
  pinned commits rather than assumed still-pending.
- **Explicit disposition.** Every reference in the ISC registry is classified
  resolved, rebased, or forward-declared with a named owning CR. None is
  unclassified. The exception register is correctly empty.
- **No forced completeness.** This slice adds no records, closes no deferred
  children, and reclassifies no reference that lacks a resolution target.

## 8. Remaining programme work

| Forward refs | Owning CR | Admits |
|---:|---|---|
| 1 | `CR-IS-CAT-03` (ISS 5-CR programme) | `dea:information-system-service-api-gateway-service` |
| 4 | `CR-IS-CAT-04` (II 5-CR programme) | 4 `dea:integration-interface-*` ids |
| 4 | data-entity CR (deferred) | 3 distinct `dea:data-entity-*` ids |
| 3 | metric catalogue CR (deferred) | 3 `dea:metric-*` ids |
| **12** | | |

ISF is complete (15/15 domains, 50 records, 0 unresolved) and its ISC-side
forward references are now reconciled. The remaining work is admission work in
four target catalogues, not reconciliation in this one.
