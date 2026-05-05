# Assembly Manifest

*This file defines the final manuscript assembly order for `make draft-pdf` and `make epub`.*
*Update as chapters reach `icm/assembled`. Word counts via `python3 build/word-count.py`.*

## Status

Last refreshed: 2026-05-01 post-cast-swap (PR #64) + Phase 7 reference-list split (PR #65) + The Crossing first draft merge (PR #59). Word counts from `build/word-count.py`. ICM stages reflect the loop's `state.yaml` (canonical) for extension-affected chapters and the last review pass (council / literary board) for the rest.

| Chapter | File | ICM Stage | Words | Target | QC-1 |
|---|---|---|---:|---:|---|
| Foreword | `chapters/front-matter/foreword-placeholder.md` | placeholder | 86 | — | pending contributor |
| Preface | `chapters/front-matter/preface.md` | icm/prose-review | 1,728 | ~1,000 | ✓ over (173%) — load-bearing authorship disclaimer 2026-05-04 (+294) |
| Ch 1 | `chapters/part-1-thesis-and-pain/ch01-when-saas-fights-reality.md` | icm/voice-passed (R1+R2 council, literary board) + King-style victims (PRs #53, #54) + cast-swap Lakshmi→Sabina (PR #64) + Phase 4a Block 2 prune (2026-05-04, -63 words) | 7,605 | ~4,500 | ⚠ over (169%); narrative scenes preserved at full altitude |
| Ch 2 | `chapters/part-1-thesis-and-pain/ch02-local-first-serious-stack.md` | icm/voice-passed (R1+R2 council, literary board) | 5,270 | ~4,000 | ✓ over (132%) |
| Ch 3 | `chapters/part-1-thesis-and-pain/ch03-inverted-stack-one-diagram.md` | icm/voice-passed (R1+R2 council, literary board) + cast-swap Petra→Hayoon (PR #64) | 4,418 | ~3,000 | ✓ over (147%); audit pending (Yeoman directive) |
| Ch 4 | `chapters/part-1-thesis-and-pain/ch04-choosing-your-architecture.md` | icm/voice-passed (R1+R2 council, literary board) | 4,909 | ~3,500 | ✓ over (140%) |
| Ch 5 | `chapters/part-2-council-reads-the-paper/ch05-enterprise-lens.md` | icm/voice-passed | 4,061 | ~3,500 | ✓ over (116%) |
| Ch 6 | `chapters/part-2-council-reads-the-paper/ch06-distributed-systems-lens.md` | icm/voice-passed | 4,192 | ~3,500 | ✓ over (120%) |
| Ch 7 | `chapters/part-2-council-reads-the-paper/ch07-security-lens.md` | icm/voice-passed | 4,349 | ~3,500 | ✓ over (124%) |
| Ch 8 | `chapters/part-2-council-reads-the-paper/ch08-product-economic-lens.md` | icm/voice-passed | 4,542 | ~3,500 | ✓ over (130%) |
| Ch 9 | `chapters/part-2-council-reads-the-paper/ch09-local-first-practitioner-lens.md` | icm/voice-passed | 4,774 | ~3,500 | ✓ over (136%) |
| Ch 10 | `chapters/part-2-council-reads-the-paper/ch10-synthesis.md` | icm/voice-passed | 3,542 | ~2,500 | ✓ over (142%) |
| Ch 11 | `chapters/part-3-reference-architecture/ch11-node-architecture.md` | icm/awaiting-voice-check (#43 §Performance Contracts) | 6,622 | ~4,000 | ⚠ over (166%); voice-pass-locked |
| Ch 12 | `chapters/part-3-reference-architecture/ch12-crdt-engine-data-layer.md` | icm/voice-passed (post-cuts) | 4,897 | ~4,000 | ✓ over (122%) |
| Ch 13 | `chapters/part-3-reference-architecture/ch13-schema-migration-evolution.md` | icm/voice-passed | 4,363 | ~3,500 | ✓ over (125%) |
| Ch 14 | `chapters/part-3-reference-architecture/ch14-sync-daemon-protocol.md` | icm/voice-passed | 4,240 | ~3,500 | ✓ over (121%) |
| Ch 15 | `chapters/part-3-reference-architecture/ch15-security-architecture.md` | icm/voice-passed (post Ch15 split UPF + Phase 7 ref split) | 5,722 | ~5,500 (revised post-split) | ✓ over (104%) |
| Ch 16 | `chapters/part-3-reference-architecture/ch16-persistence-beyond-the-node.md` | icm/awaiting-voice-check (#44 §Per-Data-Class Device-Distribution) | 6,135 | ~3,000 | ⚠ over (204%); voice-pass-locked |
| Ch 17 | `chapters/part-4-implementation-playbooks/ch17-building-first-node.md` | icm/voice-passed | 3,481 | ~4,000 | ⚠ under (87%); review pending |
| Ch 18 | `chapters/part-4-implementation-playbooks/ch18-migrating-existing-saas.md` | icm/voice-passed | 3,600 | ~3,500 | ✓ |
| Ch 19 | `chapters/part-4-implementation-playbooks/ch19-shipping-to-enterprise.md` | icm/voice-passed | 4,322 | ~3,500 | ✓ over (123%) |
| Ch 20 | `chapters/part-4-implementation-playbooks/ch20-ux-sync-conflict.md` | icm/awaiting-voice-check (#43 §Performance Budgets, #45 §Revocation UX, #10 §Data-Class Escalation UX) | 9,120 | ~3,000 | ⚠ over (304%); multiple voice-pass-locked |
| Ch 21 | `chapters/part-5-operational-concerns/ch21-operating-a-fleet.md` | icm/awaiting-voice-check (#11) | 6,390 | ~6,500 | ✓ (98%) |
| Ch 22 | `chapters/part-5-operational-concerns/ch22-security-operations.md` | icm/awaiting-voice-check (post-split; #46 §Forward Secrecy + #48 §Key-Loss Recovery sections) + Phase 7 ref split | 7,694 | ~7,400 | ✓ over (104%) |
| Ch 23 | `chapters/part-5-operational-concerns/ch23-endpoint-collaborator-ops.md` | icm/awaiting-voice-check (post-split; #45 §Collaborator Revocation, #47 §Endpoint Compromise, #9 §Chain-of-Custody, #10 §Event-Triggered) + Phase 7 ref split | 9,732 | ~9,000 | ✓ over (108%) |
| Closing Chapter | `chapters/closing/the-crossing.md` | **icm/draft** (PR #59 merged 2026-05-01; first-person staff history, Anna POV, five acts; cast-swap Lars→Diego applied PR #64; Yeoman self-review directive queued) | 4,396 | ~5,000 | ✓ under (88%); audit pending (Yeoman directive) |
| Epilogue | `chapters/epilogue/epilogue-what-the-stack-owes-you.md` | icm/voice-passed | 3,070 | ~2,500 | ✓ |
| Appendix A | `chapters/appendices/appendix-a-sync-daemon-wire-protocol.md` | icm/voice-passed | 3,570 | ~2,000 | ✓ over (178%) |
| Appendix B | `chapters/appendices/appendix-b-threat-model-worksheets.md` | icm/voice-passed | 4,330 | ~2,000 | ✓ over (216%) |
| Appendix C | `chapters/appendices/appendix-c-further-reading.md` | icm/voice-passed | 3,293 | ~2,000 | ✓ over (165%) |
| Appendix D | `chapters/appendices/appendix-d-testing-the-inverted-stack.md` | icm/voice-passed | 3,667 | ~2,000 | ✓ over (183%) |
| Appendix E | `chapters/appendices/appendix-e-citation-style.md` | icm/approved | 962 | ~500 | ✓ over (192%) |
| Appendix F | `chapters/appendices/appendix-f-regulatory-coverage.md` | icm/voice-passed (added 2026-04 + Phase 5 R-F update) | 2,223 | ~2,000 | ✓ |
| Appendix G | `chapters/appendices/appendix-g-glossary.md` | icm/voice-passed (added 2026-04) | 3,349 | ~3,000 | ✓ |

**Running total (excluding foreword placeholder):** ~154,337 words (was 144,664 on 2026-04-30; +9,673 from cast-swap King-style scening on Ch1+Ch3, Phase 7 reference split duplication tax across Ch15/Ch22/Ch23, the closing chapter landing at 4,396 words, and small literary-board polish increases on Ch5–10 / Ch13–14).

**On length targets:** the chapter targets in `book-structure.md` and the % columns in this manifest are industry-standard recommendations and sanity checks for visibility — not hard drivers (CO directive 2026-05-01). Phase 4 prune is a quality-driven editorial pass (cut what doesn't earn its place); the post-prune total is downstream of editorial judgment, not an input to it. See `.pao-inbox/_decisions/2026-05-01-phase4-prune-scope.md` for the scope of where to look during the pass.

## Voice-Pass Queue (gating event for assembly)

9 extensions sit at `awaiting-voice-check`. Per `.pao-inbox/_decisions/2026-04-30-voice-pass-priority-queue.md`:

**Tier 1 (unblocks structural work):** #45 Collaborator Revocation (Ch23), #43 Performance Contracts (Ch11+Ch20), #11 Fleet Management (Ch21).
**Tier 2 (unblocks chapter compression):** #44 Per-Data-Class Device-Distribution (Ch16), #46 Forward Secrecy (Ch22), #47 Endpoint Compromise (Ch23).
**Tier 3 (closes extension):** #9 Chain-of-Custody (Ch23), #10 Data-Class Escalation (Ch23), #12 Privacy-Aggregation (Ch15).

Each extension's working artifacts live at `docs/book-update-plan/working/<extension-id>/`.

## Ch15 Split (UPF executed 2026-04-29 / 2026-04-30; Phase 7 ref split executed 2026-05-01)

The original Ch15 (22,274 words; 5.5× target) was split into three chapters per XO's UPF (`.pao-inbox/_decisions/2026-04-29-upf-ch15-split.md`):

- **Ch15 — Security Architecture** (architectural primitives, ~5,722 words; Phase 7 pruned to 8 architecture-only refs)
- **Ch22 — Key Lifecycle Operations** (KCIR + Key-Loss Recovery + Forward Secrecy, ~7,694 words; Phase 7 added 18 ops-local refs)
- **Ch23 — Endpoint, Collaborator, and Custody Operations** (Offline Revocation + Collaborator Revocation + Endpoint Compromise + Chain-of-Custody + Event-Triggered Re-classification, ~9,732 words; Phase 7 added 24 ops-local refs)

Phase 4 prune deferred until #45 voice-pass unlocks Ch23 §Collaborator Revocation; expected to recover ~3k words.
Phase 5 cross-reference cleanup substantially complete (verified 2026-05-01: all Ch15 §section refs in manuscript .md files point to architectural sections that stayed in Ch15; section refs that moved already redirected to Ch22/Ch23). Phase 7 reference-list split complete (PR #65 merged 2026-05-01).

## Closing Chapter status (post PR #59)

**The Crossing** (vision-of-solution narrative chapter) merged 2026-05-01. First-person staff history, Anna Yusupova POV, five-act structure (Departure, Submerged Transit, Death, Window That Doesn't Come, Return). 4,396 words. Cast: Anna Yusupova (Uzbek, AARI/St. Petersburg-affiliated), Dr. Diego Vargas (Argentine, IAA, the senior technical specialist who dies), Dr. Hiroshi Nakamura (Japanese, NIPR), Maria Santos (Brazilian, medical officer), Priya Iyer (Indian, instrumentation), Sabina Rahman (Bangladeshi, logistics — Grameen lineage), Joel Reyes (Filipino, life-support), Wanjiru Kamau (Kenyan, comms — M-PESA lineage). Concept note + character sheets at `.pao-inbox/_creative/`. Yeoman self-review directive queued in `.pao-inbox/`.

**Vol-2 reframing pending revision pass:** the locked Vol 2 design (concept note 2026-05-04) replaces Diego's death with Diego's survival + the leak-and-fire-cascade landing in Segment 3 of a multi-segment under-ice mission. The existing Vol 1 closing chapter (`chapters/closing/the-crossing.md`) requires a separate revision pass to align with the multi-segment design + Anna-read-paper-not-built-it framing + leak-event-as-Diego-survival rather than death-scene; ~3-5 hour pass; CO-gated. Until that pass, the Vol 1 chapter remains the canonical Vol 1 closing as drafted.

## Vol 2 status (Book 1 of the Sunfish series — story-first restructure)

**Architectural foundation complete (2026-05-04 evening; 31 PRs landed #74→#104).** Vol 2 is a story-first restructure narrated by Anna Yusupova in first person; Vol 1 (the existing 154,337-word manuscript) is canonically Joel Reyes's research paper in-universe, with Chris Wood as real-world author (H.G. Wells convention).

**Outline drafted (2026-05-04):** 18 chapters across three acts; ~90,000-100,000 words target / ~9-10 hours audiobook. See `chapters/book-2/CHAPTER-OUTLINE.md` for the working blueprint and `chapters/book-2/README.md` for orientation.

| Phase | Days | Chapters | Words target | Status |
|---|---|---:|---:|---|
| Act I — Departure and the first under-ice realization | 1-21 | Ch 1-6 | ~30,000 | all `icm/outline` |
| Act II — Subsystems hold; the contest sharpens | 22-42 | Ch 7-12 | ~30,000 | all `icm/outline` |
| Act III — Cascade, ascent, and the cumulative reveal | 43-56 | Ch 13-18 | ~33,000 | all `icm/outline` |
| **Total** | 1-56 | 18 | **~93,000** | outline-stage |

Pipeline plumbing: `build/audiobook.py` carries `VOL2_CHAPTER_FILES` (placeholder paths matching the directory structure); paths activate (move into `CHAPTER_FILES` or render via `--only chXX`) once each chapter reaches `icm/draft`.

**Concept artifacts** (read-order for any drafter):
1. `.pao-inbox/_creative/vol-2-concept-note-2026-05-04.md` — 12-section synthesis (~7,500 words)
2. `.pao-inbox/_creative/vol-2-concept-locked-elements-2026-05-04.md` — running locks index
3. `.pao-inbox/_creative/character-sheets/` — Anna, Joel, Priya, Wanjiru, Stefan, Astrid, Helvetia
4. `.pao-inbox/_creative/forsaken-position-papers/` + `oss-architects-voices/` — voice references
5. `.pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md` — multi-segment mission timeline

**CO-gated:** listen-test pair drafting (Ch 5 *The Day-Twenty Realization* + Ch 2 *The Recruitment Interview*; concept note §9). Cheapest validation: ~15,000 words → Kokoro render → ~100-minute audiobook listen-test → verdict drives full Book 1 commit-or-revise.

**No blockers from PAO side** as of 2026-05-04 evening.

## Next Steps

1. **`icm/voice-check`** (author, 9 extensions): Tier 1 first per priority queue. Highest leverage: #45 Collaborator Revocation (closes Ch15 split UPF).
2. **Phase 4 prune** (PAO directs, Yeoman executes): quality-driven editorial pass — cut what doesn't earn its place across voice-pass-unlocked chapters (Phase 4a, single pass) and incrementally per-extension as each voice-pass clears (Phase 4b). Scope at `.pao-inbox/_decisions/2026-05-01-phase4-prune-scope.md`. No target percentage; length lands where editorial judgment lands it.
3. **Foreword**: external contributor needed.
4. **Closing Chapter audit** (Yeoman directive queued): five-pass King-style audit of The Crossing on main; Spanish-letter beat verification; Diego-thread continuity; granddaughter Sofía consistency.
5. **Audiobook regen** (Yeoman directive queued): 8 chapter alignment artifacts stale after cast-swap + Phase 7; pronunciation-flag pass on cast-swap names.
6. **Final assembly**: set all chapters to `icm/assembled` after voice-pass + Phase 4 prune + Closing Chapter audit-and-polish; run `make draft-pdf`.

## Build

```bash
make draft-pdf   # Full PDF draft
make epub        # ePub for Leanpub preview
make word-count  # Per-chapter word count vs. targets
make lint        # Check broken cross-references
```

`build/Makefile` includes Ch21–23 + Appendix F+G in `draft-pdf` (added 2026-04-30 PR #26).
`build/lint.py` recognises Ch21–23 + Appendix F+G (added 2026-04-30 PR #23).
`build/audiobook.py` includes Ch22+Ch23 in `CHAPTER_FILES` (added 2026-04-30 PR #26). Vol 2 paths staged in `VOL2_CHAPTER_FILES` (added 2026-05-04, this PR); inert until each Vol 2 chapter reaches `icm/draft`.

Lint status: 0 errors, 2 warnings (Ch16 mid-stream forward-secrecy boundary architectural Q + Ch22 Cohn-Gordon 2016 PCS deferred citation; both legitimate deferred-work trackers).
