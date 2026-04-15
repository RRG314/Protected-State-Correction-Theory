# Structural Discovery Quickstart

## Goal

Start with a failing or ambiguous setup and use the studio to answer:

- why it fails
- what weaker target already works
- what minimal change repairs it
- whether the fix is exact, asymptotic, or still blocked

## Fast Path In The Workbench

Open `docs/workbench/index.html` and switch to **Structural Discovery Studio**.

Recommended first runs:

1. `Periodic modal repair`
2. `Control history repair`
3. `Weaker vs stronger target`
4. `Boundary architecture repair`
5. `Restricted-linear repair`

For each run:

1. inspect the classification badge
2. read the failure analysis panel
3. inspect the minimal-fix cards
4. click `Apply in studio`
5. read the before/after evidence panel
6. export the report or CSV snapshot if the configuration should be kept

## Fast Path In Python

Generate the reference demos:

```bash
PYTHONPATH=src python3 scripts/compare/run_structural_discovery_examples.py
```

Read the main artifact:

- `data/generated/structural_discovery/structural_discovery_summary.json`

## When To Use Structural Discovery

Use it when you know the system family and want help deciding:

- whether the current target is too strong
- whether the current record is too coarse
- whether adding one measurement, one mode, or one extra history step is enough
- whether the setup is blocked by a real no-go

## When Not To Use It

Do not use it as if it were:

- a universal automated theorem prover
- a black-box recommender for arbitrary nonlinear systems
- a substitute for proving a new branch theorem when the branch has not been formalized yet
