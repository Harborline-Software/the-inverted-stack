# Book 2 - Chapter-by-Chapter Outline (working blueprint)

> **Working title:** TBD. Concept artifacts use *Book 1 of the Sunfish series* / *Vol 2*.
> **Status:** outline drafted 2026-05-04 (PAO). All chapters at `icm/outline`. Pipeline plumbing in `build/audiobook.py` is staged but inert until Arc 1 reaches `icm/draft`.
> **Source artifacts:** read in this order before drafting any chapter:
> 1. `.pao-inbox/_creative/vol-2-software-as-gravity.md` - **CANONICAL** structural framing (LOCKED 2026-05-05; Ch 2 v3 listen-test verdict forced this canon). Software is gravity, not character. Six rails; per-chapter rail assignments below; captain-asks-engineer demoted from default to install-engine + selective. **Read this BEFORE the chapter outline entries.**
> 2. `.pao-inbox/_creative/vol-2-concept-note-2026-05-04.md` - the 12-section synthesis (note: §6.2 captain-asks-engineer is superseded by software-as-gravity canon above)
> 3. `.pao-inbox/_creative/vol-2-concept-locked-elements-2026-05-04.md` - running locks index
> 4. `.pao-inbox/_creative/vol-2-archive-and-capture-convention.md` - **canonical** Anchor stack + voice-register split + graceful degradation + forensic substrate + OSS-funding-asymmetry (LOCKED 2026-05-05)
> 5. `.pao-inbox/_creative/vol-2-anchor-bridge-sync-mechanic.md` - **canonical** bandwidth-bounded surface windows + Wanjiru's sync-triage + conditional preservation (LOCKED 2026-05-05)
> 6. `.pao-inbox/_creative/series-arc-sunfish-trajectory.md` - series-canon-only; **never referenced from Vol 2 prose**; chapter-drafter awareness tool only (LOCKED 2026-05-05)
> 7. `.pao-inbox/_creative/character-sheets/` - Anna, Joel, Priya, Wanjiru, Stefan as a minimum for Book 1
> 8. `.pao-inbox/_creative/forsaken-position-papers/` + `oss-architects-voices/` - voice references
> 9. `.pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md` - mission timeline
> 10. `.claude/skills/crew-log-style-entry/SKILL.md` - generator skill for formal-log + diary entries
>
> **What this document is:** the working blueprint. Each chapter entry carries everything a drafter (inline PAO at xhigh, technical-book-writer agent, or human) needs to produce a first draft *without re-deriving structure from the concept note each time*. The 8 sample story arcs from concept note §7 form the spine; the supporting/connective chapters fill the act structure to ~18 chapters / ~85,000-90,000 words / ~9-10 hours audiobook.

---

## Three-act structure (concept note §6.3)

| Act | Days | Chapters | Word target | Audiobook hours |
|---|---|---|---:|---:|
| **Act I - Departure and the first under-ice realization** | 1-21 | Ch 1-6 | ~30,000-32,000 | ~3.5 |
| **Act II - Subsystems hold; the contest sharpens** | 22-42 | Ch 7-12 | ~28,000-30,000 | ~3.0-3.5 |
| **Act III - Cascade, ascent, and the cumulative reveal** | 43-56 | Ch 13-18 | ~32,000-35,000 | ~3.5-4.0 |
| **Total** | 1-56 | 18 | ~90,000-97,000 | ~9-10 |

---

## Per-chapter conventions

Every chapter entry below carries the same fields:

- **Days / setting:** mission-day window + physical location
- **Primary rail:** one of the six rails from `vol-2-software-as-gravity.md` § 2 - Trust + prior betrayal / Career-cost + aging out / Class/region/institutional politics / Mission as survival / Grief, family, memory / Rival mission + institutional capture. **The chapter is about the rail. Sunfish is gravity - substrate, consequence, evidence. Not subject.**
- **Secondary rail:** optional; may carry minor weight; primary rail determines voice and scene structure
- **Architectural claim:** the single load-bearing claim from Joel's paper this chapter exercises (one chapter, one claim - never two). **Appears as evidence/consequence under the primary rail; not as the chapter's subject.**
- **Frame ratio:** % mission-present narration vs. % flashback; default 60/40 per concept note §6.1
- **Log-opener pattern:** A (formal-log opener only), B (formal-log frame), C (formal log + diary inset), or none. Used **only where it earns its place** - never as formula. See § Structural devices below.
- **Key character beats:** what each present character does or registers in this chapter
- **Length target:** word count + estimated audiobook duration at ~9,000 words/hour
- **Verification gap:** the specific thing about Joel's paper that this chapter tests against reality
- **Drafting notes:** what the drafter needs to know that isn't obvious from the concept note

---

## Structural devices and capture conventions (LOCKED 2026-05-05)

Vol 2 carries three load-bearing structural devices that thread through specific chapters. Each is documented at depth in the convention docs; this section is the cross-reference for chapter-drafters.

### Log-opener patterns

Three patterns canonical for log-opener / log-inset placement. Used **only where they earn their place** - never as formula. Per-chapter assignment in each chapter's "Log-opener pattern" field below.

- **Pattern A - formal-log opener only.** Chapter opens with the formal log; scene plays; chapter closes without further log artifact. Cheapest. Use for chapters where the orientation is the only structural lift the device adds.
- **Pattern B - formal-log frame.** Chapter opens with formal log A (pre-event); chapter closes with formal log B (post-event). The two logs differ in tone - log B knows what log A didn't. The differential is the chapter's quiet emotional arc.
- **Pattern C - formal log + diary inset.** Chapter opens with the formal log (clean, professional). Mid-chapter or end-chapter, a single italic diary entry surfaces. The formal log is what Anna recorded; the diary is what she didn't put on the record. Use for the heaviest chapters.

Generator: `.claude/skills/crew-log-style-entry/SKILL.md`. Header conventions: `vol-2-archive-and-capture-convention.md` § 9.

### Sync-mechanic threads

Six chapters carry beats from the bandwidth-bounded sync mechanic (`vol-2-anchor-bridge-sync-mechanic.md`):

- **Ch 6** - first surface window; Wanjiru explains prioritization; reader installs the constraint
- **Ch 11** - second surface window; Wanjiru triages with Stefan-cross-check race; her institutional weight forming
- **Ch 12** - Segment 3 dive; conditional-preservation stake before climax
- **Ch 14** - leak event; the boat almost didn't surface; what is at stake is the entire post-Surface-2 record
- **Ch 16-17** - limited-bandwidth transit-north; targeted records; Anna's accumulated query list
- **Ch 18** - full-bandwidth final-sync; Bridge fills; convergence of capability and preservation at docking

### Forensic-substrate threads

Five chapters carry beats from the forensic-substrate property (`vol-2-archive-and-capture-convention.md` § 8):

- **Ch 11** - Wanjiru cross-checks Stefan's PR against the Nansen's surface-window observations of his mission
- **Ch 14** - leak event captures fully on Anchor; cause queryable post-mission; sensor head from Helvetia-aligned vendor (per § 7)
- **Ch 15** - Wanjiru begins forensic queries against sensor head's pre-failure timestream; pre-degradation
- **Ch 17** - Joel + Wanjiru complete the forensic analysis on laptop-class compute; surface the supply-chain pattern
- **Ch 18** - regulatory filing reaches consortium; architectural-political contest enters institutional phase

### Per-chapter primary-rail assignments (LOCKED 2026-05-05; canon: `vol-2-software-as-gravity.md`)

Each chapter leads with one of six rails. The architecture appears as substrate, consequence, or evidence - not as subject. **Drafters write to the rail.**

| Chapter | Primary rail | Secondary rail |
|---|---|---|
| Ch 1 - Departure | Trust + prior betrayal | Mission as survival (atmosphere) |
| Ch 2 - Recruitment Interview | **Trust + prior betrayal** | - |
| Ch 3 - Drake Passage | Mission as survival | Class/region politics (Sabina + Diego) |
| Ch 4 - First Submersion | Mission as survival | (captain-asks-engineer install-chapter; see § Captain-asks-engineer demoted below) |
| Ch 5 - Day-Twenty Realization | Grief, family, memory | - |
| Ch 6 - First Surface | Trust + prior betrayal (Wanjiru's exception-refusal) | Rival mission (Stefan name surfaces) |
| Ch 7 - Joel's Sunfish | Career-cost + aging out | Grief/Long Now (boat-that-no-longer-exists) |
| Ch 8 - Second Submersion | Class/region/institutional politics (Sabina) | Mission as survival |
| Ch 9 - Sync Daemon Under Drift | Career-cost + aging out (Priya's question Joel hadn't asked himself) | - |
| Ch 10 - Aftermath of a Mission That Once Was | Trust + prior betrayal | - |
| Ch 11 - Second Surface | Rival mission + institutional capture (cross-check race) | - |
| Ch 12 - Beginning of the End | Mission as survival | - |
| Ch 13 - Schema That Should Not Migrate | Class/region/institutional politics (Priya as decider) | Career-cost (Joel walking her direction) |
| Ch 14 - The Crossing | Mission as survival (binary tech) | Trust + prior betrayal (Joel's protective beat) |
| Ch 15 - Compromised Relay Holds | Class/region/institutional politics | Career-cost (Wanjiru's institutional thinking) |
| Ch 16 - Final Ascent | Mission as survival (post-climax adaptation) | - |
| Ch 17 - Transit North | Rival mission + institutional capture + Career-cost (joint anchor) | Trust + prior betrayal (staff-history conversation) |
| Ch 18 - Punta Arenas Surfacing | Rival mission + institutional capture | Trust + prior betrayal (Stefan exchange) |

### Captain-asks-engineer demoted (LOCKED 2026-05-05)

Per `vol-2-software-as-gravity.md` § 5, the captain-asks-engineer dialogue engine is **no longer the default**. It is:
- **The install-engine for Ch 4** (First Submersion). The architecture's operational reality lands on the page through Anna asking and Joel explaining; the reader installs partition-mode behavior here.
- **Selectively elsewhere** (1-2 technical exchanges per technically-load-bearing chapter) when the chapter is genuinely about the architecture.

Most chapters lead with a different engine - the rail's engine. **Where Anna and Joel are in a scene together, the default is *what is the human stakes question between them right now* - not *what is the next architectural detail to surface.*** See `vol-2-software-as-gravity.md` § 5 for the four-question scene checklist drafters apply before any scene.

### Capability-degradation threads

The leak event in Ch 14 damages the boat's central compute hub (workstation; RTX-class GPU). Subsequent chapters register reduced capability through *what the crew does and doesn't do*, not through technical lament:

- **Ch 14** - compute hub among the operational casualties; listed in damage report
- **Ch 15** - Wanjiru's forensic queries land *before* deeper degradation; her chapter-load extends to recognize the architecture's graceful degradation as same-shape as security-architecture-under-political-attack
- **Ch 16-17** - crew operates in degraded mode; Anna's "queries to run when we surface" list grows; Wanjiru's sync-triage happens with diminished LLM assistance
- **Ch 18** - Bridge restores full capability at docking; accumulated queries get answered

Drafters see `vol-2-archive-and-capture-convention.md` § 6 for the discipline rule on registering degradation in prose.

---

# Act I - Departure and the first under-ice realization

**Days 1-21.** Establishes Anna's narrator register; introduces the crew through her command voice; installs the captain-asks-engineer dialogue engine; lands the first architectural realization (Day 20); closes on the first surface window with HELVETICA-2's preliminary results entering Anna's awareness for the first time on the boat.

---

## Ch 1 - *Departure* (Day 0, Punta Arenas)

- **Days / setting:** Day 0, 2026-09-15 (placeholder), Punta Arenas dock; ceremonial sailing.
- **Architectural claim:** none direct - this chapter installs the narrator's voice and the mission's stakes. The architecture is foreshadowed only through Wanjiru handing Anna the key set.
- **Frame ratio:** 100% mission-present. (Flashback begins in Ch 2.)
- **Log-opener pattern:** A - formal-log opener orienting the staff history (date, mission designation, Anna's role). Reader installs the diegetic-artifact convention.
- **Key character beats:**
  - **Anna:** first-person narration installed; reader registers Anna's mid-50s command-mature voice; the staff-history framing device implied (this is being written down).
  - **Joel:** present at the dock; visible respect from the crew; reader registers him as a present figure but his architect role surfaces only in Ch 4. **One-paragraph beat: equipment review on the dock; Joel mentions in passing that the sensor heads were sourced off-the-shelf from a vendor because the consortium couldn't afford the custom-firmware option.** Plants the OSS-funding-asymmetry constraint without dwelling. **CANON: Joel signature-discipline scene (per CO directive 2026-05-05 craft note).** During the equipment review, Joel walks Anna through what he's bringing on board: official engineering laptops, the boat's compute-hub workstation specs, and - quietly, without flourish - **a personal laptop he keeps in his bunk** that hosts his pre-mission notes, scratch protocols, and his commit history. *I want you to know what's on it. I want you to know it's there.* The bunk-laptop disclosure is the disclosure-without-compulsion principle instantiated in Joel's personal practice, before the mission begins. Anna registers; says nothing back; the chapter moves on. **The reader has met Joel through what he does, not through what is described about him.** This scene is canonical Vol 2 first-introduction; do not skip.
  - **Wanjiru:** key-handover scene - keys + the relay-network handoff from Helsinki ground station + the Anchor model weights and the Bridge replication-credentials needed for surface-window sync.
  - **Priya, Sabina, Diego, Hiroshi, Maria:** boarding sequence; reader registers each by name + national background + role; lighter treatment.
  - **The rival mission:** mentioned as ambient fact - *they sailed two months ago.* Stefan's name surfaces. No dramatization yet.
- **Length target:** ~4,500 words / ~30 minutes audiobook.
- **Verification gap:** none direct.
- **Drafting notes:** the chapter has to do double duty - install the narrator and seed every later thread without bloating. Prioritize the dockside scene over exposition; trust the reader to ride out unexplained references that resolve in later chapters. The Helsinki ground station + Wanjiru's relay handoff is the load-bearing operational detail; the off-the-shelf sensor procurement is the load-bearing OSS-funding-asymmetry plant; everything else is character + atmosphere. **Log-opener installs the diegetic-artifact convention** - include the closing hash signature once here so the reader registers the convention; later chapters drop the signature once it's familiar.

## Ch 2 - *The Recruitment Interview* (Arc 2 - flashback)

- **Days / setting:** flashback to ~6 months before departure; Anna's office, video call to Joel.
- **Primary rail (LOCKED 2026-05-05):** **Trust + prior betrayal.** The chapter is *what kind of man wakes up the morning after Klett tells him he's wrong* - Anna's recruitment-as-character-test, where the architecture is the **arena** in which honesty vs self-protection plays out. The chapter is NOT about the lease protocol; the chapter is about Anna's reading of Joel as he answers questions. Architectural claim below appears as **evidence** in the test, not as the chapter's subject.
- **Architectural claim:** *the architect's response to being told he was wrong is what makes the architecture trustworthy.* The R1-BLOCK-rewrite admission as foundational trust event. **Surfaces in the chapter as the load-bearing trust beat (the four sentences and the fifth) but is NOT walked through at protocol-detail depth - the chapter is about Joel's answer, not about the protocol the answer is about.**
- **Frame ratio:** 10% mission-present (frame anchor at start + end) / 90% flashback. **Note: the Pattern A formal-log opener replaces the existing Day-14 mission-frame opener; the chapter's existing Day-14 close (~245 words after Pass-2 review) stays as the back-frame anchor.**
- **Log-opener pattern:** A - formal-log opener as a `Pre-departure record` / `Selection file entry` from Anna's selection-decision file (~95 words); reproduces the in-universe artifact that produced the offer. Per-chapter generator: crew-log-style-entry skill, tone_bias = `formal_duty_log`. Sample header: *Pre-departure record, dated 2026-04-02. Yusupova, Mission Director-designate. RV Nansen, MERIDIAN-7.*

- **VERSION HISTORY (CO directive 2026-05-05):**
  - **v1** (chapter-drafter, pre-canon; PR #110) - first draft; 8,010 words; 50.6 min audio
  - **v2** (chapter-drafter, post-canon-PR-#113) - canon-aware redraft with Pattern A opener + Anchor-grounding; 8,216 words / 50.6 min
  - **v3** (prose-reviewer, post-craft-feedback-PR-#115) - surgical compression of technical Q&A; 7,256 words / 43.5 min
  - **v3 listen-test verdict:** "still too technical" - forced the software-as-gravity canon (`vol-2-software-as-gravity.md`)
  - **v4** (chapter-drafter, post-software-as-gravity-canon - IN PROGRESS) - full redraft leading with **trust + prior betrayal** rail; technical Q&A compressed to single representative beats with Anna's interior reading of Joel as dominant register. **Word count target: ~5,500-6,200; audiobook target: ~33-37 min.**

- **v4 redraft directives (per `vol-2-software-as-gravity.md` § 6):**
  - Compress all four technical Q&A exchanges (GC, lease, Byzantine ops, ops layer) to **single representative beats each** with Anna's interior reading of Joel as the dominant register. *He answered the question. He did not soften the answer. I made a note of how he had not softened it.* The technical content is *that he gave a correct, undefensive answer*, not *what the answer was*.
  - Foreground Anna's interior throughout the technical sections. Where v3 has Joel explain the fence, v4 has Anna register *that he answered without reaching for the printout, that his voice did not change between technical clauses, that he had not looked at his notes since minute six*. The architecture is gravity; **Anna's reading of Joel is the chapter**.
  - **R1-BLOCK admission stays verbatim.** That is the chapter's load-bearing trust event; the four sentences and the fifth are protected.
  - **Yes/yes recruitment exchange stays.** The chapter ends on the exchange Anna selected him on.
  - **Day-14 close stays at v3 length** (~245 words). The coda's job is to land present-tense weight, not to recapitulate.
  - Technical content collapses to ~30% of v3's load.
  - **Cut the forecast-register intrusion** in Joel's not-naming-the-Navy passage (per Pass-2 review). *I would learn months later / in a conversation I did not yet know was coming* violates `series-arc-sunfish-trajectory.md` § 8 and pre-spends Ch 7. Replace with one present-call-register sentence.
  - **Cut the consortium-ranking procedural aside** in the notebook-line passage (per Pass-2 review).
  - **Apply Anna's voice register spec rigorously** - compressed-deliberate; controlled emotional flashes; authority assumed not performed; no hedging.
- **Key character beats:**
  - **Anna:** has read the paper + the council Round 1 review + the Round 2 review; her questions are designed to surface whether Joel will tell the truth when it matters; structural inverse of what failed her with Stefan.
  - **Joel:** the admission. *I missed it. The original protocol assumed condition X that doesn't hold under sustained partition. Klett was right. I rewrote it.* No softening, no defense, no deflection.
  - **The structural beat:** the disclosure-without-compulsion that becomes the architecture's load-bearing trust property.
- **Length target:** ~9,000 words / ~60 minutes audiobook.
- **Verification gap:** the foundational one - does Joel tell Anna the truth about the council BLOCK before she selects him? He does; that is why she selects him. The rest of the book pays this off.
- **Drafting notes:** structurally early because it establishes the trust on which the entire mission rests. This is one of the two listen-test chapters (concept note §9). Two characters; sustained back-and-forth; technical content delivered through Anna's questions and Joel's answers. The chapter is the validation test for the captain-asks-engineer pattern as the audiobook-tempo solution. Joel's voice register is `joel-reyes-principal-architect.md`. Anna's is `dr-leader-mission-director.md`. Both sheets carry the founding-act-of-grace beat at full detail.

## Ch 3 - *Drake Passage and the Ice Edge* (Days 1-7)

- **Days / setting:** Days 1-7 transit south; Drake Passage; ice edge; surface operations.
- **Architectural claim:** *the relay layer operates correctly when the network is healthy* (baseline confirmation; the architecture's claim about partition only matters because the non-partition claim is held).
- **Frame ratio:** 80% mission-present / 20% flashback (Sabina's logistics background; Diego's polar-operations history surface through Anna's questions).
- **Log-opener pattern:** none - transit chapter; setup; the device would weigh the chapter down.
- **Key character beats:**
  - **Sabina:** logistics overview - what the consortium ports expect; the bid-disaster backstory surfaces briefly during a quiet exchange (her `vol-1/part-1-thesis-and-pain/ch01` Ch 1 victim register transposed to Vol 2's mature time-frame).
  - **Diego:** polar-operations exposition through Anna's questions; reader registers him as the senior technical specialist; *quietly essential* register installed.
  - **Hiroshi:** quiet at the data console; reader registers reliability without dramatization.
  - **Priya:** **CANON: Priya signature-discipline scene (per CO directive 2026-05-05 craft note).** During pre-submersion calibration, Priya **insists on a fourth pass when standard procedure is three.** She does not argue; she does not negotiate; she takes the additional pass. Her body holds the discipline: shoulders set, jaw tight, audibly counting through the cycle, clipped one-word acknowledgments to the ops officer. *The boat is one of the days that matter.* Anna registers; respects it; the chapter moves on. **This scene seeds Ch 13's three-pass discipline-as-architectural-property climax - the reader has already seen it operate when stakes were lower, so it doesn't read as expository when stakes rise.** Canonical Vol 2 first-introduction; do not skip.
  - **Joel:** first acoustic-only mesh test (under-ice rehearsal while still on surface); explains to Anna what's about to be different.
- **Length target:** ~4,500 words / ~30 minutes audiobook.
- **Verification gap:** the architecture's surface-operation behavior matches Joel's specification. Baseline established so that partition-mode behavior in Ch 4-5 is legible by contrast.
- **Drafting notes:** the chapter is structurally a setup chapter - but no longer just setup; the Priya signature-discipline scene gives it character-load. Resist climaxing it. Diego and Sabina need to enter as recognizable people; Hiroshi gets less treatment because his moment is later. The acoustic-mesh-rehearsal is the technical anchor; the Priya scene is the character anchor; the rest is character + the ship's transit register.

## Ch 4 - *First Submersion* (Day 7, Segment 1 begins)

- **Days / setting:** Day 7 dive; Segment 1 begins; ~14 days submerged ahead.
- **Architectural claim:** *the local store is operating in partition mode now; the relay layer is dormant; the gossip protocol can no longer reach the consortium ports.* The captain-asks-engineer pattern installed.
- **Frame ratio:** 70% mission-present / 30% flashback (Joel's pre-mission walk-throughs surface during the explanation; Anna's prior-mission interior briefly compares).
- **Log-opener pattern:** none - the dialogue-engine install is the chapter's structural lift; a log header would compete for that altitude.
- **Key character beats:**
  - **Anna:** first sustained interrogation of Joel about *what is different now.* The chapter is structured around her questions; her command authority is established by what she asks.
  - **Joel:** explains. The chapter installs the dialogue-engine that carries every architectural beat in the book. Walks Anna through the local-store-as-only-reality fact; the relay-layer's dormant state; the gossip protocol's inactivity.
  - **Priya:** quiet check on the schema state at submersion; *the migration we are not running today.* Foreshadow without foregrounding.
  - **Wanjiru:** the comm-node state at submersion; the audit-log design that preserves provenance under partition.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture transitions from healthy to partition-mode without any state corruption; the local store is uncorrupted; the gossip protocol has correctly identified itself as dormant rather than failing.
- **Drafting notes:** this is the chapter that installs the captain-asks-engineer engine as the book's primary exposition mechanism. Every later technical chapter inherits this pattern. The chapter's load is the dialogue itself; the ambient submarine procedure is texture, not subject.

## Ch 5 - *The Day-Twenty Realization* (Arc 1)

- **Days / setting:** Day 14 from departure / ~Day 7 of sustained under-ice operation; mid-Segment-1.
- **Architectural claim:** *the local store is authoritative under partition because there is nothing else.*
- **Frame ratio:** 100% mission-present. (Flashback would dilute the realization.)
- **Log-opener pattern:** C - formal-log opener (brief, ~50 words; Day-14 routine watch entry) + diary inset (the Long Now mother-thread paragraph as encrypted-personal-file artifact). The existing draft already approaches this; the redraft formalizes the convention.
- **Key character beats:**
  - **Anna:** queries the local store for a colleague's prior write - a piece of provenance from before the mission. The system answers locally without ambiguity, because it cannot do otherwise. The compounding recognition: *Everything I am recording right now is only here.* / *This is what Joel built.* The emotional landing: not triumph; recognition.
  - **No other character on-page substantively.** Joel may be elsewhere on the boat. The realization is interior; the architecture's authority is registered in solitude.
- **Length target:** ~6,000 words / ~40 minutes audiobook.
- **Verification gap:** the chapter is the verification gap. The architecture's authoritative-local-store claim from the paper is exercised against Anna's lived experience under partition for the first time. The claim holds.
- **Drafting notes:** **this is one of the two listen-test chapters (concept note §9).** The chapter's primary risk is overwriting the realization; trust the silence and the single-character interior. Tight scene; one location; emotional realization at the chapter's center. If Arc 1 listens well as audiobook, Anna's first-person mission-frame voice is validated. If it does not, the issue is identifiable to the narrator-voice choice itself.

## Ch 6 - *First Surface, First Forsaken Reveal* (Day 21-23)

- **Days / setting:** Day 21 surfacing; 2-day surface window; comms reconnect.
- **Architectural claim:** *the gossip layer rapidly reconciles with the consortium ports after partition; the audit log is intact; provenance is preserved.* Reconciliation under healthy network resumed.
- **Frame ratio:** 80% mission-present / 20% flashback (the Stefan-mission cut-short surfaces briefly when Anna registers his name in the news cycle).
- **Log-opener pattern:** A - formal-log opener noting surface time, mission state, and that sync-replication-to-Bridge has begun. Reader registers the surface-window as a structural moment.
- **Key character beats:**
  - **Anna:** first external contact after Segment 1; HELVETICA-2's preliminary results land via Wanjiru's relay logs; Stefan's name surfaces in the news cycle for the first time on the boat; the architecture-vs-platform contest enters Anna's consciousness.
  - **Wanjiru:** her relay logs catch the rival's PR cycle as it lands; her structural-political reading of the rival is more sophisticated than anyone else's on the boat. **Sync-mechanic install: she explains the prioritization to Anna in dialogue. *Forty-eight hours, thirty Mbps if we're lucky, two terabytes accumulated. We push the mission record first. The sensor archive carries forward.*** Reader installs the constraint that becomes a chapter-load mechanism in Ch 11 + Ch 14 + Ch 17. **CANON: Wanjiru signature-discipline scene (per CO directive 2026-05-05 craft note).** Mid-conversation with Anna, an exception request lands on Wanjiru's queue - Diego asking for an undocumented one-off key issuance so a polar-operations sensor-data-sharing arrangement can run before the formal key-issuance chain processes (rationale: saves twenty minutes; everyone knows everyone). **Wanjiru declines. Calmly. Without raising her voice. Without making Diego feel humiliated.** *The procedure exists for the case where you most want to skip it.* She names the rule; offers the documented path; the documented path takes the additional twenty minutes. Diego accepts without argument; the rule holds. The exchange takes thirty seconds. Anna registers; says nothing; the prioritization conversation resumes. **Her body shows equanimity throughout - the hum continues, the tempo unchanged.** Canonical Vol 2 first-introduction at full operational altitude; do not skip.
  - **Joel:** absent from this chapter's main scene by design - Anna registers the rival without yet processing it through Joel.
  - **Helvetia Trust SA + Stefan:** present in the news cycle; not yet dramatized in person. the Nansen's surface-window sensor sweep observes the rival mission's operations across the open channel; that observation goes into the Anchor archive (P1 priority); cross-check evidence accumulates.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the gossip protocol's reconciliation behavior matches Joel's specification. Provenance survives the round-trip.
- **Drafting notes:** the chapter installs the corporate-sponsor-vs-OSS axis as a present concern AND the sync-mechanic as an operational reality (`vol-2-anchor-bridge-sync-mechanic.md` § 7.1). Stefan and Helvetia are off-screen but legible. Anna's command authority is undisturbed by the rival's messaging; she registers it and continues. **The chapter ends with the boat re-submerging; some material Wanjiru would have liked to push (early observations of rival mission preliminary results) carries to Surface 2.** Plant the carryover.

---

# Act II - Subsystems hold; the contest sharpens

**Days 22-42.** Each subsystem the architecture claims gets exercised against operational reality through Anna-Joel dialogue or character-driven beats. The rival mission concludes with publicly-favorable results that the architecturally sophisticated will see were partially compromised. The Anna-Joel love arc becomes legible to Anna in the surface-window micro-exchanges; she does not act.

---

## Ch 7 - *Joel's Sunfish* (Arc 3)

- **Days / setting:** Day 22, Surface 1 quiet hours.
- **Architectural claim:** *the architecture's name carries the discipline that makes it work.* The naming reveal as architectural disclosure.
- **Frame ratio:** 50% mission-present / 50% flashback (Joel's USS Sunfish SSN-649 service surfaces in the conversation).
- **Log-opener pattern:** none - intimate two-character conversation; logs would interrupt the chapter's emotional altitude.
- **Key character beats:**
  - **Joel:** discloses the name's origin - USS Sunfish SSN-649, decommissioned 1998, his first submarine. *The discipline that runs through the architecture got formed there.*
  - **Anna:** recognizes what she had been registering since she read the paper. The submarine-discipline-as-architectural-substrate becomes legible.
  - **The Long Now beat:** the boat-that-no-longer-exists left something in Joel that is now in the architecture; the architecture will outlive Joel; the discipline travels.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's discipline (the procedural rigor that produces the maintainability) traces to a specific human history. Anna sees it.
- **Drafting notes:** intimate; conversational. Two characters; one location; sustained quiet. The chapter is the first beat of the Anna-Joel love arc that Anna explicitly registers - but only as architectural recognition of Joel, not romantic recognition. The romantic register is in the *quality* of her attention, not in dialogue. Joel's nuclear-Navy register in `joel-reyes-principal-architect.md` is the voice reference.

## Ch 8 - *Second Submersion* (Day 23)

- **Days / setting:** Day 23 dive; Segment 2 begins; ~14 days ahead.
- **Architectural claim:** *the architecture is operational on the routine cycle; the partition transition is no longer novel.*
- **Frame ratio:** 80% mission-present / 20% flashback (Sabina's prior use-case work surfaces during her validation pass).
- **Log-opener pattern:** none - routine-cycle chapter.
- **Key character beats:**
  - **Sabina:** first use-case validation pass - a logistics scenario the architecture has not actually run before; she walks Joel through the constraint; the architecture handles it; her bid-disaster history retroactively legible as why she insisted on this validation.
  - **Hiroshi:** steady at the data console; first substantive on-page beat; reader registers the depth behind the quiet.
  - **Diego:** attentive; supports Sabina's validation procedurally.
  - **Anna:** command discipline tightening into routine; the chapter shows what *normal* looks like in Segment 2.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** Sabina's use-case validates against the architecture's operational behavior. The architecture handles it correctly.
- **Drafting notes:** Sabina earns the chapter's center; she has been treated lightly through Acts I, and Act II is where she becomes a person. Hiroshi's beat is brief but load-bearing. The chapter is structural cycle-as-content; it should not feel slack.

## Ch 9 - *Subsystem Test - Sync Daemon Under Drift* (mid-Segment 2)

- **Days / setting:** ~Day 30; mid-Segment 2; routine cycle.
- **Architectural claim:** *the gossip protocol handles sustained network drift without manual intervention.*
- **Frame ratio:** 70% mission-present / 30% flashback (Joel's debugging walks back to specific design decisions that are now exercised live).
- **Log-opener pattern:** B - formal-log frame. Opens with mid-Segment-2 routine watch entry; closes with post-debug log B (Joel updates the operational record after the gossip-protocol drift has been characterized). The differential between log A and log B is what the chapter documents.
- **Key character beats:**
  - **Joel:** debugs the sync daemon in real time; the chapter is Joel's running architectural commentary on what's actually happening. The dialogue-engine working at non-climactic intensity. Reader sees the architecture's specifications operating against operational drift. **The chapter also exercises Anchor's behavior under sustained partition** - local LLM transcribes, indexes, anomaly-detects; what continues working without Bridge contact is itself part of the chapter's exposition.
  - **Anna:** asks the questions that surface the architectural detail. Her questions are the reader's questions. Captain-asks-engineer at routine tempo.
  - **Priya:** present in the background; her schema-migration discipline foreshadowed without spending.
- **Length target:** ~6,000 words / ~40 minutes audiobook.
- **Verification gap:** the gossip protocol's drift-handling specification holds against actual mid-mission drift. The protocol does not require human intervention; the architecture's autonomy claim is exercised on a non-climactic problem and confirmed.
- **Drafting notes:** the chapter is the dialogue-engine pattern at its most exposed. The chapter has to be technically dense without sacrificing audiobook tempo - the test is whether Joel's architectural commentary, mediated by Anna's questions, can carry the technical load in listenable prose. If it can on this chapter, it can on Ch 13 (Priya) and Ch 15 (Wanjiru). Reference: Sunfish package surface (concept-note §2 vouches for accuracy; do not invent APIs).

## Ch 10 - *The Aftermath of a Mission That Once Was* (Arc 7 - substantial fragment)

- **Days / setting:** ~Day 33; Segment 2 quiet night; Anna's interior surfacing during a routine watch.
- **Architectural claim:** *trust hardens in specific shapes; the inverse of betrayal is disclosure-without-compulsion.* The chapter retroactively legibilizes Anna's selection criteria for Joel + Priya + Wanjiru.
- **Frame ratio:** 30% mission-present / 70% flashback (the Stefan-mission cut-short; the colleague's mix of acknowledgment and minimization; the five years between then and now).
- **Log-opener pattern:** none - Anna's interior at length; the chapter's emotional altitude is internal-restrained-not-procedural; logs would dilute.
- **Key character beats:**
  - **Anna:** prior-failure interior - the Stefan-mission cut short on operational grounds because the schema-migration limitation Stefan had not disclosed manifested under partition; the technical staff died (or were medevaced - exact prior-mission casualty terms TBD per concept-note §10.1); the trust-hardening; the inverse-of-betrayal recognition.
  - **No other character substantively on-page** - the chapter is Anna's first-person interior at length.
  - **Joel:** mentioned only in the recognition that what Anna selected him for is the structural inverse of what failed her last time. *He told me the truth about the BLOCK before I asked him. Stefan never told me.*
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architectural property of trust (disclosure-without-compulsion) is the inverse of the architectural property of failure (non-disclosure-under-pressure). Anna's selection of Joel was made on a structural property of his character that exactly inverses what failed her last time.
- **Drafting notes:** the chapter is mostly flashback; the mission-frame anchor is light. Does not dramatize Stefan in person (he is fully dramatized in Book 4); the Stefan figure is Anna's interior. Refer `stefan-reinhardt-rival-architect.md` for Stefan's dimension; the chapter does not require all of him to land - only Anna's reading of him is required. The chapter is the load-bearing prior-failure interior for Book 1; subsequent Arc 7 fragments distribute lightly across other chapters.

## Ch 11 - *Second Surface, Second Forsaken Reveal* (Day 37-39)

- **Days / setting:** Day 37 surfacing; 2-day surface window.
- **Architectural claim:** *the architecture is intact across two surface-window cycles; the audit log compounds correctly.*
- **Frame ratio:** 75% mission-present / 25% flashback (Anna's recognition of the love-arc beat retrospectively legibilizes the surface-window micro-exchanges).
- **Log-opener pattern:** A - formal-log opener noting Surface 2 commencement, sync-prioritization summary, and the rival mission's just-concluded status. The chapter is partly a clock - the log establishes its tick.
- **Key character beats:**
  - **Wanjiru:** **the chapter's chapter-load beat is sync-triage as institutional decision-making.** Stefan's mission has concluded; his PR cycle is fresh; she has 48 hours and a bounded pipe to push enough cross-check evidence (the Nansen's Surface-1-period observations of his mission, plus continued tracking) to the Bridge before the boat dives again. The race is real; the choices are political; she is not just at a console - she is choosing what becomes record. *The Stefan-cross-check race* is this chapter's structural event.
  - **Anna:** registers the love-arc beat - Joel's behavior in the surface-window's micro-exchanges has become legible to her in retrospect; she does not act. Per concept-note §6.4, the love arc is *secondary register*; not foregrounded.
  - **Joel:** behaviors continue; his discipline holds; he does not register that Anna has registered.
  - **Stefan + Helvetia + Astrid:** continued off-screen presence in the news cycle; the rival mission's *publicly favorable* results are dissected by Wanjiru in conversation with Anna **using the Nansen's archive as the cross-check evidence - the forensic substrate at first deployment**. TrustMesh's selectively-retained reports cannot disagree with the Nansen's full pre-failure timestream of its own mission, but the Nansen's *observations* of TrustMesh during open channel-overlap windows can. Wanjiru notices the divergence between Stefan's PR claims and what the Nansen's sensor sweep observed.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's two-cycle persistence; the gossip protocol holds across two reconciliations; provenance survives compounding round-trips. **The forensic-substrate property is exercised for the first time** - the Nansen's archive supplies cross-check evidence the rival's architecture cannot.
- **Drafting notes:** the chapter advances the corporate-sponsor-vs-OSS axis; Wanjiru is the reading-engine for the political dimension as Joel is for the architectural dimension. Anna's love-arc registration is *a quality of her attention,* not a beat of dialogue or action - written in the texture of how she sees Joel, not in narrative motion. **The sync-mechanic + forensic-substrate threads converge here**; the chapter is where Wanjiru's institutional weight begins forming on the page. See `vol-2-anchor-bridge-sync-mechanic.md` § 4.2 for her triage role.

## Ch 12 - *Beginning of the End - Segment 3 Dive* (Day 39)

- **Days / setting:** Day 39 dive; Segment 3 begins; ~10 days ahead - the climax segment.
- **Architectural claim:** *the architecture's discipline is the precondition for the climax* - the chapter foreshadows without pre-spending.
- **Frame ratio:** 80% mission-present / 20% flashback (Joel's last-leg-of-deployment register from his Navy days surfaces briefly).
- **Log-opener pattern:** A - formal-log opener at dive commencement: *Segment 3 dive at 0612 local. Last under-ice deployment. Final scheduled surface at Punta Arenas Day 56.* Plants the conditional-preservation stake explicitly: there is no Surface 3.
- **Key character beats:**
  - **Anna:** bridge command discipline tightens; the last-leg discipline of submarines becomes legible. **One-sentence narration register beat: *And now everything we record for the next ten days is on the boat alone until we surface in Punta Arenas.*** Plants the conditional-preservation stake before the climax.
  - **Joel:** quietly grounded; nuclear-Navy register becomes more pronounced under operational pressure.
  - **Priya:** schema state checked; the three-pass migration discipline is implicit in everything she does in this chapter; foreshadow without spending.
  - **Diego:** tempo accelerates; he is more visible; reader's anticipation primed.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's pre-climax state is intact; nothing is broken on entering Segment 3. Sets the contrast for what changes during the cascade.
- **Drafting notes:** structurally a setup chapter; the chapter's job is to install enough operational tension that the cascade in Ch 14 does not feel arbitrary. Discipline is the subject; not just discipline as theme but discipline as everyone's behavior visible on the page. **The conditional-preservation plant is load-bearing for Ch 14's emotional weight.**

---

# Act III - Cascade, ascent, and the cumulative reveal

**Days 43-56.** The two architectural climax chapters (Priya's schema migration; the leak-and-fire cascade) land back-to-back; the security architecture climax (Wanjiru's compromised-relay-holds) lands during the cascade. The mission concludes; the boat surfaces at Punta Arenas; the cumulative Forsaken reveal lands as Anna writes the staff history that produces Vol 1.

---

## Ch 13 - *The Schema That Should Not Migrate* (Arc 4)

- **Days / setting:** ~Day 43-44; mid-Segment 3.
- **Architectural claim:** *schema migration is Healing - preserving identity through transformation.* The Healing/Saidar discipline is exercised on the architecture's hardest schema-evolution case under operational duress.
- **Frame ratio:** 80% mission-present / 20% flashback (Priya's lab-review pre-mission position surfaces; the *I would have refused this in lab review* moment grounded in her prior pattern).
- **Log-opener pattern:** B - formal-log frame. Opens with pre-migration log A (Priya's *I have refused this on operational grounds and will now describe how to do it anyway* documentation register); closes with post-migration log B recording success + safety-net catches. The two logs differ in tone - log B knows what log A didn't. **Local LLM helps Priya and Joel map old fields to new during the migration** - the operator-led work, LLM-accelerated, never LLM-autonomous. (See `vol-2-archive-and-capture-convention.md` § 4.2 for the LLM's role.)
- **Key character beats:**
  - **Priya:** says no, then says how-to-do-it-anyway, then walks Joel through the migration in real time. Two near-failures during the read-confirmation cycle that Priya's three-pass discipline catches. The migration succeeds.
  - **Joel:** executes the migration under Priya's direction; the architectural protocol's schema-migration safety properties hold.
  - **Anna:** asks Priya to authorize on operational grounds; respects the *no* before respecting the *yes-with-conditions*; her command authority is the precondition for Priya's safety net.
  - **The post-migration recognition:** the architecture worked because Priya's caution was built into it as a constraint, not because the mission followed her caution as a rule. (Concept note §7 Arc 4 - load-bearing.)
- **Length target:** ~10,000 words / ~67 minutes audiobook.
- **Verification gap:** the schema-migration protocol holds under conditions Joel's paper specifies it should hold under, with three-pass confirmation that the paper specifies as the safety property. The verification is procedural, not numerical; the chapter is the verification gap.
- **Drafting notes:** technical density is high; the chapter earns the length. Captain-asks-engineer pattern is now Anna-asks-Priya / Anna-asks-Joel parallelized; Priya gets her own voice register from `priya-iyer-schema-migration.md`. The Nynaeve-says-no-until-forced register is the voice reference. Saidar (policy/healing) layer in operational form. **Chapter pairs with Ch 14:** the boat is in cascade by the end of this chapter or just after; Ch 13 ends with the migration just stable + the leak alarm just firing, or in close sequence.

## Ch 14 - *The Crossing* (Arc 6)

- **Days / setting:** Day 47 (placeholder; consistent with prior `vol-1/closing/the-crossing.md` Day 47 0317 leak alarm); Segment 3 climax.
- **Architectural claim:** *the architecture is adequate, not heroic; the procedure is the heroic act.* The architectural protocol's behavior under environmental cascade is measured against the procedural discipline Diego, Joel, and Anna bring to the cascade itself.
- **Frame ratio:** 95% mission-present / 5% flashback (Joel's nuclear-Navy training surfaces in the texture of his action, not as flashback scene; Anna's love-arc recognition compounds privately but the chapter does not flash back).
- **Log-opener pattern:** C - formal damage report at chapter open (procedural; clean) + Anna's diary inset at chapter close (encrypted personal-file artifact with the eleven-minutes-behind-the-glass beat as private record). The differential between the two registers is the chapter's load. **The damage report includes the closing hash signature** - second instance after Ch 1; the artifact's authoritativeness is what the chapter's institutional case turns on.
- **Key character beats:**
  - **The leak:** **originates from one of the new sensor heads - an off-the-shelf vendor-supplied unit that the consortium integrated because OSS budget did not allow custom-firmware development.** Instrument-malfunction at the moment (per CO direction 2026-05-05); small leak, high stakes, in a confined access compartment behind equipment. 0317 leak alarm (initially flagged by Anchor's anomaly detection on the sensor-head's pre-failure acoustic signature shift, ~30 seconds before threshold-trip); 0319 cabin-to-bridge transit; 0321 assessment; 0342 compartment isolation order. **Cause-of-failure is logged as instrument-malfunction (under investigation).** No accusation; no public framing. The forensic question is held for Wanjiru and Joel to pursue across Ch 15 + Ch 17.
  - **The compute hub:** **collateral damage.** The same compartment held the boat's central workstation (RTX-class GPU; heavy-LLM hosting; full-archive RAG index). Coolant ingress + smoke + the post-isolation residual environment combine to put the hub offline for the rest of the mission. Capability degradation begins immediately; chapter's operational damage report records it; subsequent chapters register the loss in *what the crew does and doesn't do* (see `vol-2-archive-and-capture-convention.md` § 6).
  - **Diego:** polar-operational experience landing as procedural competence; the chapter's central act-of-competence beat. Diego survives and retires to San Martín de los Andes earned through what he did. (Cast-swap from earlier draft: Diego survives, replacing the death-scene of the original closing chapter - see locked-elements doc.) **Diego is also the operator most familiar with sensor-head telemetry under polar conditions; in retrospect across Ch 15-17, his pre-failure observations of the sensor head will be among the forensic evidence.**
  - **Joel:** **the protective beat (CO direction; refined 2026-05-05).** The alarm fires; his instinct from thirty years of nuclear-Navy training fires before any cognitive part of his mind has caught up. He moves toward the leak. He pushes Anna aside on his way past her. He shuts the bulkhead door behind himself and locks it from his side. Then he turns and faces Anna through the porthole window of the bulkhead door. The look says, without a word, everything that his discipline has prevented him from saying since the recruitment interview. Anna receives it. Her command authority holds; the bridge is watching her. He turns and goes to work. Eleven minutes; he contains the instrument failure, drains the residual water, reports clear, emerges. (Source: `joel-reyes-principal-architect.md` love-arc layer; concept note §7 Arc 6.)
  - **Anna:** unsentimental command authority through the eleven minutes; the bridge is watching her; her face does not change. The recognition compounds privately for the rest of Book 1. **Anna's diary inset at chapter close** records what is not in the operational damage report - the touch in the passageway, the locked door, the look through the glass. The compartment cameras captured the moment (consent-gated; signed-at-capture; in the archive); Anna's diary acknowledges it: *I could play it back; I am not going to.* Her choice not to revisit the moment is the diary's moral content.
  - **Priya, Sabina, Hiroshi, Maria:** procedural roles during the cascade; everyone executes; the boat is a procedure not a hero.
  - **Wanjiru:** her chapter is Ch 15; she is on the comm node here, working the audit log + the gossip layer through the cascade. **The Anchor archive captures everything - sensor-head pre-failure timestream, compartment-camera video, voice logs, command-and-response between control plane and the failed instrument - all hash-chained, signed at capture, replicated across crew nodes. The forensic substrate is intact. Wanjiru notes this; pursues across Ch 15.**
- **Length target:** ~12,000-13,000 words / ~80-87 minutes audiobook. **The longest chapter in Book 1.**
- **Verification gap:** the architectural protocol behaves as specified through the cascade; the protocol's environmental-stress claim from Joel's paper is exercised against literal physical environmental stress and holds. The eleven minutes Joel is behind the door are the chapter's emotional center. **The architecture's preservation property is itself at stake - if a different fault had finished what the leak began, none of the post-Surface-2 record would have reached the Bridge. The boat surviving is what makes the architecture's promise survive.**
- **Drafting notes:** **the climax.** Inherits beats from `vol-1/closing/the-crossing.md` (Vol 1's existing closing chapter, 4,396 words) but expands ~3× through the instrument-leak protective sequence + Diego's competence at full altitude + Anna's command-watch silence + the Spanish-letter-to-María-Elena beat (recovery, not death notification, since Diego survives in the new version). The Spanish letter scene per concept-note §7 Arc 6. Vol 1's existing chapter requires a separate revision pass to align with the multi-segment design; that revision pass is gated on CO authorization (concept-note §10.2). For Vol 2 Ch 14 drafting, work from the concept note + character sheets + the new convention docs, not from the existing Vol 1 chapter - the existing chapter is the *seed* for this chapter, but the prose register is mature-Anna-narration not Vol-1-staff-history-fragment. **Three layers of archive operate simultaneously in the chapter: the formal operational damage report (public), the compartment-camera and sensor-head capture (preserved but not surfaced), Anna's diary (encrypted, private). The chapter trades among the three; the differential is the chapter's load.**

## Ch 15 - *The Compromised Relay Holds* (Arc 5)

- **Days / setting:** Day 47-48; during and immediately after the leak-and-fire cascade.
- **Architectural claim:** *security architecture designed for political fragility holds against environmental degradation; the worst case in the political dimension shares its shape with the worst case in the physical dimension.* **Extended in this chapter: the same structural-similarity recognition extends to capability architecture under hardware loss - graceful degradation IS the same shape.**
- **Frame ratio:** 75% mission-present / 25% flashback (Wanjiru's M-PESA-adjacent design history surfaces in the moment she recognizes the structural similarity).
- **Log-opener pattern:** A - formal-log opener at chapter start; Wanjiru's register; documents the transition into degraded-capability operation.
- **Key character beats:**
  - **Wanjiru:** comm-node damage threatens the gossip layer that propagates revocations; sensor compartment loss threatens the audit trail; **the compute hub is offline; heavy-RAG and full-archive queries unavailable; she works the architecture through the degraded mode in real time.** The post-cascade retrospective recognition is now THREE-fold: *the security model that defended against political coercion turned out to defend against environmental degradation AND against compute-hub loss. Three threat models, same structural shape, same architectural defense.* **She also begins forensic queries against the sensor head's pre-failure timestream BEFORE deeper degradation makes broad analysis slow** - narrow targeted queries on laptop-class compute. She notes the sensor head's firmware-update history *as a piece of metadata that doesn't quite add up*; doesn't pursue further this chapter; logs the question; carries to Ch 17.
  - **Joel:** present; participates in the recognition but the chapter is Wanjiru's; her register from `wanjiru-kamau-security-policy.md` is the lead voice. Joel notes the forensic finding; defers the deeper analysis to transit-north.
  - **Anna:** witness; the chapter compounds the architecture's case for her as the maiden voyage's chief beneficiary. Her narration begins to register the reduced-capability state through *what the crew does and doesn't do*.
- **Length target:** ~8,500 words / ~57 minutes audiobook.
- **Verification gap:** the security architecture's revocation-under-coercion specification is exercised against environmental degradation AND against compute-hub loss. **Three threat models, same structural defense.** The verification is the structural-similarity recognition, which is what makes Wanjiru the eventual standards-body chair.
- **Drafting notes:** chapter pairs immediately with Ch 14 in time (during + after the cascade); Wanjiru is the lead voice. Saidin (Joel's protocol layer) and Saidar (Wanjiru's policy layer) operating against the same physical event from different architectural angles - the chapter is the second of the two-discipline reveals (Ch 13 was Saidar; Ch 14 was Saidin under stress; Ch 15 is Saidar under stress). The Egwene/Wanjiru voice register is the one she will carry into Book 5's standards-body chair beat. **The forensic-substrate beat lands here for the first time in operationally substantive form** - the architecture being its own investigative tool.

## Ch 16 - *Final Ascent* (Days 49-52)

- **Days / setting:** Day 49-52; Segment 3 ends; the boat surfaces at Punta Arenas approach.
- **Architectural claim:** *the architecture is proven across the maiden voyage's full operational envelope - including under capability degradation.*
- **Frame ratio:** 70% mission-present / 30% flashback (Joel's mid-50s reflection on what the architecture has now demonstrated; Anna's reflection on what the mission has cost - Diego's retirement; the compute hub; nothing else lost).
- **Log-opener pattern:** A - formal-log opener at surfacing; brief; routine register. The chapter is denouement.
- **Key character beats:**
  - **Anna:** command discipline easing; the mission's stakes have settled; the regulatory landscape ahead is the new tension. **Narration register: the crew is operating in degraded mode for ten days now; routine has settled; *some questions we asked the system; some questions we wrote down to ask later.* Anna's accumulated paper-list of *queries to run when we surface* grows. Her register registers the architecture's reduced state without mourning it.**
  - **Joel:** quietly satisfied; the architecture has performed; he does not yet know what Stefan has done in his absence.
  - **Wanjiru:** preparatory work for the Punta Arenas reveal; her relay is reading the inbound regulatory traffic. **Limited surface bandwidth on Drake-Passage transit allows targeted record sync; the operational damage report and Diego's recovery documentation get prioritized to consortium ports.**
  - **Diego:** quietly grounded; he does not yet announce his retirement decision.
  - **Priya, Sabina, Hiroshi, Maria:** the routine cycle of a successful mission's last days.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture has held end-to-end. The chapter is the verification's end state.
- **Drafting notes:** structurally a denouement chapter for Acts I-III's mission-architecture spine; the chapter's emotional payoff is restraint, not triumph. The Punta Arenas reveal in Ch 18 is the contrast. **Anna's accumulated query list is a quiet structural device - visible in her narration; the items get answered after docking in Ch 18.**

## Ch 17 - *Transit North* (Days 52-56)

- **Days / setting:** Day 52-56; surface transit Drake Passage → Punta Arenas.
- **Architectural claim:** *the staff history is a load-bearing artifact; the act of writing it makes the architecture transmissible.* **Concurrent claim: the architecture is its own forensic substrate.**
- **Frame ratio:** 80% mission-present / 20% flashback (Wanjiru's earlier conversation with Anna about staff-history convention surfaces).
- **Log-opener pattern:** B - formal-log frame. Opens with the degraded-mode operational record (chapter starts mid-transit, capability still reduced); closes with Wanjiru's draft of the regulatory filing for the consortium (the chapter's institutional product). The frame's two logs differ in tone - the open is post-incident routine; the close is institutional-trajectory-forming.
- **Key character beats:**
  - **Wanjiru:** asks Anna to write the mission account. The staff-history is a load-bearing institutional convention; this is the device that produces Vol 1 (Joel's paper) and Vol 2 (Anna's narration). **Wanjiru also pursues the forensic-finding work begun in Ch 15 - alongside Joel, on laptop-class compute, slowly and deliberately. They establish: the sensor head's firmware-update history shows an unusual pattern; the patch came through a vendor whose ownership/co-development partnership traces toward Helvetia Trust SA; the post-patch behavior includes a low-frequency anomaly that the boat's anomaly detection didn't flag because it was within nominal range. Inconclusive. Could be benign coincidence; could be deliberately subtle compromise. Wanjiru drafts the regulatory filing for the consortium with this finding present but unresolved.**
  - **Joel:** **the chapter's structural anchor is the conversation between Joel and Wanjiru.** The progression they walk through:
    - The sensor head's firmware-update history
    - The vendor's recent ownership / partnership history
    - Helvetia Trust SA's co-development investments
    - The pattern of vendors that take Helvetia investment ending up with subtle firmware behaviors
    - Inconclusive but suggestive
    
    **Joel's beat is honest engineering.** *We couldn't afford to fork the firmware. We integrated their patch because their patch was what was available. The architecture's job is what it is doing right now - surfacing the analysis that is possible because we held the full pre-failure timestream. We could not have prevented this compromise. We can document it. That is enough for now.*
    
    **Wanjiru's beat is institutional.** *The consortium will need a standards body. Vendor-attestation requirements. Firmware-transparency rules. Supply-chain audit requirements that small OSS projects can comply with at scale. None of that exists. It will need to.* This is the moment her later standards-body chairmanship is *seeded* on the page.
  - **Anna:** accepts the assignment to write the staff history; the chapter shows her beginning the work that the reader has been receiving since Ch 1 of Vol 2 (and that produced Vol 1 in the H.G. Wells convention). **She also registers the OSS-funding-asymmetry as an architectural-philosophical insight without preaching it: the consortium couldn't afford to vertically integrate; off-the-shelf was the only choice; the architecture's response is to *catch* the compromise via the forensic substrate, not prevent it via supply-chain control.**
  - **Diego:** the Spanish letter to María Elena written and prepared for posting at Punta Arenas; recovery-not-death-notification register; per concept-note §7 Arc 6.
  - **Priya, Sabina, Hiroshi, Maria:** transit-cycle texture.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's transmissibility - that what Joel built can be communicated to readers who were not on the boat - is exercised in Anna's first sustained writing pass. The verification is meta-textual; the reader is reading the artifact. **AND: the architecture's forensic-substrate property is exercised at chapter-load weight; the Nansen's full pre-failure timestream of every edge device is what makes the supply-chain-pattern analysis possible. TrustMesh missions cannot do this.**
- **Drafting notes:** the chapter is the H.G. Wells convention surfaced. Anna writes; the reader reads what she wrote. The chapter's primary pleasure is recognition: *this is what we have been listening to.* Restraint required; do not over-foreground the device. **The Joel-Wanjiru forensic conversation is the chapter's structural anchor; the staff-history-conversation between Anna and Wanjiru is the parallel emotional anchor; both threads converge on the institutional-mission-seeding beat.** The chapter is also where the OSS-funding-asymmetry as the architecture's known weakness is surfaced operationally. **Stefan/Helvetia are not accused; the filing is institutional and procedural; the question remains hung over Books 2-3.**

## Ch 18 - *Punta Arenas Surfacing* (Arc 8)

- **Days / setting:** Day 56, 04:41 local, Punta Arenas dock; final surfacing.
- **Architectural claim:** *the maiden voyage proved the architecture; the contest over its meaning has only begun.* **The architecture's preservation promise is fulfilled at docking; capability is restored; both threads converge.**
- **Frame ratio:** 60% mission-present / 40% reveal (the boat is moored; first external contact; the cumulative reveal lands).
- **Log-opener pattern:** C - formal final-mission log at chapter open + Anna's diary closing the book at chapter close. The diary closes the staff history's authorship arc: the book the reader is finishing is the artifact being authored on-page.
- **Key character beats:**
  - **Anna:** receives the first external contact; the Punta Arenas dockside team has HELVETICA-2's PR cycle, the Working Group regulatory filing draft (per `forsaken-position-papers/03-regulatory-filing.md` - though that filing dates February 2027 in the locked artifact, the *preliminary response* lands here per concept-note §3.6 / §7 Arc 8); Wanjiru's standards-body has issued a preliminary response; the architectural contest enters its public phase. **Anna's accumulated query list from Ch 16 gets answered in the first hours after docking - the Bridge restores full capability; the heavy-RAG, full-archive queries, multimodal-tagging that the post-leak laptop-class fallback could not provide all come back online.**
  - **Wanjiru:** reads the regulatory landscape with full bandwidth restored; her Annex A minority opinion (per `oss-architects-voices/01-annex-a-minority-opinion.md`) is foreshadowed as the document she will write. **Her transit-north regulatory filing reaches the consortium; the sensor-head supply-chain pattern is documented; the institutional mission begins; she is already drafting in her head the standards-body framework that will be her career.** The cross-check work between Stefan's PR and the Nansen's full archive runs at full speed for the first time post-mission - the bulk catches up; Wanjiru can finally cross-check Stefan's report against the *full* the Nansen archive (Surface 1 + Surface 2 + final-sync's bulk catch-up).
  - **Joel:** quietly absorbs that Stefan has been busy; the public framing of his architecture is now contested; the work ahead is contestation, not building.
  - **Priya, Diego, Sabina, Hiroshi, Maria:** disembarkation; Diego's retirement to San Martín de los Andes announced.
  - **The cumulative Forsaken reveal:** while the boat was under, the first formal regulatory challenge to local-first architecture was filed; Stefan's mission concluded with publicly-favorable results that the architecturally sophisticated will see were partially compromised (per Wanjiru's filing, with forensic evidence); Wanjiru's standards body has issued a preliminary response. The mission's success and the world's response converge. **The architectural-political contest enters its full-data phase - the Nansen holds the only durable record of what actually happened on both boats during their parallel operations.**
  - **CANON: the unavoidable Stefan exchange (per CO directive 2026-05-05 craft note).** The consortium reception requires both architects to attend the joint mission debrief. Stefan was at Punta Arenas earlier for his own mission's conclusion; institutional convention has him present for the reception. **Anna and Stefan exchange thirty seconds of formal courtesy in front of consortium witnesses.** Nothing dramatic. The exchange is professional, polite, dry. Stefan offers the institutional version of congratulations on the mission's successful conclusion; Anna offers the institutional version of acknowledgment. **What Anna registers is what is NOT said - there is no apology and there is no offer of one.** Five years between the prior failure and now; a thirty-second formal exchange to span the distance. The reader registers the same gap. Anna does not narrate at length about it; she records the exchange in the staff history without flourish; the chapter moves on. **This is the only current-day Anna-Stefan moment in Vol 2; everything else is remembered Bremerhaven scenes (Ch 10 interior + light reference in Ch 2) or institutional press-quote register through Wanjiru's reading of the rival's PR cycle (Ch 6, Ch 11). The brevity preserves Stefan's ambiguity and protects the Book 4 dramatization runway.**
  - **Convergence at docking:** *capability* and *preservation* both come back online simultaneously. The Bridge fills; Anna's queries get answered; the architecture's long-now promise is completed. Day 56 is the political ending AND the architectural ending.
  - **Anna writes the staff history** - closing image; the device that produced the book. **She is writing the founding document of what becomes a centuries-long literary tradition - but she does not know that. The reader, having the cosmology, registers the weight retroactively.** (See `series-arc-sunfish-trajectory.md` § 5.3 for the discipline rule on Anna's authorship register.)
- **Length target:** ~7,000 words / ~47 minutes audiobook.
- **Verification gap:** the architectural maiden voyage's meaning is contested in the world. The mission's verification is private; the contest is public. The book ends with the architecture proven and the real contest beginning. **AND: the architecture's full preservation + capability promise is fulfilled at docking; the book the reader is finishing is the artifact being authored on-page; the reader experiences the meta-textual completion.**
- **Drafting notes:** **the closing chapter.** Set up the rest of the series: Book 2's regulatory war (Wanjiru-led; per concept-note §3.6); Book 3's love-arc disclosure (Anna and Joel; per concept-note §6.4); Book 4's Stefan dramatization. The chapter has to land Book 1's emotional payoff (the architecture proved; Diego survived; Anna's command authority confirmed; Joel's discipline confirmed; the supply-chain pattern documented; the regulatory filing made; the institutional trajectory begun) without short-circuiting Book 2's escalation. The closing image is Anna at her desk beginning to write - except, in this chapter's frame, she has been writing the whole time, and now Wanjiru is asking for the staff history; Anna agrees. Restraint is the register; the contest is foregrounded but the response to the contest is reserved for Book 2.

---

## Length and audiobook reconciliation

| Chapter | Words (target) | Audiobook minutes |
|---|---:|---:|
| Ch 1 - Departure | 4,500 | 30 |
| Ch 2 - The Recruitment Interview | 9,000 | 60 |
| Ch 3 - Drake Passage and the Ice Edge | 4,500 | 30 |
| Ch 4 - First Submersion | 5,000 | 33 |
| Ch 5 - The Day-Twenty Realization | 6,000 | 40 |
| Ch 6 - First Surface, First Forsaken Reveal | 5,000 | 33 |
| Ch 7 - Joel's Sunfish | 5,000 | 33 |
| Ch 8 - Second Submersion | 5,000 | 33 |
| Ch 9 - Subsystem Test - Sync Daemon Under Drift | 6,000 | 40 |
| Ch 10 - The Aftermath of a Mission That Once Was | 5,000 | 33 |
| Ch 11 - Second Surface, Second Forsaken Reveal | 5,000 | 33 |
| Ch 12 - Beginning of the End | 5,000 | 33 |
| Ch 13 - The Schema That Should Not Migrate | 10,000 | 67 |
| Ch 14 - The Crossing | 12,500 | 83 |
| Ch 15 - The Compromised Relay Holds | 8,500 | 57 |
| Ch 16 - Final Ascent | 5,000 | 33 |
| Ch 17 - Transit North | 5,000 | 33 |
| Ch 18 - Punta Arenas Surfacing | 7,000 | 47 |
| **Total** | **~113,000** | **~750 minutes / ~12.5 hours** |

**Reconciliation note:** the row-by-row sum (~113,000 words, ~12.5 hours) overshoots the concept-note target of ~80,000-100,000 words / ~9-10 hours by ~15-20%. This is the standard outline-overshoot pattern; the actual draft will compress through:

- Per-chapter pruning of low-load passages during prose-review (the same Phase 4 quality-driven pass that operated on Vol 1)
- Real-paragraph-level word counts often landing 5-10% under chapter target after voice-pass discipline removes scaffolding
- Chapters that combine in drafting (e.g., Ch 6 + Ch 7 if the surface window's Joel-Anna conversation organically flows from the Forsaken reveal scene; Ch 16 + Ch 17 if the transit-north narrative cohesion holds across the staff-history-conversation beat)

If post-listen-test verdict is positive and the full Book 1 draft begins, expect the actual word count to land at ~95,000-105,000 words / ~10.5-11.5 hours audiobook - comfortably within the trade-novel range and within audiobook listenability tolerances per concept note §8.

If chapters do not compress as expected during drafting, the structural lever is splitting Ch 14 into two chapters (the cascade itself + the eleven-minutes-behind-the-door + immediate aftermath as a separate chapter), bringing the total to 19; or holding at 18 chapters and accepting ~110,000 words / ~12 hours audiobook.

---

## Drafting sequence (per concept note §11 production sequence)

1. **Listen-test pair first:** Ch 5 (*The Day-Twenty Realization*) + Ch 2 (*The Recruitment Interview*). Render through Kokoro. CO listens uninterrupted. Verdict drives full-Book-1 commit-or-revise.
2. **If both land:** draft Acts I-III in sequence per outline. Estimated 60-90 days at sustainable Yeoman + PAO + technical-book-writer-agent tempo.
3. **If one lands, one does not:** revise the failed chapter's structural choice; re-test.
4. **If neither lands:** back to concept-note revision; the format needs structural rework before further drafting.

The two listen-test chapters are deliberately the highest-difficulty chapters for the format choice:
- Ch 5 is the *first-person mission-frame* test - single character, single location, interior recognition; the format's hardest case.
- Ch 2 is the *captain-asks-engineer dialogue engine* test - sustained technical dialogue at audiobook tempo; the format's hardest case for technical exposition.

If both listen well, every other chapter is between these two extremes. If either fails, the failure is identifiable to a specific structural choice rather than to general format weakness.

---

## Cross-references for drafters

Drafting any chapter requires reading at least these artifacts in addition to the entry above:

- **All chapters:** concept note §1-§7 + Anna sheet + (relevant chapter character) sheet
- **Ch 2:** Joel sheet at full depth; council Round 1 + Round 2 review documents (`source/kleppmann_council_review.md`, `source/kleppmann_council_review2.md`); the BLOCK-then-rewrite is canonical there
- **Ch 5:** concept note §3.4 (Long Now thread) + §6.3 (Day-20 partition realization scene as Book 1 structural requirement)
- **Ch 7:** Joel sheet's USS Sunfish SSN-649 / nuclear-Navy register at full depth
- **Ch 13:** Priya sheet + Joel sheet's schema-migration co-author register; concept note §3.2 (Saidar discipline)
- **Ch 14:** Joel sheet's leak-event protective beat at full depth (`joel-reyes-principal-architect.md` love-arc layer); Anna sheet's love-arc layer; concept note §7 Arc 6 (refined 2026-05-05); existing `vol-1/closing/the-crossing.md` as seed
- **Ch 15:** Wanjiru sheet at full depth; concept note §3.2 (Saidar discipline + structural-similarity argument)
- **Ch 18:** all three voice exemplar libraries (`forsaken-position-papers/`, `oss-architects-voices/`); concept note §3.6 (8-book series map) for what's being seeded for Book 2

---

## Status

- **2026-05-04:** outline drafted; all 18 chapters at `icm/outline`; pipeline plumbing staged in `build/audiobook.py`.
- **CO-gated:** Ch 5 + Ch 2 drafting authorization (the listen-test pair). Until those drafts exist and Kokoro renders them, no further chapter drafting is recommended.
- **No blockers from PAO side.** Every chapter entry above carries enough drafting context that the chapter can be drafted from this document + the linked artifacts without further upstream calls.
