# System Report

## Executive Summary

The repository now stands as a finished theory-first program with a real physics extension.

The strongest current picture is:
- exact protected-state correction through orthogonal projectors,
- exact sector recovery through orthogonal sector embeddings,
- exact periodic continuous projection through the Helmholtz/Leray anchor,
- exact periodic incompressible velocity projection as a narrow CFD corollary of the same projector branch,
- a constrained-observation recoverability layer that classifies exact, approximate, asymptotic, and impossible recovery under coarse records,
- asymptotic continuous correction through invariant-split generators,
- a stronger physics lane through Maxwell/gauge projection and constraint-damping comparisons,
- and a no-go layer strong enough to police overlap, mixing, sector ambiguity, insufficient correction image, finite-time overclaiming, and naive projector transplantation.

## Repository Inventory

High-level file totals from the generated inventory:
- tracked-like files: `224`
- root files: `18`
- archive files: `8`
- data files: `15`
- docs files: `96`
- papers files: `6`
- scripts files: `10`
- source files: `30`
- test files: `29`
- theory files: `7`

Machine-readable inventory:
- [data/generated/inventories/repo_file_inventory.csv](data/generated/inventories/repo_file_inventory.csv)
- [data/generated/validations/system_summary.json](data/generated/validations/system_summary.json)

## Claim Inventory

Current registered claim totals from the regenerated claim registry:
- total tracked claims: `42`
- `PROVED`: `27`, including the constrained-observation baseline criteria, robust lower bound, the restricted-linear minimal-complexity criterion, and the new periodic/control threshold generalizations
- `CONDITIONAL`: `11`, including kept QEC/control/physics bridges and the observation-layer branch's stronger open targets
- `DISPROVED`: bounded-domain naive projector transplant claim
- `OPEN`: `1`
- `ANALOGY ONLY`: `2`, namely the generic constrained-Hamiltonian automatic-fit claim and the demoted optimizer/ML bridge

Primary claim artifacts:
- [docs/overview/claim-registry.md](docs/overview/claim-registry.md)
- [docs/overview/proof-status-map.md](docs/overview/proof-status-map.md)

## Theory Inventory

### Finalization layer
- [docs/finalization/theorem-spine-final.md](docs/finalization/theorem-spine-final.md)
- [docs/finalization/no-go-spine-final.md](docs/finalization/no-go-spine-final.md)
- [docs/finalization/operator-spine-final.md](docs/finalization/operator-spine-final.md)
- [docs/finalization/architecture-final.md](docs/finalization/architecture-final.md)
- [docs/finalization/naming-and-terminology.md](docs/finalization/naming-and-terminology.md)

### Exact branch
- [docs/theorem-candidates/central-theorem.md](docs/theorem-candidates/central-theorem.md)
- [docs/theorem-candidates/sector-recovery-theorems.md](docs/theorem-candidates/sector-recovery-theorems.md)
- [docs/theorem-candidates/capacity-theorems.md](docs/theorem-candidates/capacity-theorems.md)

### Continuous / asymptotic branch
- [docs/theorem-candidates/generator-theorems.md](docs/theorem-candidates/generator-theorems.md)
- [docs/mhd/divergence-cleaning-in-ocp.md](docs/mhd/divergence-cleaning-in-ocp.md)
- [docs/mhd/glm-and-asymptotic-correction.md](docs/mhd/glm-and-asymptotic-correction.md)

### Physics extension
- [docs/physics/physics-system-matrix.md](docs/physics/physics-system-matrix.md)
- [docs/physics/maxwell-coulomb-gauge.md](docs/physics/maxwell-coulomb-gauge.md)
- [docs/physics/numerical-relativity-constraint-damping.md](docs/physics/numerical-relativity-constraint-damping.md)
- [docs/physics/continuous-quantum-error-correction.md](docs/physics/continuous-quantum-error-correction.md)
- [docs/physics/bounded-domain-projection-limits.md](docs/physics/bounded-domain-projection-limits.md)
- [docs/physics/kept-vs-rejected-physics-bridges.md](docs/physics/kept-vs-rejected-physics-bridges.md)

### Constrained-observation branch
- [docs/theory/advanced-directions/constrained-observation-recoverability.md](docs/theory/advanced-directions/constrained-observation-recoverability.md)
- [docs/theory/advanced-directions/constrained-observation-formalism.md](docs/theory/advanced-directions/constrained-observation-formalism.md)
- [docs/theory/advanced-directions/constrained-observation-results-report.md](docs/theory/advanced-directions/constrained-observation-results-report.md)
- [docs/theory/advanced-directions/constrained-observation-validation.md](docs/theory/advanced-directions/constrained-observation-validation.md)
- [docs/theory/advanced-directions/constrained-observation-assessment.md](docs/theory/advanced-directions/constrained-observation-assessment.md)
- [docs/theorem-candidates/constrained-observation-theorems.md](docs/theorem-candidates/constrained-observation-theorems.md)
- [docs/impossibility-results/constrained-observation-no-go.md](docs/impossibility-results/constrained-observation-no-go.md)

### CFD extension
- [docs/cfd/cfd-system-matrix.md](docs/cfd/cfd-system-matrix.md)
- [docs/cfd/incompressible-projection.md](docs/cfd/incompressible-projection.md)
- [docs/cfd/helmholtz-hodge-velocity-projection.md](docs/cfd/helmholtz-hodge-velocity-projection.md)
- [docs/cfd/bounded-vs-periodic-projection.md](docs/cfd/bounded-vs-periodic-projection.md)
- [docs/cfd/cfd-vs-mhd-correction-comparison.md](docs/cfd/cfd-vs-mhd-correction-comparison.md)
- [docs/cfd/kept-vs-rejected-cfd-bridges.md](docs/cfd/kept-vs-rejected-cfd-bridges.md)
- [docs/theorem-candidates/cfd-projection-results.md](docs/theorem-candidates/cfd-projection-results.md)

### No-go layer
- [docs/impossibility-results/no-go-results.md](docs/impossibility-results/no-go-results.md)
- [docs/impossibility-results/advanced-no-go-results.md](docs/impossibility-results/advanced-no-go-results.md)

## System Inventory

### 1. Finite-dimensional exact branch
Status: `finished exact anchor`
- protected object: orthogonal protected subspace `S`
- disturbance object: orthogonal disturbance subspace `D`
- operator: `P_S`
- main results: OCP-T1, OCP-C1, OCP-T4

### 2. Exact sector branch
Status: `finished exact branch`
- protected object: `S`
- disturbance object: pairwise orthogonal sector family `D_i`
- operator: global sector-conditioned recovery built from `Q_i` and sector basis maps
- main results: OCP-T5, OCP-N8

### 3. QEC branch
Status: `exact anchor under standard assumptions`
- protected object: code space
- disturbance object: correctable syndrome sectors
- operator: sector projectors and coherent recovery family
- main value: exact anchor, not a claimed replacement for standard QEC theory

### 4. Exact continuous periodic branch
Status: `strong exact continuous anchor`
- protected object: divergence-free field component
- disturbance object: gradient contamination
- operator: periodic Helmholtz/Leray projection
- main result: machine-precision divergence suppression in the tracked example

### 5. Maxwell / gauge projection branch
Status: `kept exact physics extension`
- protected object: transverse field or vector-potential component
- disturbance object: longitudinal / pure-gradient component
- operator: transverse projector
- main value: real physics-side extension of the exact projector branch

### 5b. Incompressible CFD projection branch
Status: `kept narrow CFD extension`
- protected object: divergence-free velocity field
- disturbance object: non-solenoidal velocity contamination
- operator: pressure projection / Hodge projector
- main value: strongest honest CFD lane for the exact projector branch

### 6. Asymptotic continuous generator branch
Status: `finished asymptotic branch`
- protected object: `ker(K)` or invariant protected coordinates
- disturbance object: stable disturbance subspace
- operator: damping or invariant-split generator `K`
- main results: OCP-T2, OCP-T3, OCP-C2, OCP-N5, OCP-N7

### 7. GLM branch
Status: `kept as asymptotic only`
- protected object: physical field content
- disturbance object: divergence / constraint error
- operator: coupled GLM update law
- main value: practical asymptotic comparator, not exact recovery

### 8. Numerical-relativity constraint-damping branch
Status: `conditional asymptotic physics extension`
- protected object: constraint-satisfying solution sector
- disturbance object: constraint-violating modes
- operator: constraint-damping evolution terms
- main value: strong citable asymptotic direction beyond the current MHD anchor

### 9. Continuous-QEC branch
Status: `conditional bridge`
- protected object: code sector / logical information
- disturbance object: monitored error channels and syndrome drift
- operator: continuous measurement plus feedback or engineered dissipation
- main value: strongest citable bridge between exact QEC and continuous correction

### 10. Constrained-observation branch
Status: `kept formal/computational branch`
- protected object: chosen protected variable `p(x)` on an admissible family
- disturbance object: information lost under the record map or coarse observation fiber
- operator: record map `M`, recovery map `R`, and collapse-modulus diagnostic `κ_{M,p}`
- main value: a disciplined observation layer that distinguishes exact, approximate, asymptotic, and impossible recovery before correction is even attempted
- strongest surviving branch results:
  - `κ(η)/2` adversarial lower bound,
  - qubit phase-window collision law,
  - periodic cutoff threshold on the tested two-mode incompressible family,
  - four-mode periodic functional-support threshold law,
  - diagonal functional-interpolation threshold on the tested scalar-output control family,
  - same-record weaker-versus-stronger recovery splits,
  - corrected one-step / two-step / observer split in the toy control lane

### 11. Rejected branch
- naive periodic-projector reuse for bounded-domain exact correction
- generic constrained Hamiltonian automatic-fit language
- optimizer / ML bridge material as a main theory lane

## Operator Inventory

Exact operators:
- `P_S`
- `P_D`
- sector projectors `Q_i`
- global sector recovery operator
- code projector and QEC recovery family
- periodic Helmholtz/Leray projector
- transverse projector interpretation in the Maxwell/gauge extension
- constrained-observation exact recovery maps on admissible families

Asymptotic operators:
- `x_dot = -k P_D x`
- invariant-split generators `x_dot = -Kx`
- GLM update law
- constraint-damping evolution architecture as a conditional physics-side fit
- observer-side asymptotic recovery maps in the functional-observability toy lane

Failure diagnostics:
- overlap / intersection checks
- protected mixing norm `||P_S K P_D||`
- exact-recovery residual for finite-time flows
- rank / image lower-bound checks
- bounded-domain boundary-trace failure under naive periodic-projector reuse
- divergence-only indistinguishability on bounded incompressible protected classes
- fiber-collision gap and collapse modulus `κ_{M,p}`
- restricted observation-rank lower bounds on finite admissible families

## Workbench Inventory

Workbench location:
- [docs/workbench/index.html](docs/workbench/index.html)

Core workbench files:
- [docs/workbench/app.js](docs/workbench/app.js)
- [docs/workbench/styles.css](docs/workbench/styles.css)
- [docs/workbench/lib/compute.js](docs/workbench/lib/compute.js)
- [docs/workbench/lib/state.js](docs/workbench/lib/state.js)

Workbench docs:
- [docs/app/workbench-overview.md](docs/app/workbench-overview.md)
- [docs/app/module-theory-map.md](docs/app/module-theory-map.md)
- [docs/app/github-pages-deploy.md](docs/app/github-pages-deploy.md)

Workbench modules:
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- CFD Projection Lab
- Gauge Projection Lab
- Continuous Generator Lab
- No-Go Explorer
- Recoverability Lab

## Validation Inventory

Validation status:
- full validation script: passed
- static workbench asset check: passed
- markdown link check: passed
- naming consistency check: passed
- Node workbench tests: `16 passed`
- Python theorem/operator/example tests: `48 passed`

Primary validation entry points:
- [scripts/validate/run_all.sh](scripts/validate/run_all.sh)
- [scripts/validate/check_workbench_static.py](scripts/validate/check_workbench_static.py)
- [scripts/validate/check_naming.py](scripts/validate/check_naming.py)
- [scripts/compare/build_workbench_examples.mjs](scripts/compare/build_workbench_examples.mjs)

Primary generated artifacts:
- [data/generated/validations/operator_examples.json](data/generated/validations/operator_examples.json)
- [data/generated/validations/workbench_examples.json](data/generated/validations/workbench_examples.json)
- [data/generated/validations/claim_registry.csv](data/generated/validations/claim_registry.csv)
- [data/generated/recoverability/recoverability_summary.json](data/generated/recoverability/recoverability_summary.json)

## Results Snapshot

### Exact and sector branches
- QEC sector recovery errors: `[0.0, 0.0, 0.0, 0.0]`
- sector-theorem recovery errors: `[0.0, 0.0, 0.0, 0.0]`

### Continuous exact versus asymptotic branch
- divergence before exact projection: `19.359218295532003`
- divergence after exact projection: `2.359146931297974e-14`
- divergence after short GLM run: `16.849909741931956`

### New physics-side rejection result
- bounded-domain pre-projection divergence RMS: `7.188908004215289`
- bounded-domain post-projection divergence RMS: `5.4533400392382e-15`
- bounded-domain physical boundary-normal RMS: `2.304408101585748e-32`
- bounded-domain projected boundary-normal RMS: `0.031097335905001126`

### Workbench extension snapshot
- gauge module before norm: `14.103454585100657`
- gauge module after exact projection norm: `1.147354786301552e-13`
- gauge module after damped cleanup norm: `8.623534119392536`

### Constrained-observation snapshot
- analytic benchmark: `ε=0` is impossible while every tested `ε>0` is exact in the noise-free criterion
- analytic noise lower bound: every estimator incurs worst-case protected-variable error at least `κ(η)/2`
- qubit fixed-basis record:
  - full Bloch vector exact only on the zero-phase window
  - `z` coordinate exact on every tested phase window
- periodic record family:
  - full vorticity exact with mean RMS recovery error `1.20e-15`
  - truncated vorticity approximate with mean RMS recovery error `2.98`
  - divergence only impossible with collision distance `10.13`
  - functional thresholds on the four-mode family: exact cutoff `2` for `low_mode_sum`, `3` for `bandlimited_contrast`, and `4` for `full_weighted_sum`
  - the same cutoff can exactly recover a weaker protected functional while a stronger one remains impossible
- functional observability toy lane:
  - horizon `1` not exact for tested couplings
  - horizons `2` and `3` exact for every tested `ε>0`
  - observer branch asymptotically convergent with spectral radius `0.3` on the tracked family
  - diagonal scalar-output thresholds: `sensor_sum` exact at horizon `1`, `first_moment` at `2`, `second_moment` at `3` for the fully active profile, with hidden protected-coordinate recovery impossible

## Best Current Reading Paths

### Fast reviewer path
- [docs/finalization/architecture-final.md](docs/finalization/architecture-final.md)
- [docs/finalization/no-go-spine-final.md](docs/finalization/no-go-spine-final.md)
- [docs/physics/physics-system-matrix.md](docs/physics/physics-system-matrix.md)
- [docs/peer_review/physics-scope-and-limits.md](docs/peer_review/physics-scope-and-limits.md)

### Exact / physics path
- [docs/theorem-candidates/sector-recovery-theorems.md](docs/theorem-candidates/sector-recovery-theorems.md)
- [docs/mhd/divergence-cleaning-in-ocp.md](docs/mhd/divergence-cleaning-in-ocp.md)
- [docs/physics/maxwell-coulomb-gauge.md](docs/physics/maxwell-coulomb-gauge.md)
- [docs/physics/bounded-domain-projection-limits.md](docs/physics/bounded-domain-projection-limits.md)

### Interactive path
- [docs/workbench/index.html](docs/workbench/index.html)
- [docs/references/citable-expansion-directions.md](docs/references/citable-expansion-directions.md)
