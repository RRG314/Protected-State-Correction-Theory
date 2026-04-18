# Operator Test Notes

Status: explicit mapping between computational tests and mathematical questions.
Data:
- `data/generated/operator_discovery/operator_witness_catalog.csv`
- `data/generated/operator_discovery/operator_anomaly_catalog.csv`
- `data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv`

## Test OT1 — Shared Decoder Feasibility

Question:
- Does a shared decoder exist across contexts?

Measured quantity:
- CLE residual / `CID` zero-test.

Justified conclusion:
- exact shared recoverability in declared linear class.

Not justified:
- nonlinear/infinite-dimensional/global claims.

## Test OT2 — Conditioned-vs-Invariant Split

Question:
- Can local exactness coexist with shared-decoder failure?

Measured quantity:
- pair `(local_exact_all, invariant_exact)`.

Justified conclusion:
- split existence in supported family.

Not justified:
- universality beyond generated families.

## Test OT3 — Descriptor-Only Insufficiency

Question:
- Do amount-only descriptors classify invariant exactness?

Measured quantity:
- opposite verdict groups under same descriptor signature.

Justified conclusion:
- descriptor-only insufficiency for tested descriptor class.

Not justified:
- impossibility of all future enriched descriptor classes.

## Test OT4 — Augmentation Threshold Behavior

Question:
- Is strictly positive shared augmentation needed in local-exact/global-fail cases?

Measured quantity:
- minimal found `r_*` and augmentation gain in CID.

Justified conclusion:
- positive-threshold existence under fixed admissibility class.

Not justified:
- closed-form threshold law without further proof.

## Test OT5 — Projection Sufficiency Check

Question:
- Is stack row-space projection sufficient for invariant exactness?

Measured quantity:
- stack residual near zero + invariant failure frequency.

Justified conclusion:
- stack projection alone is insufficient in supported family.

Not justified:
- rejection of projection methods generally.

## Test OT6 — Lift Conditioning as Classifier

Question:
- Does `sigma_min(A)` classify shared exactness?

Measured quantity:
- conditioning buckets with opposite exactness outcomes.

Justified conclusion:
- conditioning is not a sufficient classifier.

Not justified:
- conditioning is irrelevant; it may still aid robustness diagnostics.

## Test OT7 — Collapse Index Utility

Question:
- Does collision structure track target ambiguity severity?

Measured quantity:
- finite-pair collapse index on record fibers.

Justified conclusion:
- useful empirical diagnostic for ambiguity severity.

Not justified:
- independent theorem power beyond fiber-collision logic.

## Test OT8 — Candidate-Library Defect Feasibility

Question:
- Can a declared candidate row library restore invariant exactness at all?

Measured quantity:
- `delta_C = rank([G;C;L]) - rank([G;C])` and full-library exactness check.

Justified conclusion:
- `delta_C=0` is an exact full-pool feasibility criterion in the supported linear class.
- `delta_C>0` is an impossibility certificate for that library.

Not justified:
- claims about minimal restricted row count without additional combinatorial bounds.

## Summary of Test Correctness

- Most tests answer correct theorem/no-go questions for the declared linear supported class.
- Main overreach risks are scope inflation and novelty inflation, not metric mismatch.
- Safe usage: theorem statements for split/no-go existence and candidate-library defect feasibility; diagnostic usage for conditioning/collapse/projection gain.
