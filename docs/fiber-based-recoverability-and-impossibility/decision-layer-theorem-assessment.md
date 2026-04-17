# Decision-Layer Theorem Assessment

## Scope

This file assesses theorem candidates for the proposed stopping / switch / augment layer.

The key standard is strict:
- keep only theorem-grade or theorem-linked corollaries that survive falsification,
- reject anything that is just vague decision language.

## Candidate Table

| Candidate | Verdict | Why |
| --- | --- | --- |
| Impossibility-implies-stop theorem | `PROVED` as a corollary | If the target varies on active fibers, exact pursuit is structurally futile. This is useful, but mathematically close to existing impossibility theorems. |
| Weaker-target switch theorem | `PROVED` as a corollary | If strong target exactness fails but a weaker target is exact on the same record, switching target is justified. Strongest clean support: `OCP-048`, `OCP-051`. |
| Augmentation-vs-stop theorem | `CONDITIONAL` | Strong on restricted-linear families once an external budget is fixed. Without budget, the theorem becomes only “augmentation exists.” |
| Anti-classifier stopping theorem | `PROVED` negative theorem | Any stop/continue rule based only on rank/count/budget is unsound on supported families. Strongest support: `OCP-049`, `OCP-050`. |
| Instability-aware stopping criterion | `CONDITIONAL` | Works relative to a tolerated error scale using collapse or mismatch bounds; the tolerance is external, so this is not a standalone theorem. |
| Family-restriction caution theorem | `PROVED` on the supported family-enlargement class | `OCP-052` gives a clean stop-promotion rule when exactness breaks immediately under enlargement. |
| Universal stopping law | `DISPROVED` | The branch has no honest universal scalar or amount-only stopping law. |

## Strongest surviving statements

### 1. Exact-futility corollary
If exact recovery is impossible on the chosen family, target, and record, then continuing an exact-recovery claim is structurally futile.

Status:
- `PROVED` as a decision corollary of fiber-mixing impossibility.

### 2. Target-switch corollary
If the stronger target fails but a weaker target is exact on the same fibers, the structurally correct action is to switch target rather than continue strong-target exact pursuit.

Status:
- `PROVED` as a decision corollary of the target-hierarchy results.

### 3. Fragile-positive caution corollary
If exactness holds only on a narrow family and fails immediately on supported enlargement, the correct action is to stop promoting the result as robust.

Status:
- `PROVED` on the supported restricted-linear enlargement class.

## Honest conclusion

This pass did **not** uncover a new standalone theorem family.

It did uncover a real theorem-linked decision layer built from:
- impossibility,
- weaker-target exactness,
- minimal augmentation,
- family fragility,
- and model-mismatch instability.
