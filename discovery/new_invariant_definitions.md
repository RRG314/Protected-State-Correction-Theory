# New Invariant Definitions

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

Notation (context-sensitive linear class):
- target row map `L` (or vector `t` for scalar target)
- context observations `{M_c}_{c in C}`
- local exactness: `forall c, exists d_c: d_c M_c = L`
- shared exactness: `exists d_*: forall c, d_* M_c = L`

## 1. Context-Coherence Defect (CCD)

Definition:
`CCD(L,{M_c}) = min_d max_{c in C} ||d M_c - L||_F`

Interpretation:
- `CCD = 0` iff one shared decoder exists.
- For this pass, `CCD` is implemented as CID.

Status:
- `PROVED ON SUPPORTED FAMILY` as zero-test equivalence.

## 2. Augmentation Deficiency Pair

### 2.1 Free deficiency
`delta_free(L,{M_c}) = min r such that exists U in R^{r x n} with shared exactness for { [M_c; U] }`

### 2.2 Candidate-library defect
Given candidate row library `S`, define
`delta_C(L,{M_c},S) = rank([A; S; L]) - rank([A; S])`
where `A` is agreement-lift matrix.

Interpretation:
- `delta_C > 0` certifies that full candidate pool still misses target directions.

Status:
- `delta_free`: `PROVED ON SUPPORTED FAMILY`.
- `delta_C` no-go signal: `PROVED ON SUPPORTED FAMILY`.

## 3. Compatibility Lift (CL)

Given descriptor map `phi`, define descriptor-fiber lower-bound error:
`IDELB(phi) = (1/N) sum_f min(N_exact(f), N_fail(f))`

With lifted descriptor `phi_plus`, define
`CL(phi -> phi_plus) = IDELB(phi) - IDELB(phi_plus)`

Interpretation:
- Positive `CL` means added compatibility information strictly reduces irreducible descriptor ambiguity.

Status:
- `PROVED ON SUPPORTED FAMILY`.

## 4. Mixedness-Depth Descriptor Fiber (MDDF)

For descriptor fiber `f` with class proportions `p_f(exact), p_f(fail)`, define
`MDDF(f) = 2 * min(p_f(exact), p_f(fail)) * V_f`
where `V_f` is optional target-spread normalization.

Global MDDF:
`MDDF_global = (1/|F|) sum_f MDDF(f)`.

Status:
- `CONDITIONAL`; proposed for next pass.

## 5. Family-Enlargement Fragility Index (FEFI)

Given base family `F` and enlargement policy `E`, define
`FEFI(F,L) = min m such that exists enlargement of size m causing exact -> fail flip`

Operational variant for finite catalogs:
`FEFI_rate = (# exact->fail flips)/(# tested exact bases)`.

Status:
- `VALIDATED / NUMERICAL ONLY` in current catalogs.

## 6. Mismatch Instability Slope (MIS)

Given mismatch parameter `beta` with subspace distance `d(beta)` and deployment error `err(beta)`, define
`MIS = d(err)/d(d(beta))` (finite-difference in practice).

Status:
- `OPEN` (insufficient sweep density).

## 7. Boundary-Compatibility Defect (BCD)

Branch-limited proposal (bounded-domain/PDE):
`BCD = || P_boundary(L) - P_boundary(Recoverable(L)) ||`
with branch-specific projector choice.

Status:
- `CONDITIONAL`; requires canonical branch definition.

## 8. Distinctness checks against existing core

- CCD reduces to existing shared-decoder feasibility zero-test in the supported class.
- `(delta_free, delta_C)` is additive because `delta_C` captures candidate-library geometry not represented by free threshold alone.
- CL is additive at descriptor layer; it does not replace row-space/fiber exactness.
- MDDF/FEFI/MIS/BCD remain candidate diagnostics pending stronger theorem coupling.
