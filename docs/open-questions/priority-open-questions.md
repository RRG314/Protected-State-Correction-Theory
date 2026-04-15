# Priority Open Questions

## 1. Robust Restricted PVRT

Can the constrained-observation branch be extended from zero-noise exact restricted-linear recovery to a genuinely robust theorem that survives record noise or admissible-family enlargement?

Current status:
- the branch now has a real restricted PVRT spine
- the exact-regime upper envelope and same-rank insufficiency theorem survived repeated falsification
- the open part is the robust extension beyond zero-noise exactness

## 2. Generator Characterization Beyond Projectors

Can the asymptotic branch be extended from `K = k P_D` to a broader class of generators with:
- `ker(K)=S`,
- no corruption of `S`,
- and contractive behavior on the disturbance family?

This remains one of the strongest exact-to-asymptotic theorem directions outside the observation branch.

## 3. Sector-Based Theorem Program Beyond QEC

Can the sector-based correction picture used in QEC be formulated abstractly enough to include non-quantum correction systems without becoming empty language?

## 4. Boundary-Sensitive Continuous OCP

How much of the exact Helmholtz projection story survives on nonperiodic domains, bounded domains, or more realistic numerical boundary treatments?

Current status:
- one restricted bounded-domain exact theorem now survives on the repository's boundary-compatible finite-mode Hodge family
- the open part is the broader theorem tied to realistic domain-compatible projectors

## 5. Nonlinear Or Manifold-Valued Protected Sets

Can OCP be extended from linear subspaces to invariant manifolds or nonlinear constraint sets without losing operator-level meaning?

## 6. Category-Specific Correction Capacity

Even if one universal scalar fails, can each branch support a rigorous capacity notion that is genuinely useful?

Current status:
- the restricted-linear branch now has one finished capacity invariant, the minimal augmentation deficiency `δ(O, L; F)`
- the open part is maturing comparable invariants on the other branches without forcing false unification

## 7. Stronger No-Go Results

Can we prove sharper statements about when insufficient detectability or insufficient correction image forces failure in continuous systems or observer/controller settings?

## 8. Practical PDE Design Rules

Can OCP produce concrete criteria for choosing between projection cleaning, damping-based cleaning, or mixed architectures in real numerical solvers?
