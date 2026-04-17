# Cross-Reference Map (Final Pass)

Date: 2026-04-16

## Goal
Keep papers standalone while adding minimal orientation links where useful.

## Reference policy used
1. Each paper remains self-contained for its core claims.
2. Cross-references are orientation-only, not dependency-critical.
3. No paper relies on another paper for missing definitions/proofs of its own main results.

## Implemented cross-references

### Recoverability -> OCP Core
- Location: Introduction in `papers/recoverability_paper_final.md`
- Purpose: points readers to concise operator-foundation companion.

### OCP Core -> Recoverability / Bridge / MHD
- Location: Section 5 and Appendix A in `papers/ocp_core_paper.md`
- Purpose: clarify that OCP core is foundational companion; directs readers to theorem-heavy and domain-application companions.

### Bridge -> Recoverability / OCP Core
- Location: Introduction in `papers/bridge_paper.md`
- Purpose: orient abstract recoverability language without importing dependency.

### MHD -> Recoverability / OCP Core
- Location: Introduction in `papers/mhd_paper_upgraded.md`
- Purpose: optional high-level program context while preserving MHD standalone identity.

## Non-links intentionally preserved
- Recoverability paper does not depend on bridge/MHD for core theorems.
- Bridge and MHD papers do not depend on each other for correctness.
- OCP core does not duplicate the full anti-classifier/threshold development.
