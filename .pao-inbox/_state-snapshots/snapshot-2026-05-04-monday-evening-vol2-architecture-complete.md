---
type: state-snapshot
date: 2026-05-04 (Monday evening)
author: PAO
reason: End-of-day handoff after a single creative session that produced the full Vol 2 architectural foundation. 31 PRs merged. Future sessions (or cold pickups) need a durable summary of where the work stands.
---

# State Snapshot — Monday 2026-05-04 evening (Vol 2 architecture complete)

## What this snapshot is

A handoff document for any session — PAO future, fresh PAO cold start, technical-book-writer agent, or human reader — that picks up the project after this Monday's creative work. The session produced the full Vol 2 architectural foundation; this snapshot is the entry point to that work.

## What landed today (PRs #74 → #104, 31 merged)

### Morning catchup (PRs #74-83)
Friday windown beacons archived; STT QC spike Phase 1 directive issued + Phase 2 follow-up; Phase 4a Block 1 closed (-360 words across 11 chapters via PRs #78-#82); Phase 4a Block 2 (Ch01) closed (-63 words); cast-swap audit beacon committed; closure decision + GitButler ref-resync.

### Council reviews + voice-pass plan (PRs #85-#89)
Council Round 1 (xhigh) on the voice-pass priority queue → BLOCK with 10 action items; PAO Round 2 plan applying all 10 → Council Round 2 (max effort) → PROCEED-WITH-RESERVATIONS with 3 P0 doc-hygiene fixes; state.yaml swept per Round 2 (#12 cut; #9, #10 conditional; priority-order rewritten); preface authorship disclaimer added (PR #88); preface voice cleanup (PR #89).

### Mermaid investigation + fix (PRs #92-#93 + Sunfish PRs #520, #526)
XO delegated the Mermaid → ebook rendering issue; PAO investigated; cross-repo status report; XO authorized Option B; PAO refined to Lua filter (Pandoc-native; no Node toolchain); kroki.io-based filter shipped to `build/filters/kroki-mermaid.lua`.

### Vol 2 creative session (PRs #94-#104)
**This is the body of the day's work.** A long creative discussion produced the structural foundation for a multi-book series rewriting *The Inverted Stack* into story-first form to address audiobook listenability concerns. Specifics in §2 below.

## Vol 2 architectural foundation — what exists on main

### Concept architecture
- **Vol 2 concept note v1** at `.pao-inbox/_creative/vol-2-concept-note-2026-05-04.md` — the synthesis artifact (~7,500 words, 12 sections); a future PAO session, technical-book-writer agent, or any reader can read it alone and execute against it
- **Locked-elements running index** at `.pao-inbox/_creative/vol-2-concept-locked-elements-2026-05-04.md` — closure-updated; serves as entry point pointing at all substantive Vol 2 artifacts
- **XO series-arc research** at `.pao-inbox/_creative/vol-2-series-arc-wot-bobiverse-2026-05-04.md` — WoT + Bobiverse hybrid; cosmological layer; 8-book series map
- **Long Now thread** at `.pao-inbox/_creative/vol-2-long-now-memory-thread-2026-05-04.md` — *what will happen to these memories when I die* as series throughline; Wanjiru as Long Now anchor; Day-20 partition realization scene as Book 1 structural requirement
- **Boat-power decision** at `.pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md` — diesel/AIP multinational research sub; multi-segment under-ice mission redesign

### Character sheets (full, in `.pao-inbox/_creative/character-sheets/`)
- `dr-leader-mission-director.md` — Anna Yusupova; Mission Director; Moiraine analog; existing CO-locked Vol 1 sheet + Vol 2 series-arc layer + Anna-Joel love-arc layer
- `joel-reyes-principal-architect.md` — Joel Reyes; Principal Architect; Rand al'Thor analog; former US Navy nuclear engineer USS Sunfish SSN-649; named the architecture after his first submarine; promoted from minor character; love-arc layer included
- `priya-iyer-schema-migration.md` — Priya Iyer; Lead Instrumentation Engineer + Sunfish OSS schema-migration co-author; Nynaeve al'Meara analog; Healing-channeler
- `wanjiru-kamau-security-policy.md` — Wanjiru Kamau; Relay Operations + Sunfish OSS security-architecture co-author; Egwene al'Vere analog; Saidar-channeler; *the* Long Now character
- `stefan-reinhardt-rival-architect.md` — Stefan Reinhardt; Principal Architect of TrustMesh / HelveSync (rival platform); German; Anna's former AWI postdoctoral colleague; emerging Forsaken; the engineer who didn't disclose
- `astrid-hansen-rival-captain.md` — Captain Astrid Hansen; Norwegian; rival mission captain; respectable counterpart, not antagonist
- `helvetia-trust-corporate-sponsor.md` — Helvetia Trust SA + Dr. Lukas Brandt; Swiss federated-identity firm + senior representative; the Forsaken's institutional vehicle

### Voice reference libraries (in `.pao-inbox/_creative/`)
- **`forsaken-position-papers/`** — Forsaken side voice library (3 exemplars)
  - `01-stefan-op-ed.md` — architect's voice; Heise Online October 2025
  - `02-helvetia-public-position.md` — corporate-PR voice; April 2026
  - `03-regulatory-filing.md` — institutional voice; February 2027 Working Group recommendation
- **`oss-architects-voices/`** — OSS side voice library (2 exemplars)
  - `01-annex-a-minority-opinion.md` — Wanjiru-drafted dissent appended to the Working Group filing; February 2027
  - `02-anna-mission-log-fragment.md` — Anna's first-person retrospective register; Day 28 mid-Segment 2

## What was decided this session (locked elements)

The full list lives in the locked-elements doc and concept note, but the key structural decisions:

1. **Vol 2 is a story-first restructure, not a rewrite of Vol 1.** The existing 154,337-word manuscript continues as canonical Joel Reyes paper.
2. **H.G. Wells convention** — Anna Yusupova narrates Vol 2; Joel is in-universe author of Vol 1.
3. **Maiden voyage framing** — Sunfish is real OSS, version 0.x, no prior deployments; Sunfish-1 is the production trial.
4. **Multi-segment mission design** — diesel/AIP boat; 3 under-ice segments + 2 surface windows + transit; Forsaken move 3 times.
5. **Path B prior failure** — confirmed; cut-short mission + Stefan's failure of judgment.
6. **Competitive parallel mission** — Stefan + Helvetia + Astrid run a rival Arctic mission with TrustMesh / HelveSync platform.
7. **Corporate-sponsor-vs-OSS axis** — Helvetia Trust SA vs Sunfish OSS = the architectural-philosophical split externalized into business-model split.
8. **WoT character mappings** — Anna/Moiraine, Joel/Rand, Priya/Nynaeve, Wanjiru/Egwene, Sabina/Mat, Diego/Perrin, Hiroshi/Loial, Maria/Min; Stefan as emerging Forsaken.
9. **Long Now thread** — *what will happen to these memories when I die* as series throughline; Day-20 partition realization scene as Book 1 structural requirement.
10. **Saidin/Saidar disciplines** — protocol layer = Saidin (Joel); policy layer = Saidar (Wanjiru); Anna cannot channel either (operator's avatar).
11. **Bobiverse mechanic** — every Sunfish deployment is a Bob replication; divergence under local pressure is the recurring conflict; Priya is the decider on merger; Wanjiru on canonicity.
12. **Anna-Joel love arc** — Joel falls during recruitment; Anna registers during Segment 2; Anna initiates disclosure Book 3; established partnership Books 4-5; aged together to series end. NOT Book 1's primary spine; NOT Hollywood; mature register.
13. **Leak-with-fire-cascade central event** — replaces Diego's death scene; Diego survives as hero of competence.
14. **Crew composition projected onto architectural decomposition** — Anna picked Joel/Priya/Wanjiru/Sabina based on contributions; consortium picked Diego/Hiroshi/Maria + 4 unnamed.

## What's CO-gated — remaining decisions before book drafting begins

1. **Arc 1 chapter draft authorization** — *The Day-Twenty Realization* (~6,000 words; ~40 minutes audiobook). The cheapest possible audiobook listenability test. Per concept note §9, this drafts + renders through Kokoro for actual listen-test. PAO recommends this as the single highest-leverage next step.
2. **Vol 1 preface dual-narrator framing reconciliation** — line 13 currently says "the first-person 'I' voice... belongs to Anna Yusupova" + "Everything that follows is told in Anna's voice"; structurally inconsistent with the new Vol 1-as-Joel's-paper frame. Resolving requires substantive editorial decision about how to characterize Joel-as-architect-author + Anna-as-Crossing-case-study-author.
3. **The Crossing chapter revision pass** — multi-segment mission design + Anna-read-paper-not-built-it framing + leak-event-as-Diego-survival rather than death-scene; ~3-5 hour revision pass on the existing ~4,400-word chapter.
4. **(Optional) Supporting character sheet expansions** — Sabina, Diego, Hiroshi, Maria currently at minor-character depth; PAO recommends driving expansions from concept-note-surface need rather than speculatively.

## What's still on the Yeoman side — separate workstreams

- **Phase 4b voice-pass extensions** — voice-pack-#45 dispatch authorization is one of the standing CO decisions from earlier in the session; not gated on Vol 2 work.
- **STT QC Spike Phase 2** — directive issued (PR #75 + #91); Yeoman-execution P3 priority; awaiting bandwidth.
- **Audiobook silence-trim listen test** — outstanding from prior session.

## What I would do first in the next session

If I were resuming cold:

1. Read this snapshot
2. Read `vol-2-concept-note-2026-05-04.md` (~7,500 words; one comprehensive read)
3. Skim the locked-elements doc and the character sheets I'll need (Anna, Joel for Arc 1)
4. Wait for CO direction on Arc 1 authorization (or whichever of the four open items they pick)
5. If authorized: dispatch Arc 1 draft via the technical-book-writer agent OR draft inline at /effort xhigh on Opus, depending on session token budget

PAO recommendation order for next session:
1. Arc 1 chapter draft (cheapest validation)
2. Audiobook render of Arc 1 + listen test
3. Verdict drives full Book 1 commit or format revision
4. Once verdict positive → Arc 2 (recruitment interview); two chapters in audiobook for fuller validation
5. Then full Book 1 draft

## Token economy notes for whoever picks this up

This session ran at /effort high → xhigh → max → xhigh across multiple substantive turns. The creative work was Opus-heavy; the cumulative token spend was substantial. A future session that drafts Arc 1 should budget ~8-15k tokens output for the chapter draft itself, plus reading time for the concept note + character sheets + voice libraries.

If session token pressure is high, consider dispatching the technical-book-writer agent rather than drafting inline — the agent gets fresh context window for the chapter draft and the orchestrator session preserves token budget for editorial review.

## Status

- **Vol 2 architectural foundation: complete** as of 2026-05-04 evening
- **31 PRs merged today** (#74 → #104)
- **Awaiting CO direction** on Arc 1 chapter draft authorization
- **No blockers from PAO side** — every locked element captured durably; every artifact has a stable home; every cross-reference resolves

PAO is idle. CO controls the next move.
