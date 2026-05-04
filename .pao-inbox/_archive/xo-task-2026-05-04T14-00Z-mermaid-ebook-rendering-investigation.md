---
type: task
chapter: cross-cutting (book-build pipeline; not chapter-specific)
last-pr: n/a (XO has not investigated yet — fresh delegation from CO)
sender: xo
priority: medium
---

# XO → PAO delegation — Mermaid → ebook rendering investigation

## Background

CO reports that **Mermaid markdown blocks are not processing properly into the ebook output**. Diagrams in the source markdown render correctly when previewed in Markdown viewers / GitHub, but the EPUB / Kindle / PDF outputs of the book either:

- Show raw Mermaid source as a `<code>` block, or
- Show an empty figure where the diagram should be, or
- Some other failure mode you'll discover

CO has not specified which output formats are affected — please verify against each format the build produces and report which ones break.

## What XO has NOT done

XO has not investigated the book's build pipeline for this issue. This is a fresh delegation. Please don't assume any prior findings.

## Task

1. **Inspect the book repo's build chain** for Mermaid handling. Likely entry points:
   - `Makefile` — find the EPUB / Kindle / PDF targets; trace what processes Markdown
   - `build/*.py` — any script with "mermaid", "diagram", "figure", "epub", "pandoc" in its name or content
   - Pandoc filter inventory — `pandoc-mermaid` or `mermaid-filter` would be the canonical filter
   - Any pre-build step that converts Mermaid blocks to images (mmdc, kroki.io, etc.)
2. **Identify the actual break** — is the filter missing, misconfigured, broken, or returning wrong output? Reproduce on a single chapter that has a Mermaid block.
3. **Propose a fix** — concrete; specific to the build chain; respects existing patterns.
4. **Implement if the fix is mechanical** (adding a filter dependency; fixing a path; correcting a flag). If the fix requires architectural decision (new dependency family, output-format change), STOP and write a `pao-question-*.md` to XO's inbox at `/Users/christopherwood/Projects/Sunfish/icm/_state/research-inbox/`.

## Likely root-cause candidates (in decreasing probability)

1. **Missing Pandoc filter**: the most common Mermaid-to-EPUB chain is `pandoc --filter pandoc-mermaid` or `mermaid-filter`. If neither is installed or invoked, Mermaid blocks pass through unrendered.
2. **mmdc (`@mermaid-js/mermaid-cli`) not installed or not on PATH**: many filters delegate rendering to mmdc, which needs Node.js + Puppeteer. If mmdc is missing, the filter fails silently or errors.
3. **Format-specific gap**: EPUB readers vary in how they handle inline SVG; Kindle in particular often needs PNG fallback. If the filter renders SVG-only and Kindle is the broken format, that's the cause.
4. **Broken Mermaid syntax** in some chapters: less likely (the Markdown previewer would also fail) but worth confirming a representative chapter renders fine in an interactive preview before chasing pipeline bugs.

## Resources

- `mermaid-cli`: <https://github.com/mermaid-js/mermaid-cli> (Node.js CLI; renders to PNG/SVG via headless Chromium)
- `pandoc-mermaid`: <https://github.com/timofurrer/pandoc-mermaid-filter> or alternatives
- `mermaid-filter` (npm): <https://github.com/raghur/mermaid-filter> — Pandoc filter; uses mmdc internally
- `kroki.io` — server-rendered diagrams; can be self-hosted

## Hardware available

Whisper STT is set up at `desktop-umt08rn:8000`. **Mermaid rendering does NOT need GPU** — it's a CPU-only headless-Chromium task. Local Mac is fine.

## Reporting

When done, write a `pao-status-*.md` in the XO inbox at `/Users/christopherwood/Projects/Sunfish/icm/_state/research-inbox/` with:
- Which formats broke (EPUB / Kindle / PDF / etc.)
- What the actual root cause was
- The fix shipped (or PR # if you opened one) OR the architectural question that blocked you

## Cross-references

- This delegation: `xo-task-2026-05-04T14-00Z-mermaid-ebook-rendering-investigation.md`
- ADR 0072 (Beacon Protocol; Sunfish-side; defines the cross-repo signaling pattern this delegation uses)
- Existing book audiobook pipeline (precedent for build-chain integration): `build/audiobook.py`

---

**XO posture**: this is medium priority. Doesn't block anything CO is actively shipping; ebook output is the natural delivery channel and broken Mermaid is a quality issue that compounds. Fix when you have a clean cycle.
