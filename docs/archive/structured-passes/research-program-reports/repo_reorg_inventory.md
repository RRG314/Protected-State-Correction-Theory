# Repo Reorg Inventory

Date: 2026-04-18  
Pass type: GitHub-facing branch-first reorganization

## Current repo surfaces (post-reorg pass)

Top-level code/data infrastructure:
- `src/`
- `tests/`
- `scripts/`
- `data/`

Top-level documentation surfaces:
- `README.md` (public entry)
- `branches/` (new branch-first entry layer)
- `docs/`
- `papers/`
- `archive/`

Supporting technical surfaces:
- `figures/`
- `theory/` (legacy but still referenced by theorem/workbench docs)

## High-density documentation zones

1. `docs/research-program/` — large number of pass reports and branch analyses.
2. `docs/fiber-based-recoverability-and-impossibility/` — deep lane-specific corpus.
3. `docs/meta-governance/internal/repo_cleanup/` — internal cleanup/process-heavy documentation.
4. `papers/` — canonical papers mixed with release/checklist/process notes.

## Canonical branch-support documents identified

Core canonical set used for new branch navigation:
- `docs/finalization/architecture-final.md`
- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`
- `docs/theorem-candidates/*.md` (targeted)
- `docs/impossibility-results/*.md`
- `docs/cfd/*.md`, `docs/mhd/*.md`, `docs/physics/*.md` (scoped)
- `docs/research-program/*master_report*.md` and scoped theorem/no-go/invariant docs
- `papers/ocp_core_paper.md`
- `papers/recoverability_paper_final.md`
- `papers/mhd_paper_upgraded.md`
- `papers/bridge_paper.md`
- `papers/descriptor-fiber-anti-classifier-branch.md`

## Process-heavy / low-value-public files detected

Examples (now archived under `archive/internal-process/docs-research-program/`):
- integration-complete reports
- next-phase queue/audit/final-pass planning notes
- intermediate lens integration reports
- branch finalization/integration status notes superseded by stronger master reports

## Inventory conclusion

The repository had strong committed theorem and branch material, but public navigation was report-heavy and process-heavy. The reorg introduces a branch-first surface and archives selected internal-process reports while retaining shared infrastructure and canonical theorem/paper assets.
