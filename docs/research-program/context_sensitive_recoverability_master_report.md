# Context-Sensitive Recoverability Master Report

Status: conditional theory package on supported families.

This branch tests a narrow split between conditioned exactness and shared context-invariant exactness. The split survives on declared finite linear context-indexed families: many systems are exact per context but fail under a shared decoder. That behavior is reproducible and does not collapse to amount-only descriptors.

Three components remain central. The conditioned-vs-invariant split is proved on supported classes. Shared augmentation thresholds are positive and reproducible, with explicit constrained-library failure cases captured by `delta_C`. Multi-context opposite-verdict families are robust on catalogs, while broader robustness claims remain empirical.

The branch is additive in packaging and diagnostic power, but it is not yet ready for core-spine promotion. The key bottleneck is stronger theorem-level augmentation bounds and broader non-synthetic validation. Formation-side bridge ideas remain exploratory and should stay separate from the narrow theorem track.

The immediate next move is to deepen augmentation theorem structure before promotion.
