#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
INDEX = ROOT / 'docs/workbench/index.html'
text = INDEX.read_text()
refs = re.findall(r'(?:href|src)="([^"]+)"', text)
missing: list[str] = []
for ref in refs:
    if ref.startswith('http://') or ref.startswith('https://'):
        continue
    if ref.startswith('#'):
        continue
    path = (INDEX.parent / ref).resolve()
    if not path.exists():
        missing.append(ref)
if missing:
    raise SystemExit(f'missing workbench assets: {missing}')
print(f'checked {INDEX}')
