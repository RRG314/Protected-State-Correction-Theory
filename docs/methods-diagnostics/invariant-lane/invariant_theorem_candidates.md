# Invariant Theorem Candidates

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

All statements are scoped to supported finite linear/context-indexed families unless stated otherwise.

## T1. Fiber/Factorization Exactness Characterization

Statement:
- Exact recoverability holds iff the target factors through the record map (equivalently target constancy on record fibers).

Status:
- `PROVED`.

Evidence/proof basis:
- Existing core theorem spine and restricted-linear reductions.

## T2. Restricted-Linear Exactness via Row-space Inclusion

Statement:
- For linear maps `(L,O)`, exact recoverability holds iff `row(L)` is contained in `row(O)` (equiv. `ker(O) subset ker(L)`).

Status:
- `PROVED`.

Evidence:
- `src/ocp/recoverability.py`; canonical same-rank counterexamples (`pvrt_same_rank_counterexample.csv`).

## T3. Conditioned-vs-Invariant Split Existence

Statement:
- There exist context families `{M_c}` and target `L` such that each context is individually exact but no shared decoder exists.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `multicontext_witness_catalog.csv`: `506` rows with `local_exact_all=1`, `shared_exact=0`.
- invariant pass: `4` such rows in compact sweep.

## T4. CID Zero-test Equivalence

Statement:
- `CID(L,{M_c}) = 0` iff context-invariant exactness holds.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- Invariant pass: `cid_exact_match_violations = 0` over `32` system rows.

## T5. Positive Shared Augmentation Existence

Statement:
- There exist local-exact/global-fail families with strictly positive minimal shared augmentation threshold.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `augmentation_threshold_catalog.csv`: all `506` rows are local-only and require augmentation; thresholds in `{1,2}`.

## T6. Descriptor-Lift Improvement Theorem Candidate

Statement:
- On supported descriptor catalogs, amount-only descriptors have strictly positive irreducible error lower bound, and adding compatibility lift can reduce that bound to zero.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `meta_classifier_invariants.json`:
  - rank tuple IDELB `0.5`
  - rank+compatibility proxy IDELB `0.0`

## T7. Candidate-Library Defect No-go Threshold

Statement:
- If `delta_C > 0` for a candidate-library class, exact shared recoverability is impossible using that full candidate pool.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `agreement_operator_anomaly_catalog.csv`: `14` `candidate_library_defect_impossibility` anomalies.

## T8. Library-Gain Non-sufficiency

Statement:
- Candidate rank gain matching the free-threshold rank need does not guarantee exact shared recovery.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `agreement_operator_anomaly_catalog.csv`: `14` `library_gain_not_sufficient` anomalies.

## T9. Stress Fragility Existence

Statement:
- Exact systems can be destabilized by target mismatch, family enlargement, or observation perturbation with positive augmentation-cost increase.

Status:
- `PROVED ON SUPPORTED FAMILY` (existence), `VALIDATED / NUMERICAL ONLY` (rates).

Evidence:
- invariant stress catalog: `18/18` flips (`6` per stress type).

## Open theorem targets

1. Closed-form augmentation threshold bounds in terms of context geometry.
- Status: `OPEN`.

2. Stability theorem with explicit `gamma/epsilon` constants for CID and augmentation deficiency.
- Status: `OPEN`.

3. Representation-invariant canonical normalization for CL across mixed branch descriptors.
- Status: `CONDITIONAL`.
