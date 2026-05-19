---
type: pao-directive
audience: Yeoman (web reader maintenance)
priority: medium
related:
  - .pao-inbox/_decisions/2026-05-07-forced-alignment-evaluation.md
  - .pao-inbox/co-session-2026-05-07T14-27Z-web-reader-enhancements.md
---

# PAO Directive - Revert web reader highlighting to sentence-level only

## What

Drop the **word-level highlight layer** in the web reader (`web/`). Keep paragraph + sentence highlighting. The three-layer model becomes two-layer.

## Why

CO ear-tested the forced-alignment pilot output (Ch 1 Kokoro draft + aeneas-derived per-word interpolation in the v2 alignment JSON). Verdict: word-level highlighting **does not line up** with the audio. Two root causes:

1. **Interpolation was always a guess.** The original word-level highlight used linear interpolation across the chunk's duration; the aeneas pilot used finer-grained interpolation within sentence-fragments - but both are estimates, not measurements. ciufi-galeazzi's Italian-cadenced delivery has non-uniform speech rate within sentences; estimates drift visibly.
2. **27% tail-confidence-loss** in the aeneas output (chunks at the end of the audio compressed to zero-duration), making the back third of any chapter's word-level highlight catastrophically wrong.

Sentence-level highlighting binds against **ground-truth** data: the chunk `start_seconds` / `end_seconds` in the alignment JSON came directly from the TTS engine's own knowledge of when it started and stopped each sentence. These are not estimates.

## What changes

1. **Web reader UI:** remove the 42%-fill word-level highlight layer. Keep paragraph (7% tint + accent left border) and sentence (16% tint). For paragraphs with a single sentence or mixed-HTML elements, sentence-level falls back to paragraph-only (existing behavior).
2. **Alignment data:** no schema change required. The v2 schema's `words[]` array can stay in the JSON files; the renderer just stops binding to it. **Graceful regression** - chapters without `words[]` still render correctly at sentence level (most of Vol 1 and the new Vol 2 chapters), and chapters with `words[]` (Ch 1 v2 alignment from the pilot) render the same way.
3. **Sticky-player staleness warning + alignment-coverage logic:** unchanged. Both still operate at the chunk level, which is where sentence-level highlighting lives.

## What does NOT change

- The audio pipeline (`build/audiobook.py`). Already produces chunk-level timestamps that drive sentence-level highlighting.
- The chunk-cache, alignment-JSON regeneration, multi-track convention, or any audiobook generation behavior.
- The forced-alignment pilot artifacts - the aeneas-derived alignment for Ch 1 stays where it is. We just stop binding to its word-level fields.
- Future-option preservation: if word-level highlighting is reconsidered, the API STT path (`POST /api/v1/audio/transcriptions` via Inference Studio at `:8881/api/v1`) is the recommended production-quality replacement, NOT a return to interpolation. See decision doc.

## Acceptance check

After the change:

1. Open Ch 1 in the web reader. Audio plays; the active sentence is tinted; the active paragraph carries the accent border. Word-level fill is absent.
2. Open the **last 3-5 minutes of Ch 1**. Sentence-level highlight tracks normally - no more catastrophic drift on the tail (this was the worst symptom of the pilot's word-level output).
3. Confirm the sticky player's `⚠ sync stale` warning still fires when an MP3 is more than 1 hour newer than its alignment JSON.

## Background context for Yeoman

The forced-alignment pilot was a probe to see whether word-level timing accuracy could be lifted via aeneas. The pilot informed a decision; the decision is to drop word-level for now. The pilot's documentation remains in `.pao-inbox/_decisions/2026-05-07-forced-alignment-evaluation.md` for historical context.

If you want word-level back later, the path is **API STT** (Whisper-on-GPU via Inference Studio's transcriptions endpoint with `verbose_json` response format), with substitution-aware merge against the post-substitution audio script. The decision doc covers the schema. Aeneas is not the path forward - its tail-confidence-loss limitation is structural.
