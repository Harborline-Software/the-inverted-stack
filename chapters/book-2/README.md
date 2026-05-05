# Book 2 — orientation

> **Working title:** TBD. Use *Book 1 of the Sunfish series* / *Vol 2 of The Inverted Stack* in commits and beacons until CO locks a title.

This directory holds Book 2 (the story-first restructure) — a multi-segment under-ice mission narrated by Anna Yusupova in first person, with Joel's paper as the in-universe canonical research artifact (Vol 1 of *The Inverted Stack*). H.G. Wells convention: Anna is the in-universe narrator; Chris Wood is the real-world author.

## Read-order for any drafter or fresh session

1. `CHAPTER-OUTLINE.md` (this directory) — the working blueprint
2. `.pao-inbox/_creative/vol-2-concept-note-2026-05-04.md` — the 12-section synthesis
3. `.pao-inbox/_creative/vol-2-concept-locked-elements-2026-05-04.md` — running locks index
4. `.pao-inbox/_creative/character-sheets/` — at minimum Anna + Joel for any Book 1 chapter
5. `.pao-inbox/_creative/forsaken-position-papers/` + `oss-architects-voices/` — voice references
6. `.pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md` — mission timeline

## Directory layout

```
chapters/book-2/
├── README.md                  # this file
├── CHAPTER-OUTLINE.md         # working blueprint (18 chapters across Acts I/II/III)
├── act-1/                     # Days 1-21; Ch 1-6
├── act-2/                     # Days 22-42; Ch 7-12
└── act-3/                     # Days 43-56; Ch 13-18
```

Each act subdirectory will receive chapter `.md` files as drafts land. File naming convention follows the existing repo convention: `chXX-short-slug.md` (e.g., `ch05-day-twenty-realization.md`).

## Status snapshot

- All 18 chapters at `icm/outline` (2026-05-04)
- Pipeline plumbing staged in `build/audiobook.py` (commented; activates when files reach `icm/draft`)
- CO-gated: listen-test pair drafting (Ch 5 + Ch 2 per concept note §9)
- See `ASSEMBLY.md` for top-level status across both volumes
