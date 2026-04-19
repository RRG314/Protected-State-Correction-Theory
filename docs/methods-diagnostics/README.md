# Methods and Diagnostics

This lane explains how the repo measures recoverability behavior after theorem assumptions are fixed.

These tools are useful when two systems look similar by rank, entropy, or measurement count, but behave differently on exact recovery.

## What this lane contains

- metric definitions with clear semantics,
- harness specifications and ablations,
- method comparisons against amount-only baselines,
- implementation pointers for reproducible runs.

## Core implementation anchors

- `src/ocp/structural_information.py`
- `src/ocp/fiber_limits.py`
- `scripts/research/run_structural_information_harness.py`
- `docs/methods-diagnostics/invariant-lane/`
- `data/generated/structural-information-theory/`

## How to use this lane

1. Pick a declared family and target.
2. Run baseline checks (rank, count, standard descriptors).
3. Run compatibility-oriented diagnostics.
4. Compare whether diagnostics explain opposite-verdict cases that baseline amounts miss.

## Scope boundary

These methods are diagnostics by default. They become theorem claims only when promoted in `docs/restricted-results/` with explicit status.
