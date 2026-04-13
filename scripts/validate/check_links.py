#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
SKIP_DIRS = {
    ROOT / 'archive/raw-imports',
    ROOT / '.venv',
    ROOT / '.pytest_cache',
}

pattern = re.compile(r'\]\(([^)]+)\)')
missing: list[tuple[Path, str, Path]] = []

for path in ROOT.rglob('*.md'):
    if any(skip in path.parents or path == skip for skip in SKIP_DIRS):
        continue
    text = path.read_text()
    for target in pattern.findall(text):
        if target.startswith('http://') or target.startswith('https://') or target.startswith('#'):
            continue
        if '\\' in target or '\n' in target:
            continue
        target_path = (path.parent / target).resolve() if not target.startswith('/') else Path(target)
        if not target_path.exists():
            missing.append((path, target, target_path))

if missing:
    print(f'broken_links {len(missing)}')
    for src, dst, resolved in missing:
        print(f'{src} -> {dst} => {resolved}')
    sys.exit(1)

print('markdown link check passed')
