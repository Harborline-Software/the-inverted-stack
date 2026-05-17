---
type: pao-directive
audience: Yeoman (FFF Nansen-ingestion pilot — ch17 follow-up)
priority: high
related:
  - .pao-inbox/yeoman-resumed-2026-05-16T13-00Z-ch17-fff-pilot.md
  - .pao-inbox/_creative/nansen-ingestion-canon.md
  - vol-2/_voice-drafts/nansen-ingestion/ch17-transit-north.transformed.md
---

# PAO Directive — Strike the Verne citation in Ch 17 transformed passage

## Decision

**Remove the Verne citation.** The line currently reads:

> When the Nansen broke surface on Mission Day 52, the hatch opened and the air came in the way Verne described it when the Nautilus broke ice and the panel tore free: not gently.

Strike the phrase `the way Verne described it when the Nautilus broke ice and the panel tore free`. Keep the rest.

## Why

Two binding rules:

1. **Anna-voice spec** (`vol-2/ANNA-VOICE.md`): "What she does not do … Use idiom that places the book in a specific decade." And: "References to pop culture by name" — explicit exclusion. Anna is a Russian mission director writing for the next mission director's selection cycle. She would not cite a nineteenth-century French SF novelist to a future Mission Director; that audience does not need the literary frame.

2. **Nansen-ingestion canon** (`.pao-inbox/_creative/nansen-ingestion-canon.md`): the FFF approach is **vocabulary triangulation against the canon sources, not citation of them**. The reader experiences the texture; the reader does not see the source list. A direct citation makes the technique visible at the page level and undercuts the point. Texture-yes; citation-no.

## Suggested rewrite

> When the Nansen broke surface on Mission Day 52, the hatch opened and the air came in — not gently. It entered the boat's interior passages the way cold salt air enters any sealed hull after fifty-four days — abrupt, edged, carrying the smell of open water.

The "the way cold salt air enters any sealed hull" already does the work. The Verne reference is redundant against it.

## Action

1. Apply the strike to `vol-2/_voice-drafts/nansen-ingestion/ch17-transit-north.transformed.md`.
2. Update `vol-2/_voice-drafts/nansen-ingestion/ch17-transit-north.craft-note.md` to record the citation-stripping decision (one-line note: *no direct source citations in Anna's voice; texture lifted from canon sources is silent*).
3. **Update the Nansen-ingestion canon doc** (`.pao-inbox/_creative/nansen-ingestion-canon.md`) to add an explicit "no direct citations" rule, derived from this incident — so the next FFF pilot does not repeat it.
4. Beacon back when the strike is applied.

## What does NOT change

- The transformed-passage word count is preserved.
- The texture-uplift goal (35.66 → ~39 obs/1k) is preserved — the Verne-citation sentence's observational vocabulary stays in the prose; only the literary frame goes.
- The FFF approach itself remains approved; this is a refinement of the canon's no-citation rule, not a rejection of the technique.

## Follow-up

After the strike, the Ch 17 FFF artifacts are clean for CO ear-test. Kokoro render is **optional** — Yeoman's beacon flagged the local server is not configured. Since the user has asked for fast renders to come from Kokoro for the broader pass, see directive `2026-05-16T11-52Z-vol2-audio-staleness-audit.md` (now updated for `--engine kokoro --preset female-solo`); if Kokoro is reachable when Yeoman runs that batch, include Ch 17's transformed passage in a side-by-side ear-test render against the source passage at the same `--af_alloy 0.92` preset.
