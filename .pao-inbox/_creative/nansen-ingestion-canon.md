# Nansen Ingestion — Public-Domain Source Material Canon

**Date:** 2026-05-09
**Author:** PAO (filing CO directive 2026-05-09)
**Status:** Adopted as craft canon for Vol 2 (and future-volume) prose enrichment
**Authority:** This document is canon for any chapter prose, voice-pass, or chapter-drafter work that ingests public-domain source material to extend Anna's (or any project character's) observational density.
**Related:**
- `.pao-inbox/_creative/joel-teaching-register-canon.md` (sibling pattern: existing-source-material-then-voice-transform)
- `.pao-inbox/_creative/sunfish-submarine-security-canon.md` (canon discipline; §7 narrative restraint applies to security-adjacent ingested content)
- `~/.claude/skills/janeway_first_person_voice/SKILL.md` (the voice-side of the transform)
- `~/.claude/skills/voice-towles/SKILL.md` (alternative voice-side)
- `vol-2/_glossary/_lexical_fatigue_families.yaml` (the empirical baseline that motivated this canon)
- `build/lexical_fatigue.py` (the measurement tool)

---

## What this is

A craft discipline for **extending Anna's prose with public-domain source material**, so that the observational, atmospheric, and sensory content that the genre canonically depends on can be borrowed from human-authored expedition narratives — and then transformed through Anna's voice (or Janeway / Towles / whichever register fits the scene). The output reads as authored, not as AI-generated, because the underlying observational content was authored by Fridtjof Nansen in 1897 and the voice transformation preserves that human texture.

**Three canonical sources** (triangulated 2026-05-09):

1. **Fridtjof Nansen, *Farthest North*, 1893-1896 expedition narrative published 1897.** Public domain (Project Gutenberg #30197). First-person Arctic polar-expedition narrative. Anna's RV *Nansen* is named after this Nansen — thematic and structural alignment deliberate. Observational baseline: 73.81 hits/1k. **Strongest reference for: pack-ice texture, sealed-hull discipline under deep cold, multi-year-expedition exhaustion register, scientific instrument observations.**

2. **Jules Verne, *An Antarctic Mystery* (Le Sphinx des Glaces, 1897), trans. Frances Cashel Hoey.** Public domain (Project Gutenberg #10339). First-person captain-narrator Antarctic adventure; sequel to Poe's *Narrative of Arthur Gordon Pym of Nantucket*. Observational baseline: 52.83 hits/1k. **Strongest reference for: Antarctic geography, southern-ocean specifics, ice navigation south of the Drake, surface-ship-in-Antarctic-waters register.**

3. **Jules Verne, *Twenty Thousand Leagues Under the Sea* (1870, English translation).** Public domain (Project Gutenberg #164). First-person narrator (Professor Aronnax, naturalist) embedded aboard Captain Nemo's submersible *Nautilus*. Observational baseline: 57.34 hits/1k. **STRONGEST STRUCTURAL HOMOLOGUE FOR VOL 2:** submarine narrative; long underwater immersion; embedded narrator observing a captain; scientific-observational register. The *Nautilus*'s sustained-immersion scenes are the closest literary template for Anna's RV *Nansen* under-ice operations.

**Why all three:** Each anchors a distinct register dimension. Nansen brings expedition-diary density and pack-ice authority; *Antarctic Mystery* brings southern-ocean + Antarctic geography; *20K Leagues* brings submarine narrative shape and embedded-observer register. **Three-source weighted canon baseline: 62.87 hits/1k.** Vol 2's 48.70 sits at **0.77× of triangulated canon** — empirically robust across three independent references spanning 27 years (1870-1897).

**Source selection guidance per scene type:**

| Scene type | Primary source | Why |
|---|---|---|
| Submersion / under-ice operations / sealed-hull life | **20K Leagues** | Direct submarine-mission homologue; sustained-immersion register |
| Antarctic geography / Drake passage / southern weather | **Antarctic Mystery** | Geographic match; surface-ship-in-Antarctic-waters specifics |
| Pack-ice transitions / extended-cold conditions / instrument observations | **Nansen** | Highest observational density; real-expedition authority |
| Mixed atmospheric scenes | **Mix** of two or three | Combine for richest texture |

**Triangulation finding worth noting:** Anna's procedural vocabulary tics (register at 9.88/1k; discipline at 1.99/1k; standing at 5.46/1k) appear essentially **never** across all three canonical sources (0.00-0.03/1k for register, ~0/1k for discipline, 0.28-0.74/1k for standing). The genre canonically does not use this vocabulary at all, let alone at Anna's density. The empirical register imbalance is structural, not source-specific.

---

## The empirical case

Lexical-fatigue analysis 2026-05-09 (`build/output/qa/vol-2-lexical-fatigue-rollup.json`) revealed that Anna's voice deploys procedural-institutional vocabulary at densities **without precedent** in the canonical first-person polar-explorer tradition:

| Lemma | Anna /1k | Nansen /1k | Anna vs Nansen |
|---|---:|---:|---:|
| register | 9.88 | 0.01 | **1233×** |
| logged | 2.53 | 0.02 | **105×** |
| discipline | 1.99 | 0.00 | Anna-only |
| procedure | 1.24 | 0.00 | Anna-only |
| acknowledged | 1.99 | 0.01 | 248× |
| said | 8.62 | 0.92 | 9.35× |
| standing | 5.46 | 0.74 | 7.40× |
| read | 5.37 | 0.38 | 14× |

**Nansen's top-30 lemmas are observational nouns + action verbs:** *north, water, wind, land, drift, ship, fram, time, take, make, find, give, last, come, after, into*. Concrete, sensory, in-the-world.

**Anna's voice is institutional-procedural; Nansen's voice is observational-scientific.** Both first-person; both polar-expedition; both seventy thousand light-years (or three hundred meters of ice) from home. The register imbalance is what the reader's ear catches as fatigue.

The cull-pass alone (cutting register-density) is incomplete: it shrinks Anna without rebalancing toward observational specificity. **Ingest-and-transform addresses both axes** — cuts the procedural over-density AND adds the observational density the genre depends on.

---

## The discipline: content-yes, voice-no

The transform is bounded:

### What ingestion provides

- **Concrete observational specifics** — particular weathers, ice forms, light qualities, sea conditions, instrument behaviors, navigation events, watch-routine textures, scientific measurements
- **Sensory anchoring** — what an explorer *sees, finds, hears, smells, takes from the deck, marks on a chart*
- **Atmospheric authority** — descriptions written by a person who actually crossed the Arctic in 1893; the reader's ear registers this as authored, not generated
- **Action-verb density** — the canon Anna's voice is missing (*came across, took the reading, drifted past, made the entry, gave the order, found the change*)

### What ingestion does NOT provide

- **Plot facts** — Anna's mission events come from the chapter outline + author canon, not from Nansen
- **Character history** — Anna's character + crew remain canonical; Nansen's crew is not imported
- **Voice / cadence** — Nansen's Victorian register, his oratorical openings, his philosophical flourishes do NOT travel; the voice-pass step strips them out
- **Direct quotation** — no Nansen sentences land verbatim in Anna's chapters; transformation is mandatory, not optional

### What the voice-pass step does

After ingestion, the source content is transformed through one of the project's voice agents:

- **`janeway_first_person_voice`** (default for Anna's narration in body chapters; first-person captain register)
- **`voice-towles`** (alternate; old-world composure + observational asides; useful for reflection-density passages)
- **Anna's existing register** (current canonical; for chapters not undergoing voice migration)

The voice-pass converts Nansen's diction, syntax, and cadence into the target voice. The OBSERVATIONS survive; the VOICE is replaced.

---

## Three-step ingest-transform process

### Step 1 — Identify the target scene

Best candidates from Vol 2 (atmospheric / observational / sensory passages where Anna's existing prose is procedural-heavy and observational-light):

| Chapter | Scene | Why a candidate |
|---|---|---|
| **Ch 3** *Drake Passage* | Sea + weather + cold during the southern crossing | Nansen has extensive sea-and-weather observations; direct register match |
| **Ch 4** *First Submersion* | The dive itself; ice / water transitions | Nansen's pack-ice scenes provide rich sensory texture |
| **Ch 9** *Sync Daemon Under Drift* | Drift, navigation under ice; daily-watch register | Nansen's Fram IS a drift expedition by design — closest structural homologue in Vol 2 |
| **Ch 12** *Beginning of the End* | Third dive; thermocline; routine submersion | Nansen's daily-deep register and instrument-watching scenes |
| **Ch 16** *Final Ascent* | Surfacing after long submersion | Nansen has open-water emergence scenes |

NOT recommended for ingestion (too plot-load-bearing or wrong-register):
- Ch 1 *Departure* — opening crew register; canonical
- Ch 2 *Recruitment Interview* — dialogue-heavy; needs Joel/Anna voice work, not atmospheric ingestion
- Ch 7 *Joel's Sunfish* — disclosure scene; technical content; Joel-teaching pilot territory
- Ch 13 *Schema That Should Not Migrate* — procedural ceremony; TPI register
- Ch 14 *The Crossing* — action / cascade; Nansen's slower observational pace would dilute the dramatic tempo
- Ch 18 *Punta Arenas Surfacing* — closing chapter; institutional reception register

### Step 2 — Ingest the source content

Pick a Nansen passage whose observational content maps to the target scene. Selection criteria:

- **Concrete observational density** — multiple particular details per paragraph (specific instruments, named weather conditions, named ice forms, light qualities, navigational events)
- **Register match** — first-person captain-explorer voice; not lecture, not letter, not philosophical aside
- **Length match** — Nansen passages tend to run longer than modern reading rhythm; may need to compress at the voice-pass step

Suggested ingest workflow:

1. Read the candidate Vol 2 scene; identify what it currently lacks (sensory anchoring? atmospheric specificity? action-verb density?)
2. Browse Nansen for matching content (Project Gutenberg full text at `/tmp/gutenberg/farthest-north.txt` or fetch fresh from gutenberg.org/files/30197/)
3. Excerpt the Nansen passage to a working file (e.g., `vol-1/_voice-drafts/nansen-ingestion/<scene-id>.source.md`); annotate which Nansen page / chapter
4. Identify the SPECIFIC observational content to carry forward — the named weathers, the instrument readings, the sensory details. List them.

### Step 3 — Voice-pass through the target voice

Invoke the voice-side skill / agent with two inputs:
- The Vol 2 scene's existing context (what Anna is doing; what crew is present; what the chapter's beat requires)
- The Nansen-derived observational content (the specific details to be folded in)

The voice agent produces the transformed passage. Output goes to `vol-1/_voice-drafts/nansen-ingestion/<scene-id>.transformed.md`.

The voice-pass MUST:
- Strip Nansen's Victorian cadence
- Strip Nansen's oratorical / philosophical asides
- Strip any direct phrase that sounds anachronistic in Vol 2's setting
- Preserve the concrete observations as content the target voice would naturally render
- Preserve the project's antipattern discipline (anaphora cap 2; no tautological self-equation; no franchise imports per the Janeway skill)

---

## Attribution

Project Gutenberg / public domain. No legal attribution required, but the project's back-matter audio credits and EPUB acknowledgments should include a single attribution line:

> *Vol 2 contains observational content drawn from Fridtjof Nansen's* Farthest North *(1897, Project Gutenberg #30197). All passages have been transformed through the project's voice register; no Nansen sentences appear unchanged. Public domain; gratefully acknowledged.*

This attribution is canon for any volume that uses the ingestion canon, not just Vol 2.

---

## Risks to watch

1. **Anachronism creep.** Nansen's 1893 vocabulary includes terms that don't fit Vol 2's near-future setting (specific 19th-century instruments; obsolete navigation; pre-radio comms). The voice-pass must catch and recast these.
2. **Tonal mismatch.** Nansen's narrator carries a Victorian-romantic register (the "spotless mantle of ice" / "mighty giant" passages). Pure-content extraction works; voice carryover does not.
3. **Over-ingestion.** Anna's voice is Anna's voice, not Nansen's. Ingestion is texture-add, not substitution. Bias the discipline toward fewer, sharper observational beats; not wholesale paragraph replacement.
4. **AI-prose mitigation must be earned.** The point of ingestion is human-authored content seeding. If the voice-pass invents observations Nansen didn't make, the canon's value is eroded — we're back to AI-generated prose. Discipline: Nansen's specifics, transformed; not generated specifics dressed in Nansen flavor.
5. **§7 security canon still applies.** If an ingested Nansen passage parallels a Vol 2 scene that brushes against distress signaling / false codes / distress-only keys, the §7 narrative-restraint advisory governs. Nansen had no comparable mechanism; the parallel breaks down. Don't force.
6. **No direct source citations in the narrator's voice.** Added 2026-05-16 after Ch 17 FFF pilot surfaced a Verne citation in Anna's narration ("the air came in the way Verne described it when the Nautilus broke ice…"). The ingestion is **silent**: the reader experiences the texture, not the source. Anna does not name Nansen or Verne. Joel does not. None of the voice registers do. This rule is binding for all narrator registers; in-character dialogue by a literary-minded character could in principle reference a source, but Vol 2 has no such character and the default is no-citation. Cross-reference: ANNA-VOICE.md "What she does not do — References to pop culture by name."

---

## Cross-references

- **Joel-teaching-register canon** — same family pattern (existing material → voice transform). Joel-teaching extracts from Joel's character canon; Nansen-ingestion extracts from public-domain expedition narrative. Both validate that Anna's voice can absorb foreign content via voice-pass discipline.
- **Sunfish security canon §7** — narrative-restraint advisory binds. Nansen has no §7 equivalent (1897 polar narratives don't include covert protocols); ingestion can't generate §7 content.
- **Voice skills (`janeway_first_person_voice`, `voice-towles`, `voice-brown`, etc.)** — the voice-pass agents that perform the transform. Each carries its own antipattern discipline.
- **Lexical-fatigue detector (`build/lexical_fatigue.py`)** — the measurement tool. After ingestion, re-run the detector against the transformed scene; observational-density should rise; procedural-density may stay flat or drop. The detector is the empirical confirmation of register rebalancing.
- **Workshop entries (`vol-2/_glossary/`)** — audio glossary substitutions still apply on the transformed prose. The substitution YAML doesn't care whether the source is Anna-authored or Nansen-derived; it operates on output.

---

## Adoption sequencing

This canon is filed alongside two operational follow-ups:

1. **FFF (in flight 2026-05-09):** pilot the ingest-and-transform pattern on ONE atmospheric passage (Ch 3 or Ch 4). One scene; ear-test; if the lift is real, expand scope.
2. **GGG (in flight 2026-05-09):** extend the lexical-fatigue detector with an observational-density metric (concrete-noun + action-verb counts). Closes the measurement loop — telemetry can show whether ingestion actually rebalances the register.

After FFF lands and GGG is wired:

3. CO reviews FFF + GGG output; decides which Vol 2 chapters get ingestion treatment
4. Chapter-drafter agent invoked per ingestion target with this canon as primary reference
5. Re-run lexical-fatigue detector post-ingestion; confirm register rebalanced

---

## How to invoke this canon

When a chapter-drafter, voice-pass, or PAO session is working on a Vol 2 atmospheric scene and the question "should we ingest source material here?" arises:

1. Check this note for the chapter's row in the *Identify the target scene* table.
2. If the chapter is approved for ingestion AND the scene is observational-content-light, browse Nansen for matching content.
3. Ingest content; voice-pass through target voice; preserve antipattern + §7 discipline.
4. Re-measure with `build/lexical_fatigue.py` to confirm register rebalanced.

This canon is primary reference for any Vol 2 prose work involving Nansen ingestion.

---

**Filed by PAO. Pilot in flight (FFF). Measurement extension in flight (GGG).**
