---
type: pao-directive
audience: Yeoman (audiobook pipeline operation)
priority: high
related:
  - vol-2/act-*/ch*.md
  - build/audiobook.py
---

# PAO Directive - Vol 2 audio staleness audit + selective re-render queue

## What

Audit which of the 17 stale Vol 2 chapters need a fresh audio render, and run the renders for the ones that actually changed prose. Skip the ones where only frontmatter/tags moved.

## Why

The PAO mtime audit (2026-05-16T11:30Z) shows **17 of 18 Vol 2 chapters** have markdown newer than rendered audio:

```
STALE  12h   ch02-recruitment-interview        ← PAO already re-rendering (in flight)
STALE 132h   ch03-drake-passage-ice-edge
STALE 188h–191h  ch04 through ch18 (all)
```

The 186–191h cluster maps to commit `c48204a chore(vol-2): tag ch03-ch18 as pre-bobiverse pending rewrite` (2026-05-08). That commit likely just added a status tag to frontmatter - which the audio pipeline strips and would not change pronunciation. **Auditing first prevents 17 unnecessary 30-minute renders.**

## Classify-then-render

For each chapter ch03–ch18:

1. **Diff classification.** Run `git diff <prev-audio-render-commit>..HEAD -- vol-2/act-*/<chapter>.md` (find prev commit via mtime of the corresponding `.mp3` minus a buffer).
   - **Tag/frontmatter-only** (changes are all above the first `---` body separator) → mark `audio-current` in the audit; skip render.
   - **Prose change** (any change below the first body `---`) → queue for re-render.
2. **Build the re-render set** as a list of chapter slugs.
3. **Render the set on Kokoro (fast)** - `--engine kokoro --preset female-solo` (af_alloy @ 0.92 speed). This is a **draft re-render** after the Anna-voice rewrite pass (PAO 2026-05-16); the goal is to refresh the audio quickly for CO ear-test, not to ship final quality:
   ```
   python3 build/audiobook.py --engine kokoro \
     --preset female-solo --no-chapter-map \
     --only vol-2/act-X/chXX-... --force
   ```
   Kokoro is no-auth, ~2-5 min/chapter wall time. The full batch (16 chapters of stale-set, minus any classified tag-only) lands in well under an hour. Sentence-level cache will hit for unchanged paragraphs; only modified prose pays full chunk cost.
4. **Run renders serially**, not concurrently - even Kokoro can degrade under parallel load. Use a shell loop.
5. **Do NOT use chatterbox/ciufi-galeazzi** for this pass. Chatterbox is the final-render voice (per CO 2026-05-06) and takes ~45 min/chapter - ~12h wall time on the full set. The chatterbox final render is a **separate later pass** after CO ear-tests the fast Kokoro drafts and signs off on the text rewrite.

## Acceptance check

- A markdown audit table at `.pao-inbox/_state-snapshots/2026-05-16-vol2-audio-staleness-audit.md` showing each ch03–ch18 with its classification (`audio-current` vs `re-render-queued`) and one-line reason.
- For each `re-render-queued` chapter, a fresh MP3 with the `--af_alloy` suffix in `~/Library/CloudStorage/Dropbox/the-inverted-stack/vol-2/<slug>--af_alloy.mp3` with mtime newer than the markdown. (The unsuffixed `<slug>.mp3` is reserved for the final chatterbox render; do not overwrite it on the fast pass.)
- Buglog entries for any new render failures.

## What does NOT change

- Chapter-preset map: keep `--no-chapter-map` to force the preset PAO has chosen for this pass (Kokoro/female-solo/af_alloy).
- The Ch 2 chatterbox render that PAO ran on 2026-05-16 is already at the final-quality path; do not re-render Ch 2 on the fast pass.

## Coordination

If you find chapters with paragraph-fusion artifacts (similar to what PAO fixed in ch02), **stop and beacon back**. Those are paste-error symptoms of a "complete rewrite" - they need the canon/voice check before re-rendering.
