#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SCAN_PATHS = [
    ROOT / 'README.md',
    ROOT / 'docs' / 'theorem-core',
    ROOT / 'docs' / 'restricted-results',
    ROOT / 'docs' / 'physics-translation',
    ROOT / 'docs' / 'overview',
]

FORBIDDEN_ALWAYS = [
    re.compile(r'\bnew theory of information\b', re.IGNORECASE),
    re.compile(r'\binformation is (?:a|the)?\s*force\b', re.IGNORECASE),
    re.compile(r'\binformation is fundamental\b', re.IGNORECASE),
    re.compile(r'\binformation creates reality\b', re.IGNORECASE),
    re.compile(r'\bgravity is made of information\b', re.IGNORECASE),
    re.compile(r'\bdark matter is information\b', re.IGNORECASE),
    re.compile(r'\btheory of everything\b', re.IGNORECASE),
]

FORBIDDEN_UNLESS_NEGATED = [
    re.compile(r'\buniversal information law\b', re.IGNORECASE),
    re.compile(r'\buniversal law of information\b', re.IGNORECASE),
    re.compile(r'\buniversal scalar invariant\b', re.IGNORECASE),
    re.compile(r'\buniversal scalar correction capacity\b', re.IGNORECASE),
]

SDS_PATTERN = re.compile(r'\bSDS\b')
SDS_ALLOW_TOKENS = (
    'ANALOGY ONLY',
    'not promoted',
    'scope boundary',
    'nonclaim',
    'not theorem-core',
)

NEGATION_TOKENS = (
    'no ',
    'not ',
    'without ',
    'excluded',
    'rejected',
    'do not',
    'must not',
)


def _iter_markdown_files(base: Path):
    if base.is_file() and base.suffix.lower() == '.md':
        yield base
        return
    if base.is_dir():
        for p in sorted(base.rglob('*.md')):
            if p.is_file():
                yield p


def _is_negated(line_lower: str) -> bool:
    return any(tok in line_lower for tok in NEGATION_TOKENS)


def line_violations(rel_path: str, line: str) -> list[str]:
    stripped = line.strip()
    if not stripped:
        return []
    line_lower = stripped.lower()
    out: list[str] = []

    for patt in FORBIDDEN_ALWAYS:
        if patt.search(stripped):
            out.append(f"{rel_path}: forbidden claim phrase: {stripped}")

    for patt in FORBIDDEN_UNLESS_NEGATED:
        if patt.search(stripped) and not _is_negated(line_lower):
            out.append(f"{rel_path}: unscoped universal phrasing: {stripped}")

    if (
        (rel_path.startswith('docs/theorem-core/') or rel_path.startswith('docs/restricted-results/'))
        and SDS_PATTERN.search(stripped)
        and not any(tok.lower() in line_lower for tok in SDS_ALLOW_TOKENS)
    ):
        out.append(f"{rel_path}: SDS mention in theorem/restricted lane without scope guard: {stripped}")
    return out


def main() -> int:
    violations: list[str] = []

    for base in SCAN_PATHS:
        if not base.exists():
            continue
        for path in _iter_markdown_files(base):
            rel = path.relative_to(ROOT)
            text = path.read_text(encoding='utf-8', errors='ignore').splitlines()
            for ln, raw in enumerate(text, start=1):
                line = raw.strip()
                if not line:
                    continue
                rel_str = str(rel)
                for v in line_violations(rel_str, line):
                    violations.append(f"{rel}:{ln}: {v.split(': ', 1)[1]}")

    if violations:
        print(f"claim scope check failed: {len(violations)} violation(s)")
        for row in violations:
            print(row)
        return 1

    print('claim scope check passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
