# Quantum Alignment Audit

Status: exploratory claim audit of `/Users/stevenreid/Documents/New project/repos/topological-adam/Quantum_Alignment_Results_2026.docx` with recomputation in OCP artifacts.

Primary audit artifacts:
- `data/generated/quantum_alignment/audit_metrics.json`
- `data/generated/quantum_alignment/single_parameter_audit_table.csv`
- `data/generated/quantum_alignment/generalization_summary.csv`
- `figures/quantum_alignment/single_parameter_corrected_alpha_curves.png`

## Immediate high-priority check (single-parameter qubit section)

Starting claim in draft note:
- `|psi(theta)> = cos(theta/2)|0> + sin(theta/2)|1>`
- draft text said `Z` is blind and `X` has endpoint blind spots.

Recomputation result:
- `F_Q(theta) = 1` exactly.
- `F_M^Z(theta) = 1` for all interior points, with endpoint limits equal to `1`.
- `F_M^X(theta) = 1` for all interior points, with singular-point limits equal to `1`.
- Therefore `alpha_Q(theta,Z) = alpha_Q(theta,X) = 1` on this family.
- Blind-spot claim for this state family is incorrect.

Status label: `DISPROVED` (for the original blind-spot statement).

## Claim-by-claim audit

| ID | Draft claim | Recompute result | Status |
| --- | --- | --- | --- |
| A | `alpha_Q = sqrt(F_M/F_Q)` with `alpha_Q in [0,1]` | Correct as notation over Braunstein-Caves inequality | `KNOWN / REFRAMED` |
| B | Single-parameter section (`Z` blind, `X` endpoint blind spots) | Incorrect for the stated state family; corrected values are all `1` | `DISPROVED` |
| C | Two-parameter family `Rz(theta_2) Ry(theta_1) |0>` | Correct model; Bloch map and derivatives are standard | `KNOWN / REFRAMED` |
| D | QFIM at `(pi/3, pi/4)` equals `diag(1, 0.75)` | Correct at that point | `PROVED ON RESTRICTED CLASS` |
| E | SLD commutator norm nonzero (`2.449`) implies incompatibility | Nonzero commutator confirmed (Frobenius norm `2.4494897...`) | `KNOWN / REFRAMED` |
| F | Random search best balanced alpha (`~0.638`) used as practical limit | Random search can under-shoot optimum; explicit construction attains `1/sqrt(2)` exactly | `VALIDATED / NUMERICAL ONLY` (search value), interpretation corrected |
| G | `alpha_1^2 + alpha_2^2 = 1` in restricted projective qubit setting | Confirmed under restricted assumptions; extended coordinate-invariant trace form also verified on sampled rank-1 POVMs | `PROVED ON RESTRICTED CLASS` |

## Numeric checkpoints

At `(theta_1, theta_2) = (pi/3, pi/4)`:
- `F_Q = [[1, 0], [0, 0.75]]`.
- `||[L_1, L_2]||_F = 2.4494897447`.
- 500-random-projective search: best `min(alpha_1, alpha_2) = 0.7047567`.
- Explicit balanced construction: `(alpha_1, alpha_2) = (1/sqrt(2), 1/sqrt(2))`.

## Audit conclusion

What is correct:
- The restricted qubit tradeoff structure is real.
- The two-parameter projective identity survives on its declared class.

What is wrong and fixed:
- The one-parameter blind-spot section is wrong for the stated state family.
- Random-search underperformance is not a theorem bound.

What is reframed-known rather than novel:
- `F_M <= F_Q` bound and incompatibility interpretation.
- SLD noncommutation diagnostics.

