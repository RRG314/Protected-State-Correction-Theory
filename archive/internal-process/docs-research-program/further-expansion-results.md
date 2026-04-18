# Further Expansion Results (2026-04-16)

## Scope

This pass pushed the strongest surviving lanes after integration:
- alignment/kernel-row-space invariants,
- bounded-domain exactness vs obstruction,
- stability-vs-exactness separation,
- anti-classifier strengthening,
- family-enlargement and model-mismatch fragility,
- augmentation design limits,
- asymptotic operator-rate consequences.

All directions were handled falsification-first.

## Direction-by-Direction Outcomes

| Direction | Attempted statement | Status | What survived | What failed |
| --- | --- | --- | --- | --- |
| Stronger-than-rank alignment invariant | exactness controlled by row-space/kernel alignment rather than rank-only summaries | `PROVED` (restricted-linear classes) | `OCP-047`, `OCP-049`, `OCP-050` package survives and is operationally diagnostic | universal rank replacement across all branches is not proved |
| Bounded-domain exactness/obstruction classification | bounded exactness survives only on boundary-compatible family classes; naive transplant fails | `PARTIAL` (`PROVED` + `CONDITIONAL`) | `OCP-044` positive family theorem plus `OCP-023`/`OCP-028` no-go package | universal bounded-domain exact classifier remains open |
| Margin-protected stability vs instability | exact identifiability should be separated from stable inversion under perturbation/mismatch | `PARTIAL / OPEN` | `OCP-053` gives exact-data mismatch instability on canonical family | broad continuity-stability theorem is still open |
| Weighted/structured anti-classifier extension | same-budget anti-classifier should persist under weighted cost structures | `OPEN` | fixed-library unit-cost anti-classifier (`OCP-050`) is solid baseline | full weighted-cost theorem not yet proved |
| Family-enlargement failure taxonomy | exactness on small family can fail immediately on enlarged family | `PROVED` | `OCP-052` with explicit lower-bound witness survives | no full taxonomy beyond current restricted-linear constructions |
| Model-mismatch quantitative instability | mismatch error should be quantifiable despite exact identifiability per true family | `PROVED` | `OCP-053` closed-form mismatch floor survives brute-force checks | general nonlinear or infinite-family extension remains open |
| Minimal augmentation beyond baseline | extend `δ(O,L;F)` exact design law beyond current restricted-linear scope | `OPEN` | `OCP-045` remains strong and computable in current class | no theorem-grade generalization beyond supported linear family |
| Continuity-aware exact factorization | add continuity/stability criterion on top of factorization exactness | `OPEN` | factorization exactness remains clean (`OCP-030`, `OCP-048`) | continuity/stability layer still branch-open |
| Operator-rate asymptotic consequences | link asymptotic correction directly to spectral data | `PROVED` in current branch assumptions | `OCP-013`, `OCP-014`, `OCP-015`, `OCP-020` remain coherent and validated | no single universal rate law across all branch architectures |

## New/Strengthened Candidate Results From This Pass

1. Alignment-first anti-classifier package remains the strongest stronger-than-rank lane (`OCP-047`, `OCP-049`, `OCP-050`).
2. Family-enlargement false-positive and model-mismatch instability are now first-class fragility laws (`OCP-052`, `OCP-053`).
3. Bounded-domain lane now has an explicit positive theorem/no-go pair instead of negative-only framing (`OCP-044` with `OCP-023`/`OCP-028`).
4. Theory-level language is now constrained to branch-supported partial unification only.

## Explicit Disproof/Failure Preserved

- no rank-only exact classifier (`OCP-049`),
- no fixed-library budget-only exact classifier (`OCP-050`),
- family-enlargement false positives (`OCP-052`),
- exact-data mismatch instability (`OCP-053`),
- divergence-only bounded exact recovery failure (`OCP-028`),
- finite-time exact recovery no-go for smooth linear generator flow (`OCP-020`).

## Novelty Triage (Current Best Honest View)

- likely literature-known core: row-space/kernel exactness criteria, semigroup/spectral background, Hodge/topology machinery.
- repo framing of known facts: exact/asymptotic/impossible architecture with executable branch witnesses.
- plausibly literature-distinct package: integrated restricted-linear anti-classifier + family-enlargement + model-mismatch theorem bundle (`OCP-049` to `OCP-053`) with reproducible witness artifacts.

## Next Expansion Priorities

1. weighted-cost anti-classifier theorem (extension of `OCP-050`),
2. continuity/stability theorem layered on `OCP-030`/`OCP-048`,
3. broader bounded-domain theorem class beyond current finite-mode boundary-compatible family.
