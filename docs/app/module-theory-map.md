# Module-Theory Map

This document explains how each major workbench module is tied to theorem or validation evidence. The goal is traceability: a user should be able to see what mathematical layer supports a module’s output.

The Structural Discovery Studio is the diagnosis-and-repair module and is backed by constrained-observation and recoverability logic in `src/ocp/structural_discovery.py` plus branch theorem docs. The Discovery Mixer is the typed composition module and is backed by `src/ocp/discovery_mixer.py` together with `docs/discovery-mixer/` rules and validations. The Benchmark/Validation Console is the reproducibility surface and is backed by benchmark tests and generated validation artifacts.

Branch-specific labs follow the same pattern. Exact projection and sector modules map to core and QEC files in `src/ocp`. CFD and MHD labs map to their branch docs and tests. The no-go explorer maps to canonical impossibility documents. Each module is expected to preserve the scope level of its source evidence.

Evidence rule: module output may only be stronger than its source if a new proof/validation artifact is added and linked. Otherwise the module must inherit the source status label.
