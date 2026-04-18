# Quantum Alignment Theorem Candidates

Status: branch-limited theorem slate for the quantum-alignment lane.

## Scope discipline

- This is not a new quantum foundation.
- This does not replace quantum estimation theory.
- All statements below are explicitly scoped.

## QA-T1. Alpha notation over QFI/CFI ratio

Statement:
- For scalar parameter `theta` and measurement `M`, define
  - `alpha_Q(theta,M) = sqrt(F_M(theta)/F_Q(theta))`.

Status:
- `KNOWN / REFRAMED`.

Reason:
- Direct restatement of the Braunstein-Caves bound `F_M <= F_Q`.

## QA-T2. Restricted projective qubit conservation identity

Statement (restricted):
- Let `rho(theta_1, theta_2)` be a regular two-parameter pure qubit family with diagonal `F_Q = diag(F_Q,11, F_Q,22)` at the point of evaluation.
- Let `M` be a single two-outcome projective measurement.
- Define `alpha_k^2 = F_M,kk / F_Q,kk`.
- Then
  - `alpha_1^2 + alpha_2^2 = 1`.

Status:
- `PROVED ON RESTRICTED CLASS`.

## QA-T3. Coordinate-invariant trace form (same restricted qubit class)

Statement:
- Under the same qubit conditions but without requiring diagonal coordinate form,
  - `trace(F_Q^{-1} F_M) = 1`
  for single projective two-outcome measurements.

Status:
- `PROVED ON RESTRICTED CLASS`.

Comment:
- This is the cleaner parameterization-invariant form.
- In diagonal coordinates, QA-T3 reduces to QA-T2.

## QA-T4. Rank-1 qubit POVM extension (candidate extension)

Statement:
- For tested rank-1 qubit POVMs (`4` outcomes), pure two-parameter qubit models satisfy the same trace identity:
  - `trace(F_Q^{-1} F_M) = 1`.

Status:
- `PROVED ON RESTRICTED CLASS` (proof in notes for the rank-1 qubit setting).

Literature risk:
- High overlap with known multiparameter qubit Fisher bounds.

## QA-C1. Balanced-design corollary

Statement:
- Under QA-T2,
  - `max_M min(alpha_1, alpha_2) = 1/sqrt(2)`.
- Achieved by the measurement axis bisecting the two tangent directions.

Status:
- `PROVED ON RESTRICTED CLASS`.

## QA-N1. Mixed-state attenuation law (restricted orientation model)

Statement:
- For tested mixed qubit orientation families under single projective measurement,
  - `alpha_1^2 + alpha_2^2 < 1`
  in interior mixed-state regimes (`||r|| < 1`) and generic directions.

Status:
- `PROVED ON RESTRICTED CLASS`.

## QA-N2. Non-diagonal coordinate alpha-sum failure

Statement:
- The diagonal-coordinate scalar expression `J11/F11 + J22/F22 = 1` is not invariant under non-diagonal parameterization.

Status:
- `DISPROVED` as a coordinate-free law.

Replacement:
- Use QA-T3 (`trace(F_Q^{-1}F_M)=1`) on the restricted qubit class.

## Nonclaims (mandatory)

1. No universal law across all dimensions.
2. No claim that non-projective POVMs preserve the exact qubit equality.
3. No claim that this is new in substance relative to Gill-Massar/Holevo-family multiparameter bounds.

