# Source Map

## Purpose

This file records how local source material was used so the OCP repository keeps provenance and does not quietly rewrite the history of the ideas.

## Strongest Direct Inputs

### MHD divergence-control materials
- Source: `mhd-toolkit/docs/divergence_control.md`
- Used for: exact projection-cleaning and GLM sections
- Output docs: `docs/mhd/divergence-cleaning-in-ocp.md`, `docs/mhd/glm-and-asymptotic-correction.md`, `docs/operators/operator-constructions.md`

### MHD projection and GLM code
- Source: `mhd-toolkit/mhd_toolkit/divfree/projection.py`
- Source: `mhd-toolkit/mhd_toolkit/divfree/glm.py`
- Used for: `src/ocp/mhd.py` and local tests

### SDS correction-gap formalization
- Source: `sds-research-repo/docs/correction-gap/correction_gap_formalization.md`
- Used for: no-go framing, anti-unification discipline, operator-image failure language
- Output docs: `docs/impossibility-results/no-go-results.md`, `NOVELTY_AND_LIMITS.md`

### Topological Adam / QEC bridge note
- Source: `topological-adam/RGE_QEC_Fermat_Prime_2026.docx`
- Used for: provenance only and caution about speculative bridge claims
- Output docs: `docs/disproven-or-weak/weak-extensions.md`

### RGE cross-structure / novelty notes
- Source: `rge-research-program/docs/overview/novelty-and-opportunity.md`
- Source: `rge-research-program/docs/foundations/renormalization-and-coarse-graining.md`
- Used for: research-program discipline, operator-language emphasis, and limitation framing
- Output docs: `NOVELTY_AND_LIMITS.md`, `docs/positioning/what-ocp-would-be.md`

## Local Repo-Native Outputs

The following files are new OCP-program outputs rather than imported drafts:
- `docs/formalism/formal-theory.md`
- `docs/formalism/exact-vs-asymptotic.md`
- `docs/qec/qec-in-ocp.md`
- `docs/theorem-candidates/central-theorem.md`
- `docs/impossibility-results/no-go-results.md`
- `src/ocp/core.py`
- `src/ocp/qec.py`
- `src/ocp/mhd.py`
