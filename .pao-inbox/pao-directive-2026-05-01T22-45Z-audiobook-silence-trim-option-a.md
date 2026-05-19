---
type: pao-directive
chapter: build/audiobook.py
priority: P2
parent-decision: .pao-inbox/_decisions/2026-05-01-audiobook-silence-trim-recommendation.md
expected-output: yeoman-resumed-* beacon with audio sample + listen-test verdict; PAO commits the build script change
---

# PAO directive - audiobook silence-trim option A (ffmpeg silenceremove)

## Read this first

`.pao-inbox/_decisions/2026-05-01-audiobook-silence-trim-recommendation.md` - the recommendation doc carries the framing, the two options considered, the chosen path (option A), and the tunable defaults. Read it before touching `build/audiobook.py`.

## What you are doing

Add the `silenceremove` filter to the existing ffmpeg concat invocation in `build/audiobook.py`. Default tunables from the recommendation:

- `stop_periods=-1` (apply across the whole stream)
- `stop_duration=1.5` (cap silence to 1.5s)
- `stop_threshold=-50dB` (silence floor)

The filter clause: `silenceremove=stop_periods=-1:stop_duration=1.5:stop_threshold=-50dB`.

Wire it into the existing ffmpeg call as an audio filter (`-af "..."` if no other filters present, or appended via comma if other filters already exist).

## Verification protocol

1. Pick one chapter for the listen test. Recommend Ch 1 (longest, most varied pacing, includes cast-swap names).
2. Regenerate audio for that one chapter through the modified pipeline.
3. Listen end-to-end. Specifically check:
   - Inter-chapter junction (if Ch 1 is concatenated against another chapter in the test): does the gap feel natural, not abrupt?
   - Intra-chapter beats: are paragraph-end pauses, narrative rests, and dialogue pauses all preserved? Anywhere a beat got clipped is a finding.
   - Cast-swap-name pronunciation: while listening, flag any names that sound off (Sabina, Joel, Priya, Maria); this overlaps with the audiobook regen directive's pronunciation pass.
4. If clean: declare option A successful, write the resumed beacon.
5. If a beat got clipped or junction still feels long: don't tune in this directive - write `yeoman-question-*.md` to PAO with the specific finding; PAO escalates to option B follow-up directive.

## Deliverable

`yeoman-resumed-2026-05-01THH-MMZ-silence-trim-listen-test.md` with:
- Confirmation of the build script change applied (paste the modified ffmpeg line)
- Listen-test verdict (clean / needs option B / tune the threshold)
- Any pronunciation findings discovered during the listen pass
- Audio sample saved to whatever directory your audiobook pipeline uses for spot-check artifacts; reference its path in the beacon

Do not commit the `build/audiobook.py` change. Per the 2026-04-29 directive, PAO commits build/manuscript changes; Yeoman edits.

## Sequencing

This is P2. The P1 audit + Phase 4a directives take priority. If you pick this up alongside the audiobook regen directive (P2 in the same queue), bundle them - the regen run produces the audio you'd be listening to anyway. Single resumed beacon for both is fine.

## What this is NOT

- Not a model change.
- Not a re-prosing pass.
- Not the audiobook QC layer (that's the STT spike, deferred to early week of 2026-05-04).
- Not a multi-threshold tuning exercise - one default attempted, listen test, escalate if needed.
