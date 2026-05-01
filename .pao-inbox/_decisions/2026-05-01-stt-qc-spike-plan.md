---
type: phased-plan
date: 2026-05-01
author: PAO
audience: CO (decision), Yeoman (execution if spike validates)
status: planned — execute early week of 2026-05-04
related-decisions:
  - audiobook-topology (project memory)
  - pao-directive-2026-05-01T04-31Z-audiobook-alignment-regen-post-cast-swap.md
---

# STT QC Spike — Phased Plan

## TL;DR

A 1-day spike to validate whether speech-to-text round-trip diffing catches real errors in the TTS-generated audiobook before committing to a more durable forced-alignment QC layer. The spike is scoped tight: 1–2 sample chapters, normalized diff against source text, decision gate at the end. If the spike validates the concept, Phase 3 commits to forced alignment as the durable QC. If it doesn't, we capture learnings and defer.

Execution window: **early week of 2026-05-04**. Owner: TBD (Yeoman likely; CO may run the spike personally if desired since it's small enough).

## Why this exists

The audiobook pipeline produces TTS audio from chapter markdown. Today there's no automated check that the audio matches the text — pronunciation errors, dropped words, hallucinated insertions, or voice-clone drift on technical terms / cast-swap names go undetected until human listening discovers them. A round-trip STT pass would catch the gross-error class before committing 25+ hours of audiobook to delivery.

Two QC mechanisms were considered:

1. **Round-trip STT → diff** (this spike): generated audio → STT transcript → normalize and diff against source text. Coarse but cheap.
2. **Forced alignment** (deferred to Phase 3): align generated audio against known source text using WhisperX or MFA, emit per-word confidence + timing. Direct fit but more setup.

The spike validates whether (1) catches enough real errors to be worth keeping, and whether the false-positive rate (punctuation noise, em-dash artifacts, foreign-language passages, acceptable pronunciation variants) is tolerable. If the spike's signal-to-noise ratio is poor, that strengthens the case to skip directly to forced alignment.

## Phase 0 — Discovery (1–2 hours)

Before any code is written:

1. **Inventory the pipeline.** Where do per-chapter WAV/MP3 files land after generation? What's the build entry point (`build/audiobook.py` per project anatomy)? What format does each chapter audio live in?
2. **Pick the STT model.** Default candidate: `whisper-large-v3` or `faster-whisper` for accuracy on technical content; fall back to `whisper-base` if the GPU host is busy. Confirm Mac vs Windows GPU placement (Higgs is on Windows GPU; STT can run there or on Mac CPU at lower speed).
3. **Pick scope of the spike.** Default: 1 chapter from Part 1 (narrative-heavy, lots of cast-swap names) + 1 chapter from Part 3 (technical, lots of cryptographic vocabulary). Recommend Ch 1 (Sabina, Joel, Priya, Maria, GCC, Belo Horizonte, Bangla phrase) + Ch 15 (DEK, KEK, AES-256-GCM, Argon2id, SQLCipher).
4. **Define the success criterion.** Spike passes if it surfaces ≥ 1 real TTS error per chapter that would have shipped uncaught, AND if the false-positive ratio is < 3:1 (≤ 3 false positives per real error). Lower bar: surfaces ≥ 1 real error per 5 chapters with FP ratio < 5:1 — still worth keeping. Below either bar: defer to forced alignment.

## Phase 1 — Spike execution (1 day, ≤ 8 hours)

1. **Generate or use existing audio.** If audiobook regen (queued Yeoman directive) has run by spike time, use those artifacts. If not, regenerate the two spike chapters specifically.
2. **Run STT on each chapter.** Capture full transcript + per-segment timestamps + per-segment confidence (Whisper exposes these via `verbose_json` output).
3. **Normalize source text + STT transcript.** Lowercase, strip punctuation, collapse whitespace, optionally strip code fences and HTML annotations. The normalized comparison is what gets diffed.
4. **Diff and categorize findings.** Each diff region falls into one of:
   - **Real error** — TTS dropped, duplicated, or mispronounced something
   - **Acceptable variant** — TTS pronounced correctly, STT transcribed differently (e.g., "Sabina" vs "Saabina")
   - **Punctuation/format noise** — em-dash, quotation, IPA, code-fence content; not actionable
   - **Foreign-language passage** — Bangla `shotti'r khata`, Spanish `María Elena Vargas`; STT confidence drops naturally; flag separately
5. **Tally the four categories per chapter.** Produce a small spike report: per-chapter count of each category, the real-error examples surfaced, the worst false-positive cluster.

Intermediate decision points:

- After running STT on first chapter: if the diff is already 90% punctuation noise, abort and reset normalization rules before continuing.
- After both chapters: pause and read the spike report end-to-end before declaring outcome.

## Phase 2 — Decision (1–2 hours)

Per the success criterion in Phase 0:

- **Spike passes** → write the durable-QC ADR, scope out Phase 3 (forced alignment) as a separate planning doc.
- **Spike inconclusive** → capture learnings, retry with different STT model or different chapters, or pivot directly to forced alignment.
- **Spike fails** → document why round-trip STT didn't surface enough signal, defer audiobook QC to a future revisit, accept that human-listening QC is the only available signal in the near term.

The decision goes in `.pao-inbox/_decisions/2026-05-XX-stt-qc-spike-outcome.md` regardless of result. Even a failed spike is useful — it pre-empts the temptation to retry the same approach later without remembering why it failed.

## Phase 3 — Forced alignment integration (deferred)

Out of scope for this spike. If Phase 2 validates the concept, Phase 3 plans:

- Pick alignment tool (WhisperX is the strongest candidate — Whisper-based, GPU-friendly, emits per-word confidence + word-level timing in one pass).
- Wire alignment into `build/audiobook.py` as a post-generation QC step.
- Define confidence thresholds for "review needed" segments.
- Produce QC report per chapter alongside the audio artifacts.
- Optionally: integrate with the cast-swap name pronunciation flagging the existing audiobook regen directive already asks Yeoman to do — forced alignment automates that flagging.

Phase 3 plan to be written only if Phase 2 validates.

## What this plan does NOT cover

- Forced alignment integration (Phase 3, deferred until spike validates).
- TTS retraining or voice-clone tuning (separate concern; the QC layer surfaces issues, doesn't fix them).
- Inter-chapter silence trim — see companion finding `2026-05-01-audiobook-silence-trim-recommendation.md` (separate post-processing concern, addressable independently of QC).
- Human-listening QC — orthogonal; durable QC layer is meant to *reduce* the volume of human listening, not eliminate it.

## Status

- Plan drafted: 2026-05-01.
- Execution window: early week of 2026-05-04. Owner TBD.
- Phase 0 discovery + Phase 1 spike: pending kickoff.
- Phase 2 decision: pending Phase 1 outcome.
- Phase 3 integration: deferred conditionally on Phase 2.
