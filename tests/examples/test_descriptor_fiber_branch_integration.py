from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_descriptor_fiber_canonical_docs_exist() -> None:
    required = [
        ROOT / "docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md",
        ROOT / "docs/research-program/descriptor-fiber-anti-classifier-branch-status.md",
        ROOT / "docs/research-program/descriptor-fiber-anti-classifier-branch-integration-report.md",
        ROOT / "papers/descriptor-fiber-anti-classifier-branch.md",
    ]
    for path in required:
        assert path.exists(), f"missing canonical branch file: {path}"
        assert path.stat().st_size > 0, f"empty canonical branch file: {path}"


def test_readme_and_branch_maps_reference_canonical_name() -> None:
    readme = read(ROOT / "README.md")
    assert "Descriptor-fiber anti-classifier branch paper" in readme
    assert "meta theory" not in readme.lower()

    branch_audit = read(ROOT / "docs/research-program/branch-audit.md")
    assert "Descriptor-fiber anti-classifier branch" in branch_audit


def test_canonical_invariants_artifacts_exist_and_are_parseable() -> None:
    csv_path = ROOT / "data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.csv"
    json_path = ROOT / "data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json"
    assert csv_path.exists() and csv_path.stat().st_size > 0
    assert json_path.exists() and json_path.stat().st_size > 0

    payload = json.loads(read(json_path))
    assert "summary" in payload and isinstance(payload["summary"], list)
    assert len(payload["summary"]) >= 1
