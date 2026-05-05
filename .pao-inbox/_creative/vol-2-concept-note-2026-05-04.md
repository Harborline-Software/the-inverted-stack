---
type: concept-note
date: 2026-05-04
author: PAO (synthesizing CO creative-session decisions across the 2026-05-04 session)
status: draft v1 — comprehensive synthesis of locked elements; ready for CO review
audience: CO; future PAO sessions; technical-book-writer agent if invoked for chapter drafting
relates-to:
  - vol-2-concept-locked-elements-2026-05-04.md (running locks; companion source-of-truth)
  - vol-2-series-arc-wot-bobiverse-2026-05-04.md (XO series-arc research)
  - vol-2-long-now-memory-thread-2026-05-04.md (Long Now thread lock)
  - 2026-05-04-vol2-boat-power-option-c-locked.md (boat power decision)
  - the-crossing-concept-note-2026-04-30.md (Vol 1 closing chapter; pattern precedent)
  - character-sheets/dr-leader-mission-director.md (Anna)
  - character-sheets/joel-reyes-principal-architect.md (Joel)
  - character-sheets/priya-iyer-schema-migration.md (Priya)
  - character-sheets/wanjiru-kamau-security-policy.md (Wanjiru)
  - character-sheets/stefan-reinhardt-rival-architect.md (Stefan / rival)
  - character-sheets/astrid-hansen-rival-captain.md (Astrid / rival)
  - character-sheets/helvetia-trust-corporate-sponsor.md (Helvetia / Brandt)
working-title: *The Filchner Dark* (Book 1)
series-working-title: *The Inverted Stack: The Sunfish Cycle* (or similar)
---

# Vol 2 Concept Note — *The Filchner Dark* (Book 1 of the Sunfish Cycle)

## Frontmatter for the reader

This document is the **synthesis artifact** for Vol 2 and the multi-book series it opens. It pulls together every structural decision locked across the 2026-05-04 creative session into a single readable plan. Companion docs are listed in the frontmatter; this note references them by anchor rather than reproducing their content. A future PAO session, a technical-book-writer agent, or any reader can read this note alone and execute against it.

The note is not the book; it is the plan. The first proof-of-concept chapters (specified in §10 below) come next.

## 1. Premise

*The Inverted Stack: The Sunfish Cycle* is a multi-book novel series that uses an Antarctic submarine voyage and its decades-long aftermath to dramatize a civilizational contest over information sovereignty. Each book advances both the immediate story and the long arc; together they argue, through narrative and not through specification, that the architecture of who-holds-our-memories is the architecture of what-survives-our-deaths.

Vol 2 is the first book. Vol 1 — the existing 154,337-word *The Inverted Stack: Local-First Nodes in a SaaS World* — is canonically the **research paper Joel Reyes published**, the architecture-spec the maiden voyage tests. In Vol 2's universe the paper is referenced and quoted but not reproduced. The H.G. Wells convention applies: Wells wrote *The War of the Worlds*; the unnamed first-person narrator is a literary device; the prior monographs the narrator quotes from exist in the world but are not delivered in full. The same convention here. Chris Wood and Claude (Anthropic) wrote both volumes; **Anna Yusupova narrates Vol 2**; **Joel Reyes is the in-universe author of Vol 1**.

The book exists because the existing 154k-word manuscript — comprehensive, technically rigorous, council-vetted, literary-board-passed — is structurally a research paper with narrative bookends. Audiobook listening reveals what print consumption masked: human working memory cannot track 56 days of dense architectural specification across sustained listening. The technical bits occasionally inspire; the volume of detail wearies. Vol 2 is the response: same architecture, same characters, same stakes — distilled into stories that listen well at audiobook tempo and that carry the architectural argument by enactment rather than by enumeration.

The series argument is the existing book's argument made through narrative: **local-first vs. cloud is not a technical disagreement; it is an argument about who holds your memories when you are gone.** The cloud answer is *the platform holds them, under the platform's terms, until the platform decides otherwise.* The local-first answer is *you hold them, in a form that can be passed on, on your own terms.* The architecture is the answer. The series shows the architecture being chosen, tested, defended, and (eventually) ratified into the world that survives the cycle.

## 2. Diegetic mechanic — the paper as artifact

The relationship between Vol 1 (the existing 154k ms) and Vol 2+ (the narrative series) is the load-bearing diegetic mechanic. Six points:

1. **Vol 1 is canonically Joel Reyes's research paper**, with co-contributors named (the Sunfish OSS community: Priya Iyer on schema migration; Wanjiru Kamau on security and key management; others by name as needed). The preface signature changes from the current `— Anna Yusupova` (PR #88) to `— Joel Reyes` to align with the new authorial frame. The body text — which was always written in the architect's voice — needs no other change. *The "I helped build this architecture" voice samples in Anna's existing closing chapter (`The Crossing`) and in Anna's character sheet are flagged for one-line revision: Anna read the paper; she did not write it.*

2. **In Vol 2's universe Joel's paper exists** as a real published artifact at github.com/ctwoodwa/Sunfish (as the preface already states), reviewed by the Kleppmann Council, cleared with conditions for first deployment. The paper is referenced where it earns its place — Anna quotes from it; council-review excerpts appear as chapter epigraphs; specific architectural beats reference paper sections by chapter — but is not reproduced in full. The reader is trusted to know the paper exists and to take Anna's references as authoritative.

3. **Sunfish-the-software is real working software**, not fictional. The repository at github.com/ctwoodwa/Sunfish is the actual reference implementation. The pre-1.0 disclaimer in the existing preface becomes literally diegetic: *the architecture is real, tested, vetted, version 0.x, and the Sunfish-1 mission is its production trial.*

4. **What is fictional is the narrator + the events**. Anna Yusupova narrates; the Antarctic mission and its three under-ice segments are fiction; the leak-with-fire-cascade is fiction; the Forsaken's institutional analogs (Helvetia Trust SA + Stefan Reinhardt's rival mission) are fiction; the council-review-as-vetting-that-authorized-deployment is fictional in its specifics but real in its body of work (the existing Vol 1 Part II chapters).

5. **The architectural arguments are real**. Every architectural beat the series dramatizes — schema migration under partition; lease coordinator quorum reduction; key-rotation revocation horizons; gossip degradation under sensor loss — corresponds to real architectural decisions specified in the existing Vol 1 manuscript. The series is the architecture's enactment, not its imagination.

6. **The out-of-frame "Note from the Authors"** at the top of Vol 1's preface (added in PR #88) carries forward across the series. Vol 2 has its own front-matter note that establishes the convention for new readers, references Vol 1's note, and points readers who want the spec to Vol 1 itself.

## 3. Series structure — WoT + Bobiverse hybrid + Long Now

Per CO direction (XO research artifact `vol-2-series-arc-wot-bobiverse-2026-05-04.md`), the series is a **WoT + Bobiverse hybrid** — both simultaneously, not one or the other. *A Gentleman in Moscow* contributes the confined-location, confined-cast discipline that Book 1 specifically requires (the submarine + the small crew + the mission window). *The Boys in the Boat* contributes the ensemble-technical-achievement-under-scrutiny register.

### 3.1 The Wheel of Time spine

The series follows WoT's structural inheritance. The cosmological layer is always-on but never explained as exposition:

| WoT concept | Series analog |
|---|---|
| The Pattern | The mesh — self-healing, partition-tolerant, resistant to centralization by design |
| The Dark One | The principle of total information control (not a person; a direction of travel) |
| The Bore | The moment a major regulatory body first successfully compelled cloud disclosure |
| The Breaking | The centralized-SaaS era: user data fully corporate-controlled; the world fractured into dependent fragments |
| The Third Age | Now. The contest is live but not yet decided. |
| The Last Battle | Achieving legislative or architectural lock-in for local-first data sovereignty — whichever side gets there first wins the age |
| Ta'veren | Deployments (and people) so architecturally significant that the Pattern bends around them. Sunfish-1 is a ta'veren event. |
| The Wheel itself | Time + entropy: every closed architecture eventually fails from within; the mesh is the Wheel's natural expression because only distributed systems actually survive |

**The Forsaken** are named in-universe as institutional roles only — never cartoonish villains. Each was once on the right side. Stefan Reinhardt is the series' first Forsaken and its first dramatized fallen ally; Helvetia Trust SA is the institutional vehicle.

### 3.2 The "One Power" — disciplines as Saidin / Saidar

- **Protocol layer** (distributed systems architecture — gossip, lease, sync, partition recovery) = **Saidin**. Historically tainted by association with infrastructure that can be weaponized. Requires naval-nuclear discipline to channel safely; otherwise corrupts the channeler. **Joel channels Saidin.** His Navy-nuclear discipline is the Three Oaths analog.
- **Policy layer** (data sovereignty governance, key management, role architecture) = **Saidar**. Requires surrender before mastery: you have to understand what the data means to the person it belongs to before you can protect it. Sabina's Grameen framing is the clearest embodiment of the surrender; Wanjiru's M-PESA-formed pragmatism is the discipline that lets her channel.
- **Anna cannot channel either.** She sees what the architecture does to real missions but cannot build it. That is her limitation and her power. She is the operator's avatar: what she gets is what every operationally-minded reader of Vol 1 gets from the paper.

### 3.3 The Bobiverse mechanic — replication and divergence

Every Sunfish deployment is a **Bob replication**. The architecture clones itself into a new context; each instance faces different pressures; some diverge from founding principles. The series question: *what makes a deployment still Sunfish?*

Book 1 introduces this obliquely. The submarine partition (3 under-ice segments + reconciliation events) forces local operation. When Sunfish-1 surfaces between segments, it must reconcile diverged state with the global mesh. The reconciliation scenes are both technical and narrative — Anna's first external contact at each surfacing reveals the Forsaken moved while the boat was under, and the cumulative reveal lands at final surfacing in Punta Arenas.

Later books: specific deployments go rogue through local optimization under extreme constraint. Priya's domain (schema migration: *can these schemas merge?*) and Wanjiru's domain (governance recognition: *should they merge?*) become the recurring conflicts.

### 3.4 The Long Now thread — *what will happen to these memories when I die*

Per CO direction (XO `vol-2-long-now-memory-thread-2026-05-04.md`), this is the series' **thesis statement in human terms.** The architecture IS the answer to that question.

- Cloud answer: *the platform holds them, under the platform's terms, until the platform decides otherwise.*
- Local-first answer: *you hold them, in a form that can be passed on, on your own terms.*

Every disaster in the prior architectures Anna lived with is a version of *the memories died because the institution died.* The vendor who cut off mid-mission in 2022 (Anna's Stefan-failure) didn't just lose her science — it lost whatever state the mission had accumulated. *Cloud death = memory death.*

**Wanjiru is the Long Now character** — she thinks in decades while everyone else thinks in missions; her arc deliberately builds toward her own dispensability (institutions that survive any single keeper).

**Anna's day-20 anchor scene is a Book 1 structural requirement.** First time Anna accesses the local store during partition (~Day 14 from departure under the new multi-segment design; mid-Segment-1). She realizes everything she is recording is *only here.* No backup, no external verification, no institutional memory unless this boat surfaces. She is either the archive or she is nothing. **This scene must land before the theme becomes structural in later books.**

### 3.5 The corporate-sponsor-vs-OSS axis

The structural architectural-philosophical split externalized into business-model split. **Sunfish is OSS** (community-built; community-governed; commercially neutral). **TrustMesh / HelveSync** (the rival platform, working name) is OSS-wrapper-on-top-of-corporate-federated-identity (Helvetia Trust SA's centralized-key-rotation authority is the trust layer). The architectures look similar from outside; the centralization compromise is legible only to the architecturally sophisticated.

The series asks the reader to do the work of recognizing the difference, the way Wanjiru's standards body asks the wider community to do the work in the in-universe present.

### 3.6 The 8-book series map

| Book | WoT analog | Core move |
|---|---|---|
| **1: *The Filchner Dark*** | *Eye of the World* | Architecture proved; Forsaken notice; Anna's day-20 realization; the rival mission's preliminary results land during Sunfish-1's surface windows |
| 2 | *The Great Hunt* | First formal regulatory assault; Stefan testifies for federated-trust; a deployment compromised; who controls the proving artifact? |
| 3 | *The Dragon Reborn* | Joel's architecture reborn in second-generation form; Forsaken try to control the spec process; TrustMesh wins a major standards-body endorsement; **Anna-Joel love arc disclosure** |
| 4 | *The Shadow Rising* | Flashback / deep-lore: the Breaking fully revealed; **Anna's prior failure with Stefan fully dramatized**; the audience sees pre-pivot Stefan; the partnership collapse is the book's emotional center |
| 5 | *Fires of Heaven* | Major network attack; mesh proves resilience; **Moiraine falls — Anna may be apparently lost**; convergence with Stefan's flagship status; love arc carries unfinished business |
| 6 | *Lord of Chaos* | Regulatory offensive at full strength; *let the Lord of Chaos rule* = deliberately fragmenting the mesh; Stefan publicly identified with the centralizing direction |
| 7-8 | *Path of Daggers* / *Winter's Heart* | Wanjiru's arc; standards body; first legislative win; Helvetia begins strategic pivot |
| **Final** | *A Memory of Light* | The last battle; sealing the Bore; legislative + architectural lock-in for local-first sovereignty; **Priya's epoch-incompatibility close** = Nynaeve lifting the taint analog |

Bobiverse threading happens in Books 3-6 when deployments begin spinning off. By Book 6 there are enough diverged instances that Priya's schema work is the series' structural spine. Long Now thread runs across all books with Wanjiru as the anchor character.

## 4. Cast (with character-sheet anchors)

The Sunfish-1 crew of twelve, plus the rival cast, plus mission-fulfillment crew the consortium provided. Each named character has a full or minor sheet; this section gives one-paragraph summaries with WoT roles and the key beats Vol 2+ asks of each character.

### 4.1 Sunfish-1 crew — Anna picked the technical contributors

**Anna Yusupova — Mission Director (Moiraine Damodred analog).**
[Full sheet: `dr-leader-mission-director.md`]
Uzbek-Russian; 47-52; AARI St. Petersburg; second-attempt polar lead after the Stefan-mission failed her. *Operator's avatar* — she chose the architecture by reading the paper, not by building it. First-person narrator throughout the series; her retrospective narration is itself the Long Now answer at the human scale (*she's alive, she remembers, she's telling it*). Day-20 anchor scene is hers. Joel-love-arc subject (slow to return).

**Joel Reyes — Principal Architect, Sunfish-1 senior crew engineer (Rand al'Thor analog).**
[Full sheet: `joel-reyes-principal-architect.md`]
Filipino-American; mid-50s; former US Navy nuclear engineer on USS Sunfish SSN-649 (decommissioned 1998); paper author; named the architecture after his first submarine. The Dragon-who-hates-it. Saidin channeler — naval-nuclear discipline is the Three Oaths analog. R1 BLOCK night = founding act of grace. Anna's recruit; in love with Anna across the series.

**Priya Iyer — Lead Instrumentation Engineer + Sunfish OSS schema-migration co-author (Nynaeve al'Meara analog).**
[Full sheet: `priya-iyer-schema-migration.md`]
Indian Tamil; mid-late thirties; Bengaluru-based at mission time. Ch1 King-style victim (the 4:47 PM hospital bid disaster) → field-instrumentation engineer → Sunfish OSS contributor. Schema migration = Healing. *Says no until forced to act.* The R1 near-BLOCK (third-party-read race condition under partition) = her founding flashback. Final-book epoch-incompatibility close = Nynaeve lifting the taint.

**Wanjiru Kamau — Relay Operations + Sunfish OSS security-architecture co-author (Egwene al'Vere analog).**
[Full sheet: `wanjiru-kamau-security-policy.md`]
Kenyan Kikuyu; mid-thirties to early-forties; Nairobi-based. M-PESA-adjacent ecosystem background → Sunfish OSS contributor. Saidar channeler — the discipline that lets her channel is the M-PESA-formed pragmatism (*data is livelihood*). R1 BLOCK on key compromise (revocation-broadcast race) = founding flashback. *The Long Now character* — thinks in decades; arc deliberately builds toward her own dispensability. Eventually chairs the standards body; final-book legislative lock-in is her arc's resolution.

**Sabina Rahman — Logistics & Procurement Officer; connectivity-gradient practitioner (Mat Cauthon analog).**
[Sheet at `_minor-characters.md` § "Sabina Rahman"; expansion deferred to concept-note-driven need]
Bangladeshi; 35-42; Grameen / BRAC microfinance lineage. *Practitioner-of-record* — her Grameen-region requirements *shaped* Sunfish's offline-first profile. On the boat to validate the architecture against actual deployment context. Her tic: paper backups (*Grameen taught her not to trust networks she could not see*).

**Diego Vargas — Senior Technical Specialist (Perrin Aybara analog).**
[Sheet at `_minor-characters.md` (under "Senior Technical Specialist") + character sheet `senior-technical-specialist.md`; expansion deferred to concept-note-driven need]
Argentine; IAA institutional polar memory (continuous since 1904); retiring to San Martín de los Andes after the mission. Hero of competence in the leak event (replaces the original death-scene); the 4,017 photographs become life-affirming.

**Hiroshi Nakamura — Chief Scientist (Loial analog).**
[Sheet at `_minor-characters.md` § "Dr. Hiroshi Nakamura"; expansion deferred]
Japanese; 50-57; NIPR (National Institute of Polar Research, Tokyo) / Showa Station credentials. *The calmest man on the manifest.* Knows where the prior architectures are buried.

**Maria Santos — Mission Medical Officer (Min Farshaw analog).**
[Full sheet at `maria-santos.md`; Vol 2 series-arc layer expansion deferred]
Brazilian. Sees what others miss; her *viewings* are diagnostic, not mystic — reads bodies and behavior with clinical precision. Medical-officer as moral register.

### 4.2 Mission-fulfillment crew (consortium picked; lighter treatment)

Four additional crew members the consortium required (vessel master + engineering crew + Argentine support detachment). Names will surface as specific scenes need them. The crew of twelve is locked in count; the four unnamed are operational, not architectural.

### 4.3 Rival cast

**Dr. Stefan Reinhardt — Principal Architect of TrustMesh / HelveSync (emerging Forsaken; fallen ally archetype).**
[Full sheet: `stefan-reinhardt-rival-architect.md`]
German; 54-58; AWI Bremerhaven postdoc with Anna ~2008-2012; toolkit author; mid-2010s corporate pivot to Helvetia Trust SA partnership. The engineer who didn't disclose the schema-migration limitation on Anna's prior failed mission (Path B with shadows of D — calibrated bet under institutional pressure not fully named). Off-page in Book 1; surfaces in Book 2 testimony; fully dramatized in Book 4 flashback; series-final partial reconciliation per PAO recommendation.

**Captain Astrid Hansen — Mission Director, rival Arctic mission (operational counterpart, not antagonist).**
[Full sheet: `astrid-hansen-rival-captain.md`]
Norwegian; 48-54; NPI / Norwegian Navy Reserve; *not Stefan's architectural ally* — captain executing her mission with the tools her consortium picked. Possible Book 5 scene: *the conversation that did not happen between Anna and Stefan happens between Anna and Astrid.*

**Helvetia Trust SA + Dr. Lukas Brandt — Swiss federated-identity firm + senior representative.**
[Full sheet: `helvetia-trust-corporate-sponsor.md`]
Zurich-domiciled mid-cap European tech firm; product is operationally excellent + architecturally centralizing. Lukas Brandt (SVP Strategy and Government Relations; Swiss-German; Swiss legal background; not an engineer; not a true believer; sees Stefan's partnership asymmetry clearly) is the human face for institutional scenes. The Forsaken's institutional vehicle.

## 5. Mission timeline — Sunfish-1 multi-segment design

Per the locked boat-power decision (`2026-05-04-vol2-boat-power-option-c-locked.md`): diesel/AIP multinational research submarine, mission redesigned with multiple under-ice segments instead of one continuous 56-day partition. Real-world precedent: IODP for surface drillships, Antarctic Treaty research stations, CERN — adapted to a research submarine in 2026-2030 fiction with mild normalization.

| Phase | Days | Activity |
|---|---|---|
| Transit south | 1-7 | Surface transit Punta Arenas → Drake Passage → ice edge |
| **Segment 1** | 7-21 | First under-ice deployment (~14 days submerged); Anna's day-20 partition realization scene lands here |
| Surface 1 | 21-23 | 2-day surface window: battery recharge + mesh reconnect; **first Forsaken reveal** (rival mission preliminary results land) |
| **Segment 2** | 23-37 | Second under-ice deployment (~14 days); architectural test beats distribute |
| Surface 2 | 37-39 | 2-day surface window: recharge + reconnect; **second Forsaken reveal** (rival mission concludes; Stefan's PR spin) |
| **Segment 3** | 39-49 | Third under-ice deployment (~10 days) — **mission climax**: leak-with-fire-cascade lands here; Priya's *impossible migration* climax beat lands here |
| Transit north | 49-56 | Surface transit back to Punta Arenas; cumulative architectural reveal |
| Final surfacing | Day 56, 04:41 local | Punta Arenas. **Cumulative Forsaken reveal lands here** (full scope of what the centralizing direction did during the mission becomes legible) |

The rival mission (Stefan + Astrid + Helvetia) launches 2-4 months before Sunfish-1. By the time Sunfish-1 surfaces from Segment 1, the rival mission has had its first surfacing event and the preliminary results are public. By Sunfish-1's Segment 2 surfacing, the rival mission has concluded; Stefan is publicly framing the results as a success. Cumulative comparative reveal — what each mission actually demonstrated, what each architecture actually held — lands across Sunfish-1's three surface windows + final Punta Arenas arrival.

**Existing The Crossing chapter (Vol 1 closing) needs a revision pass** to reflect the multi-segment design; this is a separate PR when CO is ready, not gated on Vol 2 concept-note draft.

## 6. Story shape — chapter architecture

### 6.1 The 60/40 mission-frame vs flashback ratio (per chapter)

Each Vol 2 chapter is approximately:
- 60% **mission-present** narration — Anna's first-person account of events on the boat or at the consortium ports
- 40% **backstory flashback** — earned by the mission-present beat; ends back on the boat with the architectural lesson now embodied (*and that is why on day 14, when X happened, we did not lose the mission*)

The ratio is approximate, not strict. Some chapters are fully mission-present (the day-20 scene; the leak event). Some chapters lead with flashback (Anna's prior-failure interior). The 60/40 is the average across the book.

### 6.2 The captain-asks-engineer dialogue engine

Technical exposition in the book happens primarily through **Anna asking Joel what's happening; Joel explaining as he debugs.** The pattern is the standard pattern in technical-thriller fiction (*Hunt for Red October*, *Master and Commander*, *Moby Dick*'s Ishmael). The architectural complexity emerges through *what the captain asks* and *what the engineer answers*.

Anna credibly does not know what is happening at the architectural layer — she chose the architecture by reading the paper, not by building it. Joel does know, because he wrote it. The asymmetry is the engine. Architectural detail at audiobook tempo flows through their dialogue.

### 6.3 The three-act structure within Book 1

| Act | Days | Content |
|---|---|---|
| **Act I** | Days 1-21 | Departure + transit south + Segment 1; first under-ice realization (day-20 scene); first surface and first Forsaken reveal. *Establishes:* Anna's narration register; the crew; the architecture in operation; the rival mission's existence |
| **Act II** | Days 22-42 | Segment 2 + interim Surface + start of Segment 3; subsystem-by-subsystem testing through Anna-Joel dialogue; second Forsaken reveal; Sabina's use-case validation; Hiroshi's data work; Diego quietly essential; Priya's caution audited; Wanjiru's relay operations across both surface windows |
| **Act III** | Days 43-56 | Segment 3 climax (leak + fire cascade) + Priya's impossible migration + final ascent + transit home + final reconciliation at Punta Arenas; cumulative Forsaken reveal lands here |

### 6.4 The Anna-Joel love arc as series register

The love arc is **explicitly not Book 1's primary emotional spine.** Book 1's primary emotional spine is the architectural maiden voyage + Anna's command authority + the prior-failure trust hardening. The love arc is a secondary register that becomes legible to the audience over the book without being foregrounded.

Book 1 beat for the love arc: *Joel is in love; Anna registers it during Segment 2; neither acts; the discipline holds through the leak event in Segment 3.* The disclosure happens in Book 3.

Per the love-arc layer in both character sheets: not Hollywood, not a kiss-in-a-snowstorm, mid-50s mature register, disclosure is a conversation not a scene.

## 7. Sample story arcs — eight chapters, each carrying one architectural claim

This is the spine of the audiobook listenability fix. Each chapter is a **verification-gap meeting reality** — an architectural claim from Joel's paper exercised on the boat for the first time, with the relevant contributor present, and the lesson embodied through scene rather than stated through specification.

The arcs below are working candidates; specific ordering, emphasis, and titling will surface during drafting. Each chapter is roughly 8,000-10,000 words (an audiobook hour). The book targets 16-20 chapters total.

### Arc 1 — *The Day-Twenty Realization* (Anna's structural moment)
**Architectural claim:** the local store is authoritative under partition because there is nothing else.
**Setting:** mid-Segment-1, ~Day 14 from departure (which is ~Day 7 of sustained under-ice operation). Anna queries the local store for a colleague's prior write — a piece of provenance from before the mission. The system answers locally without ambiguity, because it cannot do otherwise. *Everything I am recording right now is only here.* The recognition. The compounding recognition (*This is what Joel built*). The emotional landing: not triumph; recognition.
**Length target:** ~6,000 words (a tighter chapter; the realization is the whole event).
**This chapter is a Book 1 structural requirement.**

### Arc 2 — *The Recruitment Interview* (Joel-Anna founding flashback)
**Architectural claim:** the architect's response to being told he was wrong is what makes the architecture trustworthy.
**Setting:** flashback to the months before mission departure. Anna's vetting interview with Joel via video call. Anna has read the paper and the council review; she has questions specifically designed to surface whether Joel will tell her the truth when it matters. Joel's R1-BLOCK-rewrite admission. The exchange that convinces Anna: *I missed it. The original protocol assumed condition X that doesn't hold under sustained partition. Klett was right. I rewrote it.* No softening; no defense; no deflection. The structural inverse of what failed her last time.
**Length target:** ~9,000 words.

### Arc 3 — *Joel's Sunfish* (the naming reveal)
**Architectural claim:** the architecture's name carries the discipline that makes it work.
**Setting:** mid-Segment-2 surface window. Quiet conversation between Anna and Joel during the 2-day reconnect period. Joel discloses the name's origin — USS Sunfish SSN-649, decommissioned 1998, his first submarine. *The discipline that runs through the architecture got formed there.* Anna recognizes what she had been registering since she read the paper. Long Now thread quiet beat: what the boat-that-no-longer-exists left in him.
**Length target:** ~5,000 words (intimate; conversational).

### Arc 4 — *The Schema That Should Not Migrate* (Priya's impossible-migration climax)
**Architectural claim:** schema migration is Healing — preserving identity through transformation.
**Setting:** Segment 3, mid-mission. Operational conditions force a schema change Priya would have refused in lab review. Anna asks Priya to authorize on operational grounds. Priya says no, then says how-to-do-it-anyway, then walks Joel through the migration in real time. Two near-failures during the read-confirmation cycle that Priya's three-pass discipline catches. The migration succeeds. The post-migration recognition: the architecture worked because Priya's caution was built into it as a constraint, not because the mission followed her caution as a rule.
**Length target:** ~10,000 words (the technical density is high; the chapter earns the length).

### Arc 5 — *The Compromised Relay Holds* (Wanjiru's structural moment)
**Architectural claim:** security architecture designed for political fragility holds against environmental degradation; the worst case in the political dimension shares its shape with the worst case in the physical dimension.
**Setting:** Segment 3, during and after the leak-and-fire cascade. Comm node damage threatens the gossip layer that propagates revocations. Sensor compartment loss threatens the audit trail. The cascading damage tests whether key-management decisions made during stable conditions can survive the boat's worst hour. They do. The architecture Wanjiru built for revocation-under-coercion gives the system enough redundancy to operate in the degraded mode. The retrospective recognition: *the security model that defended against political coercion turned out to defend against environmental degradation. The two threat models had a deeper structural similarity than either of us had named.*
**Length target:** ~8,500 words.

### Arc 6 — *The Crossing* (the leak event; Diego's competence; Joel's protective act; Anna's command)
**Architectural claim:** the architecture is adequate, not heroic; the procedure is the heroic act.
**Setting:** Segment 3, the leak-and-fire-cascade. 0317 leak alarm; 0319 cabin-to-bridge transit; 0321 assessment; 0342 compartment isolation order. Diego's polar-operational experience. Joel's nuclear-Navy training firing against his own architecture. Anna's command authority unsentimental. The 4,017 photographs. The Spanish letter to María Elena (recovery, not death notification). Diego retiring to San Martín de los Andes earned through what he did. *This chapter inherits beats from the existing Vol 1 closing chapter `The Crossing` — substantial revision pass required.*

**The instrument-leak protective beat (CO direction 2026-05-05; refined 2026-05-05):** The leak originates from a malfunctioning instrument — small leak, high stakes, in a confined access compartment behind equipment. The alarm fires and Joel's instinct from thirty years of nuclear-Navy training fires before any cognitive part of his mind has caught up. He moves toward the leak. **He pushes Anna aside on his way past her.** The contact is physical, brief, instinctive — the only physical contact between them in Book 1. **He shuts the bulkhead door behind himself and locks it from his side.** Then he turns and faces Anna through the porthole window of the bulkhead door. **The look says, without a word, everything that his discipline has prevented him from saying since the recruitment interview.** Anna receives it. Her command authority holds; the bridge is watching her. He turns and goes to work. Submarine leaks resolve in minutes either way — he contains the instrument failure, drains the residual water, reports clear, emerges. The boat is fine. *No one comments because nothing went wrong.* Only Anna and Joel know what the door meant, what the touch meant, what the look meant. The recognition compounds privately for the rest of Book 1; the Book 3 disclosure is not about declaring feelings but about acknowledging *what happened on Day 47* — specifically, the touch in the passageway and the look through the glass. See the love-arc layers in `joel-reyes-principal-architect.md` and `dr-leader-mission-director.md` for full treatment.

**Length target:** ~12,000-13,000 words (the climax; Vol 1's existing closing chapter is the source material; the instrument-leak beat adds ~1000-1500 words within the chapter — the eleven minutes Joel is behind the door are the chapter's emotional center, sustained through Anna's bridge-watch silence, the comms log, and the eventual all-clear).

### Arc 7 — *The Aftermath of a Mission That Once Was* (Anna's prior-failure interior; flashback)
**Architectural claim:** trust hardens in specific shapes; the inverse of betrayal is disclosure-without-compulsion.
**Setting:** flashback fragments distributed across Book 1. The Stefan-mission cut short. The colleague's mix of acknowledgment and minimization. Anna ending the working relationship. The five years between then and now. *The book does not dramatize Stefan in person in Book 1 (he is fully dramatized in Book 4); the flashback fragments are Anna's interior.*
**Length target:** ~5,000-7,000 words distributed in fragments across multiple chapters; not a single chapter.

### Arc 8 — *Punta Arenas Surfacing* (the cumulative Forsaken reveal; mission close)
**Architectural claim:** the maiden voyage proved the architecture; the contest over its meaning has only begun.
**Setting:** Day 56, 04:41 local time, Punta Arenas dock. First external contact reveals: while the boat was under, the first formal regulatory challenge to local-first architecture was filed; Stefan's mission concluded with publicly-favorable results that the architecturally sophisticated will see were partially compromised; Wanjiru's standards body has issued a preliminary response. The mission's success and the world's response converge. The book ends with the architecture proven and the real contest beginning. Anna writes the staff history (the device that produces Book 1).
**Length target:** ~7,000 words.

### Total target

8 arcs at the lengths above = ~62,500-68,500 words for the structural chapters. With supporting chapters, transitions, the Spanish letter scene, the surface-window reveals between segments, and inter-act material, **Book 1 total = ~80,000-100,000 words / ~9-10 hours audiobook.** Per the audiobook listenability target.

## 8. Length and format

- **Print word count target:** 80,000-100,000 words (Book 1)
- **Audiobook duration target:** ~9-10 hours (at typical narrative-non-fiction tempo of ~9,000 words/hour)
- **Chapters:** 16-20, each 4,000-12,000 words (variable by chapter type)
- **Series total:** 8 books at similar length per book = ~640,000-800,000 words across the series; ~70-80 hours audiobook total
- **Comparison points:** *The Bobiverse* book 1 (*We Are Legion*) is ~92,000 words; *The Wheel of Time* book 1 (*The Eye of the World*) is ~310,000 words. Vol 2 sits comfortably in the trade-novel range, well below WoT's expansive scale; this is intentional for audiobook listenability.

## 9. Audiobook listen-test plan — proof-of-concept chapters

Before committing to the full Book 1 draft, **two chapters render through Kokoro for actual listen test.** This is the cheapest possible validation that the new format works at audiobook tempo.

**Chapter 1 — *The Day-Twenty Realization* (Arc 1 above; ~6,000 words / ~40 minutes audiobook).**
Tests whether Anna's first-person mission-frame voice lands. Tight scene; one location; single character; emotional realization at the chapter's center. If this listens well, the mission-frame voice is validated. If it does not, the issue is identifiable to the narrator-voice choice itself.

**Chapter 2 — *The Recruitment Interview* (Arc 2 above; ~9,000 words / ~60 minutes audiobook).**
Tests whether the dialogue-engine for technical exposition works. Two characters; sustained back-and-forth; technical content delivered through Anna's questions and Joel's answers. If this listens well, the captain-asks-engineer pattern is validated as the audiobook-tempo solution. If it does not, the issue is identifiable to the dialogue-engine choice.

**Listen-test protocol:**
1. Draft both chapters end-to-end; render through `build/audiobook.py` (Kokoro on Mac); produce the ~100-minute listening sample
2. CO listens uninterrupted (not skim-reading; full audiobook attention; ideally on a walk or commute)
3. CO returns one of three verdicts:
   - **Both land:** proceed to full Book 1 draft using the validated format
   - **One lands, the other does not:** identifiable to a specific structural choice; revise that aspect; re-test
   - **Neither lands:** the format itself needs structural rework; back to concept-note revision

**Estimated drafting time for the two proof-of-concept chapters:** with the technical-book-writer agent dispatched at /effort xhigh on Opus, ~2-4 hours of agent time per chapter. Total: ~4-8 hours of agent time + CO listen-test time.

**This is the cheapest validation possible. The two-chapter spike answers the question that drove this whole rework — *does the story-first restructure listen better than the spec-spine?* — with an actual audiobook artifact, not with prediction.**

## 10. Open items + deferred work

### 10.1 Locked-elements doc deltas to propagate

The `vol-2-concept-locked-elements-2026-05-04.md` companion doc lists three open items. Two are now resolved by this concept note:

- ✅ Boat power source — locked (option C; multi-segment diesel/AIP; see `2026-05-04-vol2-boat-power-option-c-locked.md`)
- ✅ Prior-failure framing path B — confirmed by CO this session
- ✅ Unnamed-colleague disposition — locked as competitive parallel mission with Reinhardt + Helvetia (per CO direction); colleague is dramatized in Book 4 and present off-page across the series

The locked-elements doc can be updated to reflect closures in a separate small PR; not blocking.

### 10.2 The Crossing revision pass (Vol 1 closing chapter)

The existing `chapters/closing/the-crossing.md` reads as a single-dive 56-day mission with Anna-as-architect framing. Needs revision pass:
- Multi-segment dive structure (3 under-ice segments + 2 intermediate surface windows)
- Anna's relationship to the architecture: read the paper and bet on it (not built it)
- Diego survives the leak event (not death scene)
- Spanish letter reshapes from death notification to recovery letter
- Various existing voice samples that say "I helped build this architecture" → revised to "I read this architecture's paper" or similar
- Estimated effort: ~3-5 hour revision pass on a ~4,400-word chapter

This is a separate PR when CO is ready; not blocking Vol 2 concept-note draft.

### 10.3 Vol 1 preface signature change

Per the locked-elements doc and the corporate-sponsor framing: change the in-frame Vol 1 preface signature from `— Anna Yusupova` (current per PR #88) to `— Joel Reyes` to align with the authorial frame. One-line edit; trivial PR; not blocking.

### 10.4 Supporting character sheet expansions (Sabina, Diego, Hiroshi, Maria)

Currently at minor-character depth. Concept-note drafting will surface where deeper character work is actually needed; PAO recommendation is to expand sheets *driven by* concept-note needs rather than speculatively.

### 10.5 Epigraph device

Per `vol-2-long-now-memory-thread-2026-05-04.md`: recurring chapter epigraphs from in-universe documents (Joel's engineering papers, Anna's mission logs, council review dissenting opinions, **the Forsaken's own position papers**). The Forsaken position papers as in-world documents are a PAO deliverable — they need to be plausible and sincere. PAO will draft 2-3 exemplars before chapter drafting begins so the voice is consistent.

### 10.6 Book 4 (Aiel Waste) deep-lore preparation

The Stefan-flashback book is structurally locked in series-arc terms but its specific scene structure is not yet drafted. Notes for that book's eventual concept note: the partnership collapse is the emotional center; the audience sees pre-pivot Stefan; the prior-failure mission is fully dramatized. Defer concept work until Book 1 lands.

### 10.7 Existing repo work that overlaps

Vol 1's existing 154k-word manuscript continues to ship as the canonical Joel Reyes paper. Phase 4 prune work (Phase 4a closed today; Phase 4b deferred per existing decisions) continues independently. Vol 2 work does not displace the existing manuscript; the two volumes coexist as paper-and-narrative pair.

## 11. Production sequence — what happens after this concept note clears

1. **CO review of this concept note.** Adjustments, redirections, additional locks. Estimated: one-two passes.
2. **Two proof-of-concept chapters drafted** (Arc 1 + Arc 2 from §7).
3. **Audiobook render + CO listen test.** ~100 minutes of audio.
4. **Verdict:** both land → full Book 1 draft; one lands → revise; neither lands → format revision.
5. **(If both land)** full Book 1 draft begins. Estimated ~16-20 chapters at ~8k words each; technical-book-writer agent at /effort xhigh on Opus producing first drafts; CO + PAO editorial pass; literary-board / council review at draft-complete; revision; final.
6. **Audiobook production for Book 1.** Same pipeline as Vol 1's ongoing audiobook work; Kokoro for narrative voice; Higgs for character voices when CO opts in.
7. **Vol 1 + Vol 2 ship as paper-and-narrative pair.** The existing 154k ms remains the reference paper; Vol 2 is the readable trade book; readers can choose either or both.

## 12. PAO action — immediate next step

This concept note is the synthesis CO requested. With CO confirmation, PAO is ready to:

- Update the locked-elements doc to reflect the closures recorded in §10.1
- Begin the Sabina/Diego/Hiroshi/Maria expansion *driven by* what proof-of-concept chapter drafting surfaces (not speculatively)
- Draft 2-3 Forsaken position-paper exemplars for the epigraph device
- Begin Arc 1 and Arc 2 drafting via the technical-book-writer agent (or chapter-drafter agent depending on CO's preferred dispatch pattern)

CO's call on which of these to start first. PAO recommendation: **Forsaken position-paper exemplars first** (they shape the voice for any subsequent chapter epigraphs), then **Arc 1 chapter draft** as the cheapest proof-of-concept test.

---

**End of Vol 2 concept note v1.** Awaiting CO review.
