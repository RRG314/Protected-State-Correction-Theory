# Low-Value Clutter Review

Date: 2026-04-17

## Review Criteria

A file is low-value for public front-door use if it:
1. duplicates a stronger canonical file,
2. restates conclusions without adding theorem/validation/usage value,
3. uses stale naming/scope language,
4. is an exploratory artifact no longer part of promoted public story.

## High-Confidence Demotion Candidates (Keep, Demote from Front Door)

1. Dated multi-pass bundles in `docs/research-program/geometry-pass-2026-04-16/`.
2. Dated multi-pass bundles in `docs/research-program/soliton-geometry-discovery-2026-04-16/`.
3. Exploratory `docs/meta_theory/*` notes (now legacy supporting only).
4. Overlapping integration summary docs when same content is already in:
   - finalization spines,
   - proof-status map,
   - branch audit,
   - master validation/falsification reports.

## Keep as Public Canonical

- README / RESEARCH_MAP / STATUS,
- finalization theorem/no-go architecture,
- proof-status map + claim registry,
- branch audit + usefulness docs,
- canonical paper set,
- workbench overview/module map/benchmark console,
- master validation + falsification reports,
- references map and bib.

## Remove Candidates (Low Risk)

1. `.DS_Store` artifacts from repo root/docs.
2. stale generated files not referenced by canonical docs (only after explicit dependency check).

## Cleanup Implemented in This Pass

1. Front-door docs rewritten to reduce layered restatement.
2. Canonical branch identity and status language tightened.
3. Legacy exploratory naming kept but demoted (no longer front-door language).
4. `.DS_Store` ignore added to `.gitignore`.

## Conservative Guardrails

- No historically important theorem/proof/validation files deleted.
- No major path break introduced for canonical docs.
- Historical material remains available for provenance.
