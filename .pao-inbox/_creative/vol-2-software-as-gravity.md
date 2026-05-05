---
type: convention-doc
volume: 2
audience: chapter-drafter, technical-book-writer, future contributors
status: canonical (locked 2026-05-05; CO directive — Ch 2 listen-test verdict "still too technical" forced this canon)
related:
  - .pao-inbox/_creative/vol-2-archive-and-capture-convention.md
  - .pao-inbox/_creative/vol-2-anchor-bridge-sync-mechanic.md
  - .pao-inbox/_creative/series-arc-sunfish-trajectory.md
  - .pao-inbox/_creative/vol-2-concept-note-2026-05-04.md
  - chapters/book-2/CHAPTER-OUTLINE.md
---

# Vol 2 — Software as Gravity, Not Character

> **What this is:** the canonical structural framing for Vol 2's relationship to its own architecture. Sunfish is **gravity** — always there, always shaping the scenes, rarely explained. The chapters are about people, with the architecture as substrate.

> **Why this exists:** Ch 2 v3 (post-prose-pass; 7,256 words) listen-tested as "still too technical." The prior canon (concept-note §6.2) had positioned the captain-asks-engineer dialogue engine as *the* dialogue engine for Vol 2. This was wrong. The captain-asks-engineer engine is *one* engine among several; it should be the **install-engine** (used in Ch 4 to land partition-mode reality on the page) and selectively elsewhere when the architecture is genuinely the chapter's subject. **Most chapters lead with a different engine.** This doc names which engines, when, and why.

> **What this changes:** every chapter outline entry now carries a primary rail. Drafters write to the rail. The architecture appears as evidence, consequence, or substrate — rarely as subject. Captain-asks-engineer is demoted from default to selective.

---

## 1. The premise

**Sunfish is gravity.**

Gravity is always there. Gravity shapes how every body in the room moves. Gravity is rarely explained — *it's just what's there.* When you write a scene where two people walk across a deck, you don't pause to explain that the deck is held to the boat by gravitational force. The deck is there; the people walk; the gravity is implicit in every step.

Sunfish should appear in Vol 2 the same way. The architecture is in the room. Every conversation happens because Anchor is recording it; every decision propagates because the gossip protocol moves it; every preservation question lands because the Bridge holds (or doesn't) what reaches it. **The architecture is what makes the scene possible — not what the scene is about.**

The scenes are about people: trust, prior betrayal, career-cost, mid-life reckoning, institutional politics, family, survival under stress, the contest over what a record means.

When chapters drift into spec voice — explaining how the lease protocol works for the third time, walking the reader through the GC tier classification at depth, enumerating the failure modes — the chapter has stopped being about the people and started being about the gravity. **That is the failure mode this canon corrects.**

## 2. The six primary rails

Each chapter leads with **one** of these six rails. The architecture appears in the chapter as gravity — substrate, consequence, evidence — but is not the chapter's subject. A chapter's secondary rail can carry minor weight, but the primary rail determines voice, scene structure, and what the reader remembers.

### Rail 1 — Trust and prior betrayal (Anna's arc)

**Core question:** *How do you lead again after being failed by someone you trusted?*

Anna systematically tests each senior hire against specific failure archetypes from the prior mission. She is hyper-attuned to omission, spin, *technically true / operationally a lie* in every report. Her crises are about choosing whether to trust a recommendation from someone who just admitted to a mistake before being asked.

How the architecture appears: as the **arena** where honesty vs self-protection plays out. Conversations become *Tell me exactly what you did when you realized you were wrong*, not *Explain the protocol again.*

### Rail 2 — Career-cost and aging out (Joel's arc)

**Core question:** *What does it mean to build something that doesn't need you anymore?*

Joel debates whether to go on the boat at all vs staying home to shepherd the OSS community. Younger engineers (Priya, Wanjiru) challenge his instincts, not just his math. Discussion of who inherits Sunfish, what *maintainer succession* looks like, whether he's willing to let others make changes he wouldn't.

How the architecture appears: as **backstory**. The Round-1-BLOCK rewrite is a thing he did four years ago; the current drama is about handing over the keys, not proving he's right.

### Rail 3 — Class / region / institutional politics (Priya and Wanjiru)

**Core questions:** *Whose failure gets blamed?* and *Whose definition of "correct" wins?*

Priya treated as *just the instrumentation person* by European/US institutional reps while she's actually the schema-migration decider. Wanjiru in standards meetings where regulators want *compliance-friendly local-first* that quietly centralizes power. On the boat: a decision that will harm some users/deployments to protect others; argue about who gets sacrificed.

How the architecture appears: as **weapon or shield** in political fights. Migration and key-management rules become categories; whoever defines the category wins.

### Rail 4 — Mission as survival story

**Core question:** *What do people do under sustained, lethal stress?*

Resource shortages: oxygen margins, power, spare parts. *If we run this recomputation, we brown out the lab.* Physical risk: a leak, a stuck hatch, an EVA under ice. Crew dynamics: fatigue, conflict, micro-mutinies, people cracking or stepping up.

How the architecture appears: as **binary** — *it held* / *it didn't*. Explanations are minimal, contextual (*it did what he said it would*) and secondary to *is someone going to die in this scene.*

### Rail 5 — Grief, family, and memory (Long Now thread)

**Core questions:** *What happens to my data when I die?* and *What do we owe the dead?*

Surface-window calls with parents, partners, kids; implied futures if they don't come home. Later volumes: handling the data of someone who didn't come back. Priya and Wanjiru debating what *inheritance* means in a local-first world.

How the architecture appears: as the **literal answer** to what happens to memory. Schema migration becomes *how we carry someone's memories into a new container without losing them.* Key management becomes *who has the right to open their archive.*

### Rail 6 — Rival mission and institutional capture (Stefan / Helvetia thread)

**Core question:** *What happens when someone you once trusted builds the rival platform?*

Anna and Stefan's past and present in short, loaded encounters: conferences, hearings, media commentary. Astrid and rival crew hearing about Sunfish-1, treating it as competition, rescue hook, or cautionary tale. Internal arguments at the consortium: *Do we hedge by adopting some of Helvetia's model?*

How the architecture appears: in terms of **who can shut you off**. *Federated trust vs pure local-first* expressed in money, audits, regulatory capture, job security, public narrative — never in diagrams.

## 3. Per-chapter rail assignment (LOCKED 2026-05-05)

Every chapter leads with one rail. Secondary rail noted where useful.

| Chapter | Primary rail | Secondary rail |
|---|---|---|
| Ch 1 — Departure | **Trust + prior betrayal** | Mission as survival (atmosphere) |
| Ch 2 — Recruitment Interview | **Trust + prior betrayal** | — |
| Ch 3 — Drake Passage | **Mission as survival** | Class/region politics (Sabina + Diego) |
| Ch 4 — First Submersion | **Mission as survival** | (this is the captain-asks-engineer install-chapter; see § 5) |
| Ch 5 — Day-Twenty Realization | **Grief, family, memory** | — |
| Ch 6 — First Surface, First Forsaken Reveal | **Trust + prior betrayal** (Wanjiru's exception-refusal as discipline) | Rival mission (Stefan name surfaces) |
| Ch 7 — Joel's Sunfish | **Career-cost + aging out** | Grief/Long Now (the boat-that-no-longer-exists) |
| Ch 8 — Second Submersion | **Class/region/institutional politics** (Sabina's validation) | Mission as survival |
| Ch 9 — Sync Daemon Under Drift | **Career-cost + aging out** (Priya's question Joel hadn't asked himself) | — |
| Ch 10 — Aftermath of a Mission That Once Was | **Trust + prior betrayal** (rail's deepest interior chapter) | — |
| Ch 11 — Second Surface, Second Forsaken Reveal | **Rival mission + institutional capture** (Wanjiru cross-check race) | — |
| Ch 12 — Beginning of the End | **Mission as survival** (discipline tightening; conditional-preservation plant) | — |
| Ch 13 — The Schema That Should Not Migrate | **Class/region/institutional politics** (Priya as decider) | Career-cost (Joel walking her direction) |
| Ch 14 — The Crossing | **Mission as survival** (binary tech: held / didn't) | Trust + prior betrayal (Joel's protective beat) |
| Ch 15 — The Compromised Relay Holds | **Class/region/institutional politics** (security architecture's same political reading) | Career-cost (Wanjiru's institutional thinking forming) |
| Ch 16 — Final Ascent | **Mission as survival** (post-climax adaptation) | — |
| Ch 17 — Transit North | **Rival mission + institutional capture** + **Career-cost** (joint anchor) | Trust + prior betrayal (the staff-history-conversation) |
| Ch 18 — Punta Arenas Surfacing | **Rival mission + institutional capture** | Trust + prior betrayal (the Stefan exchange) |

Five of the six rails get substantial chapter ownership. **Grief/family/memory** is anchored by Ch 5 plus light distribution across surface windows + the Spanish-letter beat in Ch 17. The captain-asks-engineer dialogue engine is the install-chapter for Ch 4 and selective elsewhere; it is no longer a rail.

## 4. Scene-types that are not about software

Concrete templates that drafters can reach for. Sunfish appears as context only.

### 4.1 Performance review under pressure

Anna and a crew member after a near-miss: *Tell me why you made that call.* The tech reason is one paragraph; the emotional fallout is the rest. Use after Ch 14 leak event; Wanjiru's relay decisions during cascade.

### 4.2 Confession scene

Someone admits a mistake before it blows up (or after it already did). Sunfish is the problem or the witness; the real question is whether they are forgiven or sidelined. Joel's R1-BLOCK admission in Ch 2 is a confession scene structurally — Anna's frame around it should foreground the confession-vs-consequence question, not the protocol detail.

### 4.3 Family call

Short surface-window call: a parent worrying, a child asking simple questions, partner not saying what they really fear. Tech exists as **lag, glitches, delayed audio, dropped frames** — not as explanation. Use during Surface 1 (Ch 6), Surface 2 (Ch 11), final Punta Arenas (Ch 18).

### 4.4 Quiet watch

Two people on late shift together: they talk about why they came, what they're ashamed of, what they want next. Sunfish hums in the background; maybe a minor alert injects a line of work, then they go back to talking. Use mid-Segment-2 (Ch 9 or Ch 10); Ch 16 final-ascent (Anna and Joel on a transit watch); the night before Ch 14's leak event.

### 4.5 Council / boardroom argument

Off-boat chapter: Wanjiru vs regulators, Joel vs funders, Anna vs risk committee. Use **simple architectural metaphors to win or lose political fights**. Ch 11 Wanjiru's cross-check race could carry one such scene. Ch 17 transit-north could carry the regulatory-filing-drafting scene as institutional argument.

## 5. The captain-asks-engineer dialogue engine — demoted

Per concept-note §6.2 (now updated by this canon doc): captain-asks-engineer was framed as *the* dialogue engine for Vol 2's technical exposition. **This canon supersedes that framing.**

### What captain-asks-engineer is now

- **The install-engine for Ch 4.** First Submersion is where the architecture's operational reality lands on the page. The chapter uses captain-asks-engineer at full altitude: Anna asks; Joel explains; the reader installs partition-mode behavior, the local-store-as-only-reality fact, the gossip-protocol-dormant beat. **This chapter is unchanged by the gravity canon.** Captain-asks-engineer is the right engine here.
- **Selectively elsewhere.** A chapter that *is* genuinely about the architecture (e.g., Ch 13's schema migration; Ch 17's forensic-finding triangulation) can use captain-asks-engineer for one or two technical exchanges, then pivot to the rail. The engine is a tool, not the chapter's spine.

### What captain-asks-engineer is NOT

- **The default engine.** Most chapters lead with a different engine — the rail's engine (e.g., trust-test interrogation; mid-career-reckoning conversation; political-pressure council scene; family-call lag-and-glitch register; quiet-watch confession).
- **The pacing default for Anna's interactions with Joel.** Where Anna and Joel are in a scene together, the default is *what is the human stakes question between them right now* — not *what is the next architectural detail to surface.*

### The four-question scene checklist (drafter discipline)

Before writing or revising any scene:

1. **What is the non-technical stakes question here?** Name it in one sentence. Examples: *Is he the kind of man I can forgive?* / *Is she willing to risk her career for this?* / *Who gets blamed if this goes wrong?* / *Will the institution recognize what just happened?*
2. **What changes in relationships by the end of this scene?** A scene where nothing relational shifts is usually a scene that should compress to a sentence in the surrounding narration.
3. **Can I show the tech via outcome (what fails / what holds) instead of description?** Default: yes. Push the tech off-page; let the reader feel what it does.
4. **Who is driving the scene?** *Anna alone with X* / *Anna + supporting character vs. external pressure* / *one character interior at length* — not *Anna prompting Joel to explain Sunfish.*

When all four answers are sound, the scene leads with the rail. When one or more is unclear, the chapter has drifted into spec voice; revise.

## 6. Ch 2 v4 — the redraft target

Ch 2 v3 (post-prose-pass) listen-tested as *still too technical*. This canon now mandates a fourth redraft.

**Primary rail:** Trust + prior betrayal. Anna's chapter-load is *what kind of man wakes up the morning after Klett tells him he's wrong* — not *here's how the lease protocol works under partition*. The architecture appears as the **arena** where the trust-test plays out.

**Specific changes for v4:**

- **Compress all four substantive Q&A exchanges (GC, lease, Byzantine ops, ops layer)** to a single representative beat each, with Anna's interior reading of Joel as the dominant register. *He answered the question. He did not soften the answer. I made a note of how he had not softened it.* The technical content is *that he gave a correct, undefensive answer*, not *what the answer was*.
- **Foreground Anna's interior throughout the technical sections.** Where v3 has Joel explain the fence, v4 has Anna register *that he answered without reaching for the printout, that his voice did not change between technical clauses, that he had not looked at his notes since minute six*. The architecture is gravity; Anna's reading of Joel is the chapter.
- **The R1-BLOCK admission stays verbatim.** That is the chapter's load-bearing trust event. Everything around it can compress; the four sentences and the fifth are protected.
- **The yes/yes recruitment exchange stays.** The chapter ends on the exchange Anna selected him on.
- **The Day-14 close stays at v3 length** (~245 words after the Pass-2 review applied). The coda's job is to land present-tense weight, not to recapitulate.
- **The technical content collapses to ~30% of v3's load.** Word count target for v4: **~5,500-6,200 words** (down from 7,256). Audiobook target: **~33-37 min** (down from 43.5).

**Drafter discipline:** the chapter is a recruitment-as-trust-test. The technical questions Anna asks are evidence in that test. The reader must finish the chapter understanding *Anna selected Joel because of who he is when he is wrong* — not *Anna selected Joel because his lease protocol now uses monotonic clocks*.

## 7. How to redraft existing chapters under this canon

For chapters already drafted:

1. **Ch 5 (Day-Twenty Realization)** — already aligned; primary rail is grief/family/memory; the architecture is already gravity. **No major redraft needed.** Sentence-level prose-pass acceptable when listen-test verdict warrants.
2. **Ch 2 (Recruitment Interview)** — needs v4 redraft per § 6 above.
3. **All other Vol 2 chapters** — not yet drafted. Each chapter's first draft now writes to its primary rail per § 3; captain-asks-engineer is the install-engine for Ch 4 only.

For drafters dispatched from this point forward: **read this convention doc before reading the chapter outline.** The rail assignment is the spine; the outline entry's other fields are in service of the rail.

## 8. What this canon does NOT change

- **Architectural correctness.** The architecture is fixed (Vol 1 paper + the convention docs). The gravity framing is about *what's on the page*, not what's in the world.
- **Voice register specifications.** Anna's voice, Joel's voice, Wanjiru's voice — all unchanged by this canon. The voice spec applies regardless of which rail the chapter leads with.
- **Plot-binding metadata.** Each character's plot-binding bullets (per character-sheet § Book 1 plot-binding) still surface in their canonical chapters.
- **Forensic substrate, sync mechanic, OSS-funding-asymmetry, conditional preservation.** All canon. They appear in the chapters as *consequences and constraints* rather than as topics.
- **Captain-asks-engineer as install-engine.** Ch 4 retains this engine at full altitude. Selective use elsewhere (1-2 technical exchanges per technically-load-bearing chapter) is acceptable when the chapter is genuinely about the architecture.
- **Series trajectory (Sunfish → Trek-Computer).** Series-canon-only; never explicit in Vol 2 prose.

## 9. Cross-references

- **Archive + capture model + 2026 stack:** `vol-2-archive-and-capture-convention.md`
- **Sync mechanic + Wanjiru's triage role:** `vol-2-anchor-bridge-sync-mechanic.md`
- **Series trajectory:** `series-arc-sunfish-trajectory.md`
- **Per-chapter pattern + rail assignments:** `chapters/book-2/CHAPTER-OUTLINE.md`
- **Anna voice register:** `.pao-inbox/_creative/character-sheets/dr-leader-mission-director.md` § Voice register specification
- **Generator skill:** `.claude/skills/crew-log-style-entry/SKILL.md`

---

## Status

- **Locked 2026-05-05** per CO directive (Ch 2 v3 listen-test verdict "still too technical" forced this canon).
- **Supersedes concept-note §6.2** on captain-asks-engineer-as-default. Concept note's other content (story shape, frame ratio, three-act structure, love-arc layer) unchanged.
- **Ch 2 v4 redraft authorized** per § 6.
- **All future chapter drafts must consult this doc before drafting.**
