# Context-Invariant Recoverability Validation Plan

## Immediate checks

1. Recompute canonical causal and Willems witness families and verify conditioned-vs-invariant split.
2. Recompute descriptor-matched opposite-verdict pairs.
3. Recompute minimal shared augmentation threshold witnesses.
4. Verify stacked single-context exactness does not falsely certify invariant exactness.

## Stress tests

1. Add additional context scalings and check persistence of no-go behavior.
2. Perturb target maps and record maps to test robustness of threshold findings.
3. Compare against existing metrics (rank, row-space residual, DLS, delta) to quantify additive value.

## Promotion gate

Promotion is blocked unless a stronger general theorem is proved beyond the currently supported finite/restricted-linear families.
