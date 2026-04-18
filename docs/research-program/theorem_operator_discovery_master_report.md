# Theorem/Operator Discovery Master Report

Status: theorem-first formalization + operator/projection/equation discovery pass.

Artifacts produced in this pass:
- `docs/research-program/formal_core_definitions.md`
- `docs/research-program/theorem_candidates_formalized.md`
- `docs/research-program/no_go_candidates_formalized.md`
- `discovery/operator_candidates.md`
- `discovery/projection_candidates.md`
- `discovery/equation_candidates.md`
- `data/generated/operator_discovery/operator_witness_catalog.csv`
- `data/generated/operator_discovery/operator_anomaly_catalog.csv`
- `discovery/operator_test_notes.md`
- `discovery/operator_falsification_report.md`
- `docs/research-program/new_math_literature_audit.md`
- `docs/research-program/new_math_overlap_table.md`
- `docs/research-program/theorem_operator_ranked_results.md`

## Executive verdict

Final class: **CONDITIONAL THEOREM PACKAGE + OPERATOR CANDIDATES**.

Interpretation:
- theorem/no-go core is strong and sharpened,
- operator/projection/equation discovery yielded useful diagnostics,
- no broad genuinely new operator theory survived.

## 1. What exact theorem package should be pushed now?

Push now:
1. conditioned-vs-invariant split existence,
2. descriptor-only insufficiency no-go,
3. positive shared augmentation threshold existence (with explicit admissibility class).

Scope label:
- `PROVED ON SUPPORTED FAMILY`.

## 2. What exact no-go package should be pushed now?

Push now:
1. no amount-only exact classifier,
2. projection-sufficiency failure for shared decoder feasibility,
3. bounded-domain divergence-only insufficiency (CFD branch),
4. restricted variable-`eta` obstruction (MHD branch).

## 3. Did any genuinely new operator survive?

Short answer:
- not as a distinct theorem object.

Detail:
- AGO is useful and somewhat additive computationally,
- SDCO/CLE/CID mostly reduce to existing feasibility/compatibility logic.

## 4. Did any genuinely new projection method survive?

No new projection method survived as distinct mathematics.
What survived is a strong negative: stack row-space projection is insufficient for shared exactness (`491` witness cases in operator catalog).

## 5. Did any genuinely new equation survive?

No broad new equation survived.
The main equation outcome is formalization of context-lift feasibility and augmentation-threshold equations with strict scope.

## 6. What collapsed into existing OCP logic?

Collapsed/reduced:
- SDCO, CLE, CID as “new operators,”
- most projection candidates,
- broad new-operator novelty claims.

## 7. What is useful mathematically even if not novel?

Useful outputs:
- canonical formal definitions,
- theorem/no-go normalization,
- augmentation and compatibility diagnostics,
- large witness/anomaly catalogs for reproducible pressure testing.

## 8. Which 1–3 results are most worth immediate formal paper development?

1. context-sensitive split + anti-classifier theorem/no-go package,
2. augmentation-threshold bounds (proof closure target),
3. restricted MHD obstruction theorem package.

## 9. Which exploratory operator/projection ideas deserve a second pass?

Second-pass candidates:
1. AGO with admissibility-class-specific lower/upper bounds,
2. conditioning-aware robustness diagnostics (not classifier),
3. geometry-tagged compatibility functionals for CFD/MHD cross-lane comparisons.

## 10. Which ideas should be dropped now?

Drop now:
- claims of a new standalone operator/projection theory,
- universal projection law claims,
- novelty claims that are row-space/fiber restatements.

## Quantitative summary from discovery artifacts

From `data/generated/operator_discovery/summary.json` and catalogs:
- witness rows: `1000`,
- anomaly rows: `26`,
- local-exact/global-fail: `267`,
- same-descriptor opposite-verdict groups: `23`,
- projection-sufficient-but-invariant-fail cases: `491`.

## Best serious next move after theorem/operator discovery

Recommendation: **(2) push augmentation theorem and bounds before all else**.

Reason:
- split and anti-classifier theorem package is already strong on supported families,
- promotion bottleneck is closed-form/tight augmentation threshold characterization,
- operator discovery did not produce stronger immediate publishable novelty than that theorem closure step.
