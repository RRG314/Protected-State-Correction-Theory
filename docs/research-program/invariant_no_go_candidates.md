# Invariant No-Go Candidates

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

## NG1. Rank-only Classification No-go

Statement:
- No rank-only descriptor can exactly classify recoverability on supported witness families.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `meta_classifier_invariants.json`:
  - rank descriptor ambiguity rate `1.0`
  - irreducible error lower bound `0.5`

## NG2. Budget-only Classification No-go

Statement:
- No budget-only descriptor can exactly classify recoverability on supported budget witness catalogs.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- budget descriptor ambiguity rate `1.0`; IDELB `0.285714...`.

## NG3. Local Exactness Does Not Imply Shared Exactness

Statement:
- `local_exact_all=1` is insufficient for context-invariant exactness.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `506` local-exact/global-fail rows in multicontext catalog.

## NG4. Free Threshold Alone Is Insufficient Under Candidate Constraints

Statement:
- Achieving free-threshold rank gain is insufficient when candidate-library direction set is deficient.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `14` `library_gain_not_sufficient` anomalies.

## NG5. Candidate-Library Defect Impossibility

Statement:
- Positive candidate-library defect (`delta_C > 0`) prevents exact shared recovery with that library.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `14` `candidate_library_defect_impossibility` anomalies.

## NG6. Family-Enlargement False-Positive No-go

Statement:
- Exactness validated on a narrow family can fail on an enlarged family with unchanged amount descriptors.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `data/generated/unified-recoverability/family_enlargement_false_positive.csv`.
- multicontext anomaly catalog includes `family_enlargement_flip` cases.

## NG7. Mismatch Robustness No-go (current form)

Statement:
- Decoder exactness under the true family does not imply low error under off-family deployment.

Status:
- `VALIDATED / NUMERICAL ONLY`.

Evidence:
- `model_mismatch_stress.csv` shows positive reconstruction error at nonzero subspace distance.

## NG8. Collision-gap Uniform Exactness No-go

Statement:
- Exact collision-gap computation is not computationally uniform across high-null synthetic classes.

Status:
- `PROVED` (computational complexity claim in current implementation).

Evidence:
- collision-gap routine enumerates nullspace boundary configurations combinatorially in nullspace dimension.
- invariant pass now labels high-null outputs as proxy mode.

## Current strongest no-go package

1. Amount-only descriptor insufficiency (rank and budget).
2. Local-vs-shared incompatibility split.
3. Candidate-library defect/lifted compatibility no-go.
4. Family enlargement fragility.
