# Structural Discovery Validation

## What Is Validated

Python-side validation:

- demo report generation
- periodic repair path
- control history repair path
- qubit weaker-vs-stronger split
- restricted-linear measurement repair
- generated artifact consistency

Workbench-side validation:

- recommendation generation
- before/after regime-change checks
- regression of the existing recoverability logic

## Core Commands

```bash
PYTHONPATH=src python3 scripts/compare/run_structural_discovery_examples.py
PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_structural_discovery.py tests/examples/test_structural_discovery_examples_consistency.py
node --test tests/consistency/workbench_static.test.mjs
```

## What The Validation Proves

The validation proves that the current Structural Discovery subsystem can:

- detect a real structural failure
- produce at least one meaningful recommendation
- apply a validated recommendation in the supported in-studio lanes
- demonstrate a regime change on the current demo family

It does not prove a universal augmentation theorem.


## Current Snapshot

- structural-discovery Python tests: `6 passed`
- workbench / Node suite: `18 passed`
- full repo validation gate: `100 passed` on the Python suite
- browser smoke: passed across periodic modal repair, control history repair, weaker-vs-stronger qubit split, and restricted-linear repair
- generated artifacts: structural-discovery summary JSON, demo table CSV, and before/after SVG regenerated successfully
