# System Report

## Executive Summary

This repository has now crossed from a good formal build into a finished program state.

The strongest current picture is:
- exact protected-state correction through orthogonal projectors,
- exact sector recovery through orthogonal sector embeddings,
- exact periodic continuous projection through the Helmholtz/Leray anchor,
- asymptotic continuous correction through invariant-split generators,
- and a no-go layer strong enough to police overlap, mixing, sector ambiguity, insufficient correction image, and finite-time overclaiming.

The workbench layer is now real as well:
- static,
- GitHub-Pages-compatible,
- and tied directly to theorem or no-go files.

## Repository Inventory

High-level file totals from the generated inventory:
- tracked-like files: `131`
- root files: `12`
- archive files: `8`
- data files: `6`
- docs files: `55`
- papers files: `6`
- scripts files: `8`
- source files: `14`
- test files: `15`
- theory files: `7`

Machine-readable inventory:
- [data/generated/inventories/repo_file_inventory.csv](data/generated/inventories/repo_file_inventory.csv)
- [data/generated/validations/system_summary.json](data/generated/validations/system_summary.json)

## Claim Inventory

Current promoted/registered claim totals:
- total tracked claims: `21`
- `PROVED`: `12`
- `CONDITIONAL`: `7`
- `OPEN`: `1`
- `ANALOGY ONLY`: `1`

Primary claim artifacts:
- [docs/overview/claim-registry.md](docs/overview/claim-registry.md)
- [docs/overview/proof-status-map.md](docs/overview/proof-status-map.md)

## Theory Inventory

### Finalization layer
- [docs/finalization/theorem-spine-final.md](docs/finalization/theorem-spine-final.md)
- [docs/finalization/no-go-spine-final.md](docs/finalization/no-go-spine-final.md)
- [docs/finalization/operator-spine-final.md](docs/finalization/operator-spine-final.md)
- [docs/finalization/architecture-final.md](docs/finalization/architecture-final.md)

### Exact branch
- [docs/theorem-candidates/central-theorem.md](docs/theorem-candidates/central-theorem.md)
- [docs/theorem-candidates/sector-recovery-theorems.md](docs/theorem-candidates/sector-recovery-theorems.md)
- [docs/theorem-candidates/capacity-theorems.md](docs/theorem-candidates/capacity-theorems.md)

### Continuous / asymptotic branch
- [docs/theorem-candidates/generator-theorems.md](docs/theorem-candidates/generator-theorems.md)
- [docs/mhd/divergence-cleaning-in-ocp.md](docs/mhd/divergence-cleaning-in-ocp.md)
- [docs/mhd/glm-and-asymptotic-correction.md](docs/mhd/glm-and-asymptotic-correction.md)

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
Status: `new finished exact branch`
- protected object: `S`
- disturbance object: pairwise orthogonal sector family `D_i`
- operator: global sector-conditioned recovery built from `Q_i` and sector basis maps
- main results: OCP-T5, OCP-N8

### 3. QEC branch
Status: `exact anchor under standard assumptions`
- protected object: code space
- disturbance object: correctable syndrome sectors
- operator: sector projectors and coherent recovery family
- main result: exact recovery on the local 3-qubit bit-flip family

### 4. Exact continuous periodic branch
Status: `strong exact continuous anchor`
- protected object: divergence-free field component
- disturbance object: gradient contamination
- operator: periodic Helmholtz/Leray projection
- main result: exact machine-precision recovery in the tracked example

### 5. Asymptotic continuous generator branch
Status: `finished asymptotic branch`
- protected object: `ker(K)` or invariant protected coordinates
- disturbance object: stable disturbance subspace
- operator: damping or invariant-split generator `K`
- main results: OCP-T2, OCP-T3, OCP-C2, OCP-N5, OCP-N7

### 6. GLM branch
Status: `kept as asymptotic only`
- protected object: physical field content
- disturbance object: divergence / constraint error
- operator: coupled GLM update law
- main value: practical asymptotic comparator, not exact recovery

### 7. Control branch
Status: `conditional extension`
- value: design-rule and interpretation layer
- limitation: no fully promoted broad control theorem yet

### 8. Demoted branch
- optimizer / ML bridge material
- universal scalar-capacity language

## Operator Inventory

Exact operators:
- `P_S`
- `P_D`
- sector projectors `Q_i`
- global sector recovery operator
- code projector and QEC recovery family
- periodic Helmholtz/Leray projector

Asymptotic operators:
- `x_dot = -k P_D x`
- invariant-split generators `x_dot = -Kx`
- GLM update law

Failure diagnostics:
- overlap / intersection checks
- protected mixing norm `||P_S K P_D||`
- exact-recovery residual for finite-time flows
- rank / image lower-bound checks

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
- Continuous Generator Lab
- No-Go Explorer

## Validation Inventory

Validation status:
- full validation script: passed
- static workbench asset check: passed
- markdown link check: passed
- Node workbench tests: `7 passed`
- Python theorem/operator tests: `23 passed`

Primary validation entry points:
- [scripts/validate/run_all.sh](scripts/validate/run_all.sh)
- [scripts/validate/check_workbench_static.py](scripts/validate/check_workbench_static.py)
- [scripts/compare/build_workbench_examples.mjs](scripts/compare/build_workbench_examples.mjs)

Primary generated artifacts:
- [data/generated/validations/operator_examples.json](data/generated/validations/operator_examples.json)
- [data/generated/validations/workbench_examples.json](data/generated/validations/workbench_examples.json)

## Results Snapshot

### Exact and sector branches
- QEC sector recovery errors: `[0.0, 0.0, 0.0, 0.0]`
- sector-theorem recovery errors: `[0.0, 0.0, 0.0, 0.0]`

### Continuous exact vs asymptotic branch
- divergence before exact projection: `19.359218295532003`
- divergence after exact projection: `2.359146931297974e-14`
- divergence after short GLM run: `16.849909741931956`

### Finite-time flow boundary
- finite-time exact recovery possible at `t = 0.25, 1.0, 2.0`: `false, false, false`
- corresponding exact-recovery residuals: `1.0547, 0.5186, 0.2238`

## Best Current Reading Paths

### Short exact path
- [docs/finalization/architecture-final.md](docs/finalization/architecture-final.md)
- [docs/theorem-candidates/sector-recovery-theorems.md](docs/theorem-candidates/sector-recovery-theorems.md)
- [docs/impossibility-results/advanced-no-go-results.md](docs/impossibility-results/advanced-no-go-results.md)

### Reviewer path
- [docs/peer_review/how-to-read-this-repo.md](docs/peer_review/how-to-read-this-repo.md)
- [docs/peer_review/proof-status-for-reviewers.md](docs/peer_review/proof-status-for-reviewers.md)

### Interactive path
- [docs/workbench/index.html](docs/workbench/index.html)
