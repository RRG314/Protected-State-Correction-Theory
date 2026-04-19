# Main Contributions

This page summarizes the strongest current contributions and where they live in the repository.

## Core theorem and no-go spine

The core OCP architecture and its promoted theorem/no-go statements are in `docs/theorem-core/`. The canonical entry files are `architecture-final.md`, `theorem-spine-final.md`, and `no-go-spine-final.md`, with paper-level presentation in `papers/ocp_core_paper.md`.

## Constrained observation and recoverability

The recoverability branch formalizes exactness under constrained records, restricted-linear criteria, and threshold/repair structure. The key docs are `docs/theorem-candidates/constrained-observation-theorems.md`, `docs/theorem-candidates/pvrt-theorem-spine.md`, and `papers/recoverability_paper_final.md`.

## Fiber no-go and anti-classifier structure

The fiber branch provides the cleanest impossibility and opposite-verdict families when amount-only descriptors are held fixed. Canonical documents are under `docs/fiber-based-recoverability-and-impossibility/`, with branch-level synthesis in `papers/descriptor-fiber-anti-classifier-branch.md`.

## Positive recoverability and augmentation design

The restricted positive package is documented in `docs/research-program/positive_class_definitions.md`, `positive_theorem_candidates.md`, `positive_no_go_boundaries.md`, and `positive_recoverability_master_report.md` and is routed through `docs/restricted-results/README.md`.

## Invariant and augmentation program

Current invariant and diagnostic results are organized in `docs/research-program/invariant_*` files, centered on `CID`, `delta_free`, `delta_C`, and descriptor-lift diagnostics. Methods-first routing is in `docs/methods-diagnostics/README.md`.

## CFD and MHD domain branches

The CFD branch separates periodic/Helmholtz exactness from bounded-domain/Hodge limits and repairable subfamilies. The MHD branch develops divergence-cleaning and closure/obstruction structure. Canonical docs live in `docs/cfd/`, `docs/mhd/`, and `papers/mhd_paper_upgraded.md`.

## Workbench and discovery systems

The workbench is a theorem-linked analysis surface. Start with `docs/app/workbench-overview.md`, `docs/app/module-theory-map.md`, and `docs/app/benchmark-validation-console.md`, then use `docs/workbench/index.html` for the interface.

## Physics extensions

Physics notes are branch-limited extensions. Quantum and BH/cosmology materials are kept with explicit status labels in `docs/physics/` and are not promoted to core theorem spine without separate support. The canonical translation lane is `docs/physics-translation/README.md`.
