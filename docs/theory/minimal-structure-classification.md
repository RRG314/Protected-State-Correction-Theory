# Minimal Structure Classification

## Scope

This document classifies recovery architecture by structural ingredients, not by count/rank/budget slogans alone.

Primary implementation:
- [`src/ocp/next_phase.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/next_phase.py)
- [`data/generated/next-phase/structure_classes.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/structure_classes.csv)
- [`data/generated/next-phase/quantitative_profiles.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/quantitative_profiles.csv)

## Core Invariants

- Alignment defect: `theta_def` (principal-angle defect).
- Inclusion defect: `r_row` (row-space residual).
- Collision severity: `gamma` (collision gap).
- Repair deficiency: `delta` (minimal augmentation count).

These dominate raw rank/count/budget summaries in constrained-observation branches.

## Structural Classes

Current operational class labels:

1. `robust_exact_full_information`
- criteria: exact and full coefficient rank in observation.
- status: `PROVED` in branch class.

2. `aligned_exact_but_fragile`
- criteria: exact but rank-deficient observation geometry.
- status: `PROVED` by perturbation fragility witness.

3. `augmentation_repairable_misaligned`
- criteria: not exact; one or more added directions can restore exactness (`delta>0`).
- status: `PROVED` in restricted-linear design branch (`OCP-045`).

4. `collision_dominated_impossible`
- criteria: impossible with positive collision gap and no unrestricted repair.
- status: `OPEN` under current unrestricted augmentation model (not yet witnessed).

5. `misaligned_impossible`
- criteria: impossible with zero collision-gap separator and no unrestricted repair.
- status: `OPEN` under current unrestricted augmentation model.

## Stronger-Than-Rank Result

### MSC-1: Same-rank split by structure
Status: `PROVED` (`OCP-047`, `OCP-049`).

Same observation rank can map to opposite exactness outcomes; structure invariants (`r_row`, `theta_def`, `gamma`, `delta`) separate them.

### MSC-2: Minimal repair depends on direction, not count only
Status: `PROVED` (`OCP-045`).

Minimal augmentation is a directional row-space completion problem; equal added-row counts can have opposite repair outcomes.

## What Failed

- rank-only classifier: `DISPROVED` (`OCP-049`).
- fixed-library budget-only classifier: `DISPROVED` (`OCP-050`).
- universal class taxonomy across bounded-domain + constrained-observation + generator branches: `OPEN`.

## Design Guidance (Promoted)

For branch-supported design decisions:

1. compute `r_row`, `theta_def`, `gamma`, `delta` first,
2. treat exact rank-deficient cases as fragile unless robustness checks pass,
3. use augmentation direction synthesis, not count-only heuristics,
4. reject rank-only/budget-only confidence claims.

## Novelty Triage

- likely known ingredients: row-space inclusion, principal-angle diagnostics, augmentation as linear completion.
- repo-new package: theorem-ID-coupled structural class diagnostics with executable witnesses and fragility sweeps.
