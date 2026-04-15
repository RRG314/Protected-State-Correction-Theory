# Discovery Mixer Developer Reference

## Main Implementation Files

Python engine:
- `src/ocp/discovery_mixer.py`

Workbench engine:
- `docs/workbench/lib/discoveryMixer.js`
- `docs/workbench/app.js`
- `docs/workbench/lib/state.js`

Generated examples:
- `scripts/compare/run_discovery_mixer_examples.py`
- `data/generated/discovery_mixer/`

Tests:
- `tests/math/test_discovery_mixer.py`
- `tests/examples/test_discovery_mixer_examples_consistency.py`
- `tests/consistency/discovery_mixer_static.test.mjs`
- `tests/examples/test_workbench_examples_consistency.py`

## Implementation Model

The mixer uses a typed object-and-report structure.
The Python side provides the richer branch-consistent report objects used for generated artifacts and deeper validation.
The JavaScript side provides the browser-resident equivalent needed for the static workbench.

## Design Rules

- supported families must be explicit
- unsupported reductions must stay explicit
- every promoted recommendation should be traceable to a structural reason
- every testable recommendation should be re-analyzable in the studio
- UI outputs must preserve evidence-level information

## Keeping Python And JS In Sync

The workbench and offline engine will never be identical implementations, but they should agree on:

- regime classification
- root-cause interpretation
- recommendation type
- before/after outcome on tracked demo cases
- export row semantics for saved artifacts

The consistency tests are there to detect divergence early.
