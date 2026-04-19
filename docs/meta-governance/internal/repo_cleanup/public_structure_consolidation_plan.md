# Public Structure Consolidation Plan

Date: 2026-04-17

## Goal

Present one clean main-branch public story without deleting historically important material.

## Public Main-Branch Policy

- Public-facing path should read as one coherent theorem-first program.
- Feature/development branches may exist, but public presentation should center on `main`.
- Canonical docs should be obvious and limited in count.

## Canonical Public Set

### Front door
- `README.md`
- `RESEARCH_MAP.md`
- `STATUS.md`

### Core theorem/status
- `docs/finalization/architecture-final.md`
- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`
- `docs/overview/proof-status-map.md`
- `docs/overview/claim-registry.md`

### Branch-limited integration
- `docs/research-program/branch-audit.md`
- `docs/research-program/usefulness-by-branch.md`
- `docs/research-program/theory-candidate-assessment.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-status.md`

### Workbench
- `docs/workbench/index.html`
- `docs/app/workbench-overview.md`
- `docs/app/module-theory-map.md`
- `docs/app/benchmark-validation-console.md`

### Image/Figure center
- `docs/visuals/figure-index.html`
- `docs/visuals/visual-gallery.html`
- `docs/visuals/visual-guide.md`

### Papers
- `papers/recoverability_paper_final.md`
- `papers/ocp_core_paper.md`
- `papers/bridge_paper.md`
- `papers/mhd_paper_upgraded.md`
- `papers/unifying_theory_framework_final.md`
- `papers/descriptor-fiber-anti-classifier-branch.md`

### Validation and references
- `docs/validation/master_validation_report.md`
- `docs/falsification/FULL_FALSIFICATION_AND_REPAIR_REPORT.md`
- `docs/references/master_reference_map.md`
- `docs/references/protected-state-correction.bib`

## Supporting (Public but Secondary)

- deep branch docs under `docs/fiber-based-recoverability-and-impossibility/`,
- advanced workbench architecture docs,
- detailed validation/falsification subreports,
- system/final large reports.

## Archive/Internal (Demoted from Front Door)

- dated pass bundles under `docs/research-program/*2026-04-16*`,
- exploratory `docs/meta-governance/internal/meta_theory/*` narrative set,
- redundant integration summaries that do not add theorem or validation content beyond canonical docs.

## Reading Paths (Public)

### First-time reader
1. `README.md`
2. `RESEARCH_MAP.md`
3. `docs/overview/start-here.md`
4. finalization spines

### Theorem-first reader
1. finalization spines
2. proof-status map
3. branch audit / branch usefulness

### Workbench-first reader
1. workbench index
2. workbench overview
3. module-theory map
4. benchmark/validation console
5. figure/image center (figure index + visual gallery)

### Paper-first reader
1. recoverability
2. OCP core
3. bridge
4. MHD
5. unifying framework
6. descriptor-fiber branch paper

## Implementation Actions in This Pass

1. Rebuilt `README.md` as concise public front door.
2. Rewrote `RESEARCH_MAP.md` and `STATUS.md` to current branch structure.
3. Added live-repo alignment reports and audits.
4. Kept historical files but removed them from front-door navigation.

## Deferred (Next Push Window)

1. Optional path-level archival relocation for historical pass bundles.
2. Optional curated `archive/index.md` for older reports once link migrations are staged.
