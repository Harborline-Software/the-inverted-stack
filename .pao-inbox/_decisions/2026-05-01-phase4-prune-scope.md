---
type: phase-4-prune-scope
date: 2026-05-01 (revised after CO framing correction)
author: PAO
audience: CO (judgment), Yeoman (execution scope)
parent-decisions:
  - 2026-04-30-voice-pass-priority-queue.md
  - 2026-04-29-upf-ch15-split.md
status: scope — quality-driven, not number-driven
supersedes: word-count-target-revision-proposal.md (recommendation only; no ratification needed)
---

# Phase 4 Prune Scope — Quality-Driven Editorial Pass

## Framing

There are no hard drivers for length on this manuscript. Industry-standard chapter targets in `book-structure.md` and `ASSEMBLY.md` are recommendations and sanity checks — useful for visibility, not constraints that drive editorial decisions. Phase 4 cuts what doesn't earn its place. The post-prune total is a downstream consequence of editorial judgment, not an input to it.

This document is the **scope** of where to look during the prune pass: which chapters carry redundancy or unearned passages, and which sections cannot be touched yet because their parent extension is still at `awaiting-voice-check`. It is not a target-percentage exercise.

## Methodology

For each chapter, the prune pass asks one question: **does every sentence earn its place?**

A sentence earns its place when it carries one of:
- A specific claim, with a source or named anchor
- A specific decision the reader has to make, with criteria
- A scene that grounds an argument in lived altitude
- A bridge that names the structure of the next move
- A precision the reader cannot get elsewhere in the book

A sentence fails the test when it:
- Restates what the previous sentence already said
- Hedges a claim the rest of the chapter doesn't hedge
- Signposts ("As we have seen", "It is worth noting", "Importantly")
- Closes a paragraph by summarizing the paragraph
- Adds a parenthetical that doesn't change the reader's model
- Quietly defers a decision the reader needs to make

Cuts are at the sentence and clause level. Substance the adversarial review and literary board specifically asked for is not in scope — that material was earned through review and stays.

## Phase 4a — Voice-pass-unlocked (execute now under CO direction)

These chapters can be edited at any time; their voice-pass-locked extension sections (where applicable) are excluded from the pass.

| Chapter | Where to look | Lock status |
|---|---|---|
| **Ch 1** | Cast-swap audit (Yeoman directive queued) will surface trim candidates. After 6 King-style victims were introduced across two PRs, some passages restate the failure-mode taxonomy multiple times. | Unlocked |
| **Appendix A** | Sync daemon wire protocol — the state-machine narration is illustrated twice, once narratively and once via the protocol diagram | Unlocked |
| **Appendix B** | Threat-model worksheets — each of 6 worksheets repeats common boilerplate; consider a shared prelude with worksheet-specific deltas | Unlocked |
| **Appendix C** | Further reading — annotation density is by design, but the longest annotations restate what the reader can find on the linked source | Unlocked |
| **Appendix D** | Testing the stack — test-case enumeration carries some redundancy with the chapter's framing prose | Unlocked |
| **Ch 6, 7, 8, 9** | Council chapters; recent literary-board polish grew them. Look for Round-2 acknowledgment paragraphs that restate the Round-1 critique already named in the structure | Unlocked |
| **Ch 13, 14** | Schema migration + sync daemon — illustrative paragraphs may carry restatement of the spec's normative claims | Unlocked |
| **Ch 4** | Per-Zone Compliance Posture — the four zones each restate the framework. Consider whether all four restatements earn their place or whether one canonical statement plus zone deltas reads tighter | Unlocked |

The Phase 4a pass is one Yeoman editorial pass after the cast-swap and closing-chapter audit beacons land. Single PR. Yeoman edits, PAO commits.

## Phase 4b — Voice-pass-locked (execute as each extension voice-passes)

These sections are voice-pass-locked; cut candidates can only be applied after the parent extension's voice-check completes. The cuts below are *scoped to the extension section only*; the rest of each chapter is touched only by Phase 4a.

| Extension | Chapter | Section | Voice-pass needed | Where to look |
|---|---|---|---|---|
| **#43** | Ch 11 | §Performance Contracts | #43 | Sub-pattern restatement in 43e (per-deployment-class calibration) |
| **#43** | Ch 20 | §Performance Budgets and Progressive Degradation | #43 | UX surface restates Ch 11's spec content; pull back to Ch 11 reference |
| **#45** | Ch 23 | §Collaborator Revocation and Post-Departure Partition | #45 | Sub-pattern 45e (bilateral partition) overshot baseline by ~25% during draft; novelty depth justified the overshoot but the mechanics narration may carry doubled passes |
| **#45** | Ch 20 | §Revocation UX | #45 | Departure-moment placeholder paragraph (carries voice-check HTML comment) |
| **#11** | Ch 21 | Fleet management section | #11 | Per-property restatement of fleet-management commitments |
| **#44** | Ch 16 | §Per-Data-Class Device-Distribution | #44 | The data-class manifest schema is illustrated twice |
| **#46** | Ch 22 | §Forward Secrecy and Post-Compromise Security | #46 | Construction-by-construction description carries some restatement of the architectural commitment |
| **#47** | Ch 23 | §Endpoint Compromise: What Stays Protected | #47 | Sub-pattern 47a / 47b transition carries shared boilerplate |
| **#9** | Ch 23 | §Chain-of-Custody for Multi-Party Transfers | #9 | Receipt-sequence narration may share structure with the data-class log narration |
| **#10** | Ch 23 | §Event-Triggered Re-classification | #10 | Sub-patterns 10a–10d each restate the escalation contract |
| **#10** | Ch 20 | §Data-Class Escalation UX | #10 | Same as Ch 23 — UX surface restates Ch 23's spec |
| **#12** | Ch 15 | §Privacy-Aggregation (or Ch 22 if reclassified to operational) | #12 | DP family content; Phase 1 triage classified as architectural (A); revisit if reclassified to operational (O) |

Phase 4b runs **incrementally**: one focused Yeoman directive per extension section, immediately after that extension's voice-pass clears. This avoids stacking parallel editorial work and keeps the prune in lockstep with voice-pass cadence.

## Phase 4c — Closing Chapter

The Crossing landed at 4,396 words. Currently under the chapter's industry-standard sanity check; no scope unless the Yeoman audit beacon surfaces specific tighten candidates. Closing chapters tolerate the length they earn. If the audit finds the chapter holds together, leave it.

## What is explicitly out of scope

- **Material the council asked for** (R1+R2 verdict-driven additions): in scope only if a sentence in that material fails the earn-its-place test. The fact that it was added by council is not a cut justification.
- **Material the literary board asked for** (P0/P1/P2 fixes): same standard.
- **Substance the adversarial review specifically requested** (e.g., DP family in Ch 15, recovery mechanics in Ch 22, custody operations in Ch 23): these landed because the reviewers said the book was incomplete without them. Removing them is regression, not editing.
- **Reference material that scales with completeness** (Appendix F regulatory matrix, Appendix G glossary): trimming these reduces utility for the reader using them as lookup tables.
- **Council chapter substance** (Ch 5–10): each lens earned itself; cuts are at the sentence level only.
- **Part 1 narrative scening** (Ch 1–4): King-style victim scening was specifically requested by CO and validated through review; cuts are limited to redundant phrasing, never to reduction in lived altitude.
- **Closing chapter Spanish-letter beat, Argentine institutional anchors, granddaughter Sofía thread**: these landed in the cast-swap design pass and were validated by the cast-audit framework (regulatory regimes + real-world precedent).

## Execution sequencing

The order is dictated by which beacons + voice-passes land, not by any forcing function from PAO:

1. **Yeoman beacons land first.** Two audit beacons (cast-swap, closing chapter) and one regen beacon (audiobook) are queued. When those return, PAO scans them.
2. **Phase 4a directive issues** after cast-swap and closing-chapter beacons land — single Yeoman editorial pass against the scope above.
3. **Phase 4b directives issue incrementally** — one per extension as voice-pass clears, in priority-queue order (Tier 1 first: #45 / #43 / #11).
4. **Phase 4c directive issues** only if closing-chapter audit surfaces specific tighten candidates.
5. **Final pass.** After Phase 4a and 4b complete, re-read each chapter end-to-end as a hostile reader — last earn-its-place pass before final assembly.

## Status

- Scope drafted (revised post-CO framing correction): **2026-05-01.**
- Phase 4a execution: pending Yeoman audit beacons + CO direction to proceed.
- Phase 4b execution: pending each voice-pass clearance.
- Phase 4c execution: pending closing-chapter audit beacon (only if needed).

---

**End of scope.** Cuts execute when CO directs; Yeoman edits in working tree, PAO commits per the 2026-04-29 directive. Length lands where editorial judgment lands it.
