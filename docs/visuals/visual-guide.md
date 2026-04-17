# OCP Visual Guide

This package is a theorem-faithful visual layer for non-expert readers.

Every figure here is generated from explicit equations, finite toy maps, or canonical branch examples in code. Nothing is decorative art.

Quick full-image page:
- [Visual Gallery](./visual-gallery.md)
- [Visual Gallery (HTML, guided learning flow)](./visual-gallery.html)
- [Complete Visual Story (HTML tutorial)](./ocp-complete-visual-story.html)
- [Figure Index (clickable/downloadable/citable)](./figure-index.html)
- [Visual Figure BibTeX](../references/ocp-visual-figures.bib)
- [Visual Center Changelog (2026-04-16)](./visual-center-changelog-2026-04-16.md)
- [Visual Center Design Rationale](./visual-center-design-rationale.md)

## Regeneration

Entry point:
- [`scripts/visuals/generate_visuals.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/scripts/visuals/generate_visuals.py)

Run:
```bash
PYTHONPATH=src uv run --with matplotlib --with pillow python scripts/visuals/generate_visuals.py
```

Outputs:
- figures and animations: [`docs/visuals/generated/`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated)
- data summary used by all figures: [`data/generated/visuals/visual_summary.json`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/visuals/visual_summary.json)
- generation manifest: [`docs/visuals/generated/manifest.json`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/manifest.json)

## Validation

Math correctness tests:
- [`tests/math/test_visuals.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/tests/math/test_visuals.py)

Generated-artifact consistency tests:
- [`tests/examples/test_visuals_generated_consistency.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/tests/examples/test_visuals_generated_consistency.py)
- [`tests/examples/test_visual_gallery_integrity.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/tests/examples/test_visual_gallery_integrity.py)

Gallery/media integrity checker:
- [`scripts/validate/check_visual_gallery.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/scripts/validate/check_visual_gallery.py)

Run:
```bash
PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_visuals.py tests/examples/test_visuals_generated_consistency.py tests/examples/test_visual_gallery_integrity.py
python scripts/validate/check_visual_gallery.py
```

## Color Semantics

- protected / keep: teal
- disturbance / contamination: rust
- observation / collapse map: blue
- impossible / no-go: crimson
- repair / augmentation: amber

## Figure Set

### A. Core Geometry Of Recovery
Files:
- [`A_core_geometry_2d.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/A_core_geometry_2d.svg)
- [`A_core_geometry_2d.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/A_core_geometry_2d.png)
- [`A_core_geometry_3d.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/A_core_geometry_3d.svg)
- [`A_core_geometry_3d.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/A_core_geometry_3d.png)

Status:
- exact examples (2D exact split, 2D misaligned orthogonal-projector failure, 3D overlap non-identifiability).

Math source:
- `P_S = Q_S Q_S^T` from orthonormal basis of `S`.
- 2D exact case: `D ⟂ S` so `P_S(s+d)=s`.
- 2D misaligned case: `D` not orthogonal to `S`, so `P_S(s+d) != s`.
- 3D overlap case: `dim(S ∩ D)=1` and two decompositions produce the same state.

### B. Fiber-Collapse Visualization
Files:
- [`B_fiber_bipartite.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/B_fiber_bipartite.svg)
- [`B_fiber_partition_tree.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/B_fiber_partition_tree.svg)
- [`B_fiber_table_heatmap.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/B_fiber_table_heatmap.svg)
- plus PNG versions in the same folder.

Status:
- exact finite toy map.

Math source:
- state set `Ω = {0,1}^3`, map `M(x1,x2,x3)=(x1,x2)`.
- fibers are equivalence classes under equal observations.
- `τ_const(x)=x1+2x2` is fiber-constant.
- `τ_nonconst(x)=x1+x3` is not fiber-constant.

The visuals correspond directly to the theorem pattern: exact recoverability iff target is constant on fibers.

### C. Exact vs Impossible Transition
Files:
- [`C_transition_keyframes.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/C_transition_keyframes.svg)
- [`C_exact_vs_impossible_transition.gif`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/C_exact_vs_impossible_transition.gif)
- [`C_exact_vs_impossible_transition.mp4`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/C_exact_vs_impossible_transition.mp4)

Status:
- exact finite-dimensional parametric family.

Math source:
- `O_α = [[1,0],[0,α]]`, `L=[0,1]`, states on a fixed finite grid.
- threshold at `α=0`: row-space inclusion fails and fibers merge.

### D. Same-Rank Insufficiency
Files:
- [`D_same_rank_insufficiency.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/D_same_rank_insufficiency.svg)
- [`D_same_rank_insufficiency.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/D_same_rank_insufficiency.png)

Status:
- exact witness from canonical same-rank counterexample (`OCP-047`/`OCP-049` lane).

Math source:
- two observation operators with equal rank and opposite exactness verdict.
- visualized by angle/alignment of protected target row with each row space.

### E. Minimal Augmentation
Files:
- [`E_minimal_augmentation.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/E_minimal_augmentation.svg)
- [`E_minimal_augmentation.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/E_minimal_augmentation.png)

Status:
- exact restricted-linear augmentation witness (`OCP-045` lane).

Math source:
- `δ(O,L;F) = rank([OF;LF]) - rank(OF)`.
- before: impossible.
- after adding one computed augmentation row: exact recovery.

### F. Periodic Exact vs Bounded-Domain Failure
Files:
- [`F_periodic_vs_bounded.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/F_periodic_vs_bounded.svg)
- [`F_periodic_vs_bounded.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/F_periodic_vs_bounded.png)

Status:
- exact branch + no-go branch visualized from canonical formulas.

Math source:
- periodic field with contamination and exact Helmholtz projection recovery.
- bounded-domain transplant counterexample with reduced divergence but boundary-normal mismatch.
- bounded Hodge-compatible metric values included to show why divergence-only success is insufficient.

### G. Recoverability Threshold Surfaces
Files:
- [`G_threshold_surfaces.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/G_threshold_surfaces.svg)
- [`G_threshold_surfaces.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/G_threshold_surfaces.png)

Status:
- exact/validated branch surfaces.

Math source:
- control finite-history sweep: exact vs asymptotic-only vs impossible regimes.
- noisy weaker-vs-stronger target hierarchy: exact/approximate/impossible split.

### H. Cross-System Structural Map
Files:
- [`H_cross_system_structural_map.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/H_cross_system_structural_map.svg)
- [`H_cross_system_structural_map.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/H_cross_system_structural_map.png)

Status:
- schematic (explicitly labeled schematic).

What is exact in this schematic:
- node statuses (`exact anchor`, `asymptotic only`, `no-go boundary`, `branch-limited theorem`) and claim IDs are exact repo status labels.

What is schematic:
- node layout and routing are explanatory only.

### I. Alignment Landscape
Files:
- [`I_alignment_landscape.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/I_alignment_landscape.svg)
- [`I_alignment_landscape.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/I_alignment_landscape.png)

Status:
- exact finite-dimensional sweep.

Math source:
- rank-1 observation row scans all 3D orientations while target row stays fixed.
- rank is constant over the sweep; exactness varies by alignment only.

### J. Perturbation Fragility
Files:
- [`J_perturbation_fragility.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/J_perturbation_fragility.svg)
- [`J_perturbation_fragility.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/J_perturbation_fragility.png)

Status:
- exact local perturbation family.

Math source:
- perturb an exact row direction `(1,0,0)` to `(1,u,v)` and normalize.
- exactness is isolated at `(u,v)=(0,0)`; residual and collision gap rise immediately away from center.

### K. Family-Enlargement Failure
Files:
- [`K_family_enlargement_failure.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/K_family_enlargement_failure.svg)
- [`K_family_enlargement_failure.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/K_family_enlargement_failure.png)

Status:
- exact witness (false positive under family enlargement).

Math source:
- observation `O=[e1^T; e2^T]`, target `L=e3^T`.
- exact on restricted family `x3=0`, impossible on enlarged family with varying `x3`.

### L. Dynamic Rate Layer
Files:
- [`L_dynamic_rate_layer.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/L_dynamic_rate_layer.svg)
- [`L_dynamic_rate_layer.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/L_dynamic_rate_layer.png)

Status:
- exact/validated finite-history + observer-rate outputs.

Math source:
- uses `functional_observability_sweep` and observer simulation reports.
- shows finite-history exactness matrix and semigroup-style error decay traces.

### M. Augmentation Direction Scan
Files:
- [`M_augmentation_direction_scan.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/M_augmentation_direction_scan.svg)
- [`M_augmentation_direction_scan.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/M_augmentation_direction_scan.png)

Status:
- exact restricted-linear one-row augmentation scan.

Math source:
- fixed impossible base `O`, fixed target `L`.
- one added row rotates on a unit circle in `(e2,e3)` components.
- exactness depends on added direction, not only row count.

### N. Periodic vs Bounded Contamination Sweep
Files:
- [`N_periodic_bounded_contamination_sweep.svg`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/N_periodic_bounded_contamination_sweep.svg)
- [`N_periodic_bounded_contamination_sweep.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/N_periodic_bounded_contamination_sweep.png)

Status:
- validated contamination-parameter sweep.

Math source:
- repeated evaluation of periodic exact projection and bounded transplant branch metrics.
- tracks divergence and boundary-normal metrics across contamination values.

### O. Contact Sheet And Atlas
Files:
- [`O_visual_contact_sheet.png`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/O_visual_contact_sheet.png)
- [`visual-atlas.pdf`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/visuals/generated/visual-atlas.pdf)

Status:
- exact render bundle (composed from generated panels; no hand editing).

## Exact vs Schematic Index

- Exact: A, B, C, D, E, F, G, I, J, K, L, M, N.
- Schematic with exact status labels: H.
- Render bundle: O.

## Source Data Layer

All figure data is computed in:
- [`src/ocp/visuals.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/visuals.py)

This module is designed so tests can validate the math independent of plotting libraries.
