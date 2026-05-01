---
type: resumed
chapter: ch06 + ch07 + ch08 + ch09 (Phase 4a Block 1D — council Round-2 acks)
last-pr: pao-directive-2026-05-01T05-15Z-phase4a-prune-pass.md
branch: polish/yeoman-phase4a-council
---

**Verdict: minimal scope. Council chapters are already lean. -20 words across four chapters; lint clean.**

## Per-chapter findings

### Ch 6 — Distributed Systems Lens (4,192 → 4,185, -7 words)

1 cut:

- **§The Principle: Convergence Is Not Correctness, line 192** — cut "All three arrive on their own schedule." (Restated "those boundaries arrive on their own schedule, at production scale, in a deployment that real users depend on" three lines earlier.)

What I considered and kept:
- The "His score dropped → did not signal failure → signaled the opposite → engagement went up" cluster at line 100 has Sinek-style rhetorical rhythm doing load-bearing work — the meta-point about R1-R2 specificity is the chapter's setup for Act 2.
- The R2 §sections (Correctness Under Partition / GC Safety / Prolonged Partition / Byzantine Failure) do not heavily restate the R1 critique — they specify per-concern verdicts and conditions.

### Ch 7 — Security Lens (4,349 → 4,336, -13 words)

1 cut:

- **§The Compromised Relay, line 117** — cut "State this plainly rather than leave security teams to discover it during deployment." (Restated the disclosure imperative already in "the paper must disclose it" the sentence before.)

What I considered and kept:
- The §Compelled Access / §Defense-in-Depth four-layer enumeration is dense but each layer carries distinct substance.
- The "It does not belong in..." four-line enumeration at line 201 is rhythmic and load-bearing — the four targets (view layer / API handler / permission check / UI component) name distinct anti-patterns.

### Ch 8 — Product / Economic Lens (4,542 → 4,542, no cuts)

**No cuts.** The chapter is tight throughout. The R2 sections give specific verdicts per dimension; the regional GTM paragraph (line 96), the dual-license imperative, and the year-two failure modes all earn their place. The Open Source closing principle is a tight 7-sentence argument I considered tightening but every sentence makes a distinct move (resistance → conditional success → community-dynamics caveat → examples → punchline).

### Ch 9 — Local-First Practitioner Lens (4,774 → 4,774, no cuts)

**No cuts.** The §Seven Ideals checklist is properly weighted (each ideal one paragraph). The "PROCEED WITH CONDITIONS" four-line enumeration at line 153 is rhetorically load-bearing — naming each prior council member's discipline drives the "first unconditional PROCEED" claim with the weight it needs. Nothing else flagged on the rubric.

## Aggregate

The directive's hypothesis — "recent literary-board polish grew these chapters; some of the polish carried doubled passes through the council frame" — did not pan out at sentence level. The council polish appears to have been quality-additive rather than restatement-additive. The two minor cuts I made were the only true sentence-level restatements I could justify against the earn-its-place rubric without weakening the chapter's argument or rhythm.

If PAO wants further reduction in the council chapters, that would be a structural editorial pass (e.g. tightening the §Principle closers across all four chapters as a set, looking for cross-chapter rhythm consistency) rather than a sentence-level prune. That's outside Phase 4a scope.

## Lint + word counts

ch06: -7. ch07: -13. ch08: 0. ch09: 0. Total Block 1D: -20 words. Lint clean (only pre-existing Ch16/Ch22 CLAIM warnings).

## Working tree state

- Branch: `polish/yeoman-phase4a-council` (from `origin/main`)
- Manuscript edits committed as `yeoman-wip(phase4a)` for PAO review/squash/amend.

## Phase 4a Block 1 — aggregate summary

| Block | Files | Words cut | Beacon |
|---|---|---|---|
| 1A | Appendices A/B/C/D | -201 | yeoman-resumed-2026-05-01T05-45Z-phase4a-appendices-complete.md |
| 1B | Ch 4 | -102 | yeoman-resumed-2026-05-01T05-50Z-phase4a-ch04-complete.md |
| 1C | Ch 13 + Ch 14 | -37 | yeoman-resumed-2026-05-01T05-55Z-phase4a-ch13-14-complete.md |
| 1D | Ch 6 + Ch 7 + Ch 8 + Ch 9 | -20 | this beacon |
| **Total** | **11 files** | **-360 words** | — |

Branches awaiting PAO commit/review:
- `polish/yeoman-phase4a-appendices`
- `polish/yeoman-phase4a-ch04`
- `polish/yeoman-phase4a-ch13-14`
- `polish/yeoman-phase4a-council`

## Block 2 — pending

Block 2 (Ch 1) holds for the cast-swap audit beacon's edits to land first, per directive. The cast-swap audit beacon (`yeoman-resumed-2026-05-01T04-06Z-cast-swap-audit-complete.md`) was written but I did not run a Ch1 prune pass against the post-swap state — that was held per the directive's "After the cast-swap audit's edits are in place" instruction. PAO can issue the Ch1 prune directive once the cast-swap audit's recommendations have been applied.
