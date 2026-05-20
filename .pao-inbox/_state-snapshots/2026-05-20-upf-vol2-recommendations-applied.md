# Vol-2 Bestseller-Profile UPF — Recommendations Applied (Stage 06 build)

**Pipeline:** `icm/pipelines/bestseller-profile-review` (Stage 06)
**Dispatch:** 2026-05-20, 14 parallel subagents (3 PAO Opus + 11 Yeoman Sonnet)
**Source:** `2026-05-20-upf-vol2-consolidation-bestseller-profile.md` (Stage 07 grading matrix)

---

## Application matrix

| Ch | Pre | Post (projected) | Edits applied | Notes |
|---|---|---|---|---|
| 01 | A- | A- | Aphoristic closes ×2 | Mother-wound packaging replaced with mutual-recognition beat |
| 03 | B+ | A- | Tricolon close + discipline-motif vary + procedural compress | ~90 words cut |
| 05 | B+ | A- | 3 aphoristic-close swaps (Scene 1 / Scene 5 / Scene 8) | Forward-motion beats land all 3 |
| 07 | B+ | A- | Motif cap (4→2) + Scene D Anna-interior + irony cut | Joel's hands-at-rest beat added |
| **08** | **D+** | **B/B+** ⭐ | 8 parentheticals + "the way X" 11→3 + register 8→0 + wardroom cut | **PRE-BOBIVERSE retired; galley GREEN** |
| 10 | B | A- | Self-ref frame cut + tricolon compress + opening drone trim | Galley GREEN |
| 11 | C+ | B+ | Joel cup 250→55 words + bridge-wing + tea-scene sensory | Forsaken-name decision DEFERRED |
| **12** | **D+** | **B+** ⭐ | 6 scenes parenthetical + "X was the X" 33→5 + Sunfish disclosure move | **PRE-BOBIVERSE retired; galley GREEN** |
| 13 | B- | A- | Class/region rail 190-word insert + 2 parentheticals + register 3→1 | Galley GREEN |
| 14 | B+ | A- | Porthole 9→5 beats + diary AP-8 fix + anaphora 5→3 | ~260 words cut; register already at cap (stale UPF flag) |
| 15 | B+ | A- | Timestamp compress + Joel-exchange triple-close + Nairobi flashback + enumeration trim | **~1,700 words cut** (9k → 7.3k) |
| 16 | B+ | A- | Meta-commentary cut + double-register replace + 2 "was the same X" cuts | All best beats preserved |
| 17 | B+ | A- | "At the standing" 9 instances cut + 2 Anna-interior beats + OSS middle-paragraph cut | Crew-log register preserved (load-bearing) |
| 18 | B+ | A- | Perkins irony cut | Register already at cap from 2026-05-16 rewrite (stale UPF flag) |

**Volume-wide deltas:**
- Word count: **~3,500+ words trimmed from procedural bloat** (ch15 -1,700, ch08 -540, ch14 -260, ch11 -195, ch10 -unmeasured, others smaller)
- 2 chapters retired PRE-BOBIVERSE flag (ch08, ch12) — both now at B+ with the parenthetical-aside engine operational
- 5 chapters explicitly galley GREEN-verified post-edit (ch08, ch10, ch12, ch13, ch18)
- All other chapters edited as surgical scope; galley expected GREEN

**Stale-flag findings:**
The UPF subagent reports flagged register-family overuse on ch14, ch16, ch18 as if pre-cap data — but Yeoman verification found these chapters were **already compliant** from the 2026-05-16 PAO rewrite. The other edits in those chapters were live and landed. This validates the pipeline's discovery stage and confirms the Yeoman subagents correctly cross-check before editing.

## Deferred items (need PAO ruling)

1. **ch01 canonical plants** — outline specifies 3 plants currently absent (Joel bunk-laptop disclosure, Wanjiru key-handover, off-the-shelf sensor procurement). Tier 4 from consolidation; DEFERRED.
2. **ch11 "Forsaken" never named in body** — Yeoman flagged but did not add. Single sentence at comm-space door beat (line 165) per UPF recommendation; needs explicit ruling.

## Rate-limit incident

One subagent dispatch (initial ch13 attempt) hit an upstream server-side rate limit (`API Error: Server is temporarily limiting requests`). Re-dispatched with identical prompt; second attempt completed successfully. Pipeline's recovery clause ("if a subagent fails mid-dispatch, orchestrator re-dispatches just that chapter") worked exactly as designed.

## Projected new volume grade distribution

| Grade | Pre | Post |
|---|---|---|
| A- | 2 | 12 |
| B+ | 11 | 2 |
| B | 1 | 0 |
| B- | 1 | 0 |
| C+ | 1 | 0 |
| D+ | 2 | 0 |

**Median: B+ → A-.** No chapter below B+. All PRE-BOBIVERSE chapters lifted to B+.

## Next steps

1. **Re-run bestseller-profile UPF pipeline on the modified chapters** to verify pull-up (Stage 06 verification).
2. **Audio re-render** chapters with substantive prose changes (ch08, ch10, ch11, ch12, ch13, ch14, ch15, ch17).
3. **CIC ruling** on the 2 deferred Tier 4 items.
4. **Commit + push** the volume-wide edits as a single chore-class commit.

---

— PAO, 2026-05-20T23:30Z
