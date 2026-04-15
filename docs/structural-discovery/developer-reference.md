# Structural Discovery Developer Reference

## Main Python Module

- `src/ocp/structural_discovery.py`

Main dataclasses:

- `StructuralFixOption`
- `StructuralComparison`
- `StructuralDiscoveryReport`

Main entry points:

- `discover_linear_template_structure()`
- `discover_periodic_modal_structure()`
- `discover_diagonal_control_structure()`
- `discover_qubit_target_split()`
- `structural_discovery_demo_reports()`

## Main Browser-Side Logic

- `docs/workbench/lib/compute.js`
- `docs/workbench/app.js`
- `docs/workbench/lib/state.js`
- `docs/workbench/styles.css`

## Generated Artifacts

- `data/generated/structural_discovery/structural_discovery_summary.json`
- `data/generated/structural_discovery/structural_discovery_demo_table.csv`
- `docs/assets/structural-discovery/structural-discovery-before-after.svg`

## Validation Hooks

- `tests/math/test_structural_discovery.py`
- `tests/examples/test_structural_discovery_examples_consistency.py`
- `tests/consistency/workbench_static.test.mjs`
- `scripts/validate/run_all.sh`

## Design Notes

The Python module is the reference engine.

The workbench implementation mirrors the reference logic but stays lightweight enough for static-site interaction. If a studio recommendation is theorem-backed or family-backed, the studio should be able to apply and validate it locally. If it is only standard guidance or heuristic, the studio must say so explicitly.

## Maintenance Rule

Do not promote a new structural fix card unless:

1. the fix corresponds to a real branch result or validated family-specific result, and
2. the studio can either apply it or mark it clearly as doc-linked only.
