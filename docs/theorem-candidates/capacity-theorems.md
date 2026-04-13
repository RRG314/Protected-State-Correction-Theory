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
