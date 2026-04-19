# Notation Unification

Date: 2026-04-17

This file fixes notation across the unifying framework.

## Core symbols

- `X`: ambient state space.
- `A`: admissible family (all claims are relative to `A`).
- `T`: target/protected map.
- `M`: record/observation map.
- `R`: recovery map from record to target.
- `C`: correction architecture/operator/dynamics.
- `D`: disturbance/ambiguity structure.
- `~`: nuisance equivalence (symmetry/gauge/label equivalence).
- `S`: side information / augmentation object.

## Restricted-linear symbols

- `F`: family basis/embedding, `A={Fz}`.
- `O`: observation matrix/operator.
- `L`: target matrix/operator.
- exactness criterion: `ker(OF) ⊆ ker(LF)`.
- equivalent row-space form: `row(LF) ⊆ row(OF)`.
- minimal augmentation: `δ(O,L;F)=rank([OF;LF])-rank(OF)`.

## Collision and stability symbols

- `kappa_0`: zero-noise collision ambiguity quantity.
- `E_mm`: mismatch error-floor quantity on declared class.
- `phi_FE`: family-enlargement fragility indicator.

## Usage rules

1. Do not switch between `p` and `T` in the same theorem statement.
2. Do not use `M` and `O` interchangeably unless explicitly reducing to restricted-linear form.
3. Always declare whether equality/injectivity is on `A` or on quotient `A/~`.
4. Keep branch-specific symbols (e.g., MHD `η`, soliton manifold parameters) inside branch sections, not in universal statements.
