# Indistinguishability Analysis Layer — Full Exploration Report

Status: **EXPLORATION / NON-PROMOTED**

Date: 2026-04-17  
Repository: `RRG314/Protected-State-Correction-Theory`

## 1) Scope and Constraint Compliance

This pass introduced an **indistinguishability analysis lane** for supported finite/sampled families and compared the resulting metrics against existing OCP/recoverability diagnostics.

Hard constraints were respected:

- no theorem promotion,
- no edits to theorem spine,
- no renaming or replacement of OCP/PVRT language,
- all outputs explicitly labeled exploration-only.

This lane is a sandbox diagnostic layer intended to test explanatory and classificatory value.

## 2) Core Formal Objects Used

For each system `(A, M, T)` in the sampled family:

- equivalence relation: `x ~ x'` iff `M(x) = M(x')`,
- record fiber: `Fib(y) = {x in A : M(x)=y}`,
- distinguishability failure: there exist `x != x'` in a common fiber with different target values.

Computed per system:

1. **Fiber size distribution**  
   max fiber size, mean fiber size, and histogram.
2. **Fiber mixedness**  
   number of distinct target values per fiber; percent mixed fibers.
3. **DLS (Distinguishability Loss Score)**  
   sampled estimate of `P(T(x) != T(x') | M(x)=M(x'))`.
4. **Fiber geometry diagnostics**  
   within-fiber target distance/variance and cluster counts.

## 3) Implementation Added

- Core metric engine: `src/ocp/indistinguishability.py`
- Exploration runner: `scripts/compare/run_indistinguishability_examples.py`
- Consistency test: `tests/examples/test_indistinguishability_examples_consistency.py`

The runner evaluates finite/sampled representatives for:

- restricted-linear same-rank exact/fail witnesses,
- periodic modal CFD-style truncation families,
- bounded-domain CFD-style observation families,
- MHD proxy observation families.

## 4) Coverage and Dataset

Total systems evaluated: **16**

- restricted-linear: 4
- periodic-cfd: 6
- bounded-cfd: 3
- mhd-proxy: 3

Primary artifact table:

- `data/generated/indistinguishability/indistinguishability_metrics.csv`

Required columns present:

- `system_id`, `family`, `rank`, `max_fiber_size`, `percent_mixed`, `DLS`, `kappa_0`, `Gamma_r`, `delta`
- plus support columns (`target_rank`, `exact_recoverable`, geometry fields, cluster labels, threshold-series keys).

## 5) Main Quantitative Results

From `indistinguishability_summary.json`:

- `DLS vs rank` correlation: **-0.571**
- `DLS vs kappa_0` correlation: **0.994**
- `DLS vs Gamma_r` correlation: **0.994**
- `DLS vs delta` correlation: **0.951**

Interpretation (exploratory):  
In this sampled set, DLS is tightly aligned with collision/fiber-gap structure (`kappa_0`, `Gamma_r`), and not reducible to rank alone.

## 6) Anti-Classifier and Threshold Findings

### A) Same-descriptor / opposite-loss behavior

The restricted-linear same-rank witness pairs display opposite DLS outcomes under equal rank-level descriptors:

- exact witness: `DLS = 0.0`
- fail witness: `DLS ~= 0.692`

This matches the intended anti-classifier stress direction of the lane.

### B) Augmentation-threshold-style drops

Detected large DLS drops with observation-family refinement:

- periodic full-modal series: `DLS drop = 1.0`, `delta drop = 2.0`
- bounded CFD observation family: `DLS drop = 1.0`, `delta drop = 2.0`
- MHD observation family: `DLS drop = 1.0`, `delta drop = 2.0`
- periodic low-mode functional: `DLS drop ~= 0.692`, `delta drop = 1.0`

These are exploratory threshold signatures, not promoted laws.

### C) Structural clustering

Systems separate into practical clusters (`low-loss/pure`, `moderate-loss`, `high-loss/mixed`) using DLS + mixedness + within-fiber target spread.

## 7) Anomaly Scan Results

Generated anomaly catalog:

- `data/generated/indistinguishability/indistinguishability_anomalies.csv`

Anomalies flagged: **16** across four types:

- `rank_predicts_success_but_dls_high`: 5
- `augmentation_threshold_dls_drop`: 4
- `low_rank_low_dls`: 4
- `high_dls_small_delta`: 3

This satisfies the requested automatic anomaly-detection layer.

## 8) Visual Artifacts Produced

- `figures/indistinguishability/dls_vs_rank.(png|pdf)`
- `figures/indistinguishability/dls_vs_delta.(png|pdf)`
- `figures/indistinguishability/fiber_size_histogram.(png|pdf)`
- `figures/indistinguishability/mixed_vs_pure_distribution.(png|pdf)`

These correspond directly to the required plot set.

## 9) Validation and Reproducibility

Executed and passed:

- `PYTHONPATH=src .venv/bin/python scripts/compare/run_indistinguishability_examples.py`
- `PYTHONPATH=src .venv/bin/pytest -q tests/examples/test_indistinguishability_examples_consistency.py`
- `python3 scripts/validate/check_links.py`
- `python3 scripts/validate/check_naming.py`
- `python3 scripts/validate/check_workbench_static.py`
- `python3 scripts/validate/check_visual_gallery.py`

## 10) Added Value Assessment

Requested success criteria (at least one) were met:

1. **Cases where DLS explains failures not captured by rank/budget:** yes (same-rank opposite-loss cases).  
2. **Threshold behavior tied to indistinguishability collapse:** yes (multiple large DLS drops with observation refinement).  
3. **New clustering not visible in simple descriptors:** yes (mixed/pure and loss-cluster grouping).  
4. **Cleaner anti-classifier interpretation:** yes (explicitly through fiber mixedness and DLS).

Current lane verdict:

- **Useful as an exploratory diagnostic layer.**
- **Not promoted to theorem status.**

## 11) Nonclaims

This report does **not** claim:

- new theorems,
- universal indistinguishability classifiers,
- replacement of OCP/PVRT core metrics,
- theorem-spine modifications.

All outputs remain **EXPLORATION / NON-PROMOTED**.

## 12) Artifact Index (Single-Path Access)

- Report (compact): `docs/research-program/indistinguishability_exploration.md`
- Report (this full document): `docs/research-program/indistinguishability_full_report.md`
- Metrics CSV: `data/generated/indistinguishability/indistinguishability_metrics.csv`
- Anomaly CSV: `data/generated/indistinguishability/indistinguishability_anomalies.csv`
- Summary JSON: `data/generated/indistinguishability/indistinguishability_summary.json`
- Plots: `figures/indistinguishability/`

