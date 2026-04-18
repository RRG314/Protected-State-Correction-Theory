# Bounded Versus Periodic Projection

This is the main scope-control file for the CFD branch.

The periodic branch has a clean exact projector structure. Bounded domains are different because boundary trace constraints become part of the protected class. A correction map that is exact for periodic divergence-free recovery can fail on bounded classes even when divergence is numerically small.

The branch now contains both sides: a narrow positive bounded-domain finite-mode Hodge theorem on a declared compatible family, and no-go results showing that divergence-only or naive periodic transplant architectures are insufficient for nontrivial bounded protected classes.

A representative no-go statement is that if recovery factors only through divergence, then distinct bounded protected states sharing divergence data cannot both be recovered exactly. This is a structural non-uniqueness statement, not a numerical artifact.

Current branch verdict is therefore split by architecture:
- periodic projector: exact on its declared class,
- bounded compatible finite-mode Hodge projector: exact on supported family,
- naive periodic reuse on bounded domains: rejected,
- divergence-only bounded recovery: no-go.
