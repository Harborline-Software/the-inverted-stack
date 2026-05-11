# Forced Alignment for Word-Level Whispersync — Evaluation

**Date:** 2026-05-07
**Author:** PAO
**Status:** **Pilot complete 2026-05-07. Outcome: revert to sentence-level highlighting (CO ear-test verdict 2026-05-08).** Word-level interpolation — whether across full chunks or within aeneas-derived sentence fragments — is always an estimate; CO's ear-test confirmed the estimate is visibly wrong. Sentence-level highlighting binds against ground-truth chunk timestamps and is the chosen direction. **API STT (`POST /api/v1/audio/transcriptions`) remains a viable future path** if word-level is reconsidered; aeneas is NOT the path forward (structural tail-confidence-loss limitation). See PAO directive `pao-directive-2026-05-08T01-54Z-revert-to-sentence-level-highlighting.md` for the Yeoman-side implementation directive.
**Related:**
- `.pao-inbox/co-session-2026-05-07T14-27Z-web-reader-enhancements.md` (the whispersync directive)
- `.pao-inbox/_decisions/2026-05-04-stt-qc-spike-phase1-outcome.md` (prior STT spike — different problem)
- `.pao-inbox/yeoman-resumed-2026-05-06T07-38Z-stt-spike-phase2-medium.md` (FAIL verdict on QC use case)

---

## Problem statement

The current word-level highlight in the web reader uses **linear interpolation across the chunk's duration** to estimate which word the listener is hearing right now. This assumes uniform speech rate within a sentence. The assumption is wrong for ciufi-galeazzi (Italian-cadenced cloned voice with non-uniform delivery) — and arguably wrong for any voice that punctuates, emphasizes, or pauses naturally. Drift is probably 200-500ms inside typical sentences and 1+ second on long sentences.

Better-quality whispersync alignment improves the reading-while-listening experience, and is a pre-publication artifact concern (Apple Books Whispersync-style media overlays expect word-level accuracy).

## Why STT was the wrong tool — and forced alignment is the right one

The prior STT QC spike (Phases 1 + 2, 2026-05-04 to 2026-05-06) had an open-vocabulary recognition problem: *"did the audio match the source word-for-word?"* Whisper had to recognize the text from scratch. It failed on math notation, hallucinated paragraphs as "thank you", confused homophones. **Verdict: FAIL.**

The whispersync alignment problem is the inverse: **the source text is known**; the aligner only has to localize where in the audio each known word is spoken. This is **forced alignment**, not full STT. Tools designed for it are computationally lighter, tolerant of pronunciation variation, and don't need to "recognize" anything — they only need to time-stamp.

| Tool | Notes |
|---|---|
| **API STT (`/api/v1/audio/transcriptions`)** | **Discovered 2026-05-07.** Whisper-on-Windows-GPU via Inference Studio. Multipart upload; returns `verbose_json` with word-level timestamps. No local install; same Bearer auth as TTS. **Recommended path for production.** |
| **aeneas** | Italian-developed; CMU Sphinx-based; explicitly designed for audio-to-text alignment for audiobooks + EPUB Media Overlays. CPU-only. Light install. Suitable as local-pilot fallback if API STT is unavailable. |
| `whisper-timestamped` | Whisper with a forced-alignment mode. Heavier; inherits Whisper's quality profile on non-English voices. |
| Montreal Forced Aligner (MFA) | Highest accuracy; phoneme-level; Kaldi-based; heavy install. Overkill for this case. |
| `gentle` | Older; works well on clean narration. |

**Production path: API STT** — `POST /api/v1/audio/transcriptions` with `file=<chapter>.mp3, model=whisper, response_format=verbose_json`. Returns word-level timestamps. Merge against the post-substitution script to produce the new alignment JSON.

**Why API STT works for forced-alignment-style use even though the prior STT QC spike FAILED:**

The QC spike measured *open-vocabulary recognition fidelity* — "did Whisper transcribe the audio correctly?" Verdict FAIL because of math notation, hallucinations, homophones.

Forced-alignment uses Whisper's **timing data** + the **known source script**. The merge layer aligns Whisper's recognized-word stream against the source script via edit-distance matching; mistranscribed words get their timing from the matched source word. Whisper's recognition errors don't break the merge — they just have to localize *roughly* where each spoken word is, and the source-side match catches everything else.

**Pilot fallback: aeneas** — if the API STT pilot reveals unexpected merge issues, aeneas is a CPU-only local alternative that works on the same audio + text inputs.

## Substitution-awareness — required for the merge

Audio glossary substitutions create text divergence:

- **Print source:** *"the Bridge replication credentials"*
- **Spoken audio:** *"the cloud-side replication credentials"*

The aligner needs to know which print word corresponds to which audio word. Two integration patterns:

### Option A (recommended) — align against the substituted script

The aligner sees the audio and the post-substitution script (what `audiobook.py` already passes to TTS). It produces per-word timing for the AUDIO-SIDE text. The web reader's data layer maps audio-side word indices back to print-side word indices via the substitution table. Cleaner data; UI does the mapping.

### Option B — align against the print source directly

The aligner has to skip insertions and tolerate replacements. Doable but messy; alignments drift at substitution boundaries.

**Recommend Option A.** Keep the alignment honest to what was spoken; do the print↔audio mapping explicitly in the dataset.

## Schema extension

The current `_alignments/<chapter>.json` has only sentence-level boundaries (`start_seconds`, `end_seconds`, `duration_seconds`, `text`). Extend each chunk with a `words[]` array:

```json
{
  "chunk_id": "ch01-departure-c0090",
  "start_seconds": 532.4,
  "end_seconds": 537.1,
  "audio_text": "I had read the press cycle from Saint Petersburg",
  "source_text": "I had read the press cycle from St. Petersburg",
  "words": [
    { "audio": "I",          "audio_idx": 0, "source": "I",          "source_idx": 0, "start": 532.40, "end": 532.51 },
    { "audio": "had",        "audio_idx": 1, "source": "had",        "source_idx": 1, "start": 532.51, "end": 532.69 },
    { "audio": "read",       "audio_idx": 2, "source": "read",       "source_idx": 2, "start": 532.69, "end": 532.95 },
    { "audio": "the",        "audio_idx": 3, "source": "the",        "source_idx": 3, "start": 532.95, "end": 533.06 },
    { "audio": "press",      "audio_idx": 4, "source": "press",      "source_idx": 4, "start": 533.06, "end": 533.42 },
    { "audio": "cycle",      "audio_idx": 5, "source": "cycle",      "source_idx": 5, "start": 533.42, "end": 533.81 },
    { "audio": "from",       "audio_idx": 6, "source": "from",       "source_idx": 6, "start": 533.81, "end": 534.07 },
    { "audio": "Saint",      "audio_idx": 7, "source": "St.",        "source_idx": 7, "start": 535.84, "end": 536.21, "substituted": true },
    { "audio": "Petersburg", "audio_idx": 8, "source": "Petersburg", "source_idx": 8, "start": 536.21, "end": 537.05, "substituted": true }
  ]
}
```

The `substituted: true` flag also unlocks the hover-diff feature from the QA dashboard proposal — when a print word is highlighted that corresponds to a substituted audio word, the UI can show the print/audio diff inline.

## Pilot scope

**Vehicle:** Ch 1 (just rendered Chatterbox-final at 24.2 min, 258 chunks, 22.16 MB).

**Iteration cost reduction — use Kokoro draft mode for the alignment iteration loop.**

Kokoro renders Ch 1 in single-digit minutes (vs Chatterbox's 21.8 min). Forced alignment work iterates faster against the draft MP3. Once the alignment pipeline is validated, re-run against the Chatterbox final render — the forced-aligner has no engine dependency.

**Pilot steps:**

1. Render Ch 1 with Kokoro local engine + draft preset → produces a draft MP3 in single-digit minutes. Use multi-track convention (`{slug}--{voice}.mp3`) so the Chatterbox final isn't overwritten.
2. Install aeneas in a Python venv (CPU-only; no GPU dependency).
3. Run aeneas against the draft MP3 + the post-substitution script. Produce per-word timing JSON in the schema above.
4. Web reader reads the new alignment JSON; eyeball-test highlight quality on Ch 1 in the website.
5. **Decide:** does highlight quality lift justify the alignment-rebuild cost across all chapters?
6. **If yes:** extend `audiobook.py` to call aeneas after MP3 concatenation; align all rendered chapters; rebuild alignment JSONs in the new schema.
7. **If no:** keep linear interpolation; the spike was a cheap probe.

**Success criteria for pilot:**

- Aeneas runs to completion on the Ch 1 draft MP3 without crashing
- Output JSON has plausible per-word timings (no obvious garbage)
- Web reader displays the new alignment without crashing
- Highlight follows ciufi-galeazzi voice **noticeably more accurately** than linear interpolation (qualitative; CO ear-test)
- Substitution-aware print↔audio mapping renders correctly on at least one substituted phrase (e.g., the Saint Petersburg moment in Ch 1)

## Out of scope for v1 pilot

- Per-phoneme alignment (just per-word)
- Cross-chapter batch alignment (just Ch 1)
- Alignment quality metrics / drift measurement (just eyeball validation)
- Integration into `audiobook.py` rendering pipeline (just standalone script for now)

## Tooling impact

If the pilot lands, this adds:
- `aeneas` (or whichever tool wins) to the project's tooling baseline
- A new `build/align_words.py` script
- Possible new step in the `audiobook.py` post-render flow (call aeneas after MP3 concat)
- New schema in `vol-1/_voice-drafts/_alignments/` JSONs (web reader needs to handle both old and new schema gracefully)

## Filed for engineering session

This document + the pilot task (#12) drive the next forced-alignment investigation. Pilot success determines whether the technique scales to all chapters.
