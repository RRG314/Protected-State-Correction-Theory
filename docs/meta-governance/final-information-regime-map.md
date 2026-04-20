# Final Information Regime Map

This document records the strongest current map of information behavior in this repository.

Scope discipline:
- no universal scalar law is promoted,
- all statements are class-bounded,
- failures are listed explicitly.

## Arena 1: Static Structure

### S-1 Fiber exactness and restricted-linear compatibility

Setting:
- finite deterministic families and restricted-linear families with declared maps `(A, M, T)`.

Assumptions:
- deterministic records and targets on the declared family.

What works (theorem):
- exact recoverability is equivalent to target constancy on record fibers.
- in restricted-linear form, exactness is equivalent to `ker(OF) subset ker(LF)`.

What fails (no-go):
- amount-only descriptors do not classify exactness in general.

Boundary:
- theorem-grade on finite deterministic and restricted-linear declared classes only.

Evidence:
- `src/ocp/structural_information.py`
- `tests/math/test_structural_information.py`
- `tests/math/test_recoverability.py`
- `data/generated/structural-information-theory/static_regime_checks.csv`

Status:
- `PROVED` (`OCP-030`, `OCP-031`, `OCP-054`, `OCP-062`).

### S-2 Invariance and relaxed-assumption boundary

Setting:
- primitive-object exactness under family reparameterization and target postcomposition.

Assumptions:
- invertible family reparameterization (`Q` invertible) for invariance claim.

What works (theorem):
- exactness verdict is invariant under invertible reparameterization.
- target-side injective postcomposition preserves exactness class on finite support.

What fails (no-go):
- noninvertible reparameterization has no invariance guarantee and can flip verdict.
- noninjective target postcomposition can convert nonexact fine targets into exact coarse targets.

Boundary:
- invariance requires invertibility/injectivity on realized support.

Evidence:
- `data/generated/structural-information-theory/static_regime_checks.csv`
- `tests/math/test_structural_information.py`

Status:
- `PROVED_RESTRICTED` (invertible/injective subclasses), `PROVED` boundary on relaxed assumptions.

## Arena 2: Dynamic Transformations

### D-1 Target-independent garbling class

Setting:
- finite record process with target-independent Markov garbling updates.

Assumptions:
- `P(T,Y_{t+1}) = P(T,Y_t)K`, row-stochastic `K`, no target dependence.

What works (theorem):
- MMSE defect monotonicity survives (binary and finite multivalued cases).

What fails (no-go):
- broad monotonicity claim fails when target dependence is allowed.

Boundary:
- monotonicity is class-dependent, not universal.

Evidence:
- `data/generated/structural-information-theory/dynamic_garbling_law_checks.csv`
- `data/generated/structural-information-theory/dynamic_transform_regime_map.csv`

Status:
- `PROVED` on declared garbling classes (`OCP-055`, `OCP-057`),
- `PROVED` no-go outside class (`OCP-056`).

### D-2 Semigroup, horizons, and convergence

Setting:
- binary target with perfect initial record under repeated BSC degradation.

Assumptions:
- target-independent BSC semigroup, prior `0.5`, `epsilon in [0,0.5]`.

What works (theorem):
- closed-form MMSE envelope,
- explicit horizon threshold law for defect floors below `0.25`,
- monotone convergence to `0.25`.

What fails (no-go):
- closed-form horizon/convergence law does not transfer to arbitrary channel classes.

Boundary:
- branch-limited to the declared BSC semigroup class.

Evidence:
- `data/generated/structural-information-theory/dynamic_horizon_thresholds.csv`
- `data/generated/structural-information-theory/dynamic_transform_regime_map.csv`

Status:
- `PROVED` (`OCP-058`, `OCP-063`).

### Dynamic class table (current)

- target-independent Markov garbling: works.
- target-independent finite multivalued garbling: works.
- BSC target-independent semigroup: works with explicit horizons.
- contractive symmetric Markov subset: works (numerical convergence support).
- target-dependent/adversarial transforms: fails.

## Arena 3: Nonlinear Transformations

### N-1 Record-side nonlinear maps

Setting:
- nonlinear postcomposition of records on finite support.

Assumptions:
- exactness checked before/after post-map.

What works (theorem):
- injective maps on realized record support preserve exactness class.
- verified subclasses include monotone injective maps (`exp`, `cubic`, `tanh` on tested support).

What fails (no-go):
- noninjective maps (`square`, `abs`, saturation clipping) destroy exactness on explicit witnesses.
- quantization has explicit threshold where exactness breaks (`step = 1.5` on current witness support).

Boundary:
- support-level injectivity is the operative condition.

Evidence:
- `data/generated/structural-information-theory/nonlinear_regime_checks.csv`
- `tests/math/test_structural_information.py`

Status:
- `PROVED_RESTRICTED` survive class,
- `PROVED` failure boundary (`OCP-061`-consistent).

### N-2 Target-side nonlinear maps

Setting:
- nonlinear postcomposition on targets with fixed records.

Assumptions:
- finite support target map checks.

What works (theorem):
- injective target mapping preserves exactness equivalence.

What fails (no-go):
- noninjective target coarsening can convert nonexact fine targets into exact coarse targets.

Boundary:
- exactness notion is target-relative.

Evidence:
- `data/generated/structural-information-theory/static_regime_checks.csv`
- `tests/math/test_structural_information.py`

Status:
- `PROVED_RESTRICTED` + `PROVED` boundary.

## Arena 4: Real Data Systems

### E-1 External validity expansion

Setting:
- independent curated datasets integrated into the same structural harness.

Assumptions:
- declared per-lane binary targets and shared descriptor pipeline.

Datasets now integrated:
- UCI Wine Quality
- UCI MAGIC Gamma
- UCI Ionosphere
- UCI Spambase
- UCI Sonar
- UCI Breast Cancer Wisconsin (Diagnostic)

What works (theorem/validated):
- amount-scalar nonreducibility survives on all scored lanes,
- anti-classifier signatures survive on all scored lanes,
- Bayes-risk reduction from augmented profile is positive on all scored lanes.

What fails (explicit failures):
- practical classifier gains are not universal:
  - kNN amount-only outperforms augmented on `information_real_system` and `gravity_recoverability`.
  - nearest-centroid amount-only slightly outperforms augmented on `external_uci_magic_gamma`.

Boundary:
- Bayes-level refinement improvement does not imply universal practical-model improvement.

Evidence:
- `data/generated/structural-information-theory/unified_cross_domain_reduction_metrics.csv`
- `data/generated/structural-information-theory/amount_scalar_nonreducibility.csv`
- `data/generated/structural-information-theory/decision_baseline_comparison.csv`
- `data/generated/structural-information-theory/decision_practical_comparison.csv`
- `data/generated/structural-information-theory/diagnostic_failure_catalog.csv`

Status:
- `VALIDATED` (external-data support), with explicit failure rows retained.

## Strongest Surviving Theorems

1. Exactness by fiber/compatibility (`OCP-030`, `OCP-031`, `OCP-054`).
2. Dynamic monotonicity on target-independent garbling (`OCP-055`, `OCP-057`).
3. BSC semigroup envelope and horizon law (`OCP-058`, `OCP-063`).
4. Amount-code exact-classifier boundary (`OCP-062`).
5. Nonlinear injective/noninjective boundary (`OCP-061`-consistent tested class).

## Strongest No-Go Results

1. No broad dynamic monotonicity outside target-independent class (`OCP-056`).
2. No amount-only exact classifier on mixed amount-code classes (`OCP-062` no-go side).
3. Noninjective representation can destroy exactness (`OCP-061` boundary).
4. Noninvertible reparameterization has no invariance guarantee (explicit witness).

## Remaining Open Problems

1. Universal scalar law (`OCP-009`) remains open and non-promoted.
2. Branch-agnostic dynamic law beyond class assumptions remains open/false in current broad form.
3. Broad nonlinear closure beyond support-level injectivity boundary remains open.
4. Full comparison-of-experiments theorem closure remains open; current decision layer is practical and restricted.

## Final regime verdict

The current map is complete at branch level across static, dynamic, nonlinear, and data arenas for the declared classes.

- Every major behavior has a class-specific survive/fail boundary.
- Every promoted law has executable evidence.
- Every major failure mode is explicit.
- Universal claims remain open rather than inflated.
