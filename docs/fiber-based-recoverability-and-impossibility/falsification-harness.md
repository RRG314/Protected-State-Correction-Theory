# Falsification Harness

This branch now keeps an explicit false-positive harness instead of treating exact recovery claims as self-certifying.

## Harness goals

The harness is designed to catch:
1. same-rank false positives,
2. same-budget false positives,
3. family-restriction false positives,
4. target-choice false positives,
5. noise / near-collision false positives,
6. model-mismatch false positives,
7. discretization / modal-refinement false positives,
8. wrong-architecture false positives.

## Current executable pieces

### Same-rank anti-classifier
- artifact: [`rank_only_classifier_witnesses.csv`](../../data/generated/unified-recoverability/rank_only_classifier_witnesses.csv)
- theorem link: `OCP-049`

### Same-budget anti-classifier
- artifact: [`candidate_library_budget_witnesses.csv`](../../data/generated/unified-recoverability/candidate_library_budget_witnesses.csv)
- theorem link: `OCP-050`

### Noisy weaker-versus-stronger separation
- artifact: [`noisy_restricted_linear_hierarchy.csv`](../../data/generated/unified-recoverability/noisy_restricted_linear_hierarchy.csv)
- theorem link: `OCP-051`

### Family-enlargement false positive
- artifact: [`family_enlargement_false_positive.csv`](../../data/generated/unified-recoverability/family_enlargement_false_positive.csv)
- theorem link: `OCP-052`

### Model-mismatch drift
- artifact: [`model_mismatch_stress.csv`](../../data/generated/unified-recoverability/model_mismatch_stress.csv)
- status: `VALIDATED`

### Periodic refinement false positive
- artifact: [`periodic_refinement_false_positive.csv`](../../data/generated/unified-recoverability/periodic_refinement_false_positive.csv)
- status: `VALIDATED`

## What the harness is currently good at

It is strongest on:
- finite and restricted-linear exactness claims,
- target hierarchy claims,
- sensor geometry falsification,
- family-enlargement attacks,
- coarse periodic modal reconstruction attacks.

## What it does not yet certify

It does not yet certify:
- broad nonlinear robustness,
- arbitrary PDE model mismatch,
- universal discretization-stability laws,
- generic regularized inverse-problem stability.
