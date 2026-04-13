# Final Architecture

## Plain-Language Summary

The finished OCP architecture is now explicit:
- exact projector branch,
- exact sector branch,
- exact continuous projector anchor,
- asymptotic continuous generator branch,
- and a formal no-go boundary around the whole program.

This is the main architectural cleanup that makes the repository reviewable.

## 1. Exact Projector Branch

This is the narrowest and cleanest branch.

Objects:
- protected subspace `S`
- disturbance subspace `D`
- orthogonal projector `P_S`

Output:
- one-step exact recovery

Main theorem:
- OCP-T1

## 2. Exact Sector Branch

This branch handles systems where disturbance is not one complementary subspace but a family of distinguishable sectors.

Objects:
- protected space `S`
- sector family `D_i`
- sector projectors `Q_i`
- sector-conditioned recovery architecture

Output:
- exact recovery sector by sector

Main theorem:
- OCP-T5

Main anchor:
- QEC bit-flip example

## 3. Exact Continuous Projector Anchor

This branch is still exact, but now in a continuous/PDE-like setting.

Objects:
- divergence-free protected subspace
- gradient disturbance space
- Leray/Helmholtz projector

Output:
- exact continuous correction on the periodic tested branch

Main anchor:
- periodic Helmholtz/Leray projection

## 4. Asymptotic Continuous Generator Branch

This branch handles systems where exact one-shot projection is unavailable or not the right architecture.

Objects:
- protected kernel `S = ker(K)` or invariant protected coordinates
- disturbance family `D`
- generator `K`
- semigroup `e^{-tK}`

Output:
- asymptotic suppression, not exact finite-time annihilation

Main theorems:
- OCP-T2
- OCP-T3
- OCP-C2

Main boundary:
- OCP-N7

## 5. No-Go Boundary Layer

The no-go layer applies across all branches.

It rules out:
- overlap and ambiguity,
- insufficient correction image,
- mixing into protected coordinates,
- sector overlap,
- and false promotion of smooth damping as exact recovery.

## 6. What The Architecture Does Not Claim

The final architecture deliberately does **not** claim:
- universal correction theory across all systems,
- full theorem-complete control theory,
- full theorem-complete boundary-sensitive PDE theory,
- or a universal scalar capacity invariant.

## 7. Physics Extension

The strongest honest physics extension now sits alongside, not above, the main theory.

Kept physics lanes:
- Maxwell / Coulomb-gauge projection as an exact projector-compatible extension,
- numerical-relativity constraint damping as a conditional asymptotic extension,
- continuous quantum error correction as a conditional future bridge.

Rejected or demoted physics lanes:
- naive bounded-domain reuse of the periodic projector,
- generic constrained Hamiltonian systems without an explicit correction operator.

## Final Architectural Outcome

The strongest honest global statement is now:

> Protected-State Correction Theory is a finished framework with an exact projector branch, an exact sector branch, an exact periodic continuous anchor, an asymptotic generator branch, a strong no-go layer, and a disciplined physics extension.
