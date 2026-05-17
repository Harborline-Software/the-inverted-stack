---
type: pao-directive
audience: Yeoman (anatomy maintenance, OpenWolf housekeeping)
priority: low
related:
  - .wolf/anatomy.md
---

# PAO Directive — Anatomy.md auto-generated description cleanup

## What

Replace the poor auto-generated descriptions for Vol 2 chapter entries in `.wolf/anatomy.md`. Yeoman flagged this as P3 housekeeping in `yeoman-question-2026-05-06T09-00Z-vol2-complete-whats-next.md` and offered to fix it.

## Why

Several Vol 2 chapter entries currently read as fragments — "Declares of", "Declares GPU", "Declares register" — which fail the anatomy.md contract (2–3 line description so future sessions can decide whether to skip the full read). Token-discipline goal.

## Scope

- Vol 2 chapter entries only (`vol-2/act-*/ch*.md`).
- Replace any description that is fewer than 8 words, or that starts with an incomplete-sentence fragment ("Declares of …", "Contains the …" with no object), or that fails to name the chapter's narrative event.
- Each replacement description should be **one sentence**, **8–20 words**, naming the chapter's scene and the key thing that happens. Match the quality of well-written entries already in anatomy.md (e.g., ch01-departure, ch02-recruitment-interview, ch16-final-ascent).
- Update the token estimate column if the chapter mtime moved since the last anatomy scan.

## Constraint

- **Do not change file paths, sort order, or other anatomy structure.** Description column only.
- **Do not touch Vol 1 anatomy entries** — out of scope for this pass.
- **Run `openwolf anatomy refresh` first** if Yeoman wants the auto-generation baseline current before editing. Otherwise just hand-edit.

## Acceptance check

- All `vol-2/act-*/ch*.md` entries in `.wolf/anatomy.md` have a description of 8–20 words naming the chapter event.
- No fragment-style descriptions remain.
- Commit message: `chore(openwolf): anatomy descriptions — Vol 2 chapters cleanup`.
- Beacon back: one-line resumed in `.pao-inbox/` naming the count of entries edited.

## Notes

This is low-priority housekeeping; do this after #1 (audio staleness audit), #2 (Ch 17 FFF pilot), and #3 (Ch 7 Joel pilot) are complete or queued. Use it as a context-switch palate cleanser if needed.
