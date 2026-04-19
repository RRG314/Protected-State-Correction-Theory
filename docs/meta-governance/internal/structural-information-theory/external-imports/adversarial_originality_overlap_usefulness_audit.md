# Adversarial Originality, Overlap, and Usefulness Audit
Date: 2026-04-19  
Workspace audited: `/Users/stevenreid/Documents/New project`

## Method (Skeptical by default)

Audit protocol used:
1. Mined local claim/theorem/status artifacts across OCP, gravity-information, information-research, MHD, CFD, SDS/meta lanes.
2. Built overlap judgments from theorem shape, not naming alone.
3. Queried external literature for nearest analogues (decision theory, identifiability, observability, QEC, thermodynamics, black-hole information, ROM/closure).
4. Treated every claim as non-original unless distinct assumptions + distinct conclusion + distinct witness value survived.
5. Separated lexical duplication risk from conceptual duplication risk.

Hard constraints followed:
- no universal-law inflation;
- no packaging-as-novelty;
- restricted claims retained only if falsifiable and witness-backed.

---

## 1) Master Overlap Map

| Core statement in your program | Nearest standard formulation | Field(s) | Similarity | What is actually new (if anything) | Citation requirement | Originality risk |
|---|---|---|---|---|---|---|
| Exact recoverability iff target factors through record map / fiber constancy | Doob-Dynkin/factorization logic; sufficiency-style factorization | probability/statistics, decision theory | Very High | Mostly a reframing and cross-lane normalization | Mandatory, front-and-center | High if claimed as new theorem |
| Collision with target variation implies impossibility | Non-identifiability/observational equivalence | inverse problems, system ID | High | Cleaner finite witness operationalization | Strong | Medium-high |
| Row-space/kernel compatibility in restricted linear classes | Linear observability/reconstructability conditions | control, linear systems, inverse problems | Very High | Restricted-linear packaging + attached no-go corpus | Mandatory | High |
| Same-rank / same-budget opposite verdict | Rank/count insufficiency known in many guises | system ID, sensing, experiment design | High | Large reproducible witness catalogs across lanes | Strong | Medium |
| No rank-only / no budget-only exact classifier (finite witness classes) | “Amount-only insufficient” appears in Blackwell/decision and identifiability literature | decision theory, statistics, ID | High conceptually | Distinct finite-catalog theorem package with explicit IDELB/DFMI protocol | Strong | Medium |
| Coarsening theorem (strong target implies weak target recoverability) | Standard sigma-algebra/partition coarsening logic | statistics, info theory | Very High | Branch-scoped exact/noisy witness integration | Mandatory | High |
| Family-enlargement false-positive fragility | Model class misspecification / distribution shift fragility | stats, ML, system ID | High | Explicit theoremized restricted-linear witness class | Strong | Medium |
| Model-mismatch instability theorem | Known in robust ID/observer mismatch settings | control, inverse problems | High | Canonical witness family + quantified failure floor | Strong | Medium |
| Minimal augmentation rank gap (delta-type law) | Sensor augmentation/completion ideas; observability completion | control/estimation design | Medium-High | Clean explicit minimal augmentation formula in your branch formalism | Strong | Medium |
| Bounded-domain projection compatibility and transplant failure | Helmholtz/Hodge boundary-compatibility is classical | PDE/CFD | Very High | Programmatically linked exact/no-go split with explicit family boundaries | Mandatory | Medium-high |
| MHD variable-resistivity obstruction/survivor classifications | Closure obstructions known broadly; specific restricted formulas may be new | MHD/PDE | Medium | Restricted-class symbolic theorem package appears plausibly distinct | Strong | Medium |
| Descriptor-fiber invariants (DFMI/IDELB/CL) | Confusion-lower-bound style and Blackwell-style insufficiency diagnostics are conceptually related | decision theory, classification diagnostics | Medium-High concept, medium implementation | New as branch instrumentation and witness-quantification layer | Strong | Medium |
| “Information as structure/distinction preserved under transformation” | Very close to existing sufficiency / partition / experiment-comparison viewpoints | stats, info theory, category-flavored formulations | High | Mostly unifying lens + operational claim discipline | Mandatory | High if called “new theory of information” |
| Gravity hidden-mass anti-classifier no-go (IDELB > 0 on declared class) | Decision/inference insufficiency known; application-specific claim may be novel | astro inference, inverse problems | Medium | New only on declared witness class with real-data pipeline | Strong | Medium-low (if scoped) |
| Hawking-channel threshold trends (compatibility vs degradation) | Noise-degradation effects unsurprising; channel framing standard | QI/statistical physics | High | Useful restricted diagnostic lane; weak theorem novelty | Moderate | Medium-high |
| SDS as theorem-core principle | No theorem-grade unique math identified | engineering workflow | N/A | Not new theorem content | Do not present as theorem | High (if promoted) |

---

## 2) Theorem-by-Theorem Novelty Table

Legend for novelty status (requested taxonomy):
- `KNOWN`
- `KNOWN REFORMULATION`
- `KNOWN WITH DIFFERENT LANGUAGE`
- `PLAUSIBLY DISTINCT RESTRICTED RESULT`
- `CLEARLY NEW ONLY ON DECLARED WITNESS CLASS`
- `NOT NEW / TOO CLOSE TO EXISTING RESULTS`
- `OPEN / CANNOT VERIFY`

| theorem/result/package | repo/source location | claim summary | nearest known analogue | overlap level | novelty status | confidence | claim as original? | citation urgency | keep/demote/cut |
|---|---|---|---|---|---|---|---|---|---|
| OCP-030 Observation fiber exactness | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/theory/advanced-directions/constrained-observation-formalism.md` | Exact recoverability iff target constant on record fibers | Doob-Dynkin/factorization/sufficiency logic | Very High | KNOWN REFORMULATION | High | No (except branch formalization) | Critical | Keep as core baseline, not novelty |
| UC collision no-go (meta/unifying) | `/Users/stevenreid/Documents/New project/internal_docs/unifying_theory_master_internal_report_2026-04-17.md` | Target-varying collision implies impossibility | Non-identifiability under observational equivalence | High | KNOWN WITH DIFFERENT LANGUAGE | High | No | Critical | Keep |
| OCP-045 minimal augmentation theorem | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/theorem-candidates/capacity-theorems.md` | Minimal unrestricted augmentation dimension via rank-gap | Observability completion / sensing augmentation | High | PLAUSIBLY DISTINCT RESTRICTED RESULT | Medium | Only restricted | High | Keep |
| OCP-047 same-rank insufficiency | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/theorem-candidates/pvrt-theorem-spine.md` | Same rank can yield opposite exactness verdicts | Rank insufficiency in ID/sensing | High | KNOWN WITH DIFFERENT LANGUAGE | High | No (the abstract idea) | High | Keep as witness theorem |
| OCP-048 coarsening split | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/fiber-based-recoverability-and-impossibility/fiber-formalism-core.md` | Recover strong => recover weak; converse can fail | Coarsening/refinement in statistics/info | Very High | KNOWN | High | No | High | Keep as structural lemma |
| OCP-049 no rank-only exact classifier | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/fiber-based-recoverability-and-impossibility/restricted-linear-fiber-theory.md` | No rank-only exact classifier on restricted finite classes | Decision-theoretic insufficiency / Blackwell non-equivalence to scalar summaries | High concept | PLAUSIBLY DISTINCT RESTRICTED RESULT | Medium | Only restricted | Critical | Keep |
| OCP-050 no budget-only exact classifier | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/fiber-based-recoverability-and-impossibility/restricted-linear-fiber-theory.md` | No fixed-library budget-only exact classifier | Sensor-count insufficiency lore | High | PLAUSIBLY DISTINCT RESTRICTED RESULT | Medium | Only restricted | High | Keep |
| OCP-051 noisy weaker-vs-stronger separation | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/fiber-based-recoverability-and-impossibility/fibers-and-weaker-vs-stronger-targets.md` | Weak target recoverable while strong fails under noise | Task-dependent identifiability under degradation | High | KNOWN WITH DIFFERENT LANGUAGE | Medium-high | Only restricted | High | Keep |
| OCP-052 family-enlargement false positive | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/fiber-based-recoverability-and-impossibility/theorem-candidates.md` | Exactness on small family fails on enlarged family | Model misspecification/OOD fragility | High | PLAUSIBLY DISTINCT RESTRICTED RESULT | Medium-high | Only restricted | High | Keep |
| OCP-053 canonical model-mismatch instability | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/fiber-based-recoverability-and-impossibility/theorem-candidates.md` | Trained decoder can fail under admissible family shift | Robustness/mismatch theory | High | PLAUSIBLY DISTINCT RESTRICTED RESULT | Medium | Only restricted | High | Keep |
| OCP-044 bounded finite-mode Hodge exactness | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/theorem-candidates/bounded-domain-hodge-theorems.md` | Exactness on boundary-compatible restricted family | Classical Helmholtz/Hodge decomposition with boundary conditions | Very High | KNOWN WITH DIFFERENT LANGUAGE | High | No (math), yes (restricted benchmark framing) | Critical | Keep |
| OCP-023 bounded transplant failure | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/physics/bounded-domain-projection-limits.md` | Periodic projector transplant fails bounded domain | Standard boundary incompatibility | Very High | KNOWN | High | No | Critical | Keep as anti-overclaim guard |
| DFMI / IDELB / CL package | `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/research-program/invariant_inventory.md` | Descriptor-fiber mixedness/lower-bound/lift diagnostics | Blackwell order/deficiency-like comparison spirit; confusion/lower-bound diagnostics | Medium-High | CLEARLY NEW ONLY ON DECLARED WITNESS CLASS | Medium | Only restricted | High | Keep as methods layer |
| INFO-T1 SPARC amount-only no-go | `/Users/stevenreid/Documents/New project/docs/research-program/information_physics_comprehensive_report.md` | IDELB positive on real SPARC witness class | Known insufficiency principles; domain instantiation is the novelty | Medium | CLEARLY NEW ONLY ON DECLARED WITNESS CLASS | Medium-high | Only restricted | High | Keep (best publishable empirical-negative unit) |
| GRAV-T1 hidden-mass no-go | `/Users/stevenreid/Documents/New project/docs/research-program/gravity_information_theorem_candidates.md` | No amount-only exact classifier on declared hidden-mass class | Same as above; inverse-problem ambiguity | Medium | CLEARLY NEW ONLY ON DECLARED WITNESS CLASS | Medium-high | Only restricted | High | Keep |
| GRAV-T3 degradation threshold candidate | `/Users/stevenreid/Documents/New project/docs/research-program/gravity_information_theorem_candidates.md` | Strong correlation of degradation with defects | Noise-degradation monotonic behavior in channels | High | NOT NEW / TOO CLOSE TO EXISTING RESULTS | Medium | No (as theorem) | Medium | Demote to diagnostic evidence |
| GRAV-T2 strict coarsening threshold order | `/Users/stevenreid/Documents/New project/docs/research-program/gravity_information_theorem_candidates.md` | Strict k* order coarse/medium/fine | Strong ordering claim failed in own tests | N/A | NOT NEW / TOO CLOSE TO EXISTING RESULTS | High | No | Low | Cut (already collapsed) |
| MHD-O1/O2/O3 variable-eta obstruction classes | `/Users/stevenreid/Documents/New project/mhd-toolkit/docs/theorems/reconnection-structure-and-closure-defect.md` | Restricted symbolic obstruction/survivor classes | MHD closure obstruction literature | Medium | PLAUSIBLY DISTINCT RESTRICTED RESULT | Medium | Only restricted | High | Keep |
| MHD-XG1 local toroidal obstruction | `/Users/stevenreid/Documents/New project/mhd-toolkit/docs/theorems/toroidal-and-geometry-obstructions.md` | Local explicit obstruction term under shear deformation | Perturbative obstruction analysis traditions | Medium | PLAUSIBLY DISTINCT RESTRICTED RESULT | Medium | Only restricted | Medium-high | Keep |
| SDS theorem-core promotion | `/Users/stevenreid/Documents/New project/internal_docs/meta_theory_internal_master_report_2026-04-17.md` | SDS as foundational theorem core | Engineering workflow motifs | N/A | NOT NEW / TOO CLOSE TO EXISTING RESULTS | High | No | Low | Cut from theorem claims |
| “FQSO” positive information object | `/Users/stevenreid/Documents/New project/docs/research-program/structural_information_theory_comprehensive_report.md` | Information as target-relevant distinction over fibers/quotients | Sufficiency/partition/experiment-comparison/quotient viewpoints | High | KNOWN WITH DIFFERENT LANGUAGE | Medium | No (as broad theory) | Critical | Demote to framework lens unless new theorem layer added |

---

## 3) Foundations / Language Overlap (A-D audit answers)

### A1-A4: What is already known (most important collisions)

1. **Factorization/fiber-constancy exactness core**  
Very close to known factorization/sufficiency structures (Doob-Dynkin/sufficient-statistic logic).  
Risk if presented as a newly discovered universal theorem: high.

2. **Amount-only insufficiency**  
Core idea strongly overlaps with Blackwell/comparison-of-experiments and identifiability literature where “more MI/entropy/rank” does not imply better decision relevance for every target/task.

3. **Row-space compatibility and minimal augmentation**  
Overlaps with observability/reconstructability and sensing-design completion frameworks. Your contribution is mostly scoped packaging + witness curation.

4. **Bounded vs periodic projection claims**  
Classical Helmholtz/Hodge boundary dependence is established. Novelty is mostly in disciplined integration into your no-go spine and reproducible restricted tests.

5. **Gravity-information framing**  
Most black-hole entropy/Hawking/Page/holographic links are known physics; your program mostly reframes them as recoverability/inference channels.

6. **Positive “information as structure” language**  
Conceptually old in several fields (sufficiency, partitions/equivalence classes, decision relevance, coarse-graining). Current form is mostly a unifying lens.

### C1-C5: Is cross-domain synthesis useful or mainly narrative?

Assessment: **mixed**.
- Theorem-grade cross-domain transfer: limited.
- Useful transfer that does exist: witness-construction discipline, anti-overclaim status system, common diagnostics pipeline (IDELB/DFMI/CL family).
- Weak transfer: broad metaphysical unification of “information” across physics branches.

Reviewer-likely judgment:
- “Useful integrative methods/benchmark narrative with disciplined claim boundaries.”
- Not “new general mathematical foundation of information.”

### D1-D7: Positive theory of information verdict

1. “Information as structure/distinction/recoverability under transformation” is **not new in substance**.
2. Your version is sharper operationally in some lanes (finite witness diagnostics), but not a new universal theory.
3. Strongest current content is **negative limitation theory**: amount-based descriptors are insufficient on declared classes.
4. Positive theory remains incomplete until at least:
   - axiomatized primitive object with theorem consequences beyond known factorization;
   - stability theorem not reducible to existing identifiability/robustness machinery;
   - branch-transferrable quantitative law that survives non-toy external validation.

---

## 4) Language / Framing Risk Report

### High-risk framings to avoid

Do not present as original:
- “universal recoverability core theorem” (without explicit statement that this is a classical factorization-type backbone).
- “new theory of information” (current evidence does not clear this bar).
- “new invariant” for DFMI/IDELB without “restricted finite witness class” qualifier.
- “gravity-information theorem” unless strictly “inference-channel surrogate/declared class”.

### Phrases requiring explicit citation or demotion

Needs citation (not claim ban):
- “exact recoverability iff factorization/fiber constancy”
- “amount measures insufficient for task recoverability”
- “coarsening preserves weaker-target recoverability”
- “minimal augmentation by rank gap in restricted-linear setting”

Should be demoted (cannot be claimed):
- “universal scalar capacity/information law”
- “SDS theorem-core”
- “strict universal cross-domain threshold laws”

### Plagiarism / near-duplication risk

Lexical risk:
- No clear evidence of long verbatim copying found in sampled phrase checks.

Conceptual duplication risk:
- High in core theorem narrative if citations are not explicit.
- Moderate in descriptor/invariant layer (likely acceptable if clearly framed as restricted instrumentation, not foundational novelty).

Bottom line:
- This is mainly a **citation and scope-risk problem**, not a copy-paste plagiarism pattern.

---

## 5) Usefulness Report (Hard-nosed)

### Is it useful despite overlap?
Yes, **conditionally useful**.

### Useful to whom?

| Audience | Usefulness level | Why |
|---|---|---|
| Applied control / inverse-problem researchers | Medium-High | Reproducible counterexample/witness pipelines against rank/count heuristics |
| Computational scientists (CFD/MHD) | Medium | Practical no-go and compatibility diagnostics for reduced models / closure sanity checks |
| Information theorists / statisticians | Low-Medium | Conceptual overlap is high; novelty mainly in restricted witness instrumentation |
| Fundamental physicists | Low (for theorem novelty), Medium (for diagnostics framing) | Mostly interpretive recasting; strongest value is inference diagnostics, not new physics |
| Methodology/software reviewers | High | Strong reproducibility, explicit falsification discipline, useful negative-result curation |

### Is it objectively better/simpler than standard formulations?

Better:
- for organizing and testing claims with explicit statuses and witness catalogs;
- for detecting overclaim via anti-classifier stress tests.

Not better:
- as a replacement for core established theory in statistics/control/info/physics.

### Publishability utility

Most credible lane:
- **restricted negative-result + methods/benchmark paper** (not grand theory paper).

---

## 6) Reviewer-Simulation Pass

### Package: OCP recoverability core
1. Actually new: little at theorem-core level; mostly disciplined integration.
2. Known material: factorization/sufficiency-like backbone.
3. Overstated risk: calling it new universal theorem.
4. Worth keeping: explicit restricted theorem/no-go spine + witness artifacts.
5. Cut: universal scalar language.
6. Publication recommendation: theorem note + benchmark/methods supplement.
7. Allowed scope: restricted families only, with explicit overlap citations.

### Package: Anti-classifier / descriptor-fiber
1. Actually new: finite witness instrumentation and reproducible lower-bound workflow.
2. Known material: insufficiency-of-amount theme.
3. Overstated risk: implying foundational new information measure.
4. Keep: IDELB/DFMI/CL as branch diagnostics.
5. Cut: universal invariance claims.
6. Publication recommendation: restricted negative-result + empirical methods.
7. Allowed scope: declared witness classes only.

### Package: Gravity-information lane
1. Actually new: class-specific inference witnesses and evaluated restrictions.
2. Known material: most black-hole/info theory foundations.
3. Overstated risk: “resolving paradox” or new gravity law.
4. Keep: hidden-mass inference no-go and compatibility diagnostics.
5. Cut: universal gravity-information framing.
6. Publication recommendation: methods note (inference diagnostics), not fundamental theory.
7. Allowed scope: surrogate channels and declared data classes.

### Package: MHD closure lane
1. Actually new: plausible restricted symbolic obstruction/survivor subclasses.
2. Known material: closure obstruction direction broadly.
3. Overstated risk: universal closure theorem language.
4. Keep: restricted-class formulas and tests.
5. Cut: global extrapolation.
6. Publication recommendation: restricted applied-math theorem paper.
7. Allowed scope: exact ansatz families + explicit regularity assumptions.

---

## 7) Final Verdict (Plain)

1. **Is the core mostly known?**  
Yes. The backbone is mostly known mathematics in new packaging.

2. **Is the framework mostly reinterpretation?**  
Yes, at the broad “theory of information” level.

3. **Are there actually new restricted results?**  
Yes, but narrow: finite witness no-go packages, family-enlargement/mismatch restricted theorems, and some MHD restricted symbolic classes.

4. **Is cross-domain tying useful?**  
Partly useful as a diagnostic/governance layer; mostly not a source of new general theorems.

5. **Any serious publishable core?**  
Yes: a restricted negative-result + benchmark/methodology core around amount-only insufficiency with explicit real-system witness sets.

6. **Strongest publishable unit right now**  
“On declared witness classes, amount-only descriptors cannot exactly classify recoverability; compatibility-aware augmentation measurably reduces irreducible error bounds.”  
This is publishable as a **restricted no-go + methods/benchmark paper**, not a universal information theory.

7. **What should be abandoned?**  
Universal information-theory claims, universal scalar invariants, and theorem-core SDS claims.

---

## 8) Action Plan (Concrete)

### Keep
1. Restricted theorem/no-go spine (OCP-049/050/052/053 + bounded-domain compatibility splits).
2. Real-system witness pipelines (SPARC and hidden-mass lanes).
3. Descriptor-fiber diagnostics as methods layer.

### Cut
1. Universal scalar capacity language.
2. Any “new fundamental information theory” claim in abstracts/titles.
3. SDS-as-core theorem statements.

### Relabel
1. “Theory” -> “restricted recoverability framework” in broad docs.
2. “Invariant” -> “restricted diagnostic statistic” unless theorem-grade invariance proved.
3. “Universal core theorem” -> “classical factorization backbone used as organizing axiom.”

### Cite immediately (high urgency)
1. Factorization/sufficiency lineage.
2. Blackwell comparison/deficiency lineage.
3. Observability/identifiability lineage.
4. QEC (Knill-Laflamme) lineage.
5. Helmholtz/Hodge boundary dependence lineage.
6. Landauer and black-hole entropy/Page/island references for physics context statements.

### Stop claiming
1. New universal theory of information.
2. New force/new ontology.
3. Universal cross-domain threshold law.

### Test more (if originality is the goal)
1. Out-of-family generalization of anti-classifier claims across independently curated external datasets.
2. Stability theorem above factorization core with nontrivial quantitative bounds.
3. Head-to-head against known decision-theoretic baselines (Blackwell/deficiency-inspired comparators).

### Strongest paper lane now
1. **Primary:** restricted no-go + witness benchmark paper (methods + reproducibility + failure taxonomy).
2. **Secondary:** restricted MHD theorem paper (if symbolic claims survive external review).
3. **Not recommended now:** universal positive theory-of-information manuscript.

---

## 9) Literature anchors used in this audit (selected)

Decision/sufficiency/experiment comparison:
- Blackwell, *Comparison of Experiments* (1951): [PDF](https://digicoll.lib.berkeley.edu/record/112749/files/math_s2_article-08.pdf)
- Petz, *Sufficient Subalgebras and the Relative Entropy* (1986): [PDF](https://math.bme.hu/~petz/pdf/29suff.pdf)
- Torgersen, *Comparison of Statistical Experiments* (1991): [Cambridge](https://www.cambridge.org/core/books/comparison-of-statistical-experiments/405F64D2A2FB3A4E6A1893C1C8A4A60B)
- Taraldsen, *Optimal Learning from the Doob-Dynkin lemma* (2018): [arXiv](https://arxiv.org/abs/1801.00974)
- Harremoës & Vignat, *Coarse-graining and the Blackwell order* (2017): [arXiv](https://arxiv.org/abs/1701.07602)

Identifiability/observability/control:
- Bellman & Åström, *On structural identifiability* (1970): [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/002555647090132X)
- Ljung & Glad, *On global identifiability for arbitrary model parametrizations* (1994): [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0005109894900299)
- Hermann & Krener, *Nonlinear controllability and observability* (1977): [IEEE DOI](https://doi.org/10.1109/TAC.1977.1101601)
- Kalman, *A New Approach to Linear Filtering and Prediction Problems* (1960): [PDF mirror](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf)
- Villaverde, *Observability and Structural Identifiability of Nonlinear Biological Systems* (2018): [arXiv](https://arxiv.org/abs/1812.04525)

Quantum/gravity/information context:
- Knill & Laflamme, *A Theory of Quantum Error-Correcting Codes* (1996): [arXiv](https://arxiv.org/abs/quant-ph/9604034)
- Marletto & Vedral, gravitationally induced entanglement proposal (2017): [arXiv](https://arxiv.org/abs/1707.06036)
- Bose et al., spin entanglement witness (2017): [arXiv](https://arxiv.org/abs/1707.06050)
- Bekenstein, *Black Holes and Entropy* (1973): [APS](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.7.2333)
- Hawking, *Particle creation by black holes* (1975): [OSTI entry](https://www.osti.gov/biblio/4006691-particle-creation-black-holes)
- Page, *Average entropy of a subsystem* (1993): [PubMed](https://pubmed.ncbi.nlm.nih.gov/10055503/)
- Ryu & Takayanagi (2006): [arXiv](https://arxiv.org/abs/hep-th/0603001)
- Penington (2019): [arXiv](https://arxiv.org/abs/1905.08255)
- Almheiri et al. (2019): [arXiv](https://arxiv.org/abs/1908.10996)
- Replica wormholes (2019): [arXiv 1911.11977](https://arxiv.org/abs/1911.11977), [arXiv 1911.12333](https://arxiv.org/abs/1911.12333)
- Landauer (1961): [PDF mirror](https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/landauer61.pdf)
- Bérut et al. experimental Landauer verification (2012): [Nature](https://www.nature.com/articles/nature10872)

ROM/closure context:
- Rowley, balanced POD vs POD/truncation comparison (2005): [Princeton record](https://collaborate.princeton.edu/en/publications/model-reduction-for-fluids-using-balanced-proper-orthogonal-decom/)
- Data-driven closure for projection ROMs (2021): [arXiv](https://arxiv.org/abs/2103.12727)

---

## 10) Bottom-line answer to your success question

What survives as defensible originality:
- not a new universal theory;
- yes, a restricted negative-result and diagnostics program with real-system witness value.

What does not survive:
- broad foundational originality claims in “what information is” form without heavy qualification.

