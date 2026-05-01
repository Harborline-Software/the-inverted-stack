---
type: recommendation
date: 2026-05-01
author: PAO
audience: CO (decision), Yeoman (execution)
status: recommendation — option A approved by CO 2026-05-01; directive issued same day
related:
  - audiobook-topology (project memory)
  - pao-directive-2026-05-01T04-31Z-audiobook-alignment-regen-post-cast-swap.md
  - 2026-05-01-stt-qc-spike-plan.md (companion audiobook QC concern)
---

# Audiobook Silence-Trim Recommendation

## Problem

Inter-chapter silence in the generated audiobook runs longer than listening pacing benefits from. The TTS pipeline (Kokoro on Mac, Higgs Audio v2.5 on Windows GPU) emits per-chapter audio with whatever leading/trailing silence the model produces; the concat step preserves that silence as-is, stacking long pauses at chapter junctions. Local post-processing can trim this without retraining the TTS or touching model output.

## Two options considered

### Option A — `ffmpeg silenceremove` at concat time

Add a single filter to the existing ffmpeg concat invocation in `build/audiobook.py`. The filter caps inter-segment silence to a configurable duration (1.5s default).

```
silenceremove=stop_periods=-1:stop_duration=1.5:stop_threshold=-50dB
```

- **Pros:** one-line change, no schema changes, ships in minutes, easy to revert.
- **Cons:** filter operates on the concatenated stream — it cannot distinguish "intentional pause inside chapter" from "dead air at chapter boundary"; conservative threshold (1.5s, -50dB) is the buffer against accidentally cutting intra-chapter beats.
- **Risk:** narrative pauses inside a chapter that exceed 1.5s of silence below -50dB will get clipped. Probability is low (TTS rarely produces > 1.5s silence outside chapter boundaries) but non-zero. Mitigation: listen to a sample chapter post-trim before committing to the change.

### Option B — per-chapter pre-concat trim

Strip leading + trailing silence from each chapter file individually (using `silenceremove` or `pydub.silence.detect_leading_silence` / `detect_trailing_silence`), then concatenate with a fixed 1.5s pause inserted between chapters.

- **Pros:** clean mental model — "intra-chapter pacing the TTS produced" is preserved; "inter-chapter spacing we choose deliberately" is configurable; no risk of clipping intra-chapter beats.
- **Cons:** more code (per-chapter pass + concat-with-explicit-pause), more state in the build, a small regression risk if the trim threshold is misset and clips the start of the first sentence.

## Recommendation

**Start with option A.** Ship the one-line change to `build/audiobook.py`, regenerate one chapter, listen end-to-end. If the result is clean (no intra-chapter beats clipped, junctions feel natural), declare done. If junctions still feel off OR an intra-chapter beat got clipped, escalate to option B as a follow-up.

Tunables to surface in the directive:
- `stop_duration` — default 1.5s; can lower to 1.0s if junctions still feel long, or raise to 2.0s if intra-chapter beats are being touched.
- `stop_threshold` — default -50dB; -45dB is more aggressive, -55dB is more conservative.

## What this is NOT

- Not a TTS model change (Kokoro/Higgs untouched).
- Not a re-prosing of the source markdown.
- Not the audiobook QC layer (that's the STT spike, separate).
- Not a fix for in-chapter pacing inside passages — only inter-chapter dead air.

## Status

- Recommendation drafted: 2026-05-01.
- CO decision: option A (start cheap, escalate to B only if needed).
- Yeoman directive: `pao-directive-2026-05-01T22-45Z-audiobook-silence-trim-option-a.md`, issued same day.
