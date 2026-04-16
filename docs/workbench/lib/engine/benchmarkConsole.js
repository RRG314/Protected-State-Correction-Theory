import { LATEST_VALIDATION_SNAPSHOT, emptyValidationSnapshot } from '../data/validationSnapshot.js';
import { analyzeExactProjection, analyzeQecSector } from './exactLabs.js';
import { analyzeRecoverability, mergeRecoverabilityConfig } from './recoverabilityEngine.js';
import { analyzeMhdProjection, analyzeCfdProjection, analyzeGaugeProjection } from './physicsEngine.js';
import { analyzeContinuousGenerator } from './continuousEngine.js';
import { analyzeNoGo } from './noGoEngine.js';

export function analyzeBenchmarkConsole(config = {}) {
  const validationSnapshot = LATEST_VALIDATION_SNAPSHOT ?? emptyValidationSnapshot();
  const snapshotByLabel = new Map(
    (validationSnapshot.moduleHealth ?? []).map((row) => [row.label, row])
  );
  const mhdBenchmark = analyzeMhdProjection({ gridSize: 12, contamination: 0.22, glmSteps: 8, frame: 8, poissonIterations: 320, dt: 0.05, ch: 1, cp: 1 });
  const cfdBenchmark = analyzeCfdProjection({ periodicGridSize: 12, boundedGridSize: 18, contamination: 0.22, poissonIterations: 320 });
  const gaugeBenchmark = analyzeGaugeProjection({ gridSize: 12, contamination: 0.18, glmSteps: 8, frame: 8, poissonIterations: 320, dt: 0.05, ch: 1, cp: 1 });
  const continuousBenchmark = analyzeContinuousGenerator({ matrix: [[0, 0, 0], [0, 1, 1], [0, 0, 1.5]], x0: [2, -1, 0.5], time: 2, steps: 280, frame: 280 });
  const recoverabilityBenchmark = analyzeRecoverability({
    system: 'periodic',
    periodicObservation: 'cutoff_vorticity',
    periodicProtected: 'full_weighted_sum',
    periodicCutoff: 3,
    periodicDelta: 2,
  });
  const structuralBenchmark = analyzeRecoverability({
    system: 'boundary',
    boundaryArchitecture: 'periodic_transplant',
    boundaryProtected: 'bounded_velocity_class',
    boundaryGridSize: 17,
    boundaryDelta: 0.2,
  });
  const noGoBenchmark = analyzeNoGo({ example: 'boundary' });
  const demoConfigs = {
    periodic_modal_repair: {
      label: 'Periodic modal augmentation',
      config: {
        system: 'periodic',
        periodicObservation: 'cutoff_vorticity',
        periodicProtected: 'full_weighted_sum',
        periodicCutoff: 3,
        periodicDelta: 2,
      },
    },
    control_history_repair: {
      label: 'Control history augmentation',
      config: {
        system: 'control',
        controlMode: 'diagonal_threshold',
        controlProfile: 'three_active',
        controlFunctional: 'second_moment',
        controlHorizon: 2,
        controlDelta: 0.5,
      },
    },
    weaker_vs_stronger_split: {
      label: 'Weaker-versus-stronger split',
      config: {
        system: 'qubit',
        qubitProtected: 'bloch_vector',
        qubitPhaseWindowDeg: 30,
        qubitDelta: 0.2,
      },
    },
    boundary_architecture_repair: {
      label: 'Boundary architecture repair',
      config: {
        system: 'boundary',
        boundaryArchitecture: 'periodic_transplant',
        boundaryProtected: 'bounded_velocity_class',
        boundaryGridSize: 17,
        boundaryDelta: 0.2,
      },
    },
    linear_measurement_repair: {
      label: 'Restricted-linear measurement repair',
      config: {
        system: 'linear',
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
  };

  const demoRows = Object.entries(demoConfigs).map(([key, entry]) => {
    const before = analyzeRecoverability(entry.config);
    const fix = before.chosenRecommendation ?? before.recommendations?.find((item) => item.availableInStudio);
    const after = fix?.patch ? analyzeRecoverability(mergeRecoverabilityConfig(entry.config, fix.patch), 1) : before;
    return {
      demo: key,
      label: entry.label,
      family: before.systemLabel,
      beforeRegime: before.status,
      afterRegime: after.status,
      metricName: entry.config.system === 'boundary' ? 'boundary mismatch' : 'κ(0)',
      metricBefore: entry.config.system === 'boundary' ? before.transplantBoundaryMismatch : before.kappa0,
      metricAfter: entry.config.system === 'boundary'
        ? (after.boundaryArchitecture === 'boundary_compatible_hodge' ? after.compatibleRecoveryError : after.kappa0)
        : after.kappa0,
      fixTitle: fix?.title ?? 'keep current',
      theoremStatus: before.theoremStatus,
      regimeChanged: before.status !== after.status,
    };
  });

  const moduleRows = [
    {
      label: 'Exact Projection Lab',
      verdict: analyzeExactProjection({ protectedMagnitude: 1.4, disturbanceMagnitude: 0.9, angleDeg: 90 }).admissible ? 'exact' : 'recheck',
      evidence: 'theorem-backed exact anchor',
      trust: 'qualified-narrow',
    },
    {
      label: 'QEC Sector Lab',
      verdict: analyzeQecSector({ alpha: 1, beta: 1, errorIndex: 2 }).exact ? 'exact' : 'recheck',
      evidence: 'standard-anchor exact sector reinterpretation',
      trust: 'qualified-narrow',
    },
    {
      label: 'MHD Projection Lab',
      verdict: mhdBenchmark.afterExactNorm < mhdBenchmark.afterGlmNorm ? 'exact-vs-asymptotic split' : 'recheck',
      evidence: 'validated continuous exact / asymptotic split',
      trust: 'qualified',
    },
    {
      label: 'CFD Projection Lab',
      verdict: cfdBenchmark.boundedTransplantFails ? 'narrow exact + boundary limit' : 'recheck',
      evidence: 'periodic exact branch plus bounded no-go / restricted exact subcase',
      trust: 'qualified',
    },
    {
      label: 'Gauge Projection Lab',
      verdict: gaugeBenchmark.afterExactGaugeNorm < gaugeBenchmark.beforeGaugeNorm ? 'exact-fit benchmark' : 'recheck',
      evidence: 'transverse / longitudinal split on the projection-compatible benchmark',
      trust: 'qualified-narrow',
    },
    {
      label: 'Continuous Generator Lab',
      verdict: continuousBenchmark.finiteTimeExactRecoveryPossible ? 'recheck' : 'asymptotic only',
      evidence: 'validated finite-time no-go boundary',
      trust: 'qualified',
    },
    {
      label: 'Recoverability / Observation Studio',
      verdict: recoverabilityBenchmark.impossible && recoverabilityBenchmark.chosenRecommendation ? 'threshold diagnosis + minimal fix' : 'recheck',
      evidence: 'family-backed threshold studio with theorem-linked comparison output',
      trust: 'qualified',
    },
    {
      label: 'Structural Discovery Studio',
      verdict: structuralBenchmark.impossible && structuralBenchmark.comparison?.afterRegime === 'exact' ? 'diagnosis-to-repair workflow' : 'recheck',
      evidence: 'architecture mismatch diagnosis with validated before/after repair',
      trust: 'qualified',
    },
    {
      label: 'Discovery Mixer / Structural Composition Lab',
      verdict: 'typed composition and supported repair search',
      evidence: 'typed composition, custom-input rejection, and supported-family repair workflow',
      trust: 'qualified',
    },
    {
      label: 'No-Go Explorer',
      verdict: noGoBenchmark.status === 'COUNTEREXAMPLE / REJECTED BRIDGE' ? 'explicit counterexample surface' : 'recheck',
      evidence: 'kept no-go witness with no fake repair path',
      trust: 'qualified',
    },
    {
      label: 'Benchmark / Validation Console',
      verdict: 'validation-facing surface',
      evidence: 'generated trust snapshot, demo replay, and export/regression summary',
      trust: 'qualified',
    },
  ].map((row) => {
    const snapshot = snapshotByLabel.get(row.label);
    return {
      ...row,
      trust: snapshot?.qualification ?? row.trust,
      notes: snapshot?.notes ?? '',
      scenario: snapshot?.scenario ?? null,
    };
  });

  const selectedDemo = config.selectedDemo && demoRows.some((row) => row.demo === config.selectedDemo)
    ? config.selectedDemo
    : demoRows[0].demo;
  const selectedDemoRow = demoRows.find((row) => row.demo === selectedDemo);

  return {
    title: 'Benchmark and validation console',
    status: 'Validated benchmark surface',
    suite: config.suite ?? 'all',
    selectedDemo,
    selectedDemoRow,
    demoRows,
    moduleRows,
    validationSnapshot,
    summary: {
      demoCount: demoRows.length,
      regimeChangeCount: demoRows.filter((row) => row.regimeChanged).length,
      exactAfterCount: demoRows.filter((row) => row.afterRegime === 'Exact').length,
      moduleCount: moduleRows.length,
    },
  };
}

