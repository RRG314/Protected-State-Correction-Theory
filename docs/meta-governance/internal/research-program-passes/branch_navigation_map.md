# Branch Navigation Map

Date: 2026-04-18

Primary public branch entry path: `branches/`
Canonical doc routing map: `docs/overview/repo-authority-map.md`

## Branch index

- `branches/00-core-ocp/`
- `branches/01-exact-projector-and-sector/`
- `branches/02-generator-and-asymptotic/`
- `branches/03-constrained-observation-and-pvrt/`
- `branches/04-fiber-recoverability-and-no-go/`
- `branches/05-positive-recoverability-and-design/`
- `branches/06-invariants-and-augmentation/`
- `branches/07-cfd-bounded-domain/`
- `branches/08-mhd-closure-and-obstruction/`
- `branches/09-physics-extension/`
- `branches/10-workbench-and-discovery-systems/`

## Navigation design rule

Each branch README contains:
1. branch scope,
2. strongest results,
3. canonical docs/papers,
4. tests/artifacts,
5. open items,
6. pointer to shared infra.

## Shared infrastructure map

- Code: `src/`
- Tests: `tests/`
- Artifacts: `data/generated/`
- Repro scripts: `scripts/compare/`, `scripts/validate/`
- Public visuals: `figures/`, `docs/visuals/`

## Public-first routing

Recommended entry sequence for external readers:
1. root `README.md`
2. `docs/overview/main-contributions.md`
3. chosen branch in `branches/`
4. canonical paper and tests/artifacts linked from that branch README.
