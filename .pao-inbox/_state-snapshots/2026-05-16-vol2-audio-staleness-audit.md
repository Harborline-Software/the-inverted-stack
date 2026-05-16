---
type: state-snapshot
date: 2026-05-16
subject: Vol 2 audio staleness audit — ch03–ch18
auditor: Yeoman (PAO directive)
---

## Summary

All 16 stale chapters (ch03–ch18) are classified **audio-current**. No re-renders required.

**Root cause of staleness:** commit `c48204a` (2026-05-14, "chore(vol-2): tag ch03-ch18 as
pre-bobiverse pending rewrite") touched all 16 files, making them newer than the May 8
`--af_alloy` MP3 renders. However, every change in that commit is audio-transparent:

- `icm-stage: icm/draft` → `icm-stage: icm/pre-rewrite` (YAML frontmatter — stripped by
  `narratable_text()` frontmatter regex before TTS)
- Added `<!-- PRE-BOBIVERSE DRAFT... -->` HTML comment banner after closing `---` (stripped
  by `re.sub(r"<!--.*?-->", "", t)` at `build/audiobook.py` line 968–969)

No prose below the frontmatter block was modified in any chapter.

**Verification method:** `git diff c48204a..HEAD -- vol-2/act-*/ch*.md` returned empty for
all 16 chapters (no commits after c48204a touched ch03–ch18). `git show c48204a` confirmed
every file's diff was limited to the YAML `icm-stage` field and the HTML banner insertion.

## Audit Table

| Chapter | Classification | Reason | Action |
|---|---|---|---|
| ch03 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch04 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch05 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch06 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch07 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch08 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch09 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch10 | audio-current | c48204a: HTML banner only (ch10 has no frontmatter); stripped before TTS | skipped |
| ch11 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch12 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch13 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch14 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch15 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch16 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch17 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |
| ch18 | audio-current | c48204a: icm-stage field flip + HTML banner only; both stripped before TTS | skipped |

## Paragraph-fusion artifact check

No paragraph-fusion artifacts were detected. These chapters are pre-bobiverse Janeway-register
drafts that have not been touched since their migration into the repo (c2f0460). The c48204a
commit adds banners and flips metadata only — no paste operations occurred.

## Re-render queue

**Empty.** Zero chapters require re-render.

Existing `--af_alloy` renders (all dated 2026-05-08) remain valid against current prose:

| Chapter | MP3 file | Size |
|---|---|---|
| ch03 | ch03-drake-passage-ice-edge--af_alloy.mp3 | 24.9 MB |
| ch04 | ch04-first-submersion--af_alloy.mp3 | 27.4 MB |
| ch05 | ch05-day-twenty-realization--af_alloy.mp3 | 31.2 MB |
| ch06 | ch06-first-surface-first-forsaken-reveal--af_alloy.mp3 | 25.0 MB |
| ch07 | ch07-joels-sunfish--af_alloy.mp3 | 23.4 MB |
| ch08 | ch08-second-submersion--af_alloy.mp3 | 25.9 MB |
| ch09 | ch09-sync-daemon-under-drift--af_alloy.mp3 | 31.1 MB |
| ch10 | ch10-aftermath-mission-that-once-was--af_alloy.mp3 | 26.4 MB |
| ch11 | ch11-second-surface-second-forsaken-reveal--af_alloy.mp3 | 27.1 MB |
| ch12 | ch12-beginning-of-the-end--af_alloy.mp3 | 25.2 MB |
| ch13 | ch13-schema-that-should-not-migrate--af_alloy.mp3 | 58.3 MB |
| ch14 | ch14-the-crossing--af_alloy.mp3 | 63.6 MB |
| ch15 | ch15-compromised-relay-holds--af_alloy.mp3 | 46.6 MB |
| ch16 | ch16-final-ascent--af_alloy.mp3 | 26.3 MB |
| ch17 | ch17-transit-north--af_alloy.mp3 | 29.7 MB |
| ch18 | ch18-punta-arenas-surfacing--af_alloy.mp3 | 40.6 MB |

## Note on ch02

ch02 excluded from this audit per directive — PAO already handled with final-quality
chatterbox render. The `--af_alloy` render exists at
`ch02-recruitment-interview--af_alloy.mp3` (Dropbox) for reference.

## Pipeline note

These chapters carry `<!-- PRE-BOBIVERSE DRAFT -->` banners marking them as awaiting rewrite
in the Anna-voice / Filchner register. The existing `--af_alloy` Kokoro renders are
**listen-test drafts only** — not for assembly. When rewrite passes occur on a `draft/chXX`
branch, each rewritten chapter will need a fresh render before assembly QC.
