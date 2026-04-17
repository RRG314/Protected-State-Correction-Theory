# Soliton Branch Validation Summary

Date: 2026-04-17

## Validation Source

Companion source artifacts:
- `/Users/stevenreid/Documents/New project/repos/soliton-geometry-research/data/generated/validation/validation_summary.json`
- recoverability/projection generated CSV/JSON files under the same directory.

## Verified Metrics

- Validation harness status: `passed = true`.
- Family B injective observation families in scan: `local_complex_2`, `fourier_magnitudes_4`.
- Family B strongest noninjective counts:
  - `global_norms`: `1306368`
  - `local_magnitude_4`: `145152`
  - `moments_center_mass`: `145152`
  - `mixed_local_global`: `145152`
- Same-count witness present: yes (`obs_dim = 4`, opposite verdict).
- Projection split on single-soliton case:
  - `lowpass_k18pct`: `exact_or_near_exact`, manifold distance `0.0072167`
  - `subsample_interp_x8`: `no_go_failure`, manifold distance `0.1718179`

## Baseline Integrator Validation

- split-step drift:
  - mass drift `1.321e-12`
  - Hamiltonian drift `9.508e-12`
- forward Euler drift:
  - mass drift `3.678e-06`
  - Hamiltonian drift `2.047e-04`

Interpretation: branch uses a defensible structure-preserving baseline and a non-preserving comparator.

## Scope Boundary

All values above are validated on declared discrete grids and tested operator classes. They are not continuous universal theorems.
