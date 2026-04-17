# Descriptor-Fiber Anti-Classifier Branch Change Log

Date: 2026-04-17

## Naming

- Promoted canonical branch identity:
  - **Descriptor-Fiber Anti-Classifier Branch**
- Demoted as non-canonical naming:
  - `meta theory` / `meta-theory` as primary identity.

## Canonical Additions

- Added branch overview, status, and integration docs under `docs/research-program/`.
- Added canonical branch paper:
  - `papers/descriptor-fiber-anti-classifier-branch.md`.
- Added canonical generator script alias:
  - `scripts/report/compute_descriptor_fiber_invariants.py`.

## Compatibility Updates

- `scripts/report/compute_meta_theory_invariants.py` now writes:
  - canonical path `data/generated/descriptor-fiber-anti-classifier/`
  - legacy mirror `data/generated/meta-theory/`
- `scripts/falsification/build_counterexample_catalog.py` updated to read canonical path first with legacy fallback.
- `scripts/falsification/build_full_claim_audit.py` updated source references to canonical branch path.

## Canonical Surface Integration

Updated references in:
- `README.md`
- `SYSTEM_REPORT.md`
- `FINAL_REPORT.md`
- `docs/finalization/architecture-final.md`
- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`
- `docs/research-program/branch-audit.md`
- `docs/research-program/theory-candidate-assessment.md`
- `docs/research-program/usefulness-by-branch.md`
- `docs/repo_cleanup/canonical_document_map.md`
- `docs/repo_cleanup/canonical_reading_paths.md`
- `docs/repo_cleanup/paper_and_report_structure.md`

## Legacy Retention

- `docs/meta_theory/` retained and relabeled as supporting/historical archive.
- legacy exploratory papers retained with non-canonical banner.

## Net Effect

- branch identity now repo-consistent,
- theorem status remains disciplined,
- no overpromotion to universal core,
- GitHub-visible front door now points to canonical branch artifacts.
