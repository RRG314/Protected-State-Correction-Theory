# Positive Recoverability Master Report

Status: theorem-first exploration pass, branch-limited and falsification-first.

This pass asked whether a real positive architecture could be extracted without claiming universal recoverability. The result is yes, but only on a restricted class: finite linear context-structured systems with explicit admissibility and augmentation rules.

The strongest surviving package is a three-part characterization. First, compatibility characterization (`row(L) ⊆ row(G)`) gives exactness on the declared class. Second, free minimal completion gives the augmentation defect law `delta_free = rank([G;L]) - rank(G)`. Third, constrained-library completion introduces `delta_C`, which captures feasibility failure when admissible completion directions are restricted.

The strongest no-go boundary inside this positive lane is library rank-gain insufficiency: apparent amount gain can still fail to repair exactness because directional compatibility is wrong. This keeps the design story structural rather than amount-only.

Useful surviving quantities are `delta_free`, `delta_C`, and context-coherence diagnostics. These are mathematically clean and operationally useful, but novelty is narrow and overlap-sensitive. The branch should be described as a restricted theorem package with a design/diagnostic layer, not as a universal new framework.

The recommended next step is to formalize this restricted package as a theorem-backed design framework and tighten bounds/proofs around constrained completion behavior before broader promotion.
