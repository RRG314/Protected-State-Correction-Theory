#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
CSV_PATH = ROOT / 'data/generated/inventories/discovery_inventory.csv'
MD_PATH = ROOT / 'docs/overview/discovery-inventory.md'

rows = [
    {
        'source_path': '/Users/stevenreid/Documents/New project/mhd-toolkit/docs/divergence_control.md',
        'description': 'High-value local summary of projection cleaning and GLM cleaning as concrete correction operators.',
        'relevance_score': 10,
        'status': 'canonical',
        'content_type': 'exact math, operator construction, practical comparison',
        'recommended_destination': 'docs/mhd/ and docs/operators/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/New project/mhd-toolkit/mhd_toolkit/divfree/projection.py',
        'description': 'FFT-based projection-cleaning implementation; best exact continuous-operator anchor for OCP.',
        'relevance_score': 10,
        'status': 'canonical',
        'content_type': 'exact operator code',
        'recommended_destination': 'src/ocp/mhd.py and docs/operators/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/New project/mhd-toolkit/mhd_toolkit/divfree/glm.py',
        'description': 'Dedner-style GLM cleaner; useful asymptotic correction comparison to exact projection.',
        'relevance_score': 9,
        'status': 'canonical',
        'content_type': 'continuous-time asymptotic correction',
        'recommended_destination': 'docs/mhd/ and docs/control/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/New project/mhd-toolkit/tests/test_divergence_cleaning.py',
        'description': 'Empirical validation of projection and GLM divergence reduction.',
        'relevance_score': 8,
        'status': 'canonical',
        'content_type': 'tests, experiments',
        'recommended_destination': 'tests/examples/ and docs/mhd/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/sds-research-repo/docs/correction-gap/correction_gap_formalization.md',
        'description': 'Prior theorem-schema / no-go development showing how broad unification can collapse to tautology if not category-specific.',
        'relevance_score': 9,
        'status': 'canonical',
        'content_type': 'theorem material, no-go material',
        'recommended_destination': 'docs/impossibility-results/ and docs/novelty-and-limits/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/sds-research-repo/docs/correction-gap/cross_domain_analysis.md',
        'description': 'Cross-system analogy layer; useful for provenance, but not promoted as theorem-level by itself.',
        'relevance_score': 6,
        'status': 'partial',
        'content_type': 'analogy only, structural prompts',
        'recommended_destination': 'archive/raw-imports/ and docs/disproven-or-weak/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/New project/repos/topological-adam/RGE_QEC_Fermat_Prime_2026.docx',
        'description': 'Claude-generated QEC bridge memo; contains useful motivation but mixes speculative novelty claims with known QEC facts.',
        'relevance_score': 7,
        'status': 'speculative',
        'content_type': 'QEC notes, analogy, partial theorem material',
        'recommended_destination': 'archive/raw-imports/ and docs/disproven-or-weak/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/New project/repos/topological-adam/DISCOVERIES.md',
        'description': 'Original discovery memo for MHD/optimizer bridge work; useful mainly as cautionary provenance.',
        'relevance_score': 4,
        'status': 'superseded',
        'content_type': 'experiments, bridge claims, speculative extension',
        'recommended_destination': 'docs/disproven-or-weak/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/New project/mhd-toolkit/docs/discoveries/variable_resistivity_obstructions.md',
        'description': 'Clean negative-result memo about where exact closure stops and perturbative correction must begin.',
        'relevance_score': 8,
        'status': 'canonical',
        'content_type': 'no-go material, program boundary',
        'recommended_destination': 'docs/impossibility-results/ and docs/mhd/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/New project/mhd-toolkit/docs/discoveries/non_bilinear_exact_families.md',
        'description': 'Positive exact-family memo for MHD closure; secondary OCP relevance as an example of when correction becomes exact.',
        'relevance_score': 6,
        'status': 'canonical',
        'content_type': 'exact math, discovery memo',
        'recommended_destination': 'docs/mhd/'
    },
    {
        'source_path': '/Users/stevenreid/Documents/rge-research-program/docs/overview/novelty-and-opportunity.md',
        'description': 'Useful caution on novelty inflation, failure-mode-first research design, and operator-language targets.',
        'relevance_score': 5,
        'status': 'canonical',
        'content_type': 'program design, limits',
        'recommended_destination': 'docs/positioning/ and NOVELTY_AND_LIMITS.md'
    },
    {
        'source_path': '/Users/stevenreid/Documents/rge-research-program/docs/foundations/renormalization-and-coarse-graining.md',
        'description': 'Operator-language and scale-step framing; useful as a meta-level programmatic influence, not direct OCP theorem content.',
        'relevance_score': 4,
        'status': 'partial',
        'content_type': 'operator-language prompt',
        'recommended_destination': 'docs/internal-provenance/'
    },
]

CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
with CSV_PATH.open('w', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

canonical = sum(1 for row in rows if row['status'] == 'canonical')
partial = sum(1 for row in rows if row['status'] == 'partial')
speculative = sum(1 for row in rows if row['status'] == 'speculative')
superseded = sum(1 for row in rows if row['status'] == 'superseded')

lines = [
    '# Discovery Inventory',
    '',
    'This inventory records the local material used to build the OCP research program. It is intentionally selective: the goal is to capture the files that genuinely contributed mathematical structure, operator constructions, program boundaries, or provenance.',
    '',
    '## Totals',
    f'- Curated high-value sources: **{len(rows)}**',
    f'- Canonical sources: **{canonical}**',
    f'- Partial sources: **{partial}**',
    f'- Speculative sources kept only for provenance: **{speculative}**',
    f'- Superseded sources kept only for provenance: **{superseded}**',
    '',
    '## Selection Logic',
    '- Prefer files that expose exact operators, exact tests, or clear impossibility boundaries.',
    '- Keep broad analogy material only when it helped sharpen a limitation or a design criterion.',
    '- Treat QEC as the exact anchor, MHD projection cleaning as the exact continuous anchor, and GLM/control-style feedback as the asymptotic branch.',
    '',
    '## Highest-Value Inputs',
]
for row in rows[:6]:
    lines.extend([
        f"### `{Path(row['source_path']).name}`",
        f"- Path: `{row['source_path']}`",
        f"- Relevance: {row['relevance_score']}/10",
        f"- Status: `{row['status']}`",
        f"- Why it mattered: {row['description']}",
        '',
    ])
lines.extend([
    '## Machine-Readable Artifact',
    f'- CSV inventory: `{CSV_PATH}`',
])
MD_PATH.write_text('\n'.join(lines) + '\n')
print(f'wrote {CSV_PATH}')
print(f'wrote {MD_PATH}')
