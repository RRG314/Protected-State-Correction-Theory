# Quantum Measurement Alignment (Branch-Limited)

This note defines the surviving quantum alignment lane after audit and correction.

The lane is a narrow measurement-design extension of the recoverability program. It uses quantum Fisher and measurement-induced classical Fisher structure to express target-sensitive compatibility on declared qubit classes.

Core objects are `F_Q` (quantum Fisher matrix), `F_M` (measurement-induced classical Fisher matrix), and branch-level alignment quantities such as `sqrt(F_M/F_Q)` in scalar settings or `trace(F_Q^{-1}F_M)` in matrix settings.

What survives as theorem-level content is restricted. On declared pure-qubit classes with the stated assumptions, exact tradeoff identities hold and are marked `PROVED ON RESTRICTED CLASS`. Beyond that class, extension behavior is mixed: some patterns remain as inequalities or empirical trends, and several scalar identity forms collapse.

This lane should be read as a scoped design-analysis extension. It is not a replacement for standard quantum estimation theory and not a universal quantum recoverability law.

Canonical supporting files:
- `docs/physics/quantum_alignment_audit.md`
- `docs/physics/quantum_alignment_corrections.md`
- `docs/physics/quantum_alignment_theorem_candidates.md`
- `docs/physics/quantum_alignment_generalization_report.md`
- `docs/references/quantum_alignment_literature_audit.md`
