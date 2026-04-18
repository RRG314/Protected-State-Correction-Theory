# SFPR Test Validity Audit

Status: `EXPLORATION / NON-PROMOTED`

This audit checks whether each computational test actually answers its intended mathematical question.

## Audit Table

| Test family | Mathematical question | Metric used | Validity verdict | Hidden assumption risk | Redesign needed |
| --- | --- | --- | --- | --- | --- |
| Collapse/indistinguishability | Does fiber collision force exact failure? | `DLS`, exact residual | **Strong** | finite-state enumeration approximation | Low; keep, but add symbolic collision witnesses |
| Context-invariant split | Can local exactness fail globally under shared decoder constraint? | `CID`, local/global exact flags | **Strong** | fixed shared decoder dimension and linearity | Medium; add heterogeneous context dimensions |
| Amount-only insufficiency | Do rank/count/budget classify exactness? | descriptor-vs-verdict mismatch counts | **Strong** | descriptor buckets include logdet discretization | Low; include descriptor-invariant random seeds |
| Design conflict | Does D-style design fail target exactness while alignment succeeds? | pairwise `d_opt` vs `alpha_opt` exactness | **Moderate** | candidate pool is synthetic and small | High; add adversarial and real benchmark pools |
| Intervention split | Does intervention improve recoverability at fixed count? | `IL = residual(obs)-residual(itv)` | **Moderate** | observational/interventional maps partly constructed | High; add SEM-generated interventions with randomized confounders |
| Formation routes | Does structure creation improve recoverability? | new-structure flag + recoverability change | **Weak-to-Moderate** | several routes are constructive by design | High; replace with counterfactual formation controls |
| Persistence fragility | Can small changes destroy global recoverability? | drift/noise threshold flips | **Moderate** | perturbation scales chosen heuristically | Medium; add scale-normalized perturbation families |
| Distributed allocation | Does allocation geometry matter beyond total budget? | `PSI`, joint vs single exactness | **Moderate** | two-terminal template limitation | Medium; extend to k>2 and communication constraints |

## Key Failure Risks in Current Tests

1. **Constructive bias** in formation and intervention templates can produce expected wins by construction.
2. **Finite synthetic families** can overestimate universality.
3. **Metric coupling** (`TSF` from alignment) can hide true independence from row-space quantities.
4. **Descriptor signature choice** can generate apparent anti-classifier counts if bins are too coarse.

## Corrections Applied in This Pass

1. Kept all claims scope-limited to supported finite families.
2. Downgraded design/intervention/formation claims to `VALIDATED / EMPIRICAL ONLY` unless proof-level support exists.
3. Explicitly separated `PROVED` split/no-go statements from empirical diagnostics.

## Required Next Validity Upgrades

1. Replace hand-crafted formation/intervention templates with randomized mechanism generators and holdout families.
2. Add theorem-aware stress tests that preserve descriptor signatures while randomizing geometry.
3. Add symbolic checks for at least one conditioned-vs-invariant theorem family.
4. Add cross-validation on external or historical witness sets to detect setup overfit.

## Audit Conclusion

The strongest tests are collapse and context-invariant split checks. The weakest are formation and design/intervention mechanism tests due to construction bias. Current SFPR conclusions are valid as a **narrow exploratory framework assessment**, not as promotion-grade theorem evidence.
