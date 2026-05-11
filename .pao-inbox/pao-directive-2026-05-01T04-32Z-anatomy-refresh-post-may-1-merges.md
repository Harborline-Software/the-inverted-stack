---
type: pao-directive
chapter: cross-cutting (.wolf/anatomy.md)
last-pr: "#51, #57–#66 (all merged 2026-04-30 → 2026-05-01)"
priority: P3
expected-output: yeoman-resumed-* beacon; anatomy.md updated; PAO commits
---

# PAO directive — refresh `.wolf/anatomy.md` after the cast-swap + Phase 7 + Crossing landing

## Context

Per OPENWOLF protocol: "After creating, deleting, or renaming files: update `.wolf/anatomy.md`." Sixteen PRs landed between 2026-04-30 and 2026-05-01 that created or significantly modified files outside the existing anatomy entries. Most of the additions are under `.pao-inbox/_creative/` and `.pao-inbox/_decisions/`, plus one new chapter file (`vol-1/closing/the-crossing.md`). The current anatomy.md does not reflect any of this.

## What you are doing

Read `.wolf/anatomy.md` end-to-end. Run `git diff main HEAD~50 -- '*.md' '.pao-inbox/' 'chapters/closing/'` (adjust the depth to capture all of 2026-04-30 + 2026-05-01) to see what's new. For each new file ≥ 1 KB or load-bearing on the manuscript, add a 2–3 line entry to anatomy.md following the existing convention: path → 1–2 sentence description → token estimate (use `wc -w` × 1.3 as a rough proxy).

Specifically these new files need entries:

- `vol-1/closing/the-crossing.md` (4,430 words; the closing chapter; first-person staff history, Anna POV, five acts)
- `.pao-inbox/_creative/character-sheets/dr-leader-mission-director.md` (Anna Yusupova full sheet, LOCKED)
- `.pao-inbox/_creative/character-sheets/_minor-characters.md` (Sabina + Hiroshi + others)
- `.pao-inbox/_creative/character-sheets/senior-technical-specialist.md` (Diego Vargas full sheet)
- `.pao-inbox/_creative/character-sheets/maria-santos.md`
- `.pao-inbox/_creative/the-crossing-concept-note-2026-04-30.md`
- `.pao-inbox/_decisions/antarctic-vision-chapter-concept-2026-04-30.md`
- `.pao-inbox/_decisions/co-seat-deferred-structural-decisions-2026-04-30.md`
- `.pao-inbox/_decisions/2026-04-30-upf-ch15-split-phase5-ch23-addendum.md`
- `.pao-inbox/_decisions/2026-04-30-voice-pass-priority-queue.md`
- `.pao-inbox/_decisions/2026-04-30-word-count-target-revision-proposal.md`
- `.pao-inbox/_editorial-reviews/` (whatever's in there from the literary-board pass)
- `.pao-inbox/pao-directive-2026-05-01T*.md` (three directives this session, including this one)

Skip ephemeral beacons (`yeoman-question-*.md`, `yeoman-resumed-*.md`) — anatomy.md should reflect durable artifacts only.

## Deliverable

Edit `.wolf/anatomy.md` directly. Do not commit — PAO commits. Write `yeoman-resumed-2026-05-01THH-MMZ-anatomy-refresh-complete.md` with summary of what you added + any files you skipped + reasoning.

## Note

This is P3 because the anatomy is a developer-experience aid, not a manuscript correctness gate. If the audiobook regen (P2 directive) takes longer than expected, deprioritize this and finish audio first.
