# Final Operator Spine

## Plain-Language Summary

OCP is only worth keeping if it constructs or characterizes real correction operators. This file lists the operator layer that survives final review.

## Exact Projector Branch

### Protected projector
```text
P_S
```
- fixes `S`
- annihilates `D`
- gives exact recovery when `H = S ⊕ D` and `S ⟂ D`

### Complementary disturbance projector
```text
P_D = I - P_S
```
- gives the canonical decomposition `x = P_S x + P_D x`
- drives the simplest damping generator `K = k P_D`

## Exact Sector Branch

### Sector projectors
```text
Q_i
```
- orthogonal projectors onto exact disturbance sectors `D_i`
- used as the detection layer of the sector branch

### Sector-conditioned recovery operator
```text
R = Σ_i B_S B_i^{+} Q_i
```
- exact on each orthogonal sector `D_i`
- implemented in `src/ocp/sectors.py`
- instantiated concretely in the 3-qubit bit-flip QEC example

## Exact Continuous Anchor

### Periodic Leray / Helmholtz projector
```text
P_df B = B - ∇Δ^{-1}(div B)
```
- exact continuous recovery operator on the tested periodic branch
- strongest continuous exact operator in the repository

## Asymptotic Continuous Branch

### Damping generator
```text
K = k P_D
```
- simplest asymptotic correction operator
- exact on `S`, exponentially suppressive on `D`

### Invariant-split generator family
```text
x_dot = -Kx
```
with `K|_S = 0`, `K(D) ⊆ D`, stable restriction on `D`
- general asymptotic continuous branch
- includes the PSD/spectral-gap corollary as a distinguished case

### GLM update law
- kept as a practical asymptotic correction architecture
- explicitly not promoted as an exact projector

## Final Operator Boundary

The operator spine stops here intentionally. The following are not promoted as finished operators:
- any boundary-sensitive exact PDE projector beyond the periodic branch,
- any universal capacity operator,
- any optimizer/ML correction operator.
