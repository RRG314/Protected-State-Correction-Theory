# Quantum Alignment Generalization Report

Status: falsification-first extension sweep beyond the restricted two-parameter projective qubit statement.

Primary artifact:
- `data/generated/quantum_alignment/generalization_summary.csv`

Supporting artifacts:
- `data/generated/quantum_alignment/audit_metrics.json`
- `figures/quantum_alignment/two_parameter_tradeoff_circle.png`
- `figures/quantum_alignment/generalization_survival_map.png`

## Executive summary

The original scalar identity survives only in a scoped qubit class and fails as a universal law. A coordinate-invariant trace form survives much better on qubits, but higher-dimensional and non-projective settings break the exact qubit conservation constant.

## Case summary

| Case | Setting | Observed result | Status |
| --- | --- | --- | --- |
| G0 | pure qubit, 2-parameter, diagonal QFIM, projective | `alpha_1^2 + alpha_2^2 = 1` | `PROVED ON RESTRICTED CLASS` |
| G1 | pure qubit, rank-1 4-outcome POVM | same scalar sum remains `1` | `PROVED ON RESTRICTED CLASS` |
| G2 | mixed qubit, projective | scalar sum drops below `1` in interior mixed regimes | `PROVED ON RESTRICTED CLASS` |
| G3 | pure qubit, unsharp non-projective POVM | scalar sum strictly below `1` for `eta < 1` | `PROVED ON RESTRICTED CLASS` |
| G4 | pure qubit, non-diagonal QFIM coordinates | diagonal-ratio sum is not constant | `DISPROVED` |
| G5 | same as G4 | `trace(F_Q^{-1}F_M)=1` survives | `PROVED ON RESTRICTED CLASS` |
| G6 | pure qutrit, 2-parameter, random projective basis | trace metric varies over roughly `[0,2]` | `DISPROVED` (as qubit-style constant) |
| G7 | mixed qubit, 3-parameter | trace metric numerically concentrates at `1` | `VALIDATED / NUMERICAL ONLY` |
| G8 | pure qutrit, 3-parameter | no fixed conserved constant observed | `VALIDATED / NUMERICAL ONLY` |

## Requested extension checks (A-E)

## A) Mixed states

Result:
- Exact qubit scalar equality does not persist generically.
- Mixed-state orientation sweeps show strict attenuation below `1` except near boundary limits.

Status:
- `PROVED ON RESTRICTED CLASS` for attenuation behavior in tested interior regimes.

## B) Non-projective POVMs

Result:
- For unsharp two-outcome POVMs (`eta < 1`), the exact scalar equality collapses.
- For rank-1 qubit POVMs, the trace form remains exact on the tested class.

Status:
- Unsharp attenuation: `PROVED ON RESTRICTED CLASS`.
- Rank-1 extension: `PROVED ON RESTRICTED CLASS`.

## C) Non-diagonal QFIM

Result:
- Diagonal-coordinate sum (`J11/F11 + J22/F22`) is not invariant and fails as a theorem statement.
- Coordinate-invariant trace form remains exact on the restricted qubit class.

Status:
- Diagonal scalar claim: `DISPROVED` (as coordinate-free law).
- Trace form: `PROVED ON RESTRICTED CLASS`.

## D) Higher-dimensional systems

Result:
- Qubit conservation constant does not transfer directly to qutrit settings.

Status:
- `DISPROVED` as a universal extension of the qubit scalar identity.

## E) More than two parameters

Result:
- Mixed-qubit 3-parameter sweeps show a stable trace pattern (`~1`) but this remains unproved in this pass.
- Qutrit 3-parameter sweeps do not show a fixed constant.

Status:
- Qubit 3-parameter trace behavior: `VALIDATED / NUMERICAL ONLY`.
- Higher-dimensional >2-parameter universal law: `OPEN` / unsupported.

## Generalization conclusion

What survives:
- A narrow qubit measurement-compatibility package with exact restricted identities.

What fails:
- Any universal reading of `alpha_1^2 + alpha_2^2 = 1` across coordinates, POVM classes, mixed-state classes, and higher-dimensional systems.

