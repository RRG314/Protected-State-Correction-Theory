# Positive Recoverability Candidates

Status: theorem-first extraction pass from current OCP/recoverability core.

Primary question:
Can we state a nontrivial positive architecture theorem without claiming universal recoverability?

Data anchors:
- `data/generated/positive_framework/positive_witness_catalog.csv`
- `data/generated/positive_framework/positive_counterexample_catalog.csv`
- `data/generated/positive_framework/summary.json`
- agreement/context artifacts under `data/generated/context_sensitive_recoverability/`

## Candidate Formulation PFC-1: Compatibility-Organized Recoverable Systems

Core statement:
For context family `{M_c}` and target `L`, exact shared recoverability is guaranteed when the target rowspace is contained in the agreement-lift rowspace (`row(L) subseteq row(QM_1)`).

Assessment:
- mathematical status: `PROVED ON RESTRICTED CLASS`
- novelty status: `KNOWN / REFRAMED` to `PLAUSIBLY DISTINCT` packaging

What is additive:
- converts negative split/no-go language into explicit positive architectural criterion.

What is not additive:
- core mechanism is linear compatibility logic already present in OCP spine.

## Candidate Formulation PFC-2: Augmentation-Completable Recoverability Systems

Core statement:
If compatibility defect is finite in the supported linear class, exact shared recoverability is restorable by minimal free augmentation of size
`r_free^* = rank([G;L]) - rank(G)`.

Assessment:
- mathematical status: `PROVED ON RESTRICTED CLASS`
- novelty status: `PLAUSIBLY DISTINCT` in branch-limited design framing

What is additive:
- positive completion law with explicit minimality and repair interpretation.

Boundary:
- constrained candidate libraries can still fail (`delta_C > 0`).

## Candidate Formulation PFC-3: Context-Consistent Recoverability Systems

Core statement:
Local exactness is not enough; shared exactness requires context-coherence (nonempty shared decoder intersection).

Assessment:
- mathematical status: `PROVED ON SUPPORTED FAMILY`
- novelty status: `CLOSE PRIOR ART / REPACKAGED`

What is additive:
- explicit positive condition for when local exactness actually promotes to global exactness.

## Candidate Formulation PFC-4: Descriptor-Lift Recoverability Systems

Core statement:
Amount-only descriptors fail, but amount descriptor plus compatibility-lift defects (`CID`, `r_free^*`, `delta_C`) separates opposite-verdict families on supported classes.

Assessment:
- mathematical status: `PROVED ON SUPPORTED FAMILY` (finite witness classes)
- novelty status: `PLAUSIBLY DISTINCT` finite design/diagnostic package

Evidence in this pass:
- `45` same-amount opposite-verdict pairs,
- all `45/45` pairs separated by lift quantities (`CID` and `r_free^*` split).

## Candidate Formulation PFC-5: Model-Consistent Certified Architectures

Core statement:
A certified architecture for one target does not certify nearby mismatched targets unless compatibility is rechecked.

Assessment:
- mathematical status: `PROVED ON SUPPORTED FAMILY`
- novelty status: `KNOWN / REFRAMED` boundary law

Evidence:
- `50` model-mismatch failures; `49` with positive candidate-library defect.

## Candidate extraction verdict

Strongest positive extraction from current program:
1. compatibility-organized exactness criterion,
2. minimal free augmentation completion law,
3. constrained-library feasibility boundary (`delta_C`).

Interpretation:
This is not a universal positive theory. It is a branch-limited positive architecture package on finite linear mixed-observation systems.
