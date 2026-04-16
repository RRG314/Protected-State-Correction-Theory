# Exact Closure and Obstruction in Euler-Potential MHD Under Variable Resistivity

Steven Reid  
Independent Researcher  
ORCID: 0009-0003-9132-3410  
sreid1118@gmail.com  
April 2026

## Abstract
We study closure for resistive MHD written in Euler potentials `B = ∇α × ∇β`, with emphasis on exactness versus obstruction under variable resistivity. The paper upgrades the 2025 draft by tightening scope to theorem-supported cylindrical families, making domain assumptions explicit, and separating proved exact identities from validated asymptotic evidence. In constant resistivity, we keep a complete exact/conditional cylindrical classification for supported ansätze; in variable resistivity we prove a sharp obstruction layer with restricted annular survivors and no nonconstant smooth axis-touching survivors in the supported radial classes. We then add a new mixed reduced-MHD/tokamak-adjacent lane `β = z + q(r)θ`, proving a factorization criterion for constant resistivity and a restricted exact annular ODE for variable resistivity. A perturbative layer provides first-order defect formulas, and a sheet-profile benchmark validates `max|R| ~ ε/δ` localization scaling. We state precisely what is proved, what is validated, and what remains open.

**Keywords:** Euler potentials, resistive MHD, closure remainder, variable resistivity, cylindrical coordinates, annular domains, Helmholtz-Hodge structure

## 1. Introduction
The Euler-potential representation `B = ∇α × ∇β` preserves `∇·B = 0` structurally, but resistive evolution introduces a closure mismatch: naively diffusing `α` and `β` does not generically reproduce resistive diffusion of `B`. The central object is therefore the closure remainder `R`, and exact closure means solving a first-order correction equation that reproduces `R` exactly.

Relative to the 2025 draft, this upgrade enforces four corrections.

1. Coordinate scope is narrowed to currently supported cylindrical families.
2. Domain class is explicit (axis-touching versus annular).
3. Variable-resistivity survivors are separated from smooth exact families.
4. Symbolic verification is used as evidence, not as a substitute for theorem statements.

## 2. Setup and Closure Remainder
Let `(r,θ,z)` denote cylindrical coordinates, with physical-component operators used consistently.

Define:
- magnetic field: `B(α,β) = ∇α × ∇β`,
- naive source term: `N(α,β;η) = ∇(ηΔα) × ∇β + ∇α × ∇(ηΔβ)`,
- true resistive term:
  - constant `η`: `T = η Δ_vec B`,
  - variable `η(r)`: `T = η Δ_vec B + ∇η × (∇×B)`.

The closure remainder is

`R = T - N`.

Exact closure in this paper means: there exist scalar correction sources `(S_α,S_β)` such that

`∇S_α × ∇β + ∇α × ∇S_β = R`.

### Domain classes used throughout
- **Axis-touching smooth domain:** includes `r=0` and requires smooth non-singular profiles there.
- **Annular domain:** `r ∈ [r_min, r_max]` with `r_min > 0`; singular-at-axis formulas can still be admissible.

## 3. Constant-Resistivity Exact Classification

### Theorem 3.1 (Radial-`rθ` exactness)
For constant `η`, the family
`α=f(r), β=rθ`
is exactly closed for smooth `f` in the supported cylindrical framework.

**Status:** `PROVED`  
**Evidence:** direct derivation + symbolic checks (MHD-T1).

### Theorem 3.2 (Radial-`z` exactness)
For constant `η`,
`α=f(r), β=z`
is exactly closed for smooth `f`.

**Status:** `PROVED`  
**Evidence:** direct derivation + symbolic checks (MHD-T2).

### Theorem 3.3 (`rθ`-`g(z)` exactness)
For constant `η`,
`α=rθ, β=g(z)`
is exactly closed for smooth `g`.

**Status:** `PROVED`  
**Evidence:** derivation + symbolic checks (MHD-T3).

### Theorem 3.4 (Conditional radial-`θ` exactness)
For constant `η`,
`α=f(r), β=θ`
is exact iff
`f(r)=a r^2 + b`.

**Status:** `PROVED`  
**Evidence:** exact residual factorization (MHD-T4).

### Proposition 3.5 (Infinite exact-family cardinality in constant resistivity)
In the supported constant-`η` cylindrical lanes, exact closure is not isolated: each lane contains infinitely many exact ansätze (for example, arbitrary smooth `f` in Theorems 3.1 and 3.2, arbitrary smooth `g` in Theorem 3.3).

**Status:** `PROVED`  
**Evidence:** direct family parameter freedom in Theorems 3.1–3.3.

## 4. Variable-Resistivity Obstruction and Restricted Survivors

### Theorem 4.1 (Radial-`rθ` obstruction with annular survivor)
For nonconstant `η(r)`, exactness in
`α=f(r), β=rθ`
forces an ODE yielding the nontrivial annular survivor
`f(r)=a√r+b`.
In axis-touching smooth domains, only trivial constants survive.

**Status:** `PROVED` on the supported family  
**Evidence:** explicit residual + solved ODE (MHD-O1).

### Theorem 4.2 (Radial-`z` obstruction with annular survivor)
For nonconstant `η(r)`, exactness in
`α=f(r), β=z`
forces the logarithmic annular branch
`f(r)=a log r + b`;
axis-touching smooth nonconstant survivors are excluded in the supported family.

**Status:** `PROVED` on the supported family  
**Evidence:** explicit residual + solved ODE (MHD-O2).

### Theorem 4.3 (`rθ`-`g(z)` trivial-survivor theorem)
For nonconstant `η(r)` nonzero on an interval,
`α=rθ, β=g(z)`
has only trivial constant-`g` exact survivors.

**Status:** `PROVED`  
**Evidence:** residual structure and symbolic verification (MHD-O3).

### Corollary 4.4 (No-smooth-axis nonconstant survivor theorem on supported radial classes)
For the supported radial families in Sections 4.1 and 4.2 with nonconstant `η(r)`, nonconstant exact survivors are annular-only; there is no nonconstant smooth axis-touching survivor.

**Status:** `PROVED`  
**Evidence:** Theorems 4.1 and 4.2 (axis regularity exclusions).

Figure 1 compares `|R(r)|` for constant and variable resistivity in a common mixed-lane formula. Figure 2 shows the near-axis singular behavior that motivates the axis-touching versus annular distinction.

![Figure 1. Closure-defect magnitude `|R(r)|` for constant `η` and variable `η=r^2` in the mixed-lane remainder formula.](../figures/mhd/mhd_remainder_constant_vs_variable_eta.png)

Figure 1. Closure-defect magnitude `|R(r)|` for constant `η` and variable `η=r^2` in the mixed-lane remainder formula.

![Figure 2. Near-axis singular behavior of `|R(r)|` on log-log axes for representative resistivity profiles.](../figures/mhd/mhd_singularity_near_axis.png)

Figure 2. Near-axis singular behavior of `|R(r)|` on log-log axes for representative resistivity profiles.

## 5. Mixed Tokamak / Reduced-MHD-Adjacent Lane
We consider
`α=f(r), β=z+q(r)θ`.
This lane is mathematically motivated by safety-factor-like shear profiles while remaining fully explicit in the current closure framework.

### Theorem 5.1 (Constant-`η` mixed factorization law)
For constant `η`, the `z`-component of the remainder factorizes as

`R_z = (2η/r^3) (r f'' - f')(r q' - q)`,

with `R_r = R_θ = 0`.
Hence exactness is equivalent to
`(r f'' - f')(r q' - q)=0`, i.e.
- branch A: `f(r)=a r^2+b` with arbitrary `q(r)`, or
- branch B: `q(r)=c r` with arbitrary `f(r)`.

**Status:** `PROVED` (MHD-XT1).

### Theorem 5.2 (Variable-`η` annular mixed branch)
For variable `η(r)`, restricting to `f(r)=a log r+b` yields exactness iff

`(r^2 η' + 4rη) q' = (2rη' + 4η) q`.

For power law `η(r)=r^m`, one exact branch is
`q(r)=C r^((2m+4)/(m+4))`.

**Status:** `PROVED (restricted annular)` (MHD-XT2).

### Proposition 5.3 (Local toroidal shear obstruction term)
For `q(r)=q0+κr` in the same annular branch,

`R_z = a(κ r^2 η' + 2 q0 r η' + 4 q0 η)/r^4`.

This isolates curvature/shear and coefficient-gradient coupling in a closed form.

**Status:** `PROVED (local)` (MHD-XG1).

### 5.4 Tokamak-claim scope discipline
The mixed lane is mathematically tokamak-adjacent through shear-profile structure (`q(r)`), but this paper does **not** claim full tokamak equilibrium closure or global toroidal classification.

**Status:** `INTERPRETATION`  
**Scope note:** results in Section 5 are exact only for the declared cylindrical/annular ansätze.

## 6. Perturbative and Asymptotic Defect Layer

### Theorem 6.1 (First-order `η`-perturbation formula)
Around exact base `α=a r^2+b`, `β=z+q(r)θ`, `η=η0+εη1(r)`,

`[R]_ε = (0, 8aη1'(r), -2a(rq'(r)+2q(r))η1'(r)/r)`.

**Status:** `PROVED` (MHD-XP1).

### Theorem 6.2 (First-order `α`-perturbation formula)
Around exact base `α=a r^2+b+εh(r)`, `β=z+q0θ`, constant `η`,

`[R]_ε = (0,0,2ηq0(-r h'' + h')/r^3)`.

**Status:** `PROVED` (MHD-XP1 lane, alpha-perturbation component).

### Benchmark 6.3 (Sheet-thinning defect localization)
For
`η(r)=η0+ε tanh((r-r0)/δ)`,
`α=a log r`, `β=z+(q0+κr)θ`,
benchmarks show
- `max|R|` scales approximately as `ε/δ`,
- localization ratio near the sheet grows strongly as `δ` decreases,
- normalized quantity `max|R| δ / ε` remains near constant over tested `δ`.

**Status:** `VALIDATED` (MHD-XP2), not a universal theorem.

Figure 3 gives the computed sheet-thinning benchmark in the gradient-dominated lane: maxima increase with `1/δ`, and the normalized trend `max|R|·δ/ε` remains comparatively stable across the tested `δ` values.

![Figure 3. Sheet-thinning defect scaling benchmark: `max|R|` versus `1/δ` and normalized scaling check.](../figures/mhd/mhd_sheet_thinning_scaling.png)

Figure 3. Sheet-thinning defect scaling benchmark: `max|R|` versus `1/δ` and normalized scaling check.

## 7. Consolidated Classification Table

| Lane | Constant `η` | Variable `η(r)` | Domain sensitivity | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| `α=f(r), β=rθ` | exact for smooth `f` | nontrivial exact survivor `f=a√r+b` annular-only | axis-touching smooth nonconstant excluded | `PROVED` | residual factorization + ODE |
| `α=f(r), β=z` | exact for smooth `f` | nontrivial exact survivor `f=a log r+b` annular-only | axis-touching smooth nonconstant excluded | `PROVED` | residual factorization + ODE |
| `α=rθ, β=g(z)` | exact for smooth `g` | only constant `g` exact | no nontrivial survivor on supported family | `PROVED` | residual structure |
| mixed `α=f(r), β=z+q(r)θ` | factorization law with two exact branches | restricted annular exact ODE (`XT2`) | annular restriction is essential | `PROVED (restricted)` | exact derivation |
| sheet-profile asymptotic defect scaling | n/a | `max|R| ~ ε/δ` trend on tested family | profile-dependent | `VALIDATED` | reproducible benchmark |
| full toroidal/global class | open | open | global geometry unresolved | `OPEN` | not solved |

Figure 4 quantifies axis sensitivity of annular survivor profiles through a regularity proxy `||f'(r)||_{L2([r_min,1])}`: the axis-touching limit is singular, while fixed annular cutoffs remain finite.

![Figure 4. Axis-touching versus annular behavior measured by derivative-norm growth as inner radius `r_min` decreases.](../figures/mhd/mhd_axis_vs_annular_behavior.png)

Figure 4. Axis-touching versus annular behavior measured by derivative-norm growth as inner radius `r_min` decreases.

## 8. Status-Separated Claims

### 8.1 `PROVED`
- Constant-`η` exact cylindrical families (Theorems 3.1–3.4).
- Infinite exact-family cardinality in constant `η` supported lanes (Proposition 3.5).
- Variable-`η` obstruction with annular survivors (Theorems 4.1–4.3).
- No-smooth-axis nonconstant survivor theorem on supported radial classes (Corollary 4.4).
- Mixed-lane factorization and restricted variable-`η` annular law (Theorems 5.1–5.2; Proposition 5.3).
- First-order perturbative defect formulas (Theorems 6.1–6.2).

### 8.2 `VALIDATED`
- Sheet-thinning defect localization/scaling benchmark (Benchmark 6.3).

### 8.3 `INTERPRETATION`
- Tokamak/reduced-MHD adjacency as motivation for the mixed lane (Section 5.4), without a full toroidal-physics claim.

## 9. Interpretation

### 9.1 What this paper now supports
- Exact closure survives in explicit structured families.
- Variable resistivity introduces a real structural obstruction, not only a small perturbation.
- Domain class is decisive: annular exact survivors do not imply smooth axis-touching exactness.
- A limited mixed tokamak-adjacent lane is theorem-viable in restricted form.

### 9.2 What this paper does **not** claim
- No full tokamak/toroidal closure classification.
- No universal reconnection theorem from remainder structure alone.
- No statement that symbolic checks replace closed-form arguments.

### 9.3 Position Relative to Existing Work
Classical MHD literature and Euler-potential discussions already establish the broad modeling context. The contribution of this paper is narrower: a theorem-labeled closure/obstruction classification on explicit cylindrical families, with explicit annular-versus-axis scope control and a status-separated perturbative/benchmark layer. The paper does not claim a complete toroidal or reconnection theory.

## 10. Limitations and Scope
1. Main proofs are cylindrical-family restricted.
2. Annular survivor theorems do not transfer automatically to axis-touching smooth domains.
3. Dynamic PDE evolution beyond static closure remainder structure remains mostly open.
4. Asymptotic sheet scaling is benchmark-validated, not universal.

## 11. Conclusion
This upgraded paper replaces broad language with a sharper theorem/no-go package: exact constant-resistivity cylindrical anchors, explicit variable-resistivity obstruction with restricted annular survivors, a new mixed reduced-MHD/tokamak-adjacent theorem lane, and a perturbative/asymptotic defect layer with clear status labels. The next mathematically serious step is to extend restricted local/toroidal obstructions and higher-order perturbative correction theory without relaxing scope discipline.

## 12. Administrative Statements
### 12.1 Funding
This research received no external funding.

### 12.2 AI Usage Statement
AI-assisted tools were used for symbolic-code scaffolding, figure scripting, and editorial drafting support. All mathematical claims, derivations, and final manuscript text were manually verified by the author.

### 12.3 Data and Code Availability
Primary MHD repository: https://github.com/RRG314/MagnetoHydroDynamic-research.  
This finalized paper version, cross-paper synchronization notes, and companion figure scripts are also tracked in the OCP companion repository: https://github.com/RRG314/Protected-State-Correction-Theory.

### 12.4 Conflict of Interest
The author declares no conflict of interest.

### 12.5 Reproducibility Note
Figures in this manuscript are generated and checked via:
- `python scripts/figures/generate_publication_figures.py`
- `python scripts/figures/validate_publication_figures.py`
The metrics and validation outputs are stored under `data/generated/figures/`.

## 13. References
1. P. A. Davidson, *An Introduction to Magnetohydrodynamics*, Cambridge University Press, Cambridge, 2001.
2. D. Biskamp, *Magnetohydrodynamic Turbulence*, Cambridge University Press, Cambridge, 2003.
3. A. Brandenburg, “Magnetic field evolution in simulations with Euler potentials,” *Monthly Notices of the Royal Astronomical Society*, 401(1) (2010), 347–358. DOI: 10.1111/j.1365-2966.2009.15500.x.
4. A. Dedner, F. Kemm, D. Kröner, C.-D. Munz, T. Schnitzer, and M. Wesenberg, “Hyperbolic divergence cleaning for the MHD equations,” *Journal of Computational Physics*, 175(2) (2002), 645–673. DOI: 10.1006/jcph.2001.6961.
5. E. R. Priest and T. G. Forbes, *Magnetic Reconnection: MHD Theory and Applications*, Cambridge University Press, Cambridge, 2000.
6. J. P. Goedbloed, R. Keppens, and S. Poedts, *Magnetohydrodynamics of Laboratory and Astrophysical Plasmas*, Cambridge University Press, Cambridge, 2019.

## 14. Appendix A. Status Labels Used
- `PROVED`: exact mathematical statement supported by derivation/proof.
- `VALIDATED`: reproducible computational evidence on declared families.
- `CONDITIONAL`: mathematically sound under explicit additional assumptions.
- `OPEN`: unresolved in current repo theorem spine.
- `INTERPRETATION`: explanatory framing not promoted as theorem.
