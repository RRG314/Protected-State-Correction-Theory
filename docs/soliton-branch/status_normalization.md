# Soliton Branch Status Normalization

Date: 2026-04-17

## Status Policy Used

- `PROVED`: complete mathematical statement proved on declared class.
- `CONDITIONAL`: mathematically plausible and strongly supported, but still depends on unclosed assumptions or finite-family scope.
- `VALIDATED`: reproducible computational evidence on declared tested families.
- `OPEN`: theorem or counterexample gap still unresolved.
- `DISPROVED`: proposed bridge/claim fails under explicit test.
- `ANALOGY ONLY`: conceptual parallel without theorem-grade support.

## Normalized Claim Set

| Claim | Normalized status | Scope statement |
| --- | --- | --- |
| Symmetry non-identifiability no-go | `PROVED` | For declared `G`-invariant observation class on the restricted one-soliton parameter manifold. |
| Restricted injectivity for selected observation families | `CONDITIONAL` + `VALIDATED` | Exhaustive finite-grid scans support injectivity on quotient for `local_complex_2` and `fourier_magnitudes_4`; continuous-space theorem still open. |
| Same-count opposite-verdict result | `VALIDATED` + `CONDITIONAL` | Proved on tested finite families (`obs_dim=4` witness); not yet promoted as a general continuous theorem. |
| Noise-aware ambiguity floor | `PROVED ON SUPPORTED FAMILY` + `CONDITIONAL` outside | Magnitude-only fixed-time class shows structural blindness; broader observation-family theorem remains open. |
| Projection/reduction preservation vs no-go | `VALIDATED` + `CONDITIONAL` | Lowpass/subsample split on declared NLS class; no universal projection theorem claimed. |
| Broad OCP bridge claims | Mixed: kept/rejected | Narrow recoverability and projection links kept; direct linear augmentation transfer is `DISPROVED`; broad unification is `ANALOGY ONLY`. |

## Promotion Guardrails

No claim above is promoted as a repo-wide theorem unless it is either:
1. proved on an explicit continuous class, or
2. explicitly marked as finite-family theorem with that scope in the statement.
