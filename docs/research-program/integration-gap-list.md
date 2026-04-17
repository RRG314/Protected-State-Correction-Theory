# Integration Gap List (2026-04-16)

## Priority Legend

- `P0`: coherence blocker
- `P1`: major inconsistency
- `P2`: useful cleanup

## Gap Inventory

| Priority | Gap | Impact | Target files | Resolution status |
| --- | --- | --- | --- | --- |
| `P0` | Finalization theorem spine missing current recoverability/fiber theorem package | top-level repo story conflicts with claim registry | `docs/finalization/theorem-spine-final.md` | `CLOSED` (canonical spine updated) |
| `P0` | Finalization no-go spine missing constrained/fiber anti-classifier package | no-go summary understates strongest falsification results | `docs/finalization/no-go-spine-final.md` | `CLOSED` (anti-classifier package integrated) |
| `P0` | Final architecture/operator spines lag current branch set | architectural map is stale vs active branch inventory | `docs/finalization/architecture-final.md`, `docs/finalization/operator-spine-final.md` | `CLOSED` (branch map normalized) |
| `P1` | No canonical terminology/notation unification | parallel vocabulary risk | `docs/overview/terminology-unification.md`, `docs/overview/notation-unification.md` | `CLOSED` (canonical glossary + notation references added) |
| `P1` | Evidence-level labels inconsistent between docs and workbench exports | theorem-vs-validated-vs-empirical status can drift | `docs/workbench/lib/app/scenarioExports.js`, generated validation outputs, `docs/app/repo-workbench-consistency-report.md` | `CLOSED` (source-level labels normalized and regenerated) |
| `P1` | Stability-vs-exactness distinctions not canonically summarized | important open lane is easy to misread | `docs/research-program/theorem-normalization-report.md`, `docs/research-program/further-expansion-results.md`, `docs/research-program/final-theory-status-decision.md` | `CLOSED` for documentation; theorem extension remains `OPEN` |
| `P1` | Validation docs exist for lens pass but not full integration pass | no single claim-type matched validation record for this pass | `docs/validation/full-integration-validation-plan.md`, `docs/validation/full-integration-validation-results.md` | `CLOSED` (full gate + focused rechecks documented) |
| `P2` | Reference map expanded but no explicit integration reference audit | literature discipline not summarized in one place | `docs/references/integration-reference-audit.md`, `docs/references/branch-literature-map.md` | `CLOSED` (branch-lane literature map and audit added) |
| `P2` | Start-here and README pathing not yet pointing to new normalization docs | discoverability lag | `README.md`, `docs/overview/start-here.md` | `CLOSED` (paths updated) |

## Residual Open Items

- Weighted-cost anti-classifier theorem extension beyond fixed-library unit-cost baseline.
- Continuity-aware stability theorem layered on exact factorization.
- Broader bounded-domain theorem class beyond current finite-mode boundary-compatible families.

## Removal/Demotion List

Items to demote explicitly:
- inverse-problem wording where exact operator recoverability language is primary and clearer
- entropy phrasing where it only restates exactness
- decorative geometry wording not attached to theorem/no-go or executable invariant

## Completion Criteria For Closing Gaps

A gap is closed only when:
1. canonical docs match claim registry and proof map,
2. terminology and evidence levels are single-source consistent,
3. full claim-type matched validation is executed and recorded,
4. no promoted statement depends on investigation-only reports as sole source.
