# Inverse / Observability Frontier Audit

## Which current results already look like identifiability / observability results?

Strongest current identifiability-facing results:
- `OCP-030`: exact target identifiability iff target is constant on record fibers.
- `OCP-031`: restricted-linear exactness criterion `ker(O F) ⊆ ker(L F)`.
- `OCP-045`: minimal exact augmentation law.
- `OCP-046`: exact-regime upper envelope.
- `OCP-048`: coarsened target identifiability / detectable-only regime.
- `OCP-049`, `OCP-050`: amount-only anti-classifier theorems.
- `OCP-051`: noisy weaker-versus-stronger separation.
- `OCP-052`: family-enlargement false-positive theorem.
- `OCP-053`: canonical model-mismatch instability theorem.

## Which are strongest as inverse-problem no-go theorems?

Strongest current negative results:
- `OCP-030` viewed negatively: exact-data nonuniqueness kills exact target recovery.
- `OCP-047`: same-rank insufficiency.
- `OCP-049`: no rank-only classifier.
- `OCP-050`: no fixed-library budget-only classifier.
- `OCP-052`: exactness can fail under honest family enlargement.

## Which are only family-specific examples?

Still family-specific:
- periodic modal thresholds,
- diagonal/history thresholds,
- qubit phase-loss threshold,
- bounded-domain projector mismatch,
- observer versus finite-history split.

## Which are still too weak or too wording-dependent?

Still too weak to promote broadly:
- universal observability laws,
- universal discretization robustness,
- universal model-mismatch robustness,
- nonlinear generalizations beyond narrow supported families.

## Which current theorem is the strongest paper base?

Strongest current outside-facing paper base:
- `OCP-049` through `OCP-053` as a restricted theorem/falsification package for target identifiability under partial/coarse records.
