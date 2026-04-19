# Research Writing Normalization Report

Date: 2026-04-19  
Scope: local writing normalization pass for active public and theorem-facing lanes

## 1. Major Style Problems Found

1. Product or onboarding heading patterns were present in active docs.
   - Examples: `What this repo does`, `How to use this lane`, `Where to go next`, `Why this matters`.
2. Tutorial-oriented routing language appeared in entry documents.
   - Examples: `If you want ...`, `I Want To ...`.
3. AI-style explanatory scaffolding was present in theorem and methods summaries.
   - Repeated plain-language templates and transitional filler reduced research tone.
4. A small number of em dashes remained in active report files.
5. Several root and lane docs were structurally correct but still read like guidance copy instead of research front matter.

## 2. Headings Removed or Rewritten

The following heading patterns were removed from active lanes and replaced with research-grade alternatives:

- `What this repo does` -> `Scope`
- `What this does in practice` -> `Representative Witnesses` and scope-aware mapping sections
- `Where to go next` -> `Repository Map`
- `How to use this lane` -> `Evaluation Protocol`
- `What belongs here` -> `Included Material` or `Included Result Types`
- `Why this matters` lines in theorem spines -> direct theorem-role statements
- `I Want To ...` section headers -> research task headers (`Solvability Analysis`, `Failure Analysis`, etc.)

## 3. Major Docs Rewritten

Entry and routing documents:

- `README.md`
- `docs/overview/start-here.md`
- `docs/overview/repo-authority-map.md`
- `docs/overview/main-contributions.md`
- `docs/overview/user-entry-paths.md`
- `SYSTEM_REPORT.md`

Theorem and restricted-result framing:

- `docs/theorem-core/README.md`
- `docs/theorem-core/theorem-spine-final.md`
- `docs/theorem-core/no-go-spine-final.md`
- `docs/restricted-results/README.md`
- `docs/restricted-results/strongest-paper-lane.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md`

Methods and validation framing:

- `docs/methods-diagnostics/README.md`
- `docs/methods-diagnostics/metric-instrument-index.md`
- `docs/validation-evidence/README.md`
- `docs/validation-evidence/evidence-map.md`
- `docs/physics-translation/README.md`

Root status and map docs normalized to the same tone:

- `STATUS.md`
- `FINAL_REPORT.md`
- `RESEARCH_MAP.md`

## 4. Remaining Weak Spots

1. Some supporting reports in `docs/research-program/` still carry process-heavy phrasing.
   - They are now cleaner in active entry points, but a full deep rewrite of all supporting reports remains.
2. Internal/archive lanes were intentionally not rewritten in this pass.
   - These include `docs/meta-governance/internal/`, `docs/archive/structured-passes/`, and `archive/internal-process/`.
3. Some older technical docs still use absolute local filesystem links.
   - This is a publication-readiness issue, not a theory-content issue.

## 5. Final Assessment

The active repository surface now reads like a research repository rather than onboarding or product documentation.

The core entry path, theorem spines, restricted-result lanes, and method/validation summaries use a consistent research-writing style with explicit scope and status framing.

The repository no longer relies on `what this is for` style headings in active lanes, and the highest-visibility documents now read as human-edited technical research materials.
