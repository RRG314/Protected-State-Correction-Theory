export const LATEST_VALIDATION_SNAPSHOT = {
  "generatedAt": "2026-04-16T01:00:09.761Z",
  "readiness": {
    "knownCaseValidation": true,
    "guidedDiscovery": true,
    "unsupportedFreeExploration": false
  },
  "counts": {
    "qualifiedModules": 11,
    "knownAnswerPassed": 25,
    "knownAnswerTotal": 25,
    "workflowPassed": 10,
    "workflowTotal": 10,
    "adversarialPassed": 7,
    "adversarialTotal": 7
  },
  "limitations": [
    "Unsupported free-form symbolic systems are still outside the validated scope and must be rejected rather than approximated.",
    "Some artifact-consistency checks remain intentionally marked as partial because they recompute outputs from the same implementation family.",
    "Family-specific thresholds remain family-specific; this pass does not convert them into universal theorems."
  ],
  "moduleHealth": [
    {
      "label": "Exact Projection Lab",
      "scenario": "orthogonal exact recovery",
      "verdict": "exact",
      "qualification": "qualified-narrow",
      "notes": "Exact theorem anchor is working and export/report state is coherent, but this lab is intentionally narrow and does not expose unsupported free-form input."
    },
    {
      "label": "QEC Sector Lab",
      "scenario": "three-qubit bit-flip exact sector recovery",
      "verdict": "exact",
      "qualification": "qualified-narrow",
      "notes": "Known exact anchor reproduces correctly; this lab is trustworthy for the tracked sector example but not yet a broad QEC explorer."
    },
    {
      "label": "MHD Projection Lab",
      "scenario": "periodic projection versus short GLM run",
      "verdict": "exact-vs-asymptotic split",
      "qualification": "qualified",
      "notes": "Real numerical comparison is present and the exact-versus-GLM gap is preserved."
    },
    {
      "label": "CFD Projection Lab",
      "scenario": "periodic exact branch plus bounded transplant failure",
      "verdict": "mixed exact and no-go",
      "qualification": "qualified",
      "notes": "This lab is trustworthy for both the periodic exact anchor and the bounded-domain negative benchmark."
    },
    {
      "label": "Gauge / Maxwell Lab",
      "scenario": "transverse projection fit",
      "verdict": "exact fit on compatible domain",
      "qualification": "qualified-narrow",
      "notes": "The lab behaves correctly on the kept projection-compatible example, but it remains an anchor surface rather than a broad discovery tool."
    },
    {
      "label": "Continuous Generator Lab",
      "scenario": "invariant-split asymptotic correction with finite-time no-go",
      "verdict": "asymptotic only",
      "qualification": "qualified",
      "notes": "The lab correctly distinguishes asymptotic suppression from impossible finite-time exact recovery."
    },
    {
      "label": "No-Go Explorer",
      "scenario": "bounded-domain transplant failure witness",
      "verdict": "COUNTEREXAMPLE / REJECTED BRIDGE",
      "qualification": "qualified",
      "notes": "No-Go Explorer is trustworthy for explicit counterexamples and does not invent fixes for structurally rejected setups."
    },
    {
      "label": "Recoverability / Observation Studio",
      "scenario": "periodic stronger-target threshold failure",
      "verdict": "Impossible",
      "qualification": "qualified",
      "notes": "The recoverability studio is trustworthy for theorem-backed and family-backed threshold cases and keeps fix cards tied to real comparisons."
    },
    {
      "label": "Structural Discovery Studio",
      "scenario": "wrong architecture on bounded-domain protected class",
      "verdict": "Impossible",
      "qualification": "qualified",
      "notes": "This is currently the strongest end-to-end diagnosis-to-repair workflow in the workbench."
    },
    {
      "label": "Discovery Mixer / Structural Composition Lab",
      "scenario": "typed restricted-linear failure, repair, and unsupported nonlinear rejection",
      "verdict": "Impossible",
      "qualification": "qualified",
      "notes": "The mixer is strong enough for supported typed composition and explicit unsupported handling; it is not a free symbolic sandbox."
    },
    {
      "label": "Benchmark / Validation Console",
      "scenario": "validated demo replay and module-health export",
      "verdict": "Validated benchmark surface",
      "qualification": "qualified",
      "notes": "Benchmark console exports real demo rows and module-health summaries."
    }
  ]
};
