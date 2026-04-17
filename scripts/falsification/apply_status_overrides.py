#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = [
    ROOT / 'docs/overview/claim-registry.md',
    ROOT / 'docs/overview/proof-status-map.md',
]

OVERRIDES = {
    'OCP-022': 'PROVED ON SUPPORTED FAMILY',
    'OCP-027': 'PROVED ON SUPPORTED FAMILY',
    'OCP-044': 'PROVED ON SUPPORTED FAMILY',
}


def update_line(line: str) -> str:
    if not line.strip().startswith('| OCP-'):
        return line
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if not cells:
        return line
    cid = cells[0]
    if cid not in OVERRIDES:
        return line

    # claim-registry: status at index 2
    # proof-status-map: status at index 3
    if len(cells) >= 4 and cells[2] in {'PROVED', 'CONDITIONAL', 'OPEN', 'VALIDATED', 'ANALOGY ONLY', 'DISPROVED', 'RETRACTED', 'PROVED ON SUPPORTED FAMILY'}:
        cells[2] = OVERRIDES[cid]
    elif len(cells) >= 5 and cells[3] in {'PROVED', 'CONDITIONAL', 'OPEN', 'VALIDATED', 'ANALOGY ONLY', 'DISPROVED', 'RETRACTED', 'PROVED ON SUPPORTED FAMILY'}:
        cells[3] = OVERRIDES[cid]

    return '| ' + ' | '.join(cells) + ' |\n'


def main() -> None:
    for path in FILES:
        lines = path.read_text(encoding='utf-8').splitlines(keepends=True)
        updated = [update_line(ln) for ln in lines]
        path.write_text(''.join(updated), encoding='utf-8')
        print(f'updated {path}')


if __name__ == '__main__':
    main()
