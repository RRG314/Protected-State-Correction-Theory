# Field Dictionary Overview

## Purpose

This branch does not assume that all fields mean exactly the same thing by recovery, detectability, or impossibility.
The point of the dictionary is to show:
- where the match is exact,
- where it is restricted,
- and where it is only analogy.

## Summary table

| Field | Native question | Branch match strength | Strongest kept mapping | Strongest limitation |
| --- | --- | --- | --- | --- |
| Information theory | what information survives a lossy channel or statistic? | restricted but clean | exact recovery as factorization through a channel/statistic on an admissible family | branch does not replace full Shannon theory or channel coding |
| Coding theory | detect vs correct vs neither | clean | syndrome/received-word collisions map directly to weaker-vs-stronger target logic | full code-distance theory is not re-derived here |
| Inverse problems | can causes be reconstructed from effects, and how stably? | clean | fiber collisions = nonuniqueness; collapse modulus = ambiguity/stability object | branch does not solve general regularization theory |
| Control / observability | can state or functionals be reconstructed from outputs/history? | clean but not identical | restricted linear exactness and finite-history/asymptotic splits | branch detectability-only is not the full classical detectability notion |
| QEC | can logical data be exactly recovered after allowed errors? | exact on the anchor level | Knill-Laflamme fits target preservation plus sector distinguishability | general QEC remains a standard external theory, not a repo novelty claim |
| CFD / PDE | which flow quantities survive sparse records or projection choices? | restricted but strong | divergence-only no-go, periodic/bounded split, weaker-vs-stronger flow targets | broad PDE inverse theory is outside current exact scope |
| MHD | which closures or reduced descriptions preserve the target structure? | partial / restricted | explicit exact-family survival and obstruction language on restricted families | general realistic MHD recoverability is not proved here |

## Reading path

- [information-theory.md](information-theory.md)
- [coding-theory.md](coding-theory.md)
- [inverse-problems.md](inverse-problems.md)
- [control-observability.md](control-observability.md)
- [qec.md](qec.md)
- [cfd-pde.md](cfd-pde.md)
- [mhd.md](mhd.md)

## Main interpretive rule

The branch is strongest when it says:
- “these fields share the same obstruction shape,”
not when it says:
- “these fields are secretly the same theory.”
