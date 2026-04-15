# PVRT Theorem Spine

## Scope

This file records the theorem spine for the strongest surviving **Protected-Variable Recoverability Theory (PVRT)** candidate.

It is deliberately narrower than a universal theory statement.
The spine only includes statements that survived repeated derivation, implementation, and falsification.

## 1. Foundational Propositions

### PVRT-F1: Fiber-Separation Exactness
Exact recoverability holds iff the protected variable is constant on the observation fibers.

Status:
- proved
- foundational
- standard

### PVRT-F2: Collapse-Modulus Exactness

```text
κ_{M,p}(0)=0
```

iff exact recoverability holds.

Status:
- proved
- foundational
- standard-adjacent

### PVRT-F3: Restricted-Linear Exactness Criterion
For a restricted linear family `x = F z`, record `O F z`, and protected variable `L F z`, exact recovery holds iff

```text
ker(O F) ⊂ ker(L F),
```

equivalently iff

```text
row(L F) ⊂ row(O F).
```

Status:
- proved
- foundational restricted-linear theorem

## 2. Supporting Lemmas And Bounds

### PVRT-L1: Adversarial Lower Bound
For record perturbation radius `η`,

```text
worst-case protected-variable error ≥ κ_{M,p}(η)/2.
```

Status:
- proved
- strongest current lower bound attached to `κ`

### PVRT-L2: Exact-Regime Stability Envelope
If exact recovery holds and `K O F = L F`, then

```text
κ_{M,p}(δ) ≤ ||K||_2 δ.
```

Status:
- proved in the restricted-linear branch
- strongest current upper bound attached to `κ`

### PVRT-L3: Rank Lower Bound
Exact recovery implies

```text
rank(O F) ≥ rank(L F).
```

Status:
- proved
- necessary only, not sufficient

## 3. Main Threshold Theorems

### PVRT-T1: Nested Restricted-Linear Collision-Gap Threshold Law
On the bounded coefficient family

```text
A_B = {F z : ||z||_∞ ≤ B},
```

with nested record family `M_r(x)=O_r x`, define

```text
Γ_r(B) = sup { ||L F h|| : ||h||_∞ ≤ 2B, O_r F h = 0 }.
```

Then:
- `Γ_r(B)` is monotone nonincreasing in `r`
- exact recovery at level `r` holds iff `Γ_r(B)=0`
- below threshold every zero-noise estimator obeys

```text
worst-case protected-variable error ≥ Γ_r(B)/2.
```

Status:
- proved
- strongest theorem-grade threshold law in the branch

### PVRT-T2: Minimal Exact Record Complexity In Nested Restricted-Linear Families
For nested record families,

```text
r_* = min { r : row(L F) ⊂ row(O_r F) }
```

is the exact threshold for exact protected-variable recovery.

Status:
- proved
- strongest honest generalization of the periodic and diagonal family-level threshold stories

### PVRT-T3: Minimal Unrestricted Augmentation Theorem
If unrestricted extra linear measurements are allowed, the minimum number needed to restore exact recovery is

```text
δ(O, L; F) = rank([O F; L F]) - rank(O F).
```

Status:
- proved
- strongest design-side theorem in the branch

## 4. No-Go Spine

### PVRT-N1: Same-Rank Insufficiency
Observation rank alone does not determine recoverability.
For every admissible restricted-linear setting with `rank(LF)=r` and family dimension larger than `r`, and every `k` with

```text
r ≤ k < dim(range(F)),
```

there exist same-rank record families with opposite recoverability verdicts.

Status:
- proved in the restricted-linear branch
- strongest negative theorem directly supporting the PVRT core claim

### PVRT-N2: Same-Record Weaker-versus-Stronger Split
A fixed record can exactly recover a weaker protected variable while exact recovery of a stronger one remains impossible.

Status:
- proved
- useful negative result

### PVRT-N3: Family-Level No-Go Corollaries
These stay as supporting corollaries rather than central PVRT theorems:
- fixed-basis phase-loss no-go
- divergence-only no-go
- hidden protected-direction no-go

Status:
- proved on their families
- useful, but family-specific

## 5. Family-Level Corollaries

### PVRT-C1: Periodic Functional-Support Threshold
Exact recovery begins when the retained cutoff contains every Fourier mode used by the protected variable.

Status:
- proved on the tested periodic modal families

### PVRT-C2: Diagonal Functional-Interpolation Threshold
Exact finite-history recovery begins when the history is long enough to interpolate the protected functional on the active sensor spectrum.

Status:
- proved on the tested diagonal families

### PVRT-C3: Qubit Phase-Window Split
The same fixed-basis record can remain exact for `z` while becoming impossible for the full Bloch vector as phase freedom opens.

Status:
- proved on the tested qubit family

## 6. Failed Or Demoted Candidates

### PVRT-X1: Record amount alone determines recoverability
Verdict:
- false

Killed by:
- same-rank insufficiency theorem
- support-size counterexamples
- rank-only insufficiency counterexamples

### PVRT-X2: One universal cross-domain threshold law
Verdict:
- unsupported

Killed by:
- different threshold mechanisms in periodic, diagonal, and qubit lanes

### PVRT-X3: Protected rank or support size alone predicts threshold level
Verdict:
- false

Killed by:
- repeated-cutoff periodic stress cases
- diagonal polynomial threshold stress cases

## 7. Strongest Next Targets

### Strongest next theorem target
A noisy / admissible-family-enlarged extension of PVRT-T1 and PVRT-T3.

### Strongest next no-go target
A stronger insufficiency theorem for restricted candidate measurement libraries or weighted sensor-cost settings.

### Strongest next threshold target
A robust threshold law that remains valid under controlled perturbation of the admissible family rather than only on the exact restricted family.

## 8. Honest Assessment

PVRT now has a real theorem spine.

It is not broad or universal.
It is strongest as a restricted theorem program built from:
- exact fiber-compatibility,
- collision-gap thresholds,
- exact-regime stability envelopes,
- same-rank insufficiency,
- and minimal augmentation counts.
