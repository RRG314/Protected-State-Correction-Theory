# Geometry Theorem Candidate Assessment

This file attempts the requested theorem-grade candidates in falsification-first mode.

Status labels used:
- `PROVED`: derivation already supported by current theorem spine/tests/artifacts.
- `CONDITIONAL`: true on explicit supported classes, open in broader form.
- `DISPROVED`: explicit counterexample or theorem-level obstruction exists.
- `OPEN`: no decisive proof/disproof in current supported scope.

## Candidate Results

| Candidate | Proof Attempt | Disproof Attempt | Verdict | Notes |
| --- | --- | --- | --- | --- |
| 1. Principal-angle exactness/no-go criterion on supported finite-dimensional families | In restricted-linear families, exactness `row(LF) \subseteq row(OF)` is equivalent to zero inclusion defect `\Delta_\angle := \|(I-P_{row(OF)})Q_{row(LF)}\|_2 = \sin(\theta_{max})`; tested on same-rank witnesses where exact case gives `0` and fail case gives `1`. | Tried to find exact case with nonzero `\Delta_\angle`; no such case under current exact criterion. | `PROVED` (as reformulation) | Geometrically sharper than rank-only phrasing, but algebraically equivalent to existing row-space criterion (`OCP-031`, `OCP-047`, `OCP-049`). |
| 2. Geometric replacement invariant for same-rank insufficiency | Replacement invariant `\Delta_\angle` (or row-space residual) separates same-rank opposite verdicts: exact witness has `\Delta_\angle=0`; fail witness has `\Delta_\angle=1`; rank is equal in both. | Tried amount-only/rank-only alternatives; contradicted by existing anti-classifier theorems and witness suites. | `PROVED` (restricted-linear class) | This is the clean geometric explanation of `OCP-047`, `OCP-049`, `OCP-050`. |
| 3. Boundary-geometry obstruction theorem for bounded-domain exact correction | Existing proofs/counterexamples already show divergence-only and periodic-transplant failure when boundary-compatible protected class is required (`OCP-023`, `OCP-028`). | Tried to salvage boundary-oblivious exactness; explicit bounded counterexample rejects it. | `PROVED` (obstruction form) | Strong no-go lane: boundary geometry is not optional metadata. |
| 4. Hodge-compatible exactness theorem on broader explicit bounded families | Existing theorem `OCP-044` proves exactness on boundary-compatible finite-mode Hodge families; tests support. | Tried broad unconstrained bounded-domain extension; not yet proved in repo. | `CONDITIONAL` (broad), `PROVED` (finite-mode class) | Positive theorem survives narrowly; broader theorem remains open. |
| 5. Quotient/fiber reformulation of weaker-vs-stronger target exactness | Existing coarsening theorem package (`q=\phi\circ p`) and noisy hierarchy theorem (`OCP-048`, `OCP-051`) already establish quotient/fiber target hierarchy. | Tried converse (exact coarsening implies exact stronger target); explicit branch counterexamples disprove. | `PROVED` (forward), `DISPROVED` (converse) | Useful geometry survives precisely as hierarchy, not equivalence. |
| 6. Geometric stability under small subspace/operator perturbations | Positive case holds under stronger assumptions (e.g., full-row observation or explicit margins). | Broad claim fails: exact restricted-linear case can be destroyed by arbitrarily small row-space tilt (`eps=1e-8` gives nonzero residual and exactness failure). | `DISPROVED` (broad), `CONDITIONAL` (with extra margins) | Important fragility result: exactness is typically boundary-of-class property, not automatically robust. |
| 7. Geometric collapse theorem for protected-target distortion under coarse observation | Collapse-modulus and collision-gap theorems already provide quantitative collapse law (`OCP-035`, `OCP-043`, `OCP-046`). | Tried to find coarse-observation regime with positive collision gap but no lower-bound obstruction; not found on supported classes. | `PROVED` (supported classes) | Strong theorem-grade operational geometry already present. |
| 8. Gauge-orbit exactness theorem on projection-compatible classes | Maxwell/Coulomb-gauge transverse projection is an exact corollary of projector class (`OCP-022`). | Tried universal gauge-orbit extension beyond projection-compatible classes; unsupported and blocked by domain/boundary dependence. | `PROVED` (projection-compatible), `OPEN/unsupported` (broad) | Keep as corollary lane, not unifying master theorem. |

## Additional Candidate Attempt (Derived During Pass)

### 9. Generic perturbation fragility of exact row-space inclusion

Statement attempted:
- In non-full-row settings, exact restricted-linear recoverability is not open under arbitrary small observation perturbations.

Attempt outcome:
- supported by explicit witness: for `L=[1,0,0]`, exact at `O=[[1,0,0],[0,1,0]]`, but exactness fails for `O_\varepsilon=[[1,0,\varepsilon],[0,1,0]]` for any `\varepsilon>0` tested down to `1e-8`.

Status:
- `PROVED` as a no-go style fragility statement on supported finite-dimensional class.

Usefulness:
- blocks overconfident “small perturbation keeps exactness” language.

## Novelty Tiering (Candidate Set)

Repo-new:
- explicit theorem-level packaging of anti-classifier + fragility + false-positive geometry in one branch stack.

Likely literature-known:
- principal-angle reformulation itself,
- quotient/fiber forward monotonicity,
- basic perturbation fragility of inclusion constraints.

Literature-unclear:
- exact combination of anti-classifier + fixed-library budget + noisy weaker/stronger split in this form.

Plausibly literature-distinct:
- theorem/falsification package as a coherent limits program, if written narrowly and honestly.

## What Survived vs Failed

Survived:
- geometric reformulations that sharpen exactness/no-go diagnostics,
- boundary obstruction geometry,
- fiber/quotient hierarchy geometry,
- collision-gap collapse geometry.

Failed:
- broad geometric stability claims without margin assumptions,
- broad gauge-geometry unification claims.

## Next Theorem Targets

1. Weighted-cost geometric anti-classifier extension of `OCP-050`.
2. Explicit robustness theorem with geometric margin hypotheses (instead of broad perturbation stability slogans).
3. Boundary-geometry theorem that couples divergence and boundary traces in one exactness criterion family.
