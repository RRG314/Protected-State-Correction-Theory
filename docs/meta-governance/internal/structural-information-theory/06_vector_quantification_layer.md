# Vector Quantification Layer (No Universal Scalar)

Date: 2026-04-19

## Why vector-valued

Amount-only scalars are not exact classifiers on declared witness classes (`OCP-049`, `OCP-050`).
Therefore quantification is represented as a profile vector, not a single universal scalar.

## Proposed profile coordinates

For a declared dataset/lane and binary success label:
- amount coordinates: `(H, I_state, F_trace, rank)`
- structural coordinates: `(compatibility_defect, TFCD, ambiguity_index)`
- obstruction coordinates from quantized descriptor fibers: `(DFMI, IDELB)`
- augmentation gain: `(CL_abs, CL_rel)`

## Profile semantics

- `IDELB > 0`: amount-only deterministic exact classification is blocked on that declared class.
- `CL_rel > 0`: adding structural coordinates reduces that obstruction.
- `CL_rel = 0`: no additional value from current structural coordinates on that class.

## Current evidence

From `data/generated/structural-information-theory/unified_cross_domain_reduction_metrics.csv`:
- all scored datasets retain `baseline_IDELB > 0`,
- all scored datasets have `CL_rel > 0` after augmentation,
- out-of-family survivor present (`information_real_system`).

## Non-reducibility boundary (current status)

Status: `CONDITIONAL`.

Current pass provides empirical and restricted-theorem support for non-reducibility, but not yet a full general theorem that no scalar transform of amount-only coordinates can match the full vector profile on broad external families.

Next theorem target:
- prove non-reducibility on enlarged independent witness classes with explicit scalar-function class assumptions.
