# GitHub Pages Deployment

## Recommended Simple Setup

Use GitHub Pages from the repository's `docs/` folder on `main`.

That makes the workbench available at:

```text
https://<user>.github.io/<repo>/workbench/
```

## Why This Setup
- static only
- no workflow required
- no server required
- keeps the reviewer-facing tool inside the research repo

## What To Publish
The workbench lives in:
- `docs/workbench/index.html`
- `docs/workbench/styles.css`
- `docs/workbench/app.js`
- `docs/workbench/lib/`

## Validation Before Publishing
Run:

```bash
cd '/Users/stevenreid/Documents/New project/repos/ocp-research-program'
./scripts/validate/run_all.sh
```

This now checks:
- python theorem tests
- static workbench module tests
- generated validation artifacts
- markdown links
- CFD and constrained-observation recoverability module outputs, plus saved-state plumbing through the Node workbench suite
