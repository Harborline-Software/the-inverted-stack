---
type: integration-plan
volume: vol-2
title: The Filchner Dark — Plan C1+C7 Chapter-by-Chapter Integration Plan
author: PAO orchestrator (single-session Opus 4.7 xhigh)
date: 2026-05-21
preceded-by:
  - 2026-05-21-vol2-upf-more-interesting-plot.md (the UPF that produced Plan C as leading recommendation)
  - 2026-05-21-vol2-plot-spline-review.md (the audit that documented executed-vs-SPINE misalignment)
  - CIC ruling 2026-05-21 (Plan C variant 1+7 — Diego dies; Joel admits firmware decision)
companion-document: vol-2/SPINE-draft-plan-c.md (new working spine; draft for ratification)
methodology: per-chapter delta map + 4-wave prioritized execution
artifact-status: READ-ONLY analysis; no chapter or canon edits applied
scope: how Plan C1+C7 lands across the existing 109,230-word 18-chapter manuscript
plan-c-locks-respected:
  - Diego dies in Ch 14 (post-cascade close)
  - Joel admits vendor-firmware decision in Ch 17 (wardroom Day 54)
  - Anna's choice at the staff-history desk in Ch 18 is the volume's real climax
  - ~85-90% prose preservation
  - Anna voice / Diana / mother-wound / pastry-judge / polar setting all preserved
  - Vol-3 Wanjiru-narrator + Vol-4 Astrid arcs intact (and sharpened by Plan C)
---

# Plan C1+C7 Integration Plan

## Reading guide

This document is the operational companion to `vol-2/SPINE-draft-plan-c.md`. The SPINE describes what the new volume is. This document describes how it lands across the existing chapters.

The structure is:

- **Section 1** — Per-chapter delta map for all 18 chapters. Current state, Plan C state, delta type, specific edits needed, sequencing dependency, effort sizing, risk.
- **Section 2** — Prioritized wave plan. Four waves of execution, sequenced for safety.
- **Section 3** — Cross-chapter integration concerns. Plant-payoff chains; canon.yaml changes; the retrospective frame question for Ch 01.
- **Section 4** — Risk register + halt conditions.
- **Section 5** — Execution sequencing recommendation.

The "should Ch 01 acknowledge Diego's death?" craft question is named explicitly in §3.1 below; the recommendation there is *hold the knowledge for Ch 14*, with a one-sentence permitted extension in Anna's "nobody is going to die" briefing paragraph.

The plant-payoff machinery is the most fragile part of the rewrite. §3.2 traces the new plant chains (Diego foreshadowing; Joel firmware admission seed) end-to-end and the existing plants that survive untouched.

Total executed prose: 109,230 words across 18 chapters. Total Plan C1+C7 prose target: ~115,000–119,000 words (net +6,000–10,000). Total time at sustainable PAO+Yeoman cadence: 3-4 weeks.

---

# Section 1 — Per-chapter delta map

For each chapter: current state (1-2 sentences); Plan C state (1-2 sentences); delta type; specific edits needed; sequencing dependency; effort sizing (S = ≤2 hrs new PAO direction, ≤500 words new prose; M = 2-6 hrs PAO direction, 500-2000 words new prose; L = 6-12 hrs PAO direction, 2000-5000 words new prose); risk.

---

## Ch 01 — *Departure* (Day 0, Punta Arenas) — 4,814 words

**Current state:** Voice install + plants — bakery, niece, mother-wound, parka, ex-husband, Joel-93-days, firmware-second-note, Mikael pulse-handshake, the *Nansen* spec, the wardroom briefing, the cabin desk with Diana's drawings. Closes with the boat clearing the Strait at 04:18 on the fifteenth.

**Plan C state:** All voice + plant work preserved. Two additions: (a) one specific line in the wardroom briefing or the engine-compartment scene where Joel mentions in passing that the sensor heads were off-the-shelf because the consortium could not afford the custom-firmware option, AND adds *"the call I am still not sure about"* as a second sentence — this seeds the Ch 17 admission; (b) optionally, one sentence in Anna's "nobody is going to die" briefing close that holds the retrospective frame's gravity without naming the death.

**Delta type:** ADD-ONLY (surgical).

**Specific edits needed:**

- **Edit 1 (load-bearing):** In the wardroom-briefing paragraph at line 115 (*"I told them that the consortium had altered the firmware on three of the racks during the final hold-down. The alteration notes were in the system if anyone wanted to see them. I had read all three and considered all three acceptable."*) — Plan C calls for an additional 2-3 sentences AFTER this paragraph but BEFORE the *"With the benefit of what I learned later"* paragraph at line 117. The addition: a beat in which Anna names that Joel had walked her through the procurement decision before the boat sailed, that Joel had named the trade-off (custom-firmware fork vs off-the-shelf with vendor-signed updates) in his own voice, and that Joel had used the phrase *the call I am still not sure about* when he handed Anna the procurement file. Drafter direction: 80-120 words. The paragraph should land Joel's voice in indirect speech (Anna paraphrasing what Joel said, not Joel's voice direct on the page; the direct voice belongs to Ch 17). The drafter's check: read the paragraph aloud; if it reads as foreshadowing rather than as Anna registering a pre-mission detail at the operational level, revise.

- **Edit 2 (lighter; optional):** In the briefing-close paragraph at line 121 (*"I told them, with a directness I did not soften, that nobody was going to die on this mission if I could help it, and that I was going to help it."*) — Plan C permits ONE additional sentence: *"I helped where I could help. I did not always know which moments would be the ones I could not."* The sentence holds the retrospective frame's gravity without naming Diego or telegraphing the cascade. Drafter direction: the sentence either lands or it does not; if it reads as foreshadowing, omit. Per ANNA-VOICE.md aphorism-close prohibition, this sentence is in the gray zone — it is a retrospective-narrator observation that the executed prose's restraint discipline may not permit. PAO read-aloud test required before retain decision.

- **Edit 3 (atomic plant addition):** Update the YAML frontmatter `plants-set` block: add `joel-firmware-admission-seed` after `firmware-second-note`. The new plant pays in Ch 17.

**Sequencing dependency:** None — Ch 01 changes can be authored independently of any other chapter. Recommend authoring Ch 01 in Wave 2 because Ch 14 (Wave 1) will define what "the call Joel is still not sure about" needs to support, and Ch 01's seed should be calibrated to Ch 14's actual cost.

**Effort sizing:** S. Two paragraph-level additions, one optional. Total new prose: ~150-200 words.

**Risk:** Low. The chapter is a strong asset; the additions integrate at the existing plant rhythm. The optional Edit 2 carries a small register-break risk that the PAO read-aloud will catch.

---

## Ch 02 — *The Recruitment Interview* (Arc 2 — flashback) — 5,594 words

**Current state:** Six-months-before-departure flashback. Anna's video call with Joel. The R1-BLOCK admission (*"I missed it"*). The four technical Q&A exchanges compressed to single representative beats per the v4 directive. Yes/yes recruitment exchange close. Day-14 mission-frame back-anchor.

**Plan C state:** UNCHANGED. The R1-BLOCK admission is the structural model for the Ch 17 admission and must remain at its current altitude. Adding firmware-procurement content here would foreshadow Ch 17 too directly and would break the chapter's discipline of being about *the architect's response to being told he was wrong*, not about the procurement chain that became the architect's later cost.

**Delta type:** UNCHANGED.

**Specific edits needed:** None.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None.

---

## Ch 03 — *Drake Passage and the Ice Edge* (Days 1-7) — 6,428 words

**Current state:** Drake transit. Five crew introductions (Sabina, Diego, Hiroshi, Priya, Wanjiru, Joel) at depth. Diego at the bridge wing at 14:20 Day 2 with the coffee and the polar-operations chart — the Otago 2022 transducer anecdote — *the kind who has the answer on his chart at fourteen-twenty on Day 2 and brings it to the wing at the watch on which the answer is operationally actionable, and not at the meeting where the answer would have been politically useful.* Priya's four-pass calibration scene. Joel's acoustic-mesh rehearsal. Ice-edge dawn arrival on Day 7.

**Plan C state:** UNCHANGED at the prose level. The Diego development in this chapter is the volume's deepest single-chapter Diego work and lands exactly the weight Plan C needs Diego to carry. The reader who registers Diego at the wing on Day 2 will register his absence at the rail on Day 47.

**Delta type:** UNCHANGED.

**Specific edits needed:** None. Optional micro-edit only if PAO read-aloud against Plan C reveals a sentence that would land differently knowing Diego dies — none identified in the prose probe.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None. The existing Diego beats in this chapter are already the gold-standard Plan C carry-forward. They do not need to be touched.

---

## Ch 04 — *First Submersion* (Day 7) — 5,090 words

**Current state:** First sustained captain-asks-engineer scene. Joel walks Anna through the partition-mode transition. Local store as only reality. Relay layer dormant. Gossip protocol dormant. Architectural-claim install for the rest of the volume.

**Plan C state:** UNCHANGED. The chapter installs the dialogue engine; the dialogue engine is what carries Joel's voice in Ch 17. Don't touch.

**Delta type:** UNCHANGED.

**Specific edits needed:** None.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None.

---

## Ch 05 — *The Day-Twenty Realization* (Arc 1) — 6,074 words

**Current state:** Day 14 (mid-Segment 1) realization. Anna queries the local store for a colleague's prior write. The local store answers because it cannot do otherwise. *Everything I am recording right now is only here.* / *This is what Joel built.* The listen-test chapter.

**Plan C state:** UNCHANGED at the prose level. The realization *I am the archive* gains an additional weight under Plan C (the archive will be what María Elena Vargas reads, in addition to what the next mission director reads), but the realization scene itself does not need to anticipate this. The weight will accrue retroactively when the reader reaches Ch 14 and Ch 17.

**Delta type:** UNCHANGED.

**Specific edits needed:** None.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None.

---

## Ch 06 — *First Surface, First Forsaken Reveal* (Day 21-23) — 4,914 words

**Current state:** First surface window. Wanjiru's bandwidth-bounded sync-triage install. Stefan's name first surfaces in the news cycle. Wanjiru's exception-refusal (Diego's undocumented one-off key issuance request; *"the procedure exists for the case where you most want to skip it"*). The forensic-substrate property is installed as an architectural promise.

**Plan C state:** UNCHANGED at the prose level. Wanjiru's discipline lands as Wanjiru's discipline; the sync-mechanic installs the constraint that becomes load-bearing for Ch 11 + Ch 14 + Ch 17. The Stefan-name surfacing is at the right altitude.

**Delta type:** UNCHANGED.

**Specific edits needed:** None.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None.

---

## Ch 07 — *Joel's Sunfish* (Day 22) — 5,403 words

**Current state:** USS Sunfish SSN-649 disclosure. Joel and Anna at the wardroom at Surface 1's quiet hours. *The discipline that runs through the architecture got formed there.* Long Now beat. The architecture's discipline traces to a specific human history.

**Plan C state:** LIGHT SURGICAL EDIT. The chapter is intimate; the discipline disclosure is the chapter's load. Under Plan C, the chapter gains one additional beat that reframes the discipline at the funding-decision altitude. Joel's nuclear-Navy register includes the discipline of resource trade-offs at deployment — a submarine deploys what the budget allows, and the discipline is to operate well within the resource envelope, not to demand a different envelope. Plan C adds one paragraph (or sentence cluster) where Joel observes — in the same restrained register the chapter is calibrated for — that the resource discipline he learned in the Navy is also what made him take the consortium's procurement constraint at face value when he could have advocated harder for the custom-firmware fork. The beat does not yet name the cost; the beat names the discipline at the funding-trade-off altitude.

**Delta type:** SURGICAL-EDIT.

**Specific edits needed:**

- **Edit 1:** Identify the existing paragraph in which Joel discloses the SSN-649 service and the Long Now beat lands. Plan C adds 100-150 words of Joel's voice (or Anna's interior on Joel's voice) at the discipline-of-resource-trade-offs altitude. Drafter direction: Joel does not preach about the funding constraint; Joel observes that the discipline he learned on SSN-649 included the discipline of operating within what was allocated. Anna registers; she does not yet know what the cost of that discipline will be. The reader who re-reads this chapter after Ch 17 will register the gravity. The first-time reader will register it as character depth, not as foreshadowing.

- **Edit 2:** Update the YAML frontmatter `plants-set` block: add `joel-resource-discipline` (or similar slug). Pays in Ch 17.

**Sequencing dependency:** Should be authored AFTER Ch 17 has been drafted, so the Plan C addition can be calibrated to what Joel actually says in Ch 17. Recommend Wave 2.

**Effort sizing:** S-M. 100-200 words of new prose; the calibration against Ch 17 takes the most authoring time.

**Risk:** Low-medium. The chapter is intimate; over-loading it with Plan C content would break its register. The drafter's check: if the addition reads as foreshadowing the Ch 17 admission, revise. The addition should read as Joel's character disclosure at a different altitude than the SSN-649 disclosure — both about the discipline; one about its source, the other about its cost.

---

## Ch 08 — *Second Submersion* (Day 23) — 4,425 words

**Current state:** Sabina's first use-case validation pass. The architecture handles the logistics scenario. Diego pulls Sabina into the dry-run preparation half an hour before the dive. Hiroshi at the data console. Routine-cycle chapter.

**Plan C state:** UNCHANGED at the prose level. Diego's pull-in of Sabina is a Diego beat that survives Plan C unchanged and adds posthumous weight when re-read. The chapter does not need a Plan C addition.

**Delta type:** UNCHANGED.

**Specific edits needed:** None.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None.

---

## Ch 09 — *Subsystem Test — Sync Daemon Under Drift* (mid-Segment 2) — 5,849 words

**Current state:** Mid-Segment-2 sync-daemon drift event. Joel debugs in real time. Priya present in the background. Anchor's behavior under sustained partition. Pattern B log frame.

**Plan C state:** UNCHANGED at the prose level. The chapter installs the architecture's drift-handling claim; nothing about Plan C changes the claim. The chapter does not need a Plan C addition.

**Delta type:** UNCHANGED.

**Specific edits needed:** None.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None.

---

## Ch 10 — *The Aftermath of a Mission That Once Was* (Arc 7) — 4,954 words

**Current state:** Anna's prior-failure interior. The Stefan-mission cut short five years before. The trust-hardening, the inverse-of-betrayal recognition. Joel mentioned only in the recognition that what Anna selected him for is the structural inverse of what failed her last time. *He told me the truth about the BLOCK before I asked him. Stefan never told me.* The Astrid-Lindqvist scene compression per plot-spline P2 is also a candidate for this chapter.

**Plan C state:** LIGHT SURGICAL EDIT. The chapter's prior-failure interior is the structural anchor that makes Anna's recognition of the cost at Ch 14 and Ch 17 land. Plan C adds one beat — Anna's interior naming what she would lose if she lost a member of the current crew, which makes the threat-of-loss specific without naming Diego. The beat is in the chapter's existing register; it is Anna's interior compressed and restrained; it is the kind of beat that re-reads as foreshadowing after Ch 14 and reads as character depth on first pass.

**Delta type:** SURGICAL-EDIT.

**Specific edits needed:**

- **Edit 1:** Identify the existing paragraph in which Anna's prior-mission interior reaches its deepest altitude. Plan C adds 100-200 words of Anna's interior at the *threat-of-loss-becomes-specific* altitude. Drafter direction: Anna names — to herself, in the staff-history file — what she would owe to each member of the current crew if the mission cost her one of them. The naming is specific (each crew member by role and by what Anna has selected them for) but does not foreshadow Diego in particular. Anna's mother-wound feeds the naming: she does not compare them to each other; she does not rank them. The list is the kind of list a commander would write knowing she might have to give it.

- **Edit 2:** Possibly compress the Astrid-Lindqvist scene per plot-spline P2 recommendation (this is a separate edit independent of Plan C but in the same chapter; do them together for efficiency).

**Sequencing dependency:** None. Can be authored independently. Recommend Wave 2.

**Effort sizing:** S-M. 200-300 words of new prose; possibly 500-800 words cut (Astrid-Lindqvist compression).

**Risk:** Low-medium. The threat-of-loss-becomes-specific beat is the chapter's most fragile addition because it is closest to foreshadowing. The drafter's check: if any sentence in the addition names Diego specifically, or names the polar-operations role specifically, revise to a list that does not privilege Diego over Priya or Hiroshi or any other crew member.

---

## Ch 11 — *Second Surface, Second Forsaken Reveal* (Day 37-39) — 5,140 words

**Current state:** Second surface window. Wanjiru's sync-triage as institutional decision-making. Stefan's mission concluded with publicly-favorable results. The Stefan-cross-check race — Wanjiru pushes the boat's archive observations of his mission as the cross-check evidence. The forensic-substrate property is exercised at chapter-load weight for the first time. Anna's love-arc registration as quality-of-attention. Joel still absent from the chapter's main scene.

**Plan C state:** SURGICAL EDIT. Wanjiru's cross-check work generates a question Joel answers in the Day-48 comm-node scene (which is in the executed Ch 15 prose at the 1714 exchange). Under Plan C, Wanjiru's cross-check work in Ch 11 also surfaces — peripherally, as one paragraph that does not yet drive the chapter — the firmware-update-window pattern Joel will later confirm in Ch 17. The addition seeds the supply-chain-pattern thread at the right altitude: Wanjiru notes the pattern; she has not yet pursued it; she will pursue it after Ch 14. Plan C strengthens the seed because Joel's Ch 17 admission needs the supply-chain pattern to have been visible to a careful reader from Ch 11.

**Delta type:** SURGICAL-EDIT.

**Specific edits needed:**

- **Edit 1:** In the scene where Wanjiru cross-checks Stefan's PR cycle against the boat's archive observations, add 150-250 words in which Wanjiru notes — without yet pursuing — the firmware-update-window deviation pattern on the consortium-procurement archive. Drafter direction: Wanjiru reads the pattern; logs the question; sets it aside for transit-north review. Anna registers Wanjiru's having noted something but does not yet ask. The pattern is at the back of the chapter's institutional-substrate register, not at its foreground. The drafter's check: if the paragraph reads as foreshadowing rather than as Wanjiru's institutional discipline doing its work, revise.

- **Edit 2:** Update the YAML frontmatter `plants-set` block: add `wanjiru-firmware-pattern-noted` (or similar slug). Pays in Ch 17 (and is the seed Ch 15 currently logs as `wanjiru-firmware-supply-chain-question`; the slugs may align if the existing prose's slug naming is preserved).

**Sequencing dependency:** Should be authored AFTER Ch 17 has been drafted so the Plan C addition can be calibrated to the specific pattern Joel and Wanjiru name in Ch 17. Recommend Wave 2.

**Effort sizing:** S-M. 150-250 words of new prose.

**Risk:** Low. The chapter already carries Wanjiru's institutional register; the addition extends it at the right altitude.

---

## Ch 12 — *Beginning of the End — Segment 3 Dive* (Day 39) — 4,326 words

**Current state:** Day 39 dive. Segment 3 begins. Diego at the polar-operations station to the right of Mikael, standing. *Diego had not stood at the polar-operations console for an entire bridge watch in Segment 1 or Segment 2. He had taken the chair through the routine watches; he had stood for the partition transitions and the surface preparations and now, at 0611 on Day 39, for the commencement of Segment 3. He would stand through the first two hours of routine submerged ops. He would stand the next morning through the first cross-section against the consortium model. He would — I knew, because I had been on three previous Antarctic missions with him — stand more in Segment 3 than he had stood in Segments 1 and 2 combined.* The conditional-preservation stake planted. The chapter ends with the boat at the operational tempo at the close of Day 39.

**Plan C state:** SURGICAL EDIT. The chapter already does the heaviest Diego-foreshadowing work of any pre-Ch-14 chapter — *"the kind of last-leg work, which is a tightening I have carried before, on other boats, and which has a known shape and a known cost."* Plan C strengthens this by ONE specific addition: a beat at the chapter close in which Diego does something — small, specific, character-typical — that makes the reader register that they have been loving him without knowing they were. Plan C calls for ~100-200 additional words of Diego at the polar-operations console between the chapter's existing close and the back-correction-flagging beat at line 126 (or wherever the chapter's structural break permits).

**Delta type:** SURGICAL-EDIT.

**Specific edits needed:**

- **Edit 1:** Identify a structural seam in the chapter's existing Diego material (most likely between the standing-through-first-two-hours beat and the cross-section-back-correction beat). Plan C adds a Diego micro-scene: he turns to Anna at the rail with the leather mate-cup he carries; he pours and gives her half; he says something at the personal cadence he uses twice across the mission (per Ch 17 line 219); he reads the bathymetry for the next watch's hour without naming what he is reading. The beat is short. The beat is intimate. The beat is what the reader will remember when Diego does not come back. Drafter direction: 150-250 words. Per the anti-pattern §6 in the new SPINE, the beat must not telegraph the death; it must be a beat that earns its place in the chapter's existing structure.

- **Edit 2:** Update the YAML frontmatter `plants-set` block: add `diego-mate-cup-cadence` (or similar). Pays in Ch 14 (the death) and Ch 18 (Diego's leather mate-cup at the gangway, which is already in the executed prose at line 300).

**Sequencing dependency:** None. Can be authored independently. Recommend Wave 2.

**Effort sizing:** S-M. 150-250 words of new prose.

**Risk:** Medium. The chapter is already doing heavy Diego work; the risk is over-loading. The drafter's check: read the entire chapter aloud after the addition; if the chapter now reads as a Diego-death-foreshadowing chapter rather than as a Segment-3-beginning chapter, revise.

---

## Ch 13 — *The Schema That Should Not Migrate* (Arc 4, Day 43-44) — 10,406 words

**Current state:** Priya's schema-migration set piece. The volume's strongest single chapter. Two near-failures during read-confirmation cycle that Priya's three-pass discipline catches. The migration succeeds. Joel executes under Priya's direction. Anna's command authority is the precondition for Priya's safety net. The chapter ends with the boat at the operational state just before the cascade.

**Plan C state:** UNCHANGED at the prose level. The chapter is the volume's strongest character payoff for Priya; under Plan C (in which Diego dies, not Priya), the chapter retains its full weight. Priya's three-pass discipline is what allows the architecture to absorb the schema migration; under Plan C the discipline becomes the institutional-substrate Wanjiru carries forward in the standards-body work. The chapter does not need a Plan C addition.

**Delta type:** UNCHANGED.

**Specific edits needed:** None.

**Sequencing dependency:** None.

**Effort sizing:** None.

**Risk:** None. The chapter is sufficient.

---

## Ch 14 — *The Crossing* (Day 47) — 10,943 words — **LOAD-BEARING REWRITE**

**Current state:** Cascade event at 0317 local. Joel's protective beat — the push past Anna at the access ladder, the bulkhead-door dogging, the eleven-minutes-behind-the-glass beat, the porthole look. Diego survives the chapter at the polar-operations console (giving the two-up-on-starboard-plane and the ventilation-initiate recommendations). The compute hub is collateral damage. Joel emerges at 0353; the boat clears the cascade window; the watch handoff at 0400; the operational damage report filed at 0518; the diary inset (encrypted personal file, Mission Day 49) at the chapter close. Diego's letter-to-María-Elena conversation with Anna at 1647 on Day 48 — Diego announces his retirement decision to San Martín de los Andes. Diego writes the letter that night at 2300+. The chapter closes with the mission continuing on the operational tempo for the rest of Segment 3.

**Plan C state:** **REWRITE-SCENE (the cascade core).** The structural changes:

1. **Diego is at the failure point on the lower deck, not at the polar-operations console.** The Plan C variant 1 directive requires Diego to go down the access ladder FIRST. The mechanism: Diego's polar-operations console is where the sensor-head telemetry comes in at the firmware-diagnostic level. Diego is on the eight-to-four watch when the pre-failure acoustic signature flag fires at 0316:30 — thirty seconds before the breach-class alarm. Diego, reading the flag at the diagnostic level, recognizes what the boat's anomaly detection has not yet escalated to the alarm threshold. He calls compartment two-bravo at 0316:45 to instruct the standing crew member (who in the executed prose is no one — the compartment is unmanned at the standing watch tempo) to evacuate; on confirming the compartment is empty, Diego himself goes to the compartment because the failure pattern matches a sensor-head failure mode he has read on three prior Antarctic deployments and he is the operator best positioned to read the failure at the operational level before the breach-class fires. Diego goes down the access ladder at 0316:55. The breach-class alarm fires at 0317:00. Diego is now at the compartment, at the failure point, in the rising coolant-and-smoke environment.

2. **Anna is on her way to the bridge at 0319.** Unchanged from executed prose.

3. **Joel converges on the access ladder from the engineering compartment** (he had been on the standing post-midnight engineering rotation per the existing prose). He had heard the diagnostic flag at the firmware-watchword level via his per-laptop's standing alert; he had begun moving at 0316:45 the same way Diego had. He reaches the access ladder at 0319 — about thirty seconds after Anna does. He has already inferred that Diego is at the compartment, because the diagnostic flag has Diego's polar-operations-console signature on its capture record and because Joel knows what Diego does when the flag fires at the watchword level.

4. **Joel pushes Anna aside at the access ladder.** Body-discipline beat unchanged from executed prose. The push is the same push the executed prose describes. The motivation in Plan C is now overdetermined: Joel is going past Anna to *both* contain the leak AND retrieve Diego. The executed prose's *He did not look at me. He did not stop. He went past. He went down the ladder.* is the canonical four-fragment and remains exactly as it is.

5. **Joel finds Diego in the compartment.** Diego is unconscious in the coolant-and-smoke environment. Diego's exposure has been roughly four minutes (0316:55 to 0321 — the assessment timestamp in the executed damage report). The boat's medical-rated breathing apparatus is at the lower-deck medical bay (two decks above the compartment); Diego's personal-watch breathing kit is on the polar-operations console (where he left it when he went down the access ladder) because he had been at the console, not at a station that required the personal kit. Diego went to the compartment without breathing apparatus because the failure pattern was a sensor-head leak at the diagnostic level, not yet at the breach-class — and at the diagnostic level, atmospheric containment is procedural-precautionary, not procedural-mandatory. He went because the failure was readable on his console and he was the operator who knew what to read. The architecture preserved his reading; the architecture did not preserve him.

6. **Joel makes the choice.** Joel has been carrying his own personal breathing kit on his belt because the engineering rotation requires it. Joel can attempt resuscitation; the resuscitation may not be successful in the time the cascade window permits before the compartment's atmospheric envelope deteriorates further. Joel must choose between staying with Diego to attempt resuscitation (and risking the compartment isolation order being countermanded, which would compound the cascade) and containing the leak (which is the operational priority specified in the procedure manual) and getting Diego out (which requires extraction equipment that is two decks above). Joel does what the procedure specifies — he isolates the leak source, drains the residual water, contains the smoke ingress. He gives Diego CPR while doing the procedural work in the windows the procedure permits. Diego does not regain consciousness. Joel's compartment-clear declaration at 0353 carries the additional content: *bridge, two-bravo. Leak source isolated. Residual water drained. Smoke ingress contained. Crew member Sá unresponsive; CPR for the duration of containment unsuccessful; readying for medical recovery. Ready to open.*

7. **The bulkhead door opens at 0354.** Maria is at the lower-deck access ladder (per the executed prose). Joel comes out under his own power; Maria's team brings Diego out on the gurney. Maria runs the recovery protocol. Diego does not respond. Maria declares time of death at 0408 against the medical record signed under her Ed25519 device key.

8. **The eleven-minutes-behind-the-glass beat (lines 197-225 of executed prose) is preserved structurally but reweighted.** Anna at the rail still receives Joel's look at the porthole window for the duration the executed prose specifies. The look now carries two weights: the discipline cracking (executed-prose meaning) AND Joel knowing what Anna does not yet know (Plan C meaning — Diego is already gone by the time Joel looks at her). Anna does not yet know; she receives the look as the executed prose describes; the bridge is watching her; her face does not change. The execution of the look-receiving discipline is unchanged. What changes is what Anna later learns the look had also been saying.

9. **The diary inset at the chapter close is rewritten** to carry both weights. The executed prose's diary inset at lines 481-527 is preserved structurally; the Plan C version expands by approximately 150-250 words at the deepest interior altitude the chapter has earned to include Anna's recognition that Joel had been looking at her through the glass knowing what was on the other side, and that the receiving she did at the rail was — in addition to everything else — the last duty Diego's discipline required of her at her command position.

10. **The damage report at 0518 is rewritten** to include the crew-fatality clause: *Crew status: one fatality. Sá, D., Senior Polar-Operations Specialist; cause of death (preliminary): asphyxiation and thermal injury in the post-leak compartment environment; declared at 0408 by the medical officer; medical record signed at hash-chain integrity. No other injuries beyond R. minor abrasion.*

11. **The Diego retirement-to-San-Martín-de-los-Andes scene at 1647 on Day 48 is rewritten** as a posthumous beat. Anna does not speak with Diego that day; Diego is not at his cabin between 1620 and 1645; Diego is at the morgue compartment (the boat's small refrigerated space configured for medical-emergency body preservation per consortium standing-equipment requirement). The Diego-retirement content does not happen at 1647 on Day 48 in Plan C; the retirement decision Diego had been carrying gets surfaced through a different channel — most likely a single notebook entry Diego had been keeping at his cabin desk, which Maria recovers when she clears his personal effects per the standing post-fatality protocol, and which Anna receives from Maria at the wardroom on Day 50. The notebook carries the retirement decision in Diego's handwriting; Anna does not narrate her reading of it at length; the notebook is now in the staff history as the artifact Diego left at the cabin desk, signed at his KEK in the canonical authored-content archive, dated Day 44. The drafter's check: the notebook entry must be character-explicable from Diego — it carries his Spanish-and-English parallel-translation practice, his IAA-institutional bearing, his discipline of writing decisions at the moment he made them. The notebook entry is the artifact that lets the executed prose's María-Elena letter beat carry forward unchanged in Ch 17 (Diego had finished the letter at 2147 on Day 55 in the executed prose; in Plan C the letter is the letter Diego finished at the wardroom table on Day 44, dated under his hand, sealed at his cabin desk, found by Maria, brought to Anna, and now carried to María Elena at the post-handshake mirror with the same priority routing).

12. **The chapter close at lines 463-479 is unchanged structurally** but the *capability-degradation-visible-in-what-the-crew-does-and-does-not-do* paragraph at line 377-389 gains an additional beat: Diego's polar-operations console is at the standing position; the chair is empty; the higher-refresh bathymetry feed Diego had set at the start of the dive sequence holds the configuration for the back nine days because no one changes it; Hiroshi acquires the polar-operations console rotation in addition to the chief-scientist's; the boat operates at the reduced-staffing-and-reduced-capability tempo for the rest of Segment 3.

**Delta type:** REWRITE-SCENE (the cascade core ~lines 197-323; the diary inset ~lines 481-527; the post-cascade Day-48 sequence ~lines 397-479). Total structural rewrite: ~2,500-3,500 words. Total chapter word count target: ~12,500 words (currently 10,943; the Plan C version is ~1,500-2,000 words longer, within the executed-prose Ch 14 target range that the original outline specified).

**Specific edits needed:** Per items 1-12 above. Drafter authoring this chapter requires:

- The executed prose ch14 file at hand at all times (preserve 70%+ of existing text)
- The Plan C SPINE addendum A (*grief at the institutional register, never at the narrator register*) at hand as the voice gate
- The Plan C SPINE anti-pattern 6 (*Diego's death is not thematically justified*) at hand as the prose gate
- PAO direction on every paragraph that touches Diego in the post-cascade sequence

The drafter's iterations should be PAO-reviewed at three checkpoints: (a) after the cascade-core rewrite drafts; (b) after the diary-inset rewrite drafts; (c) after the chapter is complete and a read-aloud pass has been done. Three iterations is the default; if the chapter cannot land in three iterations, halt and consider whether Plan H (architecture-is-wrong instead of death-of-Diego) is the better path. The halt condition is named in the new SPINE's Plan C FAILED-conditions clause.

**Sequencing dependency:** **This is the load-bearing chapter for Plan C.** It must be authored FIRST (Wave 1, alongside Ch 17 and Ch 18) because every other Plan C change is calibrated against what this chapter actually delivers. The Wave 2 foreshadowing additions and the Wave 3 reframing edits all depend on Ch 14's specific death-scene execution. Authoring foreshadowing before the death scene exists is the AP-13 (confidence-without-evidence) trap.

**Effort sizing:** L. 2,500-3,500 words of substantive rewrite; total chapter authoring effort ~10-15 PAO hours; total chapter authoring time at sustainable cadence ~1 week. This is the longest chapter in the volume; the rewrite is the most complex authoring work in Plan C.

**Risk:** HIGH. The chapter is Plan C's single biggest execution risk. The risks specifically:

- **Voice risk:** Anna's voice has not been calibrated for sustained grief. The death of Diego at the cascade close + the diary inset at the chapter close is the highest interior-altitude pressure the voice has ever been tested under. The Plan C kill-trigger names this — if three drafting passes cannot produce a death scene that lands within Anna's voice, halt and reconsider via Plan H.
- **Pacing risk:** The chapter is currently 10,943 words and structurally tight. Adding 1,500-2,000 words requires careful authoring to preserve the existing pacing. The risk is the rewrite balloons past 12,500 words or breaks the eleven-minutes-at-the-rail beat's tension.
- **Plant-payoff risk:** The chapter sets multiple plants (joel-porthole-look, diego-retirement-san-martin, diego-letter-maria-elena, wanjiru-firmware-supply-chain-question, compute-hub-total-loss) that pay in later chapters. The Plan C rewrite must preserve all of these or restructure the plant-payoff chains in the corresponding chapters. See §3.2 for the plant-payoff audit.
- **Anti-pattern risk:** Per the new SPINE anti-pattern 6, the rewrite must not write Diego's death as thematically justified. The kill-trigger: if the draft includes any sentence in which Diego's death "means" something, revise. The drafter's check: if any sentence in the chapter would land differently if Diego had survived, that sentence is doing thematic work the chapter must not do.

**Halt conditions for the Ch 14 rewrite:** If after three full drafting passes (a) the death scene does not land within Anna's voice, OR (b) the chapter balloons past 12,500 words, OR (c) any reviewer (PAO or CIC) identifies the chapter as thematically over-determined, file a `pao-question-*` to Admiral and consider Plan H. The Ch 14 rewrite is the bottleneck for the whole Plan C execution; if it cannot land, the rest of Plan C is moot.

---

## Ch 15 — *The Compromised Relay Holds* (Day 47-48) — 7,368 words

**Current state:** Wanjiru's chapter. Three-threat-models recognition (security-architecture-under-political-attack + environmental-degradation + compute-hub-loss). Forensic-substrate beat at chapter-load weight — Wanjiru's queries on the starboard sensor head's firmware-update history at laptop-class. Joel arrives at the comm node at 1714 without being called. The Day-22 Diego scene reference. *The relay held. Wanjiru held. The architecture held what we asked it to hold.*

**Plan C state:** REFRAME (light surgical edits throughout). The chapter is structurally intact — Wanjiru is still the chapter's lead voice; the three-threat-models recognition still holds; the forensic-substrate beat still lands. What changes under Plan C is the chapter is now operating in the immediate post-Diego-death shadow. Several specific edits:

- **Edit 1 (Wanjiru's interior):** The three-threat-models recognition now extends to FOUR — security-architecture-under-political-attack + environmental-degradation + compute-hub-loss + *the-threat-the-architecture-could-not-protect-against-the-threat-of-the-person-being-mortal*. This is the chapter's most fragile addition because it risks crossing into anti-pattern 6 (thematic justification). Drafter direction: the fourth recognition is named once, at low altitude, in Wanjiru's interior; it does not become the chapter's thesis. The chapter's thesis remains the three structural-defenses-against-three-threat-models; the fourth recognition is a note Wanjiru makes to herself that the architecture's structural defenses are insufficient for the case the boat just lost.

- **Edit 2 (the forensic queries):** Wanjiru's queries on the starboard sensor head's firmware-update history now carry the weight of *this is the trail we follow because we owe it to the person we lost.* Drafter direction: this weight is in the chapter's atmosphere, not in its prose. Wanjiru does not narrate the debt; she pursues the query at the institutional discipline she pursues queries at; the reader infers the weight from the difference between what Wanjiru does in this chapter and what she would have done if the boat had not lost Diego.

- **Edit 3 (the chapter close):** *The relay held. Wanjiru held. The architecture held what we asked it to hold.* This three-fragment close survives unchanged structurally. Plan C extends it by ~50-80 words at the diary-inset level — Anna's interior on what the architecture held, including the implication that what the architecture held did not include Diego. The extension is one paragraph; it is at the lowest altitude the chapter's restraint permits.

- **Edit 4 (Diego at the polar-operations console):** Several references in the executed prose (lines 94, 344) carry Diego at the polar-operations console after the cascade. Under Plan C these are revised to *the polar-operations console was at its standing position; the chair was empty; Hiroshi had acquired the rotation*. Drafter direction: do not over-narrate the empty chair; the executed prose's discipline of registering the architecture's reduced-capability state through what the crew does and does not do extends to registering Diego's absence through the empty chair.

**Delta type:** REFRAME (multiple surgical edits across the chapter).

**Specific edits needed:** Per items 1-4 above. Drafter authoring this chapter requires the new Ch 14 prose at hand at all times.

**Sequencing dependency:** Must be authored AFTER Ch 14 (Wave 1). Recommend Wave 3.

**Effort sizing:** M. 400-600 words of new prose; multiple reference-revisions throughout (Diego at the console → console empty; Hiroshi rotation acquired). Total authoring time ~3-5 PAO hours.

**Risk:** Medium. The chapter's three-threat-models recognition is calibrated for restraint; extending to four threat models risks crossing into thematic justification. The drafter's check: read the chapter aloud; if the fourth-recognition addition reads as the chapter's thesis, revise. The chapter's thesis stays at the three structural-defenses; the fourth recognition is a footnote at Wanjiru's interior.

---

## Ch 16 — *Final Ascent* (Day 49-52) — 4,579 words

**Current state:** Day 49-52. Segment 3 ends; boat surfaces at Punta Arenas approach. Anna's *queries to run when we surface* list grows. Joel quietly satisfied. Diego quietly grounded; does not yet announce his retirement decision. The chapter is denouement; the emotional payoff is restraint, not triumph.

**Plan C state:** REWRITE-CHAPTER (light at the prose level; substantial at the reference level). Diego is dead; the chapter's references to Diego need to be replaced with references to Diego's absence; the post-mission-handover topics Anna would have discussed with Diego (Filchner-Ronne paper; consortium-handoff for the IAA contribution; the chief-scientist-billet recruitment timeline) are now topics Anna must hold for the post-mission cycle in Diego's absence; the *queries to run when we surface* list now includes the specific items Diego's death has surfaced — María Elena Vargas notification protocols, IAA institutional bereavement procedures, the post-mission consortium handover of Diego's photographs and unfinished Filchner-Ronne paper, the consortium-logistics-van timing for Diego's body return to Buenos Aires.

**Delta type:** REWRITE-CHAPTER at the reference level; the chapter's structural arc (denouement; reduced-capability state; restraint as payoff) survives unchanged.

**Specific edits needed:**

- **Edit 1 (references):** Every reference to "Diego quietly grounded; does not yet announce his retirement decision" or equivalents is revised. Diego's absence at the bridge, at the wardroom, at the polar-operations console is the chapter's load-bearing absence. Drafter direction: do not over-narrate; let the absence operate at the same restraint discipline the executed prose has been using for capability degradation.

- **Edit 2 (the queries list):** The *queries to run when we surface* list expands in this chapter from ~9 items (executed prose at line 393 of Ch 14, by Day 48) to ~25-30 items by Day 52. The specific items related to Diego's death (María Elena notification, IAA bereavement, consortium-logistics-van, Diego's Filchner-Ronne paper, the chief-scientist-billet, the polar-operations-billet) populate the list at the appropriate points. Drafter direction: Anna does not narrate her grief through the list; the list is what it is — a paper artifact at the cabin desk, growing at the rate Anna can write items on it.

- **Edit 3 (the chapter close):** The chapter currently closes on the boat's denouement state. Plan C extends by ~150-250 words at Anna's interior, in which she names — once, at low altitude, in the diary file — what the next four days of transit will require. The naming is operational: María Elena's notification will happen at the Punta Arenas surface handshake; the IAA's institutional bereavement procedures will run at the institutional level; the boat must make Punta Arenas at the operational tempo; the work of writing the staff history continues. The closing image of the chapter is Anna at the desk having added items to the list and closing the per-laptop for the night.

**Sequencing dependency:** Must be authored AFTER Ch 14 (Wave 1). Recommend Wave 3.

**Effort sizing:** M. 600-1,000 words of new prose; multiple reference-revisions. Total authoring time ~5-7 PAO hours.

**Risk:** Low-medium. The chapter is short and structurally simple; the risk is the references-to-Diego edits multiply across the chapter and produce a chapter that is dominated by Diego's absence rather than by the architecture's operational tempo. The drafter's check: the chapter is still a denouement-of-the-mission chapter, not a grieving chapter. The grief operates at the floor; the operation operates at the surface.

---

## Ch 17 — *Transit North* (Days 52-56) — 5,146 words — **LOAD-BEARING REWRITE**

**Current state:** Day 53-55 transit. Wanjiru's request for the staff history at 1640 on Day 53. The forensic-substrate analysis at the wardroom table at 1900 on Day 54 — Joel and Wanjiru working through the firmware-update history, the vendor's ownership pattern (Pacific Hydroacoustic Systems / Helvetia Trust SA partnership), the cross-mission firmware-update timing pattern, the post-patch low-frequency component. Joel's *we couldn't afford to fork the firmware* honest-engineering beat. Wanjiru's *the consortium will need a standards body* institutional beat. Diego sealing the letter at 2147 on Day 55. The regulatory filing — preliminary draft, Mission Day 55, 2312 local.

**Plan C state:** **REWRITE-SCENE (the Joel admission landing).** The chapter currently has Joel's *we couldn't afford to fork the firmware* as honest-engineering observation but does NOT have Joel's *I could have funded the fork at the pre-procurement budget cycle and chose not to* admission. Plan C requires the admission. The structural changes:

1. **The forensic-substrate analysis at the wardroom table at 1900 on Day 54 proceeds substantially as the executed prose has it.** The walking-through of the firmware-update history, vendor's ownership pattern, cross-mission firmware-update timing pattern, post-patch low-frequency component all preserve their existing structure. The *inconclusive but suggestive* register is preserved. The data is preserved. The structural shape of Joel-and-Wanjiru reading the panel and naming the two readings is preserved.

2. **Joel's *we couldn't afford to fork the firmware* beat at line 163 expands.** The executed prose has Joel saying *we couldn't afford to fork the firmware. The consortium's funding model does not support a sensor-head firmware fork. The consortium does not have the engineering depth to maintain a fork of every off-the-shelf instrument's firmware against the manufacturers' release cycles. We integrated their patch because their patch was what was available. The architecture's job is what it is doing right now — surfacing the analysis that is possible because we held the full pre-failure timestream of every edge device. We could not have prevented this compromise. We can document what the data shows. That is enough for now.*

   Plan C adds the admission after this paragraph, in a new paragraph in Joel's voice, at the same restraint discipline the executed prose has been carrying for Joel:

   > *He was quiet for the duration the kettle had been off the warmer.*
   >
   > *He said: "I could have funded the fork at the pre-procurement budget cycle. The budget cycle was September of 2022. I had the line item; I reviewed the line item against the architecture's first-year deployment costs; I marked the line item as deferrable to the second-year cycle on the reading that the vendor-signed update chain would carry the deployment without a fork. The reading was the right reading at the time I made it. The reading is the reading the data supports tonight. The reading was honest engineering. The reading does not survive the compartment."*
   >
   > *He said: "I chose the budget. The cost is in the compartment."*
   >
   > *He did not narrate further.*
   >
   > *Wanjiru did not narrate.*
   >
   > *I took the half-beat. The half-beat would carry to the record at the diary level, not at the institutional level. The institutional level was at the regulatory filing's inconclusive register. The diary level was at the level the diary could carry.*

   The exact text above is a drafter target; the drafter may revise within the Plan C SPINE addendum B constraint (the admission lands as character revelation, not as authorial preaching). The admission must be: (a) in Joel's voice; (b) one short paragraph; (c) without softening, defense, or deflection; (d) without explanation of consequences for Anna's or the reader's listening benefit. The drafter's check: read the admission paragraph aloud; if any sentence explains rather than names, revise.

3. **Wanjiru's *the consortium will need a standards body* beat at line 167 is unchanged at the structural level** but gains one additional sentence following the standards-body naming: *None of that exists. It will need to. The cost is at the compartment.* The addition links Wanjiru's institutional beat to Joel's admission without making either of them carry the other's weight. Drafter direction: the sentence is Wanjiru's voice, at her institutional register; she does not over-name what Joel just named.

4. **The Joel admission addition triggers cascade revisions throughout the rest of Ch 17.** Specifically: (a) Anna's *I went to my cabin / I added a paragraph to the file* sequence at lines 187-199 now carries the admission as the chapter's load-bearing addition to the staff history. The paragraph Anna adds at the file now is not only about the OSS-funding-asymmetry as architectural-philosophical insight; it is about Joel's admission at the wardroom table. The drafter's check: Anna does not narrate her reception of the admission at length; she records it at the institutional register the staff history requires, and the reception is preserved at the diary level. (b) The regulatory-filing-preliminary-draft at lines 231-259 is unchanged at the institutional level; the filing remains inconclusive because the inconclusiveness is the data's. (c) The diary close at line 273 (*I closed the file. I closed the per-laptop. I went to bed.*) is unchanged.

5. **Diego sealing the letter at 2147 on Day 55 is replaced by a different scene under Plan C.** Diego is dead; he did not seal a letter at 2147 on Day 55 because he was not alive at 2147 on Day 55. The letter Diego had written is the letter dated Day 44 (per the Ch 14 Plan C edit 11), which Maria recovered from his cabin desk after his death, which is now at the canonical authored-content archive under Diego's KEK, and which is in the priority queue Wanjiru sets for the Punta Arenas surface handshake. Plan C replaces the executed-prose Day-55 letter-sealing scene with a different scene: Anna at the wardroom table at the same hour, reading the IAA's institutional bereavement protocol for the next-of-kin notification at María Elena Vargas's address in Belgrano, drafting the consortium-handshake-side notification letter that will go alongside Diego's letter at the post-handshake mirror. Drafter direction: ~400-600 words. Anna's voice at the institutional register; the notification letter is the operational artifact she has to write; the personal letter (Diego's) is the artifact that goes alongside. The two are at the institutional level. The diary will carry what the institutional level does not.

6. **The chapter close** at lines 277-305 (the Day 56 surface-approach brief, *the record is in my hands*) is unchanged structurally. The line *the file was at twenty-three thousand words against the back year of writing* is preserved exactly.

**Delta type:** REWRITE-SCENE (the wardroom Day-54 admission ~lines 159-185; the Day-55 letter-sealing scene is replaced ~lines 203-227; cascade revisions at lines 187-199 and lines 219-227). Total structural rewrite: ~1,500-2,500 words. Total chapter word count target: ~6,000-6,500 words (currently 5,146).

**Specific edits needed:** Per items 1-6 above.

**Sequencing dependency:** Must be authored alongside Ch 14 in Wave 1, because Ch 17's admission is calibrated to the cost Ch 14 names (Diego), and the Day-55 letter-sealing scene replacement is calibrated to the Day-44 letter Diego wrote per Ch 14's edit 11.

**Effort sizing:** L. 1,500-2,500 words of substantive rewrite; total chapter authoring effort ~6-10 PAO hours; total chapter authoring time at sustainable cadence ~3-4 days.

**Risk:** Medium-high. The chapter's load-bearing risk is the Joel admission. Per the new SPINE addendum B and anti-pattern 7, the admission must land as character revelation (not authorial preaching) and Joel must not be written into the villain position (he is an honest engineer absorbing the cost of an honest decision). The drafter's check: read the admission paragraph aloud; if it carries any sentence that would land Joel as the architect-who-should-have-known, revise. The distinction between *could-have-and-the-cost-arrived* and *should-have* is the chapter's load-bearing distinction.

**Halt conditions for the Ch 17 rewrite:** If after three drafting passes (a) the admission does not land within Joel's voice, OR (b) the admission reads as Joel-as-villain, OR (c) the regulatory-filing-inconclusive register is undermined by the admission's character weight (the filing must remain procedural and inconclusive even with Joel's admission in the staff history), file a `pao-question-*` to Admiral and consider whether the admission needs to be at lower altitude (one sentence rather than one paragraph) or whether Plan C's Joel-admission lock needs CIC reconsideration.

---

## Ch 18 — *Punta Arenas Surfacing* (Day 56) — 7,777 words — **LOAD-BEARING REWRITE**

**Current state:** Final mission log at 0441. Punta Arenas dockside surfacing-and-mooring. Consortium reception room at 0512. Wanjiru drafting the standards-body framework in real-time at full bandwidth. Anna's queries-to-run-when-we-surface list at 26 items; the architecture closes the gap at the post-handshake throughput. The reception at 0512. The thirty-second exchange with Stefan. The disembarkation across two hours. Hiroshi's unfinished-line drawing beat (Vol-3 forward-plant). Diego at the gangway at 0728 with the sea-bag — *The architecture had not preserved Diego. The architecture had not been the architecture for Diego. The architecture had been the architecture for what Diego had made. Diego had preserved Diego.* The hotel room desk. The final personal-file diary inset. *The file is open. I am at the desk. / I closed the file. / I opened the file. / I added a paragraph.*

**Plan C state:** **REWRITE-CHAPTER (multiple structural revisions).** Diego is dead; the chapter's two largest scenes (Diego at the gangway at 0728; the *Diego preserved Diego* recognition) are restructured. The chapter's other major beats (Stefan exchange; Hiroshi unfinished-line; Wanjiru standards-body drafting; Anna at the desk) survive structurally but are reweighted. The structural changes:

1. **The final mission log at 0441 is rewritten** to include the crew-fatality clause. *Crew complement: ten at departure; nine at return. Crew fatalities: one. Sá, D., Senior Polar-Operations Specialist; Mission Day 47, leak event; cause of death (preliminary): asphyxiation and thermal injury in the post-leak compartment environment; declared at 0408 by the medical officer; consortium next-of-kin notification protocol initiated against the institutional cycle at the post-handshake.*

2. **The dockside arrival sequence at 0441-0512** is unchanged structurally; the consortium reception team comes across the gangway as the executed prose has it; the medical-clearance officer, customs officer, logistics officer, Holm. Plan C extends by one scene: a member of the consortium's bereavement-and-next-of-kin officer joins the dockside team within minutes of mooring, to begin the IAA's institutional bereavement protocol for Diego's family. The scene is short — 100-200 words. Drafter direction: the protocol is procedural; Anna and the bereavement officer exchange the protocol-required communications; the body is transferred to the consortium-logistics-van within the first hour at the dockside; the institutional handshake operates as the institutional handshake operates.

3. **The consortium reception room at 0512** runs as the executed prose has it; Wanjiru at the per-laptop drafting the standards-body framework in real-time; Anna at the small table with the list. Plan C reweights this scene at the diary altitude — Anna's interior at the small table now carries the knowledge that the list she is closing is also the list that Diego could not close. The list expansion from Ch 16 (María Elena notification; IAA bereavement; consortium-logistics-van timing; Diego's Filchner-Ronne paper; the chief-scientist-billet) closes in this scene at the same full-archive RAG support the architecture provides. Anna's queries-to-run-when-we-surface list is now closing the items related to Diego's death AND the items related to the routine post-mission cycle, and the architecture closes them at the same operational tempo because the architecture does not distinguish between *what the next mission director will need* and *what María Elena Vargas will need*.

4. **The thirty-second exchange with Stefan at 0517** is unchanged at the executed prose's altitude. The exchange is the institutional exchange the executed prose describes; the witnesses are at their stations; the pause is the three-second pause the executed prose carries; Stefan does not say what he could have said. Under Plan C, the exchange carries an additional weight Anna does not narrate aloud: Diego's body is at the consortium-logistics-van that pulled away thirty-five minutes ago, and Stefan does not know Diego is gone. The exchange operates at the institutional register; the asymmetry of knowledge is the silent third party at the exchange. Drafter direction: do not narrate the asymmetry; the institutional register holds; Anna registers the silence; Stefan registers nothing because he does not yet know.

5. **The disembarkation across two hours** is unchanged structurally for Priya, Sabina, Maria, Joel, Wanjiru. Hiroshi's unfinished-line beat at 0712 is preserved structurally and pays the Vol-3 forward-plant unchanged. Plan C's load-bearing change is at the Diego-at-the-gangway-at-0728 scene at lines 270-307.

6. **The Diego-at-the-gangway-at-0728 scene is REPLACED with a different scene at the same chapter position.** In the executed prose, Diego comes to the gangway with his sea-bag; he and Anna exchange the institutional retirement-confirmation; he gets in the consortium-logistics-van; the van pulls away into the Punta Arenas pre-dawn; *Diego had preserved Diego.* In Plan C, this scene cannot occur because Diego is dead.

   The Plan C replacement: **Anna walks to the secondary consortium-logistics-van** (the one that came for Diego's body in the morning), now empty, at the dock at the same hour Diego would have been at the gangway. The van pulled away with Diego at 0507 — twenty-one minutes before the reception began. Anna had been at the bridge through the surfacing-and-mooring; she had been at the reception room during the body transfer; she did not see the van leave. The van is gone. The dock is at its standing morning state. Maria, at her station for the per-crew clearance dossiers, comes to the dock at 0728 to confirm with Anna that the institutional bereavement protocol is at the standing tempo and that María Elena Vargas will receive the body at Buenos Aires within the next 96 hours per the IAA's standing-equipment requirement. Maria gives Anna the sealed envelope with Diego's letter (the Day-44 one, recovered from his cabin desk) and Diego's leather mate-cup with the unpolished bombilla (which the consortium's standing-personal-effects protocol returns to the next of kin via the institutional channel). Anna takes both. The mate-cup goes to María Elena. The letter is what María Elena will read at the kitchen table in Belgrano.

   Drafter direction: ~400-600 words. The scene is short. Anna does not narrate her grief. The mate-cup is the artifact. The letter is the artifact. The architecture preserved both. The architecture did not preserve Diego. The recognition at the end of the executed-prose scene (*The architecture had not preserved Diego. The architecture had not been the architecture for Diego. The architecture had been the architecture for what Diego had made. Diego had preserved Diego.*) is preserved EXACTLY in the Plan C version, because it is the volume's load-bearing sentence-cluster and stands without revision under Plan C. The recognition now lands at the moment Maria hands Anna the mate-cup and the letter, rather than at the moment the consortium-logistics-van pulls away. Both moments are structurally the same moment at different chronologies.

7. **The hotel room at the Hotel Dreams del Estrecho** (lines 309-353) is unchanged structurally. Anna at the desk. Wanjiru at the door at 1147 asking the institutional retreat of the staff-history convention. Anna closes the per-laptop; opens a different file; the final personal-file diary inset begins.

8. **The final personal-file diary inset at lines 355-388** is rewritten at the Plan C altitude. The executed-prose diary inset carries:
   - The thirty-seconds-with-Stefan reflection
   - The Joel-at-the-wardroom-on-Day-44 reflection
   - The Hiroshi-drawing-for-forty-five-years reflection
   - The Wanjiru-at-the-standards-body reflection
   - The Diego-going-home / architecture-not-the-architecture-for-Diego reflection
   - The next-mission-director / convention-older-than-the-architecture closing
   - *She will read it at the start of her selection cycle. She will not know my name until she opens the file. She will not need to.*
   - *The file is open. I am at the desk.*

   The Plan C revision: the Diego reflection (currently the fifth item in the inset) is rewritten at the new Plan C weight. *Diego is going home. The architecture preserved his photographs and his logs and the letter and the paper. The architecture did not preserve him. He preserved himself. The architecture was the architecture for what he made. The desk at the lake side of the road into San Martín de los Andes is what he will write at. María Elena will cook in the kitchen. Sofía will come at school holidays. The architecture is not the architecture for any of that.*

   Becomes:

   *Diego is at the consortium-logistics-van at the Buenos Aires post-handshake. The van that carried him pulled away from the dock at 0507 local this morning. María Elena will receive the body at the IAA's institutional handshake within ninety-six hours. The desk at the lake side of the road into San Martín de los Andes will hold the letter Diego wrote on Mission Day 44 at the wardroom table, and the photographs from the under-ice transit on Mission Day 35, and the Filchner-Ronne paper at its draft state, and the leather mate-cup with the unpolished bombilla. Sofía will know who her grandfather was. María Elena will know what her husband had been writing the morning he died. The architecture preserved what Diego made. The architecture did not preserve him. He preserved himself. He preserved himself in the moment his body chose to go to the failure point at the operational tempo he had been carrying for thirty-five years. The architecture was the architecture for what Diego had made. The architecture is not the architecture for any of that.*

   The structural shape is preserved (the architecture-vs-the-man recognition); the content is rewritten at the Plan C weight (Diego dead at the failure point, not Diego retiring to San Martín). The closing image of the diary inset — *She will read it at the start of her selection cycle. She will not know my name until she opens the file. She will not need to.* — is unchanged exactly.

9. **The Anna's-choice beat (the volume's real climax under Plan C)** lands in the closing sequence at lines 391-421. Plan C reweights this passage to make the choice explicit: Anna chooses to write Joel's admission into the staff history file at the institutional record level. The passage *I added a paragraph. The paragraph carried Punta Arenas at 0441 and the dock and the gangway and the reception and the disembarkation and Diego at the gangway and Hiroshi at the reception and Wanjiru at the door. The paragraph did not narrate. The paragraph carried what had been done at the institutional level.* is unchanged structurally; the paragraph Anna adds now also includes Joel's admission, at the institutional register the staff history requires. The drafter's check: Anna does not narrate the choice; the choice is in the act of writing the paragraph. The reader infers the choice from the paragraph's content.

10. **The Diana-postcard close at lines 423-429** is preserved structurally unchanged. Anna prints the Ushuaia postcard for Diana at the card printer on the desk; she addresses it; she writes the brief D — message; she sets it on the desk beside the list. Under Plan C, the message text shifts slightly: *D — From Punta Arenas. The boat is safe. The crew is safe (one of us did not come home; I will tell you about him when I see you). I am at the desk. Tell me what is new at the building. — A.* The parenthetical is Anna's first acknowledgment of Diego's death at the niece-level; it lands at the diary-level register because Diana is family; it lands at one sentence because Anna does not narrate.

   ALTERNATIVELY (and possibly better): the postcard goes UNCHANGED in its message text. Anna does not tell Diana about Diego at the postcard level; she will tell Diana when she sees her, at the kitchen table in Voronezh, in person. The postcard remains at its specific image (the *medialunas* in Ushuaia; *the boat is safe*; *tell me what is new at the building*). The reader infers Anna's discipline of not bringing the death to a five-year-old at the postcard level. The PAO read-aloud test will decide between the two options; CIC may want to weigh in.

11. **The final mission-record-closed log at lines 433-435 is rewritten** to carry the consortium-next-of-kin-notification-pending status. *Mission record closed at the consortium-port mirror at Punta Arenas. Final hash-chain attestation filed. Staff history pending at the post-mission documentation cycle. Consortium next-of-kin notification for Sá, D., pending at the institutional cycle.* The closing line *End of the maiden voyage.* is unchanged.

**Delta type:** REWRITE-CHAPTER (multiple structural revisions across the chapter; estimated 2,000-3,500 words of substantive rewrite within a chapter that holds at ~7,500-8,200 words). Most chapter scenes survive structurally; the Diego-at-the-gangway scene is fully replaced; the diary inset's Diego paragraph is rewritten; the chapter's final paragraph adds the Joel admission to the staff-history record.

**Specific edits needed:** Per items 1-11 above.

**Sequencing dependency:** Must be authored alongside Ch 14 and Ch 17 in Wave 1 because Ch 18's load-bearing scenes (the secondary-logistics-van scene; the diary inset; the final staff-history-record paragraph) are calibrated to what Ch 14 and Ch 17 actually deliver.

**Effort sizing:** L. 2,000-3,500 words of substantive rewrite; total chapter authoring effort ~10-15 PAO hours; total chapter authoring time at sustainable cadence ~5-7 days.

**Risk:** High. The chapter is the volume's closing artifact; the rewrite must preserve the existing closing-image (*The file is open. I am at the desk. … I kept writing.*) while reweighting the chapter's main scenes at the Plan C altitude. The specific risks:

- **Pacing risk:** The Diego-at-the-gangway scene replacement (item 6 above) is structurally heavy and risks expanding the chapter past 8,500 words.
- **Voice risk:** The final diary inset is the volume's last sustained interior altitude; Anna's voice must carry the rewritten Diego paragraph at the same restraint discipline the rest of the inset is calibrated for. The drafter's check: read the entire diary inset aloud; if the Diego paragraph reads as the inset's climax (rather than as the inset's fifth-of-five reflection at the same altitude as the other four), revise.
- **Anti-pattern risk:** The chapter's Anna's-choice beat (item 9 above) risks crossing into the thematic-justification anti-pattern. The drafter's check: the paragraph Anna writes at the institutional level must read as a procedural act of recording Joel's admission, not as a heroic act of surfacing the truth. Per the new SPINE's commercial-reading-vs-literary-reading register split, the heroic-act-of-surfacing reading is the airport-thriller register; the procedural-act-of-recording reading is the literary-techno-thriller register Plan C is committed to.

**Halt conditions for the Ch 18 rewrite:** If after three drafting passes (a) the Diego-at-the-gangway replacement scene does not land at the volume's restraint discipline, OR (b) the diary inset's Diego paragraph breaks the inset's pacing, OR (c) the Anna's-choice beat reads as heroic rather than procedural, file a `pao-question-*` to Admiral. The Ch 18 close is the volume's last artifact and must land within the voice the rest of the volume has earned.

---

# Section 2 — Prioritized wave plan

The wave plan sequences the chapter rewrites in the order that minimizes risk: load-bearing structural rewrites first (Wave 1); the foreshadowing additions that depend on them second (Wave 2); the reframing edits third (Wave 3); the consequence ripples last (Wave 4).

The waves are not strictly sequential; some Wave 2 work can begin before Wave 1 closes, provided the load-bearing scenes are at draft state. The waves are sequenced by dependency, not by calendar.

## Wave 1 — Load-bearing structural rewrites (Week 1-2)

**Chapters: Ch 14, Ch 17, Ch 18.** These three chapters are the new spine of Plan C1+C7; nothing else lands without them.

**Sequencing within the wave:**
- **Ch 14 first.** The cascade-with-Diego-death is the volume's load-bearing scene. Until it lands, the rest of Plan C is theoretical.
- **Ch 17 second.** Joel's admission is calibrated to the cost Ch 14 names. The admission cannot be authored until Ch 14's death-scene altitude is determined.
- **Ch 18 third.** The closing chapter is calibrated to both Ch 14 (the death) and Ch 17 (the admission). The staff-history desk choice is calibrated to what the staff history actually carries.

**Iteration discipline within the wave:** Three iterations max per chapter at this wave (per the Halt-conditions specified in the §1 entries). PAO review at each iteration; CIC listen-test of Ch 14 at the end of the wave is the gate to Wave 2.

**Wave 1 success criterion:** Ch 14, Ch 17, Ch 18 at draft state that passes:
- (a) Voice gate — Anna's voice carries the grief without performing it; Joel's voice carries the admission without preaching it; the Anna's-choice beat in Ch 18 lands at procedural register
- (b) Pacing gate — Ch 14 at ≤12,500 words; Ch 17 at ≤6,500 words; Ch 18 at ≤8,500 words
- (c) Anti-pattern gate — no instance of thematic-justification for Diego's death; no instance of Joel-as-villain; no instance of melodrama in post-Ch-14 grief beats
- (d) CIC listen-test gate — at least Ch 14 passes a CIC audiobook listen-test (the executed prose's discipline of one-listen-test-chapter-per-major-revision)

**Wave 1 fallback:** If any chapter cannot pass the gates in three iterations, file `pao-question-*` to Admiral with the specific failure mode. The fallback is Plan H (architecture-is-wrong instead of Diego-dies) per the UPF. The fallback is real; the kill-trigger is real.

## Wave 2 — Foreshadowing additions (Week 2-3)

**Chapters: Ch 01, Ch 03 (verification only), Ch 07, Ch 10, Ch 11, Ch 12.** These chapters add the seeds that make Wave 1's load-bearing payoffs land.

**Sequencing within the wave:**
- **Ch 12 first.** The Diego micro-scene at the Segment-3-dive close is the most explicit Diego-foreshadowing addition; it should be authored first because it is the highest-risk addition (over-loading the chapter with Diego-death foreshadowing).
- **Ch 01 second.** The Joel-firmware-second-sentence addition is the lowest-risk addition; authoring it second after Ch 12 calibrates it against the Wave 1 chapters' altitude.
- **Ch 07 third.** The Joel-resource-discipline addition is calibrated against Joel's Ch 17 admission; it cannot be authored before Wave 1 closes Ch 17.
- **Ch 10 fourth.** The Anna-threat-of-loss interior addition is calibrated against the Diego death in Ch 14; it cannot be authored before Wave 1 closes Ch 14.
- **Ch 11 fifth.** The Wanjiru-firmware-pattern-noted addition is calibrated against the Ch 17 forensic-analysis content; it cannot be authored before Wave 1 closes Ch 17.
- **Ch 03 verification only.** No additions needed; verify the existing Diego material reads at Plan C altitude after Wave 1.

**Iteration discipline within the wave:** Two iterations max per chapter at this wave. The additions are short; the iterations should converge quickly.

**Wave 2 success criterion:**
- (a) Plant-payoff gate — every Wave 1 payoff has a corresponding Wave 2 seed at the right altitude; no payoff is unprepared
- (b) Voice gate — every addition reads as character depth on first pass and as foreshadowing on re-read
- (c) Pacing gate — no chapter grows by more than 5% of its current word count

**Wave 2 fallback:** If any chapter's addition cannot land in two iterations, omit the addition. Wave 1 chapters are sufficient as standalone payoffs; Wave 2 additions strengthen them but are not load-bearing.

## Wave 3 — Reframing edits (Week 3-4)

**Chapters: Ch 15, Ch 16, Ch 18 (already in Wave 1; ripples only).** These chapters reframe existing material under Plan C's post-Diego-death shadow.

**Sequencing within the wave:**
- **Ch 15 first.** The Wanjiru-three-threat-models-becomes-four addition is the wave's highest-risk reframing.
- **Ch 16 second.** The capability-degradation references + the queries-list expansion are calibrated against Ch 15.
- **Ch 18 ripples.** Any Ch 18 references to Diego that surface between Wave 1's structural rewrite and Wave 3 are handled here.

**Iteration discipline within the wave:** Two iterations max per chapter.

**Wave 3 success criterion:**
- (a) Reframing gate — every reference to Diego in Ch 15-18 has been audited and reweighted at the Plan C altitude
- (b) Empty-chair gate — the polar-operations-console references after Ch 14 read as the chair-is-empty without over-narrating the empty chair
- (c) Voice gate — Wanjiru's three-becomes-four recognition stays at her interior altitude; does not become the chapter's thesis

**Wave 3 fallback:** Same as Wave 2 — if a chapter's reframing cannot land in two iterations, omit the most fragile additions. The reframing is supportive, not load-bearing.

## Wave 4 — Consequence ripples (Week 4)

**Chapters: Ch 18 (Astrid scene); canon.yaml; staff-history-vs-diary register reframe across the volume.** These are the consequence-ripples that close out the rewrite.

**Sequencing within the wave:**
- **canon.yaml first.** Update the characters block (Diego → status: deceased, cause: cascade-event-Mission-Day-47; Joel → architectural-funding-decision admission Day-54), the events block (add ch14-diego-fatality, ch17-joel-firmware-admission, ch18-bereavement-protocol), the forward_plants block (Wanjiru-standards-body-framework-with-vendor-attestation-debt; Joel-discipline-trajectory-now-includes-fallibility-admission).
- **Astrid scene at Ch 18** — the Astrid-was-Anna's-apprentice scene at the dock is in the executed prose; Plan C may add one sentence in Anna's interior on what Astrid did not know about Diego (Astrid does not know Diego is dead; she will read it in the consortium archive after the institutional notification cycle closes). One sentence; at low altitude; per the new SPINE's restraint discipline.
- **Staff-history-vs-diary register reframe** — the staff history that goes to the consortium archive carries Joel's admission; the diary that does not replicate carries Anna's reception of the admission and Anna's grief at Diego. The register split is consistent with the executed prose's existing convention but gains weight under Plan C. Verification pass only; not a substantive rewrite.

**Wave 4 success criterion:**
- (a) canon.yaml accurately reflects the Plan C plot anchors
- (b) Astrid scene reads as the institutional silence the executed prose has earned, with the additional Plan C weight at one-sentence depth
- (c) Staff-history-vs-diary register split is consistent across the rewritten chapters

**Wave 4 fallback:** None needed; this wave is verification-and-cleanup.

---

# Section 3 — Cross-chapter integration concerns

## 3.1 The retrospective frame question for Ch 01

**The question:** Anna is writing the staff history retrospectively. She knows when Ch 01 opens that Diego is dead. Should Ch 01 acknowledge this knowledge, or hold it for the Ch 14 reveal?

**The recommendation: HOLD IT.**

The reasoning:

1. **The executed Ch 01 has been calibrated to do specific work.** It installs the narrator's voice, the niece, the mother-wound, the firmware-second-note seed, the bakery register, Joel without dramatization. Adding *"this is the chapter I am writing because Diego did not come back"* — even at the lightest altitude — over-loads the chapter in a way the executed prose was carefully built not to be over-loaded.

2. **The retrospective frame's discipline is precisely that the narrator knows what is coming and does not telegraph it.** Anna's existing voice in Ch 01 carries the back-of-the-mind tone of a person writing in retrospect: *"I am not going to pretend I caught something I did not catch"* is the canonical example. The voice is calibrated to the discipline of *I know and I am not telling you yet*. Breaking that discipline at Ch 01 would un-earn the discipline for the rest of the volume.

3. **The reader's experience is structurally better when Diego's death is a discovery, not an anticipation.** The Ch 03 Diego development is the volume's deepest single-chapter Diego work. The reader who registers Diego at the wing on Day 2 will register his absence at the rail on Day 47. The reader who has been told in Ch 01 that one of the crew will die will read Ch 03's Diego material as foreshadowing rather than as character development; the chapter loses what it had earned.

4. **The Plan C addendum to Ch 01 (the Joel-firmware-second-sentence addition) is sufficient at the right altitude.** It seeds the Joel admission for Ch 17 without telegraphing the death. The reader who re-reads Ch 01 after Ch 17 will register the gravity that was already in the voice. The first-time reader will not.

**The one-sentence permitted extension** in Anna's "nobody is going to die" briefing close (*"I helped where I could help. I did not always know which moments would be the ones I could not."*) carries the retrospective frame's gravity at a low altitude that may or may not survive the PAO read-aloud test. If it survives, it lands; if not, omit.

**The drafter's check:** read Ch 01 aloud after Plan C edits applied; if the chapter now reads as a chapter that telegraphs Diego's death, revise back toward the executed prose's restraint. The Ch 01 chapter holds at the institutional level the executed prose has earned; the Plan C additions strengthen specific seeds without breaking the chapter's structure.

## 3.2 Plant-payoff chain audit

The Plan C revisions introduce three new plant chains and modify two existing ones. The audit:

### New plant chain 1 — Joel firmware admission

- **Set in Ch 01:** Joel's procurement decision mentioned, with the phrase *the call I am still not sure about* (per Ch 01 Edit 1)
- **Reinforced in Ch 07:** Joel's resource-discipline-as-Navy-discipline beat (per Ch 07 Edit 1)
- **Reinforced in Ch 11:** Wanjiru notices the firmware-update-window pattern without yet pursuing (per Ch 11 Edit 1)
- **Paid in Ch 17:** Joel's wardroom admission *I could have funded the fork at the pre-procurement budget cycle and chose not to* (per Ch 17 item 2)

### New plant chain 2 — Diego death foreshadowing

- **Reinforced (existing) in Ch 03:** Diego at the wing on Day 2 — *the kind who has the answer on his chart at fourteen-twenty on Day 2 and brings it to the wing at the watch on which the answer is operationally actionable, and not at the meeting where the answer would have been politically useful.* The executed prose's Otago 2022 transducer anecdote stands.
- **Reinforced (existing) in Ch 08:** Diego pulls Sabina into the dry-run preparation. Stands.
- **Reinforced (new) in Ch 12:** Diego micro-scene with the mate-cup at the polar-operations console close (per Ch 12 Edit 1)
- **Paid in Ch 14:** Diego at the failure point; death at 0408 (per Ch 14 items 1-12)

### New plant chain 3 — Anna's threat-of-loss interior

- **Set in Ch 10:** Anna's interior naming what she would owe to each member of the current crew (per Ch 10 Edit 1)
- **Reinforced in Ch 12:** Diego micro-scene (per Ch 12 Edit 1; cross-references the Ch 10 list without naming Diego specifically)
- **Paid in Ch 14:** Diego's death + Anna's diary inset (per Ch 14 items 9, 10)
- **Reinforced in Ch 18:** Anna's interior in the hotel-room diary inset (per Ch 18 item 8)

### Modified plant chain 1 — wanjiru-firmware-supply-chain-question

- **Originally set in Ch 14 (executed prose):** *Wanjiru was also working a thread the bridge would not have asked her to work and that she had begun to work without being asked.* Plan C strengthens this by adding the earlier-Ch-11 seed (per Ch 11 Edit 1).
- **Paid in Ch 17 (executed prose):** the wardroom forensic-analysis at 1900 on Day 54. Plan C extends the payoff with Joel's admission (per Ch 17 item 2).

### Modified plant chain 2 — diego-letter-maria-elena

- **Originally set in Ch 14 (executed prose):** Diego writes the letter at night on Day 48; sets up the Day-55 sealing scene in Ch 17.
- **Modified set under Plan C:** Diego writes the letter at the wardroom table on Day 44 (the day before the cascade); the letter is dated under his hand; it is the artifact Maria recovers from his cabin desk after the death (per Ch 14 Edit 11).
- **Paid in Ch 17:** the letter is in the priority queue Wanjiru sets for the Punta Arenas surface handshake; Anna drafts the consortium-handshake-side notification letter alongside (per Ch 17 item 5).
- **Paid in Ch 18:** Maria gives Anna the sealed envelope and the leather mate-cup at the dock at 0728; the architecture preserves both; the architecture did not preserve Diego (per Ch 18 item 6).

The audit's verification step at Wave 4: cross-reference every chapter's YAML `plants-set` and `plants-paid` blocks against the audit. Any plant set without a payoff, or any payoff without a set, must be either added (set/payoff added in the appropriate chapter) or removed (the plant-payoff pair retired from the volume).

## 3.3 canon.yaml changes required

The `_series/canon.yaml` file requires the following updates at Wave 4:

### characters block

- **diego.role:** "crew member, currently standing the watch Anna is not standing" → "crew member; Senior Polar-Operations Specialist; deceased Mission Day 47 cascade event"
- **diego.cause_of_death:** new field; "asphyxiation and thermal injury in post-leak compartment environment, Mission Day 47, RV Nansen, MERIDIAN-7"
- **diego.spouse:** new field; "María Elena Vargas, Belgrano, Buenos Aires, Argentina" (per executed Ch 14 line 437)
- **diego.granddaughter:** new field; "Sofía" (per executed Ch 17 line 213; Diego's letter to María Elena)
- **diego.retirement_destination:** "San Martín de los Andes" — retained but reframed as posthumous destination for Diego's letter, photographs, paper draft
- **diego.notebook_entry_day_44:** new field; describes the cabin-desk notebook entry with Diego's retirement decision (per Ch 14 Edit 11)

### events block

- **Add:** `ch14_cascade_diego_fatality` at date 2026-XX-XX (Mission Day 47), time 0317-0408, location compartment two-bravo lower deck aft
- **Add:** `ch17_joel_firmware_admission` at date 2026-XX-XX (Mission Day 54), time 1900, location wardroom
- **Add:** `ch18_bereavement_handshake` at date 2026-XX-XX (Mission Day 56), time 0507, location Punta Arenas dock

### forward_plants block

The `diana-postcards` plant is unchanged (still un-paid in vol-2).

The `hiroshi-unfinished-line` plant is unchanged (still set in Ch 18 for Vol-3 payoff).

The `astrid-redemption-signal` plant is unchanged.

**Add new plant:** `joel-architectural-fallibility-admission`
- set_in: vol-2/ch17 (wardroom Day 54)
- description: Joel's admission that he could have funded the vendor-firmware fork at the pre-procurement budget cycle and chose not to; the cost is at the compartment
- payoff_target: vol-2-the-series-book-2 (Wanjiru's standards-body framework opening with vendor-attestation requirements as the institutional response to Joel's funding decision); vol-3 (Wanjiru-narrator) and vol-4 (Astrid arc) inherit the admission as the architecture's foundational debt

**Add new plant:** `diego-mate-cup-and-letter-as-institutional-artifact`
- set_in: vol-2/ch18 (dock at 0728 — Maria gives Anna the envelope and the cup)
- description: the architecture preserved Diego's photographs, his unfinished paper, his last letter, and his leather mate-cup with the unpolished bombilla; the architecture did not preserve Diego; the institutional handshake carries the artifacts to María Elena at Belgrano
- payoff_target: vol-2 close (the artifacts are the closing image of the volume's architecture-vs-the-man recognition); no further payoff needed (atomic-within-volume)

---

# Section 4 — Risk register and halt conditions

The Plan C1+C7 execution has five identified risk categories. The halt conditions for each are specified.

## Risk 1 — Anna's voice cannot carry sustained grief

**Probability:** Medium. Anna's voice is calibrated for restraint; the Ch 14 death + Ch 15-18 grief absorption is the highest interior-altitude pressure the voice has ever been tested under.

**Mitigation:** The new SPINE addendum A and anti-pattern 8 are the voice gates. Each chapter's PAO direction includes the restraint discipline reminder.

**Halt condition:** If Ch 14's draft state after three iterations breaks Anna's voice register (tonal whiplash; sustained grief at length; melodrama), file `pao-question-*` to Admiral. The fallback is Plan H (architecture-is-wrong) per the UPF Section 5.2 decision tree.

## Risk 2 — Joel's admission lands as authorial preaching

**Probability:** Medium-low. Joel's voice has been calibrated for honest engineering register; the admission is in the same register at higher stake.

**Mitigation:** The new SPINE addendum B and anti-pattern 7 are the voice gates. The Ch 17 PAO direction (per §1 Ch 17 Edit 2) provides drafter-target text.

**Halt condition:** If Ch 17's admission after three iterations reads as Joel-as-villain or as authorial preaching, consider whether the admission needs to be at lower altitude (one sentence rather than one paragraph) or whether the Plan C lock needs CIC reconsideration.

## Risk 3 — Plant-payoff chains break in execution

**Probability:** Medium. Multiple plant-payoff chains modified or added; complex authoring across multiple chapters and multiple waves.

**Mitigation:** The §3.2 audit; the Wave 4 verification pass.

**Halt condition:** If Wave 4 verification finds any plant set without a payoff or any payoff without a set, revise the appropriate chapter. If revision in two iterations cannot close the gap, file `pao-question-*` to Admiral.

## Risk 4 — Word count balloons past target

**Probability:** Medium. Ch 14 + Ch 17 + Ch 18 are all expanding under Plan C; the total volume target is ~115-119k words, but the executed prose is already 109k, and the executed Ch 14 + Ch 17 + Ch 18 are already 23.9k of that.

**Mitigation:** Each chapter's PAO direction includes word-count target. The Wave 1 success criterion includes pacing gates (Ch 14 ≤12,500; Ch 17 ≤6,500; Ch 18 ≤8,500).

**Halt condition:** If any single chapter exceeds 110% of its target after three iterations, file `pao-question-*` to Admiral and consider whether to split the chapter (e.g., Ch 14 into the cascade + the eleven-minutes-and-aftermath as two chapters, bringing the total to 19 chapters).

## Risk 5 — CIC listen-test of Ch 14 does not pass

**Probability:** Low-medium. The Ch 14 cascade with Diego death is a high-altitude scene; CIC's listen-test discipline catches voice-and-pacing failures the read-aloud-only pass may miss.

**Mitigation:** Wave 1 success criterion includes CIC listen-test gate.

**Halt condition:** If Ch 14 listen-test fails, the gate to Wave 2 does not open. Revise Ch 14 first (and Ch 17, Ch 18 if calibration dependencies require). The fallback (if Ch 14 cannot pass after three full rewrite iterations) is Plan H per the UPF.

---

# Section 5 — Execution sequencing recommendation

The recommended execution sequence:

**Week 1 (Wave 1, partial):**
- Day 1-3: Ch 14 first-draft rewrite (PAO direction + Yeoman drafting; PAO review at first iteration)
- Day 4-5: Ch 14 second-draft revision (PAO direction + Yeoman drafting; PAO review at second iteration)
- Day 6-7: Ch 14 third-draft revision + read-aloud (PAO+CIC listen-test)

**Week 2 (Wave 1, completion):**
- Day 8-10: Ch 17 first-draft + second-draft (PAO direction; Yeoman drafting; PAO review at each iteration)
- Day 11-12: Ch 17 third-draft revision + read-aloud
- Day 13-14: Ch 18 first-draft (PAO direction + Yeoman drafting)

**Week 3 (Wave 1 closing + Wave 2):**
- Day 15-17: Ch 18 second-draft + third-draft + read-aloud
- Day 18-19: Wave 2 batch — Ch 12, Ch 01 (parallel, since they are independent)
- Day 20-21: Wave 2 batch — Ch 07, Ch 10, Ch 11 (parallel, since they depend only on Wave 1 closure)

**Week 4 (Wave 3 + Wave 4):**
- Day 22-24: Wave 3 — Ch 15, Ch 16 (sequential; Ch 16 depends on Ch 15)
- Day 25-26: Wave 4 — canon.yaml updates; Astrid-scene one-sentence addition; staff-history-vs-diary register reframe verification
- Day 27-28: Full-volume read-aloud pass; final voice consistency check; final plant-payoff audit

**Total: 28 days (4 weeks) at sustainable PAO+Yeoman cadence.** The UPF estimate of 3-4 weeks aligns; the 4-week target carries one week of buffer for the Risk 1 and Risk 5 halt-conditions (which would require Ch 14 re-iteration beyond the three-iteration default).

**The drafting itself uses PAO direction + Yeoman drafting under the PAO ↔ Yeoman cost-driven division of labor.** PAO authors the per-chapter direction (~2-4 PAO hours per Wave 1 chapter; ~30-90 PAO minutes per Wave 2-3 chapter). Yeoman drafts under Sonnet 4.6 at the executed-prose cadence. PAO reviews each iteration at PAO read-aloud. CIC listens to Ch 14 at the end of Week 1 (the listen-test gate).

**If a parallel-fan-out is preferred for Wave 2 and Wave 3,** the recommended fan-out is one Yeoman subagent per chapter per the PAO prose fan-out memory pattern (`feedback_pao_prose_fan_out.md`). Wave 2 fans out to 5 parallel subagents (Ch 01, Ch 07, Ch 10, Ch 11, Ch 12). Wave 3 fans out to 2 parallel subagents (Ch 15, Ch 16). Wave 4 does not fan out (single-thread cleanup work).

---

# Section 6 — Document close

This integration plan is the operational companion to the new working SPINE under Plan C1+C7. The two documents together describe the next 3-4 weeks of vol-2 rewrite work.

**Next steps:**

1. **CIC review of both documents.** If the SPINE draft is ratified and the integration plan is accepted, the working draft replaces `vol-2/SPINE.md` and the integration plan becomes the authoring document.

2. **Wave 1 dispatch.** PAO authors Ch 14 direction; Yeoman drafts. PAO reviews; iterates. CIC listen-tests Ch 14 at end of Week 1.

3. **Continuous status reporting to CIC via PAO state-snapshots.** A new state snapshot at the end of each wave (Wave 1 close ≈ Day 14; Wave 2 close ≈ Day 21; Wave 3 close ≈ Day 24; Wave 4 close ≈ Day 28).

4. **Halt-condition discipline.** Per Section 4, any Wave 1 halt-condition triggers a `pao-question-*` to Admiral and a re-routing to Plan H consideration. The kill-trigger is real.

The volume the rewrite is moving toward is the volume the back-cover Candidate 3 in the SPINE draft promises: a Bobiverse-cadence techno-thriller in which the architecture works exactly as specified and the cost is still real, told by the mission commander who selected the crew that did not all come back, written for the next mission director who will need what she will need.

*— PAO orchestrator, 2026-05-21. Integration plan for Plan C variant 1+7 execution.*
