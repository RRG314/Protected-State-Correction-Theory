# Restructure Execution Report

Date: 2026-04-19
Scope: local repo restructure pass (no remote push)
Primary target: `repos/ocp-research-program`

## 1. What was changed

### Canonical routing changes

- Added a single active authority map:
  - `docs/overview/repo-authority-map.md`
- Updated front-door routing to this map:
  - `README.md`
  - `docs/overview/start-here.md`
  - `branches/README.md`
  - `RESEARCH_MAP.md`, `SYSTEM_REPORT.md`, `FINAL_REPORT.md`, `STATUS.md`
- Demoted competing canonical maps to legacy status:
  - `docs/repo_cleanup/canonical_document_map.md`
  - `docs/repo_cleanup/canonical_reading_paths.md`

### Six-layer architecture created

Created new lanes:
- `docs/theorem-core/`
- `docs/restricted-results/`
- `docs/methods-diagnostics/`
- `docs/validation-evidence/`
- `docs/physics-translation/`
- `docs/meta-governance/`
- `docs/archive/structured-passes/`

Each lane now has a `README.md` with scope and routing policy.

### Rehoming and demotion actions

- Moved theorem-core anchors from `docs/finalization/` to `docs/theorem-core/`:
  - `architecture-final.md`
  - `theorem-spine-final.md`
  - `no-go-spine-final.md`
  - `operator-spine-final.md`
  - `naming-and-terminology.md`
- Kept compatibility stubs in `docs/finalization/` so legacy paths remain valid.

- Moved structural-information hardening lane from `docs/research-program/structural-information-theory/` to:
  - `docs/meta-governance/structural-information-theory/`
- Left compatibility stubs under the old path.

- Moved invariants/method diagnostics from `docs/research-program/` to:
  - `docs/methods-diagnostics/invariant-lane/`
- Left compatibility stubs under old paths.

- Moved restricted positive package from `docs/research-program/` to:
  - `docs/restricted-results/positive-recoverability/`
- Left compatibility stubs under old paths.

- Moved `docs/research-program/physics_placement_map.md` to:
  - `docs/physics-translation/physics-placement-map.md`
- Left compatibility stub under old path.

- Archived one-pass/legacy structured passes into:
  - `docs/archive/structured-passes/research-program/`
  - `docs/archive/structured-passes/research-program-reports/`
  - `docs/archive/structured-passes/unifying-theory-universal/`
- Added redirect files in old locations for moved reports/directories.

### Data/evidence organization

Added canonical evidence policy and manifests:
- `data/README.md`
- `data/generated/unified-recoverability/README.md`
- `data/generated/structural-information-theory/README.md`
- `data/imported/structural-information-theory/README.md`

## 2. What was preserved

- Branch entry architecture and branch READMEs.
- Theorem IDs and scope labels (`OCP-*` status semantics).
- Tests and script compatibility via redirect stubs at prior paths.
- Generated artifact paths and provenance references.
- Existing citation-bearing core docs (no broad theorem content rewrite).
- Primary theorem and no-go anchors (relocated, not deleted).

## 3. What was demoted or archived

Demoted from active authority:
- `docs/repo_cleanup/canonical_document_map.md`
- `docs/repo_cleanup/canonical_reading_paths.md`
- `docs/unifying_theory/` as an authority layer (now explicitly legacy framework lane)
- `docs/meta_theory/` as an authority layer (explicitly non-canonical)

Archived/demoted pass materials:
- Geometry passes from `docs/research-program/*geometry*` to structured archive
- Multiple `docs/research-program/*master_report*` and cleanup-era reports moved to structured archive with redirects
- Universal-framed unifying-theory authority files moved to archive with redirects

## 4. What the new architecture is

Active documentation routing now follows:

1. Known backbone / adopted foundations: `docs/theorem-core/`
2. Restricted theorem results / core contributions: `docs/restricted-results/`
3. Methods and diagnostics: `docs/methods-diagnostics/`
4. Validation and evidence: `docs/validation-evidence/`
5. Physics translation / interpretation boundary: `docs/physics-translation/`
6. Meta-governance / audits / claim policy: `docs/meta-governance/`
7. Historical/exploratory structured archive: `docs/archive/structured-passes/`

Single authority map:
- `docs/overview/repo-authority-map.md`

## 5. Remaining risks

1. Legacy compatibility stubs are numerous in `docs/research-program/` and `docs/finalization/`; this is intentional for path stability, but the folder remains visually dense.
2. `docs/unifying_theory/` still contains many legacy files; authority is demoted, but full content-level cleanup is still possible.
3. Some copied restricted-result files inherited older wording and may need secondary language tightening for complete style consistency.
4. Script-level hardcoded paths still target legacy locations in places; redirects preserve behavior but delay full native-path migration.

## 6. Final plain answer

- The repo now materially better matches the strongest honest state of the work.
- The strongest publishable lane is now easier to find (`docs/restricted-results/strongest-paper-lane.md` plus branch-first routing).
- Backbone vs restricted novelty vs methods vs interpretation vs governance are now explicitly separated at top level.
- Competing canonical routing has been removed from active status and replaced by one authority map.
- A further major rewrite is **not urgently required before next work**; the immediate architecture risk has been reduced to manageable follow-up cleanup (mainly legacy-stub reduction and secondary language normalization).

## Sanity checks run

- `python3 scripts/validate/check_links.py` -> pass
- `python3 scripts/validate/check_naming.py` -> pass
- `PYTHONPATH=src .venv/bin/python -m pytest -q tests/examples/test_descriptor_fiber_branch_integration.py tests/examples/test_indistinguishability_examples_consistency.py` -> pass
- `PYTHONPATH=src .venv/bin/python -m pytest -q tests/examples/test_major_expansion_candidate_outputs.py` -> pass
