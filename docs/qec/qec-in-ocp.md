# QEC Rewritten In OCP Language

## Plain-Language Summary

QEC fits OCP best when OCP is written as a **protected-space plus distinguishable error-sector** framework, not as a single vague analogy.

The protected state is the code space. The disturbance sectors are the error images. The recovery acts on the error sector while restoring the protected logical state.

## 1. OCP Translation Dictionary

| QEC language | OCP language |
| --- | --- |
| code space `C` | protected subspace `S` |
| physical error set `{E_a}` | disturbance family |
| syndrome sector `E_a C` | disturbance sector `D_a` |
| syndrome extraction | distinguishability mechanism |
| recovery map | correction operator |
| Knill-Laflamme condition | exact correctability criterion |

## 2. Sector-Based OCP Formulation

The right exact OCP formulation for QEC is:

```text
(H_phys, S, {D_a}, {R_a})
```

where
- `S = C` is the code space,
- `D_a = E_a S` are disturbance sectors,
- `R_a` are sector-conditioned recovery maps.

The sector structure matters. QEC is not just “project away the error.” It is “identify the error sector and map it back to the protected sector without disturbing logical data.”

## 3. Why Knill-Laflamme Fits OCP

Knill-Laflamme guarantees that the chosen error family does not destroy the logical information needed for recovery.

In OCP terms, it ensures that:
- the disturbance sectors are compatible with a recovery architecture,
- the protected information is not mixed irreversibly into the disturbance family,
- and the recovery can act on the error label without corrupting the logical state.

That is an exact protected-state correction system.

## 3.5 Local Operator Construction

The repository now includes an explicit sector-based recovery construction for the 3-qubit bit-flip code:
- sector projectors onto `I C`, `X_1 C`, `X_2 C`, and `X_3 C`,
- a recovery-operator family that maps each sector back to the code space,
- and a local test showing exact recovery on each tested single-bit-flip sector.

This matters because the QEC branch is not only interpretive. It also contains a concrete recovery construction.

## 4. What Orthogonality Means Here

Orthogonality in QEC is not always “one disturbance subspace `D` orthogonal to one protected space `S`.”

Instead, the important orthogonality is often sector orthogonality or syndrome distinguishability:
- different correctable error images must be separable enough,
- and recovery must not confuse one sector for another.

So QEC expands the OCP concept beyond the strict projector model while staying exact.

## 5. What QEC Adds To OCP

QEC contributes three things that the simple projector model does not capture by itself:
- indexed disturbance sectors instead of one disturbance space,
- measurement or syndrome information as part of the correction structure,
- and a precise correctability theorem already known in the literature.

## 6. What OCP Adds To QEC

OCP does not replace QEC language. It adds a cross-domain interpretation:
- protected-state preservation,
- distinguishable disturbance sectors,
- exact vs asymptotic correction categories,
- and no-go emphasis when distinguishability fails.

That makes OCP best understood as a structural reinterpretation of QEC’s correction logic, not as a competing theory of quantum codes.

## 7. Current Status

This QEC branch is best classified as:
- **exact anchor**,
- **conditional on standard QEC assumptions**,
- **useful for formalization and positioning**,
- **not claimed as a new QEC theorem**.
