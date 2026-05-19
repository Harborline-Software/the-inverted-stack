---
type: resumed
chapter: cross-cutting (.wolf/anatomy.md)
last-pr: "#51, #57–#66"
in-reply-to: pao-directive-2026-05-01T04-32Z-anatomy-refresh-post-may-1-merges.md
---

**Verdict: anatomy refresh nearly complete on PAO's pre-existing pass.** Of the 13 files PAO listed, **12 already had anatomy entries** from prior auto-OpenWolf scans. **One was missing: `vol-1/closing/the-crossing.md`** - added.

## What was added

Added new `vol-1/closing/` section between `vol-1/appendices/` and `vol-1/epilogue/`:

```
## chapters/closing/

- `the-crossing.md` - The Crossing - closing chapter, first-person staff history
  (Anna Yusupova POV), five acts, Antarctic submarine mission, Diego Vargas
  death scene, architecture-as-protagonist (~5759 tok)
```

Token estimate via `wc -w × 1.3` per directive.

## What was already in anatomy.md (no action needed)

All 12 of these had existing entries from prior scans:
- `.pao-inbox/_creative/character-sheets/dr-leader-mission-director.md` (line 135)
- `.pao-inbox/_creative/character-sheets/_minor-characters.md` (line 134)
- `.pao-inbox/_creative/character-sheets/senior-technical-specialist.md` (line 137)
- `.pao-inbox/_creative/character-sheets/maria-santos.md` (line 136)
- `.pao-inbox/_creative/the-crossing-concept-note-2026-04-30.md` (line 130)
- `.pao-inbox/_decisions/antarctic-vision-chapter-concept-2026-04-30.md` (line 144)
- `.pao-inbox/_decisions/co-seat-deferred-structural-decisions-2026-04-30.md` (line 145)
- `.pao-inbox/_decisions/2026-04-30-upf-ch15-split-phase5-ch23-addendum.md` (line 141)
- `.pao-inbox/_decisions/2026-04-30-voice-pass-priority-queue.md` (line 142)
- `.pao-inbox/_decisions/2026-04-30-word-count-target-revision-proposal.md` (line 143)
- `.pao-inbox/_editorial-reviews/` block (lines 147–163; all 15 literary-board + compression + diagram-proposal files entered)
- `.pao-inbox/pao-directive-*.md` (lines 114–116; all three current directives entered)

## Stale-description flag for PAO judgment

The dr-leader entry currently reads:

> `dr-leader-mission-director.md` - Character Sheet - Dr. Aisha Al Mansoori, Mission Director (~2091 tok)

The character was renamed via PRs #57+#61: locked as **Anna Yusupova** (Russian, not UAE). The
file path is correct but the description's name is stale. Not in scope of additive anatomy
refresh; flagging for PAO if you want me to update the description text in a follow-up edit.

## Skipped per directive

- All ephemeral beacons (`yeoman-question-*.md`, `yeoman-resumed-*.md`) - directive explicitly
  excludes them from anatomy.

## Working tree

`.wolf/anatomy.md` modified (one new section added). Working tree dirty for PAO commit per
2026-04-29 commit-authority.

## Adjacent observation

OpenWolf's auto-scan apparently caught 12 of the 13 listed files between when PAO wrote the
directive and when I executed it (roughly the last hour). Only `vol-1/closing/the-crossing.md`
remained unindexed - possibly because the closing/ directory is new and the scanner hasn't picked
up the new directory yet. Worth investigating if directory-walk depth needs updating in the
OpenWolf config.
