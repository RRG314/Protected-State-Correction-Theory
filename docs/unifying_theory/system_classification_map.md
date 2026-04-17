# System Classification Map

Date: 2026-04-17

## Classification Categories

| Class | Abstract Definition | Key Invariant / Obstruction | Example Branches |
|---|---|---|---|
| C-EXACT | `T` exactly recoverable/preserved on `A` under declared architecture | fiber constancy; compatibility satisfied | OCP projector (`OCP-002`), restricted-linear exact (`OCP-031`), MHD constant-`η` exact families |
| C-EXACT-MOD-SYM | exact recovery on quotient `A/~` but not full parameter state | symmetry quotient injectivity | soliton quotient lane (selected observation families) |
| C-ASYMPTOTIC | finite-time exactness absent but asymptotic suppression/recovery holds | generator spectral/stability structure | OCP generator branch (`OCP-013`,`014`,`020`) |
| C-DETECTABLE-NOT-EXACT | coarsened target exact while stronger target fails | target hierarchy / coarsening monotonicity | fiber target split (`OCP-048`), weaker-vs-stronger lanes |
| C-IMPOSSIBLE-COLLISION | collisions/overlap force impossibility | overlap/fiber collision | `OCP-003`, soliton symmetry non-identifiability |
| C-FALSE-POSITIVE-ENLARGEMENT | exact on `A_s` but fails on `A_l` with `A_s ⊂ A_l` | family-enlargement fragility | `OCP-052`; restricted soliton class broadening warnings |
| C-MISMATCH-UNSTABLE | decoder exact on model family but unstable on true family | model-mismatch error floor | `OCP-053`; conditional analogues in soliton scans |
| C-ARCH-MISMATCH | architecture removes one residual but misses protected structure constraints | boundary/topology incompatibility | bounded-domain transplant failure (`OCP-023`,`028`), MHD axis-vs-annular exclusions |
| C-RESTRICTED-EXACT-BY-DOMAIN | exactness survives on explicitly compatible subfamilies only | domain-compatible operator and regularity assumptions | finite-mode bounded Hodge exactness (`OCP-044`), MHD annular survivor classes |
| C-ENGINEERING-VALIDATED | theorem-linked but operational workflow result | reproducible diagnostics and benchmarks | Structural Discovery Studio / Discovery Mixer |
| C-ANALOGY-ONLY | conceptual similarity without theorem-grade transfer | missing explicit map/proof/witness package | broad OCP-self-organization equivalence, universal two-reservoir claims |

## Placement Rules

A system is placed by the first satisfied strongest class:

1. Check exactness (or quotient exactness).
2. If not exact, test asymptotic and detectable-only tiers.
3. If failure persists, identify collision/overlap vs architecture mismatch vs mismatch/family fragility.
4. Tag branch evidence level (`PROVED`, `PROVED ON SUPPORTED FAMILY`, `CONDITIONAL`, `VALIDATED`).
5. If only conceptual mapping exists, force `ANALOGY ONLY`.

## Practical Mapping Across In-Scope Programs

- **OCP core/recoverability:** occupies C-EXACT, C-ASYMPTOTIC, C-DETECTABLE-NOT-EXACT, C-IMPOSSIBLE-COLLISION, C-FALSE-POSITIVE-ENLARGEMENT, C-MISMATCH-UNSTABLE.
- **Soliton lane:** occupies C-EXACT-MOD-SYM, C-IMPOSSIBLE-COLLISION, C-FALSE-POSITIVE-ENLARGEMENT (conditional), C-MISMATCH-UNSTABLE (conditional), C-ARCH-MISMATCH (projection splits).
- **MHD closure lane:** occupies C-EXACT, C-ARCH-MISMATCH, C-RESTRICTED-EXACT-BY-DOMAIN.
- **SDS layers:** primarily C-ENGINEERING-VALIDATED; theorem claims remain inherited from source branches rather than promoted as independent math.
