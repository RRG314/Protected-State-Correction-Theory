# Soliton Branch Validation Scope Note

Date: 2026-04-17

## Validation Inputs Checked

Validated source artifacts:
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/validation/validation_summary.json`
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/recoverability/observation_collision_summary.csv`
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/recoverability/noise_ambiguity_scan.csv`
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/recoverability/observation_collision_witnesses.json`
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/recoverability/same_count_opposite_verdict.json`
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/projection/projection_preservation_summary.csv`
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/projection/integrator_baseline_comparison.csv`

Validation summary check:
- `passed = true`
- `checks_run = 15`

## What Validation Establishes

1. Reproducible finite-family collision taxonomy exists for the tested one-soliton grids.
2. Same-count opposite-verdict witness exists in generated data.
3. Noninjective observation families exhibit persistent ambiguity behavior in the tested noise scans.
4. Projection/reduction class can flip preservation classification on the tested NLS setup.
5. Structure-preserving vs non-preserving integrator drift split is reproducibly measurable.

## What Validation Does Not Establish

1. Continuous-manifold injectivity theorems.
2. Global robustness beyond tested grids and tolerances.
3. Universal nonlinear recoverability laws.
4. Direct transfer of OCP linear minimal-augmentation theorem.

## Validation Scope Verdict

Use current artifacts as `VALIDATED` support for restricted candidate claims only. Do not re-label these as unconditional continuous theorems.
