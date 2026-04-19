# Repo Keep / Archive / Remove Map

Date: 2026-04-18

## 1) Keep as public core

- `README.md`
- `branches/*/README.md` (new branch entry layer)
- `docs/finalization/*`
- `docs/theorem-candidates/*`
- `docs/impossibility-results/*`
- `docs/cfd/*`
- `docs/mhd/*`
- `docs/physics/*` (scoped)
- `docs/workbench/*` (public tooling lane)
- `papers/*.md` canonical papers
- `src/`, `tests/`, `scripts/`, `data/`

## 2) Keep but relocate (implemented)

Moved to `archive/internal-process/docs-research-program/`:
- `FULL_INTEGRATION_COMPLETE_REPORT_2026-04-16.md`
- `LENS_INTEGRATION_COMPLETE_REPORT_2026-04-16.md`
- `cross-repo-expansion-2026-04-15.md`
- `deep_continuation_master_report.md`
- `full_system_execution_queue.md`
- `next-phase-audit.md`
- `next-phase-final-report.md`
- `next-phase-paper-lanes.md`
- `ranked-roadmap.md`
- `further-expansion-results.md`
- `integration-audit.md`
- `integration-gap-list.md`
- `lens-integration-map.md`
- `lens-promotion-decisions.md`
- `descriptor-fiber-anti-classifier-branch-finalization-report.md`
- `descriptor-fiber-anti-classifier-branch-integration-report.md`
- `descriptor-fiber-anti-classifier-branch-status.md`
- `tsit-quantitative-extension-finalization-report.md`
- `tsit-quantitative-extension-integration-report.md`
- `tsit-quantitative-extension-status.md`

Moved folder:
- `output/` -> `archive/internal-process/output/playwright-output`

## 3) Keep but remove from public-facing navigation

- `docs/meta-governance/internal/repo_cleanup/*` (retained for provenance, intentionally not front-door)
- legacy pass-specific geometry/soliton folders in `docs/research-program/*2026-04-16*/`
- process/checklist/release scaffolding in `papers/finalization/`, `papers/style/`, `papers/drafts/`

## 4) Merge / consolidate decisions

- Branch public entry moved to `branches/` instead of many report links from root.
- Canonical branch docs now point to strongest current docs/papers; redundant pass logs demoted.
- Physics/BH material consolidated into scoped claim-audit + placement docs.

## 5) Remove from public-facing navigation (not deleted)

- Internal AI-process and integration housekeeping reports.
- queue/planning docs and interim pass summaries.

## 6) Update / rewrite required

- Root `README.md` rewritten branch-first.
- New `docs/overview/main-contributions.md` added as public contribution layer.
- New `papers/README.md` added for paper navigation.
