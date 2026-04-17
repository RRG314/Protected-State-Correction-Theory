# Migration Report

## Purpose

This note records what changed when the local branch was reorganized from **Unified Recoverability and Impossibility** into the clearer **Fiber-Based Recoverability and Impossibility** program.

## What was renamed

Canonical branch-facing name:
- old: `Unified Recoverability and Impossibility`
- new: `Fiber-Based Recoverability and Impossibility`

Local git branch:
- old: `steven/unified-recoverability-and-impossibility`
- new: `steven/fiber-based-recoverability-and-impossibility`

Canonical docs path:
- old: `docs/unified-recoverability-and-impossibility/`
- new: `docs/fiber-based-recoverability-and-impossibility/`

## What was preserved

Preserved without downgrading:
- theorem IDs `OCP-048` through `OCP-051`
- proof-status tags
- generated artifacts under `data/generated/unified-recoverability/`
- tests in `tests/math/test_unified_limits.py`
- artifact consistency tests in `tests/examples/test_unified_recoverability_examples_consistency.py`
- workbench integration through the recoverability / structural-discovery surfaces
- legacy detailed notes in `docs/unified-recoverability-and-impossibility/`
- compatibility code path through `src/ocp/unified_limits.py`
- compatibility script path through `scripts/compare/run_unified_recoverability_examples.py`

## What got clearer

The branch is now organized explicitly around:
- fibers of the record map
- exactness as target constancy on fibers
- impossibility as target mixing inside fibers
- weaker targets as coarsenings that are constant on coarser fibers
- measurement augmentation as fiber refinement
- amount-only failure as failure to capture fiber geometry

## What got stronger

This cleanup pass did not throw away theorems to make the story simpler.
It preserved the existing branch and also carried forward the stronger local results already added on the branch:
- `OCP-050` fixed-library same-budget anti-classifier theorem
- `OCP-051` noisy weaker-versus-stronger separation theorem

## What remains only a reformulation

Clear reformulation, not novelty by itself:
- exact recoverability in fiber language
- impossibility in fiber language
- weaker-versus-stronger targets in fiber language
- detectability/coarsening in fiber language

## What is genuinely stronger after the cleanup

The branch is more defensible now because it states sharply:
- what is universal,
- what is restricted,
- what is benchmark-only,
- and what failed.

That is not just clearer prose.
It is better scope control.

## Canonical migration targets

The new canonical surface is now:
- docs: `docs/fiber-based-recoverability-and-impossibility/`
- code: `src/ocp/fiber_limits.py`
- canonical artifact generator: `scripts/compare/run_fiber_recoverability_examples.py`

The old unified names remain as compatibility shims, not as the primary branch presentation.
