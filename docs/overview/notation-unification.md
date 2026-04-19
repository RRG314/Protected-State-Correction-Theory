# Notation Unification

Date: 2026-04-17
Status: Canonical notation reference

## Core Abstract Layer

| Symbol | Meaning |
| --- | --- |
| `X` | ambient state space |
| `A` | admissible family (`A ⊆ X`) |
| `T` | target map (protected quantity to recover/preserve) |
| `M` | observation/record map |
| `R` | recovery map from records to target |
| `C` | correction architecture/operator/process |
| `D` | disturbance/ambiguity family |
| `~` | nuisance equivalence (e.g., symmetry quotient) |

Backbone exactness statement (on `A`):
- exact recoverability iff `T` is constant on fibers of `M`
- equivalent factorization: `T = R ∘ M` on `A`

## Restricted-Linear Layer

| Symbol | Meaning |
| --- | --- |
| `x = Fz` | restricted family parameterization |
| `O` | observation matrix (`M(x)=Ox`) |
| `L` | target matrix (`T(x)=Lx`) |
| `OF`, `LF` | effective maps on coefficient space |

Canonical exactness criterion:
- `ker(OF) ⊆ ker(LF)`
- equivalent: `row(LF) ⊆ row(OF)`

Minimal augmentation law:
- `delta(O, L; F) = rank([OF; LF]) - rank(OF)`

## Quantitative Layer

| Symbol | Meaning |
| --- | --- |
| `kappa(delta)` / `κ(δ)` | collapse modulus / ambiguity profile at record tolerance `δ` |
| `Gamma` / `Γ_r(B)` | collision-gap threshold quantity |
| `delta(O, L; F)` | augmentation deficiency (not noise radius) |

Rule: never overload `delta` in one theorem statement without explicit qualification.

## Continuous/Generator Layer

| Symbol | Meaning |
| --- | --- |
| `K` | correction generator |
| `S` | protected subspace/sector |
| `P_S` | projector onto protected component |
| `P_D` | projector onto disturbance component |
| `lambda_*` | spectral-gap parameter on disturbance complement |

## PDE / Domain Layer

| Symbol | Meaning |
| --- | --- |
| `Omega` | spatial domain |
| `div`, `grad`, `curl` | standard differential operators |
| Hodge-compatible projector | boundary/domain-consistent protected-state projector |

## Cross-Paper Consistency Rules

1. Prefer `(M, T, R)` in abstract sections.
2. Switch to `(O, L, F)` only in restricted-linear sections.
3. Preserve meaning of `S`, `D`, `P_S`, `P_D` across exact/asymptotic branches.
4. Define local symbols once per document if extra branch notation is needed.

## Canonical Cross-References

- `docs/overview/terminology-unification.md`
- `docs/overview/repo-authority-map.md`
- `docs/theorem-core/theorem-spine-final.md`
- `docs/restricted-results/README.md`
