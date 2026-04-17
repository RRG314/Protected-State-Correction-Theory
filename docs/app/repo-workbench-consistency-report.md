# Repo-Workbench Consistency Report (2026-04-16)

## Purpose

Verify that workbench wording and evidence levels match the integrated theorem/no-go state.

## Audit Scope

Reviewed:
- Structural Discovery Studio,
- Discovery Mixer / Structural Composition Lab,
- Benchmark / Validation Console,
- theorem/no-go linked module labels,
- scenario export evidence levels,
- generated validation snapshots and known-results matrices.

## Consistency Checks

| Check | Result | Notes |
| --- | --- | --- |
| Canonical evidence taxonomy present in export layer | pass | `scenarioExports.js` maps to `theorem-backed`, `restricted theorem-backed`, `validated family-specific`, `benchmark empirical` |
| Same-rank insufficiency reflected in tool surfaces | pass | constrained/mixer cases retain opposite-verdict same-rank witnesses (`OCP-047`) |
| Anti-classifier and fragility language present without overclaiming | pass | no rank-only / no budget-only / family-enlargement / mismatch limits remain branch-scoped |
| Bounded-domain warning language retained | pass | transplant-failure no-go and boundary-compatible restricted exact path are both visible |
| Exact vs asymptotic split retained | pass | continuous generator lane and control lane preserve finite-time no-go vs asymptotic behavior |
| Unsupported honesty preserved | pass | unsupported custom symbolic inputs remain explicitly rejected in mixer/studio |
| Branch flattening avoided | pass | workbench remains module- and family-scoped |

## Mismatches Found and Resolution

1. Pre-regeneration artifacts still contained older evidence strings.
- Resolution: regenerate via full validation gate (`run_all`) from updated source layers.

2. Some branch-internal status strings remain richer than the canonical four-level taxonomy.
- Resolution: allowed as secondary explanatory text, as long as exported evidence levels and canonical docs remain normalized.

## Current Alignment Verdict

Workbench is now aligned with repo-level promoted claims under the current branch restrictions.

What the workbench does not do:
- it does not claim universal symbolic coverage,
- it does not upgrade validated family-specific behavior to universal theorem status,
- it does not hide no-go boundaries behind optimistic recommendations.

## Traceability Links

- module map: `docs/app/module-theory-map.md`
- terminology: `docs/overview/terminology-unification.md`
- notation: `docs/overview/notation-unification.md`
- validation results: `docs/validation/full-integration-validation-results.md`
