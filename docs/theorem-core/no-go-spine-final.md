# Final No-Go Spine

This file records promoted impossibility boundaries.

## Core Exact and Continuous Limits

Promoted no-go anchors:

- `OCP-003`: overlap-driven non-uniqueness.
- `OCP-015`: mixing obstruction in linear flows.
- `OCP-020`: no finite-time exact annihilation in smooth linear flows.
- `OCP-021`: sector-overlap failure of unique exact detection.

These limits constrain exact and finite-time recovery claims.

## PDE and Boundary Limits

- `OCP-023`: naive periodic-projector transfer to bounded domains fails.
- `OCP-028`: divergence-only bounded recovery is impossible for nontrivial protected classes.

These results make domain and boundary conditions part of theorem scope, not post hoc caveats.

## Anti-Classifier and Fragility Limits

- `OCP-047`: same-rank insufficiency.
- `OCP-049`: no rank-only exact classifier.
- `OCP-050`: no fixed-library budget-only exact classifier.
- `OCP-052`: family-enlargement false positives.
- `OCP-053`: model-mismatch instability.

These results show that amount-only descriptors can coincide while exact-recovery verdicts differ.

## Scope Guardrail

`OCP-009` remains unproved as a universal scalar capacity law and is not promoted.

Interpretation rule:

- do not classify recoverability by amount-only descriptors,
- do not transfer periodic theorems to bounded settings without boundary checks,
- do not assume decoders remain exact under family enlargement or model mismatch.
