# System Report

## Executive Summary

`RRG314/Protected-State-Correction-Theory` is a theorem-first research program centered on OCP and extended through branch-limited recoverability and impossibility results. The repository is organized to keep three things explicit at all times: what is proved, what is validated only on supported families, and what remains conditional or non-promoted.

The current system class remains `B`: a strong universal core plus branch-limited strengthening, without a universal one-law promotion.

## Repository Role

The repository serves as:

1. the formal home of OCP foundations,
2. the primary home for constrained-observation recoverability and anti-classifier limits,
3. the integration layer for theorem-linked diagnostics and reproducibility tooling,
4. the scope-control layer that distinguishes core claims from companion or conditional material.

It is not a generic cross-domain unification project and not a detached tooling demo.

## Architecture at a Glance

The architecture is deliberately hierarchical.

- Foundation:
  exact projector/sector anchors, continuous asymptotic generator structure, and the core no-go spine.
- Branch-limited strengthening:
  restricted-linear recoverability, fiber-based anti-classifier theorems, descriptor-fiber quantitative extraction, and bounded-domain/CFD obstruction analysis.
- Product surface:
  workbench modules that expose theorem-backed and validated branch behavior with explicit evidence labels.

Canonical architecture docs:
- [Final Architecture](docs/finalization/architecture-final.md)
- [Final Theorem Spine](docs/finalization/theorem-spine-final.md)
- [Final No-Go Spine](docs/finalization/no-go-spine-final.md)

## Strongest Current Branches

### Foundational OCP branch
This branch provides the clean exact and asymptotic anchors and the no-go boundaries that prevent overclaiming.

### Restricted-linear recoverability branch
This branch turns constrained observation into testable exact/approximate/impossible criteria and supports minimal-augmentation design logic.

### Fiber-based anti-classifier branch
This branch captures why amount-only descriptors fail and why family enlargement or model mismatch can produce false confidence.

### Descriptor-fiber quantitative branch
This branch adds finite-class diagnostics (`DFMI`, `IDELB`, `CL`) above anti-classifier witnesses. It is intentionally branch-limited (`PROVED ON SUPPORTED FAMILY` + `VALIDATED`).

### Bounded-domain / CFD-facing obstruction branch
This branch keeps periodic exactness and bounded-domain failure modes in one disciplined lane, with restricted bounded exact subcases where assumptions are explicit.

## Workbench and Image Center

The workbench is maintained as a theorem-linked decision surface. Modules are kept when they map to proved, validated, or explicitly conditional branch results.

Canonical workbench docs:
- [Workbench overview](docs/app/workbench-overview.md)
- [Module-theory map](docs/app/module-theory-map.md)
- [Benchmark / Validation Console](docs/app/benchmark-validation-console.md)

Image/figure center is a first-class supporting surface:
- [Figure Index (image center)](docs/visuals/figure-index.html)
- [Visual Gallery](docs/visuals/visual-gallery.html)
- [Visual Guide](docs/visuals/visual-guide.md)

## Validation and Integrity

Canonical validation surfaces:
- [Master validation report](docs/validation/master_validation_report.md)
- [Professional validation report](docs/app/professional-validation-report.md)
- [Full falsification and repair report](docs/falsification/FULL_FALSIFICATION_AND_REPAIR_REPORT.md)

Recent alignment checks include link integrity, figure existence, workbench/static tests, and branch-map consistency checks.

## Cross-Repo Boundaries

This repository remains the home of record for OCP and its branch-limited recoverability program. Companion repositories are linked where domain-first development belongs elsewhere (for example, soliton and MHD programs).

Canonical boundary docs:
- [Repo scope statement](docs/integration/repo_scope_statement.md)
- [Companion repo map](docs/repo_cleanup/companion_repo_map.md)

## Nonclaims

The repository does not claim:
- a universal amount-only recoverability classifier,
- a universal projection-preservation law,
- a universal physics unification theorem.

## Canonical Entry Points

- [README](README.md)
- [Research Map](RESEARCH_MAP.md)
- [Status](STATUS.md)
- [Canonical reading paths](docs/repo_cleanup/canonical_reading_paths.md)
