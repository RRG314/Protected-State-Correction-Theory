# Release Publishing Checklist

This checklist is for publishing a clean GitHub release from this repository.

## 1) Prepare release content

1. Add a release note file in `docs/releases/` (for example `v1.1.0.md`).
2. Update `CHANGELOG.md` with the new version and date.
3. Update `docs/releases/README.md` so the new release appears in the index.
4. Confirm README badges are current.

## 2) Validate before tagging

Run:

```bash
source .venv/bin/activate
python3 scripts/validate/check_links.py
python3 scripts/validate/check_naming.py
python3 scripts/validate/check_workbench_static.py
```

Optional full test pass:

```bash
bash scripts/validate/run_all.sh
```

## 3) Push branch and open PR

```bash
git push origin steven/push-cleanup-audit
```

Open a PR from the release branch into `main`. Merge only after review.

## 4) Tag and push after merge

```bash
git switch main
git pull --ff-only origin main
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin main
git push origin vX.Y.Z
```

## 5) Publish on GitHub Releases

1. Open the repository Releases page.
2. Create a new release from tag `vX.Y.Z`.
3. Title format: `Protected-State Correction Theory vX.Y.Z`.
4. Paste the content of `docs/releases/vX.Y.Z.md` into the release body.
5. Mark as latest release.
6. Publish.

## 6) Post-release checks

1. Confirm release badge shows the new version.
2. Confirm `docs/releases/README.md` links correctly.
3. Confirm compare link in the release note resolves.
