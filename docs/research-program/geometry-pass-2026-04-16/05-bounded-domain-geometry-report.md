# Bounded-Domain Geometry Report

Focus target: bounded-domain exact projection / Hodge / CFD geometry.

## Geometry Tested

1. Domain-sensitive decomposition geometry:
- bounded protected class with boundary trace constraints,
- disturbance class as compatible gradient modes,
- exactness tied to the actual bounded-domain projector.

2. Boundary-normal/tangential structure:
- whether correction preserves protected boundary-normal behavior,
- whether divergence-only criteria miss boundary class violations.

3. Hodge-compatible finite-mode geometry:
- stream-mode and gradient-mode orthogonality under bounded assumptions,
- sampled projector consistency checks.

## What Survived

### A. Boundary-compatible finite-mode Hodge exactness (`OCP-044`)

Survives as proved restricted theorem:
- exact correction on explicit bounded families where protected and disturbance spaces are domain-compatible and orthogonal.

Observed support (spot check):
- recovery error near machine scale,
- orthogonality residual near machine scale,
- boundary-compatible recovered state.

### B. Boundary-sensitive obstruction (`OCP-023`, `OCP-028`)

Survives strongly:
- divergence cleanup without boundary compatibility is not exact bounded correction,
- divergence-only factorization cannot recover nontrivial bounded protected class.

Tracked counterexample values (spot check):
- physical boundary-normal RMS: `~2.30e-32`,
- projected boundary-normal RMS after periodic transplant: `~3.11e-2`,
- post-projection divergence RMS: near machine scale.

This is a genuine geometric obstruction: exactness fails by boundary class mismatch, not by divergence residual alone.

## What Failed

1. Naive periodic-to-bounded transplant as exact correction architecture.
2. Scalar divergence geometry as complete exactness invariant for bounded protected classes.
3. Any boundary-agnostic exactness criterion.

## Theorem Status (Bounded-Domain Lane)

- Boundary-compatible finite-mode Hodge exactness: `PROVED`.
- Boundary-oblivious periodic transplant exactness: `DISPROVED`.
- Divergence-only bounded exact recovery: `PROVED NO-GO`.
- Broad bounded-domain exactness classification beyond finite-mode class: `CONDITIONAL` / `OPEN`.

## Obstruction Theory Upgrade (Current Pass)

Surviving obstruction principle:
- exact bounded correction requires compatibility with both divergence structure and boundary class geometry.
- preserving one without the other is insufficient.

This upgrade is mathematically stronger than a transplant warning because it identifies the missing geometric constraint class, not just one failed operator.

## Novelty Tiering

Repo-new:
- clean positive/negative split inside bounded-domain lane with explicit theorem + counterexample pairing.

Likely literature-known:
- Hodge decomposition foundations and boundary-sensitive projection issues in CFD/PDE settings.

Literature-unclear:
- exact branch-level theorem/no-go packaging under OCP claim IDs and validation artifacts.

Plausibly literature-distinct:
- the exact way bounded-domain obstruction is used to delimit transplant claims in a theorem-first correction framework.

## Next Bounded-Domain Targets

1. Prove a broader bounded-domain exactness criterion with explicit admissible boundary data classes.
2. Formalize a boundary-obstruction theorem family that certifies impossibility from boundary-trace mismatch patterns.
3. Extend finite-mode positive class cautiously (without claiming full bounded-domain closure).
