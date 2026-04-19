# Agreement-Operator No-Go Candidates

Status: falsification-focused continuation file.

Primary artifacts:
- `data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv`
- `data/generated/context_sensitive_recoverability/agreement_operator_anomaly_catalog.csv`
- `tests/math/test_context_invariant_agreement_operator.py`

## AO-N1. Stack Projection Sufficiency No-Go

Statement:
`row(L) subseteq row(stack(M_c))` is not sufficient for context-invariant exactness.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Why:
- shared-decoder compatibility is stricter than stack-rowspace inclusion.

## AO-N2. Descriptor-Only Classification No-Go

Statement:
Rank/count/budget signatures do not classify invariant exactness, including in agreement-operator instrumented runs.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `59` same-descriptor opposite-verdict groups.

## AO-N3. Universal Operator Novelty No-Go

Statement:
Current agreement operators do not establish a standalone new operator theory independent of OCP linear compatibility logic.

Status:
- `CLOSE PRIOR ART / REPACKAGED`.

## AO-N4. Restricted-Library Threshold Is Not Intrinsic

Statement:
Restricted augmentation thresholds depend on the admissible candidate library and search limit.

Status:
- `PROVED ON RESTRICTED CLASS`.

## AO-N5. Formation-to-Shared-Recovery Promotion No-Go (current)

Statement:
Formation mechanisms currently provide stress-test effects, not theorem-grade independent bridge laws.

Status:
- bridge effects: `VALIDATED / EMPIRICAL ONLY`
- independent bridge theorem: `OPEN`

## AO-N6. Positive Candidate-Library Defect Impossibility

Statement:
If `delta_C = rank([G; C; L]) - rank([G; C]) > 0`, then no augmentation using rows from `C` can restore invariant exactness.

Status:
- `PROVED ON RESTRICTED CLASS`.

Evidence:
- `14` explicit impossibility cases in current continuation catalog.

## AO-N7. Library Rank Gain Is Not Sufficient

Statement:
Matching or exceeding the free threshold with raw library rank gain does not guarantee candidate-library feasibility.

Status:
- `PROVED ON RESTRICTED CLASS`.

Evidence:
- deterministic counterexample test plus `14` catalog cases with
  `library_rank_gain >= free_threshold` and `delta_C > 0`.

## Current no-go boundary summary

1. Amount-only descriptors fail.
2. Stack projection fails as a sufficiency criterion.
3. Candidate-library amount (rank gain) fails without directional compatibility.
4. Formation remains exploratory and cannot yet be promoted into the theorem spine.
