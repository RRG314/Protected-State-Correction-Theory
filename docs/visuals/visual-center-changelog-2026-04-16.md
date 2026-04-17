# Visual Center Changelog (2026-04-16)

## What Was Improved

1. Rebuilt the visual gallery as a structured visual center with sectioned flow rather than a flat image dump.
2. Added a featured centerpiece sequence near the top to explain the repo's core logic quickly.
3. Added per-visual interpretation text and "why it matters" style summaries on cards.
4. Added evidence badges (`theorem-backed`, `restricted exact`, `validated family example`, `no-go`, `schematic`).
5. Added sticky jump navigation and lightweight filters (`theorem`, `no-go`, `recoverability`, `dynamics`, `pde`, `schematic`).
6. Added side-by-side comparison sections for key contrasts (exact vs impossible, augmentation repair, periodic vs bounded failure).
7. Added click-to-expand image behavior for readability and per-card direct download links for PNG/SVG/GIF/MP4.
8. Added stronger trust signals: generation-source note, truth-status legend, and links to branch/theory docs.
9. Added figure index and complete visual story links from the gallery surface.
10. Improved output readability by increasing static figure PNG resolution in generator output.
11. Added runtime media health checks with visible fallback blocks (`Missing visual: [filename]`) and live loaded/failed counts.
12. Reworked the visual center into an 8-step guided learning flow:
    - Core Idea,
    - Exact Recovery,
    - Failure / No-Go,
    - Structural Insight,
    - Fixing Systems,
    - Advanced Failures,
    - Dynamic Behavior,
    - Cross-System Mapping.
13. Added progress indicator and next/previous step navigation for walkthrough-style learning.

## Files Updated

- `docs/visuals/visual-gallery.html`
- `docs/visuals/visual-gallery.css`
- `docs/visuals/visual-gallery.js`
- `scripts/visuals/generate_visuals.py`
- `scripts/validate/check_visual_gallery.py`
- `tests/examples/test_visual_gallery_integrity.py`

## Why This Matters

The visual center now behaves like a reviewer-facing research surface:
- easier to scan,
- easier to trust,
- easier to navigate,
- and easier to connect back to theorem/no-go branch evidence.
