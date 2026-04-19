# New Structure Discovery Report

Status: **EXPLORATION / NON-INTEGRATED**

This pass intentionally avoids repository theory integration and focuses on falsification-first structure search.

## Scope

Focused lanes:

1. Causal inference / invariant prediction
2. Multi-terminal / distributed observation
3. Data-driven control / Willems-style trajectory recovery
4. Measurement sensitivity / Fisher geometry
5. Optional localized defect structure

## Phase 1 — New formal objects

Objects tested:

- Context-Invariance Defect (CID)
- Partition Synergy Index (PSI)
- Intervention Lift (IL)
- Target Sensitivity Floor (TSF)
- Recovery Frontier Size (RFS)

Each object was evaluated against novelty tests that target failures of rank/count descriptors.

## Phase 2 — Witness generation

Total witness systems generated: **175**

Witness counts by lane:

- `causal_inference`: 30
- `localized_defect`: 6
- `measurement_sensitivity`: 5
- `multi_terminal`: 55
- `target_lattice`: 12
- `willems_data_driven`: 67

Rows with exactness labels: **169** (exact=94, fail=75)

## Phase 3 — Anomaly detection

Detected anomalies: **18**

Top anomaly families:

- `same_descriptor_opposite_verdict`: 9
- `intervention_vs_observation`: 6
- `distributed_structure_over_amount`: 1
- `measurement_type_over_count`: 1
- `one_measurement_flip`: 1

Representative anomalies:

- `same_descriptor_split_0` (causal_inference): Rank/count descriptor fails to classify recoverability. Evidence: causal_inference|1|1|1|1|1
- `same_descriptor_split_1` (causal_inference): Rank/count descriptor fails to classify recoverability. Evidence: causal_inference|1|1|1|1|2
- `same_descriptor_split_2` (multi_terminal): Rank/count descriptor fails to classify recoverability. Evidence: multi_terminal|2|2|2|2|1
- `same_descriptor_split_3` (willems_data_driven): Rank/count descriptor fails to classify recoverability. Evidence: willems_data_driven|4|2|2|1|1
- `same_descriptor_split_4` (willems_data_driven): Rank/count descriptor fails to classify recoverability. Evidence: willems_data_driven|2|2|2|1|2
- `same_descriptor_split_5` (measurement_sensitivity): Rank/count descriptor fails to classify recoverability. Evidence: measurement_sensitivity|1|1|1|1|1
- `same_descriptor_split_6` (target_lattice): Rank/count descriptor fails to classify recoverability. Evidence: target_lattice|1|1|1|1|1
- `same_descriptor_split_7` (multi_terminal): Rank/count descriptor fails to classify recoverability. Evidence: multi_terminal|2|2|2|1|1
- `same_descriptor_split_8` (multi_terminal): Rank/count descriptor fails to classify recoverability. Evidence: multi_terminal|3|3|2|1|1
- `threshold_flip_chain_good_1_2` (multi_terminal): Single-measurement increments can trigger discontinuous exactness transitions. Evidence: exact 0 -> 1
- `intervention_lift_causal_obs_0` (causal_inference): Measurement type dominates measurement count. Evidence: residual_obs=0.09950371902099892, residual_itv=0.0
- `intervention_lift_causal_obs_1` (causal_inference): Measurement type dominates measurement count. Evidence: residual_obs=0.19611613513818404, residual_itv=0.0

## Phase 4 — Pattern extraction

- CID range across context families: min=2.22045e-16, max=0.769231.
- PSI range across multi-terminal families: min=-0.111111, max=0.692308.
- Fisher sensitivity floor range: min=0, max=4 at fixed measurement count.

## Phase 5 — Prove / disprove pressure

- `Context-architecture incompatibility theorem (supported family)`: **PROVED** — found 11 fail and 11 exact descriptor-matched context witnesses
- `Distributed arrangement anti-classifier theorem (supported family)`: **PROVED** — descriptor groups with opposite verdicts: 1
- `CID separation conjecture`: **CONDITIONAL** — CID threshold accuracy=22/22
- `Sensitivity-floor no-go`: **PROVED** — zero-floor models=1, nonzero-floor models=4
- `Naive amount-only claim`: **DISPROVED** — counterexamples found in causal, multi-terminal, and Willems lanes

Proof/disproof status distribution:

- `PROVED`: 3
- `CONDITIONAL`: 1
- `DISPROVED`: 1

## Phase 6 — Novelty filter

- `Context-Invariance Defect (CID)`: **KEPT** — CID separates invariant exact vs fail on descriptor-matched context families; captures architecture constraint absent from amount-only descriptors.
- `Partition Synergy Index (PSI)`: **KEPT** — Distributed partition anomalies detected; positive-PSI exactness rate=0.300.
- `Intervention Lift (IL)`: **KEPT** — Intervention lifted recoverability in 18 matched-count families.
- `Target Sensitivity Floor (TSF)`: **KEPT** — TSF cleanly separates sensitivity-blind vs sensitivity-resolving families at fixed count.
- `Recovery Frontier Size (RFS)`: **KEPT** — Reveals partial-recovery lattice structure (weak recoverable, strong impossible).

Objects kept after novelty filter: **5/5**.

## Phase 7 — Candidate standalone framework

Working title: **Structured Recoverability Geometry (SRG)**

Core components:

1. CID for multi-context architecture constraints.
2. PSI for distributed partition effects.
3. IL for intervention-vs-observation lifts.
4. TSF for sensitivity-limited distinguishability.
5. RFS for weak-vs-strong target frontier geometry.

SRG remains a candidate framework. It is not promoted and is intentionally decoupled from existing repo theory labels in this pass.

## Final verdict

At least one nontrivial structure survived novelty pressure (CID/PSI/IL/TSF/RFS set), with proved or conditional statements and explicit anomaly families.

## Output files

- `docs/meta-governance/internal/discovery-notes/new_structures_report.md`
- `docs/meta-governance/internal/discovery-notes/witness_catalog.csv`
- `docs/meta-governance/internal/discovery-notes/anomaly_catalog.csv`
- `docs/meta-governance/internal/discovery-notes/theory_candidates.md`
