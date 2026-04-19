# New Invariant Definitions (Master)

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This file defines the new-candidate invariants considered after the deep catalog pass (`data/generated/invariants/deep_invariant_catalog.csv`, `data/generated/invariants/deep_invariant_stress.csv`).

## Shared notation

- `L`: target map (linear representative)
- `M_c`: context-indexed record maps, `c in C`
- `E_cond`: conditioned exactness indicator
- `E_inv`: shared/invariant exactness indicator
- `CID(L,{M_c}) = min_d max_c ||d M_c - L||_F`
- `delta_free`: unconstrained shared augmentation threshold
- `delta_C`: candidate-library constrained augmentation defect

## Candidate NI-1: Context-Coherence Defect (CCD)

Definition:
`CCD(L,{M_c}) := CID(L,{M_c})`.

Role:
Detect whether local decoders can merge into one shared decoder.

Interpretation:
- `CCD = 0`: shared decoder feasible on supported class.
- `CCD > 0`: context conflict remains.

Status:
- `PROVED ON SUPPORTED FAMILY` as a zero-test (`CCD=0 <=> E_inv=1` in current class).
- `KNOWN / REFRAMED` structurally (residual-consistency object).

Distinctness check:
- Not reducible to rank/count alone.
- On current class it is tightly coupled to existing CID logic (packaging extension, not a new core invariant).

## Candidate NI-2: Structured Completion Defect Pair (SCD)

Definition:
`SCD(L,{M_c};C_lib) := (delta_free, delta_C)`.

Role:
Separate two failure modes:
1. free geometric insufficiency (`delta_free`),
2. constrained-library infeasibility (`delta_C`).

Interpretation:
- `(0,0)`: already shared-exact.
- `(k,0), k>0`: free augmentation required, candidate library can realize it.
- `(k,m), m>0`: constrained library blocks completion even with sufficient free rank-gain.

Status:
- `PROVED ON SUPPORTED FAMILY`.
- Most useful additive invariant package in this pass.

Distinctness check:
- Strictly stronger than amount-only descriptors on tested families.
- Partly overlaps known constrained-observability design ideas (`CLOSE PRIOR ART / REPACKAGED` risk remains).

## Candidate NI-3: Descriptor-Lift Gain Vector (DLG)

Definition:
For descriptor family `phi` and compatibility-lifted descriptor `phi+`:
- `DLG_dfmi := DFMI(phi) - DFMI(phi+)`
- `DLG_idelb := IDELB(phi) - IDELB(phi+)`
- `DLG := (DLG_dfmi, DLG_idelb)`

Role:
Quantify ambiguity reduction from adding compatibility information.

Interpretation:
- positive components indicate strict lift benefit.

Observed values (current meta rows):
- amount-only: `DFMI=0.3478`, `IDELB=0.25`
- lifted: `DFMI=0.0`, `IDELB=0.0`
- gains: `(0.3478, 0.25)`.

Status:
- `PROVED ON SUPPORTED FAMILY` (catalog-level).
- universal claim remains `CONDITIONAL`.

Distinctness check:
- not a new universal exactness invariant;
- strong anti-classifier diagnostic on finite catalogs.

## Candidate NI-4: Family-Enlargement Fragility Index (FEFI)

Definition:
Given stress operator `Enlarge(·)` and baseline family set `B`:
`FEFI := P( E_inv(b)=1 and E_inv(Enlarge(b))=0 )` over `b in B`.

Role:
Measure false-positive risk from narrow-family exactness claims.

Observed in deep stress pass:
- enlargement rows: `101`
- fragility flags overall: `115/116`.

Status:
- existence-level claim `PROVED ON SUPPORTED FAMILY`.
- rate law/general geometry dependence: `VALIDATED / NUMERICAL ONLY`.

Distinctness check:
- robustness diagnostic, not core exactness invariant.

## Candidate NI-5: Mismatch Instability Score (MIS)

Definition:
For mismatch stress runs:
`MIS := E[ CID_after - CID_before ]` (or paired error amplification where available).

Role:
Quantify decoder fragility under model mismatch.

Status:
- `OPEN` / `VALIDATED / NUMERICAL ONLY` due low sample depth in current pass.

Distinctness check:
- currently too weak for theorem promotion.

## Candidate NI-6: Branch-Domain Compatibility Defect (BCD)

Definition (branch-limited placeholder):
`BCD :=` branch-specific compatibility defect for boundary/closure topology mismatch (CFD/MHD lanes).

Role:
Capture geometry/domain-induced recoverability failure not explained by amount-only descriptors.

Status:
- `CONDITIONAL`.
- not normalized to canonical invariant stack yet.

Distinctness check:
- promising branch utility, insufficient cross-branch normalization.

## Candidate NI-7: BH/measurement alignment ratio

Definition:
Fisher-alignment ratio objects proposed in BH/cosmology notes (external source package).

Role:
Physics-side diagnostic for parameter observability alignment.

Status:
- mostly `KNOWN / REFRAMED` or `OPEN`.
- not accepted as core invariant.

Distinctness check:
- currently reduces to known Fisher-geometry structures or unresolved conjectural extensions.

## Survivor set after definition pass

Promote for continued theorem pressure:
1. `SCD = (delta_free, delta_C)`
2. `CCD` (as scoped CID/coherence form)
3. `DLG` (descriptor-lift quantitative lane)

Keep as diagnostics / exploratory:
1. `FEFI`
2. `MIS`
3. `BCD`
4. BH alignment ratios
