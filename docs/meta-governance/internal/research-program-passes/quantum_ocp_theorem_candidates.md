# Quantum-OCP Theorem Candidates

Status: falsification-first theorem candidate slate; no promotion to canonical theorem spine in this pass.

Primary data source:
- `data/generated/quantum_ocp/quantum_witness_catalog.csv`
- `data/generated/quantum_ocp/quantum_anomaly_catalog.csv`

## QT1. Basis-Sensitive Opposite-Verdict Split

Statement (supported family):
For the two-state equatorial qubit family `{phi=pi/3, 2pi/3}` with target `sign(cos(phi))`, one-setting Z-basis measurement is not exactly recoverable while one-setting X-basis measurement is exactly recoverable, despite identical descriptor `(dimension=2, measurement_count=1)`.

Evidence:
- `QW001` (`exact_recoverable=0`), `QW002` (`exact_recoverable=1`), `QA001`.

Status:
- Mathematical status: `PROVED ON SUPPORTED FAMILY`.
- Novelty status: `CLOSE PRIOR ART / REPACKAGED`.

Why kept:
- Serves as exact anti-classifier quantum witness beyond QEC anchor.

## QT2. Conditioned vs Invariant Recoverability Split (Quantumized Context Family)

Statement (supported family):
In the context-gain qubit family with contexts `y_c = a_c x`, each context is exactly recoverable for target `x` but there is no shared context-invariant decoder when gains differ (`a1 != a2`).

Evidence:
- `QW005-QW008`: `conditioned_exact=1`, `invariant_exact=0` for all sampled non-matching gains.
- `QA005`.

Status:
- Mathematical status: `PROVED ON SUPPORTED FAMILY`.
- Novelty status: `PLAUSIBLY DISTINCT` (packaging/criterion), not new foundational quantum theorem.

Limits:
- This is a finite linearized context model, not a universal basis/context theorem.

## QT3. One-Added-Measurement Restoration (Finite Discrete Family)

Statement (supported family):
For the sampled discrete qubit phase family, X-only one-setting records fail exact full-phase recovery, while adding one complementary Y-setting restores exact recovery.

Evidence:
- `QW003` (`exact_recoverable=0`), `QW004` (`exact_recoverable=1`), `QA006`.

Status:
- Mathematical status: `PROVED ON SUPPORTED FAMILY`.
- Novelty status: `CLOSE PRIOR ART / REPACKAGED`.

Limits:
- Scoped to sampled finite family and chosen target map.

## QT4. Distributed Allocation Geometry Split

Statement (supported family):
For the two-qubit correlation target `c=<ZZ>`, same distributed budget (`measurement_count=2`) can yield opposite exactness: local-local allocation fails, while joint-plus-local allocation succeeds.

Evidence:
- `QW009` fail vs `QW010` succeed, `QA002`, `QA007`.

Status:
- Mathematical status: `PROVED ON SUPPORTED FAMILY`.
- Novelty status: `PLAUSIBLY DISTINCT` as a target-specific distributed recoverability package.

Limits:
- Does not claim new multipartite quantum theorem beyond scoped witness class.

## QT5. Decoherence Threshold in Target Recoverability (Known-Mechanism Benchmark)

Statement (supported family):
In the dephasing family used here, target recoverability for `sign(cos(phi))` under X-basis record survives for `p<0.5` and collapses at `p=0.5`.

Evidence:
- `QW011-QW017`, `QA008`.

Status:
- Mathematical status: `PROVED ON SUPPORTED FAMILY`.
- Novelty status: `ALREADY KNOWN IN SUBSTANCE`.

Role:
- Fragility benchmark feeding OCP persistence language; not novelty lane.

## QT6. Fisher-Split Design Signal (Conditional)

Statement (empirical/diagnostic):
At fixed setting count, phase-blind and phase-sensitive measurement choices produce sharply different target Fisher information in the sampled phase range.

Evidence:
- `QW019-QW024`, `QA009`.

Status:
- Mathematical status: `VALIDATED / EMPIRICAL ONLY`.
- Novelty status: `CLOSE PRIOR ART / REPACKAGED`.

Limits:
- No new exact theorem recovered from Fisher lane in this pass.

## QT7. QEC Exact Anchor Confirmation

Statement:
Three-qubit bit-flip anchor satisfies Knill-Laflamme exactness in existing repo implementation.

Evidence:
- `QW018`; existing `tests/math/test_qec_knill_laflamme.py`.

Status:
- Mathematical status: `PROVED ON SUPPORTED FAMILY`.
- Novelty status: `ALREADY KNOWN IN SUBSTANCE`.

Role:
- Anchor only, used to calibrate claims outside QEC.

## Candidate Promotion Filter

Candidates with plausible promotion potential (adjacent lane only):
1. `QT2` conditioned-vs-invariant split (quantumized context package).
2. `QT4` distributed allocation geometry split.

Candidates to keep as benchmark/known-core:
- `QT1`, `QT3`, `QT5`, `QT7`.

Candidate to keep conditional:
- `QT6` Fisher design split.
