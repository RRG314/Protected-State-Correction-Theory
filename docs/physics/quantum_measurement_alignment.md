# Quantum Measurement Alignment (Branch-Limited)

This note defines the scope of the quantum measurement-alignment lane after correction and falsification.

## What this lane is

A narrow quantum measurement-design extension of the recoverability program focused on target-sensitive Fisher compatibility under explicit assumptions.

## What this lane is not

- not a new quantum foundation,
- not a replacement for standard quantum estimation theory,
- not a universal theorem package across all dimensions and measurement classes.

## Canonical objects

- `F_Q`: quantum Fisher information matrix.
- `F_M`: classical Fisher information matrix induced by a measurement.
- `alpha_Q`: ratio notation layer in scalar settings (`sqrt(F_M/F_Q)`).
- restricted tradeoff metric: `trace(F_Q^{-1} F_M)`.

## Surviving restricted result

On declared qubit classes, one obtains exact tradeoff identities in matrix/trace form, with diagonal-coordinate scalar corollaries where assumptions apply.

Status:
- `PROVED ON RESTRICTED CLASS`.

## Failure boundaries

The exact scalar conservation statement does not transfer universally to:
- non-diagonal scalar coordinate expressions,
- generic mixed-state and unsharp-measurement settings,
- higher-dimensional systems.

## Canonical references in this repo

- `docs/physics/quantum_alignment_audit.md`
- `docs/physics/quantum_alignment_corrections.md`
- `docs/physics/quantum_alignment_theorem_candidates.md`
- `docs/physics/quantum_alignment_generalization_report.md`
- `docs/references/quantum_alignment_literature_audit.md`

