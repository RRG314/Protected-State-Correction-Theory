# Invariant Normalization Map

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This map normalizes notation across invariant, positive-recoverability, and context-sensitive branches.

## Canonical symbols

- State space: `X`
- Target map: `tau : X -> T` (linear representative `L`)
- Record map (single context): `M` (linear representative `O`)
- Record family (multi-context): `{M_c}_{c in C}`
- Local decoders: `{d_c}`
- Shared decoder: `d_*`

## Exactness layers

- Core exactness (single context): `E_core(L,O) = 1` iff `row(L) subset row(O)`
- Conditioned exactness: `E_cond = 1` iff `forall c, exists d_c: d_c M_c = L`
- Shared/invariant exactness: `E_inv = 1` iff `exists d_*: forall c, d_* M_c = L`
- Context gap: `G_ctx = E_cond - E_inv`

## Defect/threshold invariants

- Context defect: `CID(L,{M_c}) = min_d max_c ||dM_c - L||`
- Free shared augmentation threshold: `delta_free`
- Candidate-library defect: `delta_C`

Normalization:
- `CID = 0 <=> E_inv = 1` (supported class)
- `delta_free = 0 <=> E_inv = 1` (supported class)
- `delta_C > 0 => infeasible under candidate-library constraint` (supported class)

## Descriptor-fiber invariants

Given descriptor `phi` and verdict `v in {exact, fail}`:
- DFMI: mixed-fiber fraction
- IDELB: irreducible descriptor-error lower bound
- CL: `IDELB(phi)-IDELB(phi+)`

Normalization rule:
- Use `phi_amount` for amount-only descriptors.
- Use `phi_lift` for amount + compatibility descriptors.

## Collision/collapse quantities

- Collision gap (`CG`) exact when explicit low-null solver used.
- For high-null sweeps in this pass, use labeled proxy:
  - `collision_gap_mode = proxy_rowspace_residual`.

## Stress invariants

- Enlargement fragility flag: exact-to-fail flip under family enlargement.
- Mismatch instability: off-family decoder error indicator.
- Noise fragility: exact-to-fail under bounded perturbation.

## Branch labels

- `CORE`: theorem-grade canonical spine.
- `CONTEXT`: supported-family theorem package.
- `DESCRIPTOR`: quantitative anti-classifier layer.
- `STRESS`: validated fragility layer.
- `PHYSICS-NC`: non-canonical physics extension (quantum/BH/cosmology) unless promoted by proof.

## Nonclaim normalization

The normalized map explicitly **does not claim**:
1. universal new invariant replacing fiber/row-space,
2. global closed-form `delta_free` law across all classes,
3. branch transfer of physics diagnostics into core theorem status.
