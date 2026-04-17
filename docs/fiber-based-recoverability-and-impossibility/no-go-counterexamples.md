# No-Go And Counterexample Report

## Purpose

This branch is falsification-first.
The point is not to make one positive universal law sound plausible.
The point is to isolate exactly where universal language stops working.

## Fiber-collision impossibility

Claim killed:
- exact recovery can hold while one fiber still mixes target values.

Reason:
- if `M(x)=M(x')` but `p(x)≠p(x')`, one decoder value would need to equal two different targets.

Status:
- `PROVED`
- standard

## Finite detectable-only witness

Saved artifact:
- [`unified_recoverability_summary.json`](../../data/generated/unified-recoverability/unified_recoverability_summary.json)

Lesson:
- the same record fiber can kill the stronger target while leaving a coarsened one exact.

## Same-rank opposite-verdict witness family

Saved artifact:
- [`rank_only_classifier_witnesses.csv`](../../data/generated/unified-recoverability/rank_only_classifier_witnesses.csv)

Lesson:
- same ambient dimension, same protected rank, and same observation rank can still leave different target behavior on the fibers.

## Fixed-library same-budget witness family

Saved artifact:
- [`candidate_library_budget_witnesses.csv`](../../data/generated/unified-recoverability/candidate_library_budget_witnesses.csv)

Lesson:
- even in one admissible sensor catalog, equal budget does not determine whether the active fibers are target-constant.

## Family-enlargement false-positive witness

Saved artifact:
- [`family_enlargement_false_positive.csv`](../../data/generated/unified-recoverability/family_enlargement_false_positive.csv)

Lesson:
- exactness on a smaller family does not certify exactness on a larger one,
- and the enlarged-family collision gap yields a decoder-agnostic impossibility lower bound.

## Model-mismatch drift witness

Saved artifact:
- [`model_mismatch_stress.csv`](../../data/generated/unified-recoverability/model_mismatch_stress.csv)

Lesson:
- exactness can survive on the true family while a decoder exact on a nearby reference family still drifts.

## Periodic refinement false-positive witness

Saved artifact:
- [`periodic_refinement_false_positive.csv`](../../data/generated/unified-recoverability/periodic_refinement_false_positive.csv)

Lesson:
- coarse modal truncation can make an exact claim look stable until hidden higher-mode target support is admitted again.

## Noisy stronger-versus-weaker witness

Saved artifact:
- [`noisy_restricted_linear_hierarchy.csv`](../../data/generated/unified-recoverability/noisy_restricted_linear_hierarchy.csv)

Lesson:
- bounded noise does not automatically erase the weaker/stronger hierarchy,
- and weak recovery can remain quantitatively meaningful while the stronger target keeps a fiber-mixing impossibility floor.

## Exact-versus-asymptotic control witness

Saved artifacts:
- [`control_exact_vs_asymptotic_split.csv`](../../data/generated/unified-recoverability/control_exact_vs_asymptotic_split.csv)
- [`control_regime_hierarchy.csv`](../../data/generated/unified-recoverability/control_regime_hierarchy.csv)

Lesson:
- exact, detectable-only, and asymptotic are genuinely different regimes.

## Best negative result

The strongest negative lesson is now sharper than “noninvertible maps lose information.”
It is:
- the universal exact core stops at target constancy on fibers,
- amount-only exact classifiers fail already on the restricted-linear theorem class,
- and even a true exact decoder can become a false positive under honest family enlargement.
