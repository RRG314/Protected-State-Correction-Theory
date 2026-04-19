# Changelog

## v1.2.0 — 2026-04-19

Push-readiness, architecture hardening, and release-surface cleanup.

This version prepares the repository for a clean public review path after the major expansion work in `v1.1.0`. The focus is structural clarity, claim-scope discipline, and portable documentation.

Main release moves:
- finalized six-layer documentation architecture and canonical routing
- separated known backbone, restricted results, methods, validation, physics translation, and governance surfaces
- internalized process-heavy pass artifacts under explicit non-canonical lanes
- normalized active docs to a consistent research-writing style
- added live-vs-local and push-readiness audit artifacts for reviewer-facing release control
- removed machine-specific absolute repo paths from active public docs

Release notes:
- `docs/releases/v1.2.0.md`

## v1.1.0 — 2026-04-18

Expansion and structural consolidation release.

This version adds substantial new theorem/discovery material while reorganizing the repository into a clearer branch-first structure for public reading.

Main release moves:
- expanded constrained-observation, context-sensitive recoverability, positive design, and invariant/augmentation lanes
- expanded CFD bounded-domain and MHD closure/obstruction branch material
- added scoped quantum-alignment and BH/cosmology placement audits as narrow physics extension content
- reorganized documentation around branch landing pages and canonical contribution paths
- demoted process-heavy internal pass logs from front-door navigation to archive paths
- normalized major public docs to a consistent theorem-first research tone

Release notes:
- `docs/releases/v1.1.0.md`

## v1.0.0 — 2026-04-13

Initial public research-program release.

Highlights:
- established the repository in its public theory-first form as **Protected-State Correction Theory**
- finalized the exact versus asymptotic architecture and the main theorem / no-go spine
- added the static GitHub-Pages-compatible **Protected-State Correction Workbench**
- added the physics bridge layer with kept, conditional, and rejected systems documented explicitly
- added reviewer-facing documents, citation metadata, release notes, and release entry points

Core mathematical content included in this release:
- exact orthogonal protected-subspace recovery
- exact sector recovery under orthogonal compatible sector structure
- exact correction rank lower bound
- continuous damping and invariant-split generator results
- self-adjoint PSD decay corollary
- overlap, mixing, sector-overlap, and finite-time smooth-flow no-go results
- periodic Helmholtz/Leray projection as the exact continuous anchor
- bounded-domain projector transplant failure as an explicit counterexample

Validation status at release:
- Python tests passed
- workbench tests passed
- link checks passed
- naming consistency checks passed
- static Pages assets validated
