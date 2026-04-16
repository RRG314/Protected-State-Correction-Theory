# On the Failure of Rank-Based Criteria for Exact Recovery in Restricted Linear Observation Systems

Steven Reid  
Independent Researcher  
ORCID: 0009-0003-9132-3410  
sreid1118@gmail.com  
April 2026

## Abstract
We study exact recoverability of protected linear targets under restricted linear observation models and show that amount-only criteria fail sharply. In the finite-dimensional family `x=Fz`, with observation `y=OFz` and target `p(x)=LFz`, exact linear recovery is equivalent to `ker(OF) ⊆ ker(LF)` (equivalently `row(LF) ⊆ row(OF)`). We then prove anti-classifier results: equal observation rank can yield opposite exactness verdicts, and even equal fixed-library sensor count/budget can yield opposite exactness verdicts. We next give an exact minimal augmentation law, `δ(O,L;F)=rank([OF;LF]) - rank(OF)`, which is both necessary and sufficient for unrestricted added measurements to achieve exact recovery. The paper is intentionally scoped: claims are restricted-linear and do not assert universal observability laws.

**Keywords:** exact recoverability, observability, row-space criterion, rank insufficiency, sensor budget, minimal augmentation

## 1. Introduction
A common engineering shorthand treats “more sensors,” “higher rank,” or “larger budget” as reliable indicators of exact recovery capability. This paper formalizes where that intuition fails and what replaces it in a theorem-clean restricted linear class.

Our setting keeps model scope explicit. We do not claim a universal law over all inverse problems or all nonlinear systems. Instead, we show that in a precise finite-dimensional class, exact recoverability is controlled by structural alignment (kernel/row-space compatibility), not raw amount.

## 2. Setup
Let
- admissible family: `A = {x = Fz : z ∈ R^r}`,
- observation map: `M(x)=Ox`,
- protected target: `p(x)=Lx`.

Restricted matrices are
`O_F := OF`, `L_F := LF`.

A linear decoder `K` is **exact** on `A` if
`K O_F z = L_F z` for all `z`.

## 3. Main Theorems

### Theorem 3.1 (Restricted-linear exactness criterion)
Exact linear recovery exists iff

`ker(O_F) ⊆ ker(L_F)`.

Equivalent form:
`row(L_F) ⊆ row(O_F)`.

**Status:** `PROVED` (OCP-031).

#### Proof sketch
If exactness holds, then `O_F z=0 => K O_F z=0 = L_F z`, so kernel inclusion is necessary. Conversely, if kernel inclusion holds, each target row is a linear combination of observation rows, giving a decoder `K` with `K O_F = L_F`.

### Proposition 3.2 (Same-rank insufficiency)
There exist restricted-linear instances with identical `rank(O_F)` but opposite exactness verdicts.

**Status:** `PROVED` (OCP-047).

### Theorem 3.3 (No rank-only exact classifier)
No classifier depending only on ambient dimension and rank tuple can decide exact recoverability across all restricted-linear instances.

**Status:** `PROVED` (OCP-049).

### Theorem 3.4 (No fixed-library budget-only exact classifier)
Within a fixed candidate sensor library with equal per-sensor cost, equal sensor count/equal total budget can still produce opposite exactness verdicts.

**Status:** `PROVED` (OCP-050).

### Theorem 3.5 (Minimal augmentation law)
Define

`δ(O,L;F) = rank([O_F; L_F]) - rank(O_F)`.

Then `δ` is exactly the minimum number of unrestricted added scalar linear measurements required to make exact recovery possible.

**Status:** `PROVED` (OCP-045).

## 4. Explicit Examples

## 4.1 Exact case
Take
`F=I_2`,
`O=[1 0]`,
`L=[1 0]`.
Then `row(L_F)=row(O_F)`, so exactness holds with decoder `K=[1]`.

**Label:** `PROVED` (direct construction).

## 4.2 Failure case with same rank
Take
`F=I_2`,
`L=[1 0]`,
`O_1=[1 0]`, `O_2=[0 1]`.
Both have rank 1, but:
- `row(L_F) ⊆ row(O_1F)` so `O_1` is exact,
- `row(L_F) ⊄ row(O_2F)` so `O_2` is impossible.

**Label:** `PROVED` (same-rank opposite verdict witness).

## 4.3 Repaired case via one-step augmentation
From failure case `O_2=[0 1]`, compute

`δ = rank([O_2F; L_F]) - rank(O_2F) = rank([[0,1],[1,0]]) - 1 = 1`.

Add one measurement row `[1 0]`; augmented observation has full target row support and exactness is restored.

**Label:** `PROVED` (minimal augmentation theorem witness).

## 5. Why Amount Fails and Structure Survives
Amount-only summaries collapse distinctions between:
- where the observation nullspace lies, and
- whether that nullspace carries target variation.

Kernel and row-space alignment are therefore the mathematically relevant invariants in this class.

A practical corollary is immediate: sensor design should prioritize target-row coverage, not only count or rank.

## 6. Validation and Evidence Discipline
The paper uses theorem-first evidence for exact claims and benchmark checks for stress behavior.

- Theorems 3.1–3.5: `PROVED` in restricted-linear branch documents/tests.
- Stress sweeps and witness libraries: `VALIDATED` computational support for anti-classifier behavior and design-law reproducibility.

No validated-only result is upgraded to theorem language here.

## 7. Related Work Positioning
This paper sits near linear observability and sensor placement, but with a narrower objective: exact target recoverability on admissible restricted families.

Related lanes include functional observability and constrained sensor placement, where structural criteria and complexity barriers are central.

### 7.1 Position Relative to Existing Work
The linear kernel/row-space criterion is standard finite-dimensional linear algebra. The paper's distinct contribution is the scoped negative-and-design package: same-rank insufficiency, no rank-only and no fixed-budget-only exact classifiers, and an exact minimal augmentation law in one restricted-linear framework.

## 8. Limitations and Scope
1. Scope is restricted-linear (`x=Fz`) and finite-dimensional.
2. Nonlinear, stochastic, and PDE-wide universality is not claimed.
3. Budget theorem is fixed-library and equal-cost in the stated formulation.
4. The augmentation theorem is exact for unrestricted added linear measurements; constrained hardware catalogs may require additional combinatorial analysis.

## 9. Conclusion
Rank/count/budget language alone is insufficient for exact recoverability classification in the restricted-linear class. The replacement is a structural criterion (`ker(OF) ⊆ ker(LF)`) and its design consequence (exact minimal augmentation count `δ`). The main contribution is therefore not “more data helps,” but a theorem-clean statement of when structure, not amount, controls exactness.

## 10. Administrative Statements
### 10.1 Funding
This research received no external funding.

### 10.2 AI Usage Statement
AI-assisted tools were used for coding support, test scripting, and editorial drafting support. The theorem statements, proofs, examples, and final manuscript were manually checked and verified by the author.

### 10.3 Data and Code Availability
Primary repository for this paper: https://github.com/RRG314/Protected-State-Correction-Theory.  
Public workbench entrypoint: https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/

### 10.4 Conflict of Interest
The author declares no conflict of interest.

### 10.5 Reproducibility Note
The restricted-linear examples and anti-classifier witnesses are reproducible from the repository scripts and tests under `scripts/compare/` and `tests/math/`.

## 11. References
1. R. E. Kalman, “A new approach to linear filtering and prediction problems,” *Transactions of the ASME—Journal of Basic Engineering*, 82(1) (1960), 35–45. DOI: 10.1115/1.3662552.
2. C.-T. Lin, “Structural controllability,” *IEEE Transactions on Automatic Control*, 19(3) (1974), 201–208. DOI: 10.1109/TAC.1974.1100557.
3. A. J. Krener and R. Hermann, “Nonlinear controllability and observability,” *IEEE Transactions on Automatic Control*, 22(5) (1977), 728–740. DOI: 10.1109/TAC.1977.1101601.
4. Y. Zhang, T. Fernando, and M. Darouach, “Functional observability, structural functional observability and optimal sensor placement,” arXiv:2307.08923, 2023. URL: https://arxiv.org/abs/2307.08923.
5. P. Dey, N. Balachandran, and D. Chatterjee, “Efficient constrained sensor placement for observability of linear systems,” *IEEE Control Systems Letters*, 5(3) (2021), 927–932. Preprint: https://arxiv.org/abs/1711.08264.
6. E. J. Candès, J. Romberg, and T. Tao, “Robust uncertainty principles: Exact signal reconstruction from highly incomplete frequency information,” *IEEE Transactions on Information Theory*, 52(2) (2006), 489–509. DOI: 10.1109/TIT.2005.862083.
7. D. L. Donoho, “Compressed sensing,” *IEEE Transactions on Information Theory*, 52(4) (2006), 1289–1306. DOI: 10.1109/TIT.2006.871582.

## Appendix A. Repo Claim Mapping
- Theorem 3.1 maps to OCP-031.
- Proposition 3.2 maps to OCP-047.
- Theorem 3.3 maps to OCP-049.
- Theorem 3.4 maps to OCP-050.
- Theorem 3.5 maps to OCP-045.
