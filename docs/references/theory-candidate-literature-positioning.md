# Theory Candidate Literature Positioning (2026-04-16)

## Candidate Under Positioning

Working candidate after lens integration:
- **Restricted recoverability-structure theory** for protected targets under constrained observation, centered on alignment/kernel/fiber/collision-gap/augmentation invariants.

This is positioned as a branch-limited candidate, not a universal correction theory.

## Literature Comparison Axes

| Axis | Literature baseline | Candidate relation |
| --- | --- | --- |
| Exact recoverability as factorization/fiber constancy | statistics/sufficiency and coding/inference baselines (`shannon_1948`, `jencova_petz_2006`, `junge_renner_sutter_wilde_winter_2018`) | mostly standard core; candidate does not claim novelty here |
| Restricted-family recoverability and nullspace structure | compressed sensing/observability-style structural criteria (`donoho_2006`, `candes_romberg_tao_2006`, `villaverde_2019`) | candidate aligns strongly, but adds OCP-specific regime and no-go packaging |
| Stability and inverse mismatch language | inverse-problem stability and identifiability (`alberti_capdeboscq_privat_2020`, `villaverde_2019`) | candidate currently partial; strongest stability claims remain scoped/open |
| Subspace/alignment diagnostics | principal-angle and perturbation machinery (`bjorck_golub_1973`, `davis_kahan_1970`) | candidate uses these as computable invariants surpassing rank-only summaries |
| Bounded-domain/topology obstruction | Hodge/de Rham/topology background (`arnold_falk_winther_2006`, `hatcher_2002`) | candidate integrates these into branch-specific exact/no-go gates |

## Novelty Triage for the Candidate

### Likely literature-known components
- factorization/fiber exactness principle itself,
- row-space/kernel equivalence for linear exact recovery,
- classical semigroup and Hodge machinery.

### Repo framing of known components
- explicit exact/approximate/asymptotic/impossible regime language tied to protected-target design,
- explicit demotion of amount-only/rank-only/budget-only claims by theorem-backed witnesses.

### Plausibly literature-distinct candidate components
- theorem package formed by `OCP-049` to `OCP-053` on restricted-linear families,
- family-enlargement false-positive law (`OCP-052`) coupled to collision-gap lower bounds,
- canonical model-mismatch instability law (`OCP-053`) with exact-data mismatch quantification,
- integrated theorem + generated-witness + workbench-evidence stack preserving scope labels.

## Why This Is Not Yet a Full New Theory Lane

- cross-branch positive laws remain heterogeneous,
- bounded-domain/topology lane is not yet merged into one broader theorem class,
- stability lane (exact-but-unstable vs stably recoverable) is still open.

Hence current decision remains:
- partial theory candidate survives,
- repo identity should not be renamed around a new universal brand.

## Promotion Language Guardrails

Allowed:
- "partial, branch-limited theory candidate"
- "restricted recoverability-structure lane"
- "operator/FA-backed strengthening"

Not allowed:
- "universal unified recoverability theory"
- "everything reduces to quotient geometry"
- "novel factorization principle" (without strict qualification)

## Next Literature-Facing Work

1. Formal comparison note against structural observability and identifiability baselines for `OCP-049` to `OCP-053`.
2. Explicit boundary/topology comparison note for bounded-domain exactness/no-go package (`OCP-023`, `OCP-028`, `OCP-029`, `OCP-044`).
3. Stability-lane survey and proof attempt for continuity-aware factorization criterion.
