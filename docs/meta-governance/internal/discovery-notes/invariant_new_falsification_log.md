# New Invariant Falsification Log

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This log records direct attacks on the new-candidate invariants defined in `docs/meta-governance/internal/discovery-notes/invariant_new_definitions_master.md`.

## Attack matrix

### NI-1 `CCD` (context-coherence defect)

Attack A1 (rank/count disguise):
- Test: same amount descriptors with different `CCD` and opposite shared verdict.
- Outcome: **SURVIVES**.

Attack A2 (row-space restatement only):
- Test: check whether `CCD` adds beyond single-context row-space inclusion.
- Outcome: **PARTIALLY SURVIVES**.
- Reason: still built from linear residual geometry; additive value is in multi-context mergeability, not a new core linear algebra object.

Attack A3 (tiny-hand-built only):
- Test: deep catalog includes `1800` multicontext rows.
- Outcome: **SURVIVES** on supported synthetic families.

Final status:
- `PROVED ON SUPPORTED FAMILY` zero-test form.
- novelty classification: `PLAUSIBLY DISTINCT PACKAGING`, not universal core novelty.

### NI-2 `SCD = (delta_free, delta_C)`

Attack B1 (relabeling existing augmentation law):
- Test: compare unconstrained `delta_free` to prior minimal augmentation law.
- Outcome: **PARTIALLY SURVIVES**.
- Reason: `delta_free` itself is close to existing logic, but paired constrained defect `delta_C` adds a distinct no-go axis.

Attack B2 (no constrained distinction):
- Test: search cases where free rank-gain appears sufficient but constrained completion fails.
- Evidence: `14` `library_gain_not_sufficient` anomalies.
- Outcome: **SURVIVES**.

Attack B3 (fragile under broader runs):
- Test: deep catalog rows with populated thresholds and constrained defects.
- Evidence: `delta_free` positive in `1989` rows; `delta_C>0` in `26` rows.
- Outcome: **SURVIVES** on supported class.

Final status:
- `PROVED ON SUPPORTED FAMILY`.
- strongest additive invariant package in this pass.

### NI-3 `DLG` (descriptor-lift gain)

Attack C1 (decorative metric with no predictive value):
- Test: IDELB/DFMI shifts between amount-only and lifted descriptors.
- Evidence: both ambiguity metrics drop to zero in current meta catalog.
- Outcome: **SURVIVES** on catalog-level tasks.

Attack C2 (collapses outside curated descriptors):
- Test: universality check.
- Outcome: **PARTIALLY SURVIVES**.
- Reason: universal elimination is not proved; only finite catalog theorem currently justified.

Final status:
- `PROVED ON SUPPORTED FAMILY` (catalog theorem).
- broad claim remains `CONDITIONAL`.

### NI-4 `FEFI` (enlargement fragility)

Attack D1 (artifact of one synthetic family):
- Test: include dedicated enlargement stress plus multicontext flips.
- Evidence: enlargement stress dominates deep stress (`101/116` rows).
- Outcome: **PARTIALLY SURVIVES**.

Attack D2 (no theorem consequence):
- Outcome: **SURVIVES** as diagnostic-only criticism.
- Reason: existence is strong; exact law is not proved.

Final status:
- `VALIDATED / NUMERICAL ONLY` for rates,
- existence-level fragility is `PROVED ON SUPPORTED FAMILY`.

### NI-5 `MIS` (mismatch instability)

Attack E1 (insufficient depth):
- Evidence: small mismatch subset in deep stress (`3` explicit mismatch rows + target mismatch overlays).
- Outcome: **COLLAPSES** as theorem candidate.

Final status:
- `OPEN` / diagnostic exploratory only.

### NI-6 `BCD` (boundary/domain compatibility defect)

Attack F1 (cross-branch normalization failure):
- Test: attempt to normalize CFD/MHD compatibility objects into single core invariant.
- Outcome: **PARTIALLY SURVIVES**.
- Reason: branch-level relevance clear, unified theorem object not established.

Final status:
- `CONDITIONAL`.

### NI-7 BH/measurement alignment ratios

Attack G1 (known Fisher geometry):
- Outcome: **COLLAPSES** as core novelty claim.

Attack G2 (open conjectural extensions only):
- Outcome: **PARTIALLY SURVIVES** as open-problem generator.

Final status:
- `CLOSE PRIOR ART / REPACKAGED` + `OPEN` extensions.

## Falsification summary

Strong survivors:
1. `SCD = (delta_free, delta_C)`
2. `CCD` zero-test scope
3. `DLG` on supported finite catalogs

Survivors with demotion:
1. `FEFI` (diagnostic, not theorem core)
2. `BCD` (branch-limited conditional)

Collapsed as core-new invariant claims:
1. `MIS` (current theorem maturity insufficient)
2. BH alignment ratios as universal invariant candidates
