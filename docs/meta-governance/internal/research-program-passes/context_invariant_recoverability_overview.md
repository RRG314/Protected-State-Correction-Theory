# Context-Invariant Recoverability Overview

Status: **CONDITIONAL MAJOR CANDIDATE (branch-limited)**

This lane introduces a multi-context recoverability layer where exactness is split into two regimes:

1. conditioned exactness: each context is exactly recoverable with a context-specific decoder,
2. context-invariant exactness: one shared decoder is exact across all contexts.

The lane is grounded in restricted-linear witnesses tied to causal-inference and Willems data-richness settings.
It does not replace core OCP/fiber results and is not promoted to universal status.

Primary additions in this pass:

- a branch-limited conditioned-vs-invariant exactness split,
- descriptor-matched opposite-verdict witnesses for context invariance,
- shared augmentation threshold examples restoring invariant exactness.

Non-claims:

- no theorem-spine promotion in this pass,
- no universal claim across all branches,
- no replacement of existing OCP/PVRT language.
