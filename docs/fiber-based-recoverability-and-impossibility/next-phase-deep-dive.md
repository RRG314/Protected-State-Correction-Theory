# Constrained Observation Deep Dive (Next Phase)

## Lane Definition

- Protected object: target functionals `Lx` on constrained families.
- Disturbance family: nullspace/fiber directions of record map `O`.
- Architecture: restricted-linear observation and decoder with explicit admissible-family scope.

Core sources:
- [`src/ocp/recoverability.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/recoverability.py)
- [`src/ocp/fiber_limits.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/fiber_limits.py)
- [`src/ocp/next_phase.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/next_phase.py)
- [`data/generated/next-phase/quantitative_profiles.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/quantitative_profiles.csv)
- [`data/generated/next-phase/fragility_rank_deficient.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_rank_deficient.csv)

## Starting Anchors

- exactness/fiber anchor: `OCP-030`, `OCP-031`.
- threshold anchor: `OCP-043`.
- minimal augmentation anchor: `OCP-045`.
- stronger-than-rank anchor: `OCP-047`.
- anti-classifier and fragility package: `OCP-049`, `OCP-050`, `OCP-051`, `OCP-052`, `OCP-053`.

## Next-Phase Quantitative Layer In This Lane

Promoted profile tuple:
- `(r_row, theta_def, gamma, delta, ||D||)`.

Interpretation:
- exactness -> `r_row = 0` and `theta_def = 0`,
- fragility severity -> perturbation response of `(r_row, theta_def, gamma)`,
- repair demand -> `delta`,
- noise/mismatch sensitivity -> gap/lower-bound terms and model-mismatch stress.

## Promoted Statements

### CO-NP-1: Exact rank-deficient systems can be maximally fragile
Status: `PROVED` (canonical explicit family).

### CO-NP-2: Same rank and same budget still fail as exact classifiers after quantitative enrichment
Status: `PROVED` (`OCP-049`, `OCP-050`).

### CO-NP-3: Family enlargement and model mismatch produce hard fragility boundaries
Status: `PROVED` (`OCP-052`, `OCP-053`).

### CO-NP-4: Universal scalar recoverability index across all branches
Status: `DISPROVED`.

## Validated Witness Highlights

- canonical fragile exact class fails at `epsilon=1e-4` with positive residual,
- canonical full-rank exact class stays exact over tested perturbation envelope,
- augmentation-repairable non-exact cases show positive `delta` with clear alignment defect.

See:
- [`quantitative_profiles.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/quantitative_profiles.csv)
- [`fragility_rank_deficient.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_rank_deficient.csv)
- [`fragility_full_rank.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_full_rank.csv)

## Literature Positioning

- likely known core math: linear factorization/identifiability and subspace geometry.
- plausibly literature-distinct package: anti-classifier + enlargement-false-positive + canonical mismatch theorem bundle linked to executable diagnostics.

## Next Theorem Targets

1. weighted-cost anti-classifier theorem (extends `OCP-050`),
2. continuity-aware exact factorization stability law,
3. minimal augmentation with directional/structured sensing constraints.
