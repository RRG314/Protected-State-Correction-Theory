# History Preservation Plan

Date: 2026-04-17

## Goal

Preserve prior research passes and theorem-development history without letting historical layers compete with canonical entrypoints.

## Principles

1. Keep all theorem/proof/support artifacts.
2. Do not delete dated pass reports unless truly disposable.
3. Route new readers through canonical docs first.
4. Label historical/supporting role in map/index docs.

## Practical Structure

### Canonical (default path)
- `README.md`
- `docs/overview/start-here.md`
- `docs/finalization/*`
- `docs/meta-governance/internal/unifying_theory/*` (final subset)
- canonical paper set in `papers/*.md`

### Supporting (deep technical)
- `docs/theory/*`
- `docs/fiber-based-recoverability-and-impossibility/*`
- `docs/app/*`

### Historical/Internal (preserved)
- dated pass bundles in `docs/research-program/`
- prior integration/finalization audits in `papers/finalization/` and related folders

## Deconfliction Mechanism

- Use `docs/meta-governance/internal/repo_cleanup/canonical_document_map.md` as the role authority.
- Use `docs/meta-governance/internal/repo_cleanup/canonical_reading_paths.md` for onboarding.
- Keep legacy alias paths with pointer notes rather than deletion.

## What Was Intentionally Not Done

- No deletion of historical markdown reports.
- No flattening into one monolithic summary file.
- No path-breaking mass renames.

## Follow-Up Recommendation

Add lightweight “Role: Canonical/Supporting/Historical” banners incrementally to high-traffic historical docs during future maintenance passes.
