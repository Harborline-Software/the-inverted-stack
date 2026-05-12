# Handcount Pilot — Prose Telemetry on the Filchner Trial Chapter

**Date:** 2026-05-12
**Author:** PAO + CO (live session)
**Status:** Discovery artifact; informs Phase 1 engineering session
**Source script:** `build/prose_telemetry_handcount.py` (stdlib-only)
**Source chapter:** `vol-2/act-1/ch01-departure.trial.md` (Bobiverse-register clean-slate trial)
**Output artifact:** `galley/build/the-inverted-stack/output/qa/ch01-departure.trial.prose-metrics.json`

---

## Purpose

Before Phase 1 engineering (Freestylo + StyloMetrix integration), validate three things by hand-implementation:

1. The `prose-metrics.json` schema (v2 from the architecture doc) actually serializes against real-chapter data.
2. The v1 detector logic (anaphora, tautology, asyndeton, polysyndeton, tricolon, epanorthosis) returns sane numbers on a real chapter.
3. Anna's new (Filchner / Bobiverse-register) trial chapter exhibits or does not exhibit the rhetorical-device problems CO flagged in the old Vol 2 prose.

## Headline result

**Trial chapter clears every threshold. Verdict: GREEN. No warnings, no blockers.**

This is the dramatic-improvement signal we hoped to see. The Bobiverse register fixed the original Vol 2 problems by structural change, not by linting.

## The numbers

| Device | Raw count | per 1k tokens | Sentence coverage | Old Vol 2 baseline (approx) | Verdict |
|---|---|---|---|---|---|
| **anaphora** | 1 run, max length 3 | 0.21 | 1.3% | 699 runs trapping 51% | ✅ clean |
| **tautological self-equation** | 1 | 0.21 | 0.4% | 100+ occurrences | ✅ clean |
| **asyndeton** | 51 | 10.47 | 22.3% | n/a (not flagged) | ⚠ register feature |
| **polysyndeton** | 20 | 4.11 | 8.7% | n/a (not flagged) | ⚠ register feature |
| **literal tricolon** | 13 | 2.67 | 5.7% | n/a (not flagged) | ⚠ register feature |
| **epanorthosis** | 4 | 0.82 | 1.7% | n/a (not flagged) | ✅ modest |

**Document-level:** 4,869 words, 229 sentences, 88 paragraphs. Median sentence 13 words; p90 = 52 words; longest = 91 words.

## What the findings tell us

### The original Vol 2 problems are gone

Anaphora collapsed from 699 runs / 51% coverage to **1 run / 1.3% coverage**. The single run found ("I told them…" in the wardroom briefing) is *intentional* cataloging — Anna inventorying what she briefed. Load-bearing parallelism, not decorative.

Tautology collapsed from 100+ to **1 occurrence** ("The cabin was the cabin"). That's Anna's deliberate one-off, used for character ("It always is. I have had this cabin on this boat on three prior missions and I do not redecorate"). Not a verbal tic.

The first conclusion: the structural register change — Bobiverse cadence, first-person past, parenthetical-rich sentences — kills the device-density problem by changing *what kind of sentences exist*, not by editing problematic sentences out. This is the right way to fix the problem.

### Asyndeton + polysyndeton + tricolon are register features now

Anna's voice naturally produces:
- Comma-runs without conjunctions: *"a patched rack, a scrubbed atmosphere, the logs"* (asyndeton)
- Cataloguing with deliberate conjunction repetition: *"the firmware, and the timestamps, and the official record"* (polysyndeton)
- Listing in threes: *"eleven people breathing recycled air, one she will not bury at sea, and a boat that needs to surface"* (tricolon)

These are now *signature* moves of the voice, not problems. The thresholds shouldn't fire on them — but they should be *measured* so we know if they climb into excess. Current densities (10.47, 4.11, 2.67 per 1k) are inside register; double those and the prose starts showing off.

### Long-sentence outliers are parenthetical-rich, not run-on

p90 = 52 and longest = 91 sound alarming but the top sentences are all *internally structured* — em-dashes, parentheticals, balanced clauses. They read aloud at audiobook pace without losing the listener. The Bobiverse register makes long sentences work because the rhythm has natural pauses.

**Caveat:** the detector flagged one 75-word "sentence" that's actually three short dialogue lines glommed together by the sentence-splitter (it doesn't handle `."` boundary correctly). That's a detector bug, not a real long sentence. Note for the engineering session.

## Schema validation

The v2 schema from the architecture doc serializes cleanly. All fields populated. JSON is consumable by the future QA-dashboard "Prose telemetry" chip.

One field-shape note: `detected_devices[]` has *heterogeneous* shapes per device (anaphora has `run_length` and `sentences[]`; tautology has `head` and `text`; asyndeton has `commas` and `sentence`). This is fine and probably correct — JSON Schema can express it as a discriminated union on `type` — but the Phase 1 engineering should formalize the per-device sub-schemas before publishing.

## Detector gaps surfaced

Hand-implementing the detectors with stdlib-only revealed three gaps the engineering session needs to address:

1. **Sentence segmentation needs to handle dialogue.** The naive regex `(?<=[.!?])\s+(?=[A-Z"])` misses `."` followed by another quoted line. spaCy will handle this; document the requirement.
2. **Asyndeton confidence is low (0.6).** The heuristic flags commas + tail-not-starting-with-conjunction, which catches a lot of false positives (compound modifiers, lists with implicit conjunction). Freestylo's asyndeton detector should be evaluated specifically against the trial chapter; if it produces fewer than the 51 hand-count hits, it's likely the more accurate detector.
3. **Isocolon (parallel grammatical structure across clauses) requires POS.** Skipped entirely in the handcount; needs spaCy. The engineering session should confirm Freestylo's isocolon coverage; this is the device that captures Anna's voice's *signature* parallel-clause moves and we'll want measurement on it.

## What this changes for the engineering session

1. **Freestylo's job in v1 is calibration, not catching unknown problems.** The trial chapter already clears the original Vol 2 problems; Freestylo's role is to *confirm* that and *measure register features* (asyndeton, polysyndeton, tricolon, isocolon) so we have empirical thresholds.
2. **First production target chapter is `ch01-departure.trial.md`.** It's clean; it produces a green baseline; subsequent measurements compare against it. The engineering session should ship Freestylo + StyloMetrix and reproduce the handcount numbers (plus isocolon) within ±10%. Reproducing the handcount = passing the integration test.
3. **Custom-detector list shrinks.** Tautological self-equation (the project-specific antipattern) probably stays custom — Freestylo unlikely to have it. The other six v1 detectors likely all exist in Freestylo or are derivable from spaCy primitives.
4. **Baseline run sequence:**
   - Phase 1.0: ship Freestylo + StyloMetrix integration
   - Phase 1.1: reproduce handcount numbers on `ch01-departure.trial.md` (validation)
   - Phase 1.2: run against all 18 Vol 2 chapters (corpus baseline)
   - Phase 1.3: run against the *old* `ch01-departure.md` (pre-trial draft) — comparison fixture, confirms register-change reduced the problem at the corpus level

## Files

- `build/prose_telemetry_handcount.py` — the stdlib hand-counter (this script)
- `galley/build/the-inverted-stack/output/qa/ch01-departure.trial.prose-metrics.json` — the measurement artifact

Both committable. The handcount script lives in this book repo (it's a calibration tool tied to this manuscript); the production tool will live in `galley/lib/prose_telemetry/` once Phase 1 ships.
