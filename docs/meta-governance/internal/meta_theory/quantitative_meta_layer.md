# Quantitative Meta-Layer Search

Date: 2026-04-17
Pass: Meta-theory extraction

## Objective

Identify quantitative objects above rank/count/budget summaries that add mathematical value and are not just renamed existing branch metrics.

## Q1. Descriptor-Fiber Mixedness (`DFMI`)

`DFMI(a;W) = |{alpha: E_alpha > 0 and F_alpha > 0}| / |im(a)|`.

Interpretation:
- fraction of descriptor values whose fibers contain both exact and fail verdicts.

Status: `PROVED USEFUL` on finite witness classes.

## Q2. Irreducible Descriptor Error Lower Bound (`IDELB`)

`IDELB(a;W) = (sum_alpha min(E_alpha,F_alpha))/|W|`.

Interpretation:
- unavoidable minimum error for any deterministic classifier using descriptor `a` alone.

Status: `PROVED USEFUL` on finite witness classes.

## Q3. Compatibility Lift (`CL`)

`CL(b|a;W)=IDELB(a;W)-IDELB((a,b);W)`.

Interpretation:
- exact quantitative gain from adding compatibility structure to an amount-only descriptor.

Status: `PROVED USEFUL` on supported datasets.

## Q4. Family Fragility Jump (`FFJ`)

For family pair `(A_s, A_l)`, with exactness gaps:
`FFJ = gap(A_l) - gap(A_s)` using branch gap metric.

In current false-positive witnesses:
- `FFJ ~= 2.0` by collision-gap jump (`0 -> 2`) in both enlargement and periodic-refinement examples.

Status: `CONDITIONAL` (metric choice branch-dependent, but signal is stable in current witnesses).

## Q5. Mismatch Amplification Factor (`MAF`)

`MAF = max_error / model_distance` on mismatch stress runs where distance > 0.

Current canonical dataset gives:
- ratios `[1.4142, 1.4142]`, mean `1.4142`.

Status: `CONDITIONAL` (useful canonical benchmark; not yet promoted as a theorem-level universal constant).

## Quantitative outputs generated

Source file:
- `scripts/report/compute_meta_theory_invariants.py`

Generated:
- `data/generated/meta-theory/meta_classifier_invariants.csv`
- `data/generated/meta-theory/meta_classifier_invariants.json`

Summary values:

| Descriptor | DFMI | IDELB | Majority-accuracy upper bound |
| --- | --- | --- | --- |
| `rank_tuple_(n,r,k)` | `1.0` | `0.5` | `0.5` |
| `budget_tuple_(n,r,selection,cost)` | `1.0` | `0.285714...` | `0.714285...` |
| `rank_tuple_plus_rowspace_proxy` | `0.0` | `0.0` | `1.0` |

Derived compatibility gain:
- `CL(rowspace_proxy | rank_tuple) = 0.5`.

## Renaming checks

| Candidate | Renaming check | Decision |
| --- | --- | --- |
| row-space residual score | already existing restricted-linear object | `JUST RENAMING` |
| collision gap alone | already branch quantity | `JUST RENAMING` |
| `DFMI`, `IDELB`, `CL` | new descriptor-fiber quantitative layer over existing witness suites | `PROMOTE` |

## Promotion decision

Promote as a new **quantitative invariant program**:
- `DFMI`,
- `IDELB`,
- `CL`.

Keep `FFJ` and `MAF` as conditional support metrics pending broader branch formalization.
