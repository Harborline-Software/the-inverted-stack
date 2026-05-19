---
type: pao-directive
chapter: build/stt_spike.py + ch15 audio re-spike
priority: P3
parent-decision: .pao-inbox/_decisions/2026-05-04-stt-qc-spike-phase1-outcome.md
expected-output: yeoman-resumed-* beacon with whisper-medium ch15 results + Phase 3 decision recommendation
---

# PAO directive - STT QC Spike Phase 2: medium model on ch15 only

## Read this first

`.pao-inbox/_decisions/2026-05-04-stt-qc-spike-phase1-outcome.md` - the Phase 1 verdict, the asymmetric-results finding, and why ch15-with-medium is the focused next test.

## What you are doing

Re-run the spike script against `ch15-security-architecture.mp3` only, this time with the medium whisper model. Compare the REAL counts vs Phase 1's base-model 94. The question this answers: does whisper-medium make the round-trip STT approach adequate for technical chapters, or do we need to escalate further (large-v3 or pivot to forced alignment)?

## Phase 1 fix already in tree

PAO has already applied the regex fix you flagged (`_strip_inline_code` now preserves backtick content as words instead of replacing with empty space). Pull main; the fix is on `build/stt_spike.py`. Phase 2 should benefit immediately - the 8 package-name false-positives from Phase 1 should drop from REAL to VARIANT.

## Execution

```bash
# Pull main first to get the regex fix
git pull origin main

# Re-run with medium model
python3 build/stt_spike.py \
  --model medium \
  build/output/audiobook/ch15-security-architecture.mp3 \
  chapters/part-3-reference-architecture/ch15-security-architecture.md
```

Wall-time budget: **≤30 min** on Mac CPU int8 (medium is ~3× base; Phase 1 base was ~5 min so medium estimated ~15-20 min). If wall-time exceeds 45 min, abort and beacon back with timing data; we'll pivot to large-v3 or GPU dispatch in a follow-up directive.

## What to classify

Same four categories as Phase 1 (REAL / VARIANT / NOISE / FOREIGN), plus track these specifically:

1. **Math-notation REALs** - Greek letters (ε, λ, σ, δ). These were ~20 REALs at base. Medium should resolve most; if not, large-v3 is mandatory.
2. **Package-name false-positives** - should drop to ~0 REAL with the regex fix already applied.
3. **Homophone REALs** - `sync` → "sink", `writes` → "rights", `counsel` → "council". These are model-quality issues, not script-fixable.
4. **Large section drops** - rows where multiple consecutive source sentences are missing or replaced with garbage in the transcript. This is the highest-severity class. If medium still drops sections, the round-trip approach is structurally inadequate for technical chapters.

## Decision criteria for the beacon

Pick one of three verdicts based on the data:

- **Phase 2 PASS** - medium resolves >80% of base REALs (≤19 REALs total). Two-tier model strategy is viable: base for narrative chapters, medium for technical. Beacon recommends Phase 3 forced-alignment integration as the durable QC layer using these model assignments.
- **Phase 2 LOWER-PASS** - medium resolves 50-80% of base REALs (20-47 REALs total). Most of the gain is real; remaining REALs need analysis. Beacon recommends large-v3 sub-spike as the next test.
- **Phase 2 FAIL** - medium resolves <50% of base REALs (>47 REALs total). The model-quality lever isn't large enough to bridge the gap. Beacon recommends pivot directly to Phase 3 forced alignment with WhisperX, using its per-word confidence as the QC signal rather than a transcript diff.

## Deliverable

`yeoman-resumed-2026-05-04THH-MMZ-stt-spike-phase2-medium.md` with:

- Wall-time on medium model (so we can extrapolate to other chapters)
- REAL / VARIANT / NOISE / FOREIGN counts (and the per-class breakdown for REALs)
- 3-5 example REAL errors with timestamps (to spot-check whether medium understood the math notation)
- Phase 2 verdict (PASS / LOWER-PASS / FAIL) per the criteria above
- Recommendation for Phase 3 routing

Do not commit `build/stt_spike.py` re-edits or the new diff report. PAO will commit per the 2026-04-29 protocol when ready.

## Sequencing

P3. Below the P1 voice-pass work that is gated on CO (Tier 1 #45/#11/#43 hybrid dispatches) and below other P2 items. Pick this up only when you have a clear ~30-min slot and nothing higher-priority is in flight.

## What this is NOT

- Not a Phase 3 forced-alignment integration. That is conditional on this sub-spike's outcome.
- Not a re-run on ch01. Phase 1 already found base adequate for narrative.
- Not the audiobook listen-test verdict (that is a separate CO action on the silence-trim option A).

## Escalation triggers

- If medium wall-time exceeds 45 min on ch15: write yeoman-question-* with timing data; PAO routes to large-v3 OR Higgs/GPU box.
- If medium produces no improvement (REALs ≈ 94, same as base): write yeoman-question-* with one example diff region per error class; PAO escalates to Phase 3 directly.
- If medium dramatically over-improves (REALs ≈ 0): pause and re-verify - that's suspicious, suggests something changed about the input. Spot-listen the audio to confirm it matches the source you ran against.
