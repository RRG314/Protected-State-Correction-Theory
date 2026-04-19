# Master Validation Report (OCP Discovery Pass)

Date: 2026-04-17

This report records the main reproducibility checks run on the repo and what they show.

## What was executed

Validation checks:
- `scripts/validate/check_links.py`
- `scripts/validate/check_naming.py`
- `scripts/validate/check_visual_gallery.py`
- `scripts/validate/check_workbench_static.py`
- `pytest -q` with `PYTHONPATH=src`

Generation scripts:
- `run_operator_examples.py`
- `run_recoverability_examples.py`
- `run_fiber_recoverability_examples.py`
- `run_decision_layer_examples.py`
- `run_next_phase_examples.py`
- `run_structural_discovery_examples.py`
- `run_discovery_mixer_examples.py`

## Main outcome

- 182 tests passed in this recorded pass.
- Validation checks passed.

## What this means

The core theorem and witness workflows were reproducible on the local test stack used for this pass.

## Adjustments applied during validation

Two tolerance adjustments were made for machine-precision jitter:
- decision-layer residual formatting near zero,
- near-zero principal-angle comparisons.

These changes stabilize reproducibility without changing theorem scope.

## Cross-repo artifact mirror

`data/generated/discovery-portfolio/*` mirrors cross-repo ranking, anomaly, and pattern outputs used in this pass.
