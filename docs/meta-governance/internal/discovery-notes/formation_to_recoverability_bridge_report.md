# Formation-to-Recoverability Bridge Report

Status: `EXPLORATION / NON-PROMOTED`

This report tests whether the secondary formation lane yields justified bridges to the main context-sensitive recoverability package.

Data:
- `data/generated/sfpr/formation_secondary_witnesses.csv`
- `data/generated/context_sensitive_recoverability/multicontext_witness_catalog.csv`

## Bridge Question 1

Can a formation mechanism create structure that is contextwise recoverable but not context-invariantly recoverable?

Answer: **YES**.

Evidence:
- `280/980` formation cases end in `post_local_exact=1` and `post_shared_exact=0`.
- strongest contributor: symmetry-breaking and context-conditioned differentiation templates.

Status: `VALIDATED / EMPIRICAL ONLY`.

## Bridge Question 2

Can formation increase apparent local structure while making global/shared recovery worse?

Answer: **PARTIAL**.

Evidence:
- `140` cases with local recoverability increase and no shared recoverability gain.
- direct shared-recoverability decrease was not observed (`0` cases).

Status: `CONDITIONAL`.

## Bridge Question 3

Are there formation-induced threshold flips in augmentation need?

Answer: **YES**.

Evidence:
- `632/980` cases have threshold-flip flag between pre/post formation.

Status: `VALIDATED / EMPIRICAL ONLY`.

## Bridge Question 4

Does formation generate anomaly families not explainable by current multi-context recoverability alone?

Answer: **NOT YET CLEAR**.

Reason:
- Many bridge effects map onto existing context-compatibility mechanisms (local-vs-shared split, augmentation threshold changes).
- Distinct mechanism classes exist, but no new theorem-level invariant independent of main-track objects has been isolated.

Status: `OPEN`.

## Bridge Decision

No bridge theorem is ready for promotion.

What survives:
- empirical bridge patterns useful for hypothesis generation.

What does not survive:
- claim that formation already contributes independent theorem power beyond main-track context-sensitive recoverability.
