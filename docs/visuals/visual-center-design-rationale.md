# Visual Center Design Rationale

## Design Thesis

The visual center should function as a theorem-facing explanatory layer, not a decorative gallery.

## Principles Used

1. Evidence-first framing: every card includes evidence labels and branch context.
2. Interpretation-first captions: each visual states what it shows and why it matters.
3. Comparison over ornament: key repo claims are presented as explicit contrasts.
4. Navigation as trust: users can jump by topic and filter by evidence class.
5. Readability and exportability: click-to-expand plus direct download links per asset.
6. Scope honesty: schematic visuals are clearly marked and never presented as proved structure.

## Structural Choices

- The visual center is now an 8-step guided learning flow:
  1. core idea,
  2. exact recovery,
  3. failure/no-go,
  4. structural insight,
  5. fixing systems,
  6. advanced failures,
  7. dynamic behavior,
  8. cross-system mapping.
- Each step has short orientation text plus per-visual \"what this shows / why it matters\" framing.
- Progress UI and next/previous controls support walkthrough-style reading.
- A dedicated trust legend clarifies evidence semantics without cluttering each visual.

## Technical Choices

- Static HTML/CSS/JS only; GitHub Pages safe.
- Lightweight filter and lightbox JS; no framework dependency.
- Runtime media health checks for broken/missing assets with explicit fallback messages.
- Existing generated visual assets remain source-of-truth artifacts.
- Validation checks updated to catch missing gallery-linked artifacts.

## Limits

- This surface is an explanatory index, not a substitute for proofs.
- Some sections summarize branch status and require linked docs for formal statements.
- Schematic layout remains explicitly schematic.
