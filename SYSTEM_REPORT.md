# System Report

## Executive Summary

This repository is now a serious OCP research-program base rather than a concept note.

The strongest current picture is:
- exact protected-state correction in finite-dimensional and QEC-style settings,
- exact continuous correction through periodic Helmholtz/Leray projection,
- asymptotic correction through damping generators and GLM-style cleaning,
- and a no-go program that now includes both overlap failure and linear-flow mixing failure.

The program is more grounded than before because the next-step continuous-time target was actually pursued and it held up:
- the repo now proves an invariant-split generator theorem,
- proves a self-adjoint PSD corollary,
- and proves a new linear-flow failure criterion showing when disturbance leaks into the protected coordinates.

## Repository Inventory

High-level file totals:
- tracked-like files in repo inventory: `89`
- root files: `12`
- docs files: `25`
- theory files: `7`
- papers files: `6`
- source files: `10`
- test files: `10`
- script files: `6`
- data/generated files: `5`
- archive/raw-import files: `8`

Machine-readable inventory:
- [repo_file_inventory.csv](data/generated/inventories/repo_file_inventory.csv)
- [system_summary.json](data/generated/validations/system_summary.json)

## Theory Inventory

### Core formalism
- [formal-theory.md](docs/formalism/formal-theory.md)
- [exact-vs-asymptotic.md](docs/formalism/exact-vs-asymptotic.md)

### Exact theorem spine
- [central-theorem.md](docs/theorem-candidates/central-theorem.md)
- exact orthogonal protected-subspace recovery

### Continuous-time strengthening
- [generator-theorems.md](docs/theorem-candidates/generator-theorems.md)
- invariant-split generator theorem
- self-adjoint PSD corollary with spectral-gap bound

### No-go spine
- [no-go-results.md](docs/impossibility-results/no-go-results.md)
- overlap/indistinguishability no-go
- non-preserving correction disqualification
- linear-flow mixing no-go
- no universal scalar-capacity promotion

## Systems Inventory

### 1. Finite-dimensional exact branch

Status: `strong exact anchor`

Protected object:
- orthogonal protected subspace `S`

Disturbance:
- orthogonal disturbance subspace `D`

Correction structure:
- orthogonal projector `P_S`
- complementary projector `P_D`

Main result:
- exact recovery theorem

### 2. QEC branch

Status: `exact anchor under standard assumptions`

Protected object:
- code space

Disturbance:
- error sectors

Correction structure:
- Knill-Laflamme-compatible recovery
- explicit 3-qubit bit-flip sector projectors and coherent recovery operators

Main result:
- exact sector recovery on the locally tested single-bit-flip family

### 3. MHD projection branch

Status: `strongest exact continuous anchor`

Protected object:
- divergence-free field component

Disturbance:
- gradient contamination / divergence-producing component

Correction structure:
- modewise periodic Helmholtz/Leray projection

Main result:
- the local implementation now behaves as a real projector in the tested periodic setting

### 4. GLM branch

Status: `useful asymptotic branch, not exact`

Protected object:
- physical divergence-free content

Disturbance:
- constraint-violating component

Correction structure:
- auxiliary-field transport plus damping

Main result:
- empirical divergence reduction in the test setting
- clearly weaker than exact projection in one-shot correction strength

### 5. Linear generator branch

Status: `new strong grounded branch`

Protected object:
- invariant protected subspace `S`

Disturbance:
- invariant disturbance subspace `D`

Correction structure:
- linear generator `K` with `K|_S = 0`, `K(D) ⊆ D`, and stable restriction on `D`

Main result:
- invariant-split generator theorem
- self-adjoint PSD corollary
- mixing no-go criterion

### 6. Control branch

Status: `conditional extension`

Protected object:
- system-dependent invariant or tracked coordinates

Disturbance:
- error or unstable deviation coordinates

Correction structure:
- controller or observer acting on disturbance coordinates

Main result:
- structural design rules, not a broad control theorem yet

### 7. Weak branches

Status: `demoted`

Includes:
- optimizer / ML bridge material
- broad cross-domain analogy language without operator content
- universal scalar-capacity claims

## Results Inventory

### Proved
- OCP-001 formal OCP tuple
- OCP-002 exact orthogonal projection theorem
- OCP-003 indistinguishability no-go
- OCP-004 continuous damping theorem for `k P_D`
- OCP-006 Helmholtz/Leray exact continuous anchor
- OCP-013 invariant-split generator theorem
- OCP-014 self-adjoint PSD corollary
- OCP-015 mixing no-go for linear flows

### Conditional but serious
- OCP-005 QEC exact anchor
- OCP-007 GLM as asymptotic OCP
- OCP-008 control-theoretic instantiation
- OCP-011 engineering design value
- OCP-012 exact-to-asymptotic bridge

### Open or not yet worth promoting
- OCP-009 universal scalar correction capacity
- OCP-010 current optimizer/ML extension

Primary status tables:
- [claim-registry.md](docs/overview/claim-registry.md)
- [proof-status-map.md](docs/overview/proof-status-map.md)

## Operator Inventory

Exact operators:
- `P_S` exact protected-subspace projector
- `P_D` complementary disturbance projector
- QEC code projector and sector projectors
- periodic discrete Helmholtz/Leray projector

Asymptotic operators/laws:
- `x_dot = -k P_D x`
- general linear generator `x_dot = -Kx` under invariant-split hypotheses
- GLM step operator

Failure operators / diagnostics:
- block-decomposition test for `P_S K P_D`
- report of protected mixing and disturbance preservation in [continuous.py](src/ocp/continuous.py)

## Validation Inventory

Current validation status:
- full validation script passes
- markdown link check passes
- test suite result: `14 passed`

Test coverage areas:
- exact projector recovery
- repeated exact recovery under random orthogonal splits
- overlap failure
- QEC KL check
- QEC sector orthogonality
- QEC explicit recovery
- MHD projection recovery
- MHD idempotence / reconstruction
- GLM divergence reduction
- invariant-split generator theorem examples
- PSD spectral-gap bound examples
- mixing failure examples
- repeated diagonal PSD generator family checks

Primary validation entry points:
- [run_all.sh](scripts/validate/run_all.sh)
- [operator_examples.json](data/generated/validations/operator_examples.json)

## Generated Results Snapshot

### Finite OCP example
- initial disturbance energy: `2.8125`
- corrected disturbance energy at `t=2`: `0.0515`

### QEC example
- Knill-Laflamme residual: `0.0`
- pairwise image overlap: `0.0`
- sector recovery errors: `[0.0, 0.0, 0.0, 0.0]`

### MHD example
- divergence before projection: `19.3592`
- divergence after projection: `2.36e-14`
- divergence after GLM test run: `16.8499`
- projection orthogonality residual: `1.97e-16`

### Continuous generator examples
- invariant-split example preserves the protected coordinate exactly and shrinks disturbance norm from `1.1180` to `0.2223`
- self-adjoint PSD example obeys the spectral-gap bound
- mixing-failure example changes the protected coordinate from `0.0` to `-0.3934` by `t=0.5`, confirming the no-go criterion

## What Became More Real In This Pass

The repo is more real and grounded now in four specific ways:
- the continuous-time branch is no longer only the projector special case,
- the linear-flow failure criterion is explicit and tested,
- the MHD discrete projector now matches the exact-projector story much more faithfully,
- and the repo has a full inventory-level system report rather than only a summary report.

## Viable Next Directions

Ranked viable directions:
1. boundary-sensitive continuous OCP for constrained PDE correction
2. category-specific correction-capacity theory
3. stronger sector-based OCP examples beyond the 3-qubit anchor only if they sharpen the theory
4. stronger no-go results for insufficient correction image or detectability
5. continuous quantum feedback only if it can be written in real operator language

Dedicated note:
- [viable-next-directions.md](docs/open-questions/viable-next-directions.md)

## Directions That Should Stay Unpromoted For Now

- optimizer/ML unification claims
- universal scalar-capacity claims
- diffuse cross-domain rhetoric without stronger operator or theorem content

## Overall Assessment

Current overall assessment: `GOOD`, with a stronger theorem spine than before.

Why it improved:
- the next-target generator program produced real theorem-level output
- the no-go program became sharper
- the exact continuous anchor became cleaner at the implementation level
- the validation layer is broader and deeper

Why it is still not `EXCELLENT`:
- the most distinctive results are still framework-level and operator-level rather than a clearly field-defining new theorem
- the control branch remains conditional
- category-specific capacity theory is still open
- the broader continuous/PDE boundary program is still ahead rather than complete
