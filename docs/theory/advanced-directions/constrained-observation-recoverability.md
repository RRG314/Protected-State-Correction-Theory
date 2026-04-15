# Constrained-Observation Recoverability

## Status

Branch overview for an active research lane inside **Protected-State Correction Theory**.

This file now serves as the branch-level overview. The formal and computational follow-through lives in:

- [constrained-observation-formalism.md](constrained-observation-formalism.md)
- [constrained-observation-derivations.md](constrained-observation-derivations.md)
- [constrained-observation-theorems.md](../../theorem-candidates/constrained-observation-theorems.md)
- [constrained-observation-no-go.md](../../impossibility-results/constrained-observation-no-go.md)
- [constrained-observation-results-report.md](constrained-observation-results-report.md)
- [constrained-observation-clean-results.md](constrained-observation-clean-results.md)
- [constrained-observation-failures.md](constrained-observation-failures.md)
- [constrained-observation-validation.md](constrained-observation-validation.md)
- [constrained-observation-assessment.md](constrained-observation-assessment.md)

The branch remains falsification-first. It should stay in the repository only if it continues to support useful formal structure, real negative results, or credible computational tools.

---

## 1. Branch Title

**Constrained-Observation Recoverability**

Working subtitle:

**Recoverability of Protected Variables Under Coarse Records**

This name is intentionally narrow. It is about recoverability under limited observation, not about consciousness, observer-created reality, or any metaphysical interpretation of measurement.

---

## 2. Branch Summary

### Core question

When a system is observed only through a constrained record map, when does the record preserve enough structure to recover:

- a protected state exactly,
- a protected state approximately,
- or only a weaker protected variable,
- and when is recovery impossible no matter what estimator or correction architecture is used?

### Why this is worth studying

The current repository studies correction once the relevant state/error structure is available. This branch asks a prior question:

> does the available record preserve enough information for correction or reconstruction to make mathematical sense at all?

That question is independently meaningful in:

- quantum measurement and channel recovery,
- statistical sufficiency,
- observability and functional observers,
- inverse problems and stability,
- compressed sensing and restricted recovery,
- PDE and constrained-system reconstruction.

### How it fits the existing repository

This branch plugs naturally into Protected-State Correction Theory by inserting an **observation layer** ahead of the correction layer.

Current theory asks:

- what is protected,
- what is disturbance,
- what operator removes disturbance without damaging the protected part?

This branch asks:

- what is actually visible,
- what is lost under observation or coarse-graining,
- and whether the visible record supports exact, stable approximate, asymptotic, or impossible recovery of the protected quantity.

This is not just relabeling the current OCP branch. It changes the object of study from **correction under a known split** to **recoverability under constrained access to the split itself**.

---

## 3. Standard-Known Background

This branch touches several conventional literatures.

### 3.1 Quantum measurement, reversibility, and sufficiency

Standard known material:

- Knill-Laflamme and QEC already give exact recoverability conditions for correctable error sectors.
- Petz-style recovery and later recoverability results study when a quantum channel can be reversed exactly or approximately on a chosen state family.
- Quantum sufficiency and equality conditions for data-processing are already well-developed.

Representative anchors:

- Knill and Laflamme (1997), *Theory of Quantum Error-Correcting Codes*.
- Jenčová and Petz (2006), *Sufficiency in Quantum Statistical Inference*.
- Junge, Renner, Sutter, Wilde, and Winter (2018), *Universal recovery maps and approximate sufficiency of quantum relative entropy*.
- Ahn, Doherty, and Landahl (2002), *Continuous Quantum Error Correction via Quantum Feedback Control*.

What is standard here:

- exact reversibility on a state family,
- approximate recoverability from relative-entropy or fidelity statements,
- sufficiency of a coarse-graining/channel with respect to a family of states.

What is not yet automatically provided by that literature:

- a cross-domain protected-variable language that can compare quantum, control, and PDE observation problems without pretending they are the same theorem.
- a repo-integrated classification of observation maps into exact, stable approximate, asymptotic, and impossible recoverability classes.

### 3.2 Classical statistics and sufficiency

Standard known material:

- a statistic is sufficient when it retains all information relevant to a parameter or hypothesis family.
- approximate sufficiency and experiment comparison are also standard topics.

Representative anchors:

- Pfanzagl (1974), sufficiency characterized by testing power.
- Le Cam (1964), sufficiency and approximate sufficiency.

What is standard here:

- exact recoverability of a parameter from a statistic is a sufficiency/factorization question.

What remains open enough to matter here:

- a protected-variable and no-go formulation adapted to dynamical, operator, and physics settings rather than only static statistical families.

### 3.3 Control, observability, and functional observers

Standard known material:

- classical observability determines when the full state can be reconstructed from outputs.
- detectability gives asymptotic reconstruction/stability conditions.
- functional observability and functional observers study recovery of a chosen state functional rather than the full state.

Representative anchors:

- Luenberger observer theory.
- functional observer literature for linear and nonlinear systems.
- recent nonlinear functional observability work such as *Functional observability and subspace reconstruction in nonlinear systems* (Phys. Rev. Research 4, 043195, 2022).

What is standard here:

- recovering a linear or nonlinear functional of the state from partial observations is already a real field.

Important implication:

- any claim that “recovering only the protected variable instead of the full state” is itself novel would be false.

What may still be open enough to pursue:

- importing that insight into a protected-state/no-go classification tied explicitly to exact versus asymptotic recovery and tested against non-control systems.

### 3.4 Inverse problems and stable recovery

Standard known material:

- injectivity is not enough; stability matters.
- inverse problems use stability constants, modulus-of-continuity bounds, and ill-posedness classifications.

Representative anchors:

- abstract inverse-problem stability literature,
- modulus-of-continuity formulations,
- Alberti-Capdeboscq-Privat (2020), *On the randomised stability constant for inverse problems*.

What is standard here:

- exact recoverability without stable inversion is fragile,
- stability constants and moduli already exist in some form.

What may still be worth building:

- a protected-variable version of collapse/stability metrics that speak naturally to observation maps rather than only to full inverse maps.

### 3.5 Signal recovery and compressed sensing

Standard known material:

- restricted injectivity, null-space properties, and phase transitions already govern exact and stable recovery on structured families.
- the right question is often not injectivity on the full space but injectivity on a restricted family.

Representative anchors:

- Candès-Romberg-Tao,
- Donoho-Tanner,
- RIP / null-space-property literature.

What is standard here:

- restricted recoverability on a family is a mature idea.

What may still be useful here:

- making restricted recoverability a central, theorem-linked branch for protected variables and connecting it to correction/no-go language.

### 3.6 PDE and constrained-system observability

Standard known material:

- partial-state PDE estimation, observability inequalities, and observer design already exist.
- projection and reconstruction in constrained PDEs often depend sharply on geometry, sensor placement, and boundary conditions.

Representative anchors:

- Chorin-style projection and its descendants,
- PDE observer reviews,
- wave/PDE observability literature such as Bardos-Lebeau-Rauch.

What is standard here:

- partial observation can support exact, stable, or impossible recovery depending on the geometry.

What may still be worth doing here:

- a protected-variable classification that keeps exact projector cases, asymptotic observer cases, and explicit no-go cases in one disciplined framework.

---

## 4. Exact Research Question

The branch should study the following question:

> Given an admissible state family and a protected variable of interest, when does a constrained observation map preserve enough information to support exact recovery, stable approximate recovery, asymptotic recovery, or no recovery of that protected variable?

This is more specific than “measurement changes systems” and more useful than “information loss causes irrecoverability.”

The intended target is not full-state metaphysics. It is:

- recoverability under coarse observation,
- recoverability of protected variables rather than necessarily the full state,
- threshold collapse of recoverability as observation coarsens,
- and constructive no-go criteria that say when a record can never support the intended recovery task.

---

## 5. Strongest Plausible Novelty Target

### Proposed novelty target

**A protected-variable recoverability-collapse metric and classification for constrained observation maps.**

The best candidate is not a vague statement about observation and disturbance.

It is a narrower question:

> can one define a mathematically useful collapse metric for a record map that detects the transition from exact recovery to stable approximate recovery to irrecoverability for a chosen protected variable on a chosen admissible family?

### Why this is stronger than the obvious directions

It is stronger than “measurement-disturbance tradeoff exists” because it asks for:

- a concrete metric,
- exact/no-go criteria,
- stability behavior under observation noise or coarsening,
- and computationally testable thresholds.

It is stronger than “channels are invertible on some families” because it is not just a yes/no inversion question. It distinguishes:

- exact and stable,
- exact but unstable,
- asymptotic only,
- and impossible.

It is stronger than “functional observability already exists” because it aims to:

- classify observation maps by recoverability class,
- compare static and dynamic recovery inside one branch,
- and connect quantum, PDE, and observer examples through the same protected-variable language without claiming a universal theorem prematurely.

### Honest novelty assessment

The raw ingredients are mostly known in different literatures:

- sufficiency,
- functional observability,
- inverse stability,
- restricted injectivity.

So the branch is **not** automatically novel just because it mentions them together.

The branch becomes genuinely worth keeping only if it produces at least one of:

1. a useful protected-variable recoverability metric with provable cross-domain behavior,
2. a nontrivial threshold theorem for a family of constrained observation maps,
3. a sharp no-go criterion stronger than “the map is not invertible on the whole space,”
4. or a cross-domain theorem that is not already a transparent restatement of existing observability or sufficiency results.

---

## 6. Formal Structure

Let:

- `X` be the ambient state space,
- `A ⊂ X` the admissible state family,
- `p : A -> P` the **protected variable** we want to recover,
- `M : A -> Y` the **observation/record map**,
- `R : Y -> P` a recovery or reconstruction map.

`p` may be:

- the full protected state,
- a protected component,
- a sector label,
- a divergence-free projection,
- a functional of the state,
- or another explicitly defined protected quantity.

### 6.1 Exact recoverability

Exact recoverability on `A` means:

```text
R(M(x)) = p(x),   for all x in A.
```

### 6.2 Approximate recoverability

Given metrics `d_X`, `d_Y`, `d_P`, approximate recoverability means that there exists `R` such that:

```text
d_P(R(M(x)), p(x)) <= epsilon
```

uniformly on `A`, or under record perturbations:

```text
d_P(R(y), p(x)) <= epsilon
quad whenever quad d_Y(y, M(x)) <= eta.
```

### 6.3 Irrecoverability / no-go

Irrecoverability means there is no map `R` achieving the chosen exact or approximate objective on the admissible class.

The sharp exact no-go condition is:

```text
exists x, x' in A such that M(x)=M(x') but p(x) != p(x').
```

Then no exact recovery map can exist.

### 6.4 Recoverability-collapse modulus

Define the **protected-variable collapse modulus** of the observation map by

```text
kappa_{M,p}(delta)
  = sup { d_P(p(x), p(x')) : x,x' in A, d_Y(M(x), M(x')) <= delta }.
```

Interpretation:

- `kappa(0)=0` means the record separates all protected values on `A`.
- `kappa(0)>0` means exact recovery is impossible.
- the rate at which `kappa(delta)` goes to zero measures the stability of approximate recovery.

This is the best scalar candidate for the branch.

It is closely related to a modulus of continuity for the inverse problem, so it is **not** claimed as a completely new mathematical object in the abstract. The possible contribution would come from how it is specialized to protected-variable recovery and used across several conventional systems.

### 6.5 Recoverability margin

For linear or metric-friendly settings one can also define a **recoverability margin**

```text
alpha_{M,p}(A)
  = inf_{x != x' in A, p(x) != p(x')}
      d_Y(M(x), M(x')) / d_P(p(x), p(x')).
```

Interpretation:

- `alpha > 0` means the record separates protected values with a positive margin.
- `alpha = 0` may mean either instability or true collapse.
- exact and stable recovery is strongest when `alpha > 0`.

### 6.6 Static versus asymptotic observation-recovery

Static recoverability:

- one record `M(x)` supports recovery.

Asymptotic recoverability:

- a time-indexed record stream or observer `M_t` supports recovery only over time.

For dynamics:

- state `x_t`,
- observations `y_t = C x_t`,
- protected variable `p(x_t)`,
- observer/reconstructor `\hat p_t`.

Asymptotic recoverability means:

```text
d_P(\hat p_t, p(x_t)) -> 0 as t -> infinity.
```

---

## 7. Best Theorem and No-Go Candidates

### 7.1 Candidate theorem backbone

#### COR-T1: Protected-variable factorization theorem

Statement:

There exists an exact recovery map `R : Y -> P` with `R o M = p` on `A` if and only if

```text
M(x) = M(x')  implies  p(x)=p(x')
```

for all `x,x' in A`.

Status:

- mathematically straightforward,
- essentially standard,
- but foundational for the branch.

Why still useful:

- it is the clean exact criterion,
- it exposes exact recovery as a sufficiency/factorization property,
- and it turns many vague discussions into a precise pass/fail statement.

#### COR-T2: Collapse-modulus recovery bound

Candidate statement:

If `kappa_{M,p}(0)=0`, then exact recovery is possible on `A`.

If `kappa_{M,p}(delta)` stays positive at `delta=0`, exact recovery is impossible.

If `kappa_{M,p}(delta) <= omega(delta)` for some modulus `omega`, then approximate recovery under record noise `eta` cannot beat `omega(eta)` up to geometric constants, and in favorable settings can be achieved at that scale.

Status:

- likely derivable from standard inverse-stability arguments,
- likely not new in full generality,
- still a very strong branch backbone.

Why useful:

- this is the right metric-level bridge from exact to approximate to impossible.

#### COR-T3: Linear restricted recovery criterion

Candidate statement:

Let `A` be a linear family or structured family and `p(x)=Lx`, `M(x)=Ox` linear.

Then exact protected-variable recovery is possible if and only if

```text
ker(O) cap Delta_p(A) = {0},
```

where `Delta_p(A)` is the set of admissible secants that change the protected variable.

Equivalent linear form on a linear subspace `F`:

```text
ker(O) cap F subset ker(L).
```

Status:

- standard linear algebra in spirit,
- plausibly useful in this exact form,
- not obviously publishable by itself.

Why useful:

- this is already sharper than generic non-invertibility because it is tied to the protected variable rather than the full state.

### 7.2 Best no-go candidates

#### COR-N1: Fiber-collision no-go

If two admissible states produce the same record but different protected values, exact recovery is impossible.

Status:

- standard and certain,
- should be treated as a core branch no-go.

#### COR-N2: Divergence-only no-go for protected velocity recovery

For the periodic divergence-free velocity family, the observation map `u -> div u` is identically zero on the protected class, so it cannot recover the protected velocity field.

Status:

- a direct and useful negative result,
- closely aligned with existing repo intuition,
- not new in pure PDE theory, but a strong branch anchor.

#### COR-N3: Single-basis phase-loss no-go for full qubit recovery

For the full qubit Bloch family, a single projective measurement in the `Z` basis does not recover phase information, so exact state recovery from the classical record is impossible.

Status:

- standard quantum fact,
- excellent falsification anchor.

#### COR-N4: Unobservable protected-functional no-go

For a linear dynamical system, if the unobservable subspace contains a direction on which the protected functional is nonzero, then asymptotic recovery of that functional is impossible from the observation stream alone.

Status:

- likely already standard in the functional-observer literature,
- still worth using as the control-side no-go anchor.

### 7.3 Which candidates are strongest to pursue first?

Best order:

1. `COR-T2` collapse-modulus backbone.
2. `COR-T3` linear protected-functional criterion.
3. `COR-N4` asymptotic functional-observer no-go.
4. family-specific threshold results in selected toy systems.

---

## 8. Conventional System Map

### 8.1 Quantum toy model: qubit under constrained classical record

State space:

- qubit density matrices.

Protected object:

- either the full state on a restricted one-parameter family,
- or a chosen protected variable such as the meridian angle `theta`.

Observation map:

- classical `Z`-basis measurement record,
- optionally with classical readout noise parameter `eta`.

What is lost:

- phase/coherence outside the chosen commuting family.

Exact recovery meaning:

- on the meridian family `|psi(theta)> = cos(theta/2)|0> + sin(theta/2)|1>`, the `Z`-record determines `theta` exactly.

Approximate recovery meaning:

- with noisy readout, `theta` remains recoverable but the margin collapses as `eta` approaches the fully randomizing limit.

No-go meaning:

- on the full Bloch sphere or on families with varying azimuthal phase, the same record map collapses different states to the same probability pair.

Why this system is good:

- physically standard,
- exactly analyzable,
- and it cleanly separates family-restricted exact recovery from full-family irrecoverability.

### 8.2 PDE/constrained-system toy model: periodic divergence-free velocity recovery

State space:

- periodic zero-mean velocity fields on the 2D torus.

Protected object:

- the divergence-free velocity field.

Observation maps:

1. `M_div(u) = div u`
2. `M_curl(u) = curl u` (vorticity)
3. truncated low-mode vorticity map.

What is lost:

- `div u` loses all information on the protected divergence-free class.
- low-mode vorticity loses high-frequency detail.

Exact recovery meaning:

- from full vorticity, exact recovery of the divergence-free velocity holds via Biot-Savart on the chosen periodic class.

Approximate recovery meaning:

- from low-mode vorticity, only coarse recovery is possible, with error controlled by the neglected tail.

No-go meaning:

- divergence-only records cannot recover the protected velocity field even though they are relevant to the constraint.

Why this system is good:

- it is physically standard,
- it fits the current repo’s exact continuous and no-go architecture,
- and it distinguishes meaningful records from insufficient ones.

### 8.3 Control / observability toy model: recovering a protected functional

State space:

- linear dynamical system `x_{t+1}=Ax_t`, `y_t=Cx_t` or continuous-time analogue.

Protected object:

- a chosen linear functional `p(x)=Lx`, not necessarily the full state.

Observation map:

- finite-horizon output map `M_T(x0) = (y_0, ..., y_{T-1})`,
- or the observation stream for an asymptotic observer.

What is lost:

- directions in the unobservable subspace.

Exact recovery meaning:

- the output map separates all states in the admissible family that differ in `Lx`.

Approximate recovery meaning:

- output noise and poor Gramian conditioning degrade the protected-functional estimate.

Asymptotic recovery meaning:

- a functional observer reconstructs `Lx_t` over time even when full state reconstruction is unnecessary.

No-go meaning:

- if the unobservable subspace contains directions that change `Lx`, no observer can recover the protected variable from outputs alone.

Why this system is good:

- it is a standard conventional comparison point,
- it ties directly to observability and detectability literature,
- and it shows that the branch is not just quantum or PDE language.

### 8.4 Secondary benchmark: sparse recovery under constrained measurements

This should be treated as a secondary benchmark rather than a central theorem anchor.

Protected object:

- a structured signal (e.g. sparse vector).

Observation map:

- undersampled linear measurements.

Why include it:

- the family-restricted injectivity and phase-transition language are useful computationally.

Why not make it central:

- the literature is already very mature, and novelty would be hard to claim unless the branch produces a protected-variable statement genuinely sharper than existing restricted-recovery conditions.

---

## 9. Full Falsification-First Test Suite

### Test family A: Exact recovery on restricted families

#### Test A1: qubit meridian exact-recovery test

What is tested:

- exact recovery of `theta` from a `Z`-basis classical record on the meridian family.

Why it matters:

- it shows that constrained observation can support exact recovery on a nontrivial protected family.

Success:

- zero reconstruction error up to numerical precision.

Failure:

- if exact reconstruction fails on this family, the branch formalism is probably mis-specified.

Meaning:

- success gives a clean exact constrained-observation anchor.

#### Test A2: vorticity-to-velocity exact-recovery test

What is tested:

- exact recovery of periodic divergence-free velocity from full vorticity on a chosen Fourier family.

Why it matters:

- it gives a conventional PDE exact-recovery anchor.

Success:

- reconstruction error near machine precision.

Failure:

- would likely mean the discrete reconstruction or family definition is wrong.

Meaning:

- success supports an exact continuous observation branch distinct from the correction operator branch already in the repo.

### Test family B: Partial-information collapse tests

#### Test B1: phase-loss no-go on enlarged qubit family

What is tested:

- whether distinct states with different azimuthal phase produce the same `Z`-record.

Why it matters:

- this is the canonical quantum fiber-collision no-go.

Success:

- explicit state pairs with equal record and different protected value are found.

Failure:

- if not found, the family or protected variable was chosen too narrowly.

#### Test B2: divergence-only no-go on velocity family

What is tested:

- whether distinct divergence-free fields have identical divergence record.

Why it matters:

- this is the branch’s PDE-side impossibility anchor.

Success:

- multiple distinct protected states map to the same record.

Failure:

- would indicate a mistake in the protected family choice.

### Test family C: Stability and collapse-modulus tests

#### Test C1: noisy qubit record sweep

What is tested:

- recovery margin and collapse modulus as readout noise `eta` increases.

Why it matters:

- this is the cleanest possible exact-to-unstable-to-impossible parameter sweep.

Success:

- margin decreases monotonically and collapses at the fully randomizing threshold.

Failure:

- non-monotone behavior would suggest the metric is poorly chosen or the family is not informative.

#### Test C2: low-mode vorticity truncation sweep

What is tested:

- approximate recovery error as the number of retained vorticity modes increases.

Why it matters:

- tests whether the branch captures stable approximate recovery rather than only exact/no-go extremes.

Success:

- error decays systematically with mode count.

Failure:

- if error does not improve with richer records, the chosen recovery architecture is likely wrong.

#### Test C3: linear protected-functional margin sweep

What is tested:

- for `M_epsilon = diag(1, epsilon)` or related horizon maps, estimate `alpha_{M,p}` and `kappa_{M,p}` as `epsilon -> 0`.

Why it matters:

- gives a minimal analytic benchmark for exact but unstable recovery.

Success:

- exact recoverability for `epsilon > 0`, instability as `epsilon -> 0`, no-go at `epsilon = 0` when the hidden direction affects `p`.

Failure:

- would indicate the metrics are not capturing the intended notion.

### Test family D: Asymptotic-recovery tests

#### Test D1: functional observer on LTI system

What is tested:

- whether a protected functional `Lx_t` can be reconstructed asymptotically from output history even when full state reconstruction is unnecessary.

Why it matters:

- this is the branch’s bridge to the asymptotic OCP side.

Success:

- observer error converges to zero when the unobservable subspace lies inside `ker L`.

Failure:

- convergence fails when that containment is violated.

Meaning:

- passing gives a serious dynamic recoverability lane.

### Test family E: Counterexample and edge-case tests

#### Test E1: exact-but-unstable example

Use a family where the map is injective but nearly singular.

Why it matters:

- distinguishes exact recoverability from usable recoverability.

#### Test E2: exact-on-family, impossible-on-ambient-space example

Use the qubit meridian family or a sparse-vector family.

Why it matters:

- confirms that family restriction is not an optional detail but a central structural choice.

#### Test E3: wrong protected variable test

Choose a protected variable that changes on hidden fibers.

Why it matters:

- this should force a no-go and prevent vague branch promotion.

---

## 10. Computational Experiment Designs

### Experiment 1: qubit record-collapse sweep

Setup:

- family `rho(theta) = |psi(theta)><psi(theta)|` on a meridian,
- observation map `M_eta(rho) = noisy Z-basis classical record`.

Variables:

- `theta in [0, pi]`,
- noise `eta in [0, 1/2]`.

Protected variable:

- `p(rho) = theta`.

Distance metric:

- absolute angle error `|theta - theta_hat|`.

Compute:

- exact inverse on the meridian family,
- empirical `kappa(delta)` and margin estimate as a function of `eta`.

Plots:

- reconstruction error versus `eta`,
- minimum separation between records of distinct `theta` values,
- explicit collapse at `eta = 1/2`.

Meaningful pattern:

- monotone deterioration with a clear threshold.

Weak/trivial pattern:

- if everything is either perfectly invertible or immediately impossible with no graded behavior, the branch metric is less interesting in this system.

### Experiment 2: periodic vorticity / divergence comparison

Setup:

- divergence-free periodic velocity fields with known Fourier coefficients.

Observation maps:

1. full vorticity,
2. truncated vorticity,
3. divergence only.

Protected variable:

- full divergence-free velocity field,
- or a chosen low-mode component.

Distance metric:

- `L2` field reconstruction error.

Parameter range:

- Fourier cutoff `K`,
- noise on observed modes.

Compute:

- reconstruction from vorticity,
- low-mode reconstruction error versus `K`,
- impossibility witness for divergence-only record.

Plots:

- error versus mode cutoff,
- before/after field comparisons,
- record-fiber collisions for divergence-only data.

Meaningful pattern:

- exact full recovery from full vorticity,
- systematic approximate improvement with more retained modes,
- total collapse for divergence-only.

### Experiment 3: protected-functional observability sweep

Setup:

- low-dimensional LTI systems,
- horizon map `M_T(x0)` or asymptotic functional observer.

Variables:

- sensor matrix `C`,
- horizon `T`,
- protected functional `L`,
- observation noise.

Compute:

- observability matrix rank on the protected quotient,
- restricted singular value / margin,
- observer reconstruction error over time.

Plots:

- margin versus sensor geometry,
- exact/no-go phase diagram in `(T, sensor choice)`,
- asymptotic error decay versus detectability gap.

Meaningful pattern:

- exact recovery once the horizon/sensor set separates the protected functional,
- sharp failure when the hidden mode survives in `ker L`.

### Experiment 4: simple linear collapse-modulus benchmark

Setup:

- `x in R^2`,
- `M_epsilon(x1, x2) = (x1, epsilon x2)`,
- `p(x) = x` or `p(x)=x2`.

Why include it:

- this is the simplest exact-but-unstable benchmark and should be solved analytically.

What to compute:

- `alpha_{M,p}` and `kappa_{M,p}` explicitly,
- reconstruction error under observation noise.

Meaningful pattern:

- exact recovery for `epsilon > 0`,
- stable constant collapsing as `epsilon -> 0`,
- no-go at `epsilon = 0` if `p` depends on `x2`.

This is not the flagship physics experiment, but it is the cleanest sanity-check benchmark for the branch metric.

---

## 11. What Would Count as a Real New Result?

### Trivial or already-known outcomes

These would **not** justify keeping the branch on their own:

- “observation can lose information”
- “non-invertible maps prevent recovery”
- “single-basis measurement cannot recover arbitrary qubit phase”
- “observability matters in control”
- “full vorticity carries more information than divergence only”

### Useful negative results

These are worth keeping if stated sharply:

- an explicit no-go showing that a record family cannot recover a protected variable even though it preserves some related constraint quantity,
- a theorem that exact recovery fails whenever hidden fibers change the protected variable,
- a threshold showing that coarse records collapse recoverability before any correction architecture can even begin.

### Minor but real contributions

Any of the following would be respectable:

- a protected-variable collapse metric with clean exact/no-go/stability interpretation,
- a quotient-based exact recovery criterion that is simple, reusable, and computationally checkable,
- a well-designed cross-domain benchmark suite showing the same metric classifies quantum, PDE, and observer examples sensibly.

### Stronger publishable-style contributions

These are the outcomes that would make the branch genuinely significant:

1. a nontrivial threshold theorem for a parameterized family of observation maps,
2. a sharp protected-functional no-go or sufficiency theorem not already standard in functional observability language,
3. a cross-domain exact/approximate/irrecoverable classification theorem with a metric that is not just cosmetic,
4. or a useful family-specific result in a standard physical system that existing literatures have not already stated in equivalent form.

### Honest risk

The most likely failure mode is that the branch never gets beyond repackaging:

- sufficiency,
- functional observability,
- inverse stability,
- and restricted recovery.

That is acceptable if the branch then yields a clean negative conclusion and does not get promoted too far.

---

## 12. Best Concrete Branch Design

### Working branch title

**Constrained-Observation Recoverability**

### Exact problem statement

Study when a constrained observation map `M` preserves enough information to recover a protected variable `p(x)` on an admissible family `A`, exactly, approximately, asymptotically, or not at all.

### Best theorem candidate

**Protected-variable collapse-modulus theorem**

Backbone claim:

- exact recoverability is equivalent to `kappa_{M,p}(0)=0`,
- irrecoverability follows when `kappa_{M,p}(0)>0`,
- and approximate-recovery quality is governed by the rate of decay of `kappa_{M,p}(delta)`.

This is probably not a major new theorem in full generality, but it is the strongest candidate for a branch-defining theorem framework.

### Best no-go candidate

**Fiber-collision no-go on protected variables**

If the observation fibers contain two admissible states with different protected values, then no exact recovery map from records to protected values can exist.

This is simple, but it becomes genuinely useful when paired with constructive fiber-collision witnesses in quantum, PDE, and control examples.

### Best computational experiment

**Periodic vorticity / divergence / low-mode sweep**

Why this is the strongest single experiment:

- it is physically standard,
- it links directly to the existing repository,
- it exhibits exact recovery, approximate recovery, and explicit no-go inside one family,
- and it avoids vague “measurement-disturbance” language.

### Best conventional comparison systems

1. qubit with constrained classical record,
2. periodic divergence-free velocity recovery from vorticity versus divergence only,
3. linear protected-functional recovery from observation streams.

### Best way it plugs into Protected-State Correction Theory

This branch should enter as an **observation-limited recoverability lane** with the following relationship to the current repo:

- the existing repo studies correction when the relevant structure is available,
- this branch studies whether the available record supports that structure at all,
- and it plugs into exact, asymptotic, and no-go architecture without replacing any of them.

### Why it is still useful even without a major theorem

Even if it does not produce a major new theorem, it can still be valuable if it yields:

- a disciplined observation-layer extension of the repo,
- good no-go results,
- better links to conventional literatures,
- and a clear explanation of when record-limited recovery questions are mathematically meaningful.

---

## 13. Repo Integration Plan

If this branch survives initial falsification, it should live under a dedicated lane such as:

- `docs/theory/advanced-directions/constrained-observation-recoverability.md`
- `docs/theorem-candidates/observation-recoverability-theorems.md`
- `docs/impossibility-results/observation-recoverability-no-go.md`
- `docs/applications/observation-recoverability-system-map.md`
- `src/ocp/observation_recoverability.py`
- `tests/math/test_observation_recoverability.py`

Possible workbench module if the branch survives:

- **Recoverability / Correction Studio**

with:

- qubit record-collapse module,
- PDE vorticity versus divergence module,
- linear observer / horizon module,
- collapse-modulus visualization.

This branch should **not** be promoted to the public front page until it survives the initial theorem/no-go and computational benchmark pass.

---

## 14. Honest Overall Assessment

### Strongest honest description right now

This is a **plausible branch**, not yet a proved new theory.

### What is already standard

- sufficiency and recoverability in statistics and quantum information,
- functional observability in control,
- stability/modulus ideas in inverse problems,
- restricted recovery on structured families in signal recovery.

### What still looks worth testing

- a protected-variable collapse metric and class structure,
- a quotient-based exact/no-go criterion adapted to protected variables,
- a strong PDE-side and quantum-side benchmark suite,
- and a dynamic asymptotic extension through functional observers.

### What would kill the branch cleanly

The branch should be demoted if, after the initial test program, all of the following are true:

- every theorem candidate is a transparent restatement of known sufficiency or observability results,
- the collapse metric adds no real clarity beyond standard inverse-stability language,
- the computational benchmarks show only obvious behavior,
- and no useful negative result sharper than generic non-invertibility emerges.

If that happens, the repo should keep only a short note linking existing OCP material to standard recoverability/observability literatures and should not promote this as a major new lane.

---

## 15. Recommended Next Action Sequence

1. **Formalize the static branch backbone first**
   - define `A`, `p`, `M`, `R`, `kappa_{M,p}`, and `alpha_{M,p}` cleanly
   - prove the factorization/no-go backbone in the simplest setting

2. **Run the three core toy systems**
   - qubit meridian / phase-loss
   - periodic vorticity versus divergence
   - linear protected-functional observability

3. **Estimate the collapse metric numerically**
   - especially under parameterized coarsening/noise
   - verify whether it really separates exact, unstable, approximate, and impossible regimes

4. **Decide whether the branch has real traction**
   - if the metric is just cosmetic, stop
   - if it gives clean thresholds or strong no-go structure, keep going

5. **Only then attempt stronger theorems**
   - family-specific threshold theorems
   - functional-observer asymptotic bridge theorems
   - or a PDE-side exact-versus-approximate classification result

6. **Do not promote the branch publicly until one of these happens**
   - a real theorem-level result appears,
   - a useful no-go is proved cleanly,
   - or the computational test program shows a genuinely informative collapse pattern across more than one system family.

---

## Bottom Line

The strongest honest branch is:

**Constrained-Observation Recoverability**

with the main objective:

> classify observation maps by their ability to recover a protected variable exactly, stably approximately, asymptotically, or not at all.

This is worth pursuing because it is:

- compatible with the current exact / asymptotic / no-go architecture,
- independently meaningful in conventional literatures,
- testable on standard quantum, PDE, and control examples,
- and narrow enough to survive skeptical review if it produces one strong metric, one strong no-go, or one strong threshold result.
