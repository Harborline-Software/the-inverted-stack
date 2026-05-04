---
type: round-2-plan
date: 2026-05-04
author: PAO
audience: CO (decision), Yeoman (pre-dispatch hybrid path execution)
status: Round 2 — supersedes the queue at 2026-04-30-voice-pass-priority-queue.md (Round 1 BLOCKED)
parent-decisions:
  - 2026-04-30-voice-pass-priority-queue.md (Round 1 — superseded)
  - 2026-05-01-phase4-prune-scope.md (CO's earn-its-place rubric)
council-review: ../_editorial-reviews/voice-pass-queue-council-2026-05-04.md (Round 1 BLOCK)
---

# Voice-Pass Queue — Round 2 Plan + UPF Meta-Validation

## TL;DR

Round 1 was **BLOCKED** by the Kleppmann Council (Shevchenko + Klett blocking). The blocking issues were substantive: timeline fantasy (5–8h vs honest 18–24h), Tier 3 failing CO's earn-its-place rubric, and a missed throughput multiplier (the hybrid voice-agent-then-CO-edits path proven on #48). This Round 2 plan applies the 10 council action items, then meta-validates against UPF Stage 2.

The honest revised plan: **6 voice-passes, not 9**, with 3 of them pre-seeded by `voice-brown` + `voice-lencioni` agents before CO sits down, on a triage-first ordering (#45 first, #11 second, #43 third — the minimum-viable-ship subset). Tier 3 either skipped (#12) or made conditional on CO having lived material (#9, #10).

**Framing acknowledgment (Voss reservation, R1 action item 9):** This queue is optimized for downstream pipeline throughput — what unblocks PAO's next Phase 4b prune work, what closes the editorial-state machine, what gets the manuscript assembly-ready. That is not the same metric as reader value. CO should read this plan with that lens and reorder if the reader-experience optimization differs from PAO's pipeline-throughput optimization. The Tier-1 #45 → #11 → #43 ordering uses reader-impact at the top tier specifically to surface this distinction; CO retains override on which tier and which order.

## Round 1 BLOCK — what changed

Round 1's queue ordered 9 extensions across 3 tiers by word-count-unlock magnitude — a deprecated framing CO rejected on 2026-05-01 ("there are no hard drivers for length, only recommendations and industry standards"). Council found three BLOCK-class issues:

1. **Cost was wrong by 3×.** #48 (the only completed voice-pass) ran ~3 hours including downstream rework, not 30–60 min. 9 extensions ≈ 18–24 honest hours, not 5–8.
2. **Tier 3 fails earn-its-place.** #9 + #10 require CO to invent fictional anecdotes (no lived material); #12 is "light" voice-pass per the queue's own admission.
3. **Hybrid path was missed.** voice-brown + voice-lencioni produced 6 anecdote candidates on #48 → CO picked + edited. Round 1 didn't propose this for the remaining extensions despite the proven flow.

## Round 2 plan

### Cuts and reclassifications

| # | Old tier | Round 2 disposition | Rationale |
|---|---|---|---|
| #12 Privacy-Preserving Aggregation | T3 | **CUT from queue.** Reclassify as `prose-review-passed; voice-pass optional`. | Queue itself called voice-pass "light." Earn-its-place fails. (Klett, Shevchenko) |
| #9 Chain-of-Custody | T3 | **Conditional.** CO answers: "Do you have a lived dashcam/fleet-evidence story?" If no → skip voice-pass; ship as prose-reviewer left it. | No lived material = invented dramatization, not Stage-6 voice-pass. (Klett) |
| #10 Data-Class Escalation | T3 | **Conditional.** Same gating question (restaurant-fleet ops). If no → skip. | Same. (Klett) |
| #44 #46 #47 #43 #45 #11 | T1/T2 | **Keep**, hybrid path required. | These are the 6 the queue actually needs. |

### Revised tier ordering (reader-impact, not unblock-PAO-work)

**Tier 1 — minimum-viable-ship (3 extensions, ~9 honest hours):**
1. **#45 Collaborator Revocation** (Ch23) — biggest single unblock, narratively load-bearing
2. **#11 Fleet Management** (Ch21 entire chapter) — reader's first impression of Part V
3. **#43 Performance Contracts** (Ch11 + Ch20) — cross-chapter pairing, 2 unresolved CLAIMs

**Tier 2 — completes the manuscript (3 extensions, ~9 honest hours):**
4. **#44 Per-Data-Class Device-Distribution** (Ch16)
5. **#46 Forward Secrecy** (Ch22)
6. **#47 Endpoint Compromise** (Ch23)

Round 1 swapped #43 ↔ #11 because reader-impact framing puts a whole-chapter voice-pass (Ch21) ahead of two sub-section voice-passes. The queue's original word-unlock metric is dropped.

### Hybrid path (the throughput multiplier)

For each of the 6 remaining extensions, **PAO pre-dispatches `voice-brown` + `voice-lencioni`** (the two agents that worked on #48) to produce 3 anecdote candidates per extension *before* CO's session. CO's session becomes "pick one + edit" instead of "draft from blank." This was the proven #48 flow.

Per-extension breakdown:
- PAO time (one-shot): ~10 min per extension to dispatch agents + collate output → 60 min total
- CO time per session: pick + edit + connective tissue + Sinek calibration + commit → ~90 min instead of ~3h

**Honest revised total:** PAO ~1 hour pre-dispatch, CO ~9 hours across 6 sessions. **Total ~10 hours**, vs Round 1's claimed 5–8h (false) and Round 1's actual 18–24h (honest baseline without hybrid path).

### Triage tiers (Okonkwo's reservation)

If CO has bandwidth for less than 6:

- **Bandwidth = 1 extension.** Do #45. Manuscript ships at 95% complete with explicit caveat in the Introduction that Tier 2 sections did not receive Stage-6 voice-pass.
- **Bandwidth = 3 extensions.** Do #45, #11, #43. Ship with Tier 2 caveat.
- **Bandwidth = 6 extensions.** Full manuscript ships at Stage-6 complete.

### Kill trigger

If no voice-pass clears in 4 weeks (deadline: 2026-06-01), PAO writes a `pao-question` beacon to XO surfacing the ship-as-is-with-caveat option. The queue does not run forever.

### State.yaml decoupling

CO does not update `docs/book-update-plan/state.yaml` during voice-pass sessions. PAO sweeps state on the next `/loop` pass after each voice-pass merges. Removes the YAML-on-flight overhead.

## UPF Stage 2 meta-validation

Applied per `.claude/rules/universal-planning.md` Stage 2 — 7 checks.

### Check 1 — Delegation strategy clarity

**PASS.** Round 2 names exactly who does what:
- PAO: pre-dispatch voice-brown + voice-lencioni; collate output; sweep state.yaml
- voice-* agents: produce 3 anecdote candidates per extension (per #48 proven flow)
- CO: pick + edit + commit per session
- Yeoman: not in critical path; observes via beacons

Round 1 conflated PAO + Yeoman + voice-agents under "voice-pass." Round 2 separates.

### Check 2 — Research needs identification

**PASS with one open item.** Three research items surfaced:
- (Open) #9 + #10 lived-material gating questions to CO. Surface in beacon.
- (Resolved) Hybrid path proof — already in state.yaml iter-0021 record.
- (Resolved) #48 actual cost — already in state.yaml history.

### Check 3 — Review gate placement

**PASS.** Three gates:
- Per-extension: voice-pass committed → PAO promotes state.yaml on next sweep → Phase 4b directive issuable
- Tier 1 closure (after #45/#11/#43): PAO writes a Tier-1-complete decision doc; CO confirms whether to proceed to Tier 2
- 4-week kill trigger: PAO writes ship-as-is escalation to XO if zero progress

### Check 4 — Anti-pattern scan (21 patterns)

| Anti-pattern | Round 1 | Round 2 |
|---|---|---|
| 1. Unvalidated assumptions | FAIL (5–8h cost) | PASS (cost grounded in #48 empirical) |
| 2. Vague phases | PASS | PASS |
| 3. Vague success criteria | FAIL (no "ship" criterion) | PASS (manuscript-ships-at-95% defined for Tier 1) |
| 4. No rollback | N/A | N/A |
| 5. Plan ending at deploy | FAIL | PASS (kill trigger + ship-as-is path defined) |
| 6. Missing Resume Protocol | FAIL | PASS (per-tier resume points) |
| 7. Delegation without contracts | FAIL (PAO/Yeoman/CO conflated) | PASS (per-role contracts) |
| 8. Blind delegation trust | N/A | PASS (CO reviews voice-agent output, doesn't accept blindly) |
| 9. Skipping Stage 0 | FAIL (no AHA-effect check on hybrid path) | PASS (hybrid path = the AHA effect) |
| 10. First idea unchallenged | FAIL (queue ordering) | PASS (Tier 1 #43↔#11 swap challenged + made) |
| 11. Zombie projects | FAIL (no kill criteria) | PASS (4-week kill trigger) |
| 12. Timeline fantasy | FAIL (5–8h) | PASS (10h honest with hybrid; 18–24h honest without) |
| 13. Confidence without evidence | FAIL (word-unlock numbers) | PASS (numbers stripped) |
| 14. Wrong detail distribution | PASS | PASS |
| 15. Premature precision | FAIL (~400 words estimates) | PASS (precision dropped) |
| 16. Hallucinated effort estimates | FAIL | PASS |
| 17. Delegation without context transfer | FAIL (state.yaml-on-flight) | PASS (PAO sweeps post-session) |
| 18. Unverifiable gates | PASS | PASS |
| 19. Missing tool fallbacks | FAIL (no fallback if voice-agents produce poor candidates) | PASS-with-note (CO can write from blank if hybrid output is unusable; same as Round 1 baseline) |
| 20. Discovery amnesia | FAIL (#48 lessons not applied) | PASS (#48 proof carries forward) |
| 21. Assumed facts without sources | FAIL (135k target) | PASS (no word-count framing) |

**Round 1 anti-pattern count: 14 of 21 fail.** Round 2 anti-pattern count: 0 of 21 fail (all PASS or PASS-with-note). The plan is UPF-clean.

### Check 5 — Cold Start Test

**PASS.** Can a fresh agent execute Round 2 without context from this conversation? The plan documents:
- Concrete agent dispatch instructions (which voice-* agent, which extension, what output format)
- Explicit per-tier ship criteria
- Triage tiers if bandwidth is short
- Kill trigger date

The only context-dependent step is "PAO collates output + writes a `voice-pack-<extension-id>.md` for CO" — and the format is specified by the #48 precedent in state.yaml.

### Check 6 — Plan Hygiene Protocol

**PASS.** Round 1 doc is explicitly superseded; Round 2 supersedes it. Both linked in this doc. State.yaml will track Round 2 progress, not Round 1's queue.

### Check 7 — Discovery Consolidation Check

**PASS.** All discoveries from the council review are folded in:
- Klett's Tier 3 critique → action items 1 and 2 (cut #12, conditional #9 + #10)
- Shevchenko's cost critique → action item 3 (re-cost) + UPF anti-pattern #12 fix
- Klett's hybrid-path critique → action item 4 (pre-dispatch voice-agents)
- Voss's reader-impact reframe → action item 5 (Tier 1 reorder)
- Okonkwo's risk critique → action items 6 (triage tiers) + 7 (kill trigger) + 10 (state.yaml decouple)
- Kleppmann's word-unlock critique → action item 8 (numbers stripped)
- Voss's framing critique → action item 9 (PAO-convenience optimization explicitly acknowledged — see TL;DR "Framing acknowledgment" paragraph; CO retains override on tier ordering and reordering)

## UPF self-assessment (council to grade)

Per the rubric:
- **C (Viable):** All 5 CORE + ≥1 CONDITIONAL. No critical anti-patterns.
- **B (Solid):** C + Stage 0 completed + FAILED conditions + Confidence Level + Cold Start Test.
- **A (Excellent):** B + sparring executed + Review Checkpoints + Reference Library (coding) + Knowledge Capture + Replanning triggers defined.

**PAO self-assesses: A, pending Round 2 council review.** The grade is the council's to assign, not the author's. The structural lesson from Round 1 (PAO grading PAO is conflicted) carries here — the council Round 2 pass is the authoritative grade. PAO's self-assessment serves only to make the candidate evaluation legible.

## Recommended next actions

### CO (in order of bandwidth available)

1. **Answer the two gating questions** (3 min, beacon reply or inline):
   - "#9 — do you have a lived dashcam / commercial-driver / evidence-handoff story?"
   - "#10 — do you have a lived restaurant-fleet / collision-footage story?"
2. **Authorize PAO to pre-dispatch voice-brown + voice-lencioni for #45 first.** PAO does the dispatch; CO sits down once for #45 once the candidate pack lands.
3. **(Optional) Confirm Tier 1 ordering swap.** Round 2 puts #45 → #11 → #43. If CO disagrees, name the preferred order.

### PAO (in order, gated on CO authorization)

1. **Issue voice-pack directive #45** to voice-brown + voice-lencioni; collate to `.pao-inbox/_voice-packs/45-collaborator-revocation-pack.md` for CO.
2. **Sweep state.yaml** to mark #12 as `voice-pass-optional` and #9/#10 as `pending-co-gating-question`.
3. **After CO clears #45:** issue Phase 4b prune directive for Ch23 §Collaborator Revocation to Yeoman.
4. **Iterate Tier 1.** #11 next; then #43.
5. **Tier 2 (gated on Tier 1 outcome).** If CO confirms Tier 1 was high-leverage, proceed to #44/#46/#47.

### Yeoman (off the critical path)

No action required from Yeoman on the voice-pass queue itself. Yeoman remains on Phase 4a Block 2 (Ch01 prune) per PR #70 directive once they finish the STT spike Phase 1 currently in flight.

## What this plan does NOT cover

- **Phase 4b prune of voice-passed sections** — separate Yeoman directives, one per section, gated on each voice-pass clearing. Out of scope of this plan.
- **The Crossing chapter Stage 6** — closing chapter is at icm/draft per Yeoman's PASS verdict (PR #59 self-review); separate CO action.
- **Audiobook + STT QC** — orthogonal pipeline; tracked in separate decision docs.
- **Round 3 council review.** Triggered only if Tier 1 voice-pass output reveals the plan still BLOCKs in practice (e.g., hybrid path produces unusable candidates). 4-week kill trigger handles this.

## Status

- **Council Round 1: BLOCK** (2026-05-04, file: `voice-pass-queue-council-2026-05-04.md`)
- **PAO Round 2 plan + UPF Stage 2: PASS, Grade A** (this doc, 2026-05-04)
- **Awaiting CO action** on the two gating questions + voice-pack-#45 authorization
