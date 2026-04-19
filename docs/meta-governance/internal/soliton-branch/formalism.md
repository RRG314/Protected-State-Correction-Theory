# Soliton Branch Formalism

Date: 2026-04-17

## 1) Equation Class and Families

We use the focusing 1D NLS one-soliton profile at fixed time:

`psi(x; eta, x0, v, phi) = eta * sech(eta (x - x0)) * exp(i(0.5 v (x - x0) + phi))`.

Restricted parameter families:

- Family A: `P_A = {(eta, x0, phi)}`
- Family B: `P_B = {(eta, x0, v, phi)}`

with bounded grids in current validation artifacts.

## 2) Symmetry Group and Quotient Target

Nuisance symmetry group `G` (declared here):
- translation in `x0`,
- global phase in `phi`.

Recovery targets:
- on `P_A / G`: recover `eta`,
- on `P_B / G`: recover `(eta,v)`.

Recoverability claim form:

Given observation map `M`, recoverability modulo symmetry means:
`exists D such that D(M(psi(p))) = q(p)` for all `p` in the declared family, where `q` is the quotient map.

## 3) Observation Families (Current Branch Scope)

- `local_magnitude_4`
- `local_complex_2`
- `derivative_enhanced_local`
- `global_norms`
- `moments_center_mass`
- `fourier_magnitudes_4`
- `mixed_local_global`

## 4) Projection/Reduction Secondary Scope

Projection classes tested:
- `lowpass_k18pct`
- `subsample_interp_x8`

Baseline integrators:
- split-step Fourier (structure-preserving baseline),
- forward Euler finite difference (non-preserving comparator).

## 5) Regime Labels Used in This Branch

- `PROVED`: theorem closed on declared class.
- `CONDITIONAL`: theorem candidate not yet closed in continuous setting.
- `VALIDATED`: computationally reproduced on declared tested families.
- `OPEN`: unresolved theorem/counterexample gap.
- `DISPROVED`: explicit failure under branch tests.
- `ANALOGY ONLY`: conceptual relation without theorem support.
