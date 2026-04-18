# Final Architecture

The repository is organized as a branch-first research program with one stable theorem backbone and several scoped extension lanes. The architecture is designed to keep assumptions visible, so each promoted claim can be traced to a declared family and an explicit failure boundary.

The top level has three layers. The foundation layer contains exact projector/sector structure, asymptotic generator structure, and canonical no-go constraints. The branch-strengthening layer develops constrained observation, fiber-based impossibility, augmentation design, invariants, and domain-sensitive PDE branches. The tooling layer exposes these results through workbench and benchmark surfaces without changing claim status.

This architecture is intentionally not a single-law architecture. The same mathematical language is reused across branches, but promotion is branch-limited and evidence-labeled.

## Foundation layer

The foundation combines finite-dimensional exact anchors, continuous asymptotic anchors, and no-go constraints. These provide the default interpretation frame for later branches.

Core references:
- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`
- `papers/ocp_core_paper.md`

## Branch-strengthening layer

The strongest strengthening lanes currently are constrained-observation recoverability, fiber/anti-classifier structure, restricted positive recoverability and augmentation, invariant and context-coherence analysis, bounded-domain CFD behavior, and MHD closure/obstruction analysis. Each lane is useful because it stays explicit about admissible classes and transfer limits.

## Tooling and validation layer

The workbench and discovery systems are operational interfaces for theorem-linked diagnostics, regime comparison, and supported repairs. They are not treated as theorem generators. Tool output is interpreted through the same status map used in the branch docs.

## Architectural nonclaims

The architecture does not assert a universal scalar recoverability law, a universal bounded-domain projector law, or a universal cross-branch invariant replacing fiber/row-space exactness. Those statements are either disproved, unsupported, or still open.

## Final statement

The repository should be read as a disciplined program: stable theorem/no-go backbone first, scoped branch extensions second, and tooling third. The branch boundaries are part of the mathematics, not editorial overhead.
