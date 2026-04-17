# Proof Sketches and Derivations

## Purpose

This note records the branch proofs that are short enough to state cleanly and important enough not to leave implicit.

## 1. URI-T1: Fiber-factorization exactness

Let `M : F → Y` and `p : F → P`.

### Claim

The following are equivalent:
1. `p` is exactly recoverable from `M` on `F`.
2. `p` is constant on fibers of `M`.
3. `p` factors through `M` on `F`.

### Proof

`1 ⇒ 2`:
If `R(M(x)) = p(x)` for all `x ∈ F` and `M(x)=M(x')`, then

```text
p(x) = R(M(x)) = R(M(x')) = p(x').
```

`2 ⇒ 3`:
Define `\widetilde p` on `M(F)` by `\widetilde p(M(x)) = p(x)`.
This is well-defined exactly because `p` is constant on fibers.
Then `p = \widetilde p ∘ M` on `F`.

`3 ⇒ 1`:
If `p = \widetilde p ∘ M` on `F`, then `R = \widetilde p` is a recovery map.

## 2. URI-T2: Coarsening monotonicity

### Setup

Let `q = φ ∘ p` for some map `φ`.

### Claim

If `p` is exactly recoverable from `M`, then `q` is exactly recoverable from `M`.

### Proof

If `p = R ∘ M` on `F`, then

```text
q = φ ∘ p = φ ∘ R ∘ M.
```

So `q` factors through `M` as well.

### Why the converse fails

Take a finite witness with records

```text
M(x_1)=0,
M(x_2)=1,
M(x_3)=1,
```

strong target values

```text
p(x_1)=0,
p(x_2)=1,
p(x_3)=2,
```

and weak target values

```text
q(x_1)=0,
q(x_2)=1,
q(x_3)=1.
```

Then `q` is constant on record fibers, but `p` is not.
So `q` is exact while `p` is impossible.

## 3. URI-N1: No rank-only exact classifier theorem

### Claim

For every `n > r ≥ 1` and every `r ≤ k < n`, there exist two restricted finite-dimensional linear recoverability problems with the same ambient dimension `n`, protected rank `r`, and observation rank `k`, but opposite exactness verdicts.

### Construction

Work in `\mathbb{R}^n` and take the protected matrix

```text
L =
[e_1^T]
[⋮    ]
[e_r^T].
```

So `rank(L)=r`.

Define the exact observation family by

```text
O_exact =
[e_1^T]
[⋮    ]
[e_k^T].
```

Then `rank(O_exact)=k`, and because every protected row `e_1^T, …, e_r^T`
appears in the row space of `O_exact`, we have

```text
row(L) ⊂ row(O_exact),
```

so exact recovery holds on the restricted-linear criterion.

Now define the fail family by deleting `e_1^T` from the observation rows and replacing it with one extra nonprotected coordinate:

```text
O_fail =
[e_2^T]
[⋮    ]
[e_r^T]
[e_{r+1}^T]
[⋮      ]
[e_{k+1}^T].
```

This still has rank `k`, but now `e_1^T` is not in `row(O_fail)`, so

```text
row(L) ⊄ row(O_fail).
```

Therefore exact recovery fails.

### Conclusion

The two systems have the same:
- ambient dimension `n`,
- protected rank `r`,
- observation rank `k`,

but opposite exactness verdicts.
Hence no classifier depending only on `(n, rank(LF), rank(OF))` can classify exact recoverability on all restricted finite-dimensional linear families.

## 4. URI-N2: No fixed-library budget-only exact classifier theorem

### Claim

Fix the coordinate candidate library

```text
C = {e_1^T, …, e_n^T}
```

with unit measurement costs.
For every `n > r ≥ 1` and every `r ≤ k < n`, there exist two selections from `C`
with the same selection size `k` and the same total cost `k`, but opposite exactness verdicts.

### Construction

Use the same protected matrix as in `URI-N1`:

```text
L =
[e_1^T]
[⋮    ]
[e_r^T].
```

Choose the exact set

```text
E = {e_1^T, …, e_k^T}
```

and the fail set

```text
F = {e_2^T, …, e_r^T, e_{r+1}^T, …, e_{k+1}^T}.
```

Both are subsets of the same library `C`.
Both have cardinality `k`.
Because the costs are all `1`, both have total cost `k`.

Exactness holds for `E` because `row(L) ⊂ row(E)`.
Exactness fails for `F` because `e_1^T` is missing from `row(F)`.

### Conclusion

The same fixed candidate library and the same budget still permit opposite exactness verdicts.
So budget/count alone is not a complete exactness invariant, even before leaving a shared admissible sensor catalog.

## 5. URI-T3: Noisy weaker-versus-stronger separation

### Setup

Work on a restricted linear family `x = F z`.
Let the noisy record be

```text
y = O F z + e,  ||e||_2 ≤ η.
```

Assume:
- the weaker target satisfies `K O F = W F`,
- the stronger target has collision gap `Γ > 0` on the bounded family.

### Weak-target upper bound

Because `K O F = W F`, we have

```text
K y - W F z
= K(O F z + e) - W F z
= K e.
```

So

```text
||K y - W F z||_2 ≤ ||K||_2 ||e||_2 ≤ ||K||_2 η.
```

### Strong-target lower bound

Choose admissible coefficients `z, z'` realizing the stronger collision gap:

```text
O F z = O F z',
||S F z - S F z'||_2 = Γ.
```

Apply the same noise vector `e` to both states.
Then both noisy records are still equal:

```text
O F z + e = O F z' + e.
```

So any decoder outputs the same estimate on both.
One of the two strong-target errors must therefore be at least `Γ / 2`.

### Conclusion

For every noise level `η ≥ 0`:
- weaker target error is bounded above by `||K||_2 η`,
- stronger target worst-case error is bounded below by `Γ / 2`.

Hence the noisy hierarchy remains quantitatively separated whenever

```text
η < Γ / (2 ||K||_2).
```

## 6. Why this is the branch result worth keeping

The proof is elementary.
That is a strength, not a weakness.
It shows the branch limit sharply:
- universal exactness is factorization,
- but amount-only exact classifiers already fail on a very clean restricted class,
- and the failure survives both inside a fixed library and under noisy weaker-versus-stronger comparisons.

That makes `URI-N1`, `URI-N2`, and `URI-T3` much better branch results than a vague “different fields have different thresholds” slogan.
