# Repo Reorganization Final Report

Date: 2026-04-18  
Pass type: GitHub-facing branch-first reorganization

## What changed

### 1) New public branch-first structure

Created `branches/` with canonical landing pages:
- `branches/00-core-ocp/README.md`
- `branches/01-exact-projector-and-sector/README.md`
- `branches/02-generator-and-asymptotic/README.md`
- `branches/03-constrained-observation-and-pvrt/README.md`
- `branches/04-fiber-recoverability-and-no-go/README.md`
- `branches/05-positive-recoverability-and-design/README.md`
- `branches/06-invariants-and-augmentation/README.md`
- `branches/07-cfd-bounded-domain/README.md`
- `branches/08-mhd-closure-and-obstruction/README.md`
- `branches/09-physics-extension/README.md`
- `branches/10-workbench-and-discovery-systems/README.md`
- `branches/README.md`

### 2) Public entry rewrite

- Rewrote root `README.md` to be concise, branch-first, and public-facing.
- Added contribution index: `docs/overview/main-contributions.md`.
- Added papers navigation: `papers/README.md`.

### 3) Internal-process demotion and archive moves

Archived process-heavy research-program docs to:
- `archive/internal-process/docs-research-program/`

Moved one-off output directory:
- `output/` -> `archive/internal-process/output/playwright-output`

Reduced root clutter:
- retired `FILE_INDEX.md`, `ROADMAP.md`, `USEFULNESS_REPORT.md` from active root.
- kept compact root stubs for compatibility:
  - `FINAL_REPORT.md`, `SYSTEM_REPORT.md`, `STATUS.md`, `RESEARCH_MAP.md`
- added minimal legacy pointer notes:
  - `docs/overview/legacy-root/README.md`
  - `archive/internal-process/root-legacy/README.md`

### 4) Reorg decision artifacts added

- `docs/research-program/repo_reorg_inventory.md`
- `docs/research-program/repo_keep_archive_remove_map.md`
- `docs/research-program/branch_navigation_map.md`
- `docs/research-program/branch_consolidation_notes.md`
- `docs/research-program/root_cleanup_notes.md`
- `docs/research-program/outdated_file_resolution_map.md`
- `docs/research-program/internal_doc_cleanup_map.md`
- `docs/research-program/public_contribution_map.md`
- `docs/research-program/physics_placement_map.md`

## Keep/archive/remove summary

### Kept as public core
- Branch landing pages
- Core theorem/no-go/finalization docs
- Canonical papers
- Shared code/tests/scripts/data infrastructure

### Archived/demoted from public-facing navigation
- Integration housekeeping reports
- Intermediate queue/planning pass reports
- Branch status/finalization notes superseded by stronger canonical docs
- One-off output folder
- Redundant process notes

### Kept but de-surfaced
- Provenance/process-heavy folders (e.g., `docs/meta-governance/internal/repo_cleanup/`, paper-production checklists)

## Physics/BH placement outcome

- Quantum lane: retained as narrow, scoped physics extension.
- BH/cosmology lane: retained only as audited noncanonical exploratory material with strict labels.
- No BH/cosmology promotion to OCP core theorem spine.

## Validation checks run

- `python3 scripts/validate/check_links.py` -> passed
- `python3 scripts/validate/check_naming.py` -> passed
- `python3 scripts/validate/check_workbench_static.py` -> passed

## Blunt final check

1. Does the repo now read like a coherent branch-first research repository?  
**Yes.** Public entry now routes directly into branch lanes.

2. Are the strongest committed results clearly visible?  
**Yes.** Core theorem/no-go, recoverability, invariants, CFD, MHD, and workbench are explicit branch entries.

3. Are outdated summaries fixed or demoted?  
**Yes.** Multiple pass/queue/integration docs were archived, and legacy root summaries were replaced by compact compatibility stubs.

4. Are unnecessary internal docs removed from public view?  
**Mostly yes.** Process-heavy items were archived and root clutter was reduced.

5. Is the repo less dump-like and more browsable on GitHub?  
**Yes.** Branch-first navigation substantially reduces report sprawl at entry.

6. Is BH/physics material placed correctly and honestly?  
**Yes.** It is scoped as narrow extension/noncanonical exploratory, not core promotion.

7. Is anything important still scattered?  
**Some deep historical materials remain scattered** in provenance folders by design; branch READMEs now point to canonical current docs.

8. What is the next cleanup step after this reorg?  
Consolidate `docs/meta-governance/internal/repo_cleanup/` and remaining older pass bundles into a single provenance index under `archive/` with stable redirects.
