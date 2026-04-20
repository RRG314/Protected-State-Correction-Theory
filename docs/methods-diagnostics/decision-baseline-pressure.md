# Decision-Baseline Pressure Report

## Scope

This note compares amount-only descriptor experiments against augmented structural descriptor experiments on declared datasets.

The comparison is decision-facing and restricted. It is not a universal Blackwell-deficiency theorem.

## Baseline definitions

For each dataset lane:

- amount code experiment: quantized tuple of
  `(standard_entropy, standard_mi_state, standard_fisher_trace, standard_rank)`.
- augmented code experiment: amount tuple plus
  `(compatibility_defect, tfcd, ambiguity_index)`.
- target: binary success/failure label from the lane definition.

Computed quantities:

- `amount_bayes_error`: Bayes 0-1 error from amount-code experiment.
- `augmented_bayes_error`: Bayes 0-1 error from augmented-code experiment.
- `risk_reduction_augmented_vs_amount = amount_bayes_error - augmented_bayes_error`.
- `decision_regret_amount_vs_context`: amount-code regret against full-context labels.

## Current artifact

- `data/generated/structural-information-theory/decision_baseline_comparison.csv`
- `data/generated/structural-information-theory/decision_practical_comparison.csv`
- `data/generated/structural-information-theory/diagnostic_failure_catalog.csv`

## Current results

All scored lanes show positive risk reduction from augmented descriptors:

| Dataset | Amount Bayes Error | Augmented Bayes Error | Risk Reduction |
| --- | ---: | ---: | ---: |
| `ocp_rank_witness` | 0.5000 | 0.0000 | 0.5000 |
| `information_real_system` | 0.1790 | 0.0617 | 0.1173 |
| `gravity_recoverability` | 0.2864 | 0.1636 | 0.1227 |
| `gravity_blackhole_only` | 0.2593 | 0.1667 | 0.0926 |
| `external_uci_wine_quality` | 0.1855 | 0.1662 | 0.0192 |
| `external_uci_magic_gamma` | 0.2671 | 0.2173 | 0.0498 |
| `external_uci_ionosphere` | 0.1054 | 0.0627 | 0.0427 |
| `external_uci_spambase` | 0.1865 | 0.1389 | 0.0476 |
| `external_uci_sonar` | 0.1987 | 0.1122 | 0.0865 |
| `external_uci_wdbc` | 0.0482 | 0.0359 | 0.0123 |

Mean risk reduction across scored lanes: `0.1091`.
Median risk reduction across scored lanes: `0.0682`.

## Practical classifier pressure (failure-aware)

A second comparison uses 5-fold cross-validation with simple practical models on amount vs augmented descriptors:

- nearest-centroid classifier
- kNN (`k=5`) classifier

Result summary from `decision_practical_comparison.csv`:

- kNN: augmented better on 7 datasets, worse on 2 datasets, tied on 1 dataset.
- nearest-centroid: augmented better on 2 datasets, worse on 1 dataset, tied on 7 datasets.

Explicit scalar-outperforms-augmented failures are recorded in:
- `diagnostic_failure_catalog.csv`

Current failure rows:
- `information_real_system`: kNN amount-only outperforms augmented.
- `gravity_recoverability`: kNN amount-only outperforms augmented.
- `external_uci_magic_gamma`: nearest-centroid amount-only slightly outperforms augmented.

## Interpretation boundary

What this supports:
- amount-only summaries can be decision-insufficient on declared lanes,
- structural augmentation can reduce Bayes decision error in declared lanes,
- practical classifier gains are not universal and can reverse in some regimes.

What this does not support:
- a universal superiority theorem for all datasets,
- a full comparison-of-experiments ordering across unrestricted model classes.
