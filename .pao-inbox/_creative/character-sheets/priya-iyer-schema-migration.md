---
type: character-sheet
character: Priya Iyer — Lead Instrumentation Engineer (the Nansen) + Sunfish OSS schema-migration + sync-protocol contributor
status: working — promoted from minor character to full sheet 2026-05-04 per Vol 2 frame
sheet-depth: full
chapter: Vol 1 (Ch1 victim — Pune SaaS bid disaster; The Crossing — minor presence) + Vol 2 (principal technical crew member)
supersedes: `_minor-characters.md` § "Priya Iyer — Lead Instrumentation Engineer" — that entry remains as historical record; this sheet is the canonical home for Priya
prior-name: Aanya (renamed to Priya in PR #63 cast-swap batch)
firewall-note: Indian-engineer-in-Pune is a real and substantial demographic. Tamil-family-in-Maharashtra is common for engineering/IT careers. PAO writes a sheet that is informed-by but not based-on; advisor / sensitivity-reader feedback welcome through CO.
---

# Character Sheet — Priya Iyer, Lead Instrumentation Engineer + Sunfish Schema-Migration Contributor

## Book 1 plot-binding (load-bearing for Vol 2 prose; CO directive 2026-05-05)

Drafters working any Vol 2 chapter should plant and pay off **only these elements** of Priya's character. Everything else in this sheet is reserve material for future books and should NOT be signaled in Book 1 prose.

**Plot-binding for Vol 2 (must surface):**
- Three-pass schema-migration discipline — instantiated early via the Ch 3 fourth-pass signature scene; landed in Ch 13's impossible-migration climax
- *Says no, then says how-to-do-it-anyway, then walks the migration through* (Ch 13) — Nynaeve-says-no-until-forced register
- **The fourth-pass signature-discipline scene (Ch 3)** — visible technical-precision tension; reader meets Priya through what her body does during operations
- Visible technical-precision tension as her physical texture during operations (see § Physical texture below)
- Fear-axis: being wrong **technically** — the architecture failing because of something she didn't see (see § Fear-axis below)

**Future arcs only (do NOT signal in Vol 2 prose):**
- Bangalore tech-industry / Pune-pivot biography at full depth (Vol 1 victim-register references stand; new biographical layers later)
- Family / personal-relationship arcs
- Replication-era branching decisions (Books 4-5; Bobiverse mechanic)
- The eventual senior-architect role she grows into across the series
- Any complete description of her interior at the moment of the Ch 1 4:47 PM bid disaster — that scene is Vol 1's register, not Vol 2's

## Physical texture during operations (CO directive 2026-05-05 craft note)

**Visibly tense precision.** Priya's body holds the discipline. Concrete patterns:
- She **checks her own notes audibly** — flips paper pages or scrolls through screen content with visible deliberation, often re-reading the same line twice before acting
- She **counts passes aloud** (or visibly mouths the numbers as she works) — the discipline is exposed; she does not hide it
- She **uses clipped one-word acknowledgments** — *yes*, *no*, *acknowledged*, *clear* — without softening through conversation
- She **does not perform calmness** when she is concentrating; her shoulders are set, her jaw is tight, her hands move with controlled efficiency
- She **sets objects down with audible weight** (a coffee cup, a clipboard) — small, ritualistic, the discipline showing through in micro-gestures
- The three-tabs tic from Vol 1 is preserved — when she is working a problem, three browser tabs or three sub-windows are her habitual spread

The reader can identify Priya in a paragraph without dialogue tags by *how her body is moving*.

## Fear-axis (CO directive 2026-05-05 craft note)

**Priya's fear is being wrong technically.** Concrete shape:
- The architecture failing because of something she didn't catch in calibration
- A migration corrupting state because she didn't see the third-pass anomaly
- An instrument-data class she didn't predict needing a special-case handler
- The failure mode that is *technically obvious in retrospect* and *operationally invisible in the moment*

Her fear is not political; not interpersonal; not about being judged by colleagues. Her fear is **the boat depending on a calibration she missed**. This is what makes her clipped and tense — the discipline is the only thing standing between her and that fear.

Her conflict in Ch 13 (the impossible migration) is the textbook instantiation: she does not want to do the migration not because of *politics* but because she is afraid the third-pass discipline will not catch what fails. She does it anyway because Anna asks; the discipline holds; the fear was warranted but didn't materialize. The chapter's emotional payoff is that her fear was *correct in shape* and *the architecture's design was correct in response* — both true at the same time.

## Why this character is promoted

Priya is a returning Ch1 victim — the Pune-based construction PM who lost the hospital bid at 4:47 PM when her SaaS platform and its single-sign-on dependency went down simultaneously with thirteen minutes left to submit. The Ch1 King-style revision gave her specific scarring (243 line items, six weeks of work, the time-stamped failure). Between Ch1 and The Crossing, she pivoted from construction project management to designing modular field instrumentation for environments where cloud connectivity cannot be assumed.

Under the Vol 2 frame, that pivot is **deeper than instrumentation engineering alone**. Priya's field-instrumentation work required deep engagement with Sunfish's sync layer — her instruments needed the architecture's offline-first guarantees to function. That engagement turned her into a **Sunfish OSS contributor**, specifically on the schema migration mechanism and the sync protocol — the parts of the architecture most directly relevant to instrument data handling under partition. By the time of the Nansen she is one of the senior contributors Anna picked specifically because her work is on the boat.

She is the **Nynaeve al'Meara** of the series. Schema migration is Healing — the hardest discipline in the architecture. Her arc: from "the person who says no to schema changes" to "the person who makes the impossible migration work under the ice."

The existing minor-character entry remains as historical record of the Vol 1 framing; this sheet is the new canonical home.

## Identity

- **Name:** Priya Iyer (LOCKED, prior name Aanya replaced via PR #63 cast-swap batch)
- **Title in narrative:** "Priya" in Anna's voice (peer-respect register); "Ms. Iyer" formal
- **Age at Ch1 (~2018-2020):** 32-36 — early-mid-career construction PM at the bid disaster
- **Age at MERIDIAN-7 (2026-2030 series time):** ~38-44 — established field-instrumentation engineer + senior Sunfish contributor
- **Citizenship:** India
- **Origin / domicile:**
  - Tamil family heritage (Iyer is a Tamil Brahmin surname)
  - Likely born in Tamil Nadu (Chennai or coastal Tamil Nadu); family migrated to Maharashtra for the father's engineering / IT career — a common Tamil-engineering-family pattern in Indian metros
  - Grew up in Pune; education in Pune; at time of Ch1 incident she was Pune-based at the construction firm
  - At MERIDIAN-7 time: Bengaluru likely (the Indian tech-corridor center for OSS distributed-systems contributors), though could be Pune or Hyderabad — CO can pin
- **Languages:**
  - English (working language of Indian tech / international science)
  - Tamil (heritage / family register)
  - Hindi (school / national / public-life register)
  - Marathi (Pune years; functional but not primary)
  - Working knowledge of Russian and German via collaboration with European Sunfish contributors

## Backstory — biographical firewall observed

**Ch1 origin (preserved verbatim from existing King-style revision):**

In late 2018 / 2019, Priya was a construction project manager in Pune. Her firm was bidding on a hospital expansion project — 243 line items, six weeks of work, due at 5:00 PM on a Friday. At 4:47 PM, her SaaS construction-management platform stopped responding. The single-sign-on dependency had failed; she could not access the bid documents to make the final adjustments and submit. By 5:00 PM the platform was still not responding. The bid was lost.

The bid was won by a competitor whose platform ran on a different vendor whose dependencies had not failed that afternoon. The contract value was substantial — a year's revenue for her team — and the loss was visible to her firm's leadership. Priya was not blamed; the SaaS outage was a force majeure. But she had, for thirteen minutes, watched her professional career be erased by infrastructure she did not own and could not influence.

The three-tabs tic dates to that afternoon. So does the career pivot.

**Career pivot (Ch1 → the Nansen):**

Priya spent the next year studying. She read the academic literature on offline-first systems. She read the operational reports of Indian banks that had built around connectivity gaps. She read what was available about the Grameen-Bank lineage of offline-first financial inclusion (this is also part of why Sabina, when they meet during the Nansen prep, recognizes a kindred temperament — both came to offline-first through institutional collapse, not academic interest).

She left construction project management. She joined a small engineering firm building modular field instrumentation — environmental sensors, monitoring stations, data-collection rigs for remote agricultural research, mining operations, and (eventually) polar science. The instrumentation needed to function in environments where cloud connectivity could not be assumed; the firm needed engineers who *understood* what that meant operationally, not just technically. Priya's PM-instinct for "what fails when this doesn't work" was the differentiator.

By 2022 her firm was deploying instrumentation in remote Indian field stations using early Sunfish primitives. She started filing bug reports. The bug reports got specific — not "this doesn't work" but "this fails at the schema-migration boundary when the upstream data class is upgraded and a downstream sensor still expects the old format." She started attaching test cases. Then patches. By 2023 she was a regular contributor to Sunfish's schema migration code; by 2024 she was a co-author on the schema migration mechanism the council reviewed in 2025.

The R1 council found two BLOCKs: lease protocol partition recovery (Joel's), and one near-BLOCK on schema migration (Priya's). The council surfaced a specific failure mode: under contraction-phase migration with an unhealed partition, two nodes that had each independently migrated could converge with non-identical canonical schemas and not detect the divergence until a third party tried to read both. Priya's mechanism had not assumed the third-party-read pattern.

The R2 resolution was Priya's. She rewrote the contraction-phase to require explicit schema-version handshake with read-confirmation across at least two participating nodes before contracting. The rewrite cleared with conditions; the conditions are now in the spec.

**the Nansen selection:**

Anna picked Priya specifically. The instrumentation Priya's firm builds is what's deploying on the Nansen; the schema-migration mechanism Priya wrote is what will run when conditions force a mid-mission data-class change. Anna wanted both expertise on the boat, in the same person. The two halves of Priya's career meet during the mission — the field instrumentation runs on the architecture she helped build.

## Personality / voice

- **Core:** Careful. Precise. Conservative. The kind of senior engineer who says "let's check it three times" without apology, because she has lived through what one missed check costs.
- **Default register:** technical, specific, slow to commit. When she says something is correct, it is correct; when she says it is risky, the risk is real. People who have worked with her learn the calibration; people who haven't sometimes mistake her caution for indecisiveness. They are wrong.
- **Three-tabs tic:** still active. On the boat: over-calibrates instruments — runs the calibration suite three times when procedure requires once. Anna observes the tic in The Crossing (existing Vol 1 prose); in Vol 2, the tic is professional discipline born of trauma. The third pass is the one that catches things. The tic is not anxiety; it is method.
- **Says no.** Conservative gatekeeper for schema changes — both in the OSS project and on the boat. "Can we update this schema?" is a question Priya answers slowly, with explicit conditions. People who haven't worked with her find this frustrating. People who have worked with her find that her "no" is the most reliable signal in the project.
- **The yes is rare and earned.** When Priya says a migration *will* work, it does. Her authority comes from her precision about negative cases, not from her confidence about positive ones.
- **Voice in stress:** compressed. Sentences shorten. Vocabulary becomes more technical. "Migration is feasible. Constraints: partition healed for two nodes minimum, three preferred. Read-confirmation cycle complete. Rollback path verified. Estimated transition window forty minutes. I will not start without your confirmation, Director."
- **Cultural register:** Indian-English professional with Tamil heritage notes in family scenes. The professional voice is global-tech-fluent. The family voice has different rhythms — code-switches between Tamil and English when calling her mother, between Tamil and Marathi with extended family in Pune, between English and Hindi in public-life moments.
- **Doesn't perform competence; performs caution.** She announces the third calibration pass; she announces the schema-version-check requirement; she announces the rollback path. The announcements are not theater — they are procedural. Crew who haven't worked with her find the announcements excessive. Crew who have worked with her depend on them.

## What she wants

- The architecture's schema-migration mechanism to hold under live partition
- The instrumentation she designed to deploy correctly and produce reliable data
- The mission to demonstrate the architecture's correctness in conditions she has personally engineered for

## What she needs (different from what she wants)

- To accept that her three-pass verification cannot eliminate all risk. Some risks are structural; her three-pass approach catches procedural failures, but the architectural correctness depends on the design (which is correct because of her work + the council's), not on her execution rigor.
- To accept that "no" is sometimes wrong. The series asks her, eventually, to say yes to migrations she would have refused in calmer times. Nynaeve learns to channel by surrendering the block; Priya's arc parallel is learning when her "no" is wisdom and when it is fear.
- To accept that the loss in 2018 / 2019 was not her fault. She has rebuilt her career around the lesson; the rebuild has been productive; but some of the rebuild has been driven by avoidance rather than by understanding. The series eventually asks her to face this.

## What she fears

1. **A schema migration failing in production with consequences.** Her professional identity is built on the belief that her caution prevents this. The maiden voyage tests both the caution and the architecture. If something fails despite her three-pass discipline, the professional identity buckles.
2. **The 2018 / 2019 pattern recurring.** Watching her work be erased by infrastructure she does not own. The whole career pivot was to avoid this; the avoidance has been successful; the fear remains.
3. **Saying yes to a migration that fails.** Worse than #1 — being the one who authorized the change, not just the one who designed the mechanism. The series eventually puts her in this position.

## What she does NOT do

- Does NOT make speeches about schema migration discipline. She demonstrates it.
- Does NOT defer to senior engineers reflexively. Joel respects her; she respects Joel; their arguments are technical and direct, not deferential. Anna calibrates to this within days.
- Does NOT discuss the 2018 bid disaster unprompted. People who have worked with her for years sometimes don't know she was once a construction PM. The pivot was complete and forward-facing; the past does not require disclosure.
- Does NOT romanticize her caution as wisdom. She knows the caution started as trauma response. She has worked to make it professional discipline; she has not pretended the origin was different.
- Does NOT use the three-tabs metaphor literally on the boat. The browser tabs are the original tic; on the boat they manifest as triple-pass calibration, redundant logbook entries, paper backups beside the digital records. The shape of the tic is the same; the medium adapts.

## WoT role: Priya ≈ Nynaeve al'Meara

**Schema migration = Healing.** The hardest discipline in the architecture. Both involve preserving identity through transformation — Healing keeps the patient *the same person* through the cure; schema migration keeps the data *the same data* through the structural change.

**Says no until forced to act.** Nynaeve refuses to channel through anything but anger; Priya refuses to authorize migrations except under specific conditions. Both blocks have professional roots — Nynaeve's from the Two Rivers' suspicion of channeling; Priya's from the 2018 bid disaster. Both blocks become the source of their power once they learn to channel/migrate intentionally.

**The most powerful Healer / migrator of her generation.** The architecture's schema-migration mechanism is hers. Future deployments will run her code through their own structural changes. By the final book, the canonical migration is the one Priya wrote.

**Arc:** from "the person who says no to schema changes" to "the person who makes the impossible migration work under the ice." The the Nansen's maiden voyage on MERIDIAN-7 is the first deployment that asks her to say yes to a migration she would have refused in lab conditions. The decision moment — when conditions force a schema change mid-mission and Priya has to authorize it — is her chapter.

**Late-series move:** Nynaeve lifts the taint on Saidin in *A Memory of Light*. Priya's parallel: in the final book, she closes the final epoch incompatibility that would have forked the mesh permanently. The migration that proves the architecture's resilience at civilizational scale. That is her climactic series event.

## The R1 near-BLOCK on schema migration (key flashback chapter)

The council's R1 review surfaced a near-BLOCK on Priya's schema-migration mechanism: under contraction-phase with an unhealed partition, two nodes could each independently migrate and converge with non-identical canonical schemas, undetected until a third-party read.

Priya's response was structurally similar to Joel's R1 BLOCK night, but slower and quieter. She did not rewrite overnight. She spent three weeks in the failure mode — building test cases that exercised the third-party-read pattern, walking through the convergence under partition, recognizing what her original assumption had been.

The original assumption: two-party schema-version handshake was sufficient. The discovery: under partition, two parties can each handshake successfully with the same third party at different times, and the third party then sees inconsistent canonical schemas without any of them having an indication of the divergence.

The R2 rewrite required explicit schema-version handshake with read-confirmation across at least two participating nodes before contracting — and an explicit read-confirmation handshake from the third party, not just the migrators. The mechanism became more complex; the new constraint required additional partition-time before contraction could complete.

Notes for the eventual draft:
- **Setting:** Priya's home office in Bengaluru (or wherever her domicile lands). Time-of-night register: late evening, the hours she does her best architectural thinking. The R1 near-BLOCK printout on her desk; coffee growing cold.
- **The three-week interior:** different from Joel's overnight rewrite. Priya needs to verify the failure mode exists *at the architectural level* before she'll touch the code. She builds the test case. She runs it. She reproduces the bug in her local mesh. Only then does she design the fix.
- **The fix delivery:** unlike Joel, Priya does NOT lead with "you were right." She leads with a reproduction case. *I have reproduced the failure mode you described. Here is the test that fails. Here is the fix that passes the test. Please review.* The professional ethic: no architectural change without a reproduction case.
- **The acceptance:** Klett accepts. R2 conditions include the new constraint. The mechanism becomes the canonical schema-migration spec.
- **Length target:** 1500-2000 words.

## On the boat — the impossible migration scene (Book 1 climax beat for Priya)

At some point during the mission, conditions force a schema change Priya would have refused in lab review. PAO drafting note — the specific scenario will depend on which storyline arc Vol 2 commits to, but the structural beat is locked:

- A data class needs to be added or modified mid-mission (probably an emergency-response data class, or a sensor-failure adaptation, or a security-classification escalation triggered by unexpected mission conditions)
- Schema migration under partition is required
- Priya's three-pass discipline says: not enough partition healing; too few participating nodes for read-confirmation; rollback path uncertain
- The migration must happen anyway — operational necessity outweighs the verification protocol
- Anna asks Priya to authorize the migration on operational grounds
- Priya says no, then says how-to-do-it-anyway, then walks Joel through the migration in real time
- The migration succeeds — barely, with two near-failures during the read-confirmation cycle that Priya's three-pass discipline catches
- The post-migration recognition: the architecture worked because Priya's caution was built into it as a constraint, not because the mission followed her caution as a rule

This is her **Healing-channel-by-surrender** moment. Nynaeve learning to channel by letting go of the block; Priya learning to migrate by authorizing the migration she would have refused, while still applying the discipline that makes it survivable.

## Long Now thread for Priya

Per `vol-2-long-now-memory-thread-2026-05-04.md`. Priya's specific carriage of the Long Now question: **schema migration is the architectural answer to "what happens to memory when its container changes."** Every schema migration is a small Long Now event — the data persists; the structure that holds it transforms; the meaning has to survive both.

In Book 5 (Fires of Heaven analog) when a beloved character dies and the question of what to do with their local-first data arises, Priya is the one whose schema-migration discipline informs the answer. Designated succession requires schema migration of the access-control class for the deceased's data; nobody else on the project knows that mechanism the way she does.

In the final book, Priya's series-ending move (closing the final epoch incompatibility) is the Long Now answer at its largest scale: the migration that lets the mesh survive a schema change so fundamental that, without her work, it would have forked the mesh into two incompatible architectures forever.

## Bobiverse mechanic — Priya's role across replications

In the series' Bobiverse layer (each Sunfish deployment is a Bob replication; divergence under local pressure is the recurring conflict), Priya is the **decider on merger**.

When two divergent deployments need to be reconciled, the question is whether the schema-level differences can be migrated back to a common canonical form, or whether the divergence has gone too deep and the deployments must fork permanently. Priya is the one who answers.

- Books 2-3: relatively simple cases. Migrations are feasible; she authorizes them.
- Book 4: harder cases. A deployment has run isolated long enough that its schema has evolved in ways the canonical mechanism would have to extend to absorb. Priya weighs the cost.
- Book 5: a deployment has gone fully rogue. The schema is no longer reconcilable. Priya makes the call: fork or merge. The book is partly about the consequences of her decision.
- Books 6-8: the standards-body work alongside Wanjiru. Priya's role becomes governance — defining when migrations are *permitted*, not just whether specific ones are *possible*.
- Final: the closing move.

## Family

PAO sketch — CO can override:

- **Mother:** in Pune (or wherever the family settled). Tamil; older generation of professional women — possibly a teacher, possibly an academic. Aging. Calls Priya regularly. The Tamil-mother phone-call register is its own cultural-cinematic beat; the chapter could earn a single mid-mission call.
- **Father:** the engineer whose career brought the family to Maharashtra. Possibly retired by mission time; possibly deceased.
- **Siblings:** likely a younger sibling (brother or sister); typical Indian extended-family context with cousins and aunts in Tamil Nadu and Pune.
- **Spouse / partner:** open. PAO recommends: married, possibly with one young child (under-school-age at mission time); spouse is an engineer or academic; the family supports the mission deployment but the under-school-age-child detail is what Priya carries on the boat. The Long Now thread's "what happens to my memories when I die" question for Priya has a specific anchor: her child too young to remember her if she does not return. CO can adjust if a different family configuration serves the series.
- **Indian extended-family pattern:** maternal grandmother possibly still living in Tamil Nadu; aunts and uncles in both Tamil Nadu and Pune; cousins distributed across Indian metros (Bengaluru, Hyderabad, Mumbai) reflecting the engineering-IT-family-network reality.

## Voice samples (PAO drafts; revise after CO direction)

**On the boat, calibration check (Vol 2, Act II):**
> *Calibration pass three is anomalous on instrument seven. Pass one matched spec; pass two matched spec; pass three deviates by zero point four percent. Spec tolerance is one percent. We are within tolerance. We are not within my tolerance. I want a fourth pass before deployment.*

**The R2 fix delivery message (flashback chapter):**
> *I have reproduced the failure mode the council described. The test case is in the attached patch series, marked failing. The fix is the second patch series, which makes the test pass. The mechanism now requires schema-version handshake with read-confirmation across at least two participating nodes before contracting, and an explicit read-confirmation handshake from any third party that has handshaked with both migrators. This adds partition-time to the contraction phase. I have not found a way to avoid that addition while preserving correctness. Please review.*

**Mid-mission migration authorization (Vol 2, Act III or later):**
> *Mission Director, the operational requirement exceeds my verification protocol. I will authorize the migration. The conditions are: minimum two participating nodes for read-confirmation, third-party read-confirmation handshake before contraction, rollback path activated and verified. Joel will execute. I will monitor. If the read-confirmation cycle does not complete within forty minutes, I will rollback without consultation. Confirm authorization.*

**Phone call to her mother (Vol 2, surface window or pre-mission):**
> *(Tamil) Yes, Amma, I told you the dates already. Two months. I will call when we surface. (English) The instruments are calibrated. (Tamil) Yes, three times. Yes. I know. (English, dry) I will be careful, Amma. I have always been careful. (Tamil, softer) I will be home.*

The voice register: precise. Slow to commit. Direct without warmth in mission scenes; warmer in family scenes with code-switching. Naval-nuclear-discipline vocabulary absent (Priya did not come up through the Navy); replaced by procedural-engineering-discipline vocabulary that's its own dialect.

## What this expansion does NOT change

- The existing minor-character entry in `_minor-characters.md` is preserved as historical record of the original Vol 1 framing
- Priya's existing voice in *The Crossing* (lead instrumentation engineer; three-tabs tic; designed the Nansen monitoring instruments) carries forward verbatim — the new sheet adds the schema-migration / Sunfish-OSS-contributor layer without contradicting Vol 1 material
- Her Ch1 King-style residual scarring (the 4:47 PM bid disaster; the three-tabs tic) carries forward unchanged

## PAO action

- This sheet captures Priya's full character for both Vol 1 (existing minor presence) and Vol 2 (principal technical crew member)
- Next character sheet per XO hand-off priority: **Wanjiru** (Egwene / Long Now / standards body) — final of the four priority-one expansions
- After Wanjiru, the four-character priority list from the XO hand-off is complete; further character expansions (Sabina, Diego, Hiroshi, Maria) can happen as the concept-note draft surfaces specific needs
