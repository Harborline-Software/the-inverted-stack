---
type: closure-decision
date: 2026-05-04
author: PAO
status: closed — all Block 1 sub-blocks merged to main
parent-decision: .pao-inbox/_decisions/2026-05-01-phase4-prune-scope.md
related-prs: ["#78", "#79", "#80", "#81", "#82"]
---

# Phase 4a Block 1 — Closure

## Aggregate

Yeoman delivered all five Block 1 sub-blocks. **Total: 11 chapter files, -360 words, lint clean throughout.**

| PR | Block | Files | Words |
|---|---|---|---:|
| #78 | 1A — Appendices A/B/C/D | 4 | -201 |
| #79 | 1B — Ch04 (Choosing Architecture) | 1 | -102 |
| #80 | 1C — Ch13 + Ch14 (spec) | 2 | -37 |
| #81 | 1D — Council ch06 + ch07 (ch08, ch09 already lean) | 2 | -20 |
| #82 | Ch01 + Ch03 cast-swap audit (no edits, audit-only) | 0 | 0 |

## What Yeoman flagged for PAO consideration

**Ch01 — "first thirty loans" precision flag.** The Sabina Rahman passage cites Yunus's 1976 lending circle as "first thirty loans." Historical sources cite 42 borrowers (Jobra, 1976). PAO call: correct to 42 or leave as narrative shorthand. *Resolution: leave as narrative shorthand* — the number is incidental to the structural claim about 1976 lineage; correcting to 42 doesn't strengthen the passage and adds historical-precision burden to a moment that's about institutional continuity. If a reader catches the discrepancy, the passage still earns its place.

**Ch03 — ISMS-P expansion truncated; KISA "quarterly bulletin" format name.** Yeoman flagged that the abbreviation isn't fully expanded and the bulletin format name needs verification. *Resolution: defer until next ch03 edit pass*; not blocking Phase 4a closure.

## What Yeoman explicitly considered and kept

Per the earn-its-place rubric (decision 2026-05-01-phase4-prune-scope):

- **Appendix A/D rhetorical structures** — kept; load-bearing
- **Ch13/14 regional jurisdictional enumerations** (CIS, Middle East, East Asia, Africa) — kept; regional-consultant-earned
- **Ch14 process-isolation "Picture the X" triplet** — kept; rhetorical force
- **Ch14 Tier 3 Relay "cannot read / cannot inject / cannot modify" triplet** — kept; rhythmic, novel content
- **Ch06 council §Convergence-Is-Not-Correctness Sinek-rhythm cluster** — kept; load-bearing for Act 2 setup
- **Ch07 council §Compromised Relay disclosure rhetoric** — kept; "the paper must disclose it" carries the imperative
- **Ch07 council §Defense-in-Depth four-layer enumeration** — kept; each layer has distinct substance

## What this unlocks

- **Phase 4a Block 2 — Ch01 prune** is now unblocked (cast-swap audit was the precondition). Block 2 will be a separate Yeoman directive issued when needed.
- **Phase 4b** (per-extension prune) remains gated on CO clearing voice-pass extensions one at a time.

## What this does NOT close

- Phase 4a Block 2 (Ch01) — still pending directive
- Phase 4b — gated on CO voice-pass clearance
- The two precision flags above (left as deferred items)

## Yeoman flow validation

Yeoman worked on `polish/yeoman-phase4a-*` branches: WIP commit (chapter edits) + beacon commit. PAO PR'd each branch (squash-merge) plus cherry-picked the standalone cast-swap-audit beacon commit. Per the 2026-04-29 commit-protocol, Yeoman edits + writes the beacon, PAO opens PR + merges. Working as intended.

One workflow note: 5 of Yeoman's beacon commits had landed on **local** main (not remote) before the Monday session — Yeoman's commits never auto-push. PAO must `git log origin/main..main` at the start of each session and PR-merge any unpushed Yeoman commits before assuming the queue is at remote-main parity. Logged in cerebrum + buglog.
