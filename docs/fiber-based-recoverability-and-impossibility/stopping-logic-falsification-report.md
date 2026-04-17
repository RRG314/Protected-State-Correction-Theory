# Stopping-Logic Falsification Report

## Purpose

This report records how the stopping idea was attacked.

## Failure modes tested

### 1. “Stop” is just another word for “impossible”
Result:
- partly true.

Assessment:
- the pure stop condition adds little beyond impossibility,
- but the switch-target, augment, architecture-change, and stop-promotion cases add real structure.

### 2. The layer adds nothing beyond minimal augmentation
Result:
- false as a blanket objection.

Assessment:
- augmentation alone does not decide whether to stop,
- because budget and family fragility matter,
- and weaker-target or architecture-switch decisions are genuinely different from augmentation.

### 3. The layer collapses into rank/count heuristics
Result:
- rejected by theorem.

Assessment:
- amount-only stopping rules fail for the same reason amount-only exactness rules fail.
- Strong support: `OCP-049`, `OCP-050`.

### 4. The layer could falsely promote target switching when exact recovery is still possible
Result:
- controlled successfully.

Assessment:
- the branch keeps switch-target recommendations only when the stronger target fails and the weaker target is exact on the same supported family.

### 5. The layer is too family-specific to survive even inside the repo
Result:
- partly true.

Assessment:
- architecture-change decisions are family-specific,
- threshold-based augmentation is family-specific,
- but the small decision vocabulary still survives across supported families.

### 6. The layer degenerates into vague engineering advice
Result:
- avoided, but only by keeping it small.

Assessment:
- once tied to theorem IDs, artifacts, and supported-family witnesses, it remains useful.
- without that tether it would become empty language quickly.

### 7. The layer conflicts with asymptotic cases
Result:
- conflict found and resolved.

Assessment:
- exact stop conditions do not imply “stop everything.”
- In asymptotic observer cases the correct action is change architecture, not blanket stop.

## Main falsification verdict

The idea fails as:
- a universal stopping law,
- a new branch identity,
- or a theorem family stronger than the current recoverability package.

The idea survives as:
- a theorem-linked decision layer that helps prevent fake exactness claims and wasted exact pursuit on supported families.
