# Optional Existing-Repo Bridge (Only If Honest)

Date: 2026-04-16  
Policy: do not force mergers; keep soliton program independent unless a concrete theorem/benchmark link survives.

## Bridge test criteria

A cross-link is kept only if it can support at least one of:
- exact criterion,
- sharp no-go,
- computable invariant,
- reproducible benchmark family.

## Candidate cross-links tested

### Link A — Recoverability of soliton parameters under coarse observation

**Bridge target**: constrained-observation/recoverability logic (existing OCP-style lane)  
**Soliton-side object**: restricted one-soliton manifold with symmetry quotient.

**Assessment**
- This can be made precise without importing broader OCP branding.
- Cleanly phrased as an independent identifiability/recoverability theorem problem.

**Verdict**: **KEPT (narrow bridge)**  
**Status**: **OPEN (worth a dedicated small branch or companion note)**

---

### Link B — Projection/reduction preserving coherent structures

**Bridge target**: projection-success/failure logic from bridge/PDE ideas  
**Soliton-side object**: whether a projection preserves soliton manifold or produces defect drift.

**Assessment**
- Mathematical bridge is plausible and non-forced.
- Must stay equation-class-specific (e.g., one NLS/KdV lane + one projection class).

**Verdict**: **KEPT (restricted)**  
**Status**: **CONDITIONAL**

---

### Link C — Minimal-augmentation logic transferred directly to nonlinear soliton dynamics

**Assessment**
- Direct transfer is not justified at current stage.
- Nonlinear symmetry and manifold structure make naive translation risky.

**Verdict**: **REJECTED for now**  
**Status**: **DISPROVED as immediate transfer**

---

### Link D — MHD-soliton unification lane

**Assessment**
- Soliton-like plasma waves exist, but direct theorem-sharing with current Euler-potential closure program is weak right now.
- Risk of analogy inflation is high.

**Verdict**: **REJECTED (for now)**  
**Status**: **ANALOGY ONLY currently**

---

### Link E — Bounded-vs-periodic structural mismatch analogy

**Assessment**
- Conceptual analogy exists (boundary/domain effects can alter coherent-wave persistence).
- No immediate theorem bridge established in this discovery pass.

**Verdict**: **MAYBE (investigation-only)**  
**Status**: **OPEN, not promoted**

## Kept vs rejected summary

### Kept
1. Soliton-parameter recoverability under constrained observation (narrow, explicit)
2. Projection/reduction preservation/no-go for coherent-state manifolds

### Rejected or not promoted
1. Direct minimal-augmentation transfer to nonlinear full setting
2. Broad MHD-soliton unification
3. Broad bounded-vs-periodic analogies without explicit equation-class theorem

## Recommendation

Keep the soliton program as a separate identity.  
If any bridge is pursued, start with **Link A** in a narrow standalone note that can later map to existing repo language only after results survive.
