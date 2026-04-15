# Constrained-Observation Failures and Dead Ends

## Purpose

This note records the branch directions that failed, weakened materially under testing, or should not be promoted.

It is part of the branch on purpose. The branch only stays credible if weak results are not quietly blended into the clean-results layer.

## 1. Broad Cross-Domain Phase-Transition Claim

Rejected form:
- there is one strong general phase-transition theorem governing recoverability under coarsening across the quantum, PDE, and control anchors.

Why it failed:
- the anchor systems do show threshold-like behavior,
- but the mechanisms are family-specific,
- and the current results reduce to different underlying structures:
  - fiber collisions in the qubit family,
  - Fourier support loss in the periodic modal family,
  - Vandermonde/history rank loss in the diagonal control family.

Current status:
- **not worth promoting** as a broad theorem claim

## 2. `κ` As An Automatically Novel Invariant

Rejected form:
- the collapse modulus `κ_{M,p}` is already a major new theory object.

Why it failed:
- `κ(0)=0` is the right exactness criterion,
- `κ(η)/2` is useful,
- but most of the surrounding logic remains close to existing inverse-stability and recoverability language.

Current status:
- **keep**, but only as a useful branch quantity
- **do not oversell** as automatic novelty

## 3. Sampled Collision Estimates As Final Evidence

Rejected form:
- discrete sampling of admissible state pairs is enough to classify exact versus impossible recovery.

Why it failed:
- the first control pass understated the horizon-1 obstruction,
- because the worst collision sits in the continuum nullspace structure, not necessarily on a coarse state grid.

What replaced it:
- exact nullspace-on-a-box collision calculations in the finite-dimensional linear families.

Current status:
- **sampling alone is not trustworthy** for exact/no-go claims

## 4. “Any Coarse Record Gives A Smooth Degradation Story”

Rejected form:
- every coarsening family produces a smooth recoverability collapse.

Why it failed:
- several anchor families show actual exact/no-go threshold jumps,
- while others show stable approximation or asymptotic recovery instead,
- and some observables are simply dead on arrival for the chosen protected variable.

Current status:
- **false as a general branch statement**

## 5. Observation Complexity As A Universal Scalar Capacity

Rejected form:
- there is one scalar record-complexity number that captures recoverability across all branch systems.

Why it failed:
- the periodic modal threshold depends on protected Fourier support,
- the diagonal control threshold depends on active sensed modes and distinct eigenvalues,
- the qubit threshold depends on which protected variable is chosen.

Current status:
- **not worth reviving** at the universal level
- family-specific complexity notions are still worth keeping

## 6. The Branch As A Major Standalone Theorem Program Today

Rejected form:
- the branch already supports a major new theorem program of its own.

Why it failed:
- the strongest general results remain standard or standard-adjacent,
- the strongest newer results are narrow family-level thresholds,
- no stronger cross-domain theorem survived repeated falsification in this pass.

Current status:
- **keep as a serious branch**
- **do not promote as a major standalone theorem program yet**

## 7. Weak Directions To Leave Alone For Now

Leave these alone unless a sharply stronger idea appears:
- universal phase-transition language
- generic “measurement loses information” framing
- generic “coarse records cause irrecoverability” framing
- any attempt to make the qubit/control/periodic threshold mechanisms look more unified than the proofs support

## 8. Productive Failures Worth Preserving

These failures were useful and should remain visible:

1. the branch needed exact nullspace calculations, not only sampled collision scans
2. the strongest broad generalization attempt failed, which sharpened the branch scope
3. the universal complexity idea failed again, which pushed the branch toward cleaner family-specific thresholds

## 9. Honest Bottom Line

The branch did not fail.

Several tempting bigger versions of it **did** fail.

That is good for the repo. It leaves behind:
- a cleaner theorem spine,
- a cleaner no-go spine,
- better validation discipline,
- and a much narrower set of claims that are actually worth keeping.
