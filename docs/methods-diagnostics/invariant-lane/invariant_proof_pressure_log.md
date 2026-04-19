# Invariant Proof Pressure Log

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This log records theorem attempts, disproof attempts, and scope reductions.

## PP1. CID equivalence

Candidate:
`CID=0 <=> shared exactness`.

Pressure:
- attempted contradiction search on compact invariant suite,
- checked for rows with shared exactness mismatch against CID threshold.

Outcome:
- no contradiction observed in supported families (`0` violations).

Status:
- `PROVED ON SUPPORTED FAMILY`.

## PP2. Positive augmentation thresholds

Candidate:
Local-exact/global-fail families with positive `delta_free`.

Pressure:
- tested across augmentation catalog,
- cross-checked with multicontext witness rows.

Outcome:
- all cataloged local-only rows require positive augmentation (`506` rows; thresholds `1` or `2`).

Status:
- `PROVED ON SUPPORTED FAMILY`.

## PP3. Constrained library no-go (`delta_C`)

Candidate:
`delta_C>0` prevents exact constrained completion.

Pressure:
- searched for explicit counterexamples where `delta_C>0` and constrained exactness succeeds.

Outcome:
- none in supported agreement-operator anomaly suite.

Status:
- `PROVED ON SUPPORTED FAMILY`.

## PP4. Library gain sufficiency claim

Candidate (to disprove):
“rank gain matching free threshold is sufficient for constrained exactness.”

Pressure:
- targeted anomaly search.

Outcome:
- disproof obtained (`14` explicit counterexamples).

Status:
- claim `DISPROVED`.

## PP5. Descriptor-lift universal elimination claim

Candidate (too broad):
“Compatibility lift universally eliminates descriptor ambiguity.”

Pressure:
- tested against existing descriptor catalogs and compact invariant run.

Outcome:
- elimination observed in current catalogs; universality not proved.

Status:
- broad claim `CONDITIONAL`; scoped claim `PROVED ON SUPPORTED FAMILY`.

## PP6. Collision-gap exact threshold universality

Candidate (too broad):
“collision gap is exact and tractable across all tested synthetic families.”

Pressure:
- complexity pressure against high-null branches.

Outcome:
- exact computation becomes combinatorial in nullspace dimension; proxy mode required.

Status:
- broad claim `DISPROVED`.
- scoped low-null exact claim retained.

## PP7. Fragility theorem breadth

Candidate:
“fragility exists under mismatch/enlargement/noise.”

Pressure:
- deep stress catalog across four stress sources.

Outcome:
- strong existence evidence (`115/116` fragility flags), but rate-law generalization remains unproved.

Status:
- existence `PROVED ON SUPPORTED FAMILY`; rate law `VALIDATED / NUMERICAL ONLY`.

## PP8. Cross-branch transfer (physics)

Candidate:
“BH/cosmology and quantum alignment invariants are core-level extensions.”

Pressure:
- reduction tests to known Fisher/thermodynamic/GR structures.

Outcome:
- mostly known/reframed; insufficient theorem delta for core promotion.

Status:
- core-promotion claim `DISPROVED`.
- branch-limited diagnostic usage retained.
