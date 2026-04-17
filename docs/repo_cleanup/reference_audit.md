# Reference Audit

Date: 2026-04-17

## Checks Performed

1. Internal markdown links across docs and papers
- Tool: `scripts/validate/check_links.py`
- Result: pass

2. Paper URL and DOI integrity
- Tool: `scripts/validate/validate_paper_references.py`
- Result: pass (`failing_count=0`, `doi_failing_count=0`)

3. Citation metadata consistency
- Reviewed `CITATION.cff`, bibliography files, and paper availability sections.

## Issues Identified and Addressed

- Missing canonical reference map file
  - Added `docs/references/master_reference_map.md`

- Missing bibliography consistency report
  - Added `docs/references/bibliography_consistency_report.md`

- Overlapping references in paper finalization folders
  - Kept all files; canonicalized reference routing through `master_reference_map.md`.

## Current Canonical Citation Stack

- `CITATION.cff`
- `docs/references/how-to-cite-this-work.md`
- `docs/references/protected-state-correction.bib`
- `docs/references/master_reference_map.md`

## Companion URL Handling

Confirmed public references:
- OCP repo and workbench URLs
- soliton companion URL
- MHD companion URL

Conditionally referenced:
- CFD companion remains lane-level companion unless a stable public URL is declared.

## Outcome

Reference and citation layer is now professionalized with:
- canonical map,
- bibliography consistency report,
- validated links/DOIs,
- explicit companion URL discipline.
