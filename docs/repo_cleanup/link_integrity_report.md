# Link and Path Integrity Report

Date: 2026-04-17

## Scope

Integrity checks across:
- markdown docs and papers,
- README and overview docs,
- workbench static entry assets,
- visual gallery media references,
- paper URL/DOI references.

## Executed Checks

1. Markdown link integrity
- Command: `python scripts/validate/check_links.py`
- Result: **pass** (`markdown link check passed`)

2. Workbench static asset integrity
- Command: `python scripts/validate/check_workbench_static.py`
- Result: **pass** (`checked docs/workbench/index.html`)

3. Visual gallery integrity
- Command: `python scripts/validate/check_visual_gallery.py`
- Result: **pass** (`46 referenced generated files`)

4. Paper reference URL/DOI integrity
- Command: `python scripts/validate/validate_paper_references.py`
- Result: **pass**
  - papers checked: 4
  - failing URLs: 0
  - failing DOIs: 0

## Fixes in This Pass

- Added missing canonical reference-map docs:
  - `docs/references/master_reference_map.md`
  - `docs/references/bibliography_consistency_report.md`
- Rebuilt README and start-here links around canonical path docs.
- Added legacy-path pointer:
  - `docs/soliton_branch/README.md`

## Outcome

No broken internal markdown paths detected in current repo markdown set, and workbench/visual/reference integrity checks all pass.
