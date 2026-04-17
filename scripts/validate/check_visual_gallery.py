#!/usr/bin/env python3
from __future__ import annotations

"""Validate visual-gallery references and generated media signatures.

Checks:
- every `generated/...` reference in visual-gallery.md and visual-gallery.html exists,
- every referenced file is non-empty,
- basic file signature checks for png/gif/svg/mp4,
- manifest.json exists and referenced files in manifest exist.
"""

from pathlib import Path
import json
import re
import sys

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
GALLERY_MD = ROOT / 'docs/visuals/visual-gallery.md'
GALLERY_HTML = ROOT / 'docs/visuals/visual-gallery.html'
STORY_HTML = ROOT / 'docs/visuals/ocp-complete-visual-story.html'
INDEX_HTML = ROOT / 'docs/visuals/figure-index.html'
GALLERY_CSS = ROOT / 'docs/visuals/visual-gallery.css'
GALLERY_JS = ROOT / 'docs/visuals/visual-gallery.js'
GENERATED = ROOT / 'docs/visuals/generated'
MANIFEST = GENERATED / 'manifest.json'


def _extract_generated_refs(text: str) -> set[str]:
    refs = set(re.findall(r'generated/([A-Za-z0-9_\-.]+)', text))
    return refs


def _extract_media_srcs(text: str) -> list[str]:
    return re.findall(r'<(?:img|video)[^>]*\ssrc=\"([^\"]+)\"', text, flags=re.IGNORECASE)


def _check_signature(path: Path) -> bool:
    suffix = path.suffix.lower()
    data = path.read_bytes()
    if suffix == '.png':
        return data.startswith(b'\x89PNG\r\n\x1a\n')
    if suffix == '.gif':
        return data.startswith(b'GIF87a') or data.startswith(b'GIF89a')
    if suffix == '.svg':
        head = data[:400].decode('utf-8', errors='ignore').lower()
        return '<svg' in head
    if suffix == '.mp4':
        return b'ftyp' in data[:64]
    if suffix == '.pdf':
        return data.startswith(b'%PDF-')
    return True


def main() -> int:
    missing: list[Path] = []
    bad_signature: list[Path] = []
    refs: set[str] = set()
    html_pages = [GALLERY_HTML, STORY_HTML, INDEX_HTML]

    for page in (GALLERY_MD, *html_pages):
        if not page.exists():
            missing.append(page)
            continue
        text = page.read_text(encoding='utf-8')
        refs |= _extract_generated_refs(text)

        if page.suffix.lower() == '.html':
            for src in _extract_media_srcs(text):
                if src.startswith('http://') or src.startswith('https://') or src.startswith('data:'):
                    continue
                media_path = (page.parent / src).resolve()
                if not media_path.exists() or media_path.stat().st_size <= 0:
                    missing.append(media_path)
                if page == GALLERY_HTML and src.startswith('generated/') is False:
                    missing.append(Path(f'{page}: non-normalized media path \"{src}\"'))

    for dependency in (GALLERY_CSS, GALLERY_JS):
        if not dependency.exists() or dependency.stat().st_size <= 0:
            missing.append(dependency)

    for ref in sorted(refs):
        path = GENERATED / ref
        if not path.exists() or path.stat().st_size <= 0:
            missing.append(path)
            continue
        if not _check_signature(path):
            bad_signature.append(path)

    if not MANIFEST.exists():
        missing.append(MANIFEST)
    else:
        manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
        for rel in manifest.get('generated_files', []):
            if rel.startswith('data/'):
                path = ROOT / rel
            else:
                path = GENERATED / rel
            if not path.exists() or path.stat().st_size <= 0:
                missing.append(path)

    if missing or bad_signature:
        if missing:
            print('missing or empty files:')
            for path in missing:
                print(f'  - {path}')
        if bad_signature:
            print('bad file signatures:')
            for path in bad_signature:
                print(f'  - {path}')
        return 1

    print(f'visual gallery check passed: {len(refs)} referenced generated files')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
