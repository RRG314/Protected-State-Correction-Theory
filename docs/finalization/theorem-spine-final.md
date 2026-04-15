# Final Theorem Spine

## Plain-Language Summary

This is the current promoted positive theorem spine of the repository.

It is still intentionally narrow. The strongest promoted results are:
- exact projector recovery,
- exact sector recovery,
- asymptotic generator recovery,
- the restricted-linear minimal augmentation theorem,
- and one restricted bounded-domain exact theorem on the repository's boundary-compatible finite-mode Hodge family.

Anything broader remains conditional, open, or explicitly demoted.

## Exact Branch

### OCP-T1: Exact Protected-Subspace Recovery
- Setup: `H = S ⊕ D`, `S ⟂ D`
- Result: orthogonal projection `P_S` recovers the protected component exactly.
- Role: finite-dimensional backbone.

### OCP-C1: Uniqueness Among Linear Recoveries
- Setup: same as OCP-T1.
- Result: any linear map fixing `S` and annihilating `D` agrees with `P_S`.
- Role: tells the exact projector branch there is essentially one linear recovery operator once the split is fixed.

### OCP-T5: Exact Sector Recovery For Orthogonal Sector Embeddings
- Setup: protected space `S`, pairwise orthogonal sector family `D_i`, coordinate-compatible embeddings.
- Result: a single sector-conditioned operator recovers each sector exactly.
- Role: exact sector branch and strongest bridge to QEC.

## Asymptotic Branch

### OCP-T2: Continuous Damping Theorem
- Setup: `x_dot = -k P_D x`, `k > 0`.
- Result: `S` stays fixed, `D` decays exponentially.
- Role: simplest exact-to-asymptotic bridge.

### OCP-T3: Invariant-Split Generator Theorem
- Setup: `K|_S = 0`, `K(D) ⊆ D`, stable restriction on `D`.
- Result: `x_dot = -Kx` preserves `S` and suppresses `D` asymptotically.
- Role: strongest general positive theorem in the continuous branch.

### OCP-C2: Self-Adjoint PSD Corollary
- Setup: self-adjoint PSD `K` with `ker(K)=S` and positive spectral gap on `S^⊥`.
- Result: explicit decay bound.
- Role: cleanest ready-to-cite continuous corollary.

## Minimum-Structure Layer

### OCP-T4: Exact Correction Rank Lower Bound
- Setup: exact linear recovery `R` on `V = S ⊕ D`.
- Result: `rank(I-R) >= dim(D)` and `rank(R) >= dim(S)`.
- Role: minimum correction image theorem in the exact linear branch.

### OCP-T6: Restricted-Linear Minimal Augmentation Theorem
- Setup: restricted linear family `x = F z`, record `O F z`, protected variable `L F z`.
- Result: the minimum number of unrestricted added linear measurements needed for exact recovery is `δ(O, L; F) = rank([O F; L F]) - rank(O F)`.
- Role: first finished category-specific capacity theorem in the restricted-linear design branch.

## Restricted Bounded-Domain Exact Layer

### OCP-T7: Boundary-Compatible Finite-Mode Hodge Projection
- Setup: bounded-domain family built from boundary-compatible divergence-free stream modes and Dirichlet gradient modes.
- Result: the orthogonal projector onto the protected bounded family is exact on that family.
- Role: restricted but real partial solution to the bounded-domain exact-correction problem.

## What Is Deliberately Not In The Final Theorem Spine

The following stay out of the final positive theorem spine:
- any universal scalar capacity theorem,
- any full control-theory theorem beyond the invariant-split branch,
- any claim that GLM is exact,
- any optimizer/ML theorem,
- any broad boundary-sensitive exact PDE theorem beyond the solved finite-mode bounded Hodge subcase,
- and any attempt to count the Maxwell / gauge extension as a new theorem rather than a corollary-level physics fit of the exact projector branch.

## Finished Assessment

This theorem spine is now finished enough to support outside review because each promoted statement has:
- a clean statement,
- explicit assumptions,
- operator-level meaning,
- and executable support in the repository.
