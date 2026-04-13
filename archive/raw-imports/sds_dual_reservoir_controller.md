# Dual-Reservoir Controller

## What It Is

A training controller that keeps track of two coupled observables:
- a hot reservoir for local update pressure
- a cold reservoir for stability reserve

The controller then computes:
- a deficit-like joint budget
- an efficiency-like imbalance score
- a regime label (`productive`, `transition`, `equilibrium`, `unstable`)

Those signals adapt:
- learning rate
- momentum / `beta1`
- weight decay multiplier

## Practical Problem

This tool is for runs that become brittle when the learning rate is pushed harder than the safest baseline setting.

The goal is not to beat Adam in every easy regime. The goal is to make the tuning-sensitive region more usable.

## SDS Borrowing

Borrowed structure:
- two coupled reservoirs
- a bounded shared budget
- a deficit term between them
- a useful-imbalance interpretation
- regime changes near equilibrium or instability

Not claimed:
- that Schwarzschild-de Sitter physics literally governs optimization
- that this controller is theorem-level or universal

## Benchmark Result

Dataset:
- noisy two-moons classification benchmark

Comparison:
- Adam baseline
- efficiency-only ablation
- full dual-reservoir controller

Main result:
- all-rate mean best validation loss: Adam `0.0804`, full controller `0.0780`
- aggressive-band mean best validation loss: Adam `0.0784`, full controller `0.0728`
- aggressive-band mean final validation loss: Adam `0.1749`, full controller `0.1105`

Interpretation:
- the strongest practical value is in the aggressive learning-rate band, not in the already-safe band

Status:
- recommended

## When To Use This

Use it when:
- the optimizer is oscillating or overshooting under aggressive learning rates
- you want a controller with a readable stability/progress story
- you want a stronger default in tuning-sensitive regions

## When Not To Use This

Do not use it when:
- a plain Adam or SGD baseline is already stable and well tuned
- you need the simplest possible optimizer stack
- you do not want an extra control layer

## Inputs And Outputs

Inputs per epoch:
- training loss
- validation loss
- mean gradient norm
- mean step norm

Outputs:
- learning-rate multiplier
- `beta1`
- weight-decay multiplier
- regime label
- diagnostic trace values

## Key Files

- `src/sds/tools/dual_reservoir/controller.py`
- `src/sds/tools/monitor/state_space.py`
- `src/sds/benchmarks/suite.py`
- `experiments/optimizer/run_dual_reservoir_benchmarks.py`

## Reproduce

```bash
./scripts/validate/run_sds_tools_suite.sh
```

Or run only the benchmark:

```bash
./.venv/bin/python experiments/optimizer/run_dual_reservoir_benchmarks.py
```

## Exact vs Empirical

- exact: none of the optimizer claims are exact SdS physics
- empirical: benchmark result and promotion decision
- structural borrowing: the controller design language and bounded coupling construction
