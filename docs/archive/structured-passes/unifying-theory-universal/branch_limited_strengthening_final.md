# Branch-Limited Strengthening Final

Date: 2026-04-17

This file gives the sharpened branch-limited package with explicit hypotheses and scope.

## BL-1 No Rank-Only Exact Classifier

### Hypotheses
- restricted finite-dimensional linear family `A={Fz}`,
- target `LFz`, record `OFz`,
- exactness judged by `ker(OF) ⊆ ker(LF)`.

### Statement
There is no exact classifier depending only on rank tuple data that correctly separates exact vs non-exact cases on the supported class.

### Status
`PROVED` (`OCP-049`).

### Scope
Restricted-linear class only.

## BL-2 No Fixed-Library Budget-Only Exact Classifier

### Hypotheses
- same restricted-linear setup,
- finite fixed candidate measurement library,
- unit-cost budget/count comparisons.

### Statement
Equal fixed-library budget/count can yield opposite exactness verdicts; budget-only classification is unsound.

### Status
`PROVED` (`OCP-050`).

### Scope
Fixed-library unit-cost setting only.

## BL-3 Family-Enlargement False-Positive Theorem

### Hypotheses
- restricted-linear families `A_s ⊂ A_l`,
- exactness on small family under declared decoder,
- enlarged family introduces new kernel-target collision directions.

### Statement
Exactness on `A_s` does not certify exactness on `A_l`; explicit lower-bound witness exists on enlarged family.

### Status
`PROVED` (`OCP-052`).

### Scope
Declared restricted-linear enlargement class.

## BL-4 Canonical Model-Mismatch Instability

### Hypotheses
- decoder exact on one declared model family,
- true family differs in canonical parameterized way.

### Statement
Exact-data target error floor is nonzero and explicitly quantifiable under mismatch.

### Status
`PROVED` (`OCP-053`).

### Scope
Canonical family class in theorem statement.

## BL-5 Domain/Topology Compatibility Obstruction

### Hypotheses
- bounded-domain protected class requiring boundary-compatible structure,
- architecture that removes scalar divergence-type residual but does not enforce full compatibility.

### Statement
Divergence reduction alone does not imply bounded-domain exact protected recovery.

### Status
`PROVED` (`OCP-023`, `OCP-028`).

### Scope
Bounded-domain architecture mismatch class.

## BL-6 Restricted Positive Bounded-Domain Exactness

### Hypotheses
- explicit boundary-compatible finite-mode Hodge family,
- declared compatible projector architecture.

### Statement
Exact correction holds on this restricted bounded family.

### Status
`PROVED ON SUPPORTED FAMILY` (`OCP-044`).

### Scope
Finite-mode family only; no universal bounded-domain promotion.

## BL-7 Symmetry-Quotient Obstruction (Soliton Bridge Lane)

### Hypotheses
- restricted one-soliton family,
- nuisance symmetry group (translation/phase),
- observation class invariant under symmetry action.

### Statement
Symmetry-invariant observations can force quotient non-identifiability; same-count observation families can have opposite identifiability verdicts.

### Status
- symmetry no-go: `PROVED`,
- same-count opposite-verdict: `PROVED ON SUPPORTED FAMILY` + `CONDITIONAL` continuous.

### Scope
Declared restricted nonlinear lane; no global nonlinear promotion.

## BL-8 MHD Variable-Resistivity Obstruction Package

### Hypotheses
- Euler-potential MHD closure equations on declared cylindrical/radial ansatz families,
- variable `η(r)` class with axis-touching vs annular domain distinction.

### Statement
Variable-resistivity introduces obstruction with annular-only nontrivial survivor classes on supported families; smooth axis-touching nonconstant survivors fail in those classes.

### Status
`PROVED ON SUPPORTED FAMILY` (+ `PROVED` corollaries in declared classes).

### Scope
Declared MHD families only; no full toroidal/global closure classification claim.
