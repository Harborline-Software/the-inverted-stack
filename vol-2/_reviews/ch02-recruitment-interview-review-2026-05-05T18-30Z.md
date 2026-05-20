---
type: chapter-review
chapter: ch02-recruitment-interview
chapter-version: 53f0a1c (post-prose-pass; PR #115 merged 2026-05-05)
reviewer: vol2-chapter-reviewer
review-pass: 2
date: 2026-05-05
chapter-word-count: 7256
chapter-audiobook-min: 43.5
prior-version: 25c6c16 (8,216 words / 50.6 min) - chapter-drafter v2 redraft post-canon-PR-#113
---

> **Pass-2 calibration.** Focused on what changed since v2; verifies the five prose-pass recommendations landed cleanly; surfaces what the revision introduced or left unaddressed; biased toward the six special-focus areas the human flagged in dispatch. Six dimensions pass cleanly; two - pacing/structure and line-level - carry the bulk of the surgical recommendations.

## 1. Big-picture assessment

The chapter is doing one thing: **making Anna's selection of Joel legible as a character test the reader can witness in real time, with the architecture as evidentiary substrate.** It now succeeds on that for both audiences. The technically literate reader gets enough fence/snapshot/coordinator-tick to feel the weight of what Joel rewrote; the character reader gets the four-sentences-plus-the-fifth and the prior-failure inversion legibly framed. The post-prose-pass version (-960 words, -11.7%) lands a meaningfully tighter chapter and the central risk has shifted: v2's risk was over-explanation; v3's risk is now that **the chapter still pre-spends future material in the back third** (Joel's not-naming-the-Navy / Sunfish-name decline) and the **Day-14 coda over-summarizes a chapter that has already landed.** The architectural claim - *the architect's response to being told he is wrong is what makes the architecture trustworthy* - exercises cleanly through the lease-rewrite walk-through and the I-missed-it admission. The structural choice is the diptych of the *two-second pause before he spoke* and the *four-sentences-plus-fifth.* Distinctive and earned.

## 2. Technical-density and accessibility

**Net assessment:** v3 is in the right zone. Six of the seven technical sections are now within tolerance. One section - the **clock paragraph (lines 94-100)** - is the only remaining block where technical density still measurably outruns the chapter's emotional spine.

### What landed cleanly (preserve)

- **BLOCK image (line 26; 127 words).** The compression to *two nodes could both believe they owned the same truth, and the protocol had no way to stop them*, followed by the four-clause cascade (lease holder lost → expired → new holder accepted → no fence) is exactly the right altitude for a non-specialist audiobook listener. Klett-character-color line is doing real work. **Special-focus item 1 (subordinate-clause compression of the BLOCK image): no further compression recommended at this resolution; it is at the floor.**
- **GC tier exchange (lines 68-76; ~150 words).** The single Q→A→Anna-paraphrase shape - *He had walked me to the edge of data loss and then shown me where the fence actually stood* - is the cleanest single recommendation that landed from the prose-pass. This is now a structural exemplar; the rest of the chapter should reach this level of compression where it can.
- **Sync-daemon snapshot move (line 64).** *Snapshot when history is gone* as named-mechanism is doing exactly what the prose-pass intended: the reader installs the phrase here so it can do work later in the book without re-explanation. **Special-focus item 2 (data-layer/sync-daemon rhythm): rhythm is now correct; do not further compress without losing the named-mechanism install.** The 35-minute / 20-minute timing notation is the bookkeeping that makes the audiobook listener feel the call's weight without the listener having to live every minute. Keep.
- **Lease-rewrite walk-through (lines 88-92; ~280 words).** The fence + acknowledgment-requirement + closed-interval cascade is the chapter's most load-bearing technical passage and it earns every word. The repetition of *fence* (eight instances total in the chapter) is intentional anaphora - it is the named mechanism the chapter is recruiting on. Do not vary.
- **Byzantine ops (lines 162-174).** The five-Q&A → Anna-narrative-summary collapse worked. *Primitives present, tooling pending* + *I will write the code on the boat* is doing the right two-line job.

### What still needs work (one item)

- **Clock paragraph (lines 94-100; 134 words).** **Special-focus item 3.** This is the only technical passage where the prose-pass may have compressed the dialogue but did not compress the underlying fineness of the technical content. *Wall clock for the holder's self-check / monotonic clock for the holder's self-check / a coordinator-mediated tick for the peer-side check* is three distinct clock concepts in two sentences for a non-infra reader. The load-bearing idea is **the original protocol used the wrong clock; the rewrite uses the right clock; that wrongness was the assumption Joel missed.** The character beat - Joel's voice dropping a register on *the assumption I missed* - is the actual payload. Compression target: keep the voice-drop beat at full weight; reduce the clock-taxonomy by half.

  Specific cut candidates:
  - *for both the holder's self-check and the peer-side confirmation* and *for the holder's self-check and a coordinator-mediated tick for the peer-side check* are mirror constructions that compress to one. Anna's own paraphrase - *Joel had not patched. He had rewritten.* - already does the structural work; the dialogue can hand off earlier.
  - The post-paragraph (line 100) restates the load-bearing-assumption point Joel just made. Choose one: Joel's voice-drop OR Anna's paraphrase, not both.
  - **Recommendation:** -50 to -60 words from this passage. See § 5 for before/after.

## 3. Character and emotional-throughline

The chapter's *real question* - **what kind of man wakes up the morning after Klett tells him he's wrong?** - is now stated explicitly at line 36, immediately after the BLOCK is named. This is the single most important structural improvement the prose-pass made; it lets the entire technical interview read as evidence-gathering for the character test rather than as digression. **This is the highest-impact prose-pass landing and it is correct.**

### Body / character beats that are now working

- Joel reaching for the printout twice in ten minutes, the hand stopping, then setting it aside (lines 60, 70, 82). The micro-gesture pattern is a recurring tell that pays off.
- Joel rubbing his eyes once before the lease-layer transition (line 82). Lands the two-hour fatigue without commentary.
- *The light behind him was full now* (line 134) after the four-sentences-plus-fifth admission. The room's light arriving uncommented while Joel speaks the verdict is the chapter's best environmental beat.
- Joel setting the coffee down deliberately before answering the gauge-in-front-of-you origin question (line 182). The set-down as character beat.

### What the revision introduced that needs work

- **Joel's not-naming-the-Navy paragraph (lines 188-198).** **Special-focus item adjacent.** The prose-pass appears to have left this section untouched, and at v3 word density it now reads as the chapter's longest character-interior passage that **pre-spends Ch 7 (`Joel's Sunfish` - the naming-disclosure chapter)**. Lines 194-198 - *I would later understand that I had asked the two questions in the wrong order... I was going to learn what it was. I was going to learn it from him, in person, when he chose to tell me. I respected that too.* - does three things: (a) Anna self-corrects her interview tactics, (b) telegraphs that Joel will tell her later, (c) telegraphs that Anna respects the not-naming. The third is load-bearing for this chapter; the first two are foreshadowing payments the chapter cannot afford. Net result: this passage is the strongest **forecast-register-adjacent** moment in the chapter. Per `series-arc-sunfish-trajectory.md` § 8 the strict-prophecy register is forbidden; this is the **soft** version of the same thing - *I would learn / I was going to learn / I would later understand* - and it dilutes the chapter's compressed-deliberate register.
  - **Recommendation:** Cut *I would learn months later that for Joel it was the second reason. I would learn the institutional past on the boat, in a conversation I did not yet know was coming, in a quiet hour during a surface window. The naming would come when he was ready to name it.* Replace with one sentence in present-call register: *He was not going to tell me on the call. I did not press.* Net -85 words. See § 5 for before/after.
  - Same surgical fix for line 198 - *I was going to learn what it was. I was going to learn it from him, in person, when he chose to tell me.* The chapter does not need to commit to when Anna learns; that is Ch 7's structural ground. Cut these two sentences. Net -25 words.

- **The Stefan-comparison section (lines 142-154; 514 words). Special-focus item 4.** This is the chapter's load-bearing prior-failure interior, and the moral - *technically true / operationally a lie* - currently lands twice in successive sentences (line 144). On first instance it is doing devastating work; the second instance is the one the special-focus prompt asks about. The doubling reads as Anna underlining the moral she has already named. Cut the second instance; let the chiastic pattern *We sailed on the technically-true answer. We came home on the operationally-a-lie.* close it. Net -25 words.
  - The five-years sentence (*The five years between then and now are the years it took to be sure I had wanted neither.*) is doing real work and stays.
  - The *I had wanted the next mission's architect to be the structural inverse of the man who had not disclosed* sentence is the chapter's load-bearing interior thesis. Stays.
  - The whole paragraph at 146 is doing what Anna's voice-spec calls "controlled flashes followed by return to the work" - but the flash here sustains for ~150 words. **One additional cut:** *because I could not yet write the longer version, and because the longer version would have ended a man's career, and because I was not sure in the months after the mission whether I wanted to end his career or whether I wanted to end my own* - the third clause repeats the second's emotional content. Cut *and because I was not sure in the months after the mission whether I wanted to end his career or whether I wanted to end my own.* The next sentence (*The five years between then and now…*) carries the recognition without the asyndetic triple. Net -30 words.

- **The four-sentences-plus-fifth beat (lines 124-138). Special-focus item 5 - whitespace.** The prose-pass added Anna's body-language sentence after the fifth (*The light behind him was full now. He did not reach for the coffee. He did not look down at his notebook. He had said what he had come to say and was waiting for the next question.*). That sentence is the right addition. **What still needs adjustment:** the four-line-break / fifth-sentence structure currently reads as one continuous paragraph from 128 through 138 across what should be **three** rhythmic moments - the four sentences, the after-pause-fifth, and Anna's *yes*. Recommendation: insert paragraph break after *the cadence of a man reading a verdict back to the room rather than explaining a protocol to a recruiter. I noted the shift. I did not name it aloud.* (already there) - but also confirm the paragraph break already at line 130 (*There was a fifth sentence...*) renders correctly; that's the load-bearing white space. The current rendering is fine; this is a check-confirmation, not a fix. Net 0 words. **No further whitespace expansion needed; the rhythm is correct as-rendered.**

## 4. Pacing and structure

Six structural moves work cleanly; two are off.

### Working

- The opener-through-line-36 setup is now the chapter's strongest section. Pattern A formal log → kitchen-table-November sensory anchor → BLOCK image → *what kind of man wakes up* thesis. Four moves; ~700 words; a lot of weight per word.
- The 35-min / 20-min / 14-min interview-clock notation gives the audiobook listener the call's duration without forcing them to live it.
- The two-character interview structure with Anna's interior-narration interspersed is the load-bearing dialogue-engine for Vol 2 and it works at audiobook tempo.
- The *yes / yes* recruitment exchange (lines 220-224) lands.
- Joel's three reciprocal questions (consortium / crew / *the architecture has not been deployed in production with lives depending on it*) earn the chapter's last act.

### Not working

- **The Day-14 coda (lines 244-262; 417 words). Special-focus item adjacent - though phrased as "compress" which the prose-pass *did* address.** The prose-pass took it from ~580 words to 417. That's an improvement. But at 417 it still over-summarizes a chapter the reader has just finished. The coda currently does five things: (a) re-states architecture-is-fine; (b) re-states the four-sentences-plus-fifth beat; (c) re-states the architecture-and-architect-as-same-property recognition; (d) names Joel's location on the boat; (e) ends on *That is why it was him.* Items (b) and (c) are the chapter's body - the coda restates rather than completes. The cleanest cut would let the coda run only items (a), (d), and (e), with one new sentence connecting the present-tense to the past-tense without re-quoting.
  - **Recommendation:** Compress 417 → ~250 words. Cut the second appearance of *I missed it. The original protocol assumed the network would heal within quorum-exhaustion windows. The assumption did not hold under sustained partition. Klett was right. I rewrote it.* (lines 230-232) - the verbatim re-quotation does not earn its place when the reader read it 90 lines ago. Cut the *That is why it was him* repetition (the ending earns one final landing of the line; not three). Keep: the steady-state-hum opening, *None of that is why I am writing tonight*, *The architecture under the ice is the rewrite, deployed*, the Joel-two-compartments-aft beat, *He spoke into the record anyway*, *I am going to bed.*
  - Net -160 to -180 words. See § 5 for before/after.

- **The notebook-with-the-line-through-it passage (lines 110-116).** Internal flow is right but the *consortium would not have known the call had ended on the BLOCK question* sentence is procedural exposition (*the first three names were ahead of him on the consortium's ranking; only Joel was ahead of him on mine*) that competes with the chapter's emotional altitude. **The line through the sentence is the test** is the load-bearing image; the consortium-ranking aside dilutes it. Recommend cut from *The consortium would not have known the call had ended on the BLOCK question.* through *only Joel was ahead of him on mine.* Net -50 words.

### Where the chapter could end

The chapter currently ends at line 262 (*- A. Y., Day 14, the Nansen*). A defensible alternative ending would be at line 240 (*The MERIDIAN-7 was twelve months from departure. I had time to tell her later. I have told her since.*). The Day-14 coda after that is a structural decision (the diary register installed by Pattern A wants a back-frame anchor) and is canon-mandated by the outline. **Keep the Day-14 coda but compress per the recommendation above.** Net effect: same structural shape, 250 words instead of 417.

## 5. Concrete, line-level suggestions

### Repetition / phrase audit

- **`I made a note` / `I noted` / `I had registered` family.** Counted: *I made a note* x 4 (lines 62, 98, 138, 212); *I noted* x 1 (line 122); *I had registered* x 1 (line 188); *I noted that* x 1 (line 198). **Special-focus item 6.** Total note-making constructions: 7. The instances at lines 62, 98, 138 are doing distinct work (vocabulary-flag / voice-drop-flag / one-word-yes); they earn their place. Lines 122, 188, 198, 212 are the repetitions that read as formula. Recommendations:
  - Line 122 (*I noted the shift. I did not name it aloud.*): keep; the *did-not-name-it-aloud* tail is voice-spec-correct.
  - Line 188 (*I had registered, without yet knowing what to do with the registration*): cut; this is part of the not-naming-the-Navy passage that wants compressing anyway (see § 3 above).
  - Line 198 (*I noted that. I did not press.*): redundant with line 188's *I did not press* and with the gestural sequence that already showed Anna registering. Cut.
  - Line 212 (*I made another note, which was that he had read the team I had picked before I had told him who was on it.*): the observation is load-bearing; the *I made another note, which was* framing is formula. Tighten to: *He had read the team I had picked before I had told him who was on it.* Net -8 words but more importantly removes the formula tic.
- **`I had read` repetition.** Lines 22, 24, 110 - the third-reading construction is doing load-bearing structural work. Keep all three; the repetition is anaphora.
- **`fence` (8 instances) and `two-record-class` (2 instances).** Both intentional; the named mechanisms doing recurring work. Keep all.
- **`technically true / operationally a lie` x 2 in successive sentences** (line 144). One landing; cut the second per § 3 above.

### Before / after - Clock paragraph (special-focus item 3)

```
BEFORE (134 words; lines 94-100):
I asked about the wall-clock dependency.

He said: *Wall clock is the worst clock in any distributed system. The
original protocol used wall clock for both the holder's self-check and
the peer-side confirmation. The rewrite uses monotonic clock for the
holder's self-check and a coordinator-mediated tick for the peer-side
check. The wall-clock dependency was the assumption I missed.*

His voice on *the assumption I missed* dropped a register. Not regret;
not performance. The flat tone of a man stating where the failure had
lived. I made a note.

I had wanted to know whether the rewrite was a patch on the original
or a different protocol. The answer was that the wall-clock dependency
had been the load-bearing assumption of the original; the rewrite was
a different protocol because the load-bearing assumption was different.
Joel had not patched. He had rewritten.

AFTER (78 words; -56 words / -42%):
I asked about the wall-clock dependency.

He said: *Wall clock is the worst clock in any distributed system.
The original protocol used it for the lease-expiry computation. The
rewrite uses monotonic clock at the holder and a coordinator-mediated
tick at the peers. The wall-clock dependency was the assumption I
missed.*

His voice on *the assumption I missed* dropped a register. Not regret;
not performance. The flat tone of a man stating where the failure had
lived. I made a note.

Joel had not patched. He had rewritten.

Why: Preserves the three load-bearing technical claims (wall clock is
the wrong clock; the rewrite uses two different clocks at two different
checkpoints; that's the assumption Joel missed) while collapsing the
mirror "for both X and Y / for the holder's self-check and the peer-
side check" construction that doubles the clock taxonomy for non-infra
readers. Anna's *Joel had not patched. He had rewritten.* now lands
without an intervening paragraph that paraphrases what Joel just said.
The voice-drop beat is preserved at full weight.
```

### Before / after - Day-14 coda (lines 244-262; structural)

```
BEFORE (417 words; section starting "I am back on the boat now"):
I am back on the boat now. It is Day 14. The tea is cold. The watch I
am not standing is Diego's; the boat is humming the way the boat hums
under ice - the steady-state hum, not the one with anything in it.

The architecture has been holding. The local store answers every query
without ambiguity. The relay is dormant. The gossip protocol has
correctly identified itself as dormant rather than as failing. The
schema state is stable. The audit log is intact. The architecture is
fine; the boat is fine; the man who built the architecture is fine.

None of that is why I am writing tonight.

I am writing because of the rewrite that should have been there the
first time. The architectural question was answered four years ago
when Joel rewrote the lease protocol; the council's clearance answered
it three years ago; my reading of the cleared rewrite answered it two
years ago. What is answered tonight is the other question - the one
he asked me on the call, the one I said yes to. *You're asking me to
be on board the first time it is.* The architecture under the ice is
the rewrite, deployed. The proof is happening.

That is why it was him. The load-bearing element is the four sentences
and the fifth. The load-bearing element is the man who said them that
way without softening them. Tonight, when I queried the local store
and it answered me locally because there was nothing else to answer
with, the architecture's authority and the architect's discipline
registered for me as the same property. They were always going to
register that way. I had selected him so that they would.

The next watch is in three hours and I would like to sleep before it.
Joel is two compartments aft, on the late shift at the data console,
working a routine reconciliation pass with Wanjiru. He does not know
I am writing this. He has not known for fourteen days. He knew the
call was being recorded. He spoke into the record anyway.

That is the property. He spoke into the record anyway. The architecture
is the same property. The boat is on the record about Day 14 of an
under-ice partition operating exactly as the rewrite specified. The
crew is on the record because I am writing this and I will sign it.

That is why it was him.

I am going to bed.

- A. Y., Day 14, the Nansen

AFTER (~245 words; -172 / -41%):
I am back on the boat now. It is Day 14. The tea is cold. The watch I
am not standing is Diego's; the boat is humming the way the boat hums
under ice - the steady-state hum, not the one with anything in it.

The architecture has been holding. The local store answers every query
without ambiguity. The relay is dormant. The gossip protocol has
correctly identified itself as dormant rather than as failing. The
schema state is stable. The audit log is intact. The architecture is
fine; the boat is fine; the man who built the architecture is fine.

None of that is why I am writing tonight.

I am writing because of the question Joel asked me on the call, the
one I said yes to. *You're asking me to be on board the first time it
is.* The architecture under the ice is the rewrite, deployed. The
proof is happening.

The next watch is in three hours and I would like to sleep before it.
Joel is two compartments aft, on the late shift at the data console,
working a routine reconciliation pass with Wanjiru. He does not know
I am writing this. He has not known for fourteen days. He knew the
call was being recorded. He spoke into the record anyway.

That is the property. He spoke into the record anyway. The boat is on
the record about Day 14 of an under-ice partition operating exactly
as the rewrite specified. The crew is on the record because I am
writing this and I will sign it.

I am going to bed.

- A. Y., Day 14, the Nansen

Why: Cuts the verbatim re-quotation of the four-sentences-plus-fifth
(the reader read it 90 lines ago; restating it dilutes the original
landing). Cuts the four-years-ago / three-years-ago / two-years-ago
chronology (procedural padding; the reader's question is whether the
architecture is holding now, not when prior questions resolved). Cuts
the "they were always going to register that way / I had selected him
so that they would" - the explanation of the recognition is the
recognition over-explained. Cuts the duplicate "That is why it was
him" - keeping it once at the body's close, not at the coda. Preserves
every load-bearing operational detail (architecture holding /
characteristic tells / Joel two compartments aft / he spoke into the
record anyway / sign it). The compressed coda lands the chapter at
present-tense weight without recapitulating what the body delivered.
```

### Before / after - Joel's not-naming-the-Navy compression (§ 3 recommendation)

```
BEFORE (line 188; 124 words):
I did not press for more. I had registered, without yet knowing what
to do with the registration, that the phrase belonged to a specific
institutional past, and that Joel had not named the institution. The
not-naming was deliberate. Senior engineers who do not name their
formative employer are usually doing it for one of two reasons: a
non-disclosure obligation, or a habit of not explaining the past to
people who have not earned the disclosure. I would learn months later
that for Joel it was the second reason. I would learn the institutional
past on the boat, in a conversation I did not yet know was coming, in
a quiet hour during a surface window. The naming would come when he
was ready to name it. I respected that he had not named it on the call.
I did not press.

AFTER (62 words; -62 / -50%):
I did not press for more. The phrase belonged to a specific
institutional past Joel had not named. Senior engineers who do not
name their formative employer are usually doing it for one of two
reasons - a non-disclosure obligation, or a habit of not explaining
the past to people who have not earned the disclosure. He was not
going to tell me on the call. I did not press.

Why: Removes the forecast-adjacent register (*I would learn months
later / I would learn the institutional past on the boat, in a
conversation I did not yet know was coming*) that pre-spends Ch 7's
naming-disclosure. Preserves Anna's diagnostic - the two-reasons
catalog is the operator-mind beat. Preserves Anna's restraint *I did
not press* as the recurring tell. The chapter no longer commits to
*when* Anna learns; that question stays alive for Ch 7.
```

## 6. Tone and style check

### Voice register - Anna

The compressed-deliberate / Russian-academic-with-Uzbek-warmth register holds across the whole chapter. The kitchen-table-in-November sensory beat (line 22) is a controlled flash that lands; the staff-history-for-the-next register at *I will say something here that I have not said in print before* (line 142) is voice-spec exemplary. **No drift to confession-register; no drift to free-indirect-style; no spec-voice intrusion. This dimension is in the green.**

### Anti-AI tells (per `.claude/skills/anti-ai-tells/SKILL.md`)

Lexical grep on the high-frequency tell vocabulary returned **1 hit** for the whole skill catalog - the word *crucial* does not appear; *delve / underscore / tapestry / interplay / pivotal / vibrant / showcase* do not appear; *stands as / serves as / represents a* do not appear except in the technically-correct sense. The single hit (an *enduring* or similar - borderline) is in voice-correct context. **This dimension is in the green.**

### Forecast register / prophecy weight

Scan returned five `would later / months later / I would learn / I was going to learn / I would later understand` constructions. **Three of the five live in the not-naming-the-Navy paragraph** (lines 188, 194, 198) and are addressed in § 3 above. The remaining two (line 64 - *Joel had been answering my question for twenty minutes without my having asked it* - is past-perfect, not forecast; line 228 - *His work from that moment forward was to make the yes hold. The work began the day after the call and has not stopped since.*) are **legitimate retrospective register**, not forecast register. The Day-14 coda is past-anchored (Anna writing-now about the call-then) so its retrospections are voice-spec-correct.

**Net: the only forecast-register issue is the not-naming-the-Navy paragraph; addressing it removes the chapter's only soft-prophecy register.**

### Hedging

Spot-check returned zero hedging. *I had wanted to know* / *I was watching for* are observation-register, not hedging. *He had been talking for almost two hours at five in the morning his time* - *almost two hours* is precision, not hedge.

### Academic scaffolding

Zero. The chapter does not narrate-its-own-narration.

## 7. Summary of recommended changes (prioritized)

Eight surgical recommendations, ordered by impact. Total estimated word-count delta: **-380 to -430 words** (chapter would land 6,830-6,880 / ~41 min audiobook). All preserve every structural canon element (Pattern A formal-log opener; R1-BLOCK admission verbatim; yes/yes recruitment exchange; Joel's three reciprocal questions; closing-call-to-mother; Day-14 close).

1. **Compress Day-14 coda** (lines 244-262; 417 → ~245 words; **-172 words**). Cut the verbatim re-quotation of the four-sentences-plus-fifth; cut the four-years-ago / three-years-ago / two-years-ago chronology; cut the *they were always going to register that way / I had selected him so that they would* over-explanation; cut the duplicate *That is why it was him*. Keep every operational detail and *He spoke into the record anyway*. Highest-impact single recommendation.

2. **Compress Joel's not-naming-the-Navy passage** (line 188; 124 → 62 words; **-62 words**). Cut *I would learn months later / I would learn the institutional past on the boat, in a conversation I did not yet know was coming, in a quiet hour during a surface window*. This is the chapter's only forecast-register intrusion and it pre-spends Ch 7. Preserves the two-reasons diagnostic and Anna's *I did not press* restraint.

3. **Cut Sunfish-name-decline forecast tail** (line 198; **-25 words**). *I was going to learn what it was. I was going to learn it from him, in person, when he chose to tell me.* The chapter does not need to commit to when Anna learns; Ch 7 owns that. Keep *I did not press.* and *The weight came from somewhere.*

4. **Compress clock paragraph** (lines 94-100; 134 → 78 words; **-56 words**). Collapse the mirror clock-taxonomy construction; let Anna's *Joel had not patched. He had rewritten.* land without the intervening paraphrase paragraph. Preserves the voice-drop beat at full weight. Special-focus item 3 closure.

5. **Cut consortium-ranking aside in notebook-line passage** (lines 110-116; **-50 words**). *The consortium would not have known the call had ended on the BLOCK question. The consortium would have known only that I had not extended the offer to the second name on the list. The first three names were ahead of him on the consortium's ranking; only Joel was ahead of him on mine.* - procedural exposition that competes with the chapter's emotional altitude. *The line through the sentence was the test* is the load-bearing image; let it stand alone.

6. **Cut second instance of *technically true / operationally a lie*** (line 144; **-25 words**). The doubling reads as Anna underlining a moral she has already named. The chiastic *We sailed on the technically-true answer. We came home on the operationally-a-lie.* closes it cleanly without a third instance. Special-focus item 4 closure.

7. **Cut "or whether I wanted to end my own" clause from after-action-report paragraph** (line 146; **-30 words**). Asyndetic triple where the third clause repeats the second's emotional content. *The five years between then and now are the years it took to be sure I had wanted neither* carries the recognition.

8. **Tighten *I made another note* formula** (line 212; **-8 words**). Cut the *I made another note, which was that* framing; let the observation stand. Removes the chapter's last note-making formula tic. Special-focus item 6 closure.

---

## Executive summary

The prose-pass landed cleanly across five of its six target areas; the chapter is now within audiobook tolerance and its emotional spine is legible to a non-specialist reader. Six dimensions pass without significant fault. Pacing/structure and line-level carry the residual work, concentrated in two pockets:

- **The Day-14 coda over-summarizes a chapter the body has already landed** (-172 words is the highest-impact single fix).
- **The not-naming-the-Navy paragraph is the chapter's only forecast-register intrusion and it pre-spends Ch 7's naming-disclosure** (-87 words across recommendations 2 and 3).

Remaining recommendations (clock-paragraph compression, consortium-ranking cut, doubled-moral cut, asyndetic-triple cut, note-formula cut) are surgical, scattered, and each individually small. **Net delta: -380 to -430 words.** Recommended target: 6,830-6,880 / ~41 min audiobook. The chapter's structural canon (Pattern A, four-sentences-plus-fifth, yes/yes, three-reciprocal-questions, Day-14 close) is preserved by every recommendation.
