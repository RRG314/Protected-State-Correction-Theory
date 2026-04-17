# Information Architecture Plan

Date: 2026-04-17

## Problem

The repository is content-rich but feels layered from many passes due to:
- too many competing entry points,
- overlapping overview/report files,
- legacy alias folders,
- inconsistent role labeling.

## Conservative IA Strategy

No destructive restructuring. Instead:
1. define canonical paths,
2. preserve legacy/history content,
3. add role maps and pointer docs,
4. reduce top-level link overload in README.

## IA Decisions

### A. Root Navigation
- `README.md` becomes concise front door.
- Deep navigation moves to:
  - `docs/repo_cleanup/canonical_reading_paths.md`
  - `docs/repo_cleanup/canonical_document_map.md`

### B. Theory Layer
- Canonical final layer:
  - `docs/finalization/*` + `docs/unifying_theory/*`
- Supporting/theorem-development remains in:
  - `docs/theory/*`
  - `docs/fiber-based-recoverability-and-impossibility/*`

### C. Report Layer
- Canonical status/report docs stay visible.
- Dated multi-pass reports remain preserved under `docs/research-program/` and are labeled historical/supporting in maps.

### D. Workbench Layer
- Keep existing app UX and paths unchanged.
- Normalize module naming and link to canonical docs.

### E. References Layer
- Promote a single master map and single canonical bib source.

### F. Legacy Alias Handling
- Keep `docs/soliton_branch/` for compatibility.
- Treat `docs/soliton-branch/` as canonical branch path.

## Implementation Actions (This Pass)

- Added full cleanup/audit doc set in `docs/repo_cleanup/`.
- Rebuilt `README.md` as a clean front door.
- Added canonical reference map + bibliography consistency report.
- Updated terminology and notation unification docs.
- Applied workbench module naming cleanup where labels drifted.
- Added legacy alias pointer doc for `docs/soliton_branch/`.

## Non-Goals (Preserved)

- No deletion of theorem history.
- No workbench redesign.
- No branch-theory rewrites.
