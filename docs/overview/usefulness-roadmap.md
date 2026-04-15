# Usefulness Roadmap

## Purpose

This roadmap audits the repository for practical usefulness rather than only theorem coverage.

## A. Immediate High-Value Improvements

1. keep the Recoverability / Correction Studio as the central decision surface
2. expose reusable templates that let users start from a known-good setup
3. route users by goal rather than only by theorem family
4. make branch outputs actionable: what failed, why, and what to add next
5. keep validation tied to generated artifacts so the tool layer cannot silently drift from the math

## B. Strongest Tool Directions

1. restricted-linear design reports
   - strongest current practical tool
   - gives sufficiency, ambiguity witnesses, and minimal augmentation suggestions
2. periodic cutoff / functional-support sweeps
   - useful whenever a protected variable depends on retained spectral support
3. finite-history versus observer routing
   - useful when users need to choose between exact static recovery and asymptotic recovery
4. no-go diagnosis from fiber collisions or hidden directions
   - useful because it stops wasted effort early

## C. Strongest Theorem / Result Directions

1. restricted-linear minimal-record theorems under admissible-family restriction
2. stronger robust results built on `κ(η)/2`
3. noise-aware or family-enlargement extensions of the minimal-complexity criterion
4. sharper weaker-versus-stronger protected-variable hierarchies under the same record

## D. Weak Or Dead-End Directions To Stop Spending Time On

1. universal scalar record-complexity claims
2. broad cross-domain phase-transition language without family qualifiers
3. any promotion of the qubit/control/periodic thresholds as one theorem without proof
4. analogy-only branches that do not produce operators, thresholds, lower bounds, or no-go results

## E. Product Direction

The highest-value practical identity is:

**Protected-State Correction Theory as a recoverability / correction design system**

That means the repository should help users:
- describe a protected variable
- check record sufficiency
- see what fails
- choose a recovery architecture
- decide what to add next
