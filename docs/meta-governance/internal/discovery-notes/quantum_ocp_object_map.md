# Quantum-OCP Object Map

Status: falsification-first mapping from OCP/recoverability objects into standard quantum objects.

## Mapping Table

| OCP object | Quantum analog | Exact vs loose map | Already standard in quantum formalism? | Notes for this pass |
|---|---|---|---|---|
| target / protected variable `tau(x)` | quantity of interest on state family: expectation `Tr(rho O_tau)`, logical sector label, parameter `phi` | Exact in finite witness models | Yes | Used as target-specific recoverability variable throughout witness catalog. |
| record map `M` | measurement channel: projective basis, POVM statistics, syndrome extraction, reduced record | Exact | Yes | In this pass mostly projective/finite-record channels. |
| exact recoverability | existence of decoder from measurement record to target for all states in family | Exact | Yes (observability/identifiability/recovery language) | Implemented as finite collision test in `quantum_witness_catalog.csv`. |
| fiber / indistinguishability | measurement-equivalence classes: states with identical record distribution | Exact | Yes | Qubit fixed-basis phase-loss is the canonical fiber-collision witness (`QW001`). |
| impossibility no-go | nonexistence of decoder due collisions | Exact | Yes | Directly equivalent to state-discrimination impossibility under chosen measurement family. |
| conditioned vs invariant recoverability | per-context decoder exists, but no shared decoder across contexts | Exact for context-gain family | Close (calibration/context dependence) | Distinct packaging relative to standard basis language; see `QW005-QW008`. |
| shared augmentation threshold | minimal added shared measurement channel restoring invariant decoder | Exact in sampled families | Close prior art | Appears as one-added-basis and one-shared-channel restoration (`QW003/QW004`, `QW005-QW008`). |
| anti-classifier / amount-only insufficiency | same `(dim, count, budget)` but opposite target recoverability | Exact in finite witnesses | Close prior art | Seen in basis split and multipartite allocation split (`QA001`, `QA002`). |
| target-specific design failure | information-maximizing or naive criteria miss target-sensitive recoverability | Exact in finite design witnesses | Close prior art | Fisher-based split retained as conditional design lane (`QW019-QW024`). |
| context-sensitive recoverability | recoverability depends on context family geometry, not count only | Exact in witness class | Close prior art | Survives as scoped package, not universal theorem. |
| distributed/multipartite allocation | same total budget, different subsystem allocation, opposite verdict | Exact in witness class | Close prior art | `QW009/QW010` provides explicit two-qubit allocation split. |
| persistence/fragility under environment | decoherence changes accessible target structure | Exact in dephasing sweep | Yes | `QW011-QW017` shows target FI and exactness collapse at full dephasing. |
| QEC exact anchor | Knill-Laflamme sector recoverability | Exact | Yes | Included explicitly as known anchor (`QW018`), not novelty claim. |

## Exactness Boundary Used In This Pass

- Exact map: finite state family + finite measurement family + explicit decoder/collision criterion.
- Loose map: high-level interpretive parallels without decoder-level test.
- This pass keeps only decoder-level tested mappings in theorem/no-go candidate files.

## Main Mapping Outcome

The OCP-to-quantum map is strongest when interpreted as a **target-specific measurement recoverability framework** over finite families. It is weakest when treated as a claim of new quantum foundations.
