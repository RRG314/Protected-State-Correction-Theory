# Final Theorem Spine

This is the canonical positive theorem spine. It lists what is promoted as stable theorem content and clarifies how each block contributes to the larger program.

## 1. Exact anchors

The exact anchor block establishes when one-step correction is possible under explicit structural assumptions.

- `OCP-002 (OCP-T1)`: exact orthogonal projection recovery.
- `OCP-019 (OCP-T5)`: exact sector recovery under orthogonality/distinguishability assumptions.
- `OCP-016 (OCP-T4)`: rank lower bound for exact linear correction.

These results are the finite-dimensional backbone.

## 2. Asymptotic generator block

This block describes the strongest continuous-time positive results that survive the no-go layer.

- `OCP-013 (OCP-T3)`: invariant-split generator theorem.
- `OCP-014 (OCP-C2)`: self-adjoint PSD corollary with explicit decay control.
- `OCP-004 (OCP-T2)`: basic continuous damping bridge.

Together they define the repository’s exact-to-asymptotic transition logic.

## 3. Bounded-domain restricted exactness

- `OCP-044 (OCP-T7)`: boundary-compatible finite-mode Hodge projection (`PROVED ON SUPPORTED FAMILY`).

This result is intentionally narrow and should be read as a solved subcase, not as a general bounded-domain closure.

## 4. Restricted-linear recoverability block

This block is the program’s main theorem-to-design lane under constrained observation.

- `OCP-030`: observation-fiber exactness.
- `OCP-031`: restricted-linear kernel/row-space exactness criterion.
- `OCP-043`: collision-gap threshold law.
- `OCP-045`: minimal augmentation theorem.
- `OCP-046`: exact-regime stability envelope.

## 5. Fiber-level positive hierarchy

- `OCP-048`: detectable-only through target coarsening.

This theorem is the clean positive anchor for target hierarchy without overpromoting universal recoverability laws.

## 6. Descriptor-fiber quantitative layer

On supported finite witness classes, the descriptor-fiber layer provides a purity criterion and an irreducible descriptor-only error lower bound, with computed `DFMI` / `IDELB` / `CL` diagnostics. This block remains explicitly branch-limited.

## Non-promoted positive claims

Not promoted as theorem-spine content:

- universal scalar capacity laws,
- universal rank/count/budget exactness classifiers,
- universal bounded-domain exactness beyond supported families,
- universal cross-branch unification statements.

## Reading note

Use this spine together with `docs/finalization/no-go-spine-final.md`; the program’s reliability depends on reading positive and negative structure together.
