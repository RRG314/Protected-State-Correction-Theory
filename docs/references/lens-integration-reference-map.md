# Lens Integration Reference Map (2026-04-16)

## Purpose

Map each promoted lens-integration component to:
- repo theorem/no-go artifacts,
- standard literature facts,
- repo framing of standard facts,
- and potential literature-distinct lanes.

Use with:
- `docs/references/protected-state-correction.bib`
- `docs/overview/proof-status-map.md`

## Branch-Level Reference Map

| Branch | Promoted lens payload | Standard literature anchors | Repo theorem/no-go anchors | Classification |
| --- | --- | --- | --- | --- |
| Exact finite-dimensional projection | operator factorization interpretation and projector algebra | `kato_1995` | `OCP-002`, `OCP-003`, `OCP-016` | standard fact with repo packaging |
| Exact sector/QEC | exact-sector criteria and overlap limits (no inverse/entropy inflation) | `knill_laflamme_1997`, `gottesman_1997`, `ahn_doherty_landahl_2002` | `OCP-005`, `OCP-019`, `OCP-021` | mostly literature-known, repo branch synthesis |
| Exact periodic Helmholtz/Leray | operator/FA exact projection anchor | `chorin_1968`, `brown_cortez_minion_2001`, `guermond_minev_shen_2006` | `OCP-006`, `OCP-027` | standard PDE projection facts in repo OCP framing |
| Bounded-domain/Hodge/CFD | boundary/topology obstruction + conditional exact subfamily | `arnold_falk_winther_2006`, `hatcher_2002`, `guermond_minev_shen_2006` | `OCP-023`, `OCP-028`, `OCP-029`, `OCP-044` | core math literature-known; repo obstruction/exactness packaging plausibly distinct |
| Maxwell/gauge projection | orbit/constraint projection interpretation | `berchenko_kogan_stern_2019`, `calabrese_2004` | `OCP-022` | standard physics/operator facts, repo corollary framing |
| Asymptotic generator branch | spectral/semigroup rate sharpening | `pazy_1983`, `engel_nagel_2000`, `davis_kahan_1970` | `OCP-013`, `OCP-014`, `OCP-015`, `OCP-020` | standard operator/semigroup facts with repo branch application |
| Constrained-observation recoverability | alignment/kernel invariant stronger than rank; factorization exactness | `davis_kahan_1970`, `bjorck_golub_1973`, `donoho_2006`, `candes_romberg_tao_2006` | `OCP-030` to `OCP-047` | mixture: standard algebraic core + repo theorem package likely distinct in scope/integration |
| Fiber/unified limits | anti-classifier, family-enlargement, mismatch instability, target hierarchy | `shannon_1948`, `hamming_1950`, `jencova_petz_2006`, `junge_renner_sutter_wilde_winter_2018`, `alberti_capdeboscq_privat_2020`, `villaverde_2019` | `OCP-048` to `OCP-053` | likely repo-distinct theorem package on restricted-linear class |

## Lens-by-Lens Reference Discipline

### Operator theory
- Standard facts: kernel/row-space equivalence, perturbation and spectral tools (`kato_1995`, `davis_kahan_1970`).
- Repo-specific contribution lane: anti-classifier and false-positive package interpreted through alignment/kernel invariants.

### Functional analysis
- Standard facts: semigroup decay, Hodge/decomposition background (`pazy_1983`, `engel_nagel_2000`, `arnold_falk_winther_2006`).
- Repo-specific contribution lane: bounded-domain obstruction/exactness packaging tied to OCP theorem/no-go structure.

### Geometry
- Standard facts: principal-angle computation and subspace geometry (`bjorck_golub_1973`).
- Repo use: supporting diagnostics for theorem-bearing operator claims.

### Inverse/identifiability language
- Use only where it adds stability or family-mismatch analysis (`alberti_capdeboscq_privat_2020`, `villaverde_2019`).
- Explicitly demoted on exact projector/QEC/exact Helmholtz anchors.

### Information theory
- Use only for secondary quantification (`shannon_1948`, `hamming_1950`).
- Exact branches should keep exact operator language.

## Repo-New vs Literature-Known Tracking

### Likely literature-known
- exact row-space/kernel criteria,
- standard semigroup/spectral stability implications,
- standard Hodge/topology background.

### Repo framing of standard facts
- cross-branch correction/recoverability language,
- bounded-domain obstruction translated into OCP no-go and conditional exactness gates.

### Plausibly literature-distinct lanes
- restricted-linear anti-classifier theorem package (`OCP-049` to `OCP-053`) as a coherent theorem-and-witness program,
- integrated theorem-to-workbench evidence architecture that preserves branch-level scope controls.

## Next Citation Tasks

1. Extend branch docs with explicit bib keys where lens language was promoted.
2. Keep novelty language tied to theorem IDs and generated witness artifacts.
3. Avoid citing secondary summaries where primary theorem/operator references are available.
