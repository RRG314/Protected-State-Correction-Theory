# Discovery Inventory

This inventory records the local material used to build the OCP research program. It is intentionally selective: the goal is to capture the files that genuinely contributed mathematical structure, operator constructions, program boundaries, or provenance.

## Totals
- Curated high-value sources: **12**
- Canonical sources: **8**
- Partial sources: **2**
- Speculative sources kept only for provenance: **1**
- Superseded sources kept only for provenance: **1**

## Selection Logic
- Prefer files that expose exact operators, exact tests, or clear impossibility boundaries.
- Keep broad analogy material only when it helped sharpen a limitation or a design criterion.
- Treat QEC as the exact anchor, MHD projection cleaning as the exact continuous anchor, and GLM/control-style feedback as the asymptotic branch.

## Highest-Value Inputs
### `divergence_control.md`
- Path: `/Users/stevenreid/Documents/New project/mhd-toolkit/docs/divergence_control.md`
- Relevance: 10/10
- Status: `canonical`
- Why it mattered: High-value local summary of projection cleaning and GLM cleaning as concrete correction operators.

### `projection.py`
- Path: `/Users/stevenreid/Documents/New project/mhd-toolkit/mhd_toolkit/divfree/projection.py`
- Relevance: 10/10
- Status: `canonical`
- Why it mattered: FFT-based projection-cleaning implementation; best exact continuous-operator anchor for OCP.

### `glm.py`
- Path: `/Users/stevenreid/Documents/New project/mhd-toolkit/mhd_toolkit/divfree/glm.py`
- Relevance: 9/10
- Status: `canonical`
- Why it mattered: Dedner-style GLM cleaner; useful asymptotic correction comparison to exact projection.

### `test_divergence_cleaning.py`
- Path: `/Users/stevenreid/Documents/New project/mhd-toolkit/tests/test_divergence_cleaning.py`
- Relevance: 8/10
- Status: `canonical`
- Why it mattered: Empirical validation of projection and GLM divergence reduction.

### `correction_gap_formalization.md`
- Path: `/Users/stevenreid/Documents/sds-research-repo/docs/correction-gap/correction_gap_formalization.md`
- Relevance: 9/10
- Status: `canonical`
- Why it mattered: Prior theorem-schema / no-go development showing how broad unification can collapse to tautology if not category-specific.

### `cross_domain_analysis.md`
- Path: `/Users/stevenreid/Documents/sds-research-repo/docs/correction-gap/cross_domain_analysis.md`
- Relevance: 6/10
- Status: `partial`
- Why it mattered: Cross-system analogy layer; useful for provenance, but not promoted as theorem-level by itself.

## Machine-Readable Artifact
- CSV inventory: `/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/inventories/discovery_inventory.csv`
