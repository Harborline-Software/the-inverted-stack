---
type: council-review
target: .pao-inbox/_decisions/2026-04-30-voice-pass-priority-queue.md
date: 2026-05-04
reviewer: Kleppmann Council (5 seats)
scope: ADR-style review of voice-pass queue ordering and Phase 4b sequencing
length: ~3,200 words
---

# Kleppmann Council Review - Voice-Pass Priority Queue

**Document under review:** `.pao-inbox/_decisions/2026-04-30-voice-pass-priority-queue.md`
**Companion documents read:** `2026-05-01-phase4-prune-scope.md`, `2026-04-30-word-count-target-revision-proposal.md`, `2026-05-04-phase4a-block1-closure.md`, `ASSEMBLY.md`, `docs/book-update-plan/state.yaml`, `docs/book-update-plan/working/45-collaborator-revocation/outline.md` §F, `docs/book-update-plan/working/9-chain-of-custody/outline.md` §F.

This is a planning-document review. The queue is not a chapter; it is a sequencing decision PAO drafted on 2026-04-30 and has not revisited since CO's 2026-05-01 directive that word-count targets are recommendations, not drivers. The council reads it as an ADR with a half-life problem.

---

## SEAT 1 - Kleppmann (distributed-systems pragmatist)

**Score: 6.5/10 - PROCEED with reservations.**

The queue's *technical* reasoning - what voice-pass unblocks for which chapter - is largely defensible to a hostile reviewer who doesn't know the book. The dependency graph as stated is real: Ch23 §Collaborator Revocation cannot be Phase-4b-pruned until #45 voice-pass clears, because cuts inside an extension section that hasn't been voice-checked would touch prose the human author has not yet authored. That part is sound. The Tier 1 → Tier 2 → Tier 3 ordering also has a plausible critical-path story: #45 unblocks the largest single piece of post-prune work (Ch23, currently 9,732 words), and Ch23 is the single largest chapter in the manuscript. If you wanted to argue that voice-passing #45 first minimizes the longest blocking dependency, the argument holds.

What does *not* hold under hostile reading is the precision of the unblock claims. The queue asserts "~400 words deeper compression" for #45, "~200 words" for #43 §Performance Contracts, "~150 words" for #46, "~200 words" for #47, "~100 words" for #9. Where do those numbers come from? They are not in `2026-05-01-phase4-prune-scope.md` (which explicitly disclaims numerical targets). They are not in the working-dir prose-review reports. They appear to be PAO's pre-CO-directive estimates from `2026-04-30-word-count-target-revision-proposal.md`, which CO has since explicitly downgraded ("the 135k target was a PAO recommendation, not a CO ratification"). The queue is still ordering Tier 1/2/3 by word-count-unlock magnitude - the exact metric CO told PAO not to drive on. That's a stale dependency on a deprecated framing.

A second technical concern: Tier 1's framing of #45 as "single highest-leverage voice-pass for the manuscript's overall trajectory" treats trajectory as a per-word metric. But the prune scope doc names a different metric - "earn its place." If the right question is "which voice-pass clears the largest editorial-judgment surface area," the answer might still be #45 (Ch23 is huge), but the queue doesn't make that argument. It makes the word-count argument.

**Reservations:**
1. Re-derive the Tier ordering against an "earn-its-place editorial surface" metric, not word-unlock. If #45 is still Tier 1 under that metric, fine - say so.
2. Strip or qualify the per-extension word-unlock estimates. They cite a deprecated framing.

---

## SEAT 2 - Shevchenko (production-experience skeptic)

**Score: 4.5/10 - BLOCK.**

The queue claims "30–60 min per extension, 5–8 hours total, parallelizable across sessions." This is timeline fantasy on a generous reading. Consider what the queue is actually asking the author to do for #45 alone: read the Ch23 §Collaborator Revocation section as it stands; read outline.md §F (which is itself ~500 words of candidate framings); pick or write an opening anecdote that grounds a 3,100-word section about access termination, post-departure key rotation, cached-copy management, propagation, bilateral data partition, and audit trail; calibrate Sinek register against a memory file PAO knows is stale (the `feedback_voice_sinek_calibration.md` is 6 days old per system reminder and was originally about Ch01, not a Ch23 security section); insert a Ch23↔Ch20 connective-tissue line at the right narrative seam in two chapters that are themselves under voice-pass-locked compression; commit, then promote the extension state.

The empirical evidence the queue's own working dirs provide directly contradicts the 30–60 min claim. Look at #48 key-loss recovery - the only extension that has actually completed voice-pass - its history in state.yaml runs across iter-0019 through iter-0021 (anecdote insert, connective tissue, Sinek calibration), each with separate commits, and ate roughly 90 minutes of CO time *plus* a Round-3 council recheck and a literary-board pass and an out-of-band factual correction five days later. That's the existence proof. One voice-pass took ~2 hours, generated downstream review work, and required a follow-up correction. Multiplied across 9 extensions: 18+ hours, not 5–8. And #48 was the *easiest* one - the Uncle Charlie anecdote was a real lived event the author could draw on directly.

#45 is harder. The three candidate framings in outline.md §F - departing employee at desk, business partner reading court-mediated message, administrator processing decade-long colleague's revocation - are three distinct emotional registers. None of them are pre-decided. The "departure-moment" placeholder at §B.4 is explicitly a structural void that the author must fill from lived experience. If CO doesn't have a directly applicable real story for revocation (and the queue gives no evidence they do), this is a creative-writing problem, not a 30-minute editorial task.

The queue also ignores that voice-pass #43 + #45 + #11 + #44 + #46 + #47 + #9 + #10 + #12 are not independent. Three of them touch Ch23 (#45, #47, #9, #10 - actually four). Two touch Ch20 (#43, #45, #10). Two touch Ch15 (#12). The author cannot voice-pass them in isolation; each one perturbs the chapter the next one touches. That coupling means voice-pass #1 → review #2 → re-read #1 → voice-pass #2 → review effects on Ch20 → … This is not parallelizable across sessions; it requires sequential context-loading the queue does not budget for.

**Blocking issue:** The cost estimate is materially wrong by an order of magnitude. CO will start, get tired, stop, and the queue will sit. The plan does not survive contact with the bandwidth it actually has. Until the cost is honest, sequencing is academic.

---

## SEAT 3 - Okonkwo (failure-mode/risk angle)

**Score: 6.0/10 - PROCEED with reservations.**

The interesting question for this seat is: what's the failure mode if the queue is wrong? Three scenarios, ranked by likelihood.

**Scenario A - The queue is roughly right, CO works through it slowly, manuscript ships in 6–10 weeks.** Acceptable outcome; no risk surfaced.

**Scenario B - CO doesn't have bandwidth, voice-pass cadence is one extension every 2 weeks, manuscript stalls at 95% complete for the rest of 2026.** This is the failure mode the queue does not address. The queue treats voice-pass as a ready-to-execute work item; it does not contemplate the case where the work item never gets picked up. There is no kill trigger. There is no "if this hasn't moved in N weeks, here's the fallback." A book that's 95% complete and stuck is a worse outcome than a book that ships at 90% complete with explicit caveats - but the queue offers no path to the latter.

**Scenario C - CO does Tier 1 (~3 extensions), runs out of energy, and the manuscript ships with Tier 2/3 extensions either dropped or shipped with bracket-text placeholders.** This is the most likely outcome by Bayesian prior. The queue does not contemplate this either. It treats all 9 as must-complete.

The risk this seat sees most clearly: the queue is structured to look like a checklist when it should be structured as a triage. A triage queue would say: "if you only do 3, do these. If you only do 1, do this. If you do none, here's the contingency." The current document says "do all 9 in this order" - which is a project plan, not a risk-aware queue.

A second risk: the queue's reliance on PAO state-tracking for status ("Yeoman or PAO promotes the extension `awaiting-voice-check → approved` in state.yaml afterward") creates a coupling between author work and editorial-pipeline state. If CO does the voice-pass on a flight, on paper, in a hotel - without immediately updating state.yaml - the queue's tracking decoheres from reality. The state-management overhead is non-trivial and the queue understates it.

**Reservations:**
1. Add a triage tier: "if CO only has bandwidth for N extensions, do these N." Specifically name which 3 are minimum-viable.
2. Define an explicit kill trigger: "if no voice-pass clears in 4 weeks, PAO escalates to CO with a ship-as-is option for Tier 3."
3. Decouple state.yaml updates from the voice-pass session itself; PAO can do them on the next sweep.

---

## SEAT 4 - Voss (negotiation/framing)

**Score: 5.5/10 - PROCEED with reservations.** (Bordering on BLOCK.)

This seat is the one that will not pretend the framing is neutral. Read the queue as a procurement document: who wants this work to happen in this order, and why?

The queue's stated optimization is "cost-of-delay for the manuscript's trajectory." The actual revealed optimization is "what unblocks PAO's queued work." Look at the language. Tier 1 #45's justification is "Voice-pass on this section UNBLOCKS Phase 4 prune of Ch23." Whose work is Phase 4 prune? Yeoman's, directed by PAO. Tier 1 #43's justification: "Ch11 §Performance Contracts becomes available for compression." Whose? Same. Tier 2 #44: "unlocks deeper Ch16 compression (~300 words)." Same. Every Tier 1 and Tier 2 justification is structured as "this unblocks more work for PAO+Yeoman."

That is not the same thing as "this maximizes reader value." A reader-value-driven queue would order by: which voice-pass adds the most missing emotional grounding to the chapter as a reader would experience it. Under that metric, #11 (Fleet Management - the entire Ch21, the reader's first impression of Part V) is plausibly the most reader-affecting voice-pass on the list, and the queue ranks it third. #45 is high under both metrics. But #43 (Performance Contracts - a sub-section in Ch11 plus a sub-section in Ch20, with 2 unresolved CLAIM markers) is plausibly the *least* reader-affecting voice-pass on the list, and the queue ranks it second.

The framing of "PAO continues in /loop, not blocking on this" at the document close is also revealing. Translation: PAO has work it wants to ship downstream, and the voice-pass queue is the gating event. The cost-of-delay framing is honest about whose cost - it's PAO's, not the reader's. CO should read the queue with that lens and decide whether the implicit prioritization matches what CO wants.

A specific manipulation pattern worth naming: the document opens with "9 extensions sit at `awaiting-voice-check`" - framing the count as urgent without acknowledging that the author has not actually agreed all 9 must clear before assembly. The queue assumes 9-must-complete; it does not negotiate that assumption.

**Reservations:**
1. Reframe each tier's justification in *reader value* terms, not unblock-PAO-work terms. If Tier 1 still holds under reader-value framing, say so explicitly.
2. Acknowledge the implicit PAO-convenience optimization. "The queue is optimized for downstream pipeline throughput" is honest; "highest-leverage for the manuscript" is rhetorical.
3. State the assumption that all 9 must clear, and surface the alternative: ship with subset cleared and Tier 3 either dropped or compressed-without-anecdote.

---

## SEAT 5 - Klett (architecture-economic / opportunity-cost)

**Score: 5.0/10 - BLOCK.** (The opportunity-cost analysis fails.)

This is the seat the queue has not survived. CO's 2026-05-01 directive is unambiguous: "Phase 4 and all future prune is quality-driven, not number-driven. Don't frame prune as 'land at X' arithmetic; cut what doesn't earn its place; if the answer is nothing, the chapter stays." Apply that same standard to the voice-pass queue and Tier 3 fails on contact.

Look at what Tier 3 actually proposes:

- **#9 Chain-of-Custody** - Ch23 section, ~2,400 words drafted. Voice-pass needs an opening anecdote about commercial-driver dashcam evidence handoff. CO has no professional history in commercial trucking, insurance forensics, or evidence chain-of-custody. The outline.md §F candidate framings are not lived stories; they are scenario sketches. Voice-pass would produce *invented* anecdote prose, which by the book's own standard ("personal anecdotes" - CLAUDE.md Stage 6) is not what voice-pass is for. Cost: 60+ minutes of author work to write fiction. Unlock: ~100 words of compression that wouldn't show up in a reader's experience anyway.

- **#10 Data-Class Escalation** - restaurant-collision footage scenario. Same critique. CO has no restaurant-fleet ops history. This is invented dramatization, not lived altitude. Cost: 60+ minutes. Unlock: ~150 words of compression.

- **#12 Privacy-Preserving Aggregation** - relay-side differential privacy. The queue's own description: "author voice-pass is light." If voice-pass is light, the question is not "when do we voice-pass" but "do we need voice-pass at all, or does this section ship as the prose-reviewer left it?" The queue does not consider this option.

The earn-its-place test, applied to Tier 3: does each of these voice-passes earn its 30–60 minutes of author-time investment against the alternative of *cutting the requirement entirely*? For #12 the answer is plausibly no (skip voice-pass, ship the section). For #9 and #10 the answer is "only if CO has lived material to draw on, which the queue has not surfaced evidence of."

The queue's framing implicitly assumes voice-pass is mandatory for every section flagged `awaiting-voice-check`. That assumption is not in CLAUDE.md Stage 6. Stage 6 says "the author adds personal context, field anecdotes, and the connective tissue that makes the book a book rather than a report." If a section already reads as a book and not a report - which is the prose-reviewer's job to ensure - then the voice-pass requirement may already be substantively met by the prose-review, and the formal `awaiting-voice-check` flag is editorial bookkeeping, not a real gate.

A second opportunity-cost analysis: the hybrid path. The voice-* agents (`voice-brown`, `voice-gladwell`, `voice-godin`, `voice-grant`, `voice-lencioni`, `voice-sinek`) exist at `.claude/agents/`. The voice-pass orchestrator at `build/voice-pass.py` is wired to dispatch them. The #48 voice-pass actually *used* `voice-lencioni` and `voice-brown` to produce three anecdote candidates each, then CO picked one and edited (per state.yaml iter-0021 record: "Three voice-agent anecdote candidates produced for human voice-pass: voice-lencioni (3 scenes - Elena/master-password, Daniel/encrypted drives, Marcus/missing YubiKey) and voice-brown (3 confessions - Seed Phrase, Family Death, Migration). Six total anecdote drafts available; human picks one (or writes their own using these as creative prompts)."). The queue does not propose this for the remaining 8. Why not? It would 2-3× CO's throughput on the queue.

**Blocking issues:**
1. Tier 3 fails the earn-its-place standard. Either explicitly justify why each of #9/#10/#12 needs author voice-pass (with evidence the author has lived material), or surface them as candidates for skip-voice-pass-and-ship.
2. The hybrid voice-agent-then-CO-edits path was used successfully on #48 and is not proposed for the remaining 8. That is a missed throughput multiplier the queue does not analyze.

---

## CONSOLIDATED VERDICT

| Seat | Score | Verdict |
|---|---:|---|
| Kleppmann (technical reasoning) | 6.5 | PROCEED with reservations |
| Shevchenko (bandwidth realism) | 4.5 | **BLOCK** |
| Okonkwo (failure-mode/risk) | 6.0 | PROCEED with reservations |
| Voss (framing/negotiation) | 5.5 | PROCEED with reservations |
| Klett (opportunity cost) | 5.0 | **BLOCK** |
| **Average** | **5.5** | **BLOCK (2 BLOCK votes)** |

**Final verdict: BLOCK.**

Per council rules: any BLOCK is a block. Two seats (Shevchenko, Klett) BLOCK on substantive, falsifiable grounds - the cost estimate is materially wrong, and Tier 3 fails CO's own earn-its-place standard. The queue is not unsalvageable; it is partially right (the dependency graph and Tier 1 ordering largely hold) but partially staled by CO's 2026-05-01 directive and partially misframed (PAO-convenience optimization presented as reader-value optimization).

---

## CONSOLIDATED ACTION ITEMS

Numbered, prioritized. Apply in order.

1. **Cut #12 from the queue.** Per the queue's own admission, voice-pass is "light." Reclassify the section as `prose-review-passed; voice-pass optional`. Ship it as the prose-reviewer left it unless CO opts in. (Klett blocking; Shevchenko concurs.)

2. **Reframe #9 and #10 as conditional.** Surface the question to CO directly: "Do you have a lived dashcam/fleet-evidence story for #9? A restaurant-fleet story for #10? If no to both, propose: skip voice-pass, ship as prose-reviewer left them, or strip the placeholder voice-check comments and tighten the surrounding prose." (Klett blocking.)

3. **Re-cost the queue with empirical data.** Use #48's actual voice-pass duration (~90 min anecdote + ~30 min connective tissue + ~30 min Sinek calibration + Round-3 council + literary-board + factual correction = realistically 3+ hours of CO time amortized). Multiply by 6 (remaining serious extensions, post-action-2). Honest estimate: 18–24 hours, not 5–8. (Shevchenko blocking.)

4. **Propose hybrid path for the remaining 6 (#43, #45, #11, #44, #46, #47).** Pre-dispatch `voice-brown` + `voice-lencioni` (the two registers that worked on #48) to produce 3 anecdote candidates per extension *before* CO sits down. CO's session becomes "pick + edit" instead of "draft from blank." This was the proven flow on #48. (Klett blocking; Shevchenko concurs.)

5. **Reorder Tier 1 by reader-impact, not unblock-PAO-work.** Specifically: surface whether #11 (Fleet Management - entire Ch21) outranks #43 (Performance Contracts - a sub-section in Ch11 plus a sub-section in Ch20) for the reader's first-impression-of-Part-V argument. If yes, swap. (Voss reservation.)

6. **Add a triage tier: minimum-viable voice-pass for ship.** If CO only has bandwidth for 3, name those 3 (council's tentative answer: #45, #11, #43 - in that order). State the manuscript can ship with Tiers 2 and 3 either skipped or deferred to a Volume-1 dot-release. (Okonkwo reservation.)

7. **Add a kill trigger.** "If no voice-pass clears in 4 weeks, PAO writes a `pao-question` beacon to XO surfacing ship-as-is options." The queue currently has no escape velocity. (Okonkwo reservation.)

8. **Strip the per-extension word-unlock estimates** ("~400 words", "~200 words", etc.). They cite a deprecated framing (the 135k recommendation CO has not ratified). The Phase 4b unlock claim should read "unlocks Phase 4b earn-its-place pass on the parent section" - not a number. (Kleppmann reservation.)

9. **Acknowledge the PAO-convenience optimization explicitly.** Rewrite the TL;DR as: "The queue orders the 9 by what unblocks the most downstream Phase 4b/assembly work for the editorial pipeline. CO should review whether this matches the reader-value optimization or whether to reorder accordingly." (Voss reservation.)

10. **Decouple state.yaml updates from the voice-pass session.** PAO can sweep state on the next /loop pass; CO does not have to remember to update YAML on the same flight. (Okonkwo reservation.)

---

## DISSENT

Kleppmann (Seat 1) dissents from the BLOCK verdict on grounds that the queue's *technical* dependency reasoning is sound enough to PROCEED with reservations; the queue's word-unlock claims are stale but the underlying ordering largely survives a reader-value reframe. Kleppmann would have voted PROCEED-with-reservations. Two BLOCKs from Shevchenko and Klett carry the verdict.

---

**End of review.** PAO should treat this as a Round 1 adversarial review of the queue itself, revise per the 10 action items, and re-submit for Round 2 if any council member's reservations carry into the revision.
