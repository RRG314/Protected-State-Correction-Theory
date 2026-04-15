# Usefulness By Branch

## Purpose

This note records what each branch lets a user or researcher actually do.

## Exact Branch

What it helps with:
- certify when an orthogonal correction architecture is exact
- diagnose overlap-based impossibility early

Best outputs:
- direct projector construction
- exact/no-go diagnosis

## Exact Sector / QEC Branch

What it helps with:
- understand when sector-conditioned recovery is exact
- diagnose sector ambiguity or overlap failure

Best outputs:
- exact recovery operator on sector families
- overlap-based no-go diagnosis

## Exact Continuous Projection / CFD Branch

What it helps with:
- decide whether a projection-based correction operator is exact for the actual protected class
- distinguish correct bounded-domain Hodge correction from bad transplants

Best outputs:
- projector choice and compatibility diagnosis
- boundary-sensitive exactness checks

## Asymptotic Generator Branch

What it helps with:
- decide when to use damping/observer-style correction instead of exact projection
- diagnose whether mixing destroys protected-state preservation

Best outputs:
- invariant-split or mixing diagnosis
- asymptotic-versus-exact architecture choice

## GLM / Constraint-Damping Branch

What it helps with:
- use asymptotic cleaning honestly as a comparator
- avoid mislabeling damping schemes as exact correction

Best outputs:
- asymptotic fit classification
- residual-decay comparator against projector-based exact correction

## Constrained-Observation Recoverability Branch

What it helps with:
- tell whether a record is sufficient before building a correction architecture
- identify exact, approximate, asymptotic, and impossible recovery regimes
- show when weaker protected variables remain recoverable under the same record
- falsify the claim that record amount alone determines exact recoverability

Best outputs:
- collision-gap and collapse diagnostics
- exact/no-go threshold reports
- restricted PVRT theorem-backed criteria in the finite-dimensional linear lane
- weaker-versus-stronger protected-variable comparisons

## Restricted-Linear / Design-Engine Layer

What it helps with:
- tell what extra measurements are needed
- tell the minimum unrestricted measurement count needed for exact recovery
- search candidate measurement sets

Best outputs:
- minimal augmentation counts
- candidate measurement suggestions
- nullspace witnesses and insufficiency diagnoses
- exact-regime upper-bound estimates when the restricted family is already exact

## Practical Workbench / Studio Layer

What it helps with:
- route users by goal instead of by theorem name
- make decisions about measurements, protected variables, and architectures

Best outputs:
- solvable / approximate / asymptotic / impossible classification
- next-step suggestions grounded in the design and no-go layers

## App / Engine-Facing Use

The strongest justified app-facing use is now a recoverability engine:
- define the protected state or functional that really matters
- define the coarse record actually available
- check whether it is enough
- identify what weaker target is still recoverable
- identify what extra state or measurement is needed
- route to exact projector, exact recovery, or asymptotic observer design

That is a real use even when the underlying math is standard-adjacent, because it turns theory into decisions.
