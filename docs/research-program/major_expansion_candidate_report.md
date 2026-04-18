# Major Expansion Candidate Report

Status: **EXPLORATION / NON-PROMOTED**

## 1. Executive Verdict

Verdict: **Hybrid candidate (branch-limited theorem + application)** with recommendation **KEEP AS CONDITIONAL MAJOR CANDIDATE**.

Candidate selected: **Context-Invariant Recoverability and Shared Augmentation Threshold Package**.

This pass did not alter the theorem spine. It extracted a branch-limited major candidate and subjected it to explicit falsification pressure.

## 2. Stage 1 Hard Triage (Top 5 Surviving Lanes)

Lanes scored on theorem/no-go/anomaly/application/compatibility/novelty/tractability with collapse-risk penalty.

| Lane | Theorem | No-go | Anomaly | App | Compat | Novelty | Tractability | Collapse risk | Weighted | Selected |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Causal inference / invariant prediction | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 2 | 31 | True |
| Willems’ fundamental lemma / data-driven control | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 2 | 29 | True |
| Network information theory / multi-terminal settings | 4 | 4 | 4 | 4 | 5 | 3 | 4 | 3 | 25 | False |
| Quantum Fisher information / Cramér-Rao structure | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 20 | False |
| Magnetic reconnection extension | 2 | 2 | 4 | 4 | 4 | 3 | 3 | 4 | 18 | False |

Top 2 selected for deep extraction:

1. Causal inference / invariant prediction
2. Willems’ fundamental lemma / data-driven control

Deferred this pass (not killed permanently, but not deep-developed now):

- `Network information theory / multi-terminal settings`: Strong comparator lane, but causal+Willems jointly gave a tighter path to one new common mathematical package this pass.
- `Quantum Fisher information / Cramér-Rao structure`: High diagnostic value but current gain is primarily estimation-bound benchmarking, not core theorem extraction.
- `Magnetic reconnection extension`: Produced validated regime diagnostics, but no theorem-grade core extension in the current extraction window.

## 3. Stage 2 Deep Extraction

### 3.1 Causal lane extraction

Translation into repo objects:

- `admissible_family`: environment-indexed linear families of latent causes/confounders
- `target`: cause-specific functional
- `record_map`: environment-specific observational/interventional measurement rows
- `disturbance`: confounding and environment-dependent scaling
- `compatibility`: existence of one environment-invariant decoder
- `exactness`: single decoder recovers target across all environments
- `impossibility`: cross-environment decoder incompatibility despite per-environment exactness
- `augmentation`: shared intervention/measurement row that restores invariance

Key outcomes:

- same-rank observational/interventional split: observational exact=False, interventional exact=True
- conditioned-vs-invariant split: conditioned=True, invariant=False, invariant residual=0.400000
- shared augmentation threshold: minimal_shared_rows=1, post-augmentation invariant exact=True
- descriptor-matched opposite verdict pair exists: True

Claim statuses:

- `CIR-C1` (VALIDATED): Same-rank observational and interventional measurements can produce opposite exactness verdicts. (observational rank=1 exact=false vs interventional rank=1 exact=true)
- `CIR-C2` (PROVED ON SUPPORTED FAMILY): Conditioned exactness (each context exact) does not imply context-invariant exactness (single shared decoder). (contexts [1,0] and [2,0] each recover target [1,0], but no common scalar decoder exists)
- `CIR-C3` (PROVED ON SUPPORTED FAMILY): A one-row shared intervention can collapse context-invariant failure to exactness in the canonical causal family. (minimal_shared_rows=1 with candidate row [1,0])

### 3.2 Willems lane extraction

Translation into repo objects:

- `admissible_family`: trajectory libraries indexed by experiment context
- `target`: state/output functionals to reconstruct from data
- `record_map`: data matrix rows (trajectory-derived records)
- `disturbance`: poor excitation directionality and context scaling mismatch
- `compatibility`: shared decoder consistency across data contexts
- `exactness`: single map from records to target across experiment contexts
- `impossibility`: same data volume and same rank but incompatible directional support
- `augmentation`: shared excitation row improving context-invariant richness

Key outcomes:

- same budget and same rank split: exact=True, fail=False
- conditioned-vs-invariant split: conditioned=True, invariant=False, invariant residual=0.400000
- shared augmentation threshold: minimal_shared_rows=1, post-augmentation invariant exact=True
- descriptor-matched opposite verdict pair exists: True

Claim statuses:

- `CIR-W1` (VALIDATED): Same sample budget and same observation rank can still split into exact and impossible recoverability in trajectory-data settings. (H_exact rank=2 exact=true, H_fail rank=2 exact=false, both with 4 rows)
- `CIR-W2` (PROVED ON SUPPORTED FAMILY): Per-context exactness of data maps does not imply context-invariant exactness for a shared decoder. (context pair I and diag(2,1) for target I is individually exact but jointly incompatible under one decoder)
- `CIR-W3` (PROVED ON SUPPORTED FAMILY): A one-row shared excitation augmentation restores invariant exactness in the canonical two-context data family. (minimal_shared_rows=1 with candidate row [1,0])

### 3.3 Comparator snapshots from deferred lanes

- Network lane: same-rank split remains strong (`exact DLS=0.000` vs `fail DLS=0.750`), but this pass favored a single multi-context package over two parallel packages.
- QFI lane: mean FI split remains strong (`blind=0.000`, `sensitive=1.000`), but gain is currently estimation-side and not yet a core theorem extension.
- Reconnection lane: concentration gain=0.215; important diagnostic lane, still theorem-light.

## 4. Stage 3 Major Candidate Package

Candidate: **Context-Invariant Recoverability and Shared Augmentation Threshold Package**

Exact definitions introduced:

- `conditioned_exactness`: Each context admits an exact decoder, potentially context-specific.
- `context_invariant_exactness`: A single decoder recovers the target across all contexts.
- `context_invariance_gap`: Maximum context residual under the best shared decoder (0 iff invariant exactness).
- `shared_augmentation_threshold`: Minimal number of shared rows needed to restore context-invariant exactness.

Theorem candidates:

- `CIR-T1` (PROVED ON SUPPORTED FAMILY): There exist finite restricted-linear families where conditioned exactness holds while context-invariant exactness fails. (witness: causal contexts [1,0], [2,0], target [1,0])
- `CIR-T2` (PROVED ON SUPPORTED FAMILY): No classifier using only context-count and rank descriptors can decide context-invariant exactness on the canonical scaling family. (witness: descriptor-matched exact and fail context pairs in both causal and Willems families)
- `CIR-T3` (PROVED ON SUPPORTED FAMILY): Shared augmentation threshold can be strictly positive even when conditioned exactness already holds. (witness: minimal_shared_rows=1 in both causal and Willems canonical pairs)

No-go candidates:

- `CIR-N1` (PROVED ON SUPPORTED FAMILY): Conditioned exactness does not imply context-invariant exactness.
- `CIR-N2` (VALIDATED): Stacked single-context exactness is insufficient to certify context-invariant exactness.

Validated anomaly family:

- `major_causal_same_rank_opposite_verdict`: same-rank opposite exactness (obs_dls=1.000, int_dls=0.000)
- `major_causal_conditioned_vs_invariant_split`: conditioned-exact but invariant-fail (invariant_residual_fail=0.400000, invariant_residual_exact=0.000000)
- `major_causal_one_row_threshold_drop`: small augmentation causes large invariant residual drop (post_aug_invariant_residual=0.000000)
- `major_willems_same_budget_same_rank_opposite_verdict`: same-sample-budget and same-rank opposite exactness (exact_dls=0.000, fail_dls=1.000)
- `major_willems_conditioned_vs_invariant_split`: conditioned-exact but invariant-fail (invariant_residual_fail=0.400000, invariant_residual_exact=0.000000)
- `major_willems_one_row_excitation_threshold`: small shared excitation row restores invariance (post_aug_invariant_residual=0.000000)

What is genuinely new relative to current repo:

- explicit multi-context exactness split: conditioned vs context-invariant
- context-invariance gap as a branch-level diagnostic above count/rank summaries
- shared augmentation threshold law tied to multi-context compatibility

What is likely reframing and therefore not overclaimed:

- global fiber/factorization logic still underlies the new package
- some statements can be rewritten as lifted linear compatibility constraints

## 5. Stage 4 Falsification Counterattack

All major-candidate claims were attacked directly.

### attack_1_implied_by_existing_factorization

- test: Translate invariant requirement to existing fiber language and check whether claims are purely renaming.
- result: **PARTIAL**
- details: Core logic is compatible with fiber/factorization foundations, but the conditioned-vs-invariant split and shared threshold are not explicit in the current theorem package.

### attack_2_reduces_to_single_rowspace_inclusion

- test: Check stacked row-space exactness on fail contexts.
- result: **SURVIVED**
- details: Both stacked checks are exact while context-invariant exactness fails, so stacked single-context criteria alone are insufficient.

### attack_3_small_family_overfit

- test: Extend fail families with additional scaled contexts and retest invariant exactness.
- result: **SURVIVED**
- details: Adding additional scaled contexts preserves conditioned exactness and invariant failure in the canonical family.

### attack_4_descriptor_choice_fragility

- test: Check descriptor-matched opposite verdict pairs.
- result: **SURVIVED**
- details: Exact and fail families share the same rank/count descriptor yet split on invariant exactness.

### attack_5_application_only_no_math

- test: Require theorem/no-go statements with explicit witnesses and proof sketches.
- result: **SURVIVED_ON_SUPPORTED_FAMILY**
- details: Three branch-limited proved-on-family statements were extracted; broader generalization remains open.

## 6. Stage 5 Final Decision

Final recommendation: **KEEP AS CONDITIONAL MAJOR CANDIDATE**.

Why this is the strongest current serious addition:

1. It produces branch-limited proved-on-family statements, not only narrative reframing.
2. It links two top lanes through one mathematical object (context-invariant decoder compatibility).
3. It yields explicit opposite-verdict families under matched descriptor summaries.
4. It remains falsification-aware and does not claim universal promotion.

Failure risks that remain:

1. Broader generalization could collapse into existing factorization language without additional invariant gain.
2. Current strongest claims are proved only on supported finite/restricted-linear families.
3. Application transfer to nonlinear/continuous branches needs further constructive witnesses.

## 7. Implementation Roadmap (if promoted later)

1. Add a dedicated context-invariant benchmark suite with randomized context families and explicit fail/exact pair generation.
2. Add a formal dependency map connecting context-invariant no-go to existing fiber/factorization statements.
3. Add workbench diagnostics for conditioned-vs-invariant split and shared augmentation threshold.
4. Add theorem-pressure pass for generalized multi-context anti-classifier conditions.

## 8. Artifacts Produced

- `data/generated/discovery/major_expansion_lane_ranking.csv`
- `data/generated/discovery/major_expansion_anomalies.csv`
- `data/generated/discovery/major_expansion_summary.json`
- `docs/research-program/major_expansion_candidate_report.md`
- `docs/research-program/context_invariant_recoverability_overview.md`
- `docs/research-program/context_invariant_recoverability_theorem_candidates.md`
- `docs/research-program/context_invariant_recoverability_no_go_candidates.md`
- `docs/research-program/context_invariant_recoverability_validation_plan.md`
