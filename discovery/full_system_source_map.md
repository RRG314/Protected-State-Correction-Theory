# Full System Source Map

Status: discovery inventory for cross-repo clear-new-results extraction pass.

## Scope
- Workspace roots scanned: `repos/ocp-research-program`, `repos/cfd-research-program`, `mhd-toolkit`, `repos/topological-adam`, `repos/soliton-geometry-research`, `repos/rge256`, `repos/numpyrge256`, `repos/torchrge256`, `repos/RGE-256-app`, `repos/RGE-256-Lite`.
- Included file classes: docs/papers/scripts/tests/source modules/generated artifacts/figures plus `.docx` exploratory bundles where present.
- Excluded noise: `.git`, virtualenvs, node modules, build/cache dirs.

## Inventory Totals
- Total indexed sources: **1491**
- RGE-256-Lite: 9
- RGE-256-app: 12
- cfd-research-program: 70
- mhd-toolkit: 151
- numpyrge256: 13
- ocp-research-program: 796
- rge256: 20
- soliton-geometry-research: 271
- topological-adam: 129
- torchrge256: 20

## Domain Totals
- OCP / recoverability core: 646
- soliton geometry / nonlinear-wave recoverability: 271
- MHD closure / obstruction: 151
- optimizer engineering / SDS experiments: 88
- CFD / bounded-domain projection: 78
- RGE / recursive-entropy PRNG ecosystem: 74
- workbench / image-center surface: 62
- TSIT / target-specific design: 42
- meta / structure-formation exploration: 37
- indistinguishability: 13
- context-sensitive recoverability: 9
- MHD bridge in OCP corpus: 8
- MHD-adjacent symbolic lane (legacy): 6
- SDS / thermodynamic / black-hole exploratory: 6

## Branch/Domain Map
### CFD / bounded-domain projection — cfd-research-program
- Indexed sources: 70
- Canonical anchors:
  - `FINAL_REPORT.md`
  - `README.md`
  - `STATUS.md`
  - `SYSTEM_REPORT.md`
  - `docs/no-go/no-go-spine.md`
  - `docs/theorems/proof-status-map.md`
  - `docs/theorems/theorem-spine.md`
  - `papers/bridge_paper.md`

### CFD / bounded-domain projection — ocp-research-program
- Indexed sources: 8

### MHD bridge in OCP corpus — ocp-research-program
- Indexed sources: 8

### MHD closure / obstruction — mhd-toolkit
- Indexed sources: 151
- Canonical anchors:
  - `FILE_INDEX.md`
  - `FINAL_REPORT.md`
  - `MHD_FINAL_REPORT.md`
  - `README.md`
  - `RESEARCH_MAP.md`
  - `ROADMAP.md`
  - `STATUS.md`
  - `SYSTEM_REPORT.md`
- Local-only / in-progress signals: untracked=14, modified=18

### MHD-adjacent symbolic lane (legacy) — topological-adam
- Indexed sources: 6
- Canonical anchors:
  - `MHD_Closure_Theory_New_Theorems_2026.docx`
  - `docs/variable-resistivity/obstruction.md`
- Local-only / in-progress signals: untracked=3, modified=0

### OCP / recoverability core — ocp-research-program
- Indexed sources: 646
- Canonical anchors:
  - `FILE_INDEX.md`
  - `FINAL_REPORT.md`
  - `NOVELTY_AND_LIMITS.md`
  - `README.md`
  - `RESEARCH_MAP.md`
  - `ROADMAP.md`
  - `STATUS.md`
  - `SYSTEM_REPORT.md`
- Local-only / in-progress signals: untracked=6, modified=0

### RGE / recursive-entropy PRNG ecosystem — RGE-256-Lite
- Indexed sources: 9
- Canonical anchors:
  - `README.md`
  - `docs/releases/README.md`

### RGE / recursive-entropy PRNG ecosystem — RGE-256-app
- Indexed sources: 12
- Canonical anchors:
  - `README.md`
  - `docs/releases/README.md`

### RGE / recursive-entropy PRNG ecosystem — numpyrge256
- Indexed sources: 13
- Canonical anchors:
  - `README.md`
  - `docs/releases/README.md`

### RGE / recursive-entropy PRNG ecosystem — rge256
- Indexed sources: 20
- Canonical anchors:
  - `README.md`
  - `docs/releases/README.md`

### RGE / recursive-entropy PRNG ecosystem — torchrge256
- Indexed sources: 20
- Canonical anchors:
  - `README.md`
  - `docs/releases/README.md`

### SDS / thermodynamic / black-hole exploratory — topological-adam
- Indexed sources: 6
- Local-only / in-progress signals: untracked=1, modified=0

### TSIT / target-specific design — ocp-research-program
- Indexed sources: 13

### TSIT / target-specific design — topological-adam
- Indexed sources: 29
- Canonical anchors:
  - `docs/research-program/tsit_no_go_candidates.md`
  - `docs/research-program/tsit_theorem_candidates.md`
- Local-only / in-progress signals: untracked=1, modified=0

### context-sensitive recoverability — ocp-research-program
- Indexed sources: 9
- Local-only / in-progress signals: untracked=4, modified=0

### indistinguishability — ocp-research-program
- Indexed sources: 13
- Canonical anchors:
  - `theory/no-go/indistinguishability.md`

### meta / structure-formation exploration — ocp-research-program
- Indexed sources: 37
- Canonical anchors:
  - `docs/meta_theory/README.md`
  - `docs/research-program/sfpr_no_go_candidates.md`
  - `docs/research-program/sfpr_theorem_candidates.md`
- Local-only / in-progress signals: untracked=12, modified=0

### optimizer engineering / SDS experiments — topological-adam
- Indexed sources: 88
- Canonical anchors:
  - `FINAL_REPORT.md`
  - `README.md`
  - `ROADMAP.md`
  - `STATUS.md`
  - `SYSTEM_REPORT.md`
  - `TOPOLOGICAL_ADAM_FINAL_REPORT.md`
  - `Topological_Adam_Paper_2026.docx`
  - `docs/domain-obstruction/domain_topology.md`
- Local-only / in-progress signals: untracked=15, modified=0

### soliton geometry / nonlinear-wave recoverability — soliton-geometry-research
- Indexed sources: 271
- Canonical anchors:
  - `README.md`
  - `docs/projection_lane/theorem_candidates.md`
  - `docs/research-program/first_serious_theorem_and_experiment_comprehensive_report.md`
  - `docs/theorem_attempt/open_problems_after_promotion.md`
  - `docs/theorem_attempt/proof_or_disproof_notes.md`
  - `docs/theorem_attempt/proof_pressure_notes.md`
  - `docs/theorem_attempt/soliton_recoverability_formalism.md`
  - `docs/theorem_attempt/theorem_candidates.md`
- Local-only / in-progress signals: untracked=18, modified=32

### workbench / image-center surface — ocp-research-program
- Indexed sources: 62

## Canonical vs Exploratory Decision Heuristic
- `canonical`: README/STATUS/SYSTEM_REPORT/FINAL_REPORT, theorem/no-go docs, active papers.
- `supporting`: source modules, scripts, tests, generated artifacts, figures.
- `exploratory`: discovery extracts, archive/raw-import imports, internal drafts, local untracked bundles.

## Known Risk Hotspots
- `topological-adam/discovery/extracted/*` contains untracked theory text exports (including RGE/holography/black-hole language) with low confidence until independently replicated.
- `ocp-research-program/discovery/*` and `docs/research-program/*` contain many exploratory/non-promoted packages; each claim needs theorem-status gating before promotion.
- `mhd-toolkit` has substantial modified+untracked expansion files in local tree; treat theorem claims as branch-scoped until cross-repo consistency checks are complete.
