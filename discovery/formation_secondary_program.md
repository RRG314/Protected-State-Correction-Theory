# Formation Secondary Program

Status: `EXPLORATION / NON-PROMOTED`
Track priority: secondary (separate from main theorem package).

Data source:
- `data/generated/sfpr/formation_secondary_witnesses.csv` (`980` rows)

## Program Goal

Test candidate mechanisms for creating target-relevant structure before claiming any bridge theorem to context-sensitive recoverability.

## Mechanisms Tested

1. constraint generation
2. symmetry breaking
3. context-conditioned differentiation
4. intervention-generated structure
5. feedback-induced structure
6. local-to-global organization
7. optimization-induced structure

## Summary Metrics

- structure-created flag: `397/980`
- post-formation local-exact but not shared-exact: `280/980`
- shared recoverability decreases: `0/980`
- threshold flips in shared augmentation need: frequent (`~50%` overall)

## Mechanism-Level Outcomes

### Constraint generation
- Result: local and shared recoverability both improve in this generator.
- Status: `VALIDATED / EMPIRICAL ONLY`.
- Risk: constructive bias (mechanism often injects target-aligned constraints).

### Symmetry breaking
- Result: local recoverability high, shared recoverability not restored (`140/140` post local-not-shared).
- Status: `CONDITIONAL` meaningful pattern.
- Interpretation: can create contextwise structure without invariant compatibility.

### Context-conditioned differentiation
- Result: no structure-created signal under current metric; persists as local-not-shared regime.
- Status: `DISPROVED` for current structure-creation metric.

### Intervention-generated structure
- Result: strong recoverability improvements in this generator.
- Status: `VALIDATED / EMPIRICAL ONLY`.
- Risk: closely overlaps known intervention-cleaning setups.

### Feedback-induced structure
- Result: structure-created signal appears (`69/140`) but no recoverability gains.
- Status: `CONDITIONAL` (formation-without-recoverability behavior).

### Local-to-global organization
- Result: local recoverability decreases (`local_down=140`), shared unchanged.
- Status: `VALIDATED / EMPIRICAL ONLY` as failure route.

### Optimization-induced structure
- Result: moderate structure-created signals (`70/140`) with no recoverability gains.
- Status: `CONDITIONAL`.

## Secondary-Track Decision

Keep the formation lane active but separate. It is useful for generating candidate bridge anomalies, not for main-track theorem promotion in this pass.
