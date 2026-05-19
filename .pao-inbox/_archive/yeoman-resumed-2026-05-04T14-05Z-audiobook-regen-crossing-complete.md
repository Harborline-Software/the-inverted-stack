---
type: yeoman-resumed
chapter: closing/the-crossing.md
last-pr: fix/yeoman-audiobook-add-crossing
---

The-crossing regen re-run complete: exit 0.

- **Output:** `build/output/audiobook/the-crossing.mp3` (29 MB)
- **Wall time:** 1752s (29 min, Chatterbox on Windows GPU box)
- **Root cause of Friday failure:** working tree switched to `chore/pao-silence-trim-doc-and-directive`
  mid-run while PAO prepared the silence-trim commit (22:45Z). Python re-reads `build/audiobook.py`
  from disk on each call; when the branch switched, `closing/the-crossing.md` was gone from
  CHAPTER_FILES in the working tree.
- **Fix applied:** `closing/the-crossing.md` added back to CHAPTER_FILES in working tree
  (`build/audiobook.py`, line 438). Not committed - awaiting PAO commit per commit-authority
  directive. The same fix also exists on branch `fix/yeoman-audiobook-add-crossing` (commit 659f394);
  PAO can squash or cherry-pick as preferred.

**Full regen summary (all 7 chapters now complete):**

| Chapter | Status | MP3 size | Date |
|---|---|---|---|
| ch01-when-saas | exit 0 | 55 MB | 2026-05-01 |
| ch03-inverted | exit 0 | 22 MB | 2026-05-01 |
| ch15-security | exit 0 | 48 MB | 2026-05-01 |
| ch16-persistence | exit 0 | 36 MB | 2026-05-01 |
| ch22-security | exit 0 | 37 MB | 2026-05-01 |
| ch23-endpoint | exit 0 | 55 MB | 2026-05-01 |
| the-crossing | exit 0 | 29 MB | 2026-05-04 |

Manifest updated at `build/output/audiobook/manifest.json`.
