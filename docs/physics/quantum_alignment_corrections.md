# Quantum Alignment Corrections

Status: explicit correction log for the draft quantum-alignment note.

## Correction log

## C1. Single-parameter blind-spot claim

Original draft claim:
- For `|psi(theta)> = cos(theta/2)|0> + sin(theta/2)|1>`, `Z` is blind and `X` has endpoint blind spots.

Corrected result:
- `F_Q(theta) = 1`.
- `F_M^Z(theta) = 1` (interior), endpoint limits also `1`.
- `F_M^X(theta) = 1` (interior), singular-point limits also `1`.
- `alpha_Q(theta,Z) = alpha_Q(theta,X) = 1` for this family.

Status change:
- From implicit theorem-like interpretation to `DISPROVED` for the original statement.

Evidence:
- `data/generated/quantum_alignment/single_parameter_audit_table.csv`
- `figures/quantum_alignment/single_parameter_corrected_alpha_curves.png`

## C2. Geometric wording mismatch

Original wording issue:
- The note called the family an “XZ equator.”

Correction:
- This parameterization is a meridian (great-circle arc in the `x-z` plane with fixed azimuth), not a phase-equator sweep.

Status change:
- Wording corrected; this is a geometry description fix.

## C3. Random search interpretation

Original issue:
- Random measurement search (`500` samples) used as if near-optimal evidence.

Correction:
- Random search value is a computational witness only.
- Balanced projective direction is analytically constructible and attains exact optimum `1/sqrt(2)`.

Status change:
- Search result remains `VALIDATED / NUMERICAL ONLY`.
- Balanced bound remains `PROVED ON RESTRICTED CLASS`.

Evidence:
- `data/generated/quantum_alignment/audit_metrics.json`

## C4. Scope of conservation identity

Original risk:
- The draft identity could be read too broadly.

Correction:
- Identity is restricted unless assumptions are explicitly stated.
- The diagonal-coordinate form (`alpha_1^2 + alpha_2^2 = 1`) is parameterization-dependent.
- Coordinate-invariant form (`trace(F_Q^{-1} F_M) = 1`) is the cleaner restricted statement on the tested qubit class.

Status change:
- Scope tightened; over-broad reading removed.

## C5. Non-projective and mixed-state language

Original risk:
- Potential implication that the exact equality is universal.

Correction:
- Mixed states and unsharp/non-projective POVMs generally give strict loss relative to the exact restricted identity.
- Keep these as extension checks, not theorem-promotion cases.

Status change:
- Labeled `PROVED ON RESTRICTED CLASS` (inequality behavior) or `VALIDATED / NUMERICAL ONLY` where no proof is supplied.

## Likely root causes of the one-parameter error

1. Parameterization confusion:
- Mixing a polar-angle family with phase-equator intuition.

2. Singular-point handling:
- Treating `0/0` FI evaluation points as zero instead of taking analytic limits.

3. Narrative drift:
- Interpreting random-search artifacts as structural constraints.

## Corrected canonical one-parameter table

For `|psi(theta)> = cos(theta/2)|0> + sin(theta/2)|1>`:

| Quantity | Correct value |
| --- | --- |
| `F_Q(theta)` | `1` |
| `F_M^Z(theta)` | `1` (with endpoint limits `1`) |
| `F_M^X(theta)` | `1` (with singular-point limits `1`) |
| `alpha_Q(theta,Z)` | `1` |
| `alpha_Q(theta,X)` | `1` |

