# Root Cleanup Notes

Date: 2026-04-18

## Root cleanup goals

- Make root GitHub-readable.
- Keep only high-value public entry items visible.
- Remove process-heavy outputs from top-level navigation.

## Implemented

1. Added `branches/` as branch-first top-level navigation surface.
2. Rewrote `README.md` to branch-first public entry.
3. Moved one-off output directory:
   - `output/` -> `archive/internal-process/output/playwright-output`
4. Archived selected process-heavy research-program reports under:
   - `archive/internal-process/docs-research-program/`
5. Reduced root legacy clutter:
   - retired root legacy process files from active tree:
     - `FILE_INDEX.md`, `ROADMAP.md`, `USEFULNESS_REPORT.md`
   - kept compact compatibility stubs at root for:
     - `FINAL_REPORT.md`, `SYSTEM_REPORT.md`, `STATUS.md`, `RESEARCH_MAP.md`
   - added minimal archival pointers:
     - `docs/overview/legacy-root/README.md`
     - `archive/internal-process/root-legacy/README.md`

## Kept at root (intentional)

- Licensing/community metadata: `LICENSE`, `CITATION.cff`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `CHANGELOG.md`.
- Minimal compatibility stubs for legacy root report names used by scripts/tooling:
  - `FINAL_REPORT.md`, `SYSTEM_REPORT.md`, `STATUS.md`, `RESEARCH_MAP.md`.

## Public navigation effect

External readers now enter through:
- `README.md`
- `branches/`
- `docs/overview/main-contributions.md`

rather than through process-heavy root reports.
