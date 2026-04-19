# Positive Framework Buildout Options

This note is about implementation priorities, not new theorem claims.

Inputs used here:
- `docs/restricted-results/positive-recoverability/positive_theorem_candidates.md`
- `docs/restricted-results/positive-recoverability/positive_no_go_boundaries.md`
- `discovery/positive_framework_falsification_report.md`

## Option 1: restricted theorem note

Best use:
- package PT-1 through PT-4 with explicit assumptions and counterexamples.

Why it is viable:
- strongest theorem support already exists on the restricted class.

Recommendation:
- yes, immediate candidate.

## Option 2: design framework note

Best use:
- explain how `delta_free` and `delta_C` guide measurement augmentation decisions.

Why it is viable:
- useful for design choices and already backed by restricted-class evidence.

Recommendation:
- yes, immediate candidate.

## Option 3: diagnostic toolkit expansion

Best use:
- expand descriptor-lift diagnostics for opposite-verdict collision families.

Why it is viable:
- useful on supported families, but broad generalization is still conditional.

Recommendation:
- yes, with scope labels kept explicit.

## Option 4: workbench module

Best use:
- interactive defect detection and augmentation planning.

Risk:
- UI language can overstate novelty if not tightly scoped.

Recommendation:
- conditional.

## Option 5: augmentation planner

Best use:
- operational tool around `delta_free` and `delta_C`.

Recommendation:
- yes.

## Option 6: compatibility certificate library

Best use:
- reusable checks for CORS and ACRS membership on declared families.

Recommendation:
- yes.

## Option 7: measurement-design lane

Best use:
- branch-limited guidance for candidate-library selection and insufficiency checks.

Recommendation:
- conditional, keep it as scoped design guidance.

## Option 8: context-coherence analysis tool

Best use:
- detect local-exact/global-fail behavior and enlargement fragility.

Recommendation:
- yes.

## Practical order

1. restricted theorem note
2. augmentation planner and certificate library
3. context-coherence tooling
4. workbench module after claim-language review
