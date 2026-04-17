# Final Architecture

## Plain-Language Summary

The finished architecture is branch-structured and falsification-first.

Primary branches:
1. exact projector branch
2. exact sector branch
3. exact periodic continuous projection anchor
4. asymptotic generator branch
5. bounded-domain/Hodge restricted exactness + obstruction branch
6. constrained-observation recoverability branch
7. fiber-based recoverability / impossibility limits branch
8. descriptor-fiber anti-classifier quantitative branch
9. cross-branch no-go boundary layer

This architecture is intentionally not a universal one-law system.

## 1. Exact Projector Branch

Objects:
- protected subspace `S`
- disturbance subspace `D`
- projector `P_S`

Output:
- one-step exact recovery on orthogonal split class

## 2. Exact Sector Branch

Objects:
- protected sector
- disturbance sector family
- sector projectors and sector-conditioned recovery

Output:
- exact sector recovery under orthogonality/distinguishability assumptions

## 3. Exact Periodic Continuous Anchor

Objects:
- divergence-free protected component
- gradient disturbance component
- periodic Leray/Helmholtz projector

Output:
- exact periodic continuous correction anchor

## 4. Asymptotic Generator Branch

Objects:
- generator `K`
- invariant split with stable disturbance restriction
- semigroup `e^{-tK}`

Output:
- asymptotic suppression
- explicit no finite-time exactness boundary in smooth linear-flow class

## 5. Bounded-Domain / Hodge Branch

Objects:
- bounded protected/disturbance classes
- boundary compatibility constraints
- domain-compatible Hodge/projector structures

Output:
- restricted bounded exact theorem (`OCP-044`)
- bounded transplant and divergence-only no-go boundaries (`OCP-023`, `OCP-028`)

## 6. Constrained-Observation Recoverability Branch

Objects:
- admissible family `A`
- record map `M` (`O` in restricted-linear form)
- protected target `p` (`L` in restricted-linear form)

Output:
- exact/approximate/asymptotic/impossible regime classification
- row-space/kernel compatibility criteria
- collision-gap threshold and minimal augmentation laws

## 7. Fiber-Based Recoverability / Impossibility Limits Branch

Objects:
- fibers of observation map
- target hierarchy/coarsening maps
- restricted family-enlargement and mismatch witnesses

Output:
- universal exact core: factorization/fiber constancy
- anti-classifier and false-positive limits above that core

## 8. Descriptor-Fiber Anti-Classifier Quantitative Branch

Objects:
- finite witness sets with exact/fail labels
- descriptor fibers
- compatibility refinement descriptors

Output:
- finite-class purity criterion for descriptor-only exactness
- irreducible descriptor-only error lower bound
- computed branch diagnostics (`DFMI`, `IDELB`, `CL`)

## 9. No-Go Boundary Layer

Cross-branch no-go outputs prevent overreach in:
- overlap ambiguity,
- sector overlap,
- finite-time exactness inflation,
- boundary-oblivious bounded projections,
- rank-only or budget-only exactness classifiers,
- family-blind exactness and mismatch-robustness claims.

## Architecture Claim Boundary

The architecture does **not** claim:
- one universal scalar recoverability/capacity law,
- one universal bounded-domain exact projection theorem,
- one universal theorem unifying all branches beyond supported assumptions.

## Final Architectural Outcome

The strongest honest statement is:

> Protected-State Correction Theory is a theorem-first, branch-structured program with exact and asymptotic correction anchors, constrained-observation and fiber-limit recoverability structure, bounded-domain obstruction discipline, and a strong no-go layer that enforces scope control.
