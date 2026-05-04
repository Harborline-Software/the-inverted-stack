---
type: concept-working-doc
date: 2026-05-04
author: PAO (capturing CO creative decisions across session)
audience: CO (continuity of decision record); future PAO sessions; whoever drafts the concept note
status: working — locked elements accumulating; one sub-question open before full concept-note draft
relates-to:
  - .pao-inbox/_creative/the-crossing-concept-note-2026-04-30.md (Vol 1 closing-chapter concept; pattern precedent)
  - .pao-inbox/_creative/character-sheets/ (existing character bios; will need expansion)
  - chapters/closing/the-crossing.md (existing Vol 1 closing chapter; Vol 2 inherits its mission frame)
---

# Vol 2 — *The Inverted Stack: The Sunfish-1 Mission* (working title)

## What this is

A working document capturing creative-session decisions about Vol 2 — a new book derived from but distinct from the existing 154k-word *The Inverted Stack: Local-First Nodes in a SaaS World*. Vol 2 reframes the book to address a real concern raised by audiobook listening: the current book's spec-paper spine produces dense detail that exhausts working memory across sustained listening. Vol 2 is the story-first response.

This doc accumulates locks from a long creative discussion. It is **not** the concept note itself; it is the precursor that ensures the concept note draft will be faithful to the decisions made.

## Premise

Vol 2 is **Anna Yusupova's first-person mission narrative** of the Sunfish-1 maiden voyage of the Sunfish architecture. The existing book (*Vol 1*) is canonically Joel Reyes's research paper that authorized the mission's tech bet — referenced by Vol 2's narrator but never reproduced. The relationship between the two volumes is the H.G. Wells convention: the prior monograph exists in the world; the narrator quotes from it where it earns its place; the narrator does not deliver the monograph in full. Same trick Wells used in *The War of the Worlds*.

The mission is the **maiden voyage** of Sunfish — real OSS, version 0.x, no prior deployments. Sunfish was named by Joel after his first U.S. Navy submarine, USS Sunfish SSN-649 (decommissioned 1998). The architecture has been built, tested, vetted, and reviewed (Vol 1 documents this); the mission is its first real-world deployment. Audience-facing tagline could be: *the architect built it, the council vetted it, the captain bet her crew on it, the mission tested it.*

## Locked elements

### Frame and authorship

- **Vol 2 is Anna's first-person narrative**; H.G. Wells convention preserved (Vol 1's existing out-of-frame "Note from the Authors" by Chris Wood + Claude continues to apply across both volumes)
- **Vol 1 = Joel's paper** (the existing 154k-word ms); canonical artifact in Vol 2's universe; referenced not reproduced
- **Vol 1's preface signature** changes from "— Anna Yusupova" (current, per PR #88) → **"— Joel Reyes"** to align with Joel as principal architect/author. The preface body (architect's voice; "I spent a year designing a local-node architecture...") doesn't change; only the attribution.
- Vol 2 narrator is Anna; Vol 2 has its own preface / framing language to be drafted

### Anna (Mission Director)

- Picked by the multinational consortium for **command excellence** — polar credentials (eighteen years at AAR Institute St. Petersburg, postdocs at AWI Bremerhaven and the Norwegian Polar Institute), cross-institutional relationships (kept alive after 2022 when other CIS scientists' Western relationships went silent)
- **Not** a Sunfish author and not a co-author. Read Joel's paper, recognized it answered her operational requirements, championed it within the consortium.
- **Second-attempt narrator.** A prior mission used a different architecture and **failed her**. The prior failure had a trust dimension: a colleague Anna had trusted recommended a research-grade local-first toolkit with a known schema-migration limitation that the colleague had quietly worked around but didn't disclose. The mission was cut short; crew came home alive; science objective lost; budget consequences; her professional reputation took a hit she's still rebuilding. Anna's loss of trust isn't just in the system — it's in *the engineer who recommended it.* That colleague is now off her professional radar.
- **Hardened vetting standard** for Sunfish-1: even more critical of who she lets in and who she trusts. Joel's blunt-and-unprompted disclosure pattern is the exact opposite of what failed her last time, which is why it earns her trust so precisely.
- Polar-exploration literary inheritance: Shackleton on *Endurance* after *Nimrod* — the second-time-around polar lead returning to the ice with everything she learned from the loss

### Joel (principal architect)

- **Principal author** of Joel's paper (Vol 1); named the architecture after his first submarine
- **Former U.S. Navy** Nuclear Machinist's Mate, Petty Officer Second Class (PO2 / E-5)
- Served aboard **USS Sunfish SSN-649** (Sturgeon-class fast attack, decommissioned 1998); 1990s service
- Post-Navy: civilian distributed-systems engineering; eventually authored the Sunfish paper
- Mid-50s; same generation as Anna
- Naval-nuclear operational discipline carries directly into his engineering: trust-but-verify, redundant indications, conservative actions, FAILED-conditions blocks + kill triggers in every architectural artifact, watch-handoff discipline mapped onto schema migration mechanics
- Behavioral signature in The Crossing already foreshadows this: independent diagnostics on local sensors only; doesn't trust cloud telemetry; reformatted his bunk laptop to a Linux distribution the consortium IT didn't approve; disclosed it to Anna in first watch handoff blunt and unprompted in the manner of a man who would rather you know than discover. **All of this is Navy-nuclear-trained discipline showing up in civilian systems work**, not generic engineer-skepticism.
- Contributed: lease coordinator (R1-blocked on partition-recovery, R2-cleared after Joel's rewrite); gossip protocol; FAILED-conditions discipline throughout

### Crew composition (architectural decomposition projected onto twelve human bodies)

**Anna picked (technical contributors):**
- **Joel Reyes** — principal architect; lease + gossip + sync; longest working relationship with Anna
- **Priya Iyer** — schema migration + sync protocol contributor (Vol 1 Ch13 + Ch14 areas)
- **Wanjiru Kamau** — security architecture + key management contributor (Vol 1 Ch15 area)
- **Sabina Rahman** — connectivity-gradient practitioner whose Grameen-region requirements *shaped* the offline-first profile; contributor by use-case authorship rather than code; on the boat to validate the architecture against actual deployment context

**Consortium picked (mission-fulfillment crew):**
- **Diego Vargas** — IAA institutional polar memory; the experienced polar voice on the bridge; retiring to San Martín de los Andes after the mission
- **Hiroshi Nakamura** — NIPR / Showa Station polar credentials
- **Maria Santos** — medical officer
- Plus four unnamed in The Crossing (vessel master + engineering crew + Argentine support detachment)

Anna had to **argue for her technical picks** because the consortium initially preferred standard polar engineering crew. She won the argument because she'd earned it.

### Council review (Vol 1 Part II)

- **The vetting that authorized first deployment.** Without the council review's R2 verdict + 15 conditions, the consortium wouldn't have signed off on Sunfish-1.
- R1 produced two BLOCK verdicts (per Vol 1 Ch5-10). The lease protocol BLOCK was Joel's. He rewrote it; R2 cleared with conditions.
- Anna's vetting of Joel included reading the council review and observing **how Joel handled the R1 BLOCK** — did he defend? did he listen? did he rewrite? His response is what convinced Anna he could be trusted at three in the morning under the ice.
- Vol 2 chapters: each is a verification-gap meeting reality, with the relevant contributor present to defend / debug / explain

### The boat (Sunfish-1)

- Multi-week submerged operation under the Filchner-Ronne ice shelf — realistically requires **nuclear propulsion**
- Working assumption (open question; CO override welcome): a **repurposed ex-Russian Navy nuclear research submarine**. Fits Anna's St. Petersburg biography, the multinational consortium with strong CIS-region scientific contribution, and Rustam's *kapitan 1-go ranga* commission (he's the Russian Navy peer who could have signed off on the asset's repurposing).
- Mission departure: 06:42 local time from Punta Arenas; dive 11:18 day 1; arrival back at Punta Arenas 04:41 on day 56 (per existing The Crossing).

### Central environmental event: leak with fire cascade

- **Replaces Diego's death scene** in The Crossing
- Primary event: water ingress in a non-watertight area, possibly a sensor compartment
- Secondary cascade: water reaches an electrical junction the design didn't account for → small electrical fire → suppression damages a sensor bank or comms node
- **Architecturally tests:** gossip degradation under sensor loss, partition tolerance, audit-trail integrity through equipment loss, partial-quorum sensor consensus, burst tolerance during emergency-comms spike, watch-reassignment under stress
- **Engages Joel's nuclear-Navy training acutely** — leak responses and fire procedures are deeply ingrained from Sturgeon-class boat days
- **Diego survives**, becomes hero of competence — his polar-operational experience pays off in compartment-isolation and managing crew through extended response. Retires to San Martín de los Andes at end of mission as planned, but now earned through what he did not earned by his death.
- **0317 / 0319 / 0321 / 0342 timestamp sequence** in The Crossing repurposes: leak alarm 0317; cabin-to-bridge transit 0319; assessment 0321; compartment isolation order 0342. The structural beat (Anna shifting from sleep to command in four minutes) is preserved.
- **Spanish letter beat** reshapes from death notification to recovery letter — Anna writes to María Elena from Belgrano explaining why Diego is delayed and what he did during the crisis. Same kitchen table, same Spanish-language choice, different message.
- **4,017 photographs** beat becomes life-affirming — Diego photographed *during* and *after* the leak response; Sofía sees what her grandfather did, not what was lost.

### Technical-exposition engine

- **Captain-asks-engineer dialogue.** Anna credibly doesn't know what's happening at the architectural layer; she asks Joel; he explains as he debugs. Architectural complexity emerges through their conversations and observed events — not through internal monologue.
- This is the standard pattern in technical-thriller fiction (*Hunt for Red October*, *Master and Commander*, *Moby Dick*'s Ishmael) and the strongest possible pattern for audiobook listenability.
- Each architectural beat: Anna asks Joel what's happening → Joel explains → reader/listener gets the architecture through dialogue at audiobook tempo.

### Backstory flashback architecture

Vol 2 is **mission frame + backstory flashbacks**, roughly 60% mission-present / 40% flashback. Each flashback ends back on the boat with the architectural lesson now embodied — *and that is why on day 14, when X happened, we did not lose the mission.*

High-leverage candidate flashbacks (priority order, will iterate during drafting):

1. **The selection interview.** Anna meets the consortium; realizes they're considering her for command not just for polar credentials but for her demonstrated track record of evaluating mission tech. The question they ask that confirms it. Her decision to accept.
2. **The prior failure.** The mission Anna lost; the colleague who didn't disclose; the moment she realized what had been hidden from her. The hardening that followed.
3. **Reading Joel's paper.** Anna's professional literature scan. The moment she recognized Sunfish answered her requirements. Her decision to contact Joel.
4. **The recruitment interview.** Anna's vetting conversation with Joel — she's read the council review, she's read his rewrite, she has questions specifically designed to surface whether he'll tell her the truth when it matters. His answers, including admitting the R1 BLOCK and explaining what he learned. The moment Anna decides to recruit him.
5. **The R1 BLOCK night** (Joel's POV via Anna's later reconstruction or Joel's recounting on the boat). The night Joel sat with Klett's verdict knowing the lease protocol had a partition-recovery hole. The hours between reading and starting the rewrite.
6. **The argument with the consortium** about Anna's technical-crew picks. Anna won; the consortium accepted. The argument shapes Vol 2's crew composition.

### Prior architectures Anna lived with (backstory texture)

Treated as **architectural-class-named, not real-product-named** — preserves editorial freedom and avoids straw-manning real systems.

- A centralized SaaS sync platform (geopolitical event cut off the vendor mid-mission; failure mode: dependency on commercial cloud connectivity)
- A research-grade local-first toolkit (the prior-failure mission; known schema-migration limitation undisclosed by the colleague who recommended it)
- An enterprise vendor system (assumed corporate-DLP infrastructure that doesn't exist on the ice)
- One or two more to be sketched during drafting

Each prior limitation becomes a problem Sunfish was designed to solve. Each maps onto a specific Vol 1 architectural decision Anna had read about in Joel's paper.

## Open question — boat power source

**Working assumption:** repurposed ex-Russian Navy nuclear research sub. Fits Anna's St. Petersburg biography + multinational consortium + Rustam's commission. CO override welcome.

If the boat is **not** nuclear, the equipment-failure surface is different (battery/diesel sub couldn't credibly stay submerged for 56 days under the Filchner-Ronne ice shelf without a surface refresh, which is hard to do under ice). Working assumption holds unless CO has a reason to override.

## What's still needed before full concept-note draft

1. CO confirmation on the boat-power working assumption (or override)
2. CO confirmation on the prior-failure framing — currently locked as path B (cut-short mission + colleague's failure of judgment)
3. Optional: any specific real-named or fictional-named prior-systems CO wants to anchor
4. Optional: Anna's prior-failure mission name / location / year — could be ~2-4 years before Sunfish-1 (e.g., 2022-2024 if Sunfish-1 is 2026)

Once those are settled (or accepted as drafting placeholders), the full **concept note** draft begins:

- Premise (long form)
- Diegetic mechanic (paper-as-artifact in Vol 2's universe)
- Cast (expanded character sheets for Anna, Joel, plus existing crew)
- Mission timeline (departure → 56 days → return; major beats placed)
- Story shape (mission-frame-vs-flashback ratio per chapter)
- Six to eight sample story arcs each carrying one architectural claim
- Length target (~80-100k word audiobook target; ~9-10 hour listening time)
- Audiobook listen-test plan (which two chapters to write first as proof of concept)

## Status

- Concept locks: this doc captures them
- Concept note: pending CO confirmation on the open question + path B framing
- Drafting begins after CO sign-off on the open items
