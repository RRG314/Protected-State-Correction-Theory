# Constrained-Observation / Fiber-Geometry Report

Focus target: constrained-observation geometry and recoverability under coarse records.

## Geometry Tested

1. Fiber geometry:
- exactness as target constancy on observation fibers,
- impossibility as target-mixed fibers,
- target coarsening as quotient/factor map.

2. Operator geometry in restricted-linear families:
- kernel inclusion `ker(OF) \subseteq ker(LF)`,
- row-space inclusion `row(LF) \subseteq row(OF)`,
- collision-gap geometry on bounded coefficient families.

3. Same-rank insufficiency geometry:
- does any geometry stronger than raw rank separate opposite verdicts?

## What Survived

### A. Fiber exactness backbone (`OCP-030`)

Survives as branch backbone:
- exact recoverability iff target is fiber-constant.

### B. Quantitative collapse geometry (`OCP-035`, `OCP-043`, `OCP-046`)

Survives strongly:
- lower-bound obstruction from collision/collapse geometry,
- exact-regime upper envelope when exact decoder exists,
- threshold behavior via nested collision-gap laws.

### C. Same-rank failure with geometric separator (`OCP-047`, `OCP-049`)

Survives strongly:
- same rank can produce opposite exactness verdicts,
- geometric alignment (row-space inclusion defect) separates cases.

Spot-check witness:
- exact and fail cases have equal observation rank,
- exact case residual/gap `0`, fail case residual `1`, gap `2`,
- principal-angle inclusion defect `0` vs `1`.

### D. Weaker-vs-stronger quotient hierarchy (`OCP-048`, `OCP-051`)

Survives as theorem-grade structure:
- weaker target can remain exact/stable while stronger target remains impossible on same record geometry.

## What Failed

1. Rank-only / count-only / budget-only language as exactness classifier.
2. Claim that one universal scalar record complexity governs all families.
3. Broad nonlinear fiber-geometry extrapolation from restricted-linear evidence.

## Geometric Invariant Outcome

Most useful invariant in this branch remains:
- inclusion defect between protected and observation row spaces (equivalently row-space residual / collision-gap package),
not:
- raw rank,
- raw measurement count,
- raw budget.

## Novelty Tiering

Repo-new:
- anti-classifier + noisy hierarchy + family-enlargement + model-mismatch package in one branch.

Likely literature-known:
- abstract fiber exactness and kernel/row-space equivalence statements.

Literature-unclear:
- exact strength and packaging of anti-classifier theorem bundle in current restricted class.

Plausibly literature-distinct:
- the branch-level, executable theorem/falsification pipeline around same-rank failure and target hierarchy.

## Next Targets

1. Weighted-cost geometric anti-classifier theorem.
2. Robust noisy extension under admissible-family enlargement.
3. Restricted nonlinear class test: theorem extension or clean theorem-failure.
