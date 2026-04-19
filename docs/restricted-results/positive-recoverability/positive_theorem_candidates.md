# Positive Theorem Candidates

This file summarizes the strongest positive candidates on the restricted context-linear class.

## Status vocabulary

`PROVED`, `PROVED ON SUPPORTED FAMILY`, `KNOWN / REFRAMED`, `VALIDATED / NUMERICAL ONLY`, `CONDITIONAL`, `DISPROVED`, `OPEN`.

Primary evidence artifacts:
- `data/generated/positive_framework/positive_witness_catalog.csv`
- `data/generated/positive_framework/positive_counterexample_catalog.csv`
- `data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv`

## PT-1: CORS characterization

What it says:
Shared exact recoverability is equivalent to compatibility row-space inclusion on the declared class.

Assumptions:
Finite-dimensional linear context model.

Where it applies:
Declared context-linear family only.

Why it matters:
Turns shared recoverability into a direct compatibility test.

Status:
`PROVED ON RESTRICTED CLASS`; mathematically mostly `KNOWN / REFRAMED`.

## PT-2: Compatibility sufficiency

What it says:
If compatibility holds, shared exact recoverability follows.

Evidence:
All CORS-positive generated witness families were exact in this pass.

Why it matters:
Gives a direct design criterion.

Status:
`PROVED ON RESTRICTED CLASS`.

## PT-3: Minimal free completion size

What it says:
`r_free*` is both a lower bound and an achievable completion size for unrestricted shared augmentation.

Why it matters:
It gives a concrete augmentation target instead of trial-and-error sensor addition.

Status:
`PROVED ON RESTRICTED CLASS`.

## PT-4: Constrained augmentation criterion

What it says:
`delta_C = 0` is the exact feasibility test for completion from a declared candidate library.

Why it matters:
Library rank gain alone can look promising while completion is still impossible.

Status:
`PROVED ON RESTRICTED CLASS`.

## PT-5: Context-consistency promotion

What it says:
Local exactness plus global compatibility coherence implies shared exactness.

Why it matters:
Explains the local-success/global-failure split.

Status:
`PROVED ON RESTRICTED CLASS`; mostly `KNOWN / REFRAMED` structure.

## PT-6: Descriptor-lift separation on supported families

What it says:
Amount-only signatures can collide on opposite verdicts, while descriptor-lift quantities separate those collisions on the supported generated families.

Evidence in this pass:
45 opposite-verdict same-amount pairs, all separated by `CID` and `r_free*`.

Why it matters:
Shows diagnostic value beyond amount summaries, without universal claims.

Status:
`PROVED ON SUPPORTED FAMILY`.

## PT-7: Robustness candidate

Candidate claim:
Margin-based perturbation stability above exact factorization core.

Current result:
No clean universal law survived across generated family classes.

Status:
`CONDITIONAL / OPEN`.

## Practical take-away

The strongest positive cluster is PT-1 through PT-4, with PT-6 as supported-family diagnostic reinforcement.
