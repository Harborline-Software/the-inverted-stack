---
type: phase-2-decision
date: 2026-05-04
author: PAO
audience: CO (decision: confirm Phase 2 sub-spike), Yeoman (Phase 2 execution)
status: Phase 1 LOWER-PASS → Phase 2 sub-spike recommended
parent-decisions:
  - 2026-05-01-stt-qc-spike-plan.md (the spike plan)
yeoman-beacon: ../yeoman-resumed-2026-05-04T13-30Z-stt-spike-phase1-complete.md
---

# STT QC Spike - Phase 1 Outcome + Phase 2 Decision

## TL;DR

Phase 1 ran two chapters (ch01 narrative, ch15 crypto/security) through faster-whisper base. The spike **LOWER-PASSES** the success criterion (≥1 REAL per 5 chapters with FP ratio < 5:1) on both chapters. **The findings are not symmetric** - base is **marginally usable for narrative prose, inadequate for technical/crypto prose**. Phase 2 should run a focused sub-spike: whisper-medium on ch15 only, to determine whether medium resolves the math-notation garble + large-section drops that make base unusable for technical content.

## Phase 1 results vs success criterion

Per `2026-05-01-stt-qc-spike-plan.md` Phase 0 success criterion:
- **PASSES** if ≥1 REAL per chapter AND FP ratio (NOISE+VARIANT):REAL < 3:1
- **LOWER-PASSES** if ≥1 REAL per 5 chapters with FP ratio < 5:1
- **FAILS** otherwise

| Chapter | REAL | VARIANT | NOISE | FOREIGN | FP ratio | Verdict |
|---|---:|---:|---:|---:|---:|---|
| ch01 (narrative) | 53 | 200 | 10 | 2 | 3.96:1 | **LOWER-PASS** (above 3:1, below 5:1) |
| ch15 (crypto/security) | 94 | 163 | 17 | 7 | 1.91:1 | **PASS** (within 3:1 cutoff) |

Aggregate: 147 REAL across 2 chapters = 73.5 REAL per chapter on average. Both clear the lower bar; ch15 clears the upper bar.

## What "PASS" obscures: the asymmetry between narrative and technical

The numerical pass conceals the structural finding. Phase 1 surfaced two distinct error profiles:

### Narrative chapter (ch01) - base is marginally adequate

Dominant REAL classes:
- **Time-digit corruption** (×6): "4:47" → "4:07", "9:30" → "9:000 tree". Systematic base-model failure on two-digit time components after decimal context.
- **Medication name** (×2): "sulfa" → "sulfur" - medically significant in the asthma scene; would need flagging on listen.

Dominant VARIANT classes (false positives, not errors):
- **Acronym expansion** (~50): TTS expands `saas` → "software as a service" before reading; STT transcribes the expansion.
- **Proper-noun phonetics**: `priya` → "prier/preer", `pune` → "pooner".
- **Number words ↔ digits**: "twenty" ↔ "20".

Verdict: A medium-attention listener could follow base-model output and would flag ~53 items per chapter for human review. **Adequate for narrative-chapter QC.**

### Technical chapter (ch15) - base is inadequate

Dominant REAL classes:
- **Math notation** (×~20): Greek letters (ε, λ, σ, δ) garbled or dropped throughout. Critical for §Privacy-Preserving Aggregation (DP epsilon-budget).
- **Package-name false-insertions** (×8): TTS reads ``Sunfish.Kernel.Security`` aloud; STT transcribes "sunfish kernel security"; spike script's `_strip_inline_code` regex was eliding the source content, so TTS-spoken words appeared as inserted REAL errors. **Script-level bug, fixed in this PR** (preserve backtick content as words).
- **Critical homophones** (×8 across two patterns): `sync` → "sink" (×3, distributed-systems term), `writes` → "rights" (×5, CRDT term), `counsel` → "council" (×1).
- **Large section drops**: rows 71-72, 75-78, 81, 160, 238, 250-251 - multiple consecutive sentences dropped or replaced with garbage. **Listeners would miss entire functional specifications.**

Verdict: Base-model output cannot be used as the durable QC layer on technical chapters. Math notation garbled; section drops mean an entire normative paragraph could be silently broken without flagging.

## Spike-script fix applied

Per Yeoman's flag, `build/stt_spike.py:_strip_inline_code` was replacing backtick-wrapped content with empty space, producing false REAL "insertions" when TTS spoke the package name aloud. **Fix:** preserve content as words (`re.sub(r"\`([^\`]+)\`", r" \1 ", text)`), letting downstream punctuation-strip align `Sunfish.Kernel.Security` (source) with "sunfish kernel security" (transcript). Phase 2 re-run on ch15 should drop the 8 package-name false-positives from REAL to VARIANT.

## Phase 2 decision: focused sub-spike on ch15 with medium

Two paths considered:

### Path A - Re-run Phase 1 with whisper-medium on ch15 only

Cost: ~10-20 min wall-time on Mac CPU (medium is ~3× base; ch15 was ~5 min on base; medium estimated 15-20 min).

Decision criteria:
- If medium resolves >80% of ch15 REALs (94 → ≤19), declare medium adequate for technical chapters; finalize Phase 2 outcome doc with two-tier model selection (base for narrative, medium for technical).
- If medium still fails on math-notation drop / large-section drop, escalate to large-v3 (estimated 45-60 min wall-time on Mac CPU) or pivot to GPU host once Higgs is back.
- If even large-v3 fails, the round-trip STT approach is fundamentally inadequate for technical chapters → defer technical-chapter QC to Phase 3 (forced alignment via WhisperX).

### Path B - Skip directly to Phase 3 (forced alignment)

Cost: ~1-2 hours setup + integration into `build/audiobook.py` as post-generation QC step.

Risk: forced alignment also depends on STT model quality. If whisper itself can't transcribe Greek letters or package names cleanly, alignment confidence will be low on those segments anyway. Path A first establishes whether the underlying model can handle the content before committing to alignment integration.

### Recommendation: Path A

Run a focused sub-spike. If medium resolves the technical-chapter problems, we have a proven two-tier QC layer for ~30 min of Yeoman time. If medium still fails, we have empirical grounds to choose between large-v3, GPU dispatch, or forced-alignment escalation.

## Phase 2 directive scope

The PAO directive PAO will issue (separately, not in this commit) asks Yeoman to:

1. Apply the spike-script regex fix already in this PR (`build/stt_spike.py`).
2. Re-run on ch15 with `--model medium` (or the equivalent faster-whisper model).
3. Re-classify the diff regions, focusing on whether the 94 REALs from base drop substantially.
4. Tally REALs by class (math-notation / package-name / homophone / drop / other) so the residual REAL profile after model upgrade is interpretable.
5. Beacon back with the diff report path + the verdict.

Wall-time budget: ≤30 min ch15 alone with medium. If exceeded, abort and escalate to large-v3 in a follow-up.

## What this is NOT

- Not a Phase 3 commitment. Forced-alignment integration remains conditional on Phase 2's outcome.
- Not a re-run of ch01. Phase 1 found base is marginally adequate for narrative; re-running narrative with medium is unnecessary unless we want a single-model story instead of two-tier.
- Not a TTS fix. Math notation garble could ALSO be fixed at the TTS side (Higgs Audio v2.5 voice tuning); that's a separate concern out of scope here. The QC layer is meant to surface issues, not fix them at source.
- Not the listen-test verdict. CO still has the silence-trim option-A listen test pending; that's orthogonal to this STT QC pipeline.

## Status

- Phase 0 discovery: completed PAO 2026-05-04 (PR #75 directive).
- Phase 1 spike: completed Yeoman 2026-05-04 (commit 7c616d0; beacon 13:30Z).
- Phase 2 decision: this doc.
- Phase 2 sub-spike: pending PAO directive + Yeoman execution.
- Phase 3 forced-alignment: deferred conditionally on Phase 2 sub-spike outcome.
