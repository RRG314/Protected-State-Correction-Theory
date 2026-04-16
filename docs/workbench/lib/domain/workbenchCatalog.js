export const LAB_META = {
  recoverability: {
    label: 'Structural Discovery Studio',
    short: 'Diagnose structural failure, identify the missing piece, and test a real fix.',
    branch: 'Constrained-observation branch',
    fit: 'Exact / approximate / asymptotic / impossible classification',
    status: 'ACTIVE RESEARCH BRANCH',
    lane: 'Observation and reconstruction',
    protected: 'Chosen protected variable p(x)',
    disturbance: 'Unseen ambiguity inside the observation fibers',
    correction: 'Recovery map R after constrained observation M',
    plain:
      'This studio turns the recoverability branch into a structural-discovery engine. It asks what you want to preserve, why the current architecture fails or partially fails, what is missing, and which change actually moves the system into a better regime.',
    technical:
      'Implements the constrained-observation recoverability branch as a structural-discovery studio. The module computes finite-sample collapse curves κ(δ), fiber-collision boundaries, restricted-linear sufficiency diagnostics, minimal augmentation suggestions, weaker-versus-stronger target splits, and before/after regime changes for analytic, quantum, periodic-flow, control-observer, and reusable linear-template examples.',
    use: 'Use this when you want to diagnose a failing setup, identify what structure is missing, test a minimal augmentation, compare before versus after, and decide whether to enrich the record, weaken the target, or switch architecture.',
    avoid: 'Do not treat loss of recoverability as a metaphysical statement. This branch is about operator-level information access and reconstruction limits.',
    refs: [
      { title: 'Structural Discovery overview', href: '../structural-discovery/overview.md', note: 'Capability overview and scope' },
      { title: 'Structural Discovery formalism', href: '../structural-discovery/formalism.md', note: 'Problem, failure, augmentation, and validation layers' },
      { title: 'Structural Discovery algorithms', href: '../structural-discovery/algorithms.md', note: 'Detection, augmentation, and redesign logic' },
      { title: 'Studio workflow', href: '../app/structural-discovery-studio.md', note: 'User-facing design path' },
    ],
    literature: [
      { title: 'Jenčová-Petz on quantum sufficiency', href: 'https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-263/issue-1/Sufficiency-in-quantum-statistical-inference/cmp/1143668799.full', note: 'Quantum recoverability anchor' },
      { title: 'Functional observability and subspace reconstruction', href: 'https://doi.org/10.1103/PhysRevResearch.4.043195', note: 'Control-side protected-functional anchor' },
      { title: 'Chorin projection-method foundation', href: 'https://doi.org/10.1090/S0025-5718-1968-0242392-2', note: 'Periodic constrained reconstruction anchor' },
    ],
  },
  benchmark: {
    label: 'Benchmark / Validation Console',
    short: 'Run validated demos, inspect branch health, and export reproducibility snapshots.',
    branch: 'Workbench validation layer',
    fit: 'Validated demos, benchmark cases, and evidence-level map',
    status: 'ACTIVE PRODUCT SURFACE',
    lane: 'Benchmarking and reproducibility',
    protected: 'Validated theorem-backed or benchmark-backed scenario behavior',
    disturbance: 'False positives, stale claims, or hidden regressions',
    correction: 'Recomputed demos, regression rows, and exportable snapshots',
    plain:
      'This console is the workbench’s trust surface. It gathers the built-in demos and benchmark cases, shows what changed before versus after, and makes it easy to export a reproducible snapshot instead of relying on memory or screenshots.',
    technical:
      'Aggregates the validated structural-discovery demos, module-health benchmark rows, and reproducibility exports into one console. This layer is about regression resistance and evidence visibility rather than new theorem claims.',
    use: 'Use this when you want a stable starting point, a regression check, or an exportable record of why a demo or branch result should be trusted.',
    avoid: 'Do not read this as a replacement for the repo-wide test gate. It is a live benchmark surface inside the workbench.',
    refs: [
      { title: 'Structural Discovery final report', href: '../structural-discovery/final-report.md', note: 'Capability status and limits' },
      { title: 'Structural Discovery validation', href: '../structural-discovery/validation.md', note: 'Validation surface and demo checks' },
      { title: 'Workbench overview', href: '../app/workbench-overview.md', note: 'Workbench-wide module map' },
    ],
    literature: [
      { title: 'Functional observability and subspace reconstruction', href: 'https://doi.org/10.1103/PhysRevResearch.4.043195', note: 'Benchmark anchoring on protected-function recovery' },
      { title: 'Chorin projection-method foundation', href: 'https://doi.org/10.1090/S0025-5718-1968-0242392-2', note: 'Classical benchmark anchor for constrained projection' },
      { title: 'Jenčová-Petz on quantum sufficiency', href: 'https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-263/issue-1/Sufficiency-in-quantum-statistical-inference/cmp/1143668799.full', note: 'Quantum-side recoverability anchor' },
    ],
  },
  mixer: {
    label: 'Discovery Mixer / Structural Composition Lab',
    short: 'Compose supported systems, detect conflicts, and test structural fixes before and after augmentation.',
    branch: 'Advanced composition lab',
    fit: 'Typed composition / theorem-backed where supported / explicit unsupported boundary',
    status: 'ADVANCED TOOL SURFACE',
    lane: 'Composable discovery and redesign',
    protected: 'Typed protected target chosen on a supported family',
    disturbance: 'Ambiguity, hidden support, rank deficiency, short history, or boundary mismatch',
    correction: 'Composition rules, diagnostics, augmentation search, and family-bounded redesign',
    plain:
      'This advanced lab lets you assemble supported systems out of typed building blocks, test whether the composition is coherent, see what blocks exact recovery, and compare the original design to the smallest supported fix.',
    technical:
      'Implements a typed discovery-mixer layer over the restricted-linear, periodic modal, diagonal/history, and bounded-domain benchmark families. The lab checks domain and basis compatibility, parses supported custom input, runs family-specific exactness and no-go diagnostics, proposes minimal supported augmentations, and keeps unsupported symbolic input explicit instead of pretending to solve it.',
    use: 'Use this when you want to build or stress-test a supported system family directly, enter custom linear or modal objects, or run seeded random exploration inside the engine’s validated structural rules.',
    avoid: 'Do not treat this as a general symbolic solver. It only accepts custom input that can be reduced into the supported typed families.',
    refs: [
      { title: 'Discovery Mixer overview', href: '../discovery-mixer/overview.md', note: 'Scope, modes, and supported families' },
      { title: 'Discovery Mixer supported scope', href: '../discovery-mixer/supported-scope.md', note: 'What custom input is actually supported' },
      { title: 'Discovery Mixer diagnostics guide', href: '../discovery-mixer/diagnostics-guide.md', note: 'How compatibility and failure messages are produced' },
      { title: 'Discovery Mixer developer guide', href: '../discovery-mixer/developer-reference.md', note: 'Typed object model and engine wiring' },
    ],
    literature: [
      { title: 'MathWorks on observability and state estimation workflows', href: 'https://www.mathworks.com/help/control/ug/observer-design-for-a-mass-spring-damper-system.html', note: 'Control-tool interface pattern anchor' },
      { title: 'Best practices for scientific computing', href: 'https://doi.org/10.1371/journal.pbio.1001745', note: 'Reproducibility and validation discipline' },
      { title: 'Functional observability and subspace reconstruction', href: 'https://doi.org/10.1103/PhysRevResearch.4.043195', note: 'Protected-functional benchmark anchor' },
    ],
  },
  exact: {
    label: 'Exact Projection Lab',
    short: 'Orthogonal exact recovery and overlap failure.',
    branch: 'Exact branch',
    fit: 'Exact fit',
    status: 'PROVED / NO-GO',
    lane: 'Finite-dimensional anchor',
    protected: 'Protected subspace S',
    disturbance: 'Orthogonal disturbance direction D',
    correction: 'Orthogonal projector P_S',
    plain:
      'This is the smallest exact correction model in the repo. When the disturbance is truly orthogonal to the protected direction, projection recovers the protected component exactly. When overlap is introduced, the same operator becomes a clean counterexample.',
    technical:
      'Implements the finite-dimensional direct-sum model H = S ⊕ D with recovery R = P_S. The angle control lets the example move outside the admissible OCP hypotheses and turns the module into a witness for OCP-T1 versus OCP-N1.',
    use: 'Use this to understand the clean exact theorem and the sharp overlap failure in the simplest possible setting.',
    avoid: 'Do not treat non-orthogonal cases as exact protected-state correction systems.',
    refs: [
      { title: 'Central theorem', href: '../theorem-candidates/central-theorem.md', note: 'Exact projector recovery' },
      { title: 'No-go spine', href: '../impossibility-results/no-go-results.md', note: 'Overlap / indistinguishability no-go' },
      { title: 'Operator spine', href: '../finalization/operator-spine-final.md', note: 'Projector-based correction language' },
    ],
    literature: [
      { title: 'Chorin projection-method anchor', href: 'https://doi.org/10.1090/S0025-5718-1968-0242392-2', note: 'Classical exact projection in PDE settings' },
    ],
  },
  qec: {
    label: 'QEC Sector Lab',
    short: '3-qubit bit-flip code in exact sector language.',
    branch: 'Exact sector branch',
    fit: 'Exact fit / standard-anchor reinterpretation',
    status: 'PROVED / CONDITIONAL ANCHOR',
    lane: 'Quantum information anchor',
    protected: 'Code space / logical state',
    disturbance: 'Correctable syndrome sectors',
    correction: 'Sector projectors and recovery family',
    plain:
      'This module treats QEC as the exact sector branch. The code space is what must be preserved, each bit-flip sector is a disturbance sector, and recovery works because the sectors stay distinguishable and can be mapped back without changing the logical information.',
    technical:
      'Implements the 3-qubit bit-flip sector model using orthogonal sector bases and a sector-conditioned recovery operator. The exact statement here is branch-specific: the repo is re-framing standard QEC structure, not replacing it.',
    use: 'Use this when you want the strongest exact anchor beyond the simple projector model.',
    avoid: 'Do not read this as a new QEC theorem. The value here is the protected-state correction framing.',
    refs: [
      { title: 'QEC in protected-state language', href: '../qec/qec-in-ocp.md', note: 'Protected space, sectors, and recovery' },
      { title: 'Sector recovery theorem', href: '../theorem-candidates/sector-recovery-theorems.md', note: 'Exact orthogonal sector recovery' },
      { title: 'QEC foundations', href: '../qec/qec-foundations.md', note: 'Knill-Laflamme and syndrome structure' },
    ],
    literature: [
      { title: 'Knill-Laflamme foundation', href: 'https://arxiv.org/abs/quant-ph/9604034', note: 'Foundational exact correction anchor' },
      { title: 'Continuous-QEC bridge', href: 'https://doi.org/10.1103/PhysRevA.65.042301', note: 'Useful next-step literature' },
    ],
  },
  mhd: {
    label: 'MHD Projection Lab',
    short: 'Exact periodic projection versus GLM damping.',
    branch: 'Exact and asymptotic comparison',
    fit: 'Exact fit + asymptotic comparator',
    status: 'PROVED / CONDITIONAL',
    lane: 'Fluid / MHD physics',
    protected: 'Divergence-free field component',
    disturbance: 'Gradient contamination / divergence error',
    correction: 'Helmholtz/Leray projector versus GLM cleaning',
    plain:
      'This module is the clearest continuous-system split in the repo. Exact projection removes the divergence-producing component in one shot for the periodic model, while GLM only reduces it gradually.',
    technical:
      'Builds a periodic field B = B_phys + grad(phi), applies the exact discrete Helmholtz-style projector, and compares it to a short GLM evolution. The exact branch is projection-based; the GLM branch is asymptotic and should not be promoted as exact.',
    use: 'Use this when you want the cleanest continuous exact-versus-asymptotic comparison.',
    avoid: 'Do not read the GLM side as an exact projector or assume the periodic result automatically extends to bounded domains.',
    refs: [
      { title: 'Divergence cleaning in protected-state language', href: '../mhd/divergence-cleaning-in-ocp.md', note: 'Exact Leray / Helmholtz anchor' },
      { title: 'GLM and asymptotic correction', href: '../mhd/glm-and-asymptotic-correction.md', note: 'Asymptotic branch and limits' },
      { title: 'Exact vs asymptotic split', href: '../formalism/exact-vs-asymptotic.md', note: 'Why the distinction matters' },
    ],
    literature: [
      { title: 'Dedner et al. on hyperbolic divergence cleaning', href: 'https://doi.org/10.1006/jcph.2001.6961', note: 'Asymptotic cleaning anchor' },
      { title: 'Evans-Hawley constrained transport', href: 'https://www.sciencedirect.com/science/article/pii/0021999188901209', note: 'Constraint-preserving MHD direction' },
    ],
  },
  cfd: {
    label: 'CFD Projection Lab',
    short: 'Periodic incompressible projection and bounded-domain limits.',
    branch: 'CFD extension',
    fit: 'Exact fit on the periodic branch / conditional bounded-domain extension',
    status: 'KEPT CFD EXTENSION / NO-GO LIMIT',
    lane: 'Incompressible CFD',
    protected: 'Divergence-free velocity field',
    disturbance: 'Non-solenoidal velocity contamination',
    correction: 'Pressure projection / Helmholtz-Hodge projector',
    plain:
      'This module is the narrow CFD lane that genuinely fits the theory. On the periodic branch, projection recovers the divergence-free velocity exactly. On bounded domains, the same idea becomes boundary-sensitive: the repo now has a restricted exact bounded Hodge subcase in the docs, while the live lab still focuses on the counterexample and no-go side so the limits stay visible.',
    technical:
      'Computes a periodic velocity decomposition u = u_df + grad(phi), applies the exact projector, and then compares that exact branch to a bounded-domain counterexample and a divergence-only no-go witness. The live lab emphasizes the negative bounded-domain checks; the positive boundary-compatible finite-mode Hodge theorem is linked in the docs. The point is to separate real projector fits from boundary-insensitive overreach.',
    use: 'Use this to understand where incompressible projection methods genuinely fit the protected-state correction framework and where the fit becomes conditional or fails.',
    avoid: 'Do not read this as a theorem about all CFD solvers. It is a narrow statement about projection-compatible incompressible correction architectures.',
    refs: [
      { title: 'Incompressible projection in protected-state language', href: '../cfd/incompressible-projection.md', note: 'Main CFD entry point' },
      { title: 'Bounded versus periodic projection', href: '../cfd/bounded-vs-periodic-projection.md', note: 'Boundary-sensitive scope control' },
      { title: 'Bounded-domain Hodge theorems', href: '../theorem-candidates/bounded-domain-hodge-theorems.md', note: 'Restricted exact bounded-domain subcase' },
      { title: 'CFD projection results', href: '../theorem-candidates/cfd-projection-results.md', note: 'Corollary and no-go layer' },
    ],
    literature: [
      { title: 'Chorin projection-method foundation', href: 'https://doi.org/10.1090/S0025-5718-1968-0242392-2', note: 'Classical incompressible projection anchor' },
      { title: 'Brown-Cortez-Minion on accurate projection methods', href: 'https://www.sciencedirect.com/science/article/pii/S0021999101967154', note: 'Boundary and pressure-correction context' },
      { title: 'Guermond-Minev-Shen overview', href: 'https://doi.org/10.1016/j.cma.2005.10.010', note: 'Broader projection-method literature' },
    ],
  },
  gauge: {
    label: 'Gauge Projection Lab',
    short: 'Transverse projection for Maxwell / Coulomb-gauge structure.',
    branch: 'Exact physics extension',
    fit: 'Exact fit on projection-compatible domains',
    status: 'KEPT PHYSICS EXTENSION',
    lane: 'Maxwell / gauge physics',
    protected: 'Transverse field or vector-potential component',
    disturbance: 'Longitudinal / pure-gradient component',
    correction: 'Transverse projector P_perp',
    plain:
      'This module shows the strongest additional physics bridge kept in the repo. It uses the same exact projector logic as the MHD periodic branch, but interprets the protected object as the transverse piece of a Maxwell-side field or vector potential.',
    technical:
      'Computationally this reuses the projection-compatible exact branch. The physics content is the Coulomb-gauge or transverse projection interpretation. It is a real operator-level fit, but not a new theorem beyond the existing exact projection spine.',
    use: 'Use this to see where the theory really reaches into additional physics without forcing a new universal claim.',
    avoid: 'Do not sell this as a new Maxwell theorem. It is a principled physics extension of the exact projector branch.',
    refs: [
      { title: 'Maxwell / Coulomb-gauge note', href: '../physics/maxwell-coulomb-gauge.md', note: 'Fit verdict and scope' },
      { title: 'Physics system matrix', href: '../physics/physics-system-matrix.md', note: 'Where this bridge sits' },
      { title: 'Kept vs rejected physics bridges', href: '../physics/kept-vs-rejected-physics-bridges.md', note: 'Why this one survives' },
    ],
    literature: [
      { title: 'Constraint-preserving Maxwell FEM', href: 'https://doi.org/10.1016/j.jcp.2019.109340', note: 'Operator-level Maxwell direction' },
      { title: 'Maxwell-case constraint remedy', href: 'https://arxiv.org/abs/gr-qc/0404036', note: 'Constraint-preserving evolution context' },
    ],
  },
  continuous: {
    label: 'Continuous Generator Lab',
    short: 'Invariant-split flows, spectral damping, and mixing failure.',
    branch: 'Asymptotic generator branch',
    fit: 'Asymptotic fit',
    status: 'PROVED / NO-GO',
    lane: 'Generator classification',
    protected: 'ker(K) or invariant protected coordinates',
    disturbance: 'Stable disturbance subspace',
    correction: 'Damping or invariant-split generator K',
    plain:
      'This module shows the strongest asymptotic theorem spine in the repo. Some generators preserve the protected coordinates and damp the disturbance coordinates. Others look stable overall but fail because they mix disturbance back into the protected part.',
    technical:
      'Computes the kernel-based protected space, an orthogonal disturbance complement, an RK4 flow path, the mixing norm ||P_S K P_D||, and the finite-time exact-recovery residual. This is where the theory draws the hard line between asymptotic correction and exact one-shot recovery.',
    use: 'Use this to test whether a linear correction generator actually qualifies as a protected-state correction flow.',
    avoid: 'Do not treat every dissipative matrix as a valid correction flow. Decay alone is not enough.',
    refs: [
      { title: 'Generator theorems', href: '../theorem-candidates/generator-theorems.md', note: 'Invariant-split and PSD results' },
      { title: 'Advanced no-go results', href: '../impossibility-results/advanced-no-go-results.md', note: 'Finite-time exact-recovery boundary' },
      { title: 'Worked linear example', href: '../control/worked-linear-example.md', note: 'Clean invariant-split control picture' },
    ],
    literature: [
      { title: 'Constraint damping in Z4 / harmonic gauge', href: 'https://arxiv.org/abs/gr-qc/0504114', note: 'Strong asymptotic physics lane' },
      { title: 'Continuous QEC / feedback', href: 'https://doi.org/10.1103/PhysRevA.65.042301', note: 'Potential future bridge' },
    ],
  },
  nogo: {
    label: 'No-Go Explorer',
    short: 'Failure modes the theory can actually rule out.',
    branch: 'No-go boundary layer',
    fit: 'Structural rejection layer',
    status: 'PROVED BOUNDARY LAYER',
    lane: 'Failure diagnostics',
    protected: 'Whatever the candidate architecture claims to preserve',
    disturbance: 'Ambiguous, overlapping, or unreachable disturbance families',
    correction: 'Counterexample, obstruction, or impossibility witness',
    plain:
      'The negative-results layer is part of the theory, not an appendix. These examples show when exact recovery is impossible, when sector detection collapses, when correction image is too small, and when smooth flows cannot do exact one-shot recovery.',
    technical:
      'Each preset is wired to a specific theorem, counterexample, or theorem-grade obstruction in the repository. The point is to make failure structural and inspectable rather than rhetorical.',
    use: 'Use this to understand what the framework excludes and why those exclusions matter.',
    avoid: 'Do not hide these cases. The no-go layer is one of the strongest outputs of the repo.',
    refs: [
      { title: 'No-go spine', href: '../finalization/no-go-spine-final.md', note: 'Finalized impossibility layer' },
      { title: 'Advanced no-go results', href: '../impossibility-results/advanced-no-go-results.md', note: 'Sharper flow and sector boundaries' },
      { title: 'Kept vs rejected physics bridges', href: '../physics/kept-vs-rejected-physics-bridges.md', note: 'Physics-side demotions and rejections' },
    ],
    literature: [
      { title: 'Constraint-preserving vs damped systems', href: 'https://doi.org/10.1088/1361-6382/ac88af', note: 'Useful scope-control anchor' },
    ],
  },
};

export const CONTINUOUS_PRESETS = {
  invariant: {
    matrix: [
      [0, 0, 0],
      [0, 1, 1],
      [0, 0, 1.5],
    ],
    x0: [2, -1, 0.5],
  },
  psd: {
    matrix: [
      [0, 0, 0],
      [0, 0.75, 0],
      [0, 0, 2],
    ],
    x0: [3, -4, 1],
  },
  mixing: {
    matrix: [
      [0, 1],
      [0, 1],
    ],
    x0: [0, 1],
  },
};

export const STRUCTURAL_DISCOVERY_PRESETS = {
  periodic_modal_repair: {
    label: 'Periodic modal repair',
    patch: {
      system: 'periodic',
      studioMode: 'guided',
      periodicObservation: 'cutoff_vorticity',
      periodicProtected: 'full_weighted_sum',
      periodicCutoff: 3,
      periodicDelta: 2,
    },
  },
  control_history_repair: {
    label: 'Control history repair',
    patch: {
      system: 'control',
      studioMode: 'guided',
      controlMode: 'diagonal_threshold',
      controlProfile: 'three_active',
      controlFunctional: 'second_moment',
      controlHorizon: 2,
      controlDelta: 0.5,
    },
  },
  weaker_vs_stronger_split: {
    label: 'Weaker vs stronger target',
    patch: {
      system: 'qubit',
      studioMode: 'guided',
      qubitProtected: 'bloch_vector',
      qubitPhaseWindowDeg: 30,
      qubitDelta: 0.2,
    },
  },
  linear_measurement_repair: {
    label: 'Restricted-linear repair',
    patch: {
      system: 'linear',
      studioMode: 'guided',
      linearTemplate: 'sensor_basis',
      linearProtected: 'x3',
      linearDelta: 1.0,
      linearMeasurements: {
        measure_x1: true,
        measure_x2_plus_x3: true,
        measure_x2: false,
        measure_x3: false,
        measure_x1_plus_x2: false,
      },
    },
  },
  boundary_architecture_repair: {
    label: 'Boundary architecture repair',
    patch: {
      system: 'boundary',
      studioMode: 'guided',
      boundaryArchitecture: 'periodic_transplant',
      boundaryProtected: 'bounded_velocity_class',
      boundaryGridSize: 17,
      boundaryDelta: 0.2,
    },
  },
};

export const QUICKSTARTS = [
  {
    id: 'discover-structure',
    title: 'Discover missing structure',
    body: 'Open the Structural Discovery Studio on a failing boundary-sensitive case and let the workbench identify the missing architecture.',
    action: { type: 'preset', preset: 'boundary_architecture_repair' },
  },
  {
    id: 'test-recoverability',
    title: 'Test recoverability',
    body: 'Jump straight into the theorem-linked diagnosis flow for protected variables under constrained records.',
    action: { type: 'lab', lab: 'recoverability' },
  },
  {
    id: 'compare-exact-asymptotic',
    title: 'Compare exact vs asymptotic',
    body: 'Use the MHD / continuous lanes to see when one-shot correction is real and when only asymptotic suppression survives.',
    action: { type: 'lab', lab: 'mhd' },
  },
  {
    id: 'inspect-no-go',
    title: 'Inspect no-go boundaries',
    body: 'Open explicit failure witnesses instead of guessing why a naive correction strategy breaks.',
    action: { type: 'lab', lab: 'nogo' },
  },
  {
    id: 'run-benchmarks',
    title: 'Run built-in benchmarks',
    body: 'Open the benchmark console to compare validated demo scenarios, module health, and exportable reproducibility snapshots.',
    action: { type: 'lab', lab: 'benchmark' },
  },
  {
    id: 'open-template',
    title: 'Open linear template',
    body: 'Start from a reusable restricted-linear recovery problem with exact minimal augmentation logic.',
    action: { type: 'preset', preset: 'linear_measurement_repair' },
  },
  {
    id: 'compose-system',
    title: 'Compose a supported system',
    body: 'Open the Discovery Mixer to assemble a typed system family, test compatibility, and search for the smallest supported fix.',
    action: { type: 'lab', lab: 'mixer' },
  },
];

