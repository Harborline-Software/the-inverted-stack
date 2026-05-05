# Book 2 — Chapter-by-Chapter Outline (working blueprint)

> **Working title:** TBD. Concept artifacts use *Book 1 of the Sunfish series* / *Vol 2*.
> **Status:** outline drafted 2026-05-04 (PAO). All chapters at `icm/outline`. Pipeline plumbing in `build/audiobook.py` is staged but inert until Arc 1 reaches `icm/draft`.
> **Source artifacts:** read in this order before drafting any chapter:
> 1. `.pao-inbox/_creative/vol-2-concept-note-2026-05-04.md` — the 12-section synthesis
> 2. `.pao-inbox/_creative/vol-2-concept-locked-elements-2026-05-04.md` — running locks index
> 3. `.pao-inbox/_creative/character-sheets/` — Anna, Joel, Priya, Wanjiru as a minimum for Book 1
> 4. `.pao-inbox/_creative/forsaken-position-papers/` + `oss-architects-voices/` — voice references
> 5. `.pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md` — mission timeline
>
> **What this document is:** the working blueprint. Each chapter entry carries everything a drafter (inline PAO at xhigh, technical-book-writer agent, or human) needs to produce a first draft *without re-deriving structure from the concept note each time*. The 8 sample story arcs from concept note §7 form the spine; the supporting/connective chapters fill the act structure to ~18 chapters / ~85,000-90,000 words / ~9-10 hours audiobook.

---

## Three-act structure (concept note §6.3)

| Act | Days | Chapters | Word target | Audiobook hours |
|---|---|---|---:|---:|
| **Act I — Departure and the first under-ice realization** | 1-21 | Ch 1-6 | ~30,000-32,000 | ~3.5 |
| **Act II — Subsystems hold; the contest sharpens** | 22-42 | Ch 7-12 | ~28,000-30,000 | ~3.0-3.5 |
| **Act III — Cascade, ascent, and the cumulative reveal** | 43-56 | Ch 13-18 | ~32,000-35,000 | ~3.5-4.0 |
| **Total** | 1-56 | 18 | ~90,000-97,000 | ~9-10 |

---

## Per-chapter conventions

Every chapter entry below carries the same fields:

- **Days / setting:** mission-day window + physical location
- **Architectural claim:** the single load-bearing claim from Joel's paper this chapter exercises (one chapter, one claim — never two)
- **Frame ratio:** % mission-present narration vs. % flashback; default 60/40 per concept note §6.1
- **Key character beats:** what each present character does or registers in this chapter
- **Length target:** word count + estimated audiobook duration at ~9,000 words/hour
- **Verification gap:** the specific thing about Joel's paper that this chapter tests against reality
- **Drafting notes:** what the drafter needs to know that isn't obvious from the concept note

---

# Act I — Departure and the first under-ice realization

**Days 1-21.** Establishes Anna's narrator register; introduces the crew through her command voice; installs the captain-asks-engineer dialogue engine; lands the first architectural realization (Day 20); closes on the first surface window with the rival mission's preliminary results entering Anna's awareness for the first time on the boat.

---

## Ch 1 — *Departure* (Day 0, Punta Arenas)

- **Days / setting:** Day 0, 2026-09-15 (placeholder), Punta Arenas dock; ceremonial sailing.
- **Architectural claim:** none direct — this chapter installs the narrator's voice and the mission's stakes. The architecture is foreshadowed only through Wanjiru handing Anna the key set.
- **Frame ratio:** 100% mission-present. (Flashback begins in Ch 2.)
- **Key character beats:**
  - **Anna:** first-person narration installed; reader registers Anna's mid-50s command-mature voice; the staff-history framing device implied (this is being written down).
  - **Joel:** present at the dock; visible respect from the crew; reader registers him as a present figure but his architect role surfaces only in Ch 4.
  - **Wanjiru:** key-handover scene — keys + the relay-network handoff from Helsinki ground station.
  - **Priya, Sabina, Diego, Hiroshi, Maria:** boarding sequence; reader registers each by name + national background + role; lighter treatment.
  - **The rival mission:** mentioned as ambient fact — *they sailed two months ago.* Stefan's name surfaces. No dramatization yet.
- **Length target:** ~4,500 words / ~30 minutes audiobook.
- **Verification gap:** none direct.
- **Drafting notes:** the chapter has to do double duty — install the narrator and seed every later thread without bloating. Prioritize the dockside scene over exposition; trust the reader to ride out unexplained references that resolve in later chapters. The Helsinki ground station + Wanjiru's relay handoff is the single load-bearing technical detail; everything else is character + atmosphere.

## Ch 2 — *The Recruitment Interview* (Arc 2 — flashback)

- **Days / setting:** flashback to ~6 months before departure; Anna's office, video call to Joel.
- **Architectural claim:** *the architect's response to being told he was wrong is what makes the architecture trustworthy.* The R1-BLOCK-rewrite admission as foundational trust event.
- **Frame ratio:** 10% mission-present (frame anchor at start + end) / 90% flashback.
- **Key character beats:**
  - **Anna:** has read the paper + the council Round 1 review + the Round 2 review; her questions are designed to surface whether Joel will tell the truth when it matters; structural inverse of what failed her with Stefan.
  - **Joel:** the admission. *I missed it. The original protocol assumed condition X that doesn't hold under sustained partition. Klett was right. I rewrote it.* No softening, no defense, no deflection.
  - **The structural beat:** the disclosure-without-compulsion that becomes the architecture's load-bearing trust property.
- **Length target:** ~9,000 words / ~60 minutes audiobook.
- **Verification gap:** the foundational one — does Joel tell Anna the truth about the council BLOCK before she selects him? He does; that is why she selects him. The rest of the book pays this off.
- **Drafting notes:** structurally early because it establishes the trust on which the entire mission rests. This is one of the two listen-test chapters (concept note §9). Two characters; sustained back-and-forth; technical content delivered through Anna's questions and Joel's answers. The chapter is the validation test for the captain-asks-engineer pattern as the audiobook-tempo solution. Joel's voice register is `joel-reyes-principal-architect.md`. Anna's is `dr-leader-mission-director.md`. Both sheets carry the founding-act-of-grace beat at full detail.

## Ch 3 — *Drake Passage and the Ice Edge* (Days 1-7)

- **Days / setting:** Days 1-7 transit south; Drake Passage; ice edge; surface operations.
- **Architectural claim:** *the relay layer operates correctly when the network is healthy* (baseline confirmation; the architecture's claim about partition only matters because the non-partition claim is held).
- **Frame ratio:** 80% mission-present / 20% flashback (Sabina's logistics background; Diego's polar-operations history surface through Anna's questions).
- **Key character beats:**
  - **Sabina:** logistics overview — what the consortium ports expect; the bid-disaster backstory surfaces briefly during a quiet exchange (her `chapters/part-1-thesis-and-pain/ch01` Ch 1 victim register transposed to Vol 2's mature time-frame).
  - **Diego:** polar-operations exposition through Anna's questions; reader registers him as the senior technical specialist; *quietly essential* register installed.
  - **Hiroshi:** quiet at the data console; reader registers reliability without dramatization.
  - **Joel:** first acoustic-only mesh test (under-ice rehearsal while still on surface); explains to Anna what's about to be different.
- **Length target:** ~4,500 words / ~30 minutes audiobook.
- **Verification gap:** the architecture's surface-operation behavior matches Joel's specification. Baseline established so that partition-mode behavior in Ch 4-5 is legible by contrast.
- **Drafting notes:** the chapter is structurally a setup chapter. Resist climaxing it. Diego and Sabina need to enter as recognizable people; Hiroshi gets less treatment because his moment is later. The acoustic-mesh-rehearsal is the technical anchor; the rest is character + the ship's transit register.

## Ch 4 — *First Submersion* (Day 7, Segment 1 begins)

- **Days / setting:** Day 7 dive; Segment 1 begins; ~14 days submerged ahead.
- **Architectural claim:** *the local store is operating in partition mode now; the relay layer is dormant; the gossip protocol can no longer reach the consortium ports.* The captain-asks-engineer pattern installed.
- **Frame ratio:** 70% mission-present / 30% flashback (Joel's pre-mission walk-throughs surface during the explanation; Anna's prior-mission interior briefly compares).
- **Key character beats:**
  - **Anna:** first sustained interrogation of Joel about *what is different now.* The chapter is structured around her questions; her command authority is established by what she asks.
  - **Joel:** explains. The chapter installs the dialogue-engine that carries every architectural beat in the book. Walks Anna through the local-store-as-only-reality fact; the relay-layer's dormant state; the gossip protocol's inactivity.
  - **Priya:** quiet check on the schema state at submersion; *the migration we are not running today.* Foreshadow without foregrounding.
  - **Wanjiru:** the comm-node state at submersion; the audit-log design that preserves provenance under partition.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture transitions from healthy to partition-mode without any state corruption; the local store is uncorrupted; the gossip protocol has correctly identified itself as dormant rather than failing.
- **Drafting notes:** this is the chapter that installs the captain-asks-engineer engine as the book's primary exposition mechanism. Every later technical chapter inherits this pattern. The chapter's load is the dialogue itself; the ambient submarine procedure is texture, not subject.

## Ch 5 — *The Day-Twenty Realization* (Arc 1)

- **Days / setting:** Day 14 from departure / ~Day 7 of sustained under-ice operation; mid-Segment-1.
- **Architectural claim:** *the local store is authoritative under partition because there is nothing else.*
- **Frame ratio:** 100% mission-present. (Flashback would dilute the realization.)
- **Key character beats:**
  - **Anna:** queries the local store for a colleague's prior write — a piece of provenance from before the mission. The system answers locally without ambiguity, because it cannot do otherwise. The compounding recognition: *Everything I am recording right now is only here.* / *This is what Joel built.* The emotional landing: not triumph; recognition.
  - **No other character on-page substantively.** Joel may be elsewhere on the boat. The realization is interior; the architecture's authority is registered in solitude.
- **Length target:** ~6,000 words / ~40 minutes audiobook.
- **Verification gap:** the chapter is the verification gap. The architecture's authoritative-local-store claim from the paper is exercised against Anna's lived experience under partition for the first time. The claim holds.
- **Drafting notes:** **this is one of the two listen-test chapters (concept note §9).** The chapter's primary risk is overwriting the realization; trust the silence and the single-character interior. Tight scene; one location; emotional realization at the chapter's center. If Arc 1 listens well as audiobook, Anna's first-person mission-frame voice is validated. If it does not, the issue is identifiable to the narrator-voice choice itself.

## Ch 6 — *First Surface, First Forsaken Reveal* (Day 21-23)

- **Days / setting:** Day 21 surfacing; 2-day surface window; comms reconnect.
- **Architectural claim:** *the gossip layer rapidly reconciles with the consortium ports after partition; the audit log is intact; provenance is preserved.* Reconciliation under healthy network resumed.
- **Frame ratio:** 80% mission-present / 20% flashback (the Stefan-mission cut-short surfaces briefly when Anna registers his name in the news cycle).
- **Key character beats:**
  - **Anna:** first external contact after Segment 1; the rival mission's preliminary results land via Wanjiru's relay logs; Stefan's name surfaces in the news cycle for the first time on the boat; the architecture-vs-platform contest enters Anna's consciousness.
  - **Wanjiru:** her relay logs catch the rival's PR cycle as it lands; her structural-political reading of the rival is more sophisticated than anyone else's on the boat.
  - **Joel:** absent from this chapter's main scene by design — Anna registers the rival without yet processing it through Joel.
  - **Helvetia Trust SA + Stefan:** present in the news cycle; not yet dramatized in person.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the gossip protocol's reconciliation behavior matches Joel's specification. Provenance survives the round-trip.
- **Drafting notes:** the chapter installs the corporate-sponsor-vs-OSS axis as a present concern. Stefan and Helvetia are off-screen but legible. Anna's command authority is undisturbed by the rival's messaging; she registers it and continues.

---

# Act II — Subsystems hold; the contest sharpens

**Days 22-42.** Each subsystem the architecture claims gets exercised against operational reality through Anna-Joel dialogue or character-driven beats. The rival mission concludes with publicly-favorable results that the architecturally sophisticated will see were partially compromised. The Anna-Joel love arc becomes legible to Anna in the surface-window micro-exchanges; she does not act.

---

## Ch 7 — *Joel's Sunfish* (Arc 3)

- **Days / setting:** Day 22, Surface 1 quiet hours.
- **Architectural claim:** *the architecture's name carries the discipline that makes it work.* The naming reveal as architectural disclosure.
- **Frame ratio:** 50% mission-present / 50% flashback (Joel's USS Sunfish SSN-649 service surfaces in the conversation).
- **Key character beats:**
  - **Joel:** discloses the name's origin — USS Sunfish SSN-649, decommissioned 1998, his first submarine. *The discipline that runs through the architecture got formed there.*
  - **Anna:** recognizes what she had been registering since she read the paper. The submarine-discipline-as-architectural-substrate becomes legible.
  - **The Long Now beat:** the boat-that-no-longer-exists left something in Joel that is now in the architecture; the architecture will outlive Joel; the discipline travels.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's discipline (the procedural rigor that produces the maintainability) traces to a specific human history. Anna sees it.
- **Drafting notes:** intimate; conversational. Two characters; one location; sustained quiet. The chapter is the first beat of the Anna-Joel love arc that Anna explicitly registers — but only as architectural recognition of Joel, not romantic recognition. The romantic register is in the *quality* of her attention, not in dialogue. Joel's nuclear-Navy register in `joel-reyes-principal-architect.md` is the voice reference.

## Ch 8 — *Second Submersion* (Day 23)

- **Days / setting:** Day 23 dive; Segment 2 begins; ~14 days ahead.
- **Architectural claim:** *the architecture is operational on the routine cycle; the partition transition is no longer novel.*
- **Frame ratio:** 80% mission-present / 20% flashback (Sabina's prior use-case work surfaces during her validation pass).
- **Key character beats:**
  - **Sabina:** first use-case validation pass — a logistics scenario the architecture has not actually run before; she walks Joel through the constraint; the architecture handles it; her bid-disaster history retroactively legible as why she insisted on this validation.
  - **Hiroshi:** steady at the data console; first substantive on-page beat; reader registers the depth behind the quiet.
  - **Diego:** attentive; supports Sabina's validation procedurally.
  - **Anna:** command discipline tightening into routine; the chapter shows what *normal* looks like in Segment 2.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** Sabina's use-case validates against the architecture's operational behavior. The architecture handles it correctly.
- **Drafting notes:** Sabina earns the chapter's center; she has been treated lightly through Acts I, and Act II is where she becomes a person. Hiroshi's beat is brief but load-bearing. The chapter is structural cycle-as-content; it should not feel slack.

## Ch 9 — *Subsystem Test — Sync Daemon Under Drift* (mid-Segment 2)

- **Days / setting:** ~Day 30; mid-Segment 2; routine cycle.
- **Architectural claim:** *the gossip protocol handles sustained network drift without manual intervention.*
- **Frame ratio:** 70% mission-present / 30% flashback (Joel's debugging walks back to specific design decisions that are now exercised live).
- **Key character beats:**
  - **Joel:** debugs the sync daemon in real time; the chapter is Joel's running architectural commentary on what's actually happening. The dialogue-engine working at non-climactic intensity. Reader sees the architecture's specifications operating against operational drift.
  - **Anna:** asks the questions that surface the architectural detail. Her questions are the reader's questions. Captain-asks-engineer at routine tempo.
  - **Priya:** present in the background; her schema-migration discipline foreshadowed without spending.
- **Length target:** ~6,000 words / ~40 minutes audiobook.
- **Verification gap:** the gossip protocol's drift-handling specification holds against actual mid-mission drift. The protocol does not require human intervention; the architecture's autonomy claim is exercised on a non-climactic problem and confirmed.
- **Drafting notes:** the chapter is the dialogue-engine pattern at its most exposed. The chapter has to be technically dense without sacrificing audiobook tempo — the test is whether Joel's architectural commentary, mediated by Anna's questions, can carry the technical load in listenable prose. If it can on this chapter, it can on Ch 13 (Priya) and Ch 15 (Wanjiru). Reference: Sunfish package surface (concept-note §2 vouches for accuracy; do not invent APIs).

## Ch 10 — *The Aftermath of a Mission That Once Was* (Arc 7 — substantial fragment)

- **Days / setting:** ~Day 33; Segment 2 quiet night; Anna's interior surfacing during a routine watch.
- **Architectural claim:** *trust hardens in specific shapes; the inverse of betrayal is disclosure-without-compulsion.* The chapter retroactively legibilizes Anna's selection criteria for Joel + Priya + Wanjiru.
- **Frame ratio:** 30% mission-present / 70% flashback (the Stefan-mission cut-short; the colleague's mix of acknowledgment and minimization; the five years between then and now).
- **Key character beats:**
  - **Anna:** prior-failure interior — the Stefan-mission cut short on operational grounds because the schema-migration limitation Stefan had not disclosed manifested under partition; the technical staff died (or were medevaced — exact prior-mission casualty terms TBD per concept-note §10.1); the trust-hardening; the inverse-of-betrayal recognition.
  - **No other character substantively on-page** — the chapter is Anna's first-person interior at length.
  - **Joel:** mentioned only in the recognition that what Anna selected him for is the structural inverse of what failed her last time. *He told me the truth about the BLOCK before I asked him. Stefan never told me.*
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architectural property of trust (disclosure-without-compulsion) is the inverse of the architectural property of failure (non-disclosure-under-pressure). Anna's selection of Joel was made on a structural property of his character that exactly inverses what failed her last time.
- **Drafting notes:** the chapter is mostly flashback; the mission-frame anchor is light. Does not dramatize Stefan in person (he is fully dramatized in Book 4); the Stefan figure is Anna's interior. Refer `stefan-reinhardt-rival-architect.md` for Stefan's dimension; the chapter does not require all of him to land — only Anna's reading of him is required. The chapter is the load-bearing prior-failure interior for Book 1; subsequent Arc 7 fragments distribute lightly across other chapters.

## Ch 11 — *Second Surface, Second Forsaken Reveal* (Day 37-39)

- **Days / setting:** Day 37 surfacing; 2-day surface window.
- **Architectural claim:** *the architecture is intact across two surface-window cycles; the audit log compounds correctly.*
- **Frame ratio:** 75% mission-present / 25% flashback (Anna's recognition of the love-arc beat retrospectively legibilizes the surface-window micro-exchanges).
- **Key character beats:**
  - **Wanjiru:** reads the regulatory landscape; the rival mission has concluded; Stefan's PR spin lands; the cumulative reveal sharpens; her standards-body work (foreshadowed for Book 5) gets a quiet beat.
  - **Anna:** registers the love-arc beat — Joel's behavior in the surface-window's micro-exchanges has become legible to her in retrospect; she does not act. Per concept-note §6.4, the love arc is *secondary register*; not foregrounded.
  - **Joel:** behaviors continue; his discipline holds; he does not register that Anna has registered.
  - **Stefan + Helvetia + Astrid:** continued off-screen presence in the news cycle; the rival mission's *publicly favorable* results are dissected by Wanjiru in conversation with Anna.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's two-cycle persistence; the gossip protocol holds across two reconciliations; provenance survives compounding round-trips.
- **Drafting notes:** the chapter advances the corporate-sponsor-vs-OSS axis; Wanjiru is the reading-engine for the political dimension as Joel is for the architectural dimension. Anna's love-arc registration is *a quality of her attention,* not a beat of dialogue or action — written in the texture of how she sees Joel, not in narrative motion.

## Ch 12 — *Beginning of the End — Segment 3 Dive* (Day 39)

- **Days / setting:** Day 39 dive; Segment 3 begins; ~10 days ahead — the climax segment.
- **Architectural claim:** *the architecture's discipline is the precondition for the climax* — the chapter foreshadows without pre-spending.
- **Frame ratio:** 80% mission-present / 20% flashback (Joel's last-leg-of-deployment register from his Navy days surfaces briefly).
- **Key character beats:**
  - **Anna:** bridge command discipline tightens; the last-leg discipline of submarines becomes legible.
  - **Joel:** quietly grounded; nuclear-Navy register becomes more pronounced under operational pressure.
  - **Priya:** schema state checked; the three-pass migration discipline is implicit in everything she does in this chapter; foreshadow without spending.
  - **Diego:** tempo accelerates; he is more visible; reader's anticipation primed.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's pre-climax state is intact; nothing is broken on entering Segment 3. Sets the contrast for what changes during the cascade.
- **Drafting notes:** structurally a setup chapter; the chapter's job is to install enough operational tension that the cascade in Ch 14 does not feel arbitrary. Discipline is the subject; not just discipline as theme but discipline as everyone's behavior visible on the page.

---

# Act III — Cascade, ascent, and the cumulative reveal

**Days 43-56.** The two architectural climax chapters (Priya's schema migration; the leak-and-fire cascade) land back-to-back; the security architecture climax (Wanjiru's compromised-relay-holds) lands during the cascade. The mission concludes; the boat surfaces at Punta Arenas; the cumulative Forsaken reveal lands as Anna writes the staff history that produces Vol 1.

---

## Ch 13 — *The Schema That Should Not Migrate* (Arc 4)

- **Days / setting:** ~Day 43-44; mid-Segment 3.
- **Architectural claim:** *schema migration is Healing — preserving identity through transformation.* The Healing/Saidar discipline is exercised on the architecture's hardest schema-evolution case under operational duress.
- **Frame ratio:** 80% mission-present / 20% flashback (Priya's lab-review pre-mission position surfaces; the *I would have refused this in lab review* moment grounded in her prior pattern).
- **Key character beats:**
  - **Priya:** says no, then says how-to-do-it-anyway, then walks Joel through the migration in real time. Two near-failures during the read-confirmation cycle that Priya's three-pass discipline catches. The migration succeeds.
  - **Joel:** executes the migration under Priya's direction; the architectural protocol's schema-migration safety properties hold.
  - **Anna:** asks Priya to authorize on operational grounds; respects the *no* before respecting the *yes-with-conditions*; her command authority is the precondition for Priya's safety net.
  - **The post-migration recognition:** the architecture worked because Priya's caution was built into it as a constraint, not because the mission followed her caution as a rule. (Concept note §7 Arc 4 — load-bearing.)
- **Length target:** ~10,000 words / ~67 minutes audiobook.
- **Verification gap:** the schema-migration protocol holds under conditions Joel's paper specifies it should hold under, with three-pass confirmation that the paper specifies as the safety property. The verification is procedural, not numerical; the chapter is the verification gap.
- **Drafting notes:** technical density is high; the chapter earns the length. Captain-asks-engineer pattern is now Anna-asks-Priya / Anna-asks-Joel parallelized; Priya gets her own voice register from `priya-iyer-schema-migration.md`. The Nynaeve-says-no-until-forced register is the voice reference. Saidar (policy/healing) layer in operational form. **Chapter pairs with Ch 14:** the boat is in cascade by the end of this chapter or just after; Ch 13 ends with the migration just stable + the leak alarm just firing, or in close sequence.

## Ch 14 — *The Crossing* (Arc 6)

- **Days / setting:** Day 47 (placeholder; consistent with prior `chapters/closing/the-crossing.md` Day 47 0317 leak alarm); Segment 3 climax.
- **Architectural claim:** *the architecture is adequate, not heroic; the procedure is the heroic act.* The architectural protocol's behavior under environmental cascade is measured against the procedural discipline Diego, Joel, and Anna bring to the cascade itself.
- **Frame ratio:** 95% mission-present / 5% flashback (Joel's nuclear-Navy training surfaces in the texture of his action, not as flashback scene; Anna's love-arc recognition compounds privately but the chapter does not flash back).
- **Key character beats:**
  - **The leak:** instrument-malfunction origin (per CO direction 2026-05-05); small leak, high stakes, in a confined access compartment behind equipment. 0317 leak alarm; 0319 cabin-to-bridge transit; 0321 assessment; 0342 compartment isolation order.
  - **Diego:** polar-operational experience landing as procedural competence; the chapter's central act-of-competence beat. Diego survives and retires to San Martín de los Andes earned through what he did. (Cast-swap from earlier draft: Diego survives, replacing the death-scene of the original closing chapter — see locked-elements doc.)
  - **Joel:** **the protective beat (CO direction; refined 2026-05-05).** The alarm fires; his instinct from thirty years of nuclear-Navy training fires before any cognitive part of his mind has caught up. He moves toward the leak. He pushes Anna aside on his way past her. He shuts the bulkhead door behind himself and locks it from his side. Then he turns and faces Anna through the porthole window of the bulkhead door. The look says, without a word, everything that his discipline has prevented him from saying since the recruitment interview. Anna receives it. Her command authority holds; the bridge is watching her. He turns and goes to work. Eleven minutes; he contains the instrument failure, drains the residual water, reports clear, emerges. (Source: `joel-reyes-principal-architect.md` love-arc layer; concept note §7 Arc 6.)
  - **Anna:** unsentimental command authority through the eleven minutes; the bridge is watching her; her face does not change. The recognition compounds privately for the rest of Book 1.
  - **Priya, Sabina, Hiroshi, Maria:** procedural roles during the cascade; everyone executes; the boat is a procedure not a hero.
  - **Wanjiru:** her chapter is Ch 15; she is on the comm node here, working the audit log + the gossip layer through the cascade.
- **Length target:** ~12,000-13,000 words / ~80-87 minutes audiobook. **The longest chapter in Book 1.**
- **Verification gap:** the architectural protocol behaves as specified through the cascade; the protocol's environmental-stress claim from Joel's paper is exercised against literal physical environmental stress and holds. The eleven minutes Joel is behind the door are the chapter's emotional center.
- **Drafting notes:** **the climax.** Inherits beats from `chapters/closing/the-crossing.md` (Vol 1's existing closing chapter, 4,396 words) but expands ~3× through the instrument-leak protective sequence + Diego's competence at full altitude + Anna's command-watch silence + the Spanish-letter-to-María-Elena beat (recovery, not death notification, since Diego survives in the new version). The Spanish letter scene per concept-note §7 Arc 6. Vol 1's existing chapter requires a separate revision pass to align with the multi-segment design; that revision pass is gated on CO authorization (concept-note §10.2). For Vol 2 Ch 14 drafting, work from the concept note + character sheets, not from the existing Vol 1 chapter — the existing chapter is the *seed* for this chapter, but the prose register is mature-Anna-narration not Vol-1-staff-history-fragment.

## Ch 15 — *The Compromised Relay Holds* (Arc 5)

- **Days / setting:** Day 47-48; during and immediately after the leak-and-fire cascade.
- **Architectural claim:** *security architecture designed for political fragility holds against environmental degradation; the worst case in the political dimension shares its shape with the worst case in the physical dimension.*
- **Frame ratio:** 75% mission-present / 25% flashback (Wanjiru's M-PESA-adjacent design history surfaces in the moment she recognizes the structural similarity).
- **Key character beats:**
  - **Wanjiru:** comm-node damage threatens the gossip layer that propagates revocations; sensor compartment loss threatens the audit trail; she works the architecture through the degraded mode in real time. The post-cascade retrospective recognition: *the security model that defended against political coercion turned out to defend against environmental degradation. The two threat models had a deeper structural similarity than either of us had named.*
  - **Joel:** present; participates in the recognition but the chapter is Wanjiru's; her register from `wanjiru-kamau-security-policy.md` is the lead voice.
  - **Anna:** witness; the chapter compounds the architecture's case for her as the maiden voyage's chief beneficiary.
- **Length target:** ~8,500 words / ~57 minutes audiobook.
- **Verification gap:** the security architecture's revocation-under-coercion specification is exercised against environmental degradation. It holds. The verification is the structural-similarity recognition, which is what makes Wanjiru the eventual standards-body chair.
- **Drafting notes:** chapter pairs immediately with Ch 14 in time (during + after the cascade); Wanjiru is the lead voice. Saidin (Joel's protocol layer) and Saidar (Wanjiru's policy layer) operating against the same physical event from different architectural angles — the chapter is the second of the two-discipline reveals (Ch 13 was Saidar; Ch 14 was Saidin under stress; Ch 15 is Saidar under stress). The Egwene/Wanjiru voice register is the one she will carry into Book 5's standards-body chair beat.

## Ch 16 — *Final Ascent* (Days 49-52)

- **Days / setting:** Day 49-52; Segment 3 ends; the boat surfaces at Punta Arenas approach.
- **Architectural claim:** *the architecture is proven across the maiden voyage's full operational envelope.*
- **Frame ratio:** 70% mission-present / 30% flashback (Joel's mid-50s reflection on what the architecture has now demonstrated; Anna's reflection on what the mission has cost — Diego's retirement; nothing else lost).
- **Key character beats:**
  - **Anna:** command discipline easing; the mission's stakes have settled; the regulatory landscape ahead is the new tension.
  - **Joel:** quietly satisfied; the architecture has performed; he does not yet know what Stefan has done in his absence.
  - **Wanjiru:** preparatory work for the Punta Arenas reveal; her relay is reading the inbound regulatory traffic.
  - **Diego:** quietly grounded; he does not yet announce his retirement decision.
  - **Priya, Sabina, Hiroshi, Maria:** the routine cycle of a successful mission's last days.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture has held end-to-end. The chapter is the verification's end state.
- **Drafting notes:** structurally a denouement chapter for Acts I-III's mission-architecture spine; the chapter's emotional payoff is restraint, not triumph. The Punta Arenas reveal in Ch 18 is the contrast.

## Ch 17 — *Transit North* (Days 52-56)

- **Days / setting:** Day 52-56; surface transit Drake Passage → Punta Arenas.
- **Architectural claim:** *the staff history is a load-bearing artifact; the act of writing it makes the architecture transmissible.*
- **Frame ratio:** 80% mission-present / 20% flashback (Wanjiru's earlier conversation with Anna about staff-history convention surfaces).
- **Key character beats:**
  - **Wanjiru:** asks Anna to write the mission account. The staff-history is a load-bearing institutional convention; this is the device that produces Vol 1 (Joel's paper) and Vol 2 (Anna's narration).
  - **Anna:** accepts the assignment; the chapter shows her beginning the work that the reader has been receiving since Ch 1 of Vol 2 (and that produced Vol 1 in the H.G. Wells convention).
  - **Diego:** the Spanish letter to María Elena written and prepared for posting at Punta Arenas; recovery-not-death-notification register; per concept-note §7 Arc 6.
  - **Joel:** quiet; the chapter is not centered on him; Anna's love-arc recognition continues compounding privately.
  - **Priya, Sabina, Hiroshi, Maria:** transit-cycle texture.
- **Length target:** ~5,000 words / ~33 minutes audiobook.
- **Verification gap:** the architecture's transmissibility — that what Joel built can be communicated to readers who were not on the boat — is exercised in Anna's first sustained writing pass. The verification is meta-textual; the reader is reading the artifact.
- **Drafting notes:** the chapter is the H.G. Wells convention surfaced. Anna writes; the reader reads what she wrote. The chapter's primary pleasure is recognition: *this is what we have been listening to.* Restraint required; do not over-foreground the device.

## Ch 18 — *Punta Arenas Surfacing* (Arc 8)

- **Days / setting:** Day 56, 04:41 local, Punta Arenas dock; final surfacing.
- **Architectural claim:** *the maiden voyage proved the architecture; the contest over its meaning has only begun.*
- **Frame ratio:** 60% mission-present / 40% reveal (the boat is moored; first external contact; the cumulative reveal lands).
- **Key character beats:**
  - **Anna:** receives the first external contact; the Punta Arenas dockside team has the rival mission's PR cycle, the Working Group regulatory filing draft (per `forsaken-position-papers/03-regulatory-filing.md` — though that filing dates February 2027 in the locked artifact, the *preliminary response* lands here per concept-note §3.6 / §7 Arc 8); Wanjiru's standards-body has issued a preliminary response; the architectural contest enters its public phase.
  - **Wanjiru:** reads the regulatory landscape with full bandwidth restored; her Annex A minority opinion (per `oss-architects-voices/01-annex-a-minority-opinion.md`) is foreshadowed as the document she will write.
  - **Joel:** quietly absorbs that Stefan has been busy; the public framing of his architecture is now contested; the work ahead is contestation, not building.
  - **Priya, Diego, Sabina, Hiroshi, Maria:** disembarkation; Diego's retirement to San Martín de los Andes announced.
  - **The cumulative Forsaken reveal:** while the boat was under, the first formal regulatory challenge to local-first architecture was filed; Stefan's mission concluded with publicly-favorable results that the architecturally sophisticated will see were partially compromised; Wanjiru's standards body has issued a preliminary response. The mission's success and the world's response converge.
  - **Anna writes the staff history** — closing image; the device that produced the book.
- **Length target:** ~7,000 words / ~47 minutes audiobook.
- **Verification gap:** the architectural maiden voyage's meaning is contested in the world. The mission's verification is private; the contest is public. The book ends with the architecture proven and the real contest beginning.
- **Drafting notes:** **the closing chapter.** Set up the rest of the series: Book 2's regulatory war (Wanjiru-led; per concept-note §3.6); Book 3's love-arc disclosure (Anna and Joel; per concept-note §6.4); Book 4's Stefan dramatization. The chapter has to land Book 1's emotional payoff (the architecture proved; Diego survived; Anna's command authority confirmed; Joel's discipline confirmed) without short-circuiting Book 2's escalation. The closing image is Anna at her desk beginning to write; the reader has just finished reading what she will write. Restraint is the register; the contest is foregrounded but the response to the contest is reserved for Book 2.

---

## Length and audiobook reconciliation

| Chapter | Words (target) | Audiobook minutes |
|---|---:|---:|
| Ch 1 — Departure | 4,500 | 30 |
| Ch 2 — The Recruitment Interview | 9,000 | 60 |
| Ch 3 — Drake Passage and the Ice Edge | 4,500 | 30 |
| Ch 4 — First Submersion | 5,000 | 33 |
| Ch 5 — The Day-Twenty Realization | 6,000 | 40 |
| Ch 6 — First Surface, First Forsaken Reveal | 5,000 | 33 |
| Ch 7 — Joel's Sunfish | 5,000 | 33 |
| Ch 8 — Second Submersion | 5,000 | 33 |
| Ch 9 — Subsystem Test — Sync Daemon Under Drift | 6,000 | 40 |
| Ch 10 — The Aftermath of a Mission That Once Was | 5,000 | 33 |
| Ch 11 — Second Surface, Second Forsaken Reveal | 5,000 | 33 |
| Ch 12 — Beginning of the End | 5,000 | 33 |
| Ch 13 — The Schema That Should Not Migrate | 10,000 | 67 |
| Ch 14 — The Crossing | 12,500 | 83 |
| Ch 15 — The Compromised Relay Holds | 8,500 | 57 |
| Ch 16 — Final Ascent | 5,000 | 33 |
| Ch 17 — Transit North | 5,000 | 33 |
| Ch 18 — Punta Arenas Surfacing | 7,000 | 47 |
| **Total** | **~113,000** | **~750 minutes / ~12.5 hours** |

**Reconciliation note:** the row-by-row sum (~113,000 words, ~12.5 hours) overshoots the concept-note target of ~80,000-100,000 words / ~9-10 hours by ~15-20%. This is the standard outline-overshoot pattern; the actual draft will compress through:

- Per-chapter pruning of low-load passages during prose-review (the same Phase 4 quality-driven pass that operated on Vol 1)
- Real-paragraph-level word counts often landing 5-10% under chapter target after voice-pass discipline removes scaffolding
- Chapters that combine in drafting (e.g., Ch 6 + Ch 7 if the surface window's Joel-Anna conversation organically flows from the Forsaken reveal scene; Ch 16 + Ch 17 if the transit-north narrative cohesion holds across the staff-history-conversation beat)

If post-listen-test verdict is positive and the full Book 1 draft begins, expect the actual word count to land at ~95,000-105,000 words / ~10.5-11.5 hours audiobook — comfortably within the trade-novel range and within audiobook listenability tolerances per concept note §8.

If chapters do not compress as expected during drafting, the structural lever is splitting Ch 14 into two chapters (the cascade itself + the eleven-minutes-behind-the-door + immediate aftermath as a separate chapter), bringing the total to 19; or holding at 18 chapters and accepting ~110,000 words / ~12 hours audiobook.

---

## Drafting sequence (per concept note §11 production sequence)

1. **Listen-test pair first:** Ch 5 (*The Day-Twenty Realization*) + Ch 2 (*The Recruitment Interview*). Render through Kokoro. CO listens uninterrupted. Verdict drives full-Book-1 commit-or-revise.
2. **If both land:** draft Acts I-III in sequence per outline. Estimated 60-90 days at sustainable Yeoman + PAO + technical-book-writer-agent tempo.
3. **If one lands, one does not:** revise the failed chapter's structural choice; re-test.
4. **If neither lands:** back to concept-note revision; the format needs structural rework before further drafting.

The two listen-test chapters are deliberately the highest-difficulty chapters for the format choice:
- Ch 5 is the *first-person mission-frame* test — single character, single location, interior recognition; the format's hardest case.
- Ch 2 is the *captain-asks-engineer dialogue engine* test — sustained technical dialogue at audiobook tempo; the format's hardest case for technical exposition.

If both listen well, every other chapter is between these two extremes. If either fails, the failure is identifiable to a specific structural choice rather than to general format weakness.

---

## Cross-references for drafters

Drafting any chapter requires reading at least these artifacts in addition to the entry above:

- **All chapters:** concept note §1-§7 + Anna sheet + (relevant chapter character) sheet
- **Ch 2:** Joel sheet at full depth; council Round 1 + Round 2 review documents (`source/kleppmann_council_review.md`, `source/kleppmann_council_review2.md`); the BLOCK-then-rewrite is canonical there
- **Ch 5:** concept note §3.4 (Long Now thread) + §6.3 (Day-20 partition realization scene as Book 1 structural requirement)
- **Ch 7:** Joel sheet's USS Sunfish SSN-649 / nuclear-Navy register at full depth
- **Ch 13:** Priya sheet + Joel sheet's schema-migration co-author register; concept note §3.2 (Saidar discipline)
- **Ch 14:** Joel sheet's leak-event protective beat at full depth (`joel-reyes-principal-architect.md` love-arc layer); Anna sheet's love-arc layer; concept note §7 Arc 6 (refined 2026-05-05); existing `chapters/closing/the-crossing.md` as seed
- **Ch 15:** Wanjiru sheet at full depth; concept note §3.2 (Saidar discipline + structural-similarity argument)
- **Ch 18:** all three voice exemplar libraries (`forsaken-position-papers/`, `oss-architects-voices/`); concept note §3.6 (8-book series map) for what's being seeded for Book 2

---

## Status

- **2026-05-04:** outline drafted; all 18 chapters at `icm/outline`; pipeline plumbing staged in `build/audiobook.py`.
- **CO-gated:** Ch 5 + Ch 2 drafting authorization (the listen-test pair). Until those drafts exist and Kokoro renders them, no further chapter drafting is recommended.
- **No blockers from PAO side.** Every chapter entry above carries enough drafting context that the chapter can be drafted from this document + the linked artifacts without further upstream calls.
