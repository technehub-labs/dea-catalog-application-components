# CR-IS-CAT-02C-P5: Information System Component P5 Atomic Component Population

- **CR**: CR-IS-CAT-02C-P5
- **Date**: 2026-11-12
- **Author**: Emmanuel A. Otchere
- **Status**: Proposed (this PR)
- **Catalog**: dea-catalog-information-system-components (legacy URL: dea-catalog-application-components until org-admin transfer)
- **Parent CRs**: CR-IS-CAT-02C-P4 (vendor-neutral component population; the 141 F2 composite components decomposed here), CR-IS-CAT-01C-P4 in technehub-labs/dea-catalog-system-functions (the 594 executing functions that drive the decomposition)
- **Governance**: G-06 (classification and decomposition are separate structures), G-07 (every active component has machine-readable content plus a README), G-09 (completeness is evidenced, not assumed), G-10 (all generated artefacts are reproducible and validated), G-12 (no implementation-specific component becomes canonical)

## 1. Executive Summary

CR-IS-CAT-02C-P5 populates the first F3 (Atomic Component) level of the ISC catalogue. The P4 tranche (CR-IS-CAT-02C-P4, 2026-11-10) admitted 34 F0 system classes, 63 F1 component groups and 141 F2 composite components, but left every F2 childless: the F0-F5 model in docs/decomposition-guide.md was applied only down to F2. This CR decomposes all 141 P4 F2 composite components into 459 F3 atomic components, using a deterministic, evidence-driven method: the canonical verb-cluster taxonomy of the 594 CR-IS-CAT-01C-P4 function names that P4 allocated to those F2s. Every atom is backed by at least one vendor-neutral function record; every one of the 594 functions is allocated to exactly one atom. The catalog total rises from 276 to 735 records (34 F0, 63 F1, 151 F2, 459 F3, 28 F4), which brings the ISC catalogue into the 500 to 2000 record grounding target of the IS Semantic Architecture programme.

## 2. Selection Methodology

The P5 decomposition is derived, not asserted. Per G-09 the atom inventory is computed from existing evidence in two sibling catalogues, with no discretionary selection:

1. **Function crawl.** Every function record of the CR-IS-CAT-01C-P4 population in technehub-labs/dea-catalog-system-functions declares exactly one executing component. All 594 functions execute on one of the 141 P4 F2 composite components (verified: 594 functions, 141 F2s, zero orphans on both sides; mean 4.2 functions per F2).
2. **Verb extraction.** The leading verb of each of the 594 function names is extracted deterministically (first word, lowercased). The population contains 157 distinct leading verbs.
3. **Canonical clustering.** Each verb maps into one of 15 canonical verb clusters (the taxonomy in section 4). The mapping is total and enumerated: every one of the 157 verbs appears in exactly one cluster list; there is no default branch. Merges follow documented synonym semantics (for example execute, run, perform, re-run, invoke, fire, trigger all denote the execution cluster).
4. **Atom formation.** One F3 atom is emitted per distinct (F2, cluster) pair actually present in the function evidence: the atom executes exactly the functions of that F2 whose leading verb falls into that cluster. The method yields 459 atoms (mean 3.26 per F2; distribution 1 atom on 12 F2s, 2 on 43, 3 on 41, 4 on 16, 5 on 11, 6 on 10, 7 on 6, 8 on 1, 9 on 1). 106 atoms execute two or more functions; the remaining 353 execute exactly one.
5. **Identity.** Atom id = parent F2 id plus the cluster slug (for example dea:information-system-component-card-payment-network-authorization-clearing-settlement-auth-component-execution). Atom name = cluster title plus "Atomic Component" plus the parent F2 name. Type, component_kind and component_domain are inherited from the parent F2. The F2 record and id are unchanged; the atom is attached with a composition edge (kind contains, cardinality required) appended to the F2's composition list, and the F2 README sections 8, 9, 10, 18 and 19 record the decomposition.

The programme plan estimated roughly 370 atoms before the verb evidence was crawled; the realized inventory is 459 because atom count is set by the (F2, cluster) pairs present in the evidence, not by a target. The delta is a measurement outcome, not a scope change.

## 3. P5 Atom Inventory

459 F3 atomic components across 8 of the 10 ISCC domains (the two remaining domains, Observability and AI Native, host no P4 F2 composite components and therefore contribute no atoms; their legacy F2s are out of P5 scope, see section 4):

| Domain | Code | New F3 atoms | Domain total after P5 |
|---|---|---|---|
| Core Operations | ISCC-04 | 250 | 389 |
| Customer Experience | ISCC-01 | 60 | 93 |
| Development Platform | ISCC-09 | 37 | 62 |
| Employee Experience | ISCC-02 | 32 | 51 |
| Integration | ISCC-06 | 28 | 45 |
| Security | ISCC-07 | 22 | 33 |
| Data and Analytics | ISCC-05 | 18 | 31 |
| Partner Integration | ISCC-03 | 12 | 22 |

## 4. The Canonical Verb-Cluster Taxonomy

The taxonomy is a decomposition structure, not a classification structure: per G-06 it assigns functions to atoms within a composite component and is deliberately orthogonal to the ISCC domain taxonomy of CR-IS-CAT-02A. It is recorded in machine-readable form in scripts/p5_component_data.json (verb_clusters map: title, definition, and the enumerated verb list per cluster).

| Cluster | Atoms | Functions | Verbs merged (leading verbs of CR-IS-CAT-01C-P4 names) |
|---|---|---|---|
| execution | 85 | 136 | execute, perform, run, re-run, work, invoke, fire, trigger, initiate, orchestrate, roll, pack, serve |
| administration | 74 | 102 | manage, maintain, administer, configure, self-configure, automate, control, update, adjust, optimize, self-optimize, balance, throttle, plan, schedule, refresh, elect, lock, inject, bind |
| intake-capture | 45 | 68 | process, handle, capture, collect, receive, intake, enter, record, register, import, ingest, upload, bulk, backfill |
| creation-authoring | 46 | 54 | create, generate, produce, author, compose, assemble, originate, document, issue |
| validation-gating | 34 | 38 | validate, verify, check, enforce, gate, qualify, confirm, challenge, authenticate, authorize, scrub |
| routing-delivery | 32 | 34 | route, dispatch, send, deliver, transmit, distribute, refer, exchange, transfer, fulfill, tender, hand, assign, pass |
| analysis-evaluation | 22 | 23 | evaluate, analyze, assess, correlate, reconcile, predict, stratify, rank, suggest, determine |
| integration-transformation | 21 | 23 | integrate, synchronize, sync, federate, replicate, convert, transform, normalize, map, filter, compact, consolidate, decompose, expose, broker |
| calculation-settlement | 20 | 28 | calculate, score, estimate, rate, accrue, bill, charge, settle, payout, disburse, allocate, reserve |
| provisioning-lifecycle | 17 | 20 | provision, deploy, activate, establish, open, close, release, enroll, admit, detach, invite |
| posting-application | 17 | 21 | post, apply, commit |
| detection-observation | 15 | 15 | detect, monitor, track, discover, triage |
| reporting-publication | 12 | 12 | extract, report, publish, surface, emit, manifest, print, aggregate |
| storage-persistence | 11 | 12 | store, persist, archive, index, prune, garbage-collect, restore, back, transition |
| resolution-response | 8 | 8 | resolve, retry, escalate |

Doctrine notes:

- **Scope guard (G-12).** The taxonomy clusters verbs of vendor-neutral function names; no vendor product, protocol brand or implementation is canonical. The atom records assert only the component_kind facet, inherited from the parent; deployment-specific facets remain deferred exactly as in P4.
- **Decomposition vs classification (G-06).** A cluster may appear in components of any ISCC domain; the cluster is not a domain and confers no domain membership. Atom component_domain is inherited unchanged from the parent F2.
- **Legacy F2s.** The 10 legacy F2s of the P1 to P3 populations carry F4 sub-components and execute the legacy CR-IS-CAT-01C F4 function set, not the CR-IS-CAT-01C-P4 population; they are out of P5 scope and remain valid as-is. The 28 legacy F4 sub-components are untouched.
- **Registry.** Composition edges are expressed in component.yaml composition lists, not in relationships/v1-alpha/relationships.yaml: the 02D authorized relationship kinds (executes, provides, depends-on, hosts, consumes, produces, exposes, measured_by) do not include contains. The registry is unchanged by this CR.

## 5. Executing-Function Allocation Crawl

Every atom's README section 10 lists its function records by id and name; every function is listed on exactly one atom. Verification (recorded in docs/coverage-reports/p5-coverage-report.md): 459 atoms, sum of allocated functions 594 of 594, zero unallocated functions, zero functions allocated twice, every function's executing_components entry equals the atom's parent F2 id.

## 6. Repository Deliverables (this PR)

- `scripts/generate_p5_population.py`: the deterministic, idempotent generator (per G-10; three consecutive runs are byte-identical on the full tree).
- `scripts/p5_component_data.json`: the machine-readable atom inventory (verb-cluster taxonomy plus the 459 atoms with their allocated function ids).
- 459 new `entities/v1-alpha/components/<domain>/components/<atom-dir>/component.yaml` records (f_level F3, parent = F2 id).
- 459 new 19-section READMEs (templates/README-template.md conformance).
- 141 updated P4 F2 `component.yaml` records (composition list appended) and READMEs (sections 8, 9, 10, 18, 19 updated).
- 8 updated domain-level `index.yaml` files (P5 rows and change_history 1.2).
- Updated `entities/v1-alpha/index.yaml` (component counts, total_components 276 to 735, F3 count 0 to 459, change_history 1.4).
- Regenerated `reports/` conformance reports (catalogue-conformance 735 records; reference-integrity 15 resolved, 12 forward, 0 unresolved).
- `docs/coverage-reports/p5-coverage-report.md` (this CR's coverage report).
- `CHANGELOG.md` and `change-requests/README.md` index rows.

## 7. CI Requirements

All four existing workflows must pass without modification. Pre-flight verification (local, against the full populated tree):

- validate-entities: YAML parse of 735 component.yaml; v2 schema subset validation; README existence; f_level in F0 to F5; composition kinds in the authorized set; component_domain registered in taxonomy/component-domains.yaml. PASS.
- validate-catalogue: registry parse (27 relationships, unchanged); relationship-kind authorization; cardinality; measured_by metric-target rule; reference-integrity hard check (unresolved_count == 0); conformance report regeneration and idempotency; README 19-section conformance across 735 READMEs. PASS.
- validate-taxonomy: unchanged taxonomy files; domain references of all 735 records resolve. PASS.
- validate-allocation: metamodel-pointer.yaml untouched; pinned OpenDEAM v0.7.0 validation unchanged. PASS.

## 8. Acceptance Criteria

1. 459 F3 atomic records exist, each with a 19-section README and a composition edge from its parent F2.
2. Every P4 function record of CR-IS-CAT-01C-P4 is allocated to exactly one atom; no function is unallocated or double-allocated.
3. Re-running scripts/generate_p5_population.py reproduces the tree byte-identically.
4. All four CI workflows pass on the PR.
5. reference-integrity unresolved_count remains 0.
6. The D-004 / D-005 glyph and punctuation embargo holds over every record, README, script, report and index (no em dash, no en dash, no ellipsis, no triple semicolon).

## 9. Risks and Mitigations

- **Atom granularity drift.** Cluster merges are documented in section 4; a verb reassessment is a follow-on CR that regenerates the inventory deterministically (G-10), not an in-place edit.
- **Readme bulk.** 735 READMEs are machine-checked for 19-section conformance in CI (step 13); the generator emits all of them from one template.
- **Index duplication artifacts.** The pre-existing duplicate domain rows and duplicate change_history entry in entities/v1-alpha/index.yaml (introduced by earlier tranches) are neither consumed by CI nor corrected by this CR; see section 11.

## 10. Definition of Done

All deliverables in section 6 merged to main; all four workflows green on the merge commit; the new main commit SHA recorded for downstream pinning (the ISF P5 tranche pins the ISC main).

## 11. Remaining ISC Work

- CR-IS-CAT-02-IFC (IFC migration; requires an org-admin repo create).
- Deployment-specific facet population (hosting model, criticality, security posture) per-deployment, deferred since P4.
- Cleanup of the pre-existing duplicate rows in the root index (optional hygiene CR; no CI impact).
