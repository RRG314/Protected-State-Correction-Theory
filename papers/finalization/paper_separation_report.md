# Paper Separation Report (Final Pass)

Date: 2026-04-16  
Scope: `recoverability_paper_final.md`, `ocp_core_paper.md`, `bridge_paper.md`, `mhd_paper_upgraded.md`

## Summary Decision
The paper set is now separated into four non-duplicate roles:
1. theorem-heavy recoverability package,
2. concise OCP foundation companion,
3. projection/PDE bridge paper,
4. domain-specific MHD closure paper.

## 1) Recoverability Paper
File: `papers/recoverability_paper_final.md`

Identity now:
- constrained observation and exact recoverability,
- fiber/factorization general criterion,
- restricted-linear exactness,
- anti-classifier theorems,
- quantitative obstruction (collision-gap/threshold),
- minimal augmentation design law.

Why distinct:
- only paper carrying the full anti-classifier + threshold + weak-vs-strong target package.
- intentionally serves as the main theorem-heavy recoverability manuscript.

## 2) OCP Core Paper
File: `papers/ocp_core_paper.md`

Identity now:
- orthogonal correction principle operator logic,
- exact correction operator characterization (`C = P_{S//D}`),
- restricted-linear exactness as foundational consequence,
- minimal augmentation as compact design corollary,
- concise companion role.

Separation action applied:
- rewritten from overlap-heavy format into a narrower foundation companion.
- full anti-classifier/threshold development moved out of this paper’s center and explicitly delegated to recoverability paper.
- added OCP-specific figure set (`figures/ocp/*`) so visual identity is not duplicated from recoverability.

## 3) Bridge Paper
File: `papers/bridge_paper.md`

Identity now:
- projection-based correction systems in PDE-style settings,
- periodic exactness anchor,
- bounded-domain transplant failure,
- boundary-structure mismatch mechanism,
- exact vs asymptotic vs impossible classification in tested settings.

Why distinct:
- application/bridge scope with PDE/projection mechanisms,
- explicitly non-universal and non-recoverability-core.

## 4) MHD Paper
File: `papers/mhd_paper_upgraded.md`

Identity now:
- Euler-potential MHD closure remainder,
- constant-`eta` exact families,
- variable-resistivity obstruction,
- annular vs axis-touching distinction,
- mixed tokamak-adjacent lane,
- perturbative/asymptotic validated defect structure.

Why distinct:
- domain-specific physics/mathematical closure paper with its own theorem and validation lane.

## Separation Quality Check
- No paper is now a near-duplicate of another.
- OCP core and recoverability are intentionally linked but non-competing.
- Bridge and MHD papers remain standalone and scoped to their domains.
