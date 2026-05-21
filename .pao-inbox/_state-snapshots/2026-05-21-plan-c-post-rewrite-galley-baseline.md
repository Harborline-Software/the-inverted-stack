# Galley Baseline — Vol 2 Post-Plan-C Rewrite (2026-05-21)

Measured: all 18 vol-2 chapters after Plan C1+C7 rewrite waves 1–4.
Tool: `galley_measure_chapter` (standard preset).
Purpose: baseline for audiobook re-render decision.

---

## Per-Chapter Results

| Ch | File | Verdict | Blockers | Warnings | Word count | Top issues (if not green) |
|----|------|---------|----------|----------|------------|--------------------------|
| 01 | ch01-departure.md | GREEN | 0 | 0 | 4,821 | — |
| 02 | ch02-recruitment-interview.md | GREEN | 0 | 0 | 5,573 | — |
| 03 | ch03-drake-passage-ice-edge.md | GREEN | 0 | 0 | 5,857 | — |
| 04 | ch04-first-submersion.md | GREEN | 0 | 0 | 4,991 | — |
| 05 | ch05-day-twenty-realization.md | GREEN | 0 | 0 | 6,004 | — |
| 06 | ch06-first-surface.md | GREEN | 0 | 0 | 4,838 | — |
| 07 | ch07-joels-sunfish.md | GREEN | 0 | 0 | 5,268 | — |
| 08 | ch08-second-submersion.md | GREEN | 0 | 0 | 4,305 | — |
| 09 | ch09-sync-daemon-under-drift.md | GREEN | 0 | 0 | 5,710 | — |
| 10 | ch10-aftermath-mission-that-once-was.md | GREEN | 0 | 0 | 5,072 | — |
| 11 | ch11-second-surface.md | GREEN | 0 | 0 | 5,034 | — |
| 12 | ch12-beginning-of-the-end.md | GREEN | 0 | 0 | 4,252 | — |
| 13 | ch13-schema-that-should-not-migrate.md | GREEN | 0 | 0 | 10,291 | — |
| 14 | ch14-the-crossing.md | YELLOW | 0 | 1 | 11,448 | `self_referential_frame`: 2 instances ≥ warning threshold (2) |
| 15 | ch15-compromised-relay-holds.md | GREEN | 0 | 0 | 7,378 | — |
| 16 | ch16-final-ascent.md | GREEN | 0 | 0 | 5,306 | — |
| 17 | ch17-transit-north.md | GREEN | 0 | 0 | 5,124 | — |
| 18 | ch18-punta-arenas-surfacing.md | YELLOW | 0 | 1 | 7,990 | `motif_overuse`: 1 instance ≥ warning threshold (1) |

---

## Volume Summary

| Metric | Count |
|--------|-------|
| Green | 16 |
| Yellow | 2 |
| Red | 0 |
| Total blockers (volume) | 0 |
| Total warnings (volume) | 2 |
| Total word count | 99,262 |

**Most-contaminated chapter:** Ch14 (ch14-the-crossing.md) — YELLOW, `self_referential_frame` warning (2 instances at threshold). Highest word count in the volume at 11,448 words; the density is manageable.

**Cleanest chapters:** Chs 01–13 and 15–17 are fully clean (zero blockers, zero warnings). Notably ch13 at 10,291 words is clean despite its length.

---

## Notes

- Both YELLOW chapters are warning-only (0 blockers). Neither blocks audiobook render.
- Ch14 `self_referential_frame` warning: 2 trigger-phrase instances at the warning floor of 2. A single phrase variation drops this to GREEN (per cerebrum learning 2026-05-19).
- Ch18 `motif_overuse` warning: 1 instance at the warning floor of 1. Likely a repeated image or phrase cluster introduced during Plan C7 rewrite. Targeted single-pass fix.
- Volume-wide blocker count is zero. All 18 chapters are render-eligible under standard preset.
