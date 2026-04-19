# Same-Rank Failure Geometric Invariant Report

Purpose: identify a geometry-based invariant that explains same-rank opposite exactness verdicts better than rank/count/budget language.

## Geometry Tested

1. Rank-only invariants: `rank(OF)`, `rank(LF)`, ambient dimension.
2. Row-space inclusion residuals already used in branch.
3. Principal-angle style inclusion defect between `row(LF)` and `row(OF)`.

## Proposed Invariant

For restricted-linear families `x=Fz`, define:

- `U = row(OF)` and `V = row(LF)` in coefficient space,
- `P_U` orthogonal projector onto `U`,
- `Q_V` orthonormal basis matrix for `V`.

Define geometric inclusion defect

```text
Δ_geom(O,L;F) := ||(I - P_U) Q_V||_2 = sin(θ_max(V,U)).
```

Interpretation:
- `Δ_geom = 0`: protected row space lies inside observed row space (exact class),
- `Δ_geom > 0`: protected directions leak outside observed row geometry (no exact recovery).

## Theorem Status on Supported Class

### Theorem (restricted-linear equivalence)

On the supported restricted-linear class,

```text
exact recoverability  <=>  row(LF) ⊆ row(OF)  <=>  Δ_geom = 0.
```

Status:
- `PROVED` as a geometric reformulation of existing exactness criterion (`OCP-031`).

## Same-Rank Opposite-Verdict Evidence

Representative witness (ambient 5, protected rank 2, observation rank 3):
- exact case: row-space residual `0`, collision gap `0`, `Δ_geom = 0`;
- fail case: row-space residual `1`, collision gap `2`, `Δ_geom = 1`.

Both have the same observation rank.
So rank does not classify exactness; geometric alignment does.

Across the branch witness suite:
- rank-only report: all tested levels admit same-rank opposite verdicts,
- fixed-library budget report: same size/same cost still gives opposite verdicts,
- geometric defect remains the separator when rank fails.

## What Survived

1. `Δ_geom` (or equivalent row-space residual) is the right geometric replacement for rank-only language in supported restricted-linear classes.
2. Collision-gap lower bounds add quantitative obstruction beneath the same geometric misalignment.

## What Failed

1. Any attempt to use rank-only invariants as complete classifier.
2. Any attempt to use fiber dimension alone as complete classifier.
3. Broad claim that principal-angle language creates a new theorem family by itself (it mostly restates existing exactness criterion).

## Novelty Tiering

Repo-new:
- explicit anti-classifier theorem package where geometric misalignment is made operational and artifact-backed.

Likely literature-known:
- subspace-angle/inclusion-defect equivalence itself.

Literature-unclear:
- exact packaging with fixed-library same-budget anti-classifier and collision-gap artifacts.

Plausibly literature-distinct:
- theorem/falsification integration for amount-failure claims on this supported restricted class.

## Next Steps

1. Add weighted-cost and constrained-library versions of `Δ_geom`-style classification tests.
2. Tie `Δ_geom` and collision-gap to robust perturbation margins (where possible) and fragility certificates (where not).
3. Keep reporting both geometry and no-go outputs together (avoid angle-only cosmetic reframing).
