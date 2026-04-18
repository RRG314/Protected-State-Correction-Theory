# Quantum Alignment Reference Map

Status: branch-specific claim-to-literature map for safe positioning.

## Claim map

| Claim / object | Nearest reference zone | Overlap level | Safe status wording |
| --- | --- | --- | --- |
| `F_M <= F_Q` and `alpha_Q` ratio notation | Helstrom; Braunstein-Caves | Direct overlap | `KNOWN / REFRAMED` |
| SLD noncommutation as incompatibility signal | Matsumoto; Holevo multiparameter estimation | Direct overlap | `KNOWN / REFRAMED` |
| Restricted projective qubit alpha-circle identity | qubit multiparameter Fisher tradeoffs; Gill-Massar-style trace bounds | High overlap risk | `PROVED ON RESTRICTED CLASS`; novelty `OPEN / likely close prior art` |
| Coordinate-invariant trace form on restricted qubit class | attainable qubit Fisher matrix region (`trace(F_Q^{-1}F_M)` constraints) | High overlap risk | `PROVED ON RESTRICTED CLASS`; novelty `CLOSE PRIOR ART / REPACKAGED` |
| Unsharp/mixed attenuation | standard noisy-measurement FI loss | Direct overlap | `KNOWN IN SUBSTANCE` |
| Higher-dimensional collapse of qubit constant | known dimension-dependent multiparameter geometry | Direct overlap | `KNOWN IN SUBSTANCE` (negative boundary) |

## Minimal reference anchors to cite in this lane

1. C. W. Helstrom, *Quantum Detection and Estimation Theory* (1976).
2. S. L. Braunstein and C. M. Caves, “Statistical distance and the geometry of quantum states” (1994).
3. A. S. Holevo, multiparameter quantum estimation bounds (canonical monograph-level treatment).
4. K. Matsumoto, multiparameter SLD/Holevo compatibility treatments.
5. R. D. Gill and S. Massar, qubit attainable Fisher-information trace constraints (`trace(F_Q^{-1}F_M)` family).

## Repo claim discipline

For this branch, every public-facing statement should include:
- class scope (qubit/pure/mixed/projective/rank-1 POVM),
- status label,
- literature-overlap label,
- explicit nonclaim against universal novelty.

