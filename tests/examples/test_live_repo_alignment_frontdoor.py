from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_readme_frontdoor_identity_and_links() -> None:
    text = _read(ROOT / "README.md")
    assert "protected-state correction and constrained-observation recoverability" in text.lower()
    assert "Descriptor-fiber anti-classifier branch paper" in text
    assert "https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/" in text
    assert "[Figure Index (image center)](docs/visuals/figure-index.html)" in text
    assert "[Visual Gallery](docs/visuals/visual-gallery.html)" in text

    relative_links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    for link in relative_links:
        if link.startswith("http://") or link.startswith("https://") or link.startswith("#"):
            continue
        path = (ROOT / link).resolve()
        assert path.exists(), f"README link target missing: {link}"


def test_research_map_and_status_include_branch_limited_scope() -> None:
    research_map = _read(ROOT / "RESEARCH_MAP.md")
    assert "Descriptor-fiber quantitative lane" in research_map
    assert "Foundational OCP Spine" in research_map
    assert "Figure Index (image center)" in research_map
    assert "Visual Gallery" in research_map

    status = _read(ROOT / "STATUS.md")
    assert "theorem-first, branch-limited research program" in status
    assert "descriptor-fiber quantitative package" in status.lower()
