# Canonical Document Map

Date: 2026-04-17

## Purpose

One authoritative map of where to read each topic first.

## Canonical Map

| Area | Canonical document | Supporting documents | Status |
| --- | --- | --- | --- |
| Repository overview | `README.md` | `docs/overview/start-here.md`, `FILE_INDEX.md` | Canonical |
| Theory identity | `docs/unifying_theory/final_theory_identity.md` | `docs/finalization/architecture-final.md` | Canonical |
| Theorem spine | `docs/finalization/theorem-spine-final.md` | `docs/overview/proof-status-map.md` | Canonical |
| No-go spine | `docs/finalization/no-go-spine-final.md` | `docs/impossibility-results/advanced-no-go-results.md` | Canonical |
| Proof/status registry | `docs/overview/proof-status-map.md` | `docs/overview/claim-registry.md` | Canonical |
| Unifying framework | `papers/unifying_theory_framework_final.md` | `docs/unifying_theory/final_theory_refinement_master_report.md` | Canonical |
| Universal core | `docs/unifying_theory/final_universal_core_theorems.md` | `docs/unifying_theory/universal_core_refinement_report.md` | Canonical |
| Branch-limited package | `docs/unifying_theory/branch_limited_strengthening_final.md` | `docs/unifying_theory/canonical_witnesses_and_counterexamples.md` | Canonical |
| Descriptor-fiber anti-classifier branch | `docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md` | `docs/research-program/descriptor-fiber-anti-classifier-branch-status.md`, `papers/descriptor-fiber-anti-classifier-branch.md` | Canonical branch-limited lane |
| TSIT adjacent quantitative extension | `docs/research-program/adjacent-directions/tsit_quantitative_extension.md` | `docs/research-program/adjacent-directions/tsit_claim_status_table.md`, `docs/research-program/tsit_repo_positioning_report.md`, `data/generated/tsit-extension/tsit_positioning_summary.json` | Canonical adjacent lane (non-promoted) |
| Workbench overview | `docs/app/workbench-overview.md` | `docs/app/module-theory-map.md`, `docs/workbench/index.html` | Canonical |
| Image/Figure center | `docs/visuals/figure-index.html` | `docs/visuals/visual-gallery.html`, `docs/visuals/visual-guide.md` | Canonical supporting |
| Validation summary | `docs/validation/master_validation_report.md` | `validation_summary.json`, `docs/app/tool-qualification-report.md` | Canonical |
| References/bibliography | `docs/references/master_reference_map.md` | `docs/references/protected-state-correction.bib`, `docs/references/core-references.md` | Canonical |
| Paper set | `papers/recoverability_paper_final.md`, `papers/ocp_core_paper.md`, `papers/bridge_paper.md`, `papers/mhd_paper_upgraded.md`, `papers/descriptor-fiber-anti-classifier-branch.md` | `papers/style/*`, `papers/finalization/*` | Canonical |
| Companion repos | `docs/repo_cleanup/companion_repo_map.md` | `docs/integration/repo_scope_statement.md` | Canonical |

## Overlap Resolution Rules

1. If multiple documents cover the same role, preserve all files but mark one canonical in this map.
2. Supporting documents should link upward to canonical docs.
3. Historical/internal files should include role labeling in section headers or index docs.
4. Legacy alias paths remain valid but should point readers to canonical locations.

## Legacy Alias Handling

- Canonical: `docs/soliton-branch/`
- Legacy alias preserved: `docs/soliton_branch/`
- Policy: keep both paths; references should default to the canonical hyphenated path.
