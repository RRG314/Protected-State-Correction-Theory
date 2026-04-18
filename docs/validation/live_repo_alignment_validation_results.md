# Live Repo Alignment Validation Results

Date: 2026-04-18

## Validation Scope

This validation pass checked:
- public front-door doc integrity,
- link/path integrity,
- workbench/static consistency,
- figure/image asset integrity,
- image-center/figure-index path integrity,
- branch-integration doc wiring.

## Commands and Results

1. `python3 scripts/validate/check_links.py`
   - **PASS** (`markdown link check passed`).

2. `python3 scripts/validate/check_visual_gallery.py`
   - **PASS** (`46 referenced generated files`).

3. `python3 scripts/figures/validate_publication_figures.py`
   - **PASS** (`all_passed: true`, no missing assets).

4. `node --test tests/consistency/*.mjs`
   - **PASS** (`29/29`).

5. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_live_repo_alignment_frontdoor.py -q`
   - **PASS** (`2 passed`).

6. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_descriptor_fiber_branch_integration.py -q`
   - **PASS** (`3 passed`).

7. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_validation_consistency.py -q`
   - **PASS** (`6 passed`).

8. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_visual_gallery_integrity.py -q`
   - **PASS** (`8 passed`).

## Result

Live alignment changes are validated for:
- README/RESEARCH_MAP/STATUS front-door coherence,
- canonical branch naming consistency,
- workbench and figure/image surface integrity,
- image-center (figure-index + visual-gallery + visual-guide) integrity,
- stable test and validation baseline.

## Option D TSIT Follow-Up Validation (2026-04-18)

Additional checks run during TSIT Option D adjacent-lane integration:

1. `python3 scripts/validate/check_links.py`
   - **PASS**
2. `python3 scripts/validate/check_naming.py`
   - **PASS**
3. `python3 scripts/validate/check_visual_gallery.py`
   - **PASS**
4. `python3 scripts/figures/validate_publication_figures.py`
   - **PASS**
5. `python3 scripts/validate/check_workbench_static.py`
   - **PASS**
6. `node --test tests/consistency/*.mjs`
   - **PASS** (`29/29`)
7. `bash scripts/validate/run_all.sh`
   - **PASS** (python + node + pytest suite, including `191 passed` pytest aggregate)

Follow-up conclusion:
- TSIT Option D documentation and artifact wiring did not break links, naming, workbench static integrity, image-center references, or consistency test surfaces.
