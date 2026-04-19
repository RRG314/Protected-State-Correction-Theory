# Quantum-OCP Overlap Table

Status labels used: `ALREADY KNOWN IN SUBSTANCE`, `CLOSE PRIOR ART / REPACKAGED`, `PLAUSIBLY DISTINCT`, `ANALOGY ONLY`, `CONDITIONAL`, `PROVED ON SUPPORTED FAMILY`, `VALIDATED / EMPIRICAL ONLY`, `DISPROVED / COLLAPSED`.

| OCP-to-quantum claim | Nearest known area | Overlap level | What is not new | What may still be distinct | Evidence | Safe wording |
|---|---|---|---|---|---|---|
| Fixed-basis qubit phase-loss no-go | Standard projective measurement limits | High | Single-basis record cannot recover full phase family | Explicit target/fiber packaging across repo lanes | `QW001`, `QA004` | `ALREADY KNOWN IN SUBSTANCE`; keep as benchmark no-go |
| Same count, opposite recoverability (Z vs X target-aligned basis) | State discrimination + basis dependence | Medium-high | Basis choice affects distinguishability | Descriptor-matched anti-classifier packaging | `QW001-QW002`, `QA001` | `CLOSE PRIOR ART / REPACKAGED` with finite witness scope |
| Conditioned exactness does not imply invariant exactness across contexts | Calibration/context mismatch in measurement pipelines | Medium | Context-specific decoder dependence is known in practice | Clean theorem-style split and augmentation threshold packaging | `QW005-QW008`, `QA005` | `PLAUSIBLY DISTINCT` on supported family |
| One shared augmentation can restore invariant recovery | Additional measurement setting resolves ambiguity | Medium | Extra observables can restore identifiability | Explicit minimal-threshold framing in context-sensitive form | `QW003-QW004`, `QW005-QW008`, `QA006` | `PROVED ON SUPPORTED FAMILY`; avoid universal claim |
| Same distributed budget, opposite recoverability by allocation geometry | Local-vs-global measurement access in multipartite systems | Medium | Local marginals can miss correlations | Clean budget-matched target-specific split representation | `QW009-QW010`, `QA007` | `PLAUSIBLY DISTINCT` package on finite family |
| Dephasing fragility and collapse of target recoverability | Open-system decoherence | High | Decoherence suppresses coherence-dependent recovery | Explicit threshold witness tied to target recoverability labels | `QW011-QW017`, `QA008` | `ALREADY KNOWN IN SUBSTANCE`; benchmark-only value |
| QEC sector exact anchor | Knill-Laflamme QEC | Very high | Core theorem is standard | Cross-branch anchor role only | `QW018` + repo QEC tests | Keep as exact anchor; no novelty claims |
| Same measurement count, opposite target FI (phase blind vs sensitive) | Fisher/estimation design | High | Target-sensitive FI differences are known | Integration with anti-classifier lane and branch discipline | `QW019-QW024`, `QA009` | `VALIDATED / EMPIRICAL ONLY`; design lane only |
| OCP provides new quantum foundations | Foundations | Very high conflict | Quantum formalism already covers these mechanisms | None survived under falsification | full pass | `DISPROVED / COLLAPSED` as broad claim |

## Aggregate Novelty Signal From Witness Set

From `quantum_witness_catalog.csv` (24 rows):
- `ALREADY KNOWN IN SUBSTANCE`: 8
- `CLOSE PRIOR ART / REPACKAGED`: 10
- `PLAUSIBLY DISTINCT`: 6

Interpretation: most surviving content is disciplined packaging and scoped design/no-go extraction; narrow distinctness exists mainly in the context-sensitive and distributed-allocation packaging.
