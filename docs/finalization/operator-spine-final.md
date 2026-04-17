# Final Operator Spine

## Plain-Language Summary

The repository is operator-first.

The canonical operator spine now includes both:
- correction operators in exact/asymptotic projector branches,
- and recoverability operators/maps in constrained-observation and fiber-limit branches.

## 1. Exact Projector Operators

### Protected projector
`P_S`
- fixes protected space `S`
- annihilates disturbance `D`
- exact under `H = S ⊕ D`, `S ⟂ D`

### Disturbance projector
`P_D = I - P_S`
- canonical decomposition operator
- feeds damping generator constructions

## 2. Sector Operators

### Sector projectors
`Q_i`
- orthogonal projectors onto sector family `D_i`

### Sector-conditioned recovery operator
`R = Σ_i B_S B_i^+ Q_i`
- exact on each supported orthogonal sector

## 3. Continuous/PDE Operators

### Periodic Leray/Helmholtz projector
`P_df B = B - ∇Δ^{-1}(div B)`
- exact periodic continuous anchor

### Bounded-domain restricted Hodge projector (family-restricted)
- exact on boundary-compatible finite-mode protected/disturbance families (`OCP-044`)
- not promoted as universal bounded-domain operator theorem

## 4. Asymptotic Generator Operators

### Damping generator
`K = k P_D`
- preserves protected space and damps disturbance asymptotically

### Invariant-split generator class
`x_dot = -Kx`, with `K|_S = 0`, `K(D) ⊆ D`, stable restriction on `D`
- canonical asymptotic branch operator class

## 5. Constrained-Observation Operators

### Observation and protected maps
- record map: `M` (or matrix form `O` on restricted-linear families)
- protected map: `p` (or matrix form `L`)

### Exactness compatibility operators
- exactness condition in restricted-linear families:
`ker(O F) ⊆ ker(L F)`
- equivalent row-space compatibility condition

### Exact recovery operator on restricted-linear exact class
- `K` such that `K O F = L F`
- drives exact-regime upper envelope (`OCP-046`)

### Minimal augmentation deficiency operator quantity
`δ(O, L; F) = rank([O F; L F]) - rank(O F)`
- exact unrestricted added-measurement count (`OCP-045`)

## 6. Fiber/Hierarchy Operators

### Target coarsening map
`q = φ ∘ p`
- exact stronger-target recoverability implies exact coarsened-target recoverability (`OCP-048`)

### Collision-gap quantities
- structured collision gaps used as quantitative impossibility floors in restricted classes (`OCP-043`, `OCP-051`, `OCP-052`)

## Operator Boundary

Not promoted as finished universal operator outputs:
- one universal scalar capacity operator,
- one universal bounded-domain exact projector theorem,
- one universal nonlinear inverse-operator framework across all branches.
