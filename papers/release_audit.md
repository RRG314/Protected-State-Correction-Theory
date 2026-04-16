# Public/Private Release Audit (Publication Sync)

Date: 2026-04-16  
Author: Steven Reid

This audit classifies files for public release across the active paper/research repositories.

## Repo: `Protected-State-Correction-Theory` (OCP)

### A. PUBLIC-READY (include)
- `papers/recoverability_paper_final.md`
- `papers/ocp_core_paper.md`
- `papers/bridge_paper.md`
- `papers/mhd_paper_upgraded.md` (cross-repo synchronized companion copy)
- `papers/recoverability_paper/completeness_checklist.md`
- `papers/recoverability_paper/claim_status_note.md`
- `papers/ocp_core_paper/completeness_checklist.md`
- `papers/ocp_core_paper/positioning_note.md`
- `papers/bridge_paper/completeness_checklist.md`
- `papers/bridge_paper/positioning_note.md`
- `papers/mhd_paper/completeness_checklist.md`
- `papers/mhd_paper/positioning_note.md`
- `papers/style/clean_reference_list.md`
- `scripts/figures/generate_publication_figures.py`
- `scripts/figures/validate_publication_figures.py`
- `scripts/figures/README.md`
- `scripts/validate/validate_paper_references.py`
- `figures/recoverability/*.png`, `figures/recoverability/*.pdf`
- `figures/mhd/*.png`, `figures/mhd/*.pdf`
- `figures/bridge/*.png`, `figures/bridge/*.pdf`
- `data/generated/figures/publication_figure_metrics.json`
- `data/generated/figures/publication_figure_validation.json`
- `data/generated/validations/paper_reference_validation.json`
- `papers/public_reference_map.md`
- `papers/repo_alignment_report.md`
- `papers/push_plan.md`
- `papers/release_audit.md`

### B. INTERNAL-ONLY (exclude)
- Cross-program internal memo files (for example `INTERNAL_CROSS_PROGRAM_ASSESSMENT_2026-04-11.md`)
- Draft-only status notes (for example `papers/drafts/current-draft-status.md`)
- Scratch validation outputs not directly tied to paper reproducibility
- Local app-debug artifacts (`.playwright-cli/*`, `.DS_Store`, temporary logs)
- Investigation-only theorem triage/memo material not intended for public readers

### C. UNCLEAR / REVIEW
- Large theorem-expansion docs produced during exploratory passes under `docs/research-program/` that are mathematically real but not essential to paper release
- New visualization-center docs under `docs/visuals/` beyond the publication figures already integrated into papers

## Repo: `MagnetoHydroDynamic-research` (MHD)

### A. PUBLIC-READY (include)
- `papers/mhd_paper_upgraded.md`
- `figures/mhd/*.png`, `figures/mhd/*.pdf`
- `scripts/figures/generate_mhd_paper_figures.py`
- `scripts/figures/generate_publication_figures.py`
- `scripts/figures/validate_publication_figures.py`
- `scripts/figures/README.md`
- `data/generated/figures/mhd_publication_figure_metrics.json`
- `data/generated/figures/mhd_publication_figure_validation.json`
- `papers/release_audit.md`

### B. INTERNAL-ONLY (exclude)
- Historical PDF drafts under `papers/drafts/`
- Experimental expansion scratch files not tied to paper reproducibility

### C. UNCLEAR / REVIEW
- Expansion-lane theorem docs that may be promoted later as a separate preprint package

## Repo: `cfd-research-program` (CFD)

### A. PUBLIC-READY (include when remote/public target exists)
- `papers/bridge_paper.md`
- `papers/release_audit.md`

### B. INTERNAL-ONLY (exclude)
- Any local-only sync notes created only for cross-repo coordination

### C. UNCLEAR / REVIEW
- Whether this repo should become a public companion for the bridge paper in the current release window.

## Release Safety Decision
- Proceed with public pushes for OCP and MHD only.
- Hold CFD push: no remote configured, so do not cite as a public code host in papers.
