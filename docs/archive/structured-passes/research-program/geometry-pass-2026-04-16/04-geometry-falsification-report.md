# Geometry Falsification Report

Purpose: record where geometry was tested and rejected, so only theorem-bearing geometry remains.

## Falsification Criteria Used

A geometry proposal was rejected if it was:
- only a rephrasing of existing algebra with no stronger criterion,
- weaker than existing theorem/no-go statements,
- uncomputable on supported families,
- unsupported by current admissible-family structure,
- predictive-equivalent to rank/count/budget-only statements,
- analogy without theorem consequence.

## Rejected Geometry Directions

### 1. Universal amount-geometry classifiers

Claim tested:
- rank/count/budget can be treated as geometric complexity that decides exactness.

Failure:
- contradicted by `OCP-047`, `OCP-049`, `OCP-050` and generated witness suites.

Verdict:
- rejected.

### 2. Boundary-oblivious projector geometry

Claim tested:
- periodic projector geometry can transplant unchanged to bounded domains.

Failure:
- explicit bounded-domain counterexample (`OCP-023`) with divergence cleanup but boundary-normal mismatch.

Verdict:
- rejected.

### 3. Divergence-only scalar geometry for bounded exact recovery

Claim tested:
- scalar divergence geometry is enough to recover bounded protected velocity class.

Failure:
- no-go `OCP-028` and CFD no-go formulations.

Verdict:
- rejected.

### 4. Broad geometric stability without margins

Claim tested:
- exact recoverability is robust under arbitrary small observation/subspace perturbation.

Failure:
- explicit epsilon-tilt witness destroys exactness at arbitrarily small perturbation (supported finite-dimensional class).

Verdict:
- rejected in broad form.

### 5. Universal gauge/orbit geometry claim

Claim tested:
- gauge/orbit geometry yields one unified exactness theorem across projection, CFD, QEC, constrained observation.

Failure:
- survives only on projection-compatible gauge projector classes; fails as global branch merger.

Verdict:
- rejected as universal claim.

### 6. Nonlinear fiber-curvature geometry (current repo scope)

Claim tested:
- smooth/curved fiber geometry can currently classify exactness across branches.

Failure:
- unsupported by current theorem stack and admissible-family implementations.

Verdict:
- deferred/open, not promoted.

### 7. “Everything is quotient geometry” synthesis

Claim tested:
- one quotient framing is enough to replace branch-specific criteria.

Failure:
- loses boundary conditions, operator constraints, and branch-specific obstruction content.

Verdict:
- rejected.

## Geometry That Survived Falsification

1. Subspace/projector geometry when operator and decomposition are explicit.
2. Boundary/domain geometry in bounded exactness/no-go analysis.
3. Fiber/quotient geometry for recoverability/impossibility hierarchy.
4. Row-space/collision-gap geometry for anti-classifier and threshold theorems.
5. Generator block/spectral geometry for asymptotic branch and mixing no-go.

## Novelty Tiering

Repo-new:
- explicit falsification packaging across rank-only, budget-only, family-enlargement, and model-mismatch branches.

Likely literature-known:
- individual rejection mechanisms in isolation (e.g., nonuniqueness from collisions, boundary mismatch logic).

Literature-unclear:
- exact theorem-falsification integration and artifact-backed branch boundaries.

Plausibly literature-distinct:
- this disciplined anti-overclaim scaffold as a cross-branch research method.

## Next Rejection Tests To Keep Running

1. Weighted-cost anti-classifier stress tests.
2. Perturbation fragility stress under richer family libraries.
3. Bounded-domain architecture mismatch tests beyond current modal families.
