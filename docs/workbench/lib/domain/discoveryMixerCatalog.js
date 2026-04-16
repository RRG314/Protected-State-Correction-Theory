export const DIAGONAL_EIGENVALUES = [0.95, 0.8, 0.65, 0.5];

export const DISCOVERY_MIXER_LIBRARY = {
  structuredFamilies: {
    linear: {
      label: 'Restricted-linear family',
      status: 'theorem-backed restricted-linear branch',
      note: 'Exact row-space logic, collision gaps, and minimal augmentation search are supported.',
    },
    periodic: {
      label: 'Periodic modal family',
      status: 'family-specific validated branch',
      note: 'Support and cutoff threshold analysis is supported on the finite modal basis.',
    },
    control: {
      label: 'Diagonal/history family',
      status: 'family-specific validated branch',
      note: 'Finite-history thresholds and same-record target splits are supported on the diagonal finite-history family.',
    },
    boundary: {
      label: 'Bounded-domain architecture benchmark',
      status: 'restricted exact bounded-domain branch',
      note: 'Architecture compatibility and boundary mismatch checks are supported on the current bounded-domain benchmark family.',
    },
  },
  customFamilies: {
    linear: 'Matrix rows or linear expressions in x1..xn',
    periodic: 'Linear functionals in a1..a4 on the supported periodic basis',
    control: 'Diagonal sensor profiles plus moment(k), xi, or linear-function targets in x1..xn',
  },
  randomFamilies: {
    linear: 'Random restricted-linear record subsets and protected targets',
    periodic: 'Random periodic modal functionals and cutoffs',
    control: 'Random diagonal sensor profiles and finite-history targets',
  },
};

export const DISCOVERY_MIXER_DEMOS = {
  periodic_builder: {
    label: 'User-built periodic failure and fix',
    mode: 'structured',
    family: 'periodic',
    patch: {
      structuredPeriodicProtected: 'full_weighted_sum',
      structuredPeriodicObservation: 'cutoff_vorticity',
      structuredPeriodicCutoff: 3,
      structuredDelta: 2,
    },
  },
  control_builder: {
    label: 'User-built control history failure and fix',
    mode: 'structured',
    family: 'control',
    patch: {
      structuredControlProfile: 'three_active',
      structuredControlFunctional: 'second_moment',
      structuredControlHorizon: 2,
      structuredDelta: 0.5,
    },
  },
  weaker_stronger: {
    label: 'Weaker-versus-stronger target discovery',
    mode: 'custom',
    family: 'periodic',
    patch: {
      customFamily: 'periodic',
      customPeriodicFunctionalText: 'a1 + a2 + a4',
      customPeriodicObservation: 'cutoff_vorticity',
      customPeriodicCutoff: 2,
      customDelta: 2,
    },
  },
  custom_matrix: {
    label: 'Custom matrix / functional input',
    mode: 'custom',
    family: 'linear',
    patch: {
      customFamily: 'linear',
      customLinearDimension: 3,
      customLinearObservationText: 'x1\nx2 + x3',
      customLinearProtectedText: 'x3',
      customLinearCandidateText: 'x2\nx3\nx1 + x2',
      customDelta: 1,
    },
  },
  random_search: {
    label: 'Structured randomized search',
    mode: 'random',
    family: 'linear',
    patch: {
      randomFamily: 'linear',
      randomSeed: 37,
      randomObjective: 'failure',
      randomTrials: 16,
    },
  },
};
