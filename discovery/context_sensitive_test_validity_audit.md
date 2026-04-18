# Context-Sensitive Test Validity Audit

Status: `EXPLORATION / NON-PROMOTED`

This audit checks whether each major test answers the intended mathematical question.

## Audit Matrix

| Test | Intended mathematical question | Metric/test used | Validity | Main risk | Action |
| --- | --- | --- | --- | --- | --- |
| Conditioned vs invariant split | Does local exactness imply shared exactness? | `local_exact_all` vs `shared_exact` with shared-decoder solve | Strong | linear supported-family scope only | keep |
| Shared decoder feasibility | Is there one decoder for all contexts? | max residual from stacked linear system (`CID`) | Strong | partly definitional | keep + document as characterization |
| Descriptor insufficiency | Can rank/budget classify shared exactness? | predictor mismatch counts + opposite signature groups | Strong | descriptor signature discretization | keep + add alternative signatures next pass |
| Shared augmentation threshold | Minimal shared rows needed for invariant exactness | constrained combinational search over measurement-library pool | Moderate | pool dependence; finite search horizon (`<=4`) | keep with explicit class restriction |
| Family enlargement fragility | Does adding one context flip invariant verdict? | `shared_exact` vs `enlarged_shared_exact` | Moderate | extra-context generator choice | keep + add multiple enlargement protocols |
| Formation structure creation | Does mechanism create target-relevant structure? | alignment/DLS deltas and recoverability deltas | Weak-to-moderate | constructive mechanism bias | keep as secondary-only |
| Formation-recoverability bridge | Do formation events change context gap/threshold behavior? | pre/post local/shared/threshold comparisons | Moderate | route templates are synthetic | keep as exploratory only |

## Conceptual Correctness Findings

1. Main-track split tests are conceptually aligned with theorem questions.
2. Augmentation threshold is mathematically relevant, but threshold values depend on admissible augmentation class.
3. Formation tests remain vulnerable to setup artifacts and cannot support promotion claims yet.

## Specific Weaknesses Detected

1. If direct target-row augmentation is allowed, thresholds trivialize; this was explicitly blocked in this pass.
2. Formation generators include high-control templates that can manufacture positive outcomes.
3. No non-synthetic benchmark family was used in this pass.

## Redesign Steps Applied in This Pass

1. Removed direct target-row injection from augmentation candidate pool.
2. Raised augmentation search depth (`r<=4`) and retained pool-bounded scope labels.
3. Kept formation lane explicitly secondary and non-canonical.

## Additional Required Upgrades

1. Add adversarially generated contexts that preserve descriptors while randomizing geometry.
2. Add benchmark families from non-synthetic datasets or domain simulators.
3. Add proof-backed lower bounds for augmentation threshold to reduce dependence on search catalogs.

## Audit Conclusion

Main-track tests are sufficiently aligned for a conditional narrow theory package. Secondary formation tests are useful for exploration but not theorem promotion.
