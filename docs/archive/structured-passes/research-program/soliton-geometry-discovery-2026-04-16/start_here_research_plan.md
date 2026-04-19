# Start-Here Research Plan (Soliton + Geometry)

Date: 2026-04-16  
Program identity: independent soliton-geometry program, discovery-first and falsification-first

## Chosen first direction

**Direction S1**: Observation-limited recoverability of restricted soliton manifolds (modulo symmetry).

Why first:
- narrow and theorem-accessible,
- strong falsifiability via explicit counterexamples,
- bridges naturally to numerics without forcing broad framework transfer.

## 0) Core working problem

For a selected equation class (start with focusing 1D NLS one-soliton family), define:
- parameter manifold `P` (amplitude, velocity, center, phase),
- symmetry quotient (translation/phase equivalence),
- observation operators `M` from a controlled family.

Goal:
- characterize when `M` uniquely identifies equivalence classes in `P`.

## 1) First 90-day execution plan

### Weeks 1–2: setup + precise model

Deliverables:
- formal problem statement
- admissible observation class
- exact identifiability target (mod symmetry)
- known-results boundary note (to avoid rediscovery)

Kill conditions:
- if problem reduces to immediate standard theorem with no extension value, pivot to S2.

### Weeks 3–5: theorem/no-go attempt

Deliverables:
- necessary condition theorem candidate
- sufficient condition theorem candidate (restricted)
- same-observation non-uniqueness counterexample family

Kill conditions:
- if necessary and sufficient conditions collapse into tautology with no computable criterion.

### Weeks 6–8: perturbation robustness layer

Deliverables:
- conditional robustness bound under small model perturbations/noise
- failure examples where identifiability collapses abruptly

Kill conditions:
- if robustness claims cannot be quantified beyond numerics.

### Weeks 9–12: reproducible benchmark package

Deliverables:
- script set generating witness/counterexample families
- table of exact / approximate / impossible regimes in this restricted setting
- final note: proved vs conditional vs open

## 2) Parallel backup direction (activate only if S1 stalls)

**Direction S2**: Projection/reduction preservation/no-go for soliton manifolds.

Trigger to activate:
- S1 novelty collapses quickly or theorem payload is too weak.

Minimum viable result:
- one exact preservation criterion + one explicit no-go counterexample for a projection class.

## 3) Research hygiene rules

1. No universal claims across all soliton types.
2. Every promotion must be theorem/counterexample/benchmark backed.
3. Distinguish clearly: PROVED, CONDITIONAL, VALIDATED, OPEN, DISPROVED, ANALOGY ONLY.
4. Keep geometry only where it yields explicit invariants/obstructions.

## 4) Deliverables in this discovery package

- `soliton_geometry_orientation.md`
- `geometry_connection_audit.md`
- `adjacent_topics_map.md`
- `novelty_candidates.md`
- `falsification_results.md`
- `optional_existing_repo_bridge.md`
- `start_here_research_plan.md`
- `ranked_reading_list.md`
- `ranked_theorem_simulation_opportunities.md`
- `learning_path_beginner_to_advanced.md`

## 5) Decision gates (go/no-go)

### Gate A (end of week 5)
- Keep S1 only if at least one nontrivial theorem/no-go statement survives.

### Gate B (end of week 8)
- Keep S1 as main lane only if robustness layer yields quantitative content, not only numerics.

### Gate C (end of week 12)
- Promote to paper-lane only if package contains:
  - at least one theorem-grade statement,
  - at least one counterexample family,
  - reproducible scripts and regime table.

## 6) Immediate next actions (this week)

1. Fix exact one-soliton parametrization and equivalence relation.
2. Choose two explicit observation families (one likely sufficient, one likely deficient).
3. Prove first non-uniqueness lemma for deficient observation family.
4. Build first numeric witness scripts to cross-check formulas.

## 7) Final status of this plan

- Program-level status: **VALIDATED as a viable discovery program**
- Main lane status: **OPEN (high promise)**
- Broad unification status: **DISPROVED / rejected**
