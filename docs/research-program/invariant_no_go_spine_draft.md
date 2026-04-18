# Invariant No-Go Spine (Draft)

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

## NG1. No rank-only exact classifier

Statement:
No classifier based only on rank tuple descriptors can perfectly classify exactness on supported witness families.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- rank descriptor ambiguity rate `1.0`, IDELB `0.5`.

## NG2. No budget-only exact classifier

Statement:
No amount/cost-only descriptor family can perfectly classify exactness on supported budget witness catalogs.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- budget descriptor ambiguity rate `1.0`, IDELB `0.285714...`.

## NG3. Local exactness does not globalize automatically

Statement:
`E_cond = 1` does not imply `E_inv = 1`.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `506` context-gap cases (`local exact`, `shared fail`).

## NG4. Family-enlargement false-positive no-go

Statement:
Exactness proven on restricted admissible families can fail under enlargement while amount descriptors remain unchanged.

Status:
- `PROVED ON SUPPORTED FAMILY` (existence), `VALIDATED` (frequency).

Evidence:
- canonical enlargement false-positive dataset and multicontext enlargement flips (`94` rows in deep stress catalog).

## NG5. Candidate-library constrained infeasibility

Statement:
Positive library defect (`delta_C > 0`) prevents exact completion under that candidate library.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- agreement-operator anomalies (`14` cases).

## NG6. Candidate rank-gain insufficiency

Statement:
Candidate rank gain matching unconstrained completion need does not guarantee constrained exactness.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `14` `library_gain_not_sufficient` anomalies.

## NG7. Mismatch instability no-go (current maturity)

Statement:
Exactness under true family does not guarantee low deployment error under model mismatch.

Status:
- `VALIDATED / NUMERICAL ONLY`.

Evidence:
- model mismatch stress rows with positive decoder error at nonzero subspace distances.

## NG8. Proxy overreach no-go

Statement:
High-null proxy collision metrics are not exact collision-gap invariants and cannot be promoted as exact thresholds.

Status:
- `PROVED` (methodological/computational boundary).

Evidence:
- explicit `collision_gap_mode` labeling and nullspace complexity boundary.

## Strongest no-go package now

1. amount-only insufficiency (rank, budget),
2. local-vs-shared incompatibility split,
3. constrained completion infeasibility (`delta_C`),
4. enlargement fragility.
