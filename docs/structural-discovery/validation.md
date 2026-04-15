# Structural Discovery Validation

## What Is Validated

Python-side validation:

- periodic repair path
- control history repair path
- qubit weaker-versus-stronger split
- boundary architecture repair
- restricted-linear measurement repair
- generated artifact consistency

Workbench-side validation:

- recommendation generation
- before/after regime-change checks
- bounded-domain architecture diagnosis
- benchmark-console integrity
- report and CSV export generation
- regression of the existing recoverability logic

## Core Commands

```bash
PYTHONPATH=src python3 scripts/compare/run_structural_discovery_examples.py
PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_structural_discovery.py tests/examples/test_structural_discovery_examples_consistency.py
node --test tests/consistency/workbench_static.test.mjs
```

## What The Validation Proves

The current Structural Discovery subsystem can:

- detect real structural failures
- identify at least one meaningful repair path on supported families
- distinguish stronger and weaker protected targets where the branch supports that split
- repair the bounded-domain architecture demo rather than only explaining it
- export reproducible scenario snapshots and reports
- survive the full repo validation gate while keeping the live workbench, generated artifacts, and theorem-linked narratives aligned

It does not prove a universal augmentation theorem.

## Current Snapshot

- structural-discovery Python tests: `7 passed`
- workbench / Node suite: `21 passed`
- full repo Python suite: `101 passed`
- full repo Node/workbench suite: `21 passed`
- generated artifacts: structural-discovery summary JSON, demo table CSV, and before/after SVG regenerated successfully
- benchmark console: live in the workbench and exportable
- browser smoke: benchmark console routing, periodic demo routing, and bounded-domain architecture repair passed
