# Current Repo Structure Audit for Rewrite

Date: 2026-04-19
Scope audited: `.`
Mode: audit only (no broad restructure in this pass)

## 1. Executive Verdict

The current architecture is **not coherent enough** for claim-safe long-term use.

Verdict:
- The repo is strong on theorem content and testing depth, but structurally mixed.
- Incremental cleanup alone is unlikely to remove the authority/confusion problem.
- A **moderate-to-major deliberate rewrite** is needed.

Single biggest architectural problem:
- **Competing authority layers** are active at once (branch-first core, unifying-theory universal layer, research-program pass logs, structural-information hardening lane), with inconsistent “canonical” status.

## 2. Current Repo Map

### Top-level structure (actual)

- `branches/` (11 branch READMEs + index)
- `docs/` (634 files; largest concentration of mixed content)
- `src/ocp/` (core code + theorem-adjacent utilities)
- `tests/` (math, examples, consistency)
- `scripts/` (compare, falsification, report, validate, research)
- `data/generated/` (many lanes; 26 subfolders)
- `data/imported/structural-information-theory/` (new imported evidence)
- `papers/` (multiple paper lanes + format exports + style files)
- `discovery/` (exploration sandbox; non-promoted but large)
- `theory/` (small foundational set, overlaps with docs)
- `archive/` (older process material)

### Major theory docs currently used as anchors

- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`
- `docs/theory/advanced-directions/constrained-observation-formalism.md`
- `docs/fiber-based-recoverability-and-impossibility/restricted-linear-fiber-theory.md`
- `docs/overview/proof-status-map.md`

### Major methods/validation assets

- `src/ocp/fiber_limits.py`
- `src/ocp/decision_layer.py`
- `src/ocp/structural_information.py`
- `scripts/research/run_structural_information_harness.py`
- `data/generated/unified-recoverability/`
- `data/generated/structural-information-theory/`
- `tests/math/`

### Where strongest recent hardening results currently live

- `docs/research-program/structural-information-theory/`
- `data/generated/structural-information-theory/`

### Where framework/interpretive materials are concentrated

- `docs/unifying_theory/`
- `docs/meta_theory/`
- `docs/physics/`
- `papers/unifying_theory_framework*.md`

### Where audit/governance materials are concentrated

- `docs/repo_cleanup/`
- `docs/falsification/`
- `docs/validation/`
- `docs/research-program/` (mixed with technical results)

## 3. Functional Layer Classification

### Known backbone

Well placed:
- `/docs/finalization/theorem-spine-final.md`
- `/docs/finalization/no-go-spine-final.md`
- `/docs/overview/proof-status-map.md`

Misplaced:
- Backbone appears again in `/docs/unifying_theory/final_universal_core_theorems.md` with “universal core” framing, creating authority overlap.

Mixed:
- `/docs/theory/advanced-directions/constrained-observation-formalism.md` contains known backbone and branch-specific claims in the same narrative block.

### Restricted theorem package

Well placed:
- `/docs/fiber-based-recoverability-and-impossibility/` (strong branch package)
- `/docs/theorem-candidates/` (formal theorem lane)
- `/src/ocp/fiber_limits.py`, `/src/ocp/recoverability.py`

Misplaced:
- Important restricted results are duplicated/rephrased across `/docs/research-program/*.md`, `/discovery/*.md`, and `/docs/unifying_theory/*.md`.

Mixed:
- `/docs/research-program/full_system_clear_results_master_report.md` mixes repo-wide novelty ranking, interpretation, and theorem claims.

### Methods/diagnostics

Well placed:
- `/src/ocp/` computational core
- `/scripts/research/run_structural_information_harness.py`
- `/tests/math/` + `/tests/examples/`

Misplaced:
- Method definitions and positioning are spread across `/docs/research-program/`, `/docs/meta_theory/`, `/docs/references/`, and `/papers/`.

Mixed:
- Diagnostic metrics (IDELB/DFMI/CL) are treated as methods in some docs and quasi-theory in others.

### Validation/evidence

Well placed:
- `/data/generated/unified-recoverability/`
- `/data/generated/structural-information-theory/`
- `/tests/`

Misplaced:
- `data/validations/` exists but appears empty while `data/generated/validations/` is active; naming implies unclear canonical evidence location.

Mixed:
- Evidence and exploratory artifacts coexist in `data/generated/` without strict promotion tiers.

### Interpretation/framework

Well placed:
- `/docs/physics/` mostly keeps extension material separate from core theorem files.

Misplaced:
- `/docs/unifying_theory/` still carries canonical-style files with universal framing despite later demotion logic.

Mixed:
- `/docs/repo_cleanup/canonical_document_map.md` still marks unifying/universal docs as canonical, conflicting with recent hardening guidance.

### Meta/governance

Well placed:
- `/docs/falsification/` and `/docs/validation/` are explicit governance lanes.

Misplaced:
- Meta/governance and technical research outputs are interleaved in `/docs/research-program/` (129 files).

Mixed:
- `/docs/repo_cleanup/` contains valuable policy docs but also historical cleanup logs that compete with current governance docs.

## 4. Structural Problems

1. Canonical authority conflict.
- `docs/overview/start-here.md` points to `docs/repo_cleanup/canonical_document_map.md`.
- That map still declares unifying/universal items canonical.
- Recent hardening lane recommends strict restricted-claim framing and architecture rewrite.

2. Research-program folder overload.
- `docs/research-program/` has 129 files, including top-result summaries, overlap audits, theorem candidates, geometry passes, and branch notes.
- Too many “master reports” with overlapping status language.

3. Known backbone vs restricted novelty not visibly isolated.
- Core theorem spine exists, but universal-framed files in `docs/unifying_theory/` still sit as peer authorities.

4. Methods and theory are not cleanly separated.
- The same concepts appear as theory objects, method diagnostics, and framework claims in different folders.

5. Interpretation sits too close to theorem lanes in navigation.
- Branch maps are clean, but canonical maps and paper paths still route users through broad framework docs.

6. Strongest publishable lane is present but buried.
- Restricted anti-classifier + diagnostics lane exists in fiber branch + structural-information lane.
- It is not the clearest top-level paper/repo identity from start-here paths.

7. Duplicate or near-duplicate namespace patterns increase confusion.
- `soliton-branch` and `soliton_branch`
- `discovery/` vs `docs/discovery/` vs `docs/research-program/*discovery*`
- `theory/` vs `docs/theory/` and `docs/finalization/`

8. Generated/imported evidence hierarchy is not explicit.
- `data/generated/` is large and mixed-tier.
- `data/imported/structural-information-theory/` adds value but no clear global import policy is visible from main docs.

## 5. Strengths Worth Preserving

1. Branch-first front door.
- `/branches/README.md` and branch READMEs are clear and useful.

2. Finalization spine docs.
- `/docs/finalization/theorem-spine-final.md`
- `/docs/finalization/no-go-spine-final.md`

3. Strong restricted theorem package.
- `/docs/fiber-based-recoverability-and-impossibility/`
- `OCP-049/050/052/053` style claims with explicit witnesses.

4. Code+tests credibility.
- `/src/ocp/` + `/tests/math/` are substantial and reproducible.

5. New hardening lane artifacts.
- `/docs/research-program/structural-information-theory/`
- `/data/generated/structural-information-theory/`
- `/scripts/research/run_structural_information_harness.py`

6. Governance discipline exists.
- Proof status map, falsification reports, and claim registries are already in place.

## 6. Rewrite Recommendation

Recommendation: **major architecture rewrite recommended** (deliberate, staged).

Why not incremental-only:
- The issue is not isolated file quality; it is cross-folder authority and layer blending.
- Canonical routing currently conflicts with claim-discipline corrections.
- Incremental edits will not reliably remove competing “master narrative” centers.

Why not destructive reset:
- High-value theorem/test/evidence anchors already exist and should be preserved.

Best approach:
- staged major rewrite that preserves theorem/test artifacts and rehomes narrative/meta layers.

## 7. Target Architecture Recommendation

Use this as target for the next pass.

### Proposed top-level doc architecture

1. `docs/theorem-core/`
- formal statements, assumptions, status, dependencies.
- include known-overlap notes at theorem entry.

2. `docs/restricted-results/`
- branch-limited theorem packages (fiber no-go, augmentation, mismatch, bounded-domain classes).

3. `docs/methods-diagnostics/`
- IDELB/DFMI/CL definitions, harness specs, estimator assumptions, decision-baseline comparisons.

4. `docs/validation-evidence/`
- proof/status maps, witness catalogs, generated-artifact maps, reproducibility pathways.

5. `docs/physics-translation/`
- theorem-grade mappings, validated surrogate mappings, analogy-only notes split explicitly.

6. `docs/meta-governance/`
- originality/overlap audits, claim-scope policy, citation policy, restructure policy.

7. `docs/archive/structured-passes/`
- geometry passes, one-off explorations, superseded “master reports”, cleanup logs.

### Proposed non-doc architecture adjustments

- Keep `src/ocp/`, `tests/`, `scripts/` as core executable layer.
- Add a small `data/README.md` declaring canonical generated paths and import policy.
- Separate `data/generated/` into promoted vs exploratory subtrees (or add manifest-based status labels).

### What moves where (high-level)

Promote/move to theorem-core or restricted-results:
- `docs/finalization/*`
- selected files from `docs/theorem-candidates/`
- selected files from `docs/fiber-based-recoverability-and-impossibility/`

Demote/move to methods-diagnostics:
- descriptor-fiber and harness-method docs currently under `docs/research-program/*` and `docs/meta_theory/*`

Demote/move to physics-translation:
- `docs/physics/*`
- physics-facing parts of structural-information lane

Archive:
- most one-pass `docs/research-program/*.md` that are historical rankings/notes
- exploratory `discovery/*.md` not promoted by theorem status

Keep as-is anchors:
- `branches/` front door
- `src/ocp/`
- `tests/`
- `data/generated/unified-recoverability/`
- `data/generated/structural-information-theory/`

## 8. Risks During Restructure

Do not break:
- theorem IDs and status labels (`OCP-*`, proof maps)
- citation anchors added during hardening
- provenance links for imported structural-information artifacts
- generated artifact references used by tests
- harness reproducibility (`scripts/research/run_structural_information_harness.py`)
- strongest restricted paper lane visibility (anti-classifier + diagnostics)
- known-vs-new distinction language in core theorem docs

Operational risks:
- broken links across many markdown files
- accidental promotion of archived exploratory language
- loss of consistency between docs and generated evidence file names

## 9. Requirements for the restructuring pass

- Build a single authority map first; remove competing canonical maps.
- Enforce six-layer separation: backbone, restricted results, methods, evidence, interpretation, governance.
- Keep branch READMEs and final theorem/no-go spine as preserved anchors.
- Move exploratory and historical pass logs to a structured archive.
- Create explicit “promoted vs exploratory” policy for `data/generated` artifacts.
- Make strongest publishable lane visible from start-here and branch docs.
- Preserve theorem IDs, status labels, citations, and provenance links.
- Add automated link and scope checks after file moves.
- Do not broaden claim scope during restructure.
- End restructure with a post-move overlap/scope sanity audit.
