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
  - interpolation on the active sensor spectrum in the diagonal control family.

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
- the diagonal control threshold depends on interpolation on the active spectrum,
- the qubit threshold depends on which protected variable is chosen.

Current status:
- **not worth reviving** at the universal level
- family-specific complexity notions are still worth keeping

## 6. The Branch As A Major Standalone Theorem Program Today

Rejected form:
- the branch already supports a major new theorem program of its own.

Why it failed:
- the strongest general results remain standard or standard-adjacent,
- the strongest newer results are narrow family-level thresholds plus a restricted-linear threshold criterion,
- no stronger cross-domain theorem survived repeated falsification in this pass.

Current status:
- **keep as a serious branch**
- **do not promote as a major standalone theorem program yet**

## 7. Overly Narrow Control Threshold Wording

Rejected headline form:
- the control-side threshold is simply “the number of active sensed modes containing the protected coordinate.”

Why it failed:
- that wording is only the coordinate-recovery special case,
- the stronger surviving law is functional interpolation on the active sensor spectrum,
- weaker functionals such as `sensor_sum` or `first_moment` recover earlier than the protected coordinate.

Current status:
- **demote** the coordinate-only wording to a corollary
- **promote** the functional interpolation law instead

## 8. “Support Size Is The Threshold” Heuristic

Rejected form:
- minimal exact observation complexity is always the number of protected coordinates or modes that appear with nonzero weight.

Why it failed:
- in the periodic repeated-cutoff stress family, the protected functional `repeated_cutoff_mass` uses three nonzero modal coefficients but becomes exactly recoverable already at cutoff `2`, because all three coefficients live under the same retained cutoff level;
- in the diagonal control stress family, four-active protected functionals can have thresholds `1`, `2`, `3`, or `4`, depending on the minimal interpolation degree, even though every one of them has support size `4`.

What survives instead:
- periodic thresholds are governed by **visibility support**: the largest retained cutoff level among the protected modes;
- diagonal thresholds are governed by **interpolation complexity** on the active sensor spectrum;
- the clean shared invariant is row-space inclusion, not raw support counting.

Current status:
- **false as a general branch heuristic**
- **keep only as a family-specific shortcut when the observation family is literally coordinate-revealing**

## 9. “Rank(LF) Determines The Threshold” Heuristic

Rejected form:
- once `rank(O_r F) ≥ rank(L F)`, exact recovery should occur at that same level.

Why it failed:
- scalar protected variables always have `rank(L F)=1`, but their exact thresholds can still be much larger;
- in the diagonal control lane, horizon `2` already satisfies `rank(O_r F)=2 ≥ rank(L F)=1` while exact recovery of the protected coordinate still fails;
- the right invariant is whether the **specific protected row** lies in the observation row space, not whether the observation rank merely clears the protected rank.

Current status:
- **useful failure**
- **keep the rank bound only as a necessary condition**

## 10. Weak Directions To Leave Alone For Now

Leave these alone unless a sharply stronger idea appears:
- universal phase-transition language
- generic “measurement loses information” framing
- generic “coarse records cause irrecoverability” framing
- any attempt to make the qubit/control/periodic threshold mechanisms look more unified than the proofs support

## 11. Productive Failures Worth Preserving

These failures were useful and should remain visible:

1. the branch needed exact nullspace calculations, not only sampled collision scans
2. the strongest broad generalization attempt failed, which sharpened the branch scope
3. the universal complexity idea failed again, which pushed the branch toward cleaner family-specific thresholds
4. the coordinate-only control story was too narrow, which led to the stronger functional interpolation law
5. raw support-size and raw protected-rank heuristics failed, which forced the branch onto the row-space threshold law

## 12. Honest Bottom Line

The branch did not fail.

Several tempting bigger versions of it **did** fail.

That is good for the repo. It leaves behind:
- a cleaner theorem spine,
- a cleaner no-go spine,
- better validation discipline,
- and a much narrower set of claims that are actually worth keeping.
