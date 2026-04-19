# Repo-Wide Geometry Audit (Falsification-First)

Date: 2026-04-16  
Scope: full OCP research repository with emphasis on theorem-bearing branches, no-go branches, and supported generated artifacts.

## Method

This pass used:
- theorem/proof registry (`OCP-001` through `OCP-053`),
- branch audits and open-problem notes,
- core implementation modules (`src/ocp/core.py`, `continuous.py`, `mhd.py`, `cfd.py`, `sectors.py`, `recoverability.py`, `fiber_limits.py`, `physics.py`),
- existing constrained-observation and fiber-branch reports,
- executable spot checks for key geometry-sensitive witnesses.

Falsification rule used in this pass:
- keep geometry only when it improves exactness criteria, no-go sharpness, obstruction structure, or attackability of open problems;
- reject geometry that only renames existing algebra without predictive gain.

## Geometry Already Present

Geometry is already central in the repo, but branch-dependent:
- subspace/projector geometry: exact orthogonal branch (`OCP-002`), overlap no-go (`OCP-003`), sector branch (`OCP-019`, `OCP-021`), Helmholtz/Leray branch (`OCP-006`, `OCP-027`), gauge-transverse corollary (`OCP-022`),
- operator geometry: generator block structure and mixing obstruction (`OCP-013`, `OCP-015`, `OCP-020`), row-space/kernel criteria (`OCP-031`, `OCP-040`, `OCP-045`),
- fiber/quotient geometry: exactness as fiber constancy (`OCP-030`), anti-classifier package (`OCP-047`, `OCP-049`, `OCP-050`), hierarchy and fragility (`OCP-048`, `OCP-051`, `OCP-052`, `OCP-053`),
- domain/boundary geometry: bounded-domain transplant failure (`OCP-023`) and boundary-compatible finite-mode Hodge exactness (`OCP-044`),
- gauge/orbit geometry: valid only on projection-compatible classes (`OCP-022`), not a universal branch merger.

## What Survives As Real Geometry

Survived strongly:
- projector/exactness geometry with explicit decomposition and operator formulas,
- boundary-sensitive obstruction geometry for bounded-domain correction,
- fiber/row-space/collision geometry explaining rank-only and budget-only failure,
- sector overlap geometry as exact-detection obstruction,
- generator block-geometry no-go (`P_S K P_D \neq 0`) for protected drift.

Survived conditionally:
- broader bounded-domain Hodge extension beyond explicit finite-mode class,
- gauge-orbit language beyond projection-compatible settings,
- asymptotic branch extension beyond invariant split assumptions.

Failed or rejected:
- universal amount-only/rank-only/budget-only geometry,
- boundary-insensitive projector transplantation,
- universal “one geometry fits all branches” claims,
- broad nonlinear fiber-curvature stories not supported by current admissible families.

## Global Geometry Verdict

1. Geometry is already theorem-bearing in this repo, not decorative.
2. The strongest geometric contribution lane is currently constrained-observation/fiber geometry plus anti-classifier/noisy-hierarchy results.
3. The most valuable geometry upgrade target is bounded-domain obstruction/classification, not universal unification.
4. Principal-angle/subspace-gap language can sharpen communication and diagnostics in restricted-linear branches, but is mostly equivalent to existing row-space residual logic.

## Novelty Tiering (Global)

Repo-new:
- synthesis of anti-classifier and false-positive theorem package with executable witnesses (`OCP-049`–`OCP-053`),
- bounded-domain positive+negative split integrated with explicit boundary diagnostics (`OCP-023`, `OCP-044`).

Likely literature-known:
- orthogonal projector exactness and overlap no-go in linear subspaces,
- Helmholtz/Hodge and transverse projection foundations,
- fiber-factorization exactness in abstract form,
- row-space/kernel equivalences in restricted linear recovery.

Literature-unclear:
- exact packaging of model-enlargement false-positive theorem (`OCP-052`) as a branch-level identifiability warning,
- exact packaging of fixed-library same-budget anti-classifier (`OCP-050`) in this theorem-first form.

Plausibly literature-distinct:
- the constrained, theorem-linked anti-universal package as a coherent lane (especially with explicit fixed-library witnesses + noisy weaker/stronger separation + model-mismatch exact-form witness).

## Next Steps

1. Promote a geometric obstruction formulation for bounded-domain exactness that explicitly couples divergence and boundary-trace compatibility classes.
2. Add a principal-angle/inclusion-defect diagnostic layer for same-rank witness families (without replacing existing row-space/collision invariants).
3. Keep gauge/orbit geometry narrow and projector-compatible; do not universalize.
4. Continue falsification-first weighted-cost and geometry-constrained anti-classifier work in the fiber branch.
