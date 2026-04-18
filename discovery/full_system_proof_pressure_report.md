# Full System Proof Pressure Report

Status: falsification-first pressure pass across the full corpus.

## 1) Validation Runs Executed in This Pass

| Repo | Command | Result |
|---|---|---|
| `ocp-research-program` | `PYTHONPATH=src ./.venv/bin/python -m pytest -q` | `191 passed` |
| `cfd-research-program` | `uv run --with pytest python -m pytest -q` | `21 passed` |
| `mhd-toolkit` | `uv run --extra dev --extra research python -m pytest` | `34 passed` |
| `mhd-toolkit` | `uv run --extra research python scripts/validate/run_research_checks.py` | wrote symbolic closure report |
| `mhd-toolkit` | `uv run --extra research python scripts/validate/run_expansion_checks.py` | wrote expansion artifacts |
| `soliton-geometry-research` | `./.venv/bin/python -m pytest -q` | `21 passed` |
| `rge256` | `uv run --with pytest python -m pytest -q` | `7 passed`, warnings present |
| `numpyrge256` | `uv run --with pytest python -m pytest -q` | `8 passed`, config warning |
| `torchrge256` | `uv run --with pytest python -m pytest -q` | no tests collected (`exit 5`) |
| `topological-adam` | local rerun attempt | blocked: local venv invalid/incomplete (`torch`, `pytest` absent) |

## 2) Theorem Pressure by Branch

## OCP / Recoverability

### Claims attacked
1. Rank-only sufficiency.
2. Budget-only sufficiency.
3. Exactness persistence under family enlargement.
4. Model mismatch stability.

### Pressure outcome
- Rank-only and budget-only sufficiency **fail** under explicit counterexamples (`CX-RANK-*`, `CX-BUDGET-*`).
- Family-enlargement persistence **fails** (`CX-FAMILY-001`).
- Mismatch-stability overclaim **fails** (`CX-MISMATCH-*`).

### Verdict
Strong anti-classifier no-go package survives; no universal descriptor classifier survives this pressure.

## Context-Sensitive Recoverability

### Claims attacked
1. Conditioned exactness implies invariant exactness.
2. Context split is just hand-built artifact.
3. Shared augmentation is trivial naming.
4. Descriptor tuples classify invariant exactness.

### Pressure outcome
- (1) **disproved** on supported family (`506` local-exact/global-fail cases).
- (2) **partially survives**: synthetic generator dependence exists, but opposite-verdict groups and flips are large (`23` groups; `94` flips).
- (3) **partially survives**: augmentation effect is real but class-dependent.
- (4) **disproved** on supported family.

### Verdict
Three-piece package survives as branch-limited theorem/no-go candidate; broad novelty beyond OCP core is not established.

## Indistinguishability

### Claims attacked
1. DLS adds no signal beyond rank.
2. DLS threshold effects are artifacts.

### Pressure outcome
- Rank-vs-DLS contradictions appear repeatedly (`rank_predicts_success_but_dls_high`).
- Sharp DLS drops under augmentation/refinement are reproducible in periodic/bounded/MHD examples.

### Verdict
Useful exploratory diagnostic lane survives; theorem promotion remains unsupported.

## TSIT

### Claims attacked
1. TSIT as independent foundational theory.
2. Alpha as fundamentally new invariant in linear class.
3. Target-lossless theorem as independent core theorem.
4. D-optimal claims as one-off witnesses.

### Pressure outcome
- (1) **collapses** under reduction and literature-risk checks.
- (2) **collapses** (`alpha=1` equivalent to row-space inclusion in supported linear class).
- (3) **partially collapses** to existing fiber-purity logic.
- (4) **survives as empirical no-go package** with high witness counts.

### Verdict
TSIT survives as adjacent quantitative design/application lane; not foundational replacement.

## CFD

### Claims attacked
1. Bounded-domain behavior can be inferred from periodic anchor.
2. Sensor count/rank suffices for exactness.
3. High energy capture certifies branch-sensitive recovery.

### Pressure outcome
- (1) **disproved** by transplant failure no-go.
- (2) **disproved** by sensor-geometry split.
- (3) **disproved** by reduced-order benchmark counterexample.

### Verdict
CFD branch remains strong when scoped to implemented families; validated lanes remain non-theorem.

## MHD

### Claims attacked
1. Variable-resistivity obstruction is only numerical artifact.
2. Mixed tokamak lane is symbolic overfit.
3. Reconnection interpretation is theorem-grade.

### Pressure outcome
- (1) **survives** as theorem-level symbolic classification in supported families.
- (2) **survives (restricted)** with factorized symbolic condition and tests.
- (3) **fails as theorem claim**; remains validated benchmark signature.

### Verdict
MHD has one of the strongest surviving theorem/no-go boundaries in the corpus, but reconnection claims must remain benchmark-scoped.

## Soliton

### Claims attacked
1. Same-count opposite-verdict may be unstable.
2. CGL random-superiority anomaly is robust.

### Pressure outcome
- (1) **survives on supported family**.
- (2) **fails robustness** (`ARTIFACT RISK`).

### Verdict
Formal soliton recoverability lane survives; self-organization superiority claim is demoted.

## RGE / PRNG ecosystem

### Claims attacked
1. Statistical pass implies theorem-grade novelty.
2. Counter-mode torch path maturity equals default path.

### Pressure outcome
- (1) **fails** as theorem claim; remains validation-level.
- (2) **fails** per explicit counter-mode-status note.

### Verdict
RGE branches are engineering/validation layers, not theorem lanes in current corpus.

## SDS / thermodynamic / black-hole exploratory text

### Claims attacked
1. Extracted high-claim text is ready for canonical theorem promotion.

### Pressure outcome
- **collapses** under canonical-harness test: claims live in extracted/untracked materials without matching promoted test/proof pipeline.

### Verdict
Keep outside canonical theorem ranking unless independently formalized and tested.

## 3) Survive / Collapse Matrix

| Branch | Core survives | Key collapse |
|---|---|---|
| OCP | anti-classifier no-go corpus | none at scoped level |
| Context-sensitive | conditioned-vs-invariant + augmentation existence | broad novelty claims beyond OCP core |
| Indistinguishability | diagnostic value | theorem-promotion claims |
| TSIT | design/allocation failure package | standalone foundational-theory narrative |
| CFD | bounded-vs-periodic obstruction + geometry split | generalized unscoped CFD claims |
| MHD | variable-eta boundary + mixed-lane factorization | universal reconnection theorem framing |
| Soliton | symmetry and same-count formal lane | CGL random-superiority claim |
| RGE | package-level validation | theorem-grade randomness novelty framing |
| SDS exploratory | useful experimental branching | black-hole/holography promotion readiness |

## 4) Pressure-Pass Conclusion

The strongest survivors are scoped theorem/no-go packages in OCP, context-sensitive recoverability, CFD finite-design branch, and MHD symbolic closure boundary. The highest-risk overreach zones are TSIT-core replacement claims, SDS/black-hole extracted theory claims, and benchmark-to-universal promotion attempts.
