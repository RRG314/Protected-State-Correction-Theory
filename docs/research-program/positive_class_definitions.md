# Positive Class Definitions

Scope of all classes in this file:
- finite-dimensional linear mixed-observation systems,
- context-indexed measurement families,
- branch-limited theorem discipline.

Base objects:
- state space `X = R^n`,
- target map `tau(x) = Lx` with `L in R^{q x n}`,
- context records `y_c = M_c x`, `M_c in R^{p x n}` for `c in C={1,...,k}`,
- optional shared augmentation `U in R^{r x n}` appended to all contexts.

## Class C1 — Compatibility-Organized Recoverable Systems (CORS)

Membership:
A system belongs to CORS iff there exists a shared decoder `D in R^{q x p}` satisfying
`D M_c = L` for all contexts `c`.

Equivalent architecture form:
Let `G = Q M_1` with `Q` spanning context agreement rows.
Then CORS iff `row(L) subseteq row(G)`.

Exact recoverability notion:
- shared/global exact recoverability.

Failure boundary:
- any positive compatibility defect `rank([G;L]) - rank(G) > 0` exits CORS.

Augmentation:
- external (not built in).

Status of class:
- mathematically nontrivial but close to canonical compatibility logic.

## Class C2 — Augmentation-Completable Recoverability Systems (ACRS)

Membership:
A system belongs to ACRS if:
1. baseline shared exactness may fail,
2. there exists shared augmentation restoring exactness.

Free-completion criterion:
- free threshold `r_free^* = rank([G;L]) - rank(G)`.
- ACRS-free always completable in supported linear class with `r_free^*` rows.

Constrained-completion criterion:
For candidate library `C`, define
`delta_C = rank([G;C;L]) - rank([G;C])`.
- `delta_C = 0` => completable with full library,
- `delta_C > 0` => not completable from that library.

Failure boundary:
- positive library defect.

Augmentation:
- built-in as class feature.

## Class C3 — Context-Consistent Recoverability Systems (CCRS)

Membership:
A system belongs to CCRS if:
1. each context is locally exact (`forall c, exists D_c: D_c M_c = L`),
2. context coherence holds (`exists D_*: D_* M_c = L` for all `c`).

Interpretation:
- CCRS is the local-to-global consistent subclass of local exact systems.

Failure boundary:
- local exact/global fail split (`G=1` in context-invariance gap notation).

Augmentation:
- optional; can move a local-only system into CCRS.

## Class C4 — Descriptor-Lift Recoverability Systems (DLRS)

Membership:
A system belongs to DLRS if classification/decision is performed using
`(amount descriptor, compatibility lift descriptor)` rather than amount-only descriptors.

Minimal lift descriptor in this pass:
- `CID`,
- `r_free^*`,
- `delta_C` (when constrained library is declared).

Recoverability role:
- design/diagnostic class, not a standalone theorem class.

Failure boundary:
- amount-only descriptor collisions with opposite exactness verdicts.

Augmentation:
- optional but naturally coupled through `r_free^*` and `delta_C`.

## Class admissibility note

These are meaningful only with explicit declarations of:
1. supported family,
2. augmentation admissibility,
3. context structure,
4. target map class.

Without these declarations the classes collapse into vague restatements and should not be promoted.
