# Indistinguishability Exploration

Status: **EXPLORATION / NON-PROMOTED**

This lane adds a finite-family indistinguishability analysis layer to supported OCP/recoverability families.
It is diagnostic only and does not modify theorem status, theorem spine, or promotion decisions.

## Definitions Used

- Equivalence relation: `x ~ x'` iff `M(x) = M(x')`.
- Fiber: `Fib(y) = {x in A : M(x)=y}`.
- Mixed fiber: a fiber containing more than one distinct target value.
- Distinguishability Loss Score (DLS): estimated probability that two states with the same record have different targets.

## Families Covered

| Family | Systems |
| --- | ---: |
| restricted-linear | 4 |
| periodic-cfd | 6 |
| bounded-cfd | 3 |
| mhd-proxy | 3 |

## Comparison to Existing Metrics

| Comparison | Pearson correlation |
| --- | ---: |
| DLS vs rank | -0.571 |
| DLS vs kappa_0 | 0.994 |
| DLS vs Gamma_r | 0.994 |
| DLS vs delta | 0.951 |

Interpretation for this pass: DLS is strongly coupled to fiber-collision metrics (`kappa_0`, `Gamma_r`) and only partially aligned with rank and augmentation count.
That behavior is expected for an indistinguishability-based diagnostic and is kept exploratory.

## Anomaly Cases (Automatic Flags)

Flag count: **16**

| System | Type | Severity | Details |
| --- | --- | --- | --- |
| restricted_linear_same_rank_exact_n5_r2_k2 | low_rank_low_dls | MEDIUM | rank=2.0, DLS=0.000 |
| restricted_linear_same_rank_fail_n5_r2_k2 | rank_predicts_success_but_dls_high | HIGH | rank=2.0, target_rank=2.0, DLS=0.692 |
| restricted_linear_same_rank_fail_n5_r2_k2 | high_dls_small_delta | MEDIUM | delta=1.0, DLS=0.692 |
| restricted_linear_same_rank_fail_n6_r2_k3 | rank_predicts_success_but_dls_high | HIGH | rank=3.0, target_rank=2.0, DLS=0.692 |
| restricted_linear_same_rank_fail_n6_r2_k3 | high_dls_small_delta | MEDIUM | delta=1.0, DLS=0.692 |
| periodic_modal_cutoff_1_low_mode_sum | rank_predicts_success_but_dls_high | HIGH | rank=1.0, target_rank=1.0, DLS=0.692 |
| periodic_modal_cutoff_1_low_mode_sum | high_dls_small_delta | MEDIUM | delta=1.0, DLS=0.692 |
| periodic_modal_cutoff_2_low_mode_sum | low_rank_low_dls | MEDIUM | rank=2.0, DLS=0.000 |
| bounded_cfd_divergence_only_bounded_observation | rank_predicts_success_but_dls_high | HIGH | rank=2.0, target_rank=2.0, DLS=1.000 |
| bounded_cfd_protected_projected_bounded_observation | low_rank_low_dls | MEDIUM | rank=2.0, DLS=0.000 |
| mhd_mhd_divergence_only_observation | rank_predicts_success_but_dls_high | HIGH | rank=2.0, target_rank=2.0, DLS=1.000 |
| mhd_mhd_Helmholtz_projected_observation | low_rank_low_dls | MEDIUM | rank=2.0, DLS=0.000 |
| periodic_modal_cutoff_4_full_modal_coefficients | augmentation_threshold_dls_drop | HIGH | series=periodic_modal_full_modal_coefficients, DLS drop=1.000, delta drop=2.0 (periodic_modal_cutoff_2_full_modal_coefficients -> periodic_modal_cutoff_4_full_modal_coefficients) |
| periodic_modal_cutoff_2_low_mode_sum | augmentation_threshold_dls_drop | HIGH | series=periodic_modal_low_mode_sum, DLS drop=0.692, delta drop=1.0 (periodic_modal_cutoff_1_low_mode_sum -> periodic_modal_cutoff_2_low_mode_sum) |
| bounded_cfd_full_bounded_state_observation | augmentation_threshold_dls_drop | HIGH | series=bounded_cfd_observation_family, DLS drop=1.000, delta drop=2.0 (bounded_cfd_divergence_only_bounded_observation -> bounded_cfd_full_bounded_state_observation) |
| mhd_mhd_full_field_observation | augmentation_threshold_dls_drop | HIGH | series=mhd_observation_family, DLS drop=1.000, delta drop=2.0 (mhd_mhd_divergence_only_observation -> mhd_mhd_full_field_observation) |

## Threshold Behavior

The following transitions show the largest DLS drops tied to observation-family changes.

| Series | From -> To | DLS drop | delta drop |
| --- | --- | ---: | ---: |
| periodic_modal_full_modal_coefficients | periodic_modal_cutoff_2_full_modal_coefficients -> periodic_modal_cutoff_4_full_modal_coefficients | 1.000 | 2.0 |
| bounded_cfd_observation_family | bounded_cfd_divergence_only_bounded_observation -> bounded_cfd_full_bounded_state_observation | 1.000 | 2.0 |
| mhd_observation_family | mhd_mhd_divergence_only_observation -> mhd_mhd_full_field_observation | 1.000 | 2.0 |
| periodic_modal_low_mode_sum | periodic_modal_cutoff_1_low_mode_sum -> periodic_modal_cutoff_2_low_mode_sum | 0.692 | 1.0 |
| periodic_modal_full_modal_coefficients | periodic_modal_cutoff_1_full_modal_coefficients -> periodic_modal_cutoff_2_full_modal_coefficients | 0.000 | 1.0 |

## Highest-DLS Systems

| System | Family | Rank | DLS | percent mixed | delta |
| --- | --- | ---: | ---: | ---: | ---: |
| periodic_modal_cutoff_1_full_modal_coefficients | periodic-cfd | 1 | 1.000 | 100.0% | 3.0 |
| periodic_modal_cutoff_2_full_modal_coefficients | periodic-cfd | 2 | 1.000 | 100.0% | 2.0 |
| bounded_cfd_divergence_only_bounded_observation | bounded-cfd | 2 | 1.000 | 100.0% | 2.0 |
| mhd_mhd_divergence_only_observation | mhd-proxy | 2 | 1.000 | 100.0% | 2.0 |
| restricted_linear_same_rank_fail_n5_r2_k2 | restricted-linear | 2 | 0.692 | 100.0% | 1.0 |

## Lane Assessment

Assessment: **adds exploratory predictive signal (non-promoted)**

Current readout: indistinguishability metrics provide clearer failure interpretation and anti-classifier diagnostics on sampled families.
The lane remains exploratory and non-promoted until additional families and stress checks are completed.

## Artifacts

- `data/generated/indistinguishability/indistinguishability_metrics.csv`
- `data/generated/indistinguishability/indistinguishability_anomalies.csv`
- `data/generated/indistinguishability/indistinguishability_summary.json`
- `figures/indistinguishability/dls_vs_rank.png`
- `figures/indistinguishability/dls_vs_delta.png`
- `figures/indistinguishability/fiber_size_histogram.png`
- `figures/indistinguishability/mixed_vs_pure_distribution.png`

> Label reminder: EXPLORATION / NON-PROMOTED.
