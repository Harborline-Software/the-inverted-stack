---
type: yeoman-resumed
chapter: build/stt_spike.py + ch15 audio phase2
last-pr: n/a
---

# STT QC Spike Phase 2 - Verdict: FAIL

## Wall-time

1963s (32.7 min). RTF=0.62 on Mac CPU int8 (394% CPU, 4-core burst). Medium is
~6.5× slower than base (not 3× as estimated). This makes medium impractical for
systematic multi-chapter runs; each 48MB chapter would take ~30+ min.

## Counts

| Category | Phase 1 (base) | Phase 2 (medium) | Delta |
|---|---|---|---|
| Total diff regions | 281 | 230 | −51 |
| REAL | 94 | 66 | −28 (−29.8%) |
| VARIANT | 163 | 136 | −27 |
| NOISE | 17 | 21 | +4 |
| FOREIGN | 7 | 7 | 0 |

**REAL per class:**

| Class | Count | Notes |
|---|---|---|
| Math notation (ε, λ, σ, δ) | 17 | ~20 in Phase 1; minimal improvement |
| role→row/roll mispronunciation | 15 | Systematic; voice-model issue; unfixable by STT upgrade |
| Large section drops + hallucinations | 13 | 3× "thank you" insertions; 3× paragraph-length drops |
| Homophone errors | 12 | writes→rights ×5; surface→service; floors→flaws; etc. |
| Package-name false positives | 2 | Down from 8 (inline_code fix worked) |
| Other word substitutions | 7 | compellable→compatible; 2018→2010; per→pair; etc. |

## Example REAL errors

1. **Region 154** - `λ 1 ε` → "deferrin" (Greek letter math notation → complete gibberish;
   medium shows no improvement on ε/λ/σ relative to base)

2. **Region 81** - ~100-word KEK rotation paragraph → "thank you" (section-level hallucination;
   TTS reads a block the model cannot transcribe and inserts a filler utterance)

3. **Region 212** - ~500-word security-properties table + surrounding paragraphs → single word
   "book" (catastrophic section-level drop)

4. **Regions 26–30** - "writes/write" → "rights/right" × 5 (homophone error; TTS pronounces
   correctly but STT conflates; not fixable by model upgrade)

5. **Region 161** - `λ` → "w1 for query number1 per query number01 adding" (single Greek letter
   expanding to word-salad; illustrates that medium decodes false confidence around math)

## Phase 2 verdict: FAIL

66 REAL errors against a 47-REAL LOWER-PASS threshold and a 19-REAL PASS threshold.
Medium resolves 29.8% of base REALs - below the 50% threshold for even LOWER-PASS.

The model-quality lever is not large enough. The primary failure classes (math notation,
large section drops, systematic homophones) do not respond to model size in this domain.
Spending large-v3 compute on this chapter would reduce the ~2 remaining package-name REALs
further but cannot fix Greek-letter garbling, "thank you" hallucinations, or role→row.

## Phase 3 recommendation

Per Phase 2 FAIL criteria: pivot directly to **Phase 3 forced alignment with WhisperX**.
Use per-word confidence as the QC signal rather than a transcript diff.

Specifically:
- WhisperX forced alignment gives word-level timestamps + confidence; low-confidence words
  flag TTS pronunciation issues without requiring full transcript accuracy
- Math-notation sections can be flagged by low-confidence clusters → reviewed by a human
  listener rather than normalized for comparison
- Large section drops would surface as timestamp gaps (silence-without-words > threshold)
- The "role→row" pattern would appear as consistent low-confidence on a specific token

The round-trip STT diff approach is structurally inadequate for this technical chapter.
WhisperX forced alignment + confidence-scoring is the adequate alternative.

**Yeoman has no further Vol 1 STT action pending.** Per P0 directive 2026-05-05, all Vol 1
audio QC work (including Phase 3 routing) is deferred to the post-Vol-2 period unless
CO/PAO explicitly reactivates. Beacon delivered per Phase 2 directive protocol.
