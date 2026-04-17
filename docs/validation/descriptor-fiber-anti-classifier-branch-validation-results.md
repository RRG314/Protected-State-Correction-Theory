# Descriptor-Fiber Anti-Classifier Branch Validation Results

Date: 2026-04-17

## Validation Scope

Validation covered:
- canonical doc wiring,
- branch naming consistency,
- generated descriptor-fiber artifacts,
- workbench/static consistency,
- link/image/figure integrity.

## Commands and Results

1. `python3 scripts/report/compute_descriptor_fiber_invariants.py`
   - pass
   - wrote canonical artifacts:
     - `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.csv`
     - `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json`
   - wrote legacy mirrors for compatibility under `data/generated/meta-theory/`.

2. `python3 scripts/validate/check_links.py`
   - pass (`markdown link check passed`).

3. `python3 scripts/validate/check_visual_gallery.py`
   - pass (`46` referenced generated files).

4. `python3 scripts/figures/validate_publication_figures.py`
   - pass (`all_passed: true`, no missing assets).

5. `node --test tests/consistency/*.mjs`
   - pass (`29/29`).

6. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_descriptor_fiber_branch_integration.py -q`
   - pass (`3 passed`).

7. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_visual_gallery_integrity.py -q`
   - pass (`8 passed`).

8. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_generated_artifact_consistency.py -q`
   - pass (`2 passed`).

9. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_validation_consistency.py -q`
   - pass (`6 passed`).

## Outcome

Branch integration is validated for:
- canonical naming and placement,
- generated quantitative artifacts,
- workbench/static and figure surfaces,
- link/path integrity.
