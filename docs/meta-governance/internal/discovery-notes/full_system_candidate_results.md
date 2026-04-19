# Full System Candidate Results

Status: discovery extraction for full-system clear-new-results pass.

This file enumerates major candidate results across the full corpus and records their scoped statement, assumptions, evidence, and current status discipline.

## OCP / Recoverability Core

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| OCP-01 | Restricted-linear exactness criterion | For finite linear families, exact target recovery holds iff target row lies in observation row-space (`t in row(O)`). | Finite-dimensional linear class in repository. | `docs/theorem-candidates/constrained-observation-theorems.md`; `tests/math/test_recoverability.py`. | theorem | PROVED ON SUPPORTED FAMILY |
| OCP-02 | No rank-only exact classifier | Same rank tuple can produce exact and non-exact targets. | Enumerated finite restricted-linear families. | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv`; `data/generated/falsification/counterexample_catalog.csv` (`CX-RANK-*`). | no-go / counterexample family | PROVED ON SUPPORTED FAMILY |
| OCP-03 | No fixed-budget-only exact classifier | Equal budget can produce opposite exactness verdicts. | Candidate-library constrained finite family. | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` (`CX-BUDGET-*`). | no-go / counterexample family | PROVED ON SUPPORTED FAMILY |
| OCP-04 | Family enlargement fragility | Exactness on a smaller family can fail under honest enlargement. | Explicit small->large family construction. | `data/generated/unified-recoverability/family_enlargement_false_positive.csv` (`CX-FAMILY-001`). | no-go | PROVED ON SUPPORTED FAMILY |
| OCP-05 | Mismatch instability lower bound | Decoder mismatch introduces irreducible target error tied to mismatch geometry. | Canonical linear mismatch class. | `data/generated/unified-recoverability/canonical_model_mismatch.csv` (`CX-MISMATCH-*`). | theorem/no-go boundary | PROVED ON SUPPORTED FAMILY |

## Context-Sensitive Recoverability

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| CSR-01 | Conditioned-vs-invariant split | There exist families where each context is exactly decodable but no single shared decoder works across contexts. | Finite context-indexed linear families. | `docs/research-program/context_split_theorem_candidates.md`; `data/generated/context_sensitive_recoverability/summary.json`. | theorem / split law | PROVED ON SUPPORTED FAMILY |
| CSR-02 | Positive shared augmentation threshold | Some local-exact/global-fail families require positive shared augmentation (`r*>0`) to restore invariant exactness. | Restricted augmentation library in current generator. | `docs/research-program/shared_augmentation_threshold_candidates.md`; `data/generated/context_sensitive_recoverability/augmentation_threshold_catalog.csv`. | threshold law | PROVED ON SUPPORTED FAMILY |
| CSR-03 | Descriptor-only split failure | Descriptor tuples `(n,k,m,rank_stack,budget)` cannot classify invariant exactness. | Synthetic multi-context catalog. | `data/generated/context_sensitive_recoverability/multicontext_anomaly_catalog.csv` (23 opposite-verdict groups). | no-go / anti-classifier | PROVED ON SUPPORTED FAMILY |
| CSR-04 | Enlargement flip in context families | Adding one context can flip shared exactness from `1 -> 0`. | Same generator families. | `data/generated/context_sensitive_recoverability/summary.json` (`family_enlargement_flip_count=94`). | fragility pattern | VALIDATED / EMPIRICAL ONLY |

## Indistinguishability Lane

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| IND-01 | Rank-success / DLS-failure split | Systems with rank matching target can still have high distinguishability loss score. | Sampled finite systems from OCP/CFD/MHD examples. | `data/generated/indistinguishability/indistinguishability_anomalies.csv`. | anomaly family | VALIDATED / EMPIRICAL ONLY |
| IND-02 | DLS threshold collapse | Small augmentation/refinement can produce sharp DLS drop while rank descriptors change little. | Same sampled finite systems. | `data/generated/indistinguishability/indistinguishability_anomalies.csv` (`augmentation_threshold_dls_drop`). | threshold pattern | VALIDATED / EMPIRICAL ONLY |

## TSIT / Target-Specific Design Lane

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| TSIT-01 | D-optimal design can be target-blind | Sensor choice maximizing Fisher logdet can fail exact target recovery while alignment-optimal choice succeeds. | Structured finite linear sensor pools. | `data/generated/tsit-extension/tsit_positioning_expansion_anomalies.csv`; `data/generated/tsit/tsit_anomaly_catalog.csv` (`A002*`). | design-failure no-go | VALIDATED / EMPIRICAL ONLY |
| TSIT-02 | Same-capacity opposite target recoverability | Equal capacity/rank/count descriptors can still split exactness for fixed target. | Finite linear channel witness class. | `data/generated/tsit/tsit_anomaly_catalog.csv` (`A001`). | no-go / witness family | PROVED ON SUPPORTED FAMILY |
| TSIT-03 | Distributed allocation split | Same total budget can yield opposite target recoverability depending on allocation geometry. | Multi-terminal linear witness family. | `data/generated/tsit_positioning/summary.json` (`allocation_split_count=280`). | theorem candidate / no-go package | VALIDATED / EMPIRICAL ONLY |
| TSIT-04 | Alpha novelty collapse in linear class | `alpha=1` reduces to row-space inclusion in supported linear families. | Finite linear channel class. | `docs/research-program/tsit_literature_overlap_audit.md`; `docs/research-program/tsit_repo_positioning_report.md`. | reduction result | ALREADY KNOWN IN SUBSTANCE |

## CFD Branch

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| CFD-01 | Periodic projection exact anchor | Periodic Helmholtz projector exactly recovers divergence-free component on implemented periodic family. | Implemented periodic benchmark family. | `docs/theorems/theorem-spine.md` (`CFD-T1`); `data/generated/benchmarks/cfd_benchmark_summary.json`. | theorem | PROVED ON SUPPORTED FAMILY |
| CFD-02 | Bounded transplant failure | Naive periodic projector reuse fails bounded-domain class compatibility. | Bounded benchmark counterexample. | `docs/no-go/no-go-spine.md` (`CFD-N2`). | no-go | PROVED |
| CFD-03 | Divergence-only insufficiency | Distinct bounded states can share divergence-only record; velocity not uniquely determined. | Bounded benchmark family. | `docs/theorems/theorem-spine.md` (`CFD-T4`). | no-go | PROVED |
| CFD-04 | Sensor geometry beats sensor count/rank | Same sensor count and same rank can still produce opposite recoverability verdicts. | Restricted linear CFD reconstruction family. | `data/generated/benchmarks/sensor_geometry_cases.csv`; `docs/theorems/theorem-spine.md` (`CFD-T8`). | theorem/no-go pair | PROVED ON SUPPORTED FAMILY |
| CFD-05 | Energy-capture false security | Rank-1 model can keep >99% energy but fail bifurcation-sensitive wake proxy; rank-2 restores sign. | Reduced-order benchmark lane. | `data/generated/benchmarks/reduced_order_rank_rows.csv`. | benchmark counterexample | VALIDATED / EMPIRICAL ONLY |

## MHD Closure / Obstruction Branch

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| MHD-01 | Constant-eta exact cylindrical families | Explicit Euler-potential families are exactly closed under constant resistivity. | Cylindrical families listed in proof map. | `docs/theorems/proof_status.md` (`MHD-T1..T4`). | theorem family | PROVED |
| MHD-02 | Variable-eta obstruction with annular survivors | Nonconstant `eta(r)` breaks smooth exactness in supported radial families; only annular/singular survivor classes remain (`sqrt(r)`, `log(r)` branches). | Supported radial/separable cylindrical families. | `docs/theorems/proof_status.md` (`MHD-O1..O3`). | theorem/no-go boundary | PROVED |
| MHD-03 | Mixed tokamak/reduced-MHD factorization | For `alpha=f(r), beta=z+q(r)theta`, exactness factorizes as `(r f''-f')(r q'-q)=0` (constant eta), with restricted variable-eta ODE branch. | Mixed separable family in expansion lane. | `docs/theorems/tokamak-and-reduced-mhd-lane.md`. | theorem | PROVED (restricted scope) |
| MHD-04 | Sheet thinning concentrates closure defect | Decreasing sheet width (`delta`) strongly increases defect concentration and localization ratio. | Sheet-profile benchmark family. | `data/generated/expansion/reconnection_sheet_scaling.csv`. | regime anomaly | VALIDATED / EMPIRICAL ONLY |

## Soliton Geometry Branch

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| SOL-01 | Symmetry non-identifiability no-go | Observation classes invariant under symmetry quotients can block unique recovery. | Formal lane supported families. | `docs/research_program/status_registry.md` (`SOL-THM-001`). | no-go | PROVED |
| SOL-02 | Same-count opposite-verdict witness | Same observation dimension can produce opposite non-identifiability outcomes across observation families. | Supported finite family scans. | `data/generated/recoverability/same_count_opposite_verdict.json`; status registry `SOL-THM-003`. | counterexample family | PROVED ON SUPPORTED FAMILY |
| SOL-03 | CGL random-superiority instability | Random self-organization superiority signal collapses under artifact checks. | CGL self-organization benchmark lane. | `data/generated/docs/meta-governance/internal/discovery-notes/anomalies/anomaly_catalog_expanded.json` (`A-CGL-SELF-ORG`). | falsified anomaly | ARTIFACT RISK |

## RGE / Recursive-Entropy Ecosystem

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| RGE-01 | Statistical sanity across variants | Core RGE variants pass repository small-stat/cycle tests; major claims are validation-level, not theorem-level randomness guarantees. | Repo test suites and technical reference scope. | `repos/rge256/tests/*`; `docs/reference/technical-readme-2026-04-12.md`. | implementation validation | VALIDATED / EMPIRICAL ONLY |
| RGE-02 | Counter-mode branch maturity split (Torch) | Torch counter-mode branch is retained but not default due biased empirical moments in validation note. | Torch package internal validation lane. | `repos/torchrge256/docs/validation/counter-mode-status.md`. | branch maturity no-go | VALIDATED / EMPIRICAL ONLY |

## SDS / Thermodynamic / Black-Hole Exploratory Layer

| ID | Short name | Precise statement | Scope / assumptions | Evidence anchor | Result type | Current status |
|---|---|---|---|---|---|---|
| SDS-01 | SDS optimizer branch neutrality | SDS-inspired optimizer branch is stable but not clearly superior to supported V2 baseline. | TopologicalAdam benchmark suite. | `docs/sds-candidate.md`; `TOPOLOGICAL_ADAM_FINAL_REPORT.md`. | benchmark result | VALIDATED / EMPIRICAL ONLY |
| SDS-02 | Holography/black-hole extracts are non-canonical | High-claim thermodynamic/holographic material appears in extracted discovery text and remains outside canonical theorem/test spine. | Untracked extracted text bundle. | `docs/meta-governance/internal/discovery-notes/extracted/RGE_Physical_Laws_2026.txt`. | placement/risk finding | OPEN |

