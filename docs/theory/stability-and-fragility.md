# Stability And Fragility Layer

## Scope

This layer tests whether exact recoverability is robust under perturbation, family enlargement, mismatch, and noise. It is falsification-first and branch-scoped.

Primary sources:
- [`src/ocp/next_phase.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/next_phase.py)
- [`src/ocp/fiber_limits.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/fiber_limits.py)
- [`data/generated/next-phase/fragility_rank_deficient.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_rank_deficient.csv)
- [`data/generated/next-phase/fragility_full_rank.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_full_rank.csv)

## Promoted Results

### STAB-1: Arbitrary-small perturbation fragility in rank-deficient exact class
Status: `PROVED` (canonical restricted-linear family).

Setup:
- exact aligned pair with `rank(O)<dim(F)`.
- perturb `O` by `epsilon * E` along a fixed transverse direction.

Observed and verified law:
- exactness fails for every sampled `epsilon>0`.
- residual follows `epsilon / sqrt(1 + epsilon^2)` in the canonical witness.

Evidence:
- math test: [`tests/math/test_next_phase.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/tests/math/test_next_phase.py)
- artifact: [`fragility_rank_deficient.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_rank_deficient.csv)

### STAB-2: Local robustness in full-information exact class
Status: `PROVED` (restricted-linear full-rank class).

If `rank(O)=dim(F)`, exact recoverability persists under sufficiently small perturbations that keep full column rank.

Evidence:
- `first_failure_epsilon = None` on canonical full-rank sweep.
- artifact: [`fragility_full_rank.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_full_rank.csv)

### STAB-3: Family-enlargement false-positive law
Status: `PROVED` (`OCP-052`).

Exactness certified on a small admissible family can fail on an enlarged family even with the same architecture and decoder class.

### STAB-4: Canonical model-mismatch instability law
Status: `PROVED` (`OCP-053`).

A decoder exact for family `F_ref` can incur nonzero unavoidable error on `F_true` with small subspace drift.

### STAB-5: Noisy weak-vs-strong target split
Status: `PROVED` (`OCP-051`, family-scoped).

Weak target can retain bounded error while strong target remains impossible under the same records.

## Results Not Promoted

- Global branch-agnostic Lipschitz stability theorem: `OPEN`.
- One universal perturbation margin invariant valid across bounded-domain and constrained-observation branches: `OPEN`.

## Falsification Ledger

Attempted and rejected broad claims:

- "exact implies stable" -> false (rank-deficient exact class breaks at arbitrarily small perturbation).
- "same rank/budget implies similar fragility" -> false (`OCP-049`, `OCP-050`).
- "small model mismatch always small target error" -> false (`OCP-053` canonical law).

## Literature Positioning

- likely known foundations: perturbation and subspace-angle control ([Kato 1995], [Davis-Kahan 1970]).
- repo-new package: joint exactness/fragility/no-go benchmark harness with reproducible witness artifacts and branch-coupled status labels.

## Next Theorem Targets

1. weighted-cost anti-classifier extension (`OPEN`),
2. quantitative stability envelope that combines mismatch + noise + family drift (`OPEN`),
3. continuity-aware factorization stability theorem (`OPEN`).
