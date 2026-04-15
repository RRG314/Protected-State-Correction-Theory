# Open Problem Catalog

## OCP-OP6: Robust Restricted PVRT Beyond Zero-Noise Exactness
- Type: theorem-completion
- Priority: high
- Current status: open but newly sharpened
- Why it matters: the constrained-observation branch now supports a restricted Protected-Variable Recoverability Theory spine, but its strongest theorems still live mainly in zero-noise finite-dimensional linear settings.
- What is already known: fiber-separation exactness, `κ(0)=0`, the adversarial lower bound `κ(η)/2`, the exact-regime upper envelope `κ(δ) ≤ ||K||_2 δ`, the nested restricted-linear collision-gap threshold law, the same-rank insufficiency theorem, and the minimal augmentation invariant `δ(O, L; F)`.
- What blocks progress: broad noisy extensions can collapse into standard conditioning language unless the admissible family, protected map, and record perturbation model remain explicit.
- What might solve it: a theorem that preserves the collision-gap and augmentation logic under bounded record noise or controlled admissible-family enlargement.
- How to falsify bad formulations: produce same-rank or same-size record families with opposite robust behavior, or show that a proposed noisy theorem reduces to a vacuous norm inequality with no recoverability content.
- Recommendation: this is now the strongest next theorem direction in the constrained-observation lane and the strongest current candidate for turning that branch into a more serious theory program.

## OCP-OP1: Boundary-Sensitive Exact Continuous Correction
- Type: foundational
- Priority: high
- Current status: partially resolved, still open
- Why it matters: this is the main obstacle to extending the strongest continuous exact anchor beyond the periodic setting.
- What is already known: periodic Helmholtz/Leray projection is exact in the tested branch; the repository now also proves a bounded-domain exact result on an explicit boundary-compatible finite-mode Hodge family.
- What blocks progress: general bounded domains, harmonic components, discretization choices, and realistic boundary data make the decomposition more delicate.
- What might solve it: a careful Hodge-theoretic formulation tied to admissible boundary conditions and to the actual discrete operator used by the solver.
- How to falsify weak versions: show a proposed exact projector fails to preserve the intended protected space once boundary modes are introduced.
- Recommendation: pursue the general bounded-domain theorem, but keep the already-solved finite-mode boundary-compatible subcase separate.

## OCP-OP2: Mature Branch-Specific Capacity Theory
- Type: theorem-completion
- Priority: high
- Current status: partially resolved, still open
- Why it matters: the repo now has lower bounds and branch-specific capacity language, but not yet a finished theory.
- What is already known: exact rank lower bounds, sector distinguishability requirements, stable-disturbance dimension summaries, and now a proved restricted-linear minimal-augmentation invariant `δ(O, L; F)`.
- What blocks progress: the branches encode correctability in genuinely different mathematical objects, so the mature theory must remain category-specific.
- What might solve it: a family of category-specific invariants rather than a forced universal scalar, with the restricted-linear deficiency theorem as the first finished member of that family.
- How to falsify bad formulations: test whether they collapse distinct exact and asymptotic systems into the same number without preserving correctability information.
- Recommendation: keep extending the category-specific route; do not revive universal scalar language.

## OCP-OP3: Sector Branch Beyond The 3-Qubit Anchor
- Type: theorem-completion
- Priority: medium-high
- Current status: open but promising
- Why it matters: the new exact sector theorem is real, but the repo still leans heavily on the bit-flip anchor.
- What is already known: orthogonal sector embeddings admit exact recovery; sector overlap kills unique detection.
- What blocks progress: identifying the right next exact sector system that adds theory rather than just another example.
- What might solve it: one carefully chosen stabilizer or classical coding example with a genuinely cleaner operator statement.
- How to falsify weak versions: avoid examples that merely restate the same basis-level construction without improving the theorem program.
- Recommendation: one more anchor is enough if it sharpens the formalism.

## OCP-OP4: Control / Observer Completion Beyond Invariant Splits
- Type: application-facing
- Priority: medium
- Current status: conditional
- Why it matters: this is the main route toward engineering relevance outside QEC and PDE projection.
- What is already known: invariant-split linear systems fit the asymptotic branch.
- What blocks progress: real feedback systems often mix coordinates or only approximately preserve the protected object.
- What might solve it: a careful theorem with explicit separation assumptions and robustness bounds.
- How to falsify weak versions: show protected drift or mixing under coordinate changes.
- Recommendation: viable, but do not promote beyond conditional design rules yet.

## OCP-OP5: Continuous Measurement / Reset Branch
- Type: speculative but promising
- Priority: medium-low
- Current status: open
- Why it matters: OCP-N7 strongly suggests that exact finite-time correction in the continuous branch requires non-flow structure.
- What is already known: smooth linear semigroups are asymptotic only.
- What blocks progress: the repo does not yet formalize a hybrid continuous-measurement/reset architecture.
- What might solve it: a piecewise or event-triggered operator model.
- How to falsify bad versions: rule out constructions that are still just smooth semigroups in disguise.
- Recommendation: only pursue after the boundary-sensitive and capacity directions are stronger.
