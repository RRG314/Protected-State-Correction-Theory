# Invariant Formalization and BH Placement Master Report

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

Primary artifacts from this pass:
- `docs/research-program/invariant_formal_audit.md`
- `docs/research-program/invariant_normalization_map.md`
- `docs/research-program/invariant_theorem_spine_draft.md`
- `docs/research-program/invariant_no_go_spine_draft.md`
- `docs/research-program/invariant_proof_pressure_log.md`
- `docs/research-program/invariant_expansion_master.md`
- `data/generated/invariants/deep_invariant_catalog.csv`
- `data/generated/invariants/deep_invariant_stress.csv`
- `discovery/invariant_new_candidates_master.md`
- `discovery/invariant_new_definitions_master.md`
- `discovery/invariant_new_falsification_log.md`
- `discovery/invariant_global_falsification_report.md`
- `docs/physics/bh_cosmology_claim_audit.md`
- `docs/physics/bh_cosmology_literature_positioning.md`
- `docs/research-program/bh_repo_fit_decision.md`
- `docs/research-program/bh_keep_demote_cut_map.md`

---

## A. Invariant program verdict

### A1) What exact invariant stack survives now?

Surviving stack:
1. Core exactness invariants: fiber constancy/factorization and row-space/kernel compatibility.
2. Context-sensitive layer: `CID`/context-gap split.
3. Repair layer: `delta_free` (unconstrained threshold), `delta_C` (candidate-library constrained defect).
4. Descriptor anti-classifier layer: `DFMI`, `IDELB`, `CL`/descriptor-lift gains.
5. Stress layer (diagnostic only): enlargement/mismatch/perturbation fragility indicators.

### A2) What was clarified?

1. Canonical notation and branch labels were normalized.
2. Collision-gap regime was explicitly split into exact vs proxy computation modes.
3. Free vs constrained augmentation was separated cleanly (`delta_free` vs `delta_C`).
4. Context coherence was scoped as supported-family theorem content, not universal law.

### A3) What was expanded?

Deep evidence expansion:
- deep catalog rows: `2640`
- deep stress rows: `116`
- `context_gap=1` rows: `1096`
- `delta_free` nonzero frequencies: `1:721`, `2:585`, `3:408`, `4:275`
- `delta_C>0` rows: `26`
- fragility flags in stress: `115/116`

### A4) What new invariants survived?

Most credible additive candidates:
1. `SCD = (delta_free, delta_C)` as a two-axis completion defect package.
2. `CCD` (CID-form context coherence defect) as mergeability zero-test.
3. `DLG` (descriptor-lift gain vector) for anti-classifier ambiguity reduction.

Status:
- all three: `PROVED ON SUPPORTED FAMILY` with explicit scope limits.

### A5) Which are theorem-grade vs diagnostic?

Theorem-grade (supported-family):
- CID zero-test equivalence,
- conditioned-vs-shared split existence,
- positive shared augmentation thresholds,
- constrained library no-go (`delta_C`) and gain-insufficiency,
- descriptor-lift ambiguity reduction on catalog class.

Diagnostic-only:
- enlargement fragility rates,
- mismatch-instability slopes,
- high-null collision proxies,
- branch-transfer alignment heuristics.

### A6) What collapsed?

Collapsed claims:
1. Any universal new invariant replacing fiber/row-space core.
2. Universal exact collision-gap threshold claims in high-null regimes.
3. Broad branch-transfer invariance claims without independent theorem proofs.

### A7) Strongest theorem package now

Strongest reviewer-safe package:
1. T0/T1 core exactness characterization,
2. T2/T3 context split + CID equivalence,
3. T4/T5/T6 augmentation + constrained-library theorem/no-go cluster,
4. T7 descriptor-lift quantitative anti-classifier theorem (catalog-scoped).

### A8) Exact invariant lane to push next

Highest-value lane:
- **augmentation-threshold invariant program** (`CID + delta_free + delta_C`) with formal bounds and candidate-library geometry theorems.

---

## B. Positive/design side verdict

### B9) Can the invariant stack support a theorem-backed design framework?

Yes, on restricted classes.

Current theorem-backed design flow:
1. feasibility gate: `CID = 0 ?`
2. if not feasible, compute free completion cost `delta_free`,
3. check constrained-library realizability via `delta_C`,
4. apply descriptor-lift diagnostics (`DFMI/IDELB/CL`) for anti-classifier robustness.

Status:
- `PROVED ON SUPPORTED FAMILY`.
- no universal design optimality claim.

### B10) Constructive checklist that survives

Surviving constructive checklist:
1. test shared exactness with CID,
2. quantify minimum free repair via `delta_free`,
3. test candidate-library feasibility via `delta_C`,
4. reject amount-only decisions when descriptor-fiber ambiguity remains high,
5. stress-test under enlargement/mismatch before promotion.

---

## C. BH/cosmology placement verdict

### C11) What is actually new?

Most BH/cosmology content is not new theorem content.

What appears additive:
1. disciplined claim/status packaging,
2. correction logs (temperature factor, Davies point fix),
3. numerical observability-degeneracy benchmark tables,
4. a small set of clearly posed open problems.

### C12) What is known/reframed?

Predominantly known/reframed:
- linearized gauge decomposition,
- first-law thermodynamics identities,
- GW chirp-mass degeneracy framing,
- Page-curve baseline interpretations,
- standard Fisher-geometry decomposition facts.

### C13) Theorem-grade vs observational

- `PROVED` (mostly known identities): first-law/entropy identities, selected analytic constraints.
- `VALIDATED / NUMERICAL ONLY`: Fisher correlations, Hubble contamination tables, Rényi sensitivity numerics.
- `OPEN`: BH alignment invariants, exact `rho(t/t_Page)` laws, several proposed conservation extensions.

### C14) What belongs in OCP?

Belongs in OCP only as:
- **narrow noncanonical physics extension notes** with strict labels.
- no core theorem-spine promotion.

### C15) What belongs in SDS?

Better SDS-side (or companion repo) fit:
- broad BH thermodynamic synthesis narratives,
- extremality-as-ground-state framing,
- entropy-unification narrative expansions.

### C16) What remains noncanonical/spin-off?

Remain noncanonical or spin-off:
- conjectural BH Fisher conservation identities,
- broad cosmology-resolution claims,
- any claim of new foundational BH theory via OCP.

---

## Final BH placement class

**SPLIT PLACEMENT WITH STRICT LABELS**.

Operationally:
1. keep narrow benchmark/diagnostic subset in OCP noncanonical physics notes,
2. route broad thermodynamic synthesis toward SDS-side/external,
3. demote unresolved/conjectural material from promotion queue.

---

## Overall pass verdict

1. Invariant program is sharper and more formalized than baseline, with a clear theorem-ready restricted package.
2. New invariant search produced additive scoped candidates, but no universal replacement of core fiber/row-space logic.
3. Positive-recoverability/design architecture is supportable on restricted classes through `CID + delta_free + delta_C`.
4. BH/cosmology material should be retained only under strict placement and status control; no automatic core promotion.

---

## Best serious next move after invariant formalization + BH placement pass

Recommended move: **2. push CID + delta_free + delta_C into one formal paper lane**.

Why this is the strongest next step:
1. it has the best theorem/no-go balance,
2. it is already backed by deep catalog evidence,
3. it gives immediate constructive design value,
4. it avoids overclaiming in weaker physics-transfer zones.

Immediate execution plan:
1. write one proof-clean paper draft for the context/augmentation theorem package,
2. add bound-tightening work for `delta_free` and feasibility conditions for `delta_C`,
3. keep BH/cosmology as strictly labeled noncanonical diagnostics until new theorem content appears.
