# Live vs Current Repo Audit

Date: 2026-04-17  
Target live repo: `RRG314/Protected-State-Correction-Theory` (`origin/main`)  
Current working state: local `main` after live-alignment merge/push

## Audit Method

Compared:
- live public main branch (`origin/main`),
- current local main branch (`main`),
- canonical front-door and branch integration documents,
- workbench + image center surfaces,
- references + validation artifacts.

Classification labels:
- **Canonical**: required public entry or core theorem/status surface.
- **Supporting**: useful technical expansion for serious readers.
- **Archive**: historical/internal provenance; keep but demote.

## Snapshot Summary

1. Live public `main` is aligned with current local `main` (`ahead=0`, `behind=0`).
2. Front-door identity now reflects OCP foundation + branch-limited recoverability/anti-classifier expansion.
3. Workbench and image center are both present in public navigation and validated.
4. Historical pass bundles are preserved but demoted from canonical onboarding paths.

## Core File Matrix

| Area | File | Live main | Current local | Role | Action |
| --- | --- | --- | --- | --- | --- |
| Front door | `README.md` | present | present | Canonical | keep canonical |
| Front door | `RESEARCH_MAP.md` | present | present | Canonical | keep canonical |
| Front door | `STATUS.md` | present | present | Canonical | keep canonical |
| System status | `SYSTEM_REPORT.md` | present | present | Canonical supporting | keep |
| System status | `FINAL_REPORT.md` | present | present | Canonical supporting | keep |
| Spine | `docs/finalization/architecture-final.md` | present | present | Canonical | keep |
| Spine | `docs/finalization/theorem-spine-final.md` | present | present | Canonical | keep |
| Spine | `docs/finalization/no-go-spine-final.md` | present | present | Canonical | keep |
| Status map | `docs/overview/proof-status-map.md` | present | present | Canonical | keep |
| Status map | `docs/overview/claim-registry.md` | present | present | Canonical supporting | keep |
| Branch integration | `docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md` | present | present | Supporting (branch-limited) | keep scoped |
| Branch integration | `docs/research-program/descriptor-fiber-anti-classifier-branch-status.md` | present | present | Supporting (branch-limited) | keep scoped |
| Workbench | `docs/workbench/index.html` | present | present | Canonical | keep |
| Workbench docs | `docs/app/workbench-overview.md` | present | present | Canonical | keep |
| Workbench docs | `docs/app/module-theory-map.md` | present | present | Canonical supporting | keep |
| Image center | `docs/visuals/figure-index.html` | present | present | Canonical supporting | keep |
| Image center | `docs/visuals/visual-gallery.html` | present | present | Canonical supporting | keep |
| Image center | `docs/visuals/visual-guide.md` | present | present | Canonical supporting | keep |
| Papers | `papers/recoverability_paper_final.md` | present | present | Canonical | keep |
| Papers | `papers/ocp_core_paper.md` | present | present | Canonical | keep |
| Papers | `papers/bridge_paper.md` | present | present | Canonical | keep |
| Papers | `papers/mhd_paper_upgraded.md` | present | present | Canonical | keep |
| Papers | `papers/unifying_theory_framework_final.md` | present | present | Canonical supporting | keep |
| References | `docs/references/master_reference_map.md` | present | present | Canonical supporting | keep |
| Validation | `docs/validation/master_validation_report.md` | present | present | Canonical supporting | keep |
| Validation | `validation_summary.json` | present | present | Supporting machine-readable | keep |

## Duplicated/Overlapping and Low-Value Candidates

### Demote from front-facing (keep as archive/supporting)
- dated multi-pass bundles in `docs/research-program/*2026-04-16*`,
- exploratory `docs/meta_theory/*` files that are not promoted theorem-core surfaces,
- layered summaries that restate canonical spines without adding theorem/validation content.

### Keep public-facing
- finalization spines,
- proof/claim maps,
- canonical papers,
- workbench overview + module map + benchmark console,
- image center (figure index + visual gallery + visual guide),
- validation/reference maps.

## Audit Conclusion

Live and current are aligned. Remaining cleanup work is organizational: keep canonical onboarding concise, keep image center visible as a first-class supporting surface, and keep historical research bundles demoted rather than deleted.
