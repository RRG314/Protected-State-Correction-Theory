# Family-By-Family Decision-Layer Report

## Machine-backed examples

Generated artifacts:
- [`decision_layer_summary.json`](../../data/generated/unified-recoverability/decision_layer_summary.json)
- [`decision_layer_examples.csv`](../../data/generated/unified-recoverability/decision_layer_examples.csv)

## Supported family table

| Family | Scenario | Natural decision | Evidence class | Value beyond current regime label |
| --- | --- | --- | --- | --- |
| Restricted linear | exact target blocked but one-row repair exists | augment the record | `CONDITIONAL` decision corollary on top of `OCP-045` | yes |
| Restricted linear | same blocker, but budget below minimum | stop exact pursuit | `CONDITIONAL` decision corollary on top of `OCP-045` | yes |
| Qubit phase-loss | Bloch target fails, z target exact | switch to weaker target | `PROVED` decision corollary from `OCP-048`, `OCP-051` | yes |
| Periodic modal | current cutoff misses the exact threshold | augment the record | `VALIDATED` family decision | yes |
| Control / finite history | one-step history fails, exact threshold known | augment the record | `VALIDATED` family decision | yes |
| Control / observer | finite-step exactness fails, observer converges | change architecture | `VALIDATED` family decision | yes |
| Bounded-domain CFD | transplanted projector fails strong target | change architecture | `PROVED` / theorem-backed family decision | yes |
| Family enlargement | narrow exactness breaks under enlargement | stop promoting exactness | `PROVED` from `OCP-052` | yes |
| Model mismatch | exact true family but wrong inverse map | stop trusting mismatched inverse map | `CONDITIONAL` from `OCP-053` plus tolerated error | yes |

## Honest summary

The family study shows:
- the decision vocabulary is not empty,
- it is not universal either,
- and its strongest use is to prevent wasted effort and fake promotion on supported families.
