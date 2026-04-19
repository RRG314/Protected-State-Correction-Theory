# Master Object Language

Date: 2026-04-17

## 1. Core Objects

Let a branch instance be represented by

`(X, A, T, M, C, D, ~, S)`

with:

- `X`: ambient state space.
- `A ⊆ X`: admissible family actually considered by the branch.
- `T : A -> Z`: target/protected map (what we want to preserve/recover/track).
- `M : A -> Y`: observation or record map (what is measured/available).
- `C`: correction architecture (operator, decoder, dynamics, projection, control law, or redesign action).
- `D`: disturbance/ambiguity family (null directions, contaminant sectors, closure remainder, nonlinear defects, etc.).
- `~`: nuisance-equivalence relation (symmetry quotient, gauge-equivalence class, label-equivalence class).
- `S`: side-information/augmentation object (extra rows, history, modal support, boundary constraints, additional sensors, priors).

## 2. Regime Labels

Given `(A,T,M,C,S)` define statuses:

- **Exact recoverable**: there exists `R` (or induced architecture output) with exact target reconstruction on `A`.
- **Exact modulo symmetry**: exact reconstruction of equivalence classes in `A/~`.
- **Approximate**: bounded error law under declared perturbation/noise regime.
- **Asymptotic**: target error tends to zero in time under declared dynamics.
- **Impossible**: no architecture in declared class can recover the target exactly on `A`.
- **Detectable but not exact**: at least one coarsened target is recoverable, stronger one is not.

## 3. Recoverability / Preservation / Obstruction

### Recoverability
`T` is recoverable from `M` on `A` iff `T` factors through `M` on `A`.
Equivalent fiber form: `T` is constant on every record fiber of `M`.

### Preservation
A correction architecture `C` preserves structure if `C(x)` remains in the protected class or target-equivalent class for declared branch conditions.

### Obstruction
An obstruction is any branch-valid mechanism that prevents exactness, e.g.:
- overlap/indistinguishability,
- target variation inside fibers,
- row-space/kernal incompatibility,
- boundary/topology mismatch,
- family enlargement introducing new collision directions,
- model mismatch decoders.

## 4. Family Enlargement and Model Mismatch

- **Family enlargement**: replace `A_s` by `A_l` with `A_s ⊂ A_l` and test whether exactness survives.
- **Model mismatch**: decoder/correction `C_hat` is exact on declared model family `A_hat` but evaluated on true family `A_true`.

Both are first-class objects in the unifying language because they create false-positive exactness claims in multiple branches.

## 5. Side-Information Augmentation

Augmentation is represented by `S` and modifies `(M,C)` to `(M_S, C_S)`.
Canonical branch pattern: augmentation refines fibers / resolves compatibility defects / repairs architecture mismatch.

## 6. Branch Translation Map

| Branch | `X` | `A` | `T` | `M` | `C` | `D` | `~` | `S` |
|---|---|---|---|---|---|---|---|---|
| OCP exact projector | linear state space | decomposition-compatible states | protected component | identity or full state | orthogonal projector | disturbance subspace | trivial | optional added operator constraints |
| OCP restricted-linear recoverability | `R^n` | `A={Fz}` | `LFz` | `OFz` | linear decoder `K` + redesign rules | kernel/fiber directions | trivial | added rows/history (`δ`) |
| OCP bounded-domain/Hodge | velocity/field function space | boundary-compatible finite-mode family | protected bounded-domain class | divergence or projected records | compatible Hodge projector | boundary-incompatible components | gauge/representation classes as needed | boundary/operator compatibility side info |
| Soliton recoverability | one-soliton parameterized manifold samples | restricted one-soliton families | parameters or quotient parameters | selected local/Fourier/moment observations | estimator class per observation family | observation collisions + non-identifiable pairs | translation/phase symmetry group | extra observation types |
| Soliton projection lane | same as above | declared scenarios | manifold closeness / structural score | projected states/diagnostics | projection/reduction operator | operator-induced distortion | symmetry quotient optional | cutoff, resolution, operator class |
| MHD closure branch | Euler-potential field class | declared cylindrical/annular ansätze | closure exactness (or zero remainder target) | derived remainder/field terms | correction source PDE/ODE on ansatz | variable-`η` obstruction terms | gauge-like representational redundancy | domain class, ansatz class, profile assumptions |
| SDS structural discovery layer | typed branch model space | supported branch compositions | regime correctness + repair objective | diagnostics records | recommendation/repair workflow | missing-support / mismatch diagnostics | branch-dependent | user-selected augmentations |
| Two-reservoir SDS engineering | optimizer state space | benchmark task families | loss + stability diagnostics | run metrics | SDS-gated optimizer update | instability / inefficiency | n/a | two-reservoir efficiency gate parameters |

## 7. What This Language Enables

1. Uniform statement of exactness/impossibility without forcing branch flattening.
2. Clear distinction between theorem-core and engineering layers.
3. Explicit treatment of symmetry quotient, family enlargement, and model mismatch.
4. Honest transfer testing: branch claims can be mapped, then either promoted, restricted, or rejected.
