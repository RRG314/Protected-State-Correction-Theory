# Methods and Diagnostics

## Scope

This lane specifies diagnostic tools used after theorem assumptions and admissible families are fixed.

The methods are designed for cases where rank, entropy, or measurement count agree, yet exact-recovery verdicts differ.

## Contents

- metric definitions with explicit semantics,
- harness specifications and ablation protocols,
- method comparisons against amount-only baselines,
- implementation anchors for reproducible runs.

## Core Implementation Anchors

- `src/ocp/structural_information.py`
- `src/ocp/fiber_limits.py`
- `scripts/research/run_structural_information_harness.py`
- `docs/methods-diagnostics/invariant-lane/`
- `data/generated/structural-information-theory/`

## Evaluation Protocol

1. Fix admissible family and target.
2. Compute baseline descriptors (rank, counts, standard summaries).
3. Compute compatibility-oriented diagnostics.
4. Compare diagnostic behavior on opposite-verdict witness pairs.

## Status Boundary

These tools are diagnostics by default. They are theorem claims only when promoted in `docs/restricted-results/` with explicit status.
