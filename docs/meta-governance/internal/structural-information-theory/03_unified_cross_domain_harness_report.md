# Unified Cross-Domain Reduction Harness Report

Date: 2026-04-19  
Harness: `scripts/research/run_structural_information_harness.py`

## Purpose

Provide one reproducible local harness that stress-tests structural-information claims across:
- OCP restricted witness classes,
- imported information real-system metrics,
- imported gravity recoverability lanes,
- decision-baseline compression regret checks,
- stability and coarse-graining checks.

## Inputs

- `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv`
- `data/imported/structural-information-theory/real_system_metrics.csv`
- `data/imported/structural-information-theory/gravity_recoverability_metrics.csv`

## Outputs

- `data/generated/structural-information-theory/unified_cross_domain_reduction_metrics.csv`
- `data/generated/structural-information-theory/out_of_family_anti_classifier.csv`
- `data/generated/structural-information-theory/decision_baseline_comparison.csv`
- `data/generated/structural-information-theory/coarse_graining_monotonicity.csv`
- `data/generated/structural-information-theory/stability_checks.csv`
- `data/generated/structural-information-theory/harness_summary.json`

## Key results

1. Amount-only anti-classifier baseline remains positive in all scored lanes (`IDELB > 0`).
2. Compatibility-augmented profile lowers IDELB in all scored lanes.
3. Independent out-of-family survivor present:
   - `information_real_system` (`CL_rel = 0.6552`).
4. Decision compression regret (amount descriptors vs full-context labels) is positive in all scored datasets.
5. Restricted stability bounds hold in all configured perturbation checks.
6. Coarse-graining defect monotonicity holds in synthetic theorem sanity chain and imported Hawking-surrogate trends.

## Evidence table

| Dataset | Baseline IDELB | Augmented IDELB | CL_rel | Status |
| --- | ---: | ---: | ---: | --- |
| `ocp_rank_witness` | 0.5000 | 0.0000 | 1.0000 | SURVIVES |
| `information_real_system` | 0.1790 | 0.0617 | 0.6552 | SURVIVES (independent out-of-family) |
| `gravity_recoverability` | 0.2864 | 0.1636 | 0.4286 | SURVIVES |
| `gravity_blackhole_only` | 0.2593 | 0.1667 | 0.3571 | SURVIVES |

## Boundary notes

- Decision-baseline file uses a compression-regret proxy, not a complete Blackwell deficiency implementation.
- Coarse-graining physics entries are surrogate-lane validations, not universal theorem claims.
- No universal scalar metric claim is made.
