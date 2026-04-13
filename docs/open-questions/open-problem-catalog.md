# Open Problem Catalog

## OCP-OP1: Boundary-Sensitive Exact Continuous Correction
- Type: foundational
- Priority: high
- Current status: open
- Why it matters: this is the main obstacle to extending the strongest continuous exact anchor beyond the periodic setting.
- What is already known: periodic Helmholtz/Leray projection is exact in the tested branch.
- What blocks progress: boundary conditions and harmonic components make the decomposition more delicate.
- What might solve it: a careful Hodge-theoretic formulation tied to admissible boundary conditions.
- How to falsify weak versions: show a proposed exact projector fails to preserve the intended protected space once boundary modes are introduced.
- Recommendation: pursue, but keep the boundary assumptions explicit from the start.

## OCP-OP2: Mature Branch-Specific Capacity Theory
- Type: theorem-completion
- Priority: high
- Current status: open but viable
- Why it matters: the repo now has lower bounds and branch-specific capacity language, but not yet a finished theory.
- What is already known: exact rank lower bounds, sector distinguishability requirements, and stable-disturbance dimension summaries.
- What blocks progress: the branches encode correctability in genuinely different mathematical objects.
- What might solve it: a family of category-specific invariants rather than a forced universal scalar.
- How to falsify bad formulations: test whether they collapse distinct exact and asymptotic systems into the same number without preserving correctability information.
- Recommendation: strong next theorem-completion target.

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
