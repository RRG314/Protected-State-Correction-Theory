# Proof Sketches

This note keeps the short branch proofs and derivations worth reading directly in the canonical fiber-centered stack.

## `OCP-030` fiber-factorization exactness

If `p` is constant on fibers of `M`, define `g(y) = p(x)` for any `x` with `M(x)=y`.
This is well-defined because `p` is fiber-constant.
Then `p = g ∘ M` and exact recovery follows.
The converse is immediate.

## `OCP-048` detectable-only through coarsening

If `q = φ ∘ p` and `p` is exactly recoverable, then `q` factors through the same record.
The converse fails whenever one fiber mixes strong target values while the coarsened target stays constant there.

## `OCP-049` and `OCP-050`

The restricted-linear coordinate witnesses show that equal rank or equal unit-budget does not determine whether the protected rows lie in the observation row space.
So equal amount can still leave different fiber alignment.

## `OCP-051`

The weak target is exact, so its decoder has the error upper bound `||K||_2 η` under bounded record noise.
The stronger target has collision gap `Γ`, so every decoder keeps worst-case error at least `Γ/2`.
The separation persists while `||K||_2 η < Γ/2`.

## `OCP-052`

Let `F_s` and `F_ℓ` be family bases with `span(F_s) ⊆ span(F_ℓ)`.
Assume exactness on the smaller family:

```text
ker(O F_s) ⊆ ker(L F_s).
```

Assume failure on the enlarged family:

```text
ker(O F_ℓ) ⊄ ker(L F_ℓ).
```

Then there exists `v` with `O F_ℓ v = 0` but `L F_ℓ v ≠ 0`, so the enlarged family contains one record fiber mixing target values.
Exact recovery therefore fails on `F_ℓ`.
On a bounded coefficient box the enlarged-family collision gap `Γ_ℓ` gives the lower bound `Γ_ℓ/2` for every decoder on that family.

## `OCP-053`

Take the canonical family

```text
F_beta = span{e1, e2 + beta e3}.
```

After orthonormalization the second family basis vector is

```text
(e2 + beta e3) / sqrt(1 + beta^2).
```

So on coefficient coordinates `(z1, z2)` the record and target are

```text
y = (z1, z2 / sqrt(1 + beta^2)),
p = beta z2 / sqrt(1 + beta^2).
```

Hence the exact decoder on family `beta0` is `K_beta0(y) = beta0 y2`.
Applied to the true family `beta`, its error is

```text
(beta0 - beta) z2 / sqrt(1 + beta^2).
```

Taking the supremum over `|z2| <= 1` gives

```text
|beta - beta0| / sqrt(1 + beta^2).
```

This proves the exact formula and shows that true-family exact identifiability does not imply robustness of a mismatched inverse map.
