# Cross-Repo Audit (OCP + Soliton)

Date: 2026-04-16/17
Scope: OCP / Protected-State-Correction-Theory + soliton-geometry-research

## Audit objective

This audit classifies current material across both repositories into:
1. core and stable
2. newly added but needs cleanup
3. internal-only / not for public promotion
4. should be demoted
5. should be promoted
6. duplicate / overlapping / conflicting

## OCP repository audit

### 1) Core and stable

- OCP theorem and no-go spines for exact projection, asymptotic generator, and constrained-observation restricted-linear lanes.
- fiber-based recoverability/impossibility anti-classifier results.
- structural discovery + workbench layers tied to generated validation artifacts.
- bounded-domain negative transplant and bounded finite-mode Hodge restricted positive lane.

### 2) Newly added but needs cleanup

- soliton branch admission package in `docs/soliton-branch/*` is strong but split across many files and naming conventions.
- top-level reports mention soliton branch but do not yet expose a clean public-vs-internal split map.
- several generated validation inventories changed alongside paper/visual updates and need explicit release discipline.

### 3) Internal-only / not for public promotion

- private comprehensive cross-program memos and internal audit notebooks.
- intermediate integration sweep notes not intended as canonical repo-facing theory docs.

### 4) Should be demoted

- any wording that implies self-organization is already an OCP theorem branch.
- any phrasing implying direct transfer of linear minimal augmentation theorem into nonlinear soliton class.

### 5) Should be promoted

- explicit branch-admission rule set for soliton overlap.
- status registry with strict labels for soliton-bridge claims.
- explicit external literature alignment table for bridge claims.

### 6) Duplicate / overlapping / conflicting

- duplicated branch identity wording between `docs/soliton-branch/*` and top-level reports.
- mixed naming (`soliton-branch` vs `soliton_branch`) across recent requests.

## Soliton repository audit

### 1) Core and stable

- deep discovery engine script and generated artifact structure under `data/generated/discovery/*`.
- formal lane (restricted one-soliton recoverability modulo symmetry) with collision/noise/projection scans.
- anomaly/pattern outputs with explicit statuses and source-file references.

### 2) Newly added but needs cleanup

- report set expanded rapidly; some docs are concise stubs while others are detailed.
- status labels are mostly consistent but not yet centralized in one canonical status registry doc.
- research program map is not yet one-stop (spread across `docs/research-program` and `docs/research_program`).

### 3) Internal-only / not for public promotion

- internal comprehensive report in `internal/` should remain internal-only.

### 4) Should be demoted

- any wording that overreads CGL random-self-organization signal as robust phenomenon.

### 5) Should be promoted

- explicit master program map + status registry.
- theorem promotion report separating finite-family proofs from continuous open problems.
- deep verification/falsification reports tied to rerun logs.

### 6) Duplicate / overlapping / conflicting

- metric-specific conflict in CGL lane (final-defect vs coherence-defect) was present and must remain explicitly labeled.
- duplicate summary statements across experiment reports without a central status authority.

## Cross-repo overlap classification

| Topic | OCP classification | Soliton classification | Decision |
| --- | --- | --- | --- |
| Symmetry non-identifiability no-go | exact analogue | core formal theorem lane | Keep in both with scoped wording |
| Same-count opposite-verdict | restricted analogue | core formal finite-family finding | Keep in both; no continuous overpromotion |
| Projection preservation vs no-go | restricted analogue | core secondary formal lane | Keep in both with operator-class scope |
| CGL random self-organization superiority | analogy-only at most | artifact-risk anomaly | Keep only in soliton as anomaly lane |
| Direct linear minimal-augmentation transfer | rejected bridge | rejected transfer | Keep rejected in both |

## Immediate cleanup actions (this pass)

1. Add scope statements in both repos under `docs/integration/repo_scope_statement.md`.
2. Create unified status registries and theorem-promotion notes.
3. Add deep verification and deep falsification reports in both repos.
4. Keep OCP soliton integration branch-limited and status-explicit.
5. Keep soliton repo as primary home for nonlinear discovery outputs.

