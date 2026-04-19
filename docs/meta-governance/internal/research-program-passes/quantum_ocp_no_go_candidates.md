# Quantum-OCP No-Go Candidates

Status: no-go candidates extracted under falsification-first discipline.

Evidence sources:
- `data/generated/quantum_ocp/quantum_witness_catalog.csv`
- `data/generated/quantum_ocp/quantum_anomaly_catalog.csv`

## QN1. Fixed-Basis Fiber-Collision No-Go

Statement:
In the sampled qubit phase-sign family, Z-basis one-setting records collide across distinct target values, so exact target recovery is impossible.

Evidence:
- `QW001`, `QA004`.

Status:
- `PROVED ON SUPPORTED FAMILY`
- Novelty: `ALREADY KNOWN IN SUBSTANCE`

## QN2. Descriptor-Only Classifier No-Go (Quantum Analog)

Statement:
Descriptors based on dimension/setting count/context count do not classify target recoverability in sampled quantum families.

Evidence:
- `QA001`, `QA002`, `QA003` (three descriptor signatures with opposite verdicts).

Status:
- `PROVED ON SUPPORTED FAMILY`
- Novelty: `PLAUSIBLY DISTINCT` as a cross-lane packaging claim; mechanism is close to known practice.

## QN3. Context-Invariant Decoder No-Go Under Gain Mismatch

Statement:
For context-gain family `y_c = a_c x`, when `a1 != a2` there is no shared linear decoder recovering `x` across both contexts even though each context alone is exact.

Evidence:
- `QW005-QW008`, `QA005`.

Status:
- `PROVED ON SUPPORTED FAMILY`
- Novelty: `PLAUSIBLY DISTINCT` (context-sensitive recoverability framing).

## QN4. Distributed Local-Only Allocation No-Go for Correlation Target

Statement:
For the two-qubit family used here, local-local allocation `(ZI, IZ)` is target-blind for `ZZ` correlation and cannot recover the target exactly.

Evidence:
- `QW009`, `QA007`.

Status:
- `PROVED ON SUPPORTED FAMILY`
- Novelty: `CLOSE PRIOR ART / REPACKAGED`.

## QN5. Complete-Dephasing Collapse No-Go

Statement:
In the sampled dephasing family, complete dephasing (`p=0.5`) eliminates target sensitivity for the chosen phase-sign target under X-basis readout.

Evidence:
- `QW017`, `QA008`.

Status:
- `PROVED ON SUPPORTED FAMILY`
- Novelty: `ALREADY KNOWN IN SUBSTANCE`.

## QN6. Broad “OCP gives new quantum foundations” No-Go

Statement:
The pass does not support promoting OCP as a replacement or foundational extension of quantum mechanics.

Evidence:
- Literature overlap audit + falsification attacks.

Status:
- `DISPROVED / COLLAPSED` (as a broad claim).

## No-Go Set To Keep

Keep for quantum adjacent lane:
- QN2, QN3, QN4 (scoped no-go/design package).

Keep as known benchmark no-go:
- QN1, QN5.

Reject as overreach:
- QN6 broad foundational narrative.
