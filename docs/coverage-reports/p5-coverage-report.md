# P5 Coverage Report (CR-IS-CAT-02C-P5)

- **Date**: 2026-11-12
- **Scope**: F3 atomic component population derived from the CR-IS-CAT-01C-P4 function population of technehub-labs/dea-catalog-system-functions and the CR-IS-CAT-02C-P4 F2 composite components.

## 1. Population methodology

Deterministic verb-cluster decomposition (per G-09, G-10):

1. Crawled all 594 CR-IS-CAT-01C-P4 function records; each declares exactly one executing component, and all 594 execute on one of the 141 P4 F2 composite components (141 of 141 covered, zero orphans both directions).
2. Extracted the leading verb of each function name (157 distinct verbs across the population).
3. Mapped each verb into the 15-cluster canonical taxonomy (see the CR doc section 4 and scripts/p5_component_data.json); the map is total and enumerated with no default branch.
4. Emitted one F3 atom per (F2, cluster) pair present in the evidence; each atom executes exactly the functions of that F2 in that cluster.

## 2. Population summary

| Measure | Value |
|---|---|
| New F3 atomic components | 459 |
| P4 F2 composite components decomposed | 141 of 141 |
| P4 functions allocated | 594 of 594 (each to exactly one atom) |
| Atoms executing 1 function | 353 |
| Atoms executing 2 or more functions | 106 (max 5) |
| Mean atoms per F2 | 3.26 (min 1, max 9) |
| Catalog total after P5 | 735 records (34 F0, 63 F1, 151 F2, 459 F3, 28 F4) |
| Distinct verb clusters exercised | 15 of 15 |

## 3. Cluster to domain mapping

Atom counts by cluster and ISCC domain (rows: clusters; columns: domains; a cluster is a decomposition structure, not a domain, per G-06):

| Cluster | ISCC-01 | ISCC-02 | ISCC-03 | ISCC-04 | ISCC-05 | ISCC-06 | ISCC-07 | ISCC-09 | Total |
|---|---|---|---|---|---|---|---|---|---|
| execution | 15 | 9 | 1 | 50 | 3 | 1 | 1 | 5 | 85 |
| administration | 10 | 8 | 2 | 41 | 3 | 5 | 1 | 4 | 74 |
| creation-authoring | 7 | 2 | 1 | 29 | 0 | 2 | 3 | 2 | 46 |
| intake-capture | 3 | 1 | 2 | 28 | 3 | 4 | 3 | 1 | 45 |
| validation-gating | 5 | 0 | 0 | 16 | 1 | 2 | 4 | 6 | 34 |
| routing-delivery | 6 | 3 | 1 | 14 | 1 | 3 | 1 | 3 | 32 |
| analysis-evaluation | 2 | 2 | 1 | 12 | 1 | 0 | 2 | 2 | 22 |
| integration-transformation | 4 | 1 | 1 | 8 | 1 | 3 | 3 | 0 | 21 |
| calculation-settlement | 3 | 1 | 0 | 14 | 1 | 0 | 0 | 1 | 20 |
| posting-application | 2 | 0 | 0 | 12 | 0 | 2 | 0 | 1 | 17 |
| provisioning-lifecycle | 0 | 1 | 0 | 7 | 1 | 3 | 3 | 2 | 17 |
| detection-observation | 0 | 2 | 1 | 8 | 0 | 2 | 1 | 1 | 15 |
| reporting-publication | 2 | 0 | 1 | 6 | 1 | 0 | 0 | 2 | 12 |
| storage-persistence | 1 | 0 | 0 | 3 | 1 | 1 | 0 | 5 | 11 |
| resolution-response | 0 | 2 | 1 | 2 | 1 | 0 | 0 | 2 | 8 |
| **Total** | **60** | **32** | **12** | **250** | **18** | **28** | **22** | **37** | **459** |

(ISCC-08 Observability and ISCC-10 AI Native host no P4 F2 composite components and contribute no atoms; their legacy F2s are out of P5 scope.)

## 4. Coverage closure

- 141 of 141 P4 F2 composite components decomposed (100 percent).
- 594 of 594 P4 functions allocated to exactly one atom (100 percent, zero unallocated, zero double-allocated).
- Every atom's function list verified against the live ISF records: each listed function's executing_components contains the atom's parent F2 id.
- Every F2 composition list contains exactly its emitted atoms (kind contains, cardinality required).
- Decomposition depth check: maximum chain depth 3 parent hops (F0-F1-F2-F3), acyclic, within the depth budget of docs/decomposition-guide.md.

## 5. Facet coverage

All 459 atoms inherit component_kind from the parent F2: 352 apc, 72 igc, 22 security, 13 data (the aic value is absent because the AI-native domain hosts no P4 F2s). Hosting model, execution characteristics, criticality, deployment pattern, security posture and automation characteristics remain not asserted per the vendor-neutral P4 doctrine; they are populated per-deployment in a follow-on CR.

## 6. Embargo and doctrine hygiene

- The D-004 / D-005 embargo scans passed over every emitted file: glyph scan (em dash, en dash, ellipsis) and punctuation scan (triple semicolon).
- No vendor product, protocol brand or implementation name is canonical in any atom identity or definition (G-12); vendor corroborations remain evidence-only on the parent F2 records.
- The relationship registry is unchanged (composition is not a registry kind per CR-IS-CAT-02D).
- Reference integrity after regeneration: 15 resolved, 12 forward, 0 unresolved (hard check passes).
