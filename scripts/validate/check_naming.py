#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')

required = {
    ROOT / 'README.md': 'Protected-State Correction Theory',
    ROOT / 'docs/index.html': 'Protected-State Correction Theory',
    ROOT / 'docs/workbench/index.html': 'Protected-State Correction Workbench',
    ROOT / 'docs/finalization/naming-and-terminology.md': 'Protected-State Correction Theory',
}

for path, needle in required.items():
    text = path.read_text()
    if needle not in text:
        raise SystemExit(f'missing required naming string in {path}: {needle}')

forbidden = {
    ROOT / 'README.md': ['# Orthogonal Correction Principle (OCP) Research Program'],
    ROOT / 'docs/workbench/index.html': ['<title>OCP Workbench</title>'],
    ROOT / 'docs/index.html': ['Open OCP Workbench'],
}

for path, needles in forbidden.items():
    text = path.read_text()
    for needle in needles:
        if needle in text:
            raise SystemExit(f'found outdated naming string in {path}: {needle}')

print('naming consistency check passed')
