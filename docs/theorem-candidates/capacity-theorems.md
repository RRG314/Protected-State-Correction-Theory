# Capacity Theorems

## Plain-Language Summary

The OCP program needed something stronger than “this correction architecture works in a nice case.” It also needed lower bounds on how much correction structure is required.

This file develops the cleanest version of that idea now supported by the repository.

## Theorem OCP-T4: Exact Linear Correction Rank Lower Bound

Let `V = S ⊕ D` be a finite-dimensional vector space with a linear exact recovery map `R : V -> V` satisfying

```text
R(s + d) = s
```

for all `s in S`, `d in D`.

Define the associated correction operator

```text
C = I - R.
```

Then:

```text
R|_S = I_S,
R|_D = 0,
C|_S = 0,
C|_D = I_D.
```

In particular,

```text
rank(R) >= dim(S),
rank(C) >= dim(D).
```

### Proof

Because `R(s+0)=s`, one has `R|_S = I_S`. Because `R(0+d)=0`, one has `R|_D = 0`.

Then for `C = I - R`:
- `C(s)=0` for `s in S`,
- `C(d)=d` for `d in D`.

So the image of `C` contains `D`, giving `rank(C) >= dim(D)`. Likewise the image of `R` contains `S`, giving `rank(R) >= dim(S)`.

## Corollary OCP-C3: Rank-Deficient Exact Correction Is Impossible

Under the same setup, if a proposed linear correction operator `C` has

```text
rank(C) < dim(D),
```

then it cannot serve as the correction part of an exact OCP recovery architecture on `(S,D)`.

This is one of the cleanest minimum-structure results in the repository.

## Proposition OCP-P4: Sector Distinguishability Lower Bound

Consider an exact sector-based correction architecture with nonzero disturbance sectors

```text
D_1, ..., D_m
```

that are pairwise orthogonal and are to be corrected exactly by a sector-conditioned recovery rule.

Then any exact architecture must distinguish at least `m` sectors. In particular, any syndrome or correction-label space must have cardinality at least `m`.

### Status Note

This proposition is conceptually straightforward, but still presented in a modest form because the repository does not yet formalize a full abstract measurement model beyond the QEC anchor.

## Category-Specific Capacity View

The repo now supports the following grounded capacity picture:
- exact linear branch: minimum correction rank at least `dim(D)`
- QEC branch: minimum distinguishable sector count at least the number of mutually orthogonal correctable sectors
- generator branch: stable disturbance dimension under protected-state preservation
- PDE branch: still incomplete, but naturally tied to the reachable constrained-error mode family

This is not a universal scalar invariant, but it is a real structural improvement over the earlier all-in-one capacity language.

## Theorem OCP-T6: Restricted-Linear Minimal Augmentation Theorem

Let the admissible family be

```text
A = { x = F z : z ∈ R^r }
```

with orthonormalized family basis `F`. Let the current record be `M(x) = O x` and the protected variable be `p(x) = L x`.

Define the restricted row-space deficiency

```text
δ(O, L; F) = rank([O F; L F]) - rank(O F).
```

Then:

1. Any exact recovery architecture obtained by adding `k` unrestricted linear measurements to `O` must satisfy

```text
k ≥ δ(O, L; F).
```

2. There exists an augmentation by exactly `δ(O, L; F)` unrestricted linear measurements for which exact protected-variable recovery becomes possible.

Equivalently, `δ(O, L; F)` is the minimum number of unrestricted added measurements required to make `L F` lie in the augmented observation row space.

### Proof

Let `O_aug F` be the restricted observation matrix after adding `k` measurements.

Exact recovery requires

```text
row(L F) ⊆ row(O_aug F),
```

so

```text
rank(O_aug F) ≥ rank([O F; L F]).
```

Each added measurement contributes at most one new restricted row-space dimension, hence

```text
rank(O_aug F) ≤ rank(O F) + k.
```

Combining the two gives

```text
k ≥ rank([O F; L F]) - rank(O F) = δ(O, L; F).
```

This proves necessity.

For sufficiency, choose any basis of a complement of `row(O F)` inside `row([O F; L F])`. Its dimension is exactly `δ(O, L; F)`. Add one unrestricted measurement for each complement basis row. Then the augmented restricted row space contains `row([O F; L F])`, hence contains `row(L F)`, so exact restricted-linear recovery follows from the row-space criterion.

### Status

`PROVED`

### Why This Matters

This is the first genuinely finished branch-specific capacity invariant beyond lower bounds alone:
- it does not revive the failed universal scalar-capacity story,
- it gives an exact minimum-augmentation count in the restricted linear design layer,
- and it turns a practical “what extra measurements do I need?” question into a clean theorem.

## Corollary OCP-C7: Below-Deficiency Augmentation Is Impossible

Under the same setup, any proposal to add fewer than `δ(O, L; F)` unrestricted linear measurements cannot yield exact protected-variable recovery on the admissible family.

### Status

`PROVED`
