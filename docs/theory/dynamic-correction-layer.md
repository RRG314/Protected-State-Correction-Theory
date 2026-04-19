# Dynamic Correction Layer

## Scope

This layer addresses time-dependent recovery/suppression: finite-time impossibility, asymptotic correction rates, and repeated-observation threshold behavior.

Primary sources:
- [`src/ocp/continuous.py`](../../src/ocp/continuous.py)
- [`src/ocp/next_phase.py`](../../src/ocp/next_phase.py)
- [`data/generated/next-phase/dynamic_accumulation.csv`](../../data/generated/next-phase/dynamic_accumulation.csv)
- [`data/generated/next-phase/generator_dynamics.csv`](../../data/generated/next-phase/generator_dynamics.csv)

## Promoted Dynamic Statements

### DYN-1: Finite-time exact recovery no-go for smooth linear generator flow
Status: `PROVED` (`OCP-020`).

No finite positive time can produce exact cancellation of generic disturbance components in the linear smooth-flow class.

### DYN-2: Asymptotic suppression with spectral margin
Status: `PROVED` (`OCP-013`, `OCP-014`).

For split-preserving generators with strictly stable disturbance block, disturbance norm decays exponentially at a spectral-margin-governed rate.

### DYN-3: Canonical repeated-observation threshold (finite history)
Status: `VALIDATED` (explicit branch witness).

In the canonical accumulation family, exact recoverability appears only after the 4th observation block. Before that, row-space residual remains positive.

Evidence:
- `exact_threshold_step = 4` in [`dynamic_accumulation.csv`](../../data/generated/next-phase/dynamic_accumulation.csv).

### DYN-4: Generator rate tracking bound
Status: `VALIDATED` (canonical branch witness).

For canonical flow witness:
- finite-time exact recovery remains false,
- bound is respected at all sampled times,
- disturbance-to-bound ratio decreases from `1.0` to about `0.708` over `t in [0,3]`.

Evidence:
- [`generator_dynamics.csv`](../../data/generated/next-phase/generator_dynamics.csv).

## Disproved/Unresolved Dynamic Narratives

- "finite-time exactness can be recovered by smooth linear evolution" -> `DISPROVED` in branch class (`OCP-020`).
- "one universal history-length law across all branches" -> `OPEN`.
- "observation-with-time always improves to exactness in finite horizon" -> `DISPROVED` in general; depends on record architecture.

## Domain Tie-In

This dynamic layer is intentionally connected to:
- asymptotic generator branch (operator-semigroup lane),
- repeated-record constrained-observation lane (history threshold lane),
- CFD/GLM asymptotic suppression interpretation (branch-scoped, not universalized).

## Literature Positioning

- likely literature-known foundations: semigroup and spectral theory ([Pazy 1983], [Engel-Nagel 2000]).
- repo framing: exact/no-go/rate separation with executable branch witnesses and theorem-ID-coupled diagnostics.

## Next Dynamic Targets

1. prove explicit horizon lower bounds for broader restricted-linear history families (`OPEN`),
2. quantify perturbation-to-rate sensitivity in generator branch (`OPEN`),
3. bridge dynamic thresholds to minimal augmentation laws (`OPEN`).
