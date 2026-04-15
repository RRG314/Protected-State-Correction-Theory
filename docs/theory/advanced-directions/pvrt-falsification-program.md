# PVRT Falsification Program

## Purpose

This file records how the repository is trying to kill or sharply restrict **Protected-Variable Recoverability Theory (PVRT)**.

The point is not to preserve the theory candidate at any cost.
The point is to keep only the form that survives repeated attempts to break it.

## 1. Broad Forms Already Attacked

### Claim A: Record amount alone determines recoverability
Status:
- false

How it was attacked:
- same-rank restricted-linear counterexample construction
- rank-lower-bound insufficiency tests
- periodic support-size stress sweeps
- diagonal support-size and polynomial-degree stress sweeps

What survived instead:
- alignment between record structure and protected-variable structure matters

### Claim B: One universal cross-domain threshold law exists
Status:
- unsupported

How it was attacked:
- periodic modal thresholds
- diagonal interpolation thresholds
- qubit phase-window family
- cross-branch comparison against exact projector and asymptotic branches

What survived instead:
- branch-specific threshold laws
- one restricted-linear threshold spine that explains several families but not all branches

### Claim C: `κ` alone already gives a major new theory
Status:
- unsupported in broad form

How it was attacked:
- searched for stronger general theorems beyond `κ(0)=0`
- searched for broad cross-domain threshold statements expressed only through `κ`
- compared `κ` behavior across analytic, qubit, periodic, and control cases

What survived instead:
- `κ(0)=0` exactness
- `κ(η)/2` lower bound
- exact-regime linear upper bound through a recovery operator
- collision-gap strengthening in the restricted-linear box family

## 2. Surviving Restricted Form

The surviving restricted form is:

> On finite-dimensional restricted linear families, protected-variable recoverability is governed by row-space compatibility, structured collision gaps, and minimal augmentation counts. Record amount alone is not enough.

This is the form that current proofs and tests support.

## 3. Falsification Protocol For The Surviving Form

### Step 1: alternative derivations
- kernel inclusion
- row-space inclusion
- nullspace collision construction
- explicit recovery-operator construction

### Step 2: alternative implementations
- direct linear-recovery construction
- pseudoinverse reconstruction
- exact nullspace-on-a-box collision gap evaluation
- finite-family sample collapse evaluation

### Step 3: edge and degenerate cases
- zero protected rank excluded
- exact identity records
- no-record / zero-record cases
- hidden protected directions
- one-dimensional nullspaces

### Step 4: parameter extremes
- larger box families
- repeated-cutoff periodic mode families
- diagonal families with more active modes
- exact versus barely-exact nested record levels

### Step 5: artifact cross-checking
- generated JSON compared to recomputed outputs
- workbench outputs compared to offline computations
- threshold figures compared to raw CSV values

## 4. Active Counterexample Targets

### Target 1: break the exact-regime upper envelope
Try to find an exact restricted-linear example where

```text
κ(δ) > ||K||_2 δ
```

for an exact recovery operator `K`.

Current result:
- no counterexample found
- generic exact linear and diagonal exact-history checks remain below the bound

### Target 2: break same-rank insufficiency
Try to find same-rank observation families on a restricted linear system where exactness is determined by rank alone.

Current result:
- no counterexample found
- explicit same-rank exact/fail constructions persist across multiple dimensions

### Target 3: break the row-space threshold law by admissible-family enlargement
Try to enlarge a restricted family so that row-space inclusion no longer predicts the exact threshold.

Current result:
- broad universal extension failed
- strongest surviving law remains explicitly restricted to finite-dimensional linear families

### Target 4: force a universal threshold story anyway
Try to unify periodic, diagonal, and qubit threshold behavior under one scalar law.

Current result:
- failed
- the periodic and diagonal families unify under the restricted-linear spine
- the qubit family remains a fiber-collision benchmark, not part of the same linear threshold theorem

## 5. What Counts As Failure

PVRT would need to be demoted further if any of the following occurred.

1. an exact restricted-linear counterexample to row-space inclusion exactness
2. a valid restricted-linear counterexample to the same-rank insufficiency theorem
3. a contradiction between generated artifacts and direct recomputation for the PVRT summary cases
4. a workbench verdict that disagrees with the underlying restricted-linear computation

## 6. What Counts As Strengthening

PVRT would become materially stronger if one of the following were proved.

1. a noisy extension of the exact-regime upper envelope and `κ(η)/2` lower bound on enlarged restricted families
2. a candidate-library or weighted-cost augmentation theorem extending `δ(O, L; F)`
3. a sharper structural theorem connecting `κ`, `Γ_r(B)`, and robust threshold behavior without collapsing into generic inverse-stability language

## 7. Current Honest Verdict

Broad PVRT did not survive.

Restricted PVRT did survive.

The current theory candidate is worth keeping because it now has:
- a real theorem spine,
- a real falsification record,
- useful negative results,
- family-level threshold laws,
- and tool integration.

It is **not** worth promoting as a universal new theory of observation or information.
