---
type: yeoman-resumed
chapter: build/audiobook.py
last-pr: fix/yeoman-audiobook-add-crossing
---

Audiobook regen (7 chapters, headless, PID 67494) ran 2026-05-01 18:47–22:38. Six
chapters succeeded; the-crossing failed.

## Results

| Chapter | Status | Wall time |
|---|---|---|
| ch01-when-saas | exit 0 | 39 min |
| ch03-inverted | exit 0 | 25 min |
| ch15-security | exit 0 | 33 min |
| ch16-persistence | exit 0 | 35 min |
| ch22-security | exit 0 | 43 min |
| ch23-endpoint | exit 0 | 55 min |
| the-crossing | **exit 2** | <1s |

## the-crossing failure

Root cause: `closing/the-crossing.md` was not in CHAPTER_FILES when the-crossing
chunk ran at 22:37. The fix (commit 659f394 on `fix/yeoman-audiobook-add-crossing`)
was on a branch that was checked out when the wrapper launched (18:47), but the
working tree switched to `chore/pao-silence-trim-doc-and-directive` before 22:37
while the PAO prepared the silence-trim commit (22:45Z). Python reads the file from
disk each call — when the branch switched, the fix was gone.

Fix re-applied to current working tree (`build/audiobook.py` line 438). The-crossing
re-launched headlessly — see yeoman-resumed-silence-trim beacon for details.

## Pronunciation flags (cast-swap names)

These names appear in the chapters that rendered and are worth a listen pass:

- **Sabina** (ch01, ch03) — per directive; Eastern European name, likely reads cleanly
- **Joel** (ch01, ch03) — common English name, low risk
- **Priya** (ch15, ch22) — Indian name; Chatterbox tends to handle this well
- **María Elena** (ch22) — Spanish double-name; the accent on "María" is the risk;
  Chatterbox v2.5 handles Unicode but the space between names can cause a pause

No programmatic check is possible without listening. These are flags for CO's listen pass.
