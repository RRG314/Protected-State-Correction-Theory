# Style Normalization Report

Date: 2026-04-18

## Goal

This pass normalized public-facing documentation tone and structure to match the new README style: theorem-first, branch-first, direct prose, explicit scope, and no promotional framing.

## What was rewritten

### Public entry and navigation

The following files were rewritten to establish canonical tone and branch alignment:
- `README.md`
- `branches/README.md`
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

### Core contribution and index surfaces

These files were rewritten to reduce bullet-dump structure and improve branch-linked prose:
- `docs/research-program/README.md`
- `docs/overview/main-contributions.md`
- `papers/README.md`

### Core theorem/no-go architecture

The core formal surfaces were rewritten to use direct explanatory prose while preserving theorem IDs and scope:
- `docs/finalization/architecture-final.md`
- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`

### Workbench and tool explanation surfaces

Workbench docs were rewritten to remove product-style tone and tie modules to theorem/validation structure:
- `docs/app/workbench-overview.md`
- `docs/app/module-theory-map.md`
- `docs/app/benchmark-validation-console.md`
- `docs/app/structural-discovery-studio.md`
- `docs/app/discovery-mixer-structural-composition-lab.md`

### CFD / MHD branch notes

Core CFD and MHD explanation notes were rewritten for consistent branch-limited theorem language:
- `docs/cfd/incompressible-projection.md`
- `docs/cfd/helmholtz-hodge-velocity-projection.md`
- `docs/cfd/bounded-vs-periodic-projection.md`
- `docs/cfd/restricted-flow-recoverability.md`
- `docs/mhd/divergence-cleaning-in-ocp.md`
- `docs/mhd/closure-and-observation-links.md`
- `docs/mhd/glm-and-asymptotic-correction.md`

### Physics extension scope docs

Physics docs were rewritten to keep extension language narrow and status-explicit:
- `docs/physics/quantum_measurement_alignment.md`
- `docs/physics/quantum_measurement_design_lane.md`
- `docs/physics/bh_cosmology_claim_audit.md`
- `docs/physics/bh_cosmology_literature_positioning.md`

### Research-program synthesis docs

The following list-heavy synthesis docs were normalized into cleaner prose:
- `docs/research-program/branch-audit.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md`
- `docs/research-program/positive_recoverability_master_report.md`
- `docs/research-program/invariant_discovery_master_report.md`
- `docs/research-program/context_sensitive_recoverability_master_report.md`

## What was removed or demoted in this pass

No additional file deletions were required for style normalization itself. Demotion/archival actions from the prior reorg remain in effect under `archive/internal-process/` and continue to keep internal process notes out of public-facing navigation.

## What was merged

No file-level merges were executed in this pass. Instead, canonical entry docs were rewritten so overlapping content is routed through branch READMEs and main contribution indices rather than duplicated narrative summaries.

## What was promoted for visibility

The rewrite reinforces these as canonical public surfaces:
- root README branch-first overview
- branch README layer under `branches/`
- `docs/overview/main-contributions.md`
- theorem/no-go spine docs in `docs/finalization/`
- workbench explanation surfaces tied to theorem/validation structure

## Remaining inconsistencies

1. The repository still contains a large long-tail of historical and process-adjacent markdown files (especially under `docs/research-program/`, `discovery/`, and some `docs/app/` audits) that keep older list-heavy style.
2. Some auxiliary paper production files in `papers/finalization/`, `papers/style/`, and `papers/formats/` remain workflow-oriented rather than reader-oriented.
3. Several CSV/JSON-backed discovery reports are intentionally terse and machine-oriented; they were not rewritten as prose documents.

## Recommended next normalization pass

1. Normalize remaining high-traffic docs under `docs/theorem-candidates/` and `docs/impossibility-results/` to the same prose structure.
2. Move remaining low-value pass logs from active doc trees into archive provenance where they are still preserved but not front-facing.
3. Add a lightweight documentation style lint checklist to keep new files aligned with this tone.
