# Two-Lane Audit Summary

- structurally sound and functioning: lower-level theorem kernels, browser-qualified supported workflows, benchmark trust snapshot, explicit unsupported rejection on advanced surfaces
- structurally messy but functioning: workbench shell and analysis layer, especially [app.js](../workbench/app.js) and [compute.js](../workbench/lib/compute.js)
- structurally clean but functionally weak: none of the audited primary modules fit this bucket right now
- both structurally weak and functionally weak: none of the audited primary modules fit this bucket right now, but unsupported free exploration remains outside safe scope
- highest-risk modules: [app.js](../workbench/app.js), [compute.js](../workbench/lib/compute.js), [discoveryMixer.js](../workbench/lib/discoveryMixer.js), [recoverability.py](../../src/ocp/recoverability.py)
- immediate refactor priorities: split shell/render/event logic, extract shared JS analysis core, remove duplicated mixer/control helpers, split persistence from export formatting, move scripts/tests off the docs runtime path
- immediate functional repair priorities: make export capabilities explicit per lab, keep unsupported scope warnings visible in-module, continue replacing partial/circular checks with independent cross-checks where possible
- what should be frozen until rewritten: another major feature wave into [app.js](../workbench/app.js) and [compute.js](../workbench/lib/compute.js) without decomposition first
- what is safe to build on: lower-level Python theorem kernels, qualified supported workflows, benchmark/trust snapshot pipeline, explicit unsupported handling, known-answer validation surface
