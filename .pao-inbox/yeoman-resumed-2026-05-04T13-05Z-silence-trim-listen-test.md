---
type: yeoman-resumed
chapter: build/m4b.py
last-pr: chore/pao-silence-trim-doc-and-directive
---

Silence-trim filter applied. Listen test requires CO (see below).

## Build script change applied

The directive specified `build/audiobook.py`. The ffmpeg concat is actually in
`build/m4b.py` — `audiobook.py` writes per-chapter MP3 bytes directly in Python
without an ffmpeg concat step. Applied to `m4b.py` instead.

Modified `cmd` list in `build/m4b.py` (before the `-c:a aac` line):

```python
cmd += [
    "-af", "silenceremove=stop_periods=-1:stop_duration=1.5:stop_threshold=-50dB",
    "-c:a", "aac", "-b:a", args.bitrate, "-ac", "1",
    "-movflags", "+faststart",
    str(args.out),
]
```

Defaults used: `stop_periods=-1`, `stop_duration=1.5`, `stop_threshold=-50dB` — per the
recommendation doc. One-line change; easy to revert or tune.

## the-crossing also relaunched

Simultaneously re-launched the-crossing regen (PID 15664, headless). Log:
`/tmp/audiobook-regen-logs/regen-the-crossing-2026-05-04.log`. Expected ~20-30 min.
See yeoman-resumed-2026-05-04T13-00Z-audiobook-regen-complete.md for context on the
Friday failure.

## Listen test — requires CO

Cannot perform the listen test autonomously (no audio playback). What CO needs to do:

1. PAO first commits the `build/m4b.py` change (Yeoman does not commit build scripts).
2. Run `python3 build/m4b.py` to assemble the full M4B from the 27 rendered chapters.
3. Listen end-to-end, or spot-check: last 30s of Ch 1 + first 5s of Ch 2 (inter-chapter
   junction), plus one mid-chapter stretch of 60s or more (intra-chapter beat check).
4. Specifically check: does any intra-chapter pause below 1.5s feel cut?
   - PAUSE_DURATIONS map (from audiobook.py): `....` = 1.2s (H2 break), `......` = 1.8s
     (H1 break). The H2 break at 1.2s is below the 1.5s stop_duration and may be
     affected. H1 break at 1.8s is above threshold and should be preserved.
5. If clean: option A is done. If an H2 intra-chapter beat got clipped: escalate to
   option B (per-chapter pre-concat trim) or lower stop_duration to 1.0s.

## Recommendation for listen-test scope

Suggest Ch 6 (council chapter, heavy H2 structure) rather than Ch 1 for the
intra-chapter beat check — more section breaks, faster to verify the 1.2s H2 pause
survives. Ch 1 is still the right chapter for cast-swap name pronunciation check.

## Pending PAO actions

1. Commit `build/audiobook.py` change (closing/the-crossing.md in CHAPTER_FILES)
2. Commit `build/m4b.py` change (silenceremove filter)
3. Merge `fix/yeoman-audiobook-add-crossing` or squash into current branch
4. Run listen test and issue verdict directive
