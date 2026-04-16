# Public Push Plan (Audit-First)

Date: 2026-04-16

This plan stages only public-release files and excludes internal/scratch material.

## Repo 1: `Protected-State-Correction-Theory` (public push planned)

## Include in commit

### Papers
- `papers/recoverability_paper_final.md`
- `papers/ocp_core_paper.md`
- `papers/bridge_paper.md`
- `papers/mhd_paper_upgraded.md`
- `papers/recoverability_paper/completeness_checklist.md`
- `papers/recoverability_paper/claim_status_note.md`
- `papers/ocp_core_paper/completeness_checklist.md`
- `papers/ocp_core_paper/positioning_note.md`
- `papers/bridge_paper/completeness_checklist.md`
- `papers/bridge_paper/positioning_note.md`
- `papers/mhd_paper/completeness_checklist.md`
- `papers/mhd_paper/positioning_note.md`
- `papers/style/clean_reference_list.md`

### Figures + scripts + validation
- `figures/recoverability/*`
- `figures/mhd/*`
- `figures/bridge/*`
- `scripts/figures/generate_publication_figures.py`
- `scripts/figures/validate_publication_figures.py`
- `scripts/figures/README.md`
- `scripts/validate/validate_paper_references.py`
- `data/generated/figures/publication_figure_metrics.json`
- `data/generated/figures/publication_figure_validation.json`
- `data/generated/validations/paper_reference_validation.json`

### Release-audit docs
- `papers/release_audit.md`
- `papers/public_reference_map.md`
- `papers/repo_alignment_report.md`
- `papers/push_plan.md`

## Exclude from commit
- Internal memos and scratch files (for example `INTERNAL_CROSS_PROGRAM_ASSESSMENT_2026-04-11.md`)
- Draft tracker notes (`papers/drafts/current-draft-status.md`)
- Massive unrelated theorem/workbench integration files from previous passes not needed for this publication sync
- Local runtime junk (`.DS_Store`, logs, temporary caches)

## Commit message
- `Finalize paper release package, figures, and public reference alignment`

## Repo 2: `MagnetoHydroDynamic-research` (public push planned)

## Include in commit
- `papers/mhd_paper_upgraded.md`
- `figures/mhd/*`
- `scripts/figures/generate_mhd_paper_figures.py`
- `scripts/figures/generate_publication_figures.py`
- `scripts/figures/validate_publication_figures.py`
- `scripts/figures/README.md`
- `data/generated/figures/mhd_publication_figure_metrics.json`
- `data/generated/figures/mhd_publication_figure_validation.json`
- `papers/release_audit.md`

## Exclude from commit
- Historical draft PDFs under `papers/drafts/`
- Internal expansion artifacts not referenced in the publication package
- Unrelated in-progress theorem expansion files

## Commit message
- `Upgrade MHD publication paper, reproducible figures, and release audit`

## Repo 3: `cfd-research-program` (no public push this pass)

## Current state
- No remote configured; cannot safely push as a public release target.

## Action this pass
- Keep local-only status.
- Do not add public URL references in papers until remote is configured.

## Post-condition checks before pushing

1. `git status --short` shows only intended files staged.
2. `git diff --cached --name-only` matches this push plan.
3. Paper links validated (URL/DOI checks pass).
4. Figure generation/validation artifacts present.
