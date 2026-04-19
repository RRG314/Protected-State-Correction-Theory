# Terminology Change Log

Date: 2026-04-17

## Purpose

Records terminology normalization decisions made in this cleanup pass.

## Changes Applied

| Previous wording (seen in repo) | Normalized wording | Reason |
| --- | --- | --- |
| universal correction language (broad) | branch-limited structural criteria | Avoid overclaiming |
| amount-only recoverability phrasing | amount-only heuristics fail on supported classes | Preserve anti-classifier precision |
| rank-only sufficiency language | row-space/kernel compatibility | Mathematical correctness |
| ambiguous “recovery” in damping contexts | asymptotic suppression/correction | Exact vs asymptotic separation |
| mixed “state recovery” / “target recovery” | target-specific recoverability | Target-sensitivity clarity |
| duplicate module names across docs | Structural Discovery Studio, Discovery Mixer / Structural Composition Lab, Benchmark / Validation Console | Workbench consistency |
| soliton branch path ambiguity | canonical `docs/meta-governance/internal/soliton-branch/`, legacy `docs/meta-governance/internal/soliton_branch/` | Path stability + clarity |

## Status Vocabulary Adjustment

- Standardized promoted statuses to:
  - `PROVED`
  - `PROVED ON SUPPORTED FAMILY`
  - `CONDITIONAL`
  - `VALIDATED`
  - `OPEN`
  - `ANALOGY ONLY`
  - `REJECTED`

## Scope Notes

- No theorem content was deleted.
- No branch was removed.
- Changes are naming and navigation discipline to reduce ambiguity.

## Canonical References

- `docs/overview/terminology-unification.md`
- `docs/overview/notation-unification.md`
- `docs/meta-governance/internal/repo_cleanup/canonical_document_map.md`
