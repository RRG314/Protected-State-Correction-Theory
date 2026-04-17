from __future__ import annotations

from pathlib import Path
import re

import pytest

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
GENERATED = ROOT / 'docs/visuals/generated'
GALLERY_FILES = [
    ROOT / 'docs/visuals/visual-gallery.md',
    ROOT / 'docs/visuals/visual-gallery.html',
    ROOT / 'docs/visuals/ocp-complete-visual-story.html',
    ROOT / 'docs/visuals/figure-index.html',
]
GALLERY_ASSETS = [
    ROOT / 'docs/visuals/visual-gallery.css',
    ROOT / 'docs/visuals/visual-gallery.js',
]


def _extract_generated_refs(text: str) -> set[str]:
    return set(re.findall(r'generated/([A-Za-z0-9_\-.]+)', text))


@pytest.mark.parametrize('path', GALLERY_FILES)
def test_gallery_file_exists(path: Path) -> None:
    assert path.exists()


@pytest.mark.parametrize('path', GALLERY_ASSETS)
def test_gallery_support_assets_exist(path: Path) -> None:
    assert path.exists()
    assert path.stat().st_size > 0


def test_gallery_references_exist_and_are_nonempty() -> None:
    refs: set[str] = set()
    for path in GALLERY_FILES:
        refs |= _extract_generated_refs(path.read_text(encoding='utf-8'))

    assert refs
    for ref in refs:
        file_path = GENERATED / ref
        assert file_path.exists(), f'missing: {file_path}'
        assert file_path.stat().st_size > 0, f'empty: {file_path}'


def test_visual_gallery_has_required_learning_surface() -> None:
    html = (ROOT / 'docs/visuals/visual-gallery.html').read_text(encoding='utf-8')
    assert 'id="asset-health"' in html
    assert 'id="progress-label"' in html
    assert 'id="progress-bar"' in html
    assert 'id="prev-step"' in html
    assert 'id="next-step"' in html
    for idx in range(1, 9):
        assert f'id="step-{idx}"' in html
    assert 'theorem-backed' in html
    assert 'validated' in html
    assert 'schematic' in html
