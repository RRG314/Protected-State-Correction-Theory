# Internal Document Cleanup Map

Date: 2026-04-18

## Objective

Reduce public-facing exposure of internal AI/process documents while preserving reproducibility and provenance.

## Archived internal-process material (implemented)

Archive destination:
- `archive/internal-process/docs-research-program/`

Archived classes:
1. integration-complete reports,
2. next-phase queue/planning docs,
3. pass-level consolidation housekeeping,
4. branch-specific status/finalization process notes superseded by stronger canonical docs.

Additional archive move:
- `output/` -> `archive/internal-process/output/playwright-output`

## Root declutter actions

- Retired root process files from active navigation:
  - `FILE_INDEX.md`, `ROADMAP.md`, `USEFULNESS_REPORT.md`
- Kept minimal compatibility stubs at root:
  - `FINAL_REPORT.md`, `SYSTEM_REPORT.md`, `STATUS.md`, `RESEARCH_MAP.md`
- Added archival pointer readmes:
  - `docs/overview/legacy-root/README.md`
  - `archive/internal-process/root-legacy/README.md`

## Kept but intentionally de-surfaced

- `docs/repo_cleanup/*`
- `papers/finalization/*`
- `papers/style/*`
- `papers/drafts/*`

These remain for provenance but are no longer front-door navigation targets.

## Public-facing rule after cleanup

Public docs should answer theorem, no-go, branch scope, validation, and reproducibility questions. Internal workflow artifacts should live in archive/provenance zones.
