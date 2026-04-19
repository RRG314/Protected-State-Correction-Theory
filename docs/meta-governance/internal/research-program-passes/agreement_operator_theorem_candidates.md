# Agreement-Operator Theorem Candidates

Status: theorem-pressure continuation pass on context-sensitive recoverability.

Primary artifacts:
- `data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv`
- `data/generated/context_sensitive_recoverability/agreement_operator_anomaly_catalog.csv`
- `tests/math/test_context_invariant_agreement_operator.py`

Run snapshot (current continuation):
- witness rows: `300`
- lift/direct consistency: `300/300`
- same-descriptor opposite-verdict groups: `59`
- positive candidate-library defect cases: `14`

## AO-T1. Agreement-Lift Equivalence Theorem

Statement (supported linear class):
Let `M_1, ..., M_k in R^{p x n}` be context matrices and `L in R^{q x n}` a target matrix. Define
`A = { d in R^p : d(M_c - M_1) = 0 for all c }`.
Let `Q` be any row-basis matrix for `A`, and set `G = Q M_1`.

Then:
`invariant_exact(L; {M_c})` iff `row(L) subseteq row(G)`.

Status:
- `PROVED ON RESTRICTED CLASS`.

Evidence:
- exact agreement between direct shared-decoder solver and agreement-lift criterion in all `300/300` sampled families.

Proof idea:
1. Shared decoder `D` implies each decoder row is in `A`, so `L = D M_1` lies in `row(G)`.
2. If `row(L) subseteq row(G)`, write `L = B Q M_1`, set `D = BQ`, then `D M_c = L` for all `c`.

## AO-T2. Free Shared-Augmentation Threshold Formula

Statement (supported linear class, unconstrained shared rows):
With `G = Q M_1` as above,

`r_free^* = rank([G; L]) - rank(G)`

is the minimal number of arbitrary shared augmentation rows required to restore invariant exactness.

Status:
- `PROVED ON RESTRICTED CLASS`.

Evidence:
- constructive residual-row augmentation achieves invariant exactness in all tested cases.

## AO-T3. Descriptor Anti-Classifier Persistence Under Agreement Instrumentation

Statement:
Descriptor signatures built from rank/budget/count summaries do not classify invariant exactness, even after agreement-lift diagnostics are added.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `59` descriptor-matched opposite-verdict anomaly groups.

## AO-T4. Candidate-Library Defect Feasibility Theorem

Objects:
- candidate row library `C` (finite admissible shared augmentation rows),
- lifted matrix `G`,
- library defect
`delta_C = rank([G; C; L]) - rank([G; C])`.

Statement (supported linear class):
Using only rows from candidate library `C`, exact shared recovery after augmentation is feasible with full-library availability iff `delta_C = 0`.

Status:
- `PROVED ON RESTRICTED CLASS`.

Why it matters:
- cleanly separates free-threshold geometry from candidate-library feasibility,
- gives a direct impossibility certificate for constrained augmentation design.

Evidence:
- defect/full-pool exactness agreement across all sampled families.

## AO-T5. Library Rank-Gain Is Not Sufficient (Counterexample Family)

Statement:
`library_rank_gain >= r_free^*` is not sufficient for candidate-library feasibility.

Status:
- `PROVED ON RESTRICTED CLASS`.

Witness form:
- deterministic finite example in `tests/math/test_context_invariant_agreement_operator.py::test_library_rank_gain_is_not_sufficient_for_exactness`.

Interpretation:
- augmentation amount is insufficient; augmentation direction relative to target complement is decisive.

## AO-C1. Restricted Search Threshold Bound

Statement:
For any restricted candidate library and finite search limit,
`r_restricted >= r_free^*` whenever restricted search succeeds.

Status:
- `PROVED ON RESTRICTED CLASS`.

## Novelty and overlap labels

- AO-T1/AO-T2: `PLAUSIBLY DISTINCT PACKAGING`, high overlap risk with known linear compatibility formulations.
- AO-T4/AO-T5: `PLAUSIBLY DISTINCT` as constrained design no-go packaging; likely close to known rank-feasibility principles in systems/design literature.
- AO-T3: anti-classifier persistence is strong on supported families but remains `PROVED ON SUPPORTED FAMILY`.

## Nonclaims

1. No claim beyond finite linear context families.
2. No claim of a standalone operator theory replacing OCP core logic.
3. No unrestricted novelty claim without branch-specific literature closure.
