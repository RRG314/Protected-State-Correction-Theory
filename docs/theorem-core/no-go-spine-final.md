# Final No-Go Spine

This file records the promoted impossibility boundaries. These are first-class results, not side notes.

## Core exact and continuous limits

Promoted no-go anchors include:
- `OCP-003`: overlap-driven non-uniqueness.
- `OCP-015`: mixing obstruction in linear flows.
- `OCP-020`: no finite-time exact annihilation in smooth linear flows.
- `OCP-021`: sector-overlap failure of unique exact detection.

Why this matters: these results prevent overclaiming in exact or finite-time settings.

## PDE and boundary limits

- `OCP-023`: naive periodic-projector transfer to bounded domains fails.
- `OCP-028`: divergence-only bounded recovery is impossible for nontrivial protected classes.

Why this matters: domain and boundary structure are part of recoverability, not implementation detail.

## Anti-classifier and fragility limits

- `OCP-047`: same-rank insufficiency.
- `OCP-049`: no rank-only exact classifier.
- `OCP-050`: no fixed-library budget-only exact classifier.
- `OCP-052`: family-enlargement false positives.
- `OCP-053`: model-mismatch instability.

Why this matters: amount-only summaries can look sufficient while exact recovery still fails.

## Scope guardrail

`OCP-009` remains unproved as a universal scalar capacity law and is not promoted.

Practical interpretation:
- do not classify recoverability by amount-only descriptors,
- do not transfer periodic theorems to bounded settings without boundary checks,
- do not assume decoders remain exact under family enlargement or model mismatch.
