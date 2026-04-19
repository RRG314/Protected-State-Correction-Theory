# Final Universal Core Theorems

Date: 2026-04-17

## UCT-1 — Exact Recoverability by Factorization / Fiber Constancy

Let `A` be an admissible family, `T : A -> Z` a target, and `M : A -> Y` a record map.
The following are equivalent:
1. `T` is exactly recoverable from `M` on `A`.
2. `T` is constant on every fiber of `M` over `A`.
3. `T` factors through `M` on `A`.

Status: `PROVED`.

## UCT-2 — Collision No-Go

Under the same setup, if there exist `x,x' in A` with `M(x)=M(x')` and `T(x) != T(x')`, then no exact recovery map for `T` from `M` exists on `A`.

Status: `PROVED`.

## UCT-3 — Coarsening Monotonicity (Core-Adjacent)

If `q = phi ∘ T` and `T` is exactly recoverable from `M` on `A`, then `q` is exactly recoverable from `M` on `A`.
The converse need not hold.

Status: `PROVED` (forward implication and converse-failure package).

## Universal-Core Boundary Note

These theorems define the universal core. Stronger statements involving rank/budget anti-classifiers, family enlargement, mismatch, domain topology, and symmetry quotient are promoted only in branch-limited packages.
