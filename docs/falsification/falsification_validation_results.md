# Falsification Validation Results

Date: 2026-04-17

## Commands run

## 1. JS consistency suite

```bash
node --test tests/consistency/*.mjs
```

Initial result:
- failed (`benchmark console exposes validated demos and module-health rows`).

Root cause:
- benchmark module rows did not include required labels expected by consistency tests.

Repair:
- updated `docs/workbench/lib/engine/benchmarkConsole.js` to restore required module labels.

Final result:
- pass (`29 passed, 0 failed`).

## 2. Python math suite

```bash
PYTHONPATH=src .venv/bin/pytest tests/math -q
```

Initial issue:
- import path collection failure when running without `PYTHONPATH=src`.

Final result with correct invocation:
- pass (`153 passed`).

## 3. Python examples suite

```bash
PYTHONPATH=src .venv/bin/pytest tests/examples -q
```

Initial result:
- one failing consistency check requiring professional validation link in README.

Repair:
- added `Professional validation report` link in `README.md`.

Final result:
- pass (`29 passed`).

## 4. Artifact regeneration scripts

Executed:
- `scripts/compare/run_operator_examples.py`
- `scripts/compare/run_recoverability_examples.py`
- `scripts/compare/run_fiber_recoverability_examples.py`
- `scripts/compare/run_design_examples.py`
- `scripts/compare/run_decision_layer_examples.py`
- `scripts/compare/run_next_phase_examples.py`
- `scripts/compare/run_discovery_mixer_examples.py`
- `scripts/compare/run_structural_discovery_examples.py`
- `scripts/compare/run_professional_validation_audit.py`
- `scripts/report/compute_meta_theory_invariants.py`

Result:
- all completed and regenerated expected JSON/CSV/SVG artifacts.

## 5. Link integrity

```bash
python3 scripts/validate/check_links.py
```

Result:
- pass (`markdown link check passed`).

## Open items

- Wolfram symbolic verification not available locally (`wolframscript` absent).
- This pass used Python/SymPy-equivalent pathways only.
