# Full Repository Audit

Date: 2026-04-17
Scope: `ocp-research-program`
Pass type: integration + cleanup + professionalization (non-destructive)

## Method

Audit covered:
- root navigation docs and metadata,
- `docs/` theory/report/workbench/reference layers,
- `papers/` production and supporting files,
- `docs/workbench/` static app links and copy surfaces,
- bibliography and citation metadata.

Checks used:
- markdown path scan (`scripts/validate/check_links.py`),
- paper URL/DOI validation (`scripts/validate/validate_paper_references.py`),
- workbench static asset checks (`scripts/validate/check_workbench_static.py`),
- visual gallery checks (`scripts/validate/check_visual_gallery.py`).

## Inventory Snapshot

- Markdown files in `docs/`: 356
- Markdown files in `papers/`: 33
- Files in `docs/workbench/`: 27
- Major density hotspots:
  - `docs/fiber-based-recoverability-and-impossibility/` (50+ files)
  - `docs/research-program/` (multi-pass report accumulation)
  - `docs/unifying_theory/` (new canonical theory layer)

## High-Impact Findings

1. Entry path overload
- README had too many equal-priority links, which obscured the canonical path.

2. Duplicate namespace risk
- Both `docs/soliton-branch/` and `docs/soliton_branch/` exist with overlapping purposes.
- Decision: keep both paths for compatibility; treat `docs/soliton-branch/` as canonical.

3. Reference-map gap
- `docs/references/master_reference_map.md` and `docs/references/bibliography_consistency_report.md` were missing despite being needed by the repo’s publication workflow.

4. Multi-pass layering without role labels
- Several report families were useful but unlabeled as canonical/supporting/historical/internal.
- Result was trust friction and navigation ambiguity.

5. Workbench-doc integration mostly strong
- Core static workbench paths and linked module docs are present.
- Needs clearer canonical mapping and copy consistency notes, not UI redesign.

## Canonical Classification (Important Files)

### Canonical
- `README.md`
- `docs/overview/start-here.md`
- `docs/overview/proof-status-map.md`
- `docs/finalization/architecture-final.md`
- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`
- `docs/unifying_theory/final_theory_identity.md`
- `docs/unifying_theory/theorem_hierarchy_final.md`
- `docs/unifying_theory/final_universal_core_theorems.md`
- `docs/unifying_theory/branch_limited_strengthening_final.md`
- `docs/unifying_theory/final_theory_refinement_master_report.md`
- `papers/unifying_theory_framework_final.md`
- `papers/recoverability_paper_final.md`
- `papers/ocp_core_paper.md`
- `papers/bridge_paper.md`
- `papers/mhd_paper_upgraded.md`
- `docs/workbench/index.html`
- `docs/app/workbench-overview.md`
- `docs/references/how-to-cite-this-work.md`
- `docs/references/protected-state-correction.bib`

### Supporting
- `SYSTEM_REPORT.md`
- `FINAL_REPORT.md`
- `USEFULNESS_REPORT.md`
- `docs/app/tool-qualification-report.md`
- `docs/app/professional-validation-report.md`
- `docs/app/module-theory-map.md`
- `docs/discovery-mixer/*`
- `docs/structural-discovery/*`
- `docs/fiber-based-recoverability-and-impossibility/*`
- `docs/theory/advanced-directions/*`

### Archival But Keep
- `docs/research-program/geometry-pass-2026-04-16/*`
- `docs/research-program/soliton-geometry-discovery-2026-04-16/*`
- `docs/research-program/FULL_INTEGRATION_COMPLETE_REPORT_2026-04-16.md`
- `docs/research-program/LENS_INTEGRATION_COMPLETE_REPORT_2026-04-16.md`
- `docs/research-program/GEOMETRY_FINDINGS_FOR_REPO_2026-04-16.md`

### Redirect Needed (Compatibility Label)
- `docs/soliton_branch/*` (legacy alias path)
  - canonical set: `docs/soliton-branch/*`

### Merge Needed (Semantic, Not Deletion)
- Thematic overlap across:
  - `docs/research-program/*` status reports,
  - `docs/unifying_theory/*` final theory package,
  - top-level summary docs.
- Action: preserve all files; add canonical map and reading-path guidance to reduce conflict.

### Outdated But Historically Important
- Older transition reports and migration memos in `docs/fiber-based-recoverability-and-impossibility/` and `docs/research-program/`.
- Keep for provenance with “historical/supporting” role labels in map docs.

### Delete Only If Disposable (Very Rare)
- No theorem/proof/report file was marked for deletion in this pass.
- Candidate disposable files are limited to transient OS artifacts (e.g., `.DS_Store`) and temporary generated scratch output not used by docs/tests.

## Cleanup Decision Summary

- Preserve theorem/proof and branch history.
- Promote a strict canonical reading and document map.
- Relabel overlapping material rather than removing it.
- Normalize references/metadata/terminology.
- Keep workbench UX recognizable; only correctness/consistency updates.
