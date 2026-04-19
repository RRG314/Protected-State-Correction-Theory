# Invariant Theorem Spine (Draft)

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This is a theorem-first draft spine with explicit scope and boundaries.

## Theorem T0 (Core factorization exactness)

Statement:
For target `tau` and record map `M`, exact recoverability holds iff `tau` factors through `M` (equivalently constant on record fibers).

Assumptions:
- deterministic map setting,
- exact (non-noisy) recoverability notion.

Status:
- `PROVED`.

Boundary:
- does not provide stability/noise robustness constants by itself.

## Theorem T1 (Restricted-linear exactness)

Statement:
For linear target `L` and observation `O`, exact recoverability iff `row(L) subset row(O)` (equiv. `ker(O) subset ker(L)`).

Assumptions:
- finite-dimensional linear maps.

Status:
- `PROVED`.

Boundary:
- amount descriptors (rank/count) are necessary but not sufficient for classification.

## Theorem T2 (Conditioned-vs-invariant split existence)

Statement:
There exist supported context families `{M_c}` with:
- `E_cond = 1`,
- `E_inv = 0`.

Assumptions:
- finite context-indexed linear families.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `506` rows with `local_exact_all=1`, `shared_exact=0` in multicontext catalog.

Boundary:
- theorem is existential; global characterization remains open.

## Theorem T3 (CID zero-test equivalence on supported class)

Statement:
`CID(L,{M_c}) = 0` iff shared exactness holds.

Assumptions:
- supported context-indexed linear class,
- Frobenius-norm defect definition.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- zero violations in compact invariant witness run.

Boundary:
- no global robustness constants proved for perturbed/noisy settings.

## Theorem T4 (Positive shared augmentation threshold existence)

Statement:
There exist local-exact/global-fail families requiring strictly positive shared augmentation (`delta_free > 0`) to restore shared exactness.

Assumptions:
- supported finite context-indexed linear class.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- augmentation catalog rows: `506`, with thresholds `1` or `2`.

Boundary:
- closed-form formula for threshold in full generality is open.

## Theorem T5 (Constrained-library no-go via delta_C)

Statement:
In the supported candidate-library setting, `delta_C > 0` implies no exact shared recovery with that full candidate pool.

Assumptions:
- agreement-lift construction and candidate-library feasibility definition in current module.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `14` candidate-library-defect impossibility anomalies.

Boundary:
- broader library classes and nonlinear settings not covered.

## Theorem T6 (Library gain non-sufficiency)

Statement:
Matching free-threshold rank gain is not sufficient for constrained exact recovery; alignment defects can still block exactness.

Assumptions:
- supported candidate-library construction.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `14` `library_gain_not_sufficient` anomalies.

## Theorem T7 (Descriptor-lift ambiguity reduction)

Statement:
On supported descriptor catalogs, amount-only descriptor families have positive irreducible ambiguity, while adding compatibility-lifted information can strictly reduce it (to zero in cataloged cases).

Assumptions:
- finite descriptor-fiber catalogs and IDELB definition.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- rank-only IDELB `0.5` -> lifted IDELB `0.0` in descriptor branch metadata.

Boundary:
- does not imply universal zero ambiguity for all future descriptor constructions.

## Theorem T8 (Fragility existence under stress)

Statement:
Exact systems can lose exactness under target mismatch, enlargement, and perturbation stresses.

Assumptions:
- stress operators implemented in current synthetic suites.

Status:
- `PROVED ON SUPPORTED FAMILY` (existence), `VALIDATED / NUMERICAL ONLY` (rates).

Evidence:
- deep stress catalog includes `115/116` fragility-flagged rows.

## Promotion-ready theorem subset

Most reviewer-safe subset for near-term formal writeup:
1. T0 + T1 (core exactness)
2. T2 + T3 (context split + CID equivalence on supported family)
3. T4 + T5 + T6 (augmentation and constrained-library package)
4. T7 (descriptor-lift anti-classifier improvement)
