# Terminology Unification

Date: 2026-04-17
Status: Canonical vocabulary reference

## Purpose

This file defines preferred terms across README, theory docs, workbench copy, validation reports, and papers.

## Core Terms (Canonical)

| Canonical term | Meaning | Typical branch scope |
| --- | --- | --- |
| protected state / protected target | The component, variable, or functional that must be preserved/recovered | all branches |
| disturbance / ambiguity | Unwanted component or indistinguishable variation relative to current observation/correction structure | all branches |
| observation / record map (`M`) | Map from state to measured/available record | recoverability/fiber branches |
| correction architecture | Operator/process proposed to suppress disturbance while preserving protected content | exact/asymptotic/operator branches |
| recoverability | Ability to reconstruct target from record on a declared admissible family | recoverability/fiber branches |
| exact | Zero-error reconstruction/correction under branch assumptions | all branches |
| approximate | Nonzero bounded error regime | recoverability + empirical branches |
| asymptotic | Converges toward protected object as time/iterations increase | generator/damping branches |
| impossible / no-go | Exact recovery/correction cannot hold under declared assumptions | no-go layer |
| admissible family | Explicit set/class on which a theorem or validation statement is made | all theorem-grade branches |
| fiber | Preimage class of equal records under `M` | fiber branch |
| factorization | Existence of `R` such that `T = R ∘ M` on admissible family | universal core |
| anti-classifier result | No exact classifier from amount-only metadata (rank/count/budget) on declared class | branch-limited strengthening |
| family enlargement | Expansion of admissible family that may invalidate exactness | fiber-limits branch |
| model mismatch | Decoder built for one family evaluated on another | fiber-limits branch |
| branch-limited theory | Results that are exact only within explicit branch assumptions | unifying framework |
| Structural Discovery Studio | Workbench module for diagnosis/fix comparison and regime movement | app/workbench |
| Discovery Mixer / Structural Composition Lab | Workbench module for typed composition, compatibility checks, and repair search | app/workbench |
| Benchmark / Validation Console | Workbench module for demo replay, health checks, and exportable evidence | app/workbench |

## Evidence/Status Labels (Canonical)

Use only:
- `PROVED`
- `PROVED ON SUPPORTED FAMILY`
- `CONDITIONAL`
- `VALIDATED`
- `OPEN`
- `ANALOGY ONLY`
- `REJECTED`

Workbench evidence tags may additionally use:
- `theorem-backed`
- `restricted theorem-backed`
- `validated family-specific`
- `benchmark empirical`
- `unsupported`

## Alias Resolution

| Use instead of | Preferred term |
| --- | --- |
| “amount solves recoverability” | “amount-only heuristics fail on restricted classes” |
| “universal correction law” | “branch-limited structural criteria” |
| “just rank” | “row-space/kernel compatibility or fiber collision structure” |
| “model works in general” | “works on the declared admissible family” |
| “same information” | “same count/rank/cost metadata” |

## Style Rules

1. Do not use “universal” unless the statement is explicitly in the universal core set.
2. Do not use “exact” for asymptotic damping behavior.
3. Do not use “recoverable” without naming the target and admissible family.
4. Distinguish “validated” from “proved” in all summaries.

## Canonical Cross-References

- `docs/overview/notation-unification.md`
- `docs/unifying_theory/final_theory_identity.md`
- `docs/unifying_theory/theorem_hierarchy_final.md`
- `docs/repo_cleanup/canonical_document_map.md`
