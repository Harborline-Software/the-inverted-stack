---
type: pao-directive
audience: Yeoman (chapter pilot drafting)
priority: high
related:
  - .pao-inbox/_creative/nansen-ingestion-canon.md
  - vol-2/_voice-drafts/nansen-ingestion/ch03-ice-edge-arrival.source.md
  - vol-2/_voice-drafts/nansen-ingestion/ch03-ice-edge-arrival.transformed.md
  - vol-2/_voice-drafts/nansen-ingestion/ch03-ice-edge-arrival.craft-note.md
  - vol-2/act-3/ch17-transit-north.md
---

# PAO Directive — FFF Nansen-ingestion pilot on Ch 17 (transit north)

## What

Run the FFF (Nansen-Verne triangulated ingestion) pilot on **Ch 17 — Transit North**, following the same shape as the completed Ch 3 ice-edge pilot.

## Why

Phase 0 obs-density rollup (`build/output/qa/vol-2-observational-density.json`) names Ch 17 as the lowest-density Vol 2 chapter — 35.66/1k vs canon 48.83/1k (0.73× canon). Ch 17 is also a transit/atmospheric chapter — the chapter type the canon ingestion is most calibrated for. Ch 3 pilot completed; CO ear-tested the original-vs-transformed A/B and the FFF posture is approved for scale. Ch 17 is the next data point.

## Source-vocabulary canon

Three Project Gutenberg public-domain sources, all logged in `.pao-inbox/_creative/nansen-ingestion-canon.md`:

- **Nansen 1897** (Arctic field diary) — `/tmp/gutenberg/farthest-north.txt`
- **Verne 1897** (Antarctic Mystery) — `/tmp/gutenberg/source-10339.txt`
- **Verne 1870** (Twenty Thousand Leagues) — `/tmp/gutenberg/source-164.txt`

Observational-lemma seed at `vol-2/_glossary/_observational_lemmas.yaml`.

## Template artifacts (mirror Ch 3 shape)

Produce three files under `vol-2/_voice-drafts/nansen-ingestion/`:

1. `ch17-transit-north.source.md` — verbatim extract of the highest-leverage Ch 17 passage (the atmospheric one with the most potential observational uplift; ear-test candidate).
2. `ch17-transit-north.transformed.md` — same passage rewritten with vocabulary triangulated against the three canon sources. **Preserve Anna's compressed-deliberate first-person register** — voice does not change, only the concrete-noun and action-verb density. Texture-yes; plot-no.
3. `ch17-transit-north.craft-note.md` — brief notes: which lemmas were lifted from which canon source, what was kept original, what dropped because Anna would not say it.

## Constraints

- **No franchise imports.** The Janeway skill is voice-toned, not setting-toned. No Federation/Starfleet/Prime-Directive coloration anywhere.
- **No invented plot.** Ingestion is observational vocabulary only. No new scenes, no new characters, no new actions.
- **§7 narrative-restraint canon holds.** Distress signaling / false codes remain narratively un-named.
- **Voice telemetry check.** After transformed draft, run `python3 build/lexical_fatigue.py --chapter ch17` and confirm verdict still green; transformed obs/1k should rise meaningfully (target: 45–55/1k, into canon range).
- **Render the ear-test pair.** Use Kokoro `af_alloy` at speed 0.92 (the draft-render preset from Ch 3 pilot) for both source.mp3 and transformed.mp3 — fast comparison cost, not final.

## Acceptance check

- Three pilot artifacts present.
- Galley verdict green on transformed chapter (run on the in-place file after applying the transform; revert before commit if scaling has not been approved).
- A `.pao-inbox/yeoman-resumed-*` beacon naming the two MP3 paths so CO can ear-test.

## Decision the pilot informs

If Ch 17 ear-test passes, the FFF approach scales to the rollup's remaining 4 candidates (ch13, ch10, ch18, ch15) in priority order. If it fails or distorts Anna's voice, we stop and reconsider.

## Coordination

Beacon back when ear-test MP3s are ready. PAO will coordinate the ear-test with CO and the verdict — do not auto-apply the FFF transformation into `vol-2/act-3/ch17-transit-north.md` canon unless directed.
