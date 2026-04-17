# Theorem Candidates And Surviving Results

## Universal backbone

### FBRI-T1: Fiber-constant exactness

Let `F ⊂ X`, `M : F → Y`, and `p : F → P`.
Then the following are equivalent:

1. `p` is exactly recoverable from `M` on `F`
2. `p` is constant on every fiber of `M`
3. `p` factors through `M` on `F`

Status:
- `PROVED`
- standard in spirit
- preserved branch backbone

Repo mapping:
- `OCP-030`

## Coarsening and detectability hierarchy

### FBRI-T2: Fiber-coarsening monotonicity

If `q = φ ∘ p` and `p` is exactly recoverable from `M`, then `q` is exactly recoverable from `M`.
The converse fails even on finite and restricted-linear witnesses.

Status:
- forward implication: `PROVED`, standard
- converse failure: `PROVED`, branch witness-backed

Repo mapping:
- `OCP-048`

## Strongest surviving anti-universal theorems

### FBRI-N1: No rank-only exact classifier theorem

For every `n > r ≥ 1` and every `r ≤ k < n`, there exist restricted finite-dimensional linear recoverability problems with the same ambient dimension `n`, protected rank `r`, and observation rank `k`, but opposite exactness verdicts.

Status:
- `PROVED`

Repo mapping:
- `OCP-049`

### FBRI-N2: No fixed-library budget-only exact classifier theorem

Inside one fixed coordinate candidate library with unit costs, same measurement count and same total budget can still give opposite exactness verdicts.

Status:
- `PROVED`

Repo mapping:
- `OCP-050`

### FBRI-N3: Restricted-linear family-enlargement false-positive theorem

Let `F_s` and `F_ℓ` be admissible linear family bases with `span(F_s) ⊆ span(F_ℓ)`.
If exact recovery holds on `F_s` but

```text
ker(O F_ℓ) ⊄ ker(L F_ℓ),
```

then exact recovery fails on the enlarged family `F_ℓ`.
Moreover, on a bounded coefficient box, the enlarged-family collision gap `Γ_ℓ` yields the lower bound `Γ_ℓ / 2` for every decoder on the enlarged family, including any decoder exact on `F_s`.

Status:
- `PROVED`
- repo-new theorem form
- likely literature-known in spirit

Repo mapping:
- `OCP-052`

## Inverse-map instability theorem

### FBRI-T3: Canonical model-mismatch instability theorem

Let

```text
F_beta = span{e1, e2 + beta e3},
M(x) = (x1, x2),
p(x) = x3.
```

For each fixed `beta`, the target is exactly identifiable on `F_beta`.
If `K_beta0` is the decoder exact on `F_beta0`, then on the true family `F_beta` its worst-case exact-data target error over the unit coefficient box is

```text
|beta - beta0| / sqrt(1 + beta^2).
```

Status:
- `PROVED`
- repo-new exact formulation
- likely literature-known in spirit, but useful as a clean branch theorem

Repo mapping:
- `OCP-053`

Meaning:
- exact identifiability of the true family does not imply robustness of a mismatched inverse map.

## Strongest current noisy hierarchy theorem

### FBRI-T4: Noisy weaker-versus-stronger separation theorem

On the current restricted-linear class, if the weaker target is exact and the stronger target has positive collision gap `Γ`, then the weaker target keeps the upper bound `||K||_2 η` under bounded record noise while the stronger target keeps the lower bound `Γ/2`.

Status:
- `PROVED`

Repo mapping:
- `OCP-051`

## Restricted-linear fiber theorem package

### FBRI-T5: Restricted-linear affine-fiber criterion

For `x = F z`, `y = O F z`, and `p(x) = L F z`, exact recovery holds iff

```text
ker(O F) ⊆ ker(L F).
```

Equivalent row-space form:

```text
row(L F) ⊆ row(O F).
```

Status:
- `PROVED`

Repo mapping:
- `OCP-031`

### FBRI-T6: Fiber refinement under unrestricted augmentation

In the same restricted-linear class, unrestricted added measurements refine the affine fibers until exact recovery first becomes possible at

```text
δ(O, L; F) = rank([O F; L F]) - rank(O F).
```

Status:
- `PROVED`

Repo mapping:
- `OCP-045`

## Family-level threshold laws

### FBRI-T7: Fiber-threshold laws on supported benchmark families

Supported periodic, diagonal/history, and qubit families exhibit exact thresholds when the nested records stop mixing the chosen target on their fibers.

Status:
- `PROVED` or `VALIDATED` according to the original family branch status

Repo mapping:
- `OCP-037`, `OCP-038`, `OCP-039`, `OCP-042`, `OCP-043`
