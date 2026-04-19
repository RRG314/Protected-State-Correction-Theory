# Formal Positive-Theory Draft (Restricted Structural Information)

Date: 2026-04-19  
Status labels in this document are mandatory and local-scope.

## 1) Scope and nonclaims

Scope:
- finite and restricted-linear admissible families,
- recoverability of declared targets from declared records,
- falsification-first no-go + compatibility diagnostics.

Nonclaims:
- no new universal scalar information law,
- no information-ontology or new force claims,
- no universal physics theorem beyond declared surrogate classes.

## 2) Primitive object (MP-1)

Define the restricted object

`I = (A, M, T, Pi_M, Pi_T, C_{M,T})`, where:

- `A` is a declared admissible family,
- `M: A -> Y` is the record map,
- `T: A -> Z` is the target map,
- `Pi_M` is the record-fiber partition,
- `Pi_T` is the target-fiber partition,
- `C_{M,T}` is a compatibility-obstruction component (zero in exact regime).

Executable finite representation in this repo:
- `src/ocp/structural_information.py::StructuralInformationObject`.

Status:
- `CONDITIONAL` (typed object finalized for finite/restricted classes only).

## 3) Axiom sketch (restricted)

Axiom A1 (Exactness):
- `Rec(I)=1` iff each block of `Pi_M` is contained in a block of `Pi_T`.

Axiom A2 (Loss witness):
- `Loss(I)=1` iff there exists `x1,x2 in A` with `M(x1)=M(x2)` and `T(x1)!=T(x2)`.

Axiom A3 (Defect nonnegativity):
- `D(T|M) >= 0`, and `D(T|M)=0` iff exactness holds in finite deterministic setting.

Axiom A4 (Coarsening monotonicity, declared class):
- if `Y2 = g(Y1)` on same sample set, then `D(T|Y2) >= D(T|Y1)`.

Axiom A5 (No scalar sufficiency, declared witness classes):
- amount-only descriptors are not exact classifiers on declared witness classes.

Status:
- A1/A2/A3: `PROVED` on finite/restricted classes in this repo.
- A4: `PROVED` on finite coarsening chains and `VALIDATED_SURROGATE` in imported Hawking-like lane.
- A5: `PROVED` on restricted witness classes (`OCP-049/OCP-050`) and `VALIDATED` out-of-family diagnostics.

## 4) The strongest branch-limited theorem package currently supported

T1 (known backbone, not novel):
- exact recoverability iff factorization/fiber constancy (`KNOWN REFORMULATION`).

T2 (restricted no-go, promoted):
- no amount-only exact classifier on declared restricted witness classes (`PROVED`, restricted).

T3 (stability above factorization, restricted):
- with exact decoder `K` and perturbation `Delta`, bounded-coefficient error is upper-bounded by `||K Delta|| * sqrt(m) * B` (`PROVED`, restricted linear box class).

T4 (family fragility and mismatch):
- family-enlargement false positives and mismatch instability (`PROVED`, restricted classes).

T5 (compatibility lift diagnostics):
- compatibility-augmented profile reduces descriptor-fiber irreducible lower bound in all scored lanes (`VALIDATED`, diagnostic law).

## 5) What is known backbone versus repo-distinct

Known backbone (must be cited as known):
- factorization/sufficiency relations,
- identifiability/observability structural limits,
- coarse-graining information loss frameworks.

Repo-distinct (restricted):
- executable finite witness catalog and anti-classifier diagnostics,
- branch-limited family-enlargement and mismatch theorem package,
- integrated local harness across OCP + hidden-state/gravity surrogate lanes.

## 6) Explicit overlap positioning

Closest overlap anchors (non-exhaustive):
- Doob-Dynkin/sufficiency style factorization: <https://arxiv.org/abs/1801.00974>
- Blackwell experiment comparison: <https://digicoll.lib.berkeley.edu/record/112749/files/math_s2_article-08.pdf>
- Structural identifiability: <https://www.sciencedirect.com/science/article/abs/pii/002555647090132X>
- Nonlinear observability: <https://doi.org/10.1109/TAC.1977.1101601>

## 7) Why this is not just language-only

This draft remains branch-limited and does not claim foundational novelty, but it is not only wording because it now has:
- executable object operations,
- a restricted stability theorem with checks,
- unified cross-domain falsification artifacts,
- explicit decision-baseline comparisons.

## 8) Remaining open pieces before broader promotion

- a stronger stability theorem beyond fixed linear decoder on restricted box families,
- theorem-grade semigroup degradation law beyond surrogate trend checks,
- explicit non-reducibility theorem for vector profile versus amount-only scalars on broader external datasets.
