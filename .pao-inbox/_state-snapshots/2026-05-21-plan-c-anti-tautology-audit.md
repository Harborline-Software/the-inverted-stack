---
type: audit
volume: vol-2
title: Plan C rewrite-target chapters — anti-tautology / hollow-meaningful / noun-parade audit
author: PAO subagent (focused literary anti-pattern hunt)
date: 2026-05-21
calibration-rubric: vol-2/SPINE-draft-plan-c.md § "Committed back cover (Candidate 4)" + § "What changed vs Candidate 3"
companion-documents:
  - .pao-inbox/_state-snapshots/2026-05-21-plan-c-integration-plan.md (Wave 1+2+3 chapter map)
  - vol-2/ANNA-VOICE.md (anti-pattern list, esp. #1 aphoristic closes, #5 motif-phrase cap, #8 echo-and-confirm, #9 register overuse)
scope: 10 chapters — ch14, ch17, ch18 (Wave 1); ch01, ch07, ch10, ch11, ch12 (Wave 2); ch15, ch16 (Wave 3)
methodology: live-grep + paragraph context audit + insertion-site risk
artifact-status: READ-ONLY — punch list for PAO orchestrator + Yeoman; no chapter prose modified
failure-modes-hunted:
  - FM1 — tautological "X was the X" construction (the-noun-was-the-noun)
  - FM2 — architectural-noun-parade (abstract nouns piled without a physical referent)
  - FM3 — aphoristic-mush / packaged-truth paragraph closes
---

# Anti-tautology audit — Plan C rewrite-target chapters

## Reading guide

The Candidate 4 back cover is the calibration rubric. CIC retired Candidate
3 because three back-to-back opening sentences read *"the architecture
preserved what the architecture had been built to preserve / the forensic
substrate caught what the forensic substrate had been built to catch /
the graceful degradation absorbed what the graceful degradation had been
built to absorb"* — load-bearing in cadence, vacuous in content. Candidate 4
replaces those with concrete things the architecture caught: *the
pre-failure timestream / the firmware-update signature / the vendor's name
on the procurement paperwork.* That is the model. When this audit flags an
instance as DECORATIVE, the calibration is: would Candidate 4 have written
it this way? If the answer is no, the prose is at the Candidate-3 register
and needs to drop down to Candidate 4.

This audit walks 10 chapters in the order Plan C will rewrite them (Wave 1
first, then Wave 2, then Wave 3). For each chapter:

1. **Live-grep counts** for FM1.
2. **FM1 instances** — every hit, verdict (LOAD-BEARING / DECORATIVE /
   BORDERLINE), proposed replacement when DECORATIVE.
3. **FM2 instances** — sentences flagged as abstract noun-parade.
4. **FM3 instances** — aphoristic-mush paragraph closes.
5. **Plan C insertion risk** — for chapters slated for new prose, where the
   new prose lands AND which failure mode is the operative trap at that
   location.

A summary punch list closes the document with S/M/L sizing per chapter and
volume-wide priority order.

**Note on motif-phrase cap:** ANNA-VOICE.md anti-pattern #5 caps recurring
phrases at one per chapter — but cross-chapter recurrence at the volume
level *is* permitted for genuine voice tics. The "the X was the X"
construction is borderline-tic in Anna's executed register; it lands as
character (Anna's flat-affect duty-log shorthand under stress) when used
once or twice per chapter for chapter-load weight. It fails when it
becomes the chapter's default cadence for restraint. The verdict per
instance is calibrated against this distinction.

---

# Section 1 — Wave 1 chapters (LOAD-BEARING rewrites)

## Ch 14 — *The Crossing*

**Live-grep FM1 count:** 17 hits across 527 lines.

This is the chapter where the construction does its most work *and* breaks
down most. It is the highest-FM1-density chapter in the volume. Some hits
are LOAD-BEARING — Anna's flat-affect duty-log register holding under the
cascade is a literary effect the construction earns. Others are
DECORATIVE — the construction has become Anna's default cadence and is
saying nothing.

### FM1 instances

**Line 51 — "The push was the push of a man whose body had decided to be at the leak..."**
Verdict: **LOAD-BEARING.** This is the chapter's introduction of Joel's
push-past beat and the rhetorical move is "the push was the push of [a
specific man with a specific decision]" — the second "push" is not a
self-reference; it's setting up the descriptive clause that follows. The
construction earns its place because it triggers content. Keep.

**Line 99 — "The bridge was running on procedure. The procedure was the procedure I had read in the Mission Director's manual and had never executed against an active casualty event."**
Verdict: **LOAD-BEARING.** Same shape as 51 — second "procedure" sets up a
relative clause that lands a real content beat ("had never executed
against an active casualty event"). Keep.

**Line 143 — "Her position was the position the manual specified. She returned to the lab compartment."**
Verdict: **BORDERLINE / lean DECORATIVE.** The second "position" sets up
"the manual specified" — but the sentence carries no content the prior
sentence ("She knew the manual specified what she would do") hadn't
already established. The chapter has earned the move by line 143; the
move is doing redundant work here.
**Replacement:** *"She knew the manual specified what she would do at
each stage of the cascade. She returned to the lab compartment."* — drop
the position-was-the-position sentence entirely; the next sentence already
delivers the beat.

**Line 159 — "The clipboard's checklist was Sabina's cascade procedure. She had run it at every drill. The drills had been the drills. The procedure was the same."**
Verdict: **DECORATIVE.** Four consecutive flat-affect sentences and TWO
tautologies ("drills had been the drills" / "procedure was the same"
where "the same" relative to what is not specified). This is the
construction-as-stylistic-tic going past where it has utility. The reader
is being lectured on Sabina's preparation in a register that flattens
her.
**Replacement:** *"The clipboard's checklist was Sabina's cascade
procedure. She had run it at every drill since the Belo Horizonte
work-up. The procedure tonight was the same procedure; the alarm was
not."* — preserves the construction's rhythm at one instance, swaps the
second tautology for a content-bearing contrast (procedure same / alarm
not).

**Line 175 — "The procedure was the procedure — you do not leave a door open with active leakage..."**
Verdict: **LOAD-BEARING.** This one earns it: the second "procedure" sets
up the em-dash-introduced rule-statement that follows. The construction
is doing what construction does — naming a rule by quoting it. Keep.

**Line 189 — "I held the look for the duration the look required... The receipt was the receipt. He saw it. He turned."**
Verdict: **BORDERLINE / lean DECORATIVE on "The receipt was the
receipt"** — the line is structurally building toward the porthole-look
climax, but the receipt-was-the-receipt construction is the third
content-empty closer in close succession ("only the receipt of the look at
the level the look could be received at without breaking the standing").
The earlier "the look could be received at without breaking the standing"
is doing the load-bearing work; the "receipt was the receipt" is rhythm.
**Replacement:** *"only the receipt of the look at the level the look
could be received at without breaking the standing. He saw the receipt.
He turned."* — drop "The receipt was the receipt" entirely; the receipt
*landing* (he saw it; he turned) is the load-bearing beat.

**Line 217 — "The pattern was the pattern of vendor firmware updates on sensors deployed in OSS-architecture missions over the back four years..."**
Verdict: **LOAD-BEARING.** The second "pattern" sets up a relative clause
naming the actual pattern's content. This is exactly the Candidate-4
shape — name the thing, then name what specifically. Keep.

**Line 217 (second hit, same paragraph) — "The pattern was the kind of pattern she had been reading institutionally for the back several years against the OSS-architecture supply-chain landscape. The pattern was here now."**
Verdict: **DECORATIVE (the second hit).** This is the anti-pattern in
microcosm. Three "the pattern was [the pattern...]" sentences in a row;
the third ("The pattern was here now") collapses into pure tautology
because "here now" is what every prior sentence has established. The
paragraph reads as Anna's flat-affect saying "look at this look at this
look at this." The reader needs ONE pattern-statement, then a specific
piece of content.
**Replacement:** Cut "The pattern was the kind of pattern she had been
reading institutionally for the back several years against the
OSS-architecture supply-chain landscape." Replace with: *"She had been
reading this institutionally for several years against the
OSS-architecture supply-chain landscape. The shape was familiar. The
shape was here now."* — replaces tautology-repetition with verb (read /
was familiar / was here).

**Line 231 — "The recommendation had been Diego's. The recommendation had not been in the procedure manual."**
Verdict: **LOAD-BEARING.** Adjacent sentences with same subject but
different predicates — this is parallelism doing work, not tautology.
Keep. The construction names a contrast (Diego's recommendation vs
manual's specification).

**Line 277 — "I had not moved my hands from the rail... The face was the face."**
Verdict: **BORDERLINE.** "The face was the face" is the lone closer of a
paragraph that has just listed four operational acts Anna performed. The
closer can be read as Anna naming her composure without commenting on it
— which is the executed register — but it can also be read as her
narrating in flat-affect-as-mannerism. The paragraph closes a beat about
holding composure during the eleven minutes; the closer is doing a
restraint move.
Verdict refinement: **KEEP** as a single instance. Cap-1 per ANNA-VOICE.md
anti-pattern #5; this is the chapter's load-bearing instance of the
"the X was the X" close on composure. The chapter cannot have two of
these. The other one needs to go.
**Action:** Verify by audit that no OTHER paragraph in this chapter
closes on "the X was the X" composure-naming. If yes, this one stays;
the other is cut.

**Line 421 — Spanish letter: "*My love - the boat is the boat. The lights are red at this hour; the air smells of the system; the bunk is narrow.*"**
Verdict: **LOAD-BEARING.** This is Diego's voice, not Anna's. Diego's
parallel-translation idiom ("el barco es el barco" → "the boat is the
boat") is a deliberate register marker — Spanish-speaker writing in
parallel English. The construction here is *exactly* the kind of
construction Spanish-speakers reach for ("X es X" = settled-acceptance
register; closest English is "it is what it is"). The Plan C rewrite
should preserve this line untouched. Keep.

**Line 443 (also line 12 of the broader grep output) — "The watch rotations held. The cycle held. The standing was the standing."**
Verdict: **DECORATIVE.** Three back-to-back flat-affect sentences. The
first two are content-bearing (watch rotations held / cycle held); the
third is pure tautology and the closer pattern is exactly the
Candidate-3 vice. The paragraph has just delivered the boat-made-N-knots
mini-list (already a Bobiverse-style cadence beat) and the
standing-was-the-standing closer flattens it.
**Replacement:** *"The watch rotations held. The cycle held. The boat
held its tempo against the Drake."* — replace the third with a content
beat that physically grounds (the Drake).

**Line 465 — "The discipline had held its discipline across the mission. The recognition had held its discipline across the mission. The recognition had been disciplined. The recognition had not been spoken. The discipline had been the discipline that made Joel the engineer Anna Yusupova had recruited, and the recognition had been disciplined because Joel was the engineer he was, and the discipline had held for one hundred and forty-seven days from the recruitment interview until 0317 on Mission Day 47. The discipline had been adequate. The discipline had been the work."**
Verdict: **DECORATIVE (mixed) — load-bearing aphoristic-style paragraph
that has earned its place but is overworked.** This is the diary inset's
"discipline" paragraph and the chapter's prose-highpoint on Joel's
held-bearing. The paragraph runs eight instances of "discipline" + four
of "recognition" and the construction-density crosses from rhythm into
tic. The paragraph IS load-bearing in the chapter (it explains why the
porthole-look matters) but the prose can carry the load at lower
construction-density.
**Replacement:** Cut "The discipline had been the discipline that made
Joel the engineer Anna Yusupova had recruited" — collapses into
itself. Cut "The discipline had been adequate. The discipline had been
the work." — both terminal closers reach for aphorism. Replace closer
with concrete: *"The discipline held for one hundred and forty-seven
days from the recruitment interview until 0317 on Mission Day 47. It had
been the work of every one of them."* — the work has been done; the
work need not be named as work.

**Lines 469 (the "discipline cracked because" anaphora) and 477 (capture/receiving)** — these are different anti-patterns (anaphoric inventory; the receiving-was-the-receiving on line 477). For this audit:

**Line 477 — "The receiving was the receiving. The capture would not give me what I had at the porthole window. The capture would give me the capture."**
Verdict: **DECORATIVE.** Two consecutive tautologies in three sentences.
The middle sentence ("The capture would not give me what I had at the
porthole window") is doing the load-bearing work; the two flanking
tautologies are rhythmic filler that reads as Anna's prose stuttering.
**Replacement:** *"The capture would not give me what I had at the
porthole window. The capture would give me a recording. The two were not
the same."* — replaces tautology with content (recording vs receiving).

**Line 487 — "I was selfless in the moment because I had to be... the standing required the face; the face was the face."**
Verdict: **DECORATIVE on the closer.** This is the second composure-naming
"the X was the X" in the chapter (the first is at line 277). Per the
cap-1 ruling above, this one is the one to cut. The paragraph's content
beat is "the bridge required the standing" — the closer adds nothing.
**Replacement:** *"the standing required the face. I gave it what I
had."* — replaces the tautology with a single short sentence that lands
agency without aphorism.

### FM2 instances

**Lines 49-51 (damage report) — "Heavy-LLM hosting unavailable. Full-archive RAG index unavailable. Multilingual-real-time across all common pairs unavailable. Per-laptop nodes operational; transcription, common-pair translation, hash-chain integrity, KEK/DEK access control, signed audit log, and per-author personal RAG continue at full capacity."**
Verdict: **LOAD-BEARING.** This is a damage report, an in-prose log
artifact. The architectural-noun parade IS the genre — bureaucratic
register on purpose. Per ANNA-VOICE.md, log register is a permitted
voice mode. Keep.

**Line 99 — "The bridge had taken in the cascade window. The trim was adjusted. The depth was held. The ventilation was held against the smoke ingress that would follow the leak's source identification."**
Verdict: **LOAD-BEARING.** Each sentence names a specific action (trim,
depth, ventilation) tied to a specific outcome. Not abstract.

**Lines 467, 475 — post-cascade architecture-naming paragraphs.**
*"The architecture was at the operational tempo. The architecture was at
the operational tempo at reduced capability. The architecture had been
built so that the compute hub's loss would be capability loss, not
preservation loss. The architecture was operating at the case the
architecture had been built for. The protocol's environmental-stress
claim from Joel's paper had been exercised against literal physical
environmental stress. The protocol had held."*
Verdict: **DECORATIVE noun-parade.** Six sentences, each starting with
"The architecture" or "The protocol." Zero physical referents. This is
exactly the Candidate-3 vice ("the architecture preserved what the
architecture had been built to preserve") at chapter-scale.
**Replacement:** *"The architecture ran at reduced capability. The
compute hub was gone; the per-laptops held what the per-laptops were
specified to hold; the boat made its bearing. Joel's environmental-stress
claim from the paper had been exercised against actual coolant and
actual smoke. The claim held."* — names physical things (per-laptops /
bearing / coolant / smoke); reduces six sentences to four.

### FM3 instances

**Line 519 (diary close) — "The cracking is at the archive. The capture is at the archive. The receiving is in me."**
Verdict: **BORDERLINE → keep as LOAD-BEARING.** This is the diary's
chapter-close cadence and it lands as aphorism but the aphorism is
specific (archive / archive / me) not universal. Per the back-cover
calibration (*Only one of those documents serves the architecture. The
other serves Diego.* — two short parallel sentences as structural pivot),
this is the executed prose's analogous move and it is permitted.

**Line 517 — "The part is mine. The file is mine. The choice not to play the capture back is mine. The receiving was mine. The standing was mine. The boat is mine. The mission is mine. The discipline is mine. The cracking was his."**
Verdict: **BORDERLINE → DECORATIVE in the middle, LOAD-BEARING at the
endpoints.** Nine sentences with the same opener ("The X is/was mine"),
followed by a single contrast (his). The anaphoric run is well past the
ANNA-VOICE.md cap (`anaphora_max_run_length: 2`). The closer is the
load-bearing beat; the middle is filler.
**Replacement:** Compress to four sentences. *"The part is mine. The
file is mine. The boat and the mission and the discipline are mine. The
cracking was his."* — preserves the structural pivot at the end;
reduces the anaphoric run to within voice-spec.

### Plan C insertion risk for Ch 14

Per the integration plan, the cascade-core rewrite (lines 197-323) replaces
the executed prose's "Diego survives at console / Joel emerges alone"
sequence with "Diego goes down ladder first / Joel retrieves / Diego dies
in compartment." This is ~2,500-3,500 words of new prose.

**FM1 risk at insertion:** HIGH. The cascade-core rewrite operates in the
chapter's flat-affect duty-log register, which is exactly the register
where "the X was the X" reflexes fire. The drafter will be reaching for
this construction every time Anna needs a restraint beat. **Cap the new
prose at TWO instances of the construction across the entire rewrite, no
two adjacent.** The two earned instances should be: (a) one in the
cascade-core flat-affect operations sequence (Anna giving orders /
bridge holding); (b) one in the diary inset's grief-receiving sequence
(once, at chapter-load weight). All other restraint beats must land on
physical or actional content.

**FM2 risk at insertion:** HIGH. The damage report (line 49-51 area) will
need a fatality clause added. The fatality clause MUST stay at log
register (concrete: "asphyxiation and thermal injury in the post-leak
compartment environment; declared at 0408") and not drift into
architectural-noun-parade ("the architecture preserved what the architecture
could preserve about the fatality"). Per Plan C anti-pattern 6 (Diego's
death is not thematically justified), any sentence that asserts the
architecture's relationship to the death IS thematic justification and
must be cut.

**FM3 risk at insertion:** EXTREME. The new diary inset paragraph(s)
about Diego's death (per integration plan Item 9, ~150-250 words at
deepest interior altitude) is the chapter's single highest-risk
aphoristic-mush surface. Anna's voice has never been calibrated for
sustained grief; the drafter's reflex will be to package the grief into
truth. **Per ANNA-VOICE.md anti-pattern #1 and Plan C SPINE addendum A,
the diary inset's Diego paragraph MUST close on a concrete physical
detail OR a forward-motion transition, NEVER on packaged grief-truth.**
Pre-emptive flag examples of forbidden closes:
  - *"Some men do not come back, and we are the women who write their absence."*
  - *"Discipline is what the architecture cannot preserve."*
  - *"What the system holds is not the man."*
Acceptable closes:
  - A specific image — *"His mate-cup was on the polar-operations
    console. Hiroshi had not moved it."*
  - A forward-motion — *"I closed the file. The watch was at 0400."*
  - A question — *"What had I been told the procedure was for?"*

The drafter should compose the Diego paragraph with the close written FIRST
(pinned to a physical referent or action), then build the rest of the
paragraph back toward that close. Inverting the composition order is the
single best defense against FM3 at this site.

---

## Ch 17 — *Transit North*

**Live-grep FM1 count:** 3 hits across 305 lines. Lowest density in Wave 1.

This chapter's existing prose runs cleaner than Ch 14 on FM1 — Anna's
register here is institutional-reflective rather than cascade-flat-affect,
and the construction reflex doesn't fire as often. The chapter's
substantive risk is FM2 (the regulatory filing IS noun-parade by genre)
and FM3 (the diary close).

### FM1 instances

**Line 79 — "The analysis was the analysis Wanjiru had logged at 1207 on Day 48..."**
Verdict: **LOAD-BEARING.** Second "analysis" sets up a relative clause
naming what specifically the analysis is. Same Candidate-4 shape: name
the thing, then name what specifically. Keep.

**Line 85 (Joel's voice) — "The patch is the patch the manufacturer published."**
Verdict: **LOAD-BEARING but flag for read-aloud.** This is in Joel's
voice (italicized direct speech), and it reads as Joel's
honest-engineering refusal-to-embellish — *what the manufacturer
published is what we have*. The construction fits Joel's register
(nuclear-Navy flat-affect). Keep, but the drafter must avoid letting Joel
say this twice. One per Joel-voice beat, max.

**Line 179 — "The address was the address he had written on letters home from research stations across the back thirty-four years. The hand was the hand. The seal was a routine paper seal."**
Verdict: **BORDERLINE / LOAD-BEARING on "address," DECORATIVE on "hand."**
The first construction earns its place (the second "address" sets up the
load-bearing time-content "across the back thirty-four years"). The second
construction ("the hand was the hand") reaches for a recognition-by-Anna
beat — *I know this man's handwriting* — but does so without naming
anything. The third sentence ("The seal was a routine paper seal") is
content-bearing and clean.
**Replacement:** *"The address was the address he had written on letters
home from research stations across the back thirty-four years. The
handwriting was Diego's. The seal was a routine paper seal."* — replace
"hand was the hand" with the actional naming.

**Note:** Under Plan C, this scene is REPLACED (Diego is dead; the letter
was sealed Day 44, not Day 55). The replacement scene per integration
plan is Anna at the wardroom table reading the IAA's institutional
bereavement protocol. The replacement scene needs its own audit before
draft-state, but the executed scene's "hand was the hand" tic does not
carry into the replacement.

### FM2 instances

**Lines 161-163 (Joel's voice) — "The architecture's job at this case was preservation and detection. The architecture preserved the pre-failure timestream of the unit at the audit log under the unit's signing key. The architecture preserved the firmware-update event in chain. The architecture preserved the post-patch reading stream..."**
Verdict: **BORDERLINE → LOAD-BEARING per genre constraint, but flag for
post-Plan-C-addition pacing.** Joel is summarizing the forensic-substrate's
function in his own voice; the architectural-noun-density is appropriate
because this is a technical debrief, not narration. The construction is
LOAD-BEARING in genre.

However — under Plan C, this paragraph is followed by Joel's new
admission paragraph (the *I could have funded the fork at the
pre-procurement budget cycle* beat per Integration Plan §17 Item 2). The
existing "architecture preserved / architecture preserved / architecture
preserved" anaphora in Joel's voice followed by his admission paragraph
in his voice WILL stack two adjacent Joel-anaphoric runs and the second
will read as authorial preaching (anti-pattern 7).

**Pre-emptive fix (insertion-site direction):** When the admission
paragraph is drafted, it MUST NOT open with "I could have / I could have
/ I could have" or any anaphoric construction. It should open with a
specific timestamp or specific budget-cycle reference (per integration
plan target text: *"I could have funded the fork at the pre-procurement
budget cycle. The budget cycle was September of 2022."*) and proceed in
content-bearing flat sentences. Anaphoric structure in Joel's voice
within four paragraphs of itself becomes the chapter's voice signature
and reads as authorial.

**Lines 233-257 (regulatory filing) — "The cascade event of Mission Day 47 produced the failure of the starboard sensor head and collateral loss of the boat's compute hub. The boat's local-first architecture preserved the full pre-failure timestream of the failed unit, the firmware-update history, and the boat-internal replication of both at the standing capture..."**
Verdict: **LOAD-BEARING.** The regulatory filing is in-prose log artifact;
architectural-noun-parade is the *correct* register for a regulatory
filing. Per Plan C SPINE addendum B, the filing's procedural and
inconclusive register must survive Joel's admission unchanged. The
filing stays.

### FM3 instances

**Line 273 — "I closed the file. I closed the per-laptop. I went to bed."**
Verdict: **LOAD-BEARING. This is the gold-standard ANNA-VOICE.md
paragraph close — three short sentences, forward-motion transition, no
packaging.** Keep exactly.

**Line 199 — "I left the paragraph in the file. I closed the per-laptop."**
Verdict: **LOAD-BEARING.** Forward-motion close. Keep.

**The chapter has no FM3 instances at the executed close.** The chapter
already lands on Anna's procedural-act-of-recording register that Plan C
requires.

### Plan C insertion risk for Ch 17

Per the integration plan, two structural rewrites: (a) Joel's admission
paragraph (~150-200 words, his voice, in new paragraph after current
line 163); (b) replacement scene for the Day-55 Diego letter-sealing (~400-600
words at lines 203-225 area).

**FM1 risk at insertion (admission paragraph):** MEDIUM. Joel's voice
already runs flat-affect; the construction will reach. **Cap the
admission paragraph at ZERO "the X was the X" instances.** Joel's
admission cannot afford ANY tautological softening — the integration
plan's target text *"I could have funded the fork at the pre-procurement
budget cycle. The budget cycle was September of 2022. I had the line
item; I reviewed the line item against the architecture's first-year
deployment costs; I marked the line item as deferrable to the second-year
cycle on the reading that the vendor-signed update chain would carry the
deployment without a fork. The reading was the right reading at the time
I made it. The reading is the reading the data supports tonight."* —
contains two "the reading was/is the X" constructions. **Cut both.**
Replacement: *"The reading was correct at the time I made it. The
data tonight supports it."* — same content; no tautology.

**FM2 risk at insertion (admission paragraph):** MEDIUM. Joel's voice
will reach for architectural nouns (budget cycle / line item /
procurement / vendor / fork). The drafter should ensure the admission
names a **physical thing** somewhere in the paragraph. Per the back-cover
calibration: *the vendor's name on the procurement paperwork*. Joel's
admission should include at least one comparable concrete — a specific
date (September 2022 — already in target text); a specific dollar
amount or budget-line-number if Joel can be character-explicably specific
about it; a specific document (the procurement file Anna mentions in Ch
01).

**FM3 risk at insertion (admission paragraph):** EXTREME. The admission
*will* reach for an aphoristic close. Per Plan C SPINE addendum B and
anti-pattern 7, Joel's admission must close on a NAMING of cost, not on
a packaging of regret. The integration-plan target text closes on *"The
cost is in the compartment."* — this is the right move. **PRESERVE EXACTLY.**
No softening, no follow-up sentence in Joel's voice, no Anna-interior
paragraph immediately after.

**FM1/FM2/FM3 risk at insertion (Day-55 replacement scene):** The
replacement scene is Anna at the institutional register drafting the
bereavement notification. This is institutional-register work and the
constructions will not loop the way the cascade-core does. **Cap on
"the X was the X" at ZERO instances in the replacement scene** — the
scene is short (~400-600 words) and the construction adds nothing the
institutional register hasn't already established.

---

## Ch 18 — *Punta Arenas Surfacing*

**Live-grep FM1 count:** 11 hits across 435 lines.

The chapter is the volume's closing artifact. It carries the highest FM1
density outside Ch 14, primarily because the dockside-institutional
scenes and the final diary inset both fall into Anna's flat-affect
register at moments where the chapter is reaching for closing weight.

### FM1 instances

**Line 96 — "Her voice in the first message was at the tone I knew it at... The tone was the tone. She was fine."**
Verdict: **BORDERLINE → LOAD-BEARING.** This is the mother-voicemail
moment. "The tone was the tone" reads as Anna's mother-wound bearing —
recognizing the mother's familiar register without naming what it means
emotionally. The construction is doing real character work (Anna refusing
to perform emotional reaction). The closer "She was fine" is the
content-bearing payoff. Keep.

**Line 106 — "The system did not answer because the question was not a question the system could answer; the question was a question I would answer when I had thought about the maiden voyage long enough..."**
Verdict: **LOAD-BEARING.** The construction is parallelism doing work —
"not a question the system could answer / a question I would answer." The
contrast lands. Keep.

**Line 140 — "The English was the English. The English-as-second-language formality was the same it had been at Bremerhaven..."**
Verdict: **DECORATIVE on "English was the English."** The next sentence
already carries the content beat (English-as-second-language formality
preserved across years). The opening tautology is rhythm-filler.
**Replacement:** *"His English was unchanged. The
English-as-second-language formality was the same it had been at
Bremerhaven and at the Helsinki workshop in 2019 and at the Tromsø
workshop in 2023. The vocabulary was institutional. The cadence was
correct."* — replaces tautology with an actional contrast (his English
was unchanged).

**Line 144 — "The English was the English I had used when I had been at the AWI postdoctoral wardroom in 2010..."**
Verdict: **LOAD-BEARING.** The second "English" sets up a relative clause
that carries time-specific content. Keep.

**But:** This is the SECOND "The English was the English" within 4 lines
(line 140 and line 144). Per ANNA-VOICE.md anti-pattern #5 cap-1 rule,
one of them has to go. **Cut line 140's tautology (per replacement
above), keep line 144.**

**Line 156 — "The pause was the pause at which the institutional level stops being able to carry what is not at the institutional level. The pause was three seconds long. I did not note the pause aloud. Stefan did not note the pause aloud. The witnesses did not note the pause."**
Verdict: **LOAD-BEARING.** The second "pause" sets up the load-bearing
relative clause (the institutional level / what is not at the
institutional level). The four-sentence anaphoric run on "pause" is at
the cap (anaphora_max_run_length: 2 is exceeded — five sentences total).
However, the anaphoric run here is dialogue-pattern, not anaphoric
inventory; it's mimicking institutional silence as four-people-not-
noting-the-pause. The chapter has earned this. Keep with a flag.

**Note:** This is the Stefan-exchange beat. Under Plan C, the exchange
carries additional asymmetry weight (Diego's body in the logistics van).
The drafter must NOT add commentary on Diego's absence here; the
institutional level holds; Stefan does not know; Anna does not narrate.
The existing "pause" anaphora carries the asymmetry without naming it.
Keep.

**Line 174 — "The room was at the institutional level... The room was not the room at which Anna Yusupova would have narrated to anyone what had not been said. The room was the room at which the institutional level held."**
Verdict: **DECORATIVE.** Two "the room was the room" constructions in
adjacent sentences. The first is doing work (the negation — the room
was NOT the room where she would have narrated — names what the
institutional level forbids). The second collapses into tautology (the
room was the room at which the institutional level held = the
institutional level was holding).
**Replacement:** *"The room was at the institutional level. Holm was
speaking to Wanjiru at the table. The IAA's reception lead was speaking
to Diego at the door. Joel was at the room's north wall speaking to the
medical-clearance officer at the post-clearance. Anna Yusupova would not
have narrated to anyone what had not been said. The institutional level
held."* — replaces both tautologies with the action-content beat (Anna
would not have narrated) and the closing fact (institutional level held)
as direct statements.

**Note:** Under Plan C, the Diego reference at this line ("The IAA's
reception lead was speaking to Diego at the door") needs to be revised
or removed — Diego is dead at this point. The drafter should track this
in the wave-3 reframing pass.

**Line 230 — "The laughter was warm. The laughter was the laughter of two senior scientists at the close of a maiden voyage they had been on at the institutional level."**
Verdict: **LOAD-BEARING.** Second "laughter" sets up the relative
clause naming the specific kind of laughter. The construction is doing
the same Candidate-4 work: name the thing, then name what specifically.
Keep.

**Note:** This is also a Diego scene under Plan C (Diego at side table
laughing with Hiroshi). Under Plan C the scene cannot occur with Diego.
The integration plan handles this in the Wave-3 reframing for ch18; the
replacement scene removes the Diego-Hiroshi laughter beat. Verify in
Wave 3.

**Line 232 — "I noted Hiroshi at the institutional level the record would carry him at. I noted him also at the register the record would not carry. That second level was where the diary would carry him. The level was the level at which a man who had stopped drawing at twenty had been drawing in the back of every notebook for forty-five years..."**
Verdict: **LOAD-BEARING.** "The level was the level at which [specific
content follows]" — Candidate-4 shape. Keep.

**However:** Note the over-use of "register" / "level" in this paragraph
plus the prior chapters. Per ANNA-VOICE.md anti-pattern #9, register
overuse is BLOCKED at ≤3 per chapter. Cross-reference with the full
register-count audit (separate document); this is one of the candidates
to swap.

**Line 240 — "The bag was the bag he had brought aboard at Bremerhaven on Mission Day minus one; the same bag."**
Verdict: **LOAD-BEARING.** Construction earns its place — second "bag"
sets up a time-specific relative clause that physically grounds (Bremerhaven,
Day minus one). Keep.

**Note:** This is the Diego-at-gangway scene. Under Plan C, this scene
is REPLACED entirely (Diego is dead). The replacement scene per
integration plan §18 Item 6 needs its own anti-tautology audit at
draft-state, including a hard cap of ZERO "the X was the X" constructions
in the replacement scene (the scene is short and the construction adds
nothing).

**Line 272 — "The architecture had preserved what reached the consortium ports. The architecture had preserved Diego's photographs and Diego's logs and the unfinished paper in the canonical authored-content archive and the letter that would carry to María Elena at the post-handshake mirror against the IAA's institutional handshake. The architecture had not preserved Diego. The architecture had not been the architecture for Diego. The architecture had been the architecture for what Diego had made. Diego had preserved Diego."**
Verdict: **MIXED. LOAD-BEARING on first 3 sentences; DECORATIVE on
"The architecture had not been the architecture for Diego" + "The
architecture had been the architecture for what Diego had made"; the
final "Diego had preserved Diego" is the chapter's biggest
authorial-aphorism risk.**

This passage is the volume's load-bearing prose-highpoint per the
integration plan (§18 Item 6 marks it as "preserved EXACTLY in the Plan
C version" as "the volume's load-bearing sentence-cluster"). The Plan C
integration plan calls for preservation. **This audit disagrees with the
integration plan on this specific passage.** Reasoning:

The Candidate 4 back cover specifically called out and CUT *"He preserved
himself, in the way one preserves oneself by being the person one is"* —
Candidate 3's least defensible sentence. The Ch 18 passage at line 272
ends with *"Diego had preserved Diego"* — which is the same aphoristic
move at slightly higher concreteness (Diego rather than "oneself"). The
move is the same: take a verb (preserve), apply it to a subject (the
architecture), reverse it, apply to the subject the architecture didn't
preserve (Diego), and close on the subject as its own predicate (Diego
had preserved Diego).

Under Plan C, this passage CANNOT survive unchanged. The volume just
flagged this construction as the back cover's worst literary tic. The
chapter close cannot reproduce the move.

**Replacement (PAO recommendation, supersedes integration plan §18 Item
6's preservation directive):**

*"The architecture had preserved what reached the consortium ports. The
architecture had preserved Diego's photographs and Diego's logs and the
unfinished paper in the canonical authored-content archive and the
letter that would carry to María Elena at the post-handshake mirror.
The architecture had not preserved Diego. The architecture had not been
built to preserve him. The architecture had been built to preserve what
he made. He made the rest of it himself."*

What this preserves: the architecture-vs-the-man recognition; the
parallelism of preserved/preserved/not-preserved; the load-bearing
closing distinction (he made it himself).

What this changes: cuts "Diego had preserved Diego" (the tautology);
cuts "The architecture had been the architecture for what Diego had
made" (the second-order tautology); replaces with two flat statements
that name physical things he made (the photographs, the logs, the paper,
the letter — all already in the prior sentence; the closer references
what he made without re-tautologizing).

**This change requires CIC sign-off because it modifies a passage the
integration plan explicitly marked PRESERVE EXACTLY.** Flag at top of
audit summary.

**Line 315 — "I had not seen the writing for what it was at the institutional level until the moment Wanjiru had asked. The asking had named what I had been doing. The naming was the naming. The work was the work."**
Verdict: **DECORATIVE.** Two consecutive "the X was the X" constructions
closing the paragraph. Both reach for aphoristic structural-weight; both
collapse into themselves. The actual content is in the prior sentences
(the asking named what Anna had been doing).
**Replacement:** *"I had not seen the writing for what it was at the
institutional level until the moment Wanjiru had asked. The asking had
named what I had been doing. The naming had been Wanjiru's. The work was
ahead."* — replaces tautologies with attribution (Wanjiru's naming) and
forward-motion (work ahead).

**Line 341 (the diary inset's Diego paragraph) — "*Diego is going home. The architecture preserved his photographs and his logs and the letter and the paper. The architecture did not preserve him. He preserved himself. The architecture was the architecture for what he made. The desk at the lake side of the road into San Martín de los Andes is what he will write at. María Elena will cook in the kitchen. Sofía will come at school holidays. The architecture is not the architecture for any of that.*"**
Verdict: **MIXED. Same architectural-aphorism vice as line 272, but
under Plan C, Diego is dead, so the "Diego is going home / he will write
/ María Elena will cook / Sofía will come" sequence is itself a fiction
the chapter is no longer permitted to carry.**

The integration plan §18 Item 8 prescribes a specific replacement for
this paragraph. The replacement preserves "He preserved himself" and
"The architecture was the architecture for what he made" — both of which
this audit flags as DECORATIVE per the back-cover-Candidate-4 calibration.

**Replacement (PAO recommendation, supersedes integration plan §18 Item
8's specific target text):**

*"Diego is at the consortium-logistics-van at the Buenos Aires
post-handshake. The van that carried him pulled away from the dock at
0507 local this morning. María Elena will receive the body at the IAA's
institutional handshake within ninety-six hours. The desk at the lake
side of the road into San Martín de los Andes will hold the letter Diego
wrote on Mission Day 44 at the wardroom table, and the photographs from
the under-ice transit on Mission Day 35, and the Filchner-Ronne paper
at its draft state, and the leather mate-cup with the unpolished
bombilla. Sofía will know who her grandfather was. María Elena will know
what her husband had been writing the morning he died. The architecture
preserved what he made. He made the rest of it. The architecture has
nothing to say about that.*"

What this changes from the integration plan target:
- Cuts "He preserved himself in the moment his body chose to go to the
  failure point at the operational tempo he had been carrying for
  thirty-five years" — this is the integration plan's most thematically
  loaded sentence (per Plan C anti-pattern 6, no sentence in which
  Diego's death "means" something — and "his body chose to go to the
  failure point" reaches for meaning).
- Cuts "The architecture was the architecture for what Diego had made"
  (second-order tautology).
- Replaces "The architecture is not the architecture for any of that"
  with "The architecture has nothing to say about that" — preserves the
  architectural-distance beat without the tautology.
- Closes on the architecture being silent rather than on the architecture
  being-not-itself. The silence is the correct landing per Plan C
  addendum A (grief at institutional register, never at narrator register).

### FM2 instances

**The dockside reception scenes (lines 130-270 area) — heavy
architectural-noun-density at "consortium" / "institutional" /
"post-handshake" / "standing" / "mirror" / "channel" / "throughput" /
"queue."**

Verdict: **LOAD-BEARING.** This is the chapter's institutional register
and the noun-density is genre-appropriate. The back-cover rubric does
not apply here because these scenes are operating at a different
altitude than the back cover's narrator-voice — they are in-prose log
artifacts of institutional process. Keep.

### FM3 instances

**Line 381 (diary close) — "The mission is at the close. The contest is
at the institutional level. The architecture has held. The convention is
older than the architecture. The convention will hold."**
Verdict: **BORDERLINE → DECORATIVE.** Five short flat-affect sentences
closing on a generalization (convention will hold). The closer reaches
for permanence-claim that the volume's restraint discipline does not
support. Per ANNA-VOICE.md "A paragraph in Anna's narration may NOT end
on... a 'We are all of us...' universal claim," this is the bordering
case — "the convention will hold" is a generalization about institutional
practice, not about humanity, but it is still future-tense aphorism.
**Replacement:** *"The mission is at the close. The contest is at the
institutional level. The architecture has held. The convention has been
held tonight by the directors who came before me, and will be held by
those who come after."* — replaces "convention will hold" (vague future-
permanence claim) with "has been held / will be held by [specific
agents]" — same continuity claim, grounded in agents.

**Line 383 — "*She will read it at the start of her selection cycle.
She will not know my name until she opens the file. She will not need
to.*"**
Verdict: **LOAD-BEARING.** Specific image (next mission director
reading at selection cycle); concrete closer (She will not need to);
forward-motion through time. Keep exactly.

**Line 385 — "*The file is open. I am at the desk.*"**
Verdict: **LOAD-BEARING.** Forward-motion close; physical detail. The
chapter's defining close. Keep.

**Line 421 — "I kept writing."**
Verdict: **LOAD-BEARING.** Single short sentence; forward-motion; no
packaging. Chapter's volume-close. Keep.

### Plan C insertion risk for Ch 18

The chapter has multiple insertion sites under Plan C: the Diego-fatality
clause in the final mission log; the bereavement-officer micro-scene;
the secondary-logistics-van replacement scene (the Diego-at-gangway
substitute); the diary-inset Diego paragraph rewrite; the
Anna's-choice beat.

**FM1 risk at insertion (Diego-fatality clause in mission log):** LOW.
Log register; the construction will not reach.

**FM1 risk at insertion (bereavement-officer scene, ~100-200 words):**
LOW-MEDIUM. Procedural-register scene; the construction may reach for
restraint. **Cap at ZERO "the X was the X" instances.**

**FM1 risk at insertion (secondary-logistics-van replacement scene,
~400-600 words):** MEDIUM. The scene is Anna receiving the letter +
mate-cup from Maria; it carries grief-receiving weight that will reach
for restraint constructions. **Cap at ONE instance, and only if it lands
on a relative clause carrying content (Candidate-4 shape).**

**FM2 risk at insertion (secondary-logistics-van scene):** HIGH. The
scene names institutional artifacts (consortium-logistics-van, IAA's
institutional bereavement protocol, Punta Arenas surface handshake,
post-handshake mirror, ninety-six hours, Belgrano post-handshake, etc.).
The drafter must include at least one CONCRETE PHYSICAL referent
beyond the institutional language. Candidates: the dock itself (the wood
of the gangway, the morning light, the temperature of the air), Maria's
hands as she gives Anna the envelope, the weight of the leather mate-cup,
the unpolished bombilla, the wax of the seal on Diego's envelope. The
back-cover Candidate 4's parallel: *Diego Sá made it nineteen steps down
the access ladder* — physical, countable, embodied. Scene-close must
land on a physical detail or an action, not on an institutional naming.

**FM3 risk at insertion (Diego-paragraph in diary inset):** EXTREME. See
the substantive flag above at line 341 — the integration plan's target
text reproduces the back-cover-Candidate-3 vice. PAO orchestrator MUST
make a ruling: either (a) accept the audit's proposed replacement
(cuts "He preserved himself" and "The architecture was the architecture
for what Diego had made"); (b) confirm the integration plan's target
text and accept the inconsistency with the back cover Candidate-4
rubric; (c) draft a third option that threads the needle.

**FM3 risk at insertion (Anna's-choice beat per integration plan §18 Item
9):** MEDIUM. The beat is procedural — Anna writes Joel's admission into
the staff history record. The beat is "the paragraph Anna writes" / "the
paragraph carries Joel's admission." Per integration plan, this scene is
preserved structurally; Plan C only adds the admission's content to the
paragraph. The risk is the surrounding paragraphs reach for heroic
register (heroism-of-surfacing) rather than procedural register (act-of-
recording). The integration plan flags this already; this audit
endorses the flag.

---

# Section 2 — Wave 2 chapters (foreshadowing inserts)

## Ch 01 — *Departure*

**Live-grep FM1 count:** 1 hit across 211 lines. Cleanest chapter in the
target set.

### FM1 instances

**Line 181 — "The cabin was the cabin. It always is."**
Verdict: **LOAD-BEARING.** The construction here lands as character-tic
(Anna refusing to redecorate, refusing to perform). The "It always is"
follow-up is the load-bearing content beat — three-prior-missions-in-
this-cabin without ceremony. Keep.

This chapter's executed prose runs almost entirely free of FM1. Anna's
voice in Ch 01 has not yet been calibrated to flat-affect duty-log
register; she is in pre-mission narrative-introduction register, which
runs richer in image and parenthetical aside. The construction does not
reach. The Plan C foreshadowing additions (Edit 1 + 2 per integration
plan §1) are slated to land in the briefing-paragraph area (lines
115-121), which runs in narrative register; FM1 risk at insertion is
LOW.

### FM2 instances

None at chapter scale. The executed prose grounds nearly every
architectural reference in physical/sensory content (the wardroom's
diesel smell, the cabin's bunk and bookshelf, the cup Joel was holding,
the postcard's card stock).

### FM3 instances

**Line 117 — "With the benefit of what I learned later, I am leaving
this on the page: I had read all three. I had considered all three
acceptable. I am not going to pretend I caught something I did not
catch."**
Verdict: **LOAD-BEARING.** This is the chapter's canonical retrospective-
frame beat that the SPINE references explicitly. The close ("I am not
going to pretend I caught something I did not catch") is the retrospective
narrator's bearing — acknowledging the limit of foresight without
packaging it. Keep.

**Line 189 (mother-wound paragraph close) — "I have stopped believing
her words. I have not, in any meaningful way, stopped being driven by
them. There is a difference, and I have not, in forty-seven years,
earned the right not to notice it."**
Verdict: **LOAD-BEARING.** This is the volume's canonical mother-wound
beat. The close ("I have not earned the right not to notice it") is
specific (forty-seven years), grounded in Anna's biography, and refuses
the packaging that would make it a universal claim. Per ANNA-VOICE.md
"Mother wound" section, this paragraph is the canonical model for how
the wound lands. Keep exactly.

**Line 201 — "I set it aside. I went to sleep."**
Verdict: **LOAD-BEARING.** Forward-motion close. Keep.

**Line 203 — "I am leaving this on the page not because the feeling
turned out to be correct - it did, and the correctness was useless. At
22:51 on the fourteenth of February I could not have done anything with
it that I had not already done with the laptop open. The consortium
archive has the firmware log and the timestamps and the official record.
What it does not have is the feeling I had that night, and that is the
part of this story I most want, looking back, to have respected."**
Verdict: **BORDERLINE → LOAD-BEARING.** The close ("the part of this
story I most want, looking back, to have respected") reaches for
retrospective-narrator weight. But it lands on a specific noun (this
story / looking back / respected) and not on aphorism. The construction
"I most want, looking back, to have respected" is grammatically
recursive but content-specific. Keep — but flag for Plan C's Edit 2
risk (see below).

### Plan C insertion risk for Ch 01

Per integration plan, two additions: (a) 80-120 words on Joel's
procurement-decision pre-mission walkthrough including the phrase *"the
call I am still not sure about"*; (b) optional 1-sentence retrospective-
frame extension after the "nobody is going to die" briefing close.

**FM1 risk at insertion (Edit 1, Joel procurement walkthrough):** LOW.
Anna's narrative register in Ch 01 does not reach for the construction.
The drafter must keep the new paragraph in Anna's pre-mission narrative
register, not in the later cascade-flat-affect register.

**FM2 risk at insertion (Edit 1):** LOW-MEDIUM. The new paragraph
mentions "firmware fork," "off-the-shelf with vendor-signed updates,"
"procurement file" — these are architectural nouns. The drafter must
ground the paragraph in a physical/sensory referent. Candidates from
the existing scene (lines 113-121 area): the wardroom-still-smelling-
of-diesel detail; the white bakery box on the table; the pot of coffee
already mostly gone; Wanjiru's notepad. The new paragraph should
reference at least one of these to keep it in the chapter's existing
sensory register.

**FM3 risk at insertion (Edit 2, optional retrospective-frame
sentence):** HIGH. The integration plan target text — *"I helped where
I could help. I did not always know which moments would be the ones I
could not."* — IS APHORISTIC. Two parallel sentences ending on a
recursive subordinate clause ("which moments would be the ones I could
not [help in]"). This is the Janeway aphoristic-close move that
ANNA-VOICE.md anti-pattern #1 specifically prohibits.

**PAO recommendation:** OMIT Edit 2. The integration plan flagged it as
optional. The audit confirms the optional flag — the sentence is in
the prohibited register. The retrospective-frame's existing beat (line
117, *"I am not going to pretend I caught something I did not catch"*)
already lands the retrospective gravity Plan C needs Ch 01 to carry. A
second retrospective beat in the briefing close is redundant AND
aphoristic. Cut.

**If CIC overrides the OMIT recommendation:** rewrite the target text to
land on action rather than aphorism. *"I helped where I could help. I
did what was in front of me. I am writing this knowing what I did not
do."* — replaces the recursive-aphoristic close with three short flat-
sentences; the third sentence preserves the retrospective-frame's
gravity without packaging.

---

## Ch 07 — *Joel's Sunfish*

**Live-grep FM1 count:** 12 hits across 251 lines. The chapter is
SSN-649 disclosure scene; Joel's voice carries flat-affect register;
the construction reaches.

### FM1 instances

**Line 25 — "The wardroom hum was the hum of a galley refrigerator and
the recirculation fans and the deck plate above us... The hum was the
hum the hum had been on every night I had been on the boat."**
Verdict: **DECORATIVE on the second sentence.** Three "hum" instances
in eight words ("The hum was the hum the hum had been") — the
construction has collapsed into stuttering.
**Replacement:** *"The wardroom hum was the hum of a galley
refrigerator and the recirculation fans and the deck plate above us
that carried the bridge watch's footstep when one happened to land in
the band the deck plate transmitted. It was the same hum the boat had
carried every night I had been on her."* — replaces tautology-stack
with a single content-bearing recognition.

**Line 51 — "I had said *acknowledged* the way I said *acknowledged*
on the bridge... The word had arrived because the word was the word
the moment wanted... the level was the level the conversation needed
to be at."**
Verdict: **MIXED. LOAD-BEARING on "the word was the word the moment
wanted" (it sets up an actional clause); DECORATIVE on "the level was
the level the conversation needed to be at."** The second instance is
the third construction in close proximity and reads as Anna's prose
losing density.
**Replacement (for second instance only):** *"We were two senior
operators in a wardroom and we had been at this level for the entire
mission and on the recruitment call before that. The conversation
needed it."* — replaces the tautology with the content beat
(conversation needed it).

**Line 61 (Joel's voice) — "The boat was eighteen years old when I
joined her. She had been built for the late seventies and the
discipline she ran on was the discipline the late-seventies boats ran
on. The men on her were the men the discipline produced. The boat was
a fast attack and the duty was the duty fast attacks did..."**
Verdict: **MIXED.**
- *"the discipline she ran on was the discipline the late-seventies
  boats ran on"* — **LOAD-BEARING.** Second "discipline" sets up
  time-specific relative clause (late-seventies boats); the construction
  is doing Candidate-4 work.
- *"The men on her were the men the discipline produced"* —
  **LOAD-BEARING.** Same shape; the second "men" sets up the
  production-by-discipline content.
- *"the duty was the duty fast attacks did"* — **LOAD-BEARING.** Same
  shape; the second "duty" sets up the fast-attacks specifier.

All three instances are in JOEL's voice, in a recruitment-disclosure
monologue. Joel's nuclear-Navy register is one of the rare voices in the
volume where the construction is character-correct because Joel's flat
delivery is part of his characterization. Keep.

**BUT:** Three instances in five sentences exceeds the cap. Per
ANNA-VOICE.md cap-1 motif rule, Joel's voice should still observe a
hard cap; the volume cannot accept "this is just how Joel talks" as
license to triple the construction inside a single paragraph. **Cut the
weakest of the three.** Recommendation: cut *"The men on her were the
men the discipline produced."* Reasoning: the discipline-by-itself
content is carried in the prior sentence ("the discipline she ran on
was the discipline the late-seventies boats ran on"); the men/discipline
beat duplicates. Replacement: *"The men on her had been built by it."*
— preserves the discipline-produced-them content; cuts the tautology.

**Line 65 (Joel's voice) — Long monologue, multiple instances:**
- *"The casebook is a starting point. The procedure is what you do
  when the casebook is one minute behind the boat."* — **LOAD-BEARING.**
  Parallelism doing content-work (casebook / procedure as separable
  things). Keep.

**Line 69 — "The tempo was the tempo Wanjiru had used at the comm
space on the morning of Day 21... The tempo was the tempo Joel had used
in the conference space on the morning of Day 7... The tempo was a
tempo I had marked in him three different times and was marking again.
He was telling me about the boat at the tempo he used for telling me
about the architecture. The two tempos were the same tempo."**
Verdict: **MIXED → DECORATIVE on cumulative density.** Five "tempo"
instances in five sentences plus a closing tautology ("The two tempos
were the same tempo"). The first two instances are LOAD-BEARING (each
sets up a specific time-and-place referent — Wanjiru at the comm space
Day 21; Joel at the conference space Day 7). The third instance starts
to loop ("The tempo was a tempo I had marked in him three different
times and was marking again"). The fourth is content-bearing ("at the
tempo he used for telling me about the architecture"). The fifth ("The
two tempos were the same tempo") is the closer and collapses.

**Replacement:** *"The tempo was the tempo Wanjiru had used at the comm
space on the morning of Day 21 to walk me through the priority queue.
The tempo was the tempo Joel had used in the conference space on the
morning of Day 7 to walk me through the partition. I had marked it in
him three different times across the mission and was marking it again.
He was telling me about the boat at the rate he used for telling me
about the architecture. The rate was the same."* — preserves the two
load-bearing instances; cuts the looping third and the collapsing fifth;
swaps the closer to "the rate was the same" (one tautology removed,
content equivalent).

**Line 87 (Joel's voice) — "I watched a lot of senior engineers tell
senior managers that the cloud platform the company was running on was
making decisions it was going to regret, and I watched the senior
managers run the platform anyway because the platform was the platform
on the budget."**
Verdict: **LOAD-BEARING.** Second "platform" sets up "on the budget" —
specific institutional content. Keep.

**Line 139-143 ("the prose was the prose of a man" anaphoric run) —
This is FM3 (anaphoric inventory) more than FM1, but the construction
overlaps.**
*"I had noted the texture of the prose. The prose had been the prose
of a man who did not soften. The prose had been the prose of a man who
did not stage. The prose had been the prose of a man who had been
operating on a system that decided ten years before the paper was
written that the system was going to be honest about what it had and
what it did not have, and the prose had inherited the system's
discipline without commenting on the inheritance."*

Verdict: **DECORATIVE.** Three "The prose had been the prose of a man
who..." sentences exceeds anaphora cap; the construction's content is
in the relative clauses (didn't soften / didn't stage / had been
operating on a system that...), so the anaphora is rhythmic
amplification, not structural.

**Replacement:** *"I had noted the texture of the prose. The prose was
of a man who did not soften and did not stage. He had been operating on
a system that decided ten years before the paper was written that the
system was going to be honest about what it had and what it did not
have, and the prose had inherited the system's discipline without
commenting on the inheritance."* — collapses three anaphoric sentences
into two; preserves all content.

**Line 147 — "The wardroom was the wardroom. The clock was the clock.
The naming would have been ceremony. We were not in the frame the
ceremony belonged in."**
Verdict: **DECORATIVE on both opening tautologies.** This is the
chapter's "we sat with the recognition" beat, and the executed prose
opens it with two flat tautologies that are exactly the construction
the back cover Candidate 4 cut. The naming-content is in the third and
fourth sentences.
**Replacement:** *"Neither of us spoke. The clock at the bulkhead read
its hour. Naming what we had recognized would have been ceremony. We
were not in the frame the ceremony belonged in."* — replaces the
two tautologies with sensory grounding (silence + clock-reading) and
preserves the content beats.

**Line 181 — "The shape had been the shape of submarine engineering
written into civilian distributed-systems work... I had bet on the
shape and the shape had been the discipline of a man who had been
honest about what his system had and what his system did not have for
fifteen years before he sat down to write a paper."**
Verdict: **LOAD-BEARING.** Two "shape" instances each carry a relative-
clause content (submarine engineering / discipline of a man). Keep.

**Line 215 — "I sat at the desk. The wardroom was the wardroom. The
hum was the hum. The clock at twenty-three forty-three was the clock
at twenty-three forty-three."**
Verdict: **DECORATIVE.** Three consecutive "X was the X" constructions.
This is the chapter's transition-back-to-narrative-after-disclosure beat;
the construction-density here reads as Anna's prose marking-time. The
content (Anna sat at the desk; she returned to her station; the boat
would resume Segment 2) lands in the surrounding sentences.
**Replacement:** *"I sat at the desk. The wardroom was empty around me.
The hum continued. The clock read twenty-three forty-three. The window
had twenty-nine hours and forty-seven minutes left on it. The boat
would dive at oh-five-thirty on Day 23 and Segment 2 would commence at
the routine tempo and the architecture would resume the partition
bearing the architecture had been honest about since the morning of
Day 7."* — replaces three tautologies with content-bearing observations
(empty around me / continued / read twenty-three forty-three).

### FM2 instances

**Lines 130-150 (the architecture-discipline disclosure passages) —
Joel's voice doing architectural-discipline meta-commentary.**

*"The architecture's procedural rigor is the procedural rigor of a
casualty drill. The architecture's redundant-indications expectation is
the redundant-indications expectation of an engine room..."*

Verdict: **LOAD-BEARING.** This is Joel's structured disclosure in his
own voice, with each "architecture's X" sentence anchored to a specific
naval-discipline referent (casualty drill, engine room, watch handoff,
gauge-in-front-of-you, etc.). The pairings make the noun-parade carry
its weight. Keep.

### FM3 instances

**Line 207 — "The architecture's discipline was the source's discipline.
The source was gone."**
Verdict: **LOAD-BEARING.** This is the chapter's structural pivot
sentence — short, specific, no packaging. Keep.

**Line 211 — "I noted, in a frame I would not name aloud either, the
texture of the man across the desk from me... The setting-down was a
setting-down. I saw the setting-down. I saw the man who had set it
down."**
Verdict: **DECORATIVE on closer.** Three consecutive "setting-down"
nominals; the closer reaches for poignancy ("I saw the man who had set
it down") that lands as aphorism. The content (Anna recognized Joel
had decided to disclose; the disclosure was a deliberate decision) is
in the prior sentences.
**Replacement:** *"I noted, in a frame I would not name aloud either,
the texture of the man across the desk from me. I had been taking
Joel's measure in the operational bearing since the recruitment call.
The operational bearing was not the only bearing I was measuring him in
tonight. The wardroom hum was the wardroom hum. The light was the
wardroom light. Joel was Joel, in the chair across the desk, with the
empty coffee mug at the precise place he had set it down before, and
his eyes were the eyes of a man who had finished telling me a thing he
had been carrying for some time. He had set it down. I had seen him do
it."* — replaces three-fold setting-down repetition with two short
sentences that name the act (set it down / saw him do it) without
aphorism.

### Plan C insertion risk for Ch 07

Per integration plan, one addition: 100-150 words of Joel's voice (or
Anna's interior on Joel's voice) on the discipline of resource trade-offs
at the funding-decision altitude, slated to land near the SSN-649
disclosure paragraph.

**FM1 risk at insertion:** EXTREME. Ch 07 has 12 FM1 hits in the
executed prose, and Joel's voice reaches for the construction every
beat. The Plan C addition is IN Joel's voice. The drafter will reach
for "the discipline was the discipline" or "the trade-off was the
trade-off." **Cap the new prose at ZERO "the X was the X" instances.**

The addition's content is the discipline-of-resource-trade-offs at
funding-decision altitude. The drafter should pick concrete physical
anchors from the SSN-649 era: a specific deployment budget; a specific
piece of equipment the boat was deployed without; a specific scene from
Joel's nuclear-Navy years; the leather-wallet detail from Ch 16. The
addition must land in a SCENE, not in an abstraction. Candidate
opening: *"He set the empty mug down. He looked at the porthole. He
said: 'The Sturgeon-class boats deployed on the budget the year they
deployed. We deployed without the gear we wanted because the gear we
wanted was not in the cost envelope the consortium was running on.'"*
— grounds the abstraction in a specific (mug / porthole / Sturgeon-class
deployment year / cost envelope).

**FM2 risk at insertion:** HIGH. The addition is about discipline /
resource / trade-off / funding / consortium / procurement / fork — all
architectural nouns. The drafter MUST include at least one physical
or sensory referent. The integration plan's directive ("Joel does not
preach about the funding constraint") is correct but does not flag the
noun-parade risk specifically. This audit adds the flag.

**FM3 risk at insertion:** MEDIUM. The addition closes near the
SSN-649 disclosure climax (Joel: *"The discipline is somewhere else."*).
The Plan C addition cannot reach for parallel rhetorical weight; it must
land at the operational register, not the structural-pivot register.
Per integration plan: "The reader who re-reads this chapter after Ch 17
will register the gravity." That's the right frame — the addition is
character depth, not foreshadowing. The drafter's check: read aloud;
if the addition lands at the same altitude as "The discipline is
somewhere else," cut and lower the altitude.

---

## Ch 10 — *Aftermath of a Mission That Once Was*

**Live-grep FM1 count:** 3 hits across 185 lines.

### FM1 instances

**Line 22 — "The calibration ran for the time it took her to satisfy
herself that the desk was the desk and that I was at it because I had
chosen to be."**
Verdict: **LOAD-BEARING.** The construction here is doing a specific
character-discrimination move (Maria checking that Anna was at the desk
voluntarily, not in a state of distress). The second "desk" is part of a
content-discriminating clause ("I was at it because I had chosen to
be"). Keep.

**Line 92 — "The institute's institutional interests were the interests
she was paid to carry. She handled the conversation within those
interests with the calibration of a senior officer who had handled
many such conversations. The conversation was the conversation she had
come to have."**
Verdict: **LOAD-BEARING on the first; BORDERLINE on the closer.**
"The institute's institutional interests were the interests she was
paid to carry" earns its place (second "interests" sets up "paid to
carry"). The closer "The conversation was the conversation she had come
to have" sets up "she had come to have" — relative clause with content.
Keep both.

**Line 142 — "The cup of tea at my left elbow was cold. The clock on
the bulkhead read oh-four-twelve. The watch had been the watch for an
hour and twenty-one minutes since Maria had crossed the wardroom and
recrossed it. The boat was at depth."**
Verdict: **LOAD-BEARING.** The construction ("The watch had been the
watch for an hour and twenty-one minutes") IS doing content work — the
second "watch" sets up the specific duration (an hour and twenty-one
minutes). Without the construction, the sentence would lose the
flat-affect register that grounds the diary-inset's interior. Keep.

### FM2 instances

The chapter's prior-mission interior (lines 75-180) runs heavy on
architectural language at the institutional level — non-disclosure-
under-pressure, disclosure-without-compulsion, the architectural inverse,
the architectural property, the institutional discipline. The
abstraction-density here is exceptionally high — and yet the chapter
LANDS, because each abstract construct is paired with a specific
biographical anchor (Tomáš Havránek dying; Stefan on the dock six days
later with the folder Anna had built; Astrid in the debrief room with
the calibrated-acknowledgment language; Joel's four-sentences-and-the-
fifth admission; Priya's fourth pass; Wanjiru's exception-refusal).

Verdict: **LOAD-BEARING.** This is the chapter's structural mode — Anna
naming what she had been selecting for. The abstractions are working
because each one is anchored to a named scene. Keep.

**One sentence to watch:** Line 167 — *"My father's mother had the
practice of naming what had happened, in plain words, before she did
anything about it. The naming was her work before any other work could
begin."* The closer ("The naming was her work before any other work
could begin") reaches for aphoristic structural weight; in the executed
prose it lands because the prior sentence has specified *what* the
grandmother named (the cut on Anna's wrist, in Uzbek, by name). The
abstract closer is permitted because it has a physical referent two
sentences back.

Verdict: **LOAD-BEARING.** Keep.

### FM3 instances

**Line 173 — "I have not forgiven Stefan. I have not absolved Astrid.
I have not closed the question of what was owed to Tomáš Havránek's
mother that has not been paid. The architecture does not close those
questions. The architecture is a different question, asked at a
different scale, in a vocabulary that the question of what was owed
cannot be answered in."**
Verdict: **LOAD-BEARING.** The close ("the architecture is a different
question... in a vocabulary that the question of what was owed cannot
be answered in") reaches for aphoristic-structural weight but lands on
a SPECIFIC distinction (the architecture vs the question of what was
owed). Per ANNA-VOICE.md, this is permitted — Anna naming a structural
distinction, not packaging human wisdom. Keep.

**Line 175 — "What I know tonight is what mine had been forged in, and
what I had built around me on this boat, and what the building had
cost."**
Verdict: **BORDERLINE → DECORATIVE.** Three-fold anaphoric inventory
("what... what... what...") closing on a generalization ("what the
building had cost"). The construction reaches for chapter-close weight.
**The sentence is doing canonical Anna-narrator work** — naming the
chapter's thematic shape — but per the back-cover Candidate-4
calibration, sentences that close on abstract cost-naming ("the
building had cost") without specifying what cost are exactly the
prose-fail mode.
**Replacement:** *"What I know tonight is what mine had been forged in,
and what I had built around me on this boat. I do not yet know what it
had cost."* — replaces the third anaphoric clause with a forward-
motion close (don't yet know) that acknowledges cost without
generalizing it.

**Line 177 — "I do not know yet what trust costs to harden. I am
sitting with the question."**
Verdict: **LOAD-BEARING.** The close is a literal acknowledgment of
not-knowing, paired with a present-moment action (sitting with the
question). Per ANNA-VOICE.md, this is the acceptable register — a
question, real or rhetorical-without-aphorizing. Keep.

### Plan C insertion risk for Ch 10

Per integration plan, one addition: 100-200 words of Anna's interior at
the *threat-of-loss-becomes-specific* altitude, naming what she would
owe to each member of the current crew if the mission cost her one of
them.

**FM1 risk at insertion:** LOW. The chapter's executed prose runs low
on FM1; the new prose will be in Anna's prior-mission-interior register,
which does not reach for the construction.

**FM2 risk at insertion:** MEDIUM. The new prose names crew members by
role and by what Anna has selected them for. Per the integration plan's
own directive: "the naming is specific (each crew member by role and by
what Anna has selected them for) but does not foreshadow Diego in
particular." Risk: the new prose may land as a list of architectural
roles (the polar-operations specialist; the principal architect; the
relay-operations officer; the medical officer; the chief scientist;
the logistics officer; the instrumentation specialist) without
attaching each role to a specific Anna-selected-quality. The drafter
must pair every role-naming with a quality-naming. Example: *"What I
owed Diego was the recognition that he read the consoles at the rate
the consoles needed reading."* The recognition (Diego's reading at
console-rate) is the qualitative anchor; the role (Diego) is the
addressee.

**FM3 risk at insertion:** EXTREME. The new prose closes on what Anna
WOULD owe IF she lost one of them. The prose is structurally
counterfactual ("if I had to give this list... if I were the one
giving the list to María Elena..."). Counterfactual prose at chapter-
interior altitude is one of Anna's voice's worst aphoristic-mush traps;
the executed prose at Ch 10 avoids it by staying in past-tense for the
prior mission and future-tense for the unknown ahead. The new prose
must NOT open or close on a counterfactual sentence. It must stay in
present-tense diary register: *"Tonight I do not know which of them I
would be writing about. The list is at the wardroom table. The
list is in my head. The list does not yet have a name on it."* — names
the act of listing without naming what the listing would contain.

The drafter should compose the new paragraph with the close written
FIRST (per the Ch 14 FM3 protocol), pinned to the diary-register
present-tense. The close must NOT generalize about command (*"this is
what it means to carry crew"*) or about cost (*"some debts come due
unexpectedly"*) or about preparation (*"I prepare the list because
preparing is what I can do"*). The close must name a specific present-
tense action.

---

## Ch 11 — *Second Surface, Second Forsaken Reveal*

**Live-grep FM1 count:** 4 hits across 200 lines.

### FM1 instances

**Line 57 — "*Three passes. Clear.* She did not elaborate. She did not
need to. The discipline was the discipline."**
Verdict: **DECORATIVE.** "The discipline was the discipline" closes a
paragraph that has already named Priya's discipline three times in the
prior sentences (three-pass schema check / clean read on third pass /
clipped one-word cadence). The closer is rhythm-only.
**Replacement:** *"*Three passes. Clear.* She did not elaborate. She
did not need to. Anna had marked Priya's schema-state-check pattern at
the first segment boundary on Day 21 and noted it again now without
comment."* — drops "The discipline was the discipline" sentence
entirely; the Anna-noted-pattern sentence already carries the content.

**Line 131 — "The institution was the institution. The procedure was
the procedure. The cross-check had landed."**
Verdict: **DECORATIVE on the two opening tautologies.** Two consecutive
"the X was the X" constructions closing a paragraph that has already
established the consortium's procedure and timing. The third sentence
("The cross-check had landed") is the load-bearing closer.
**Replacement:** *"The institution would respond on the institution's
clock. The procedure required the wait. The cross-check had landed."*
— replaces the two tautologies with content-bearing reframings (would
respond / required the wait).

**Line 169 — "The institution was the institution. The procedure was
the procedure. The boat had filed what the boat could file."**
Verdict: **DECORATIVE.** Exact same pattern as line 131 — two tautologies
+ a closing fact. This is now the second occurrence of the SAME triple
within 40 lines. Per ANNA-VOICE.md cap-1 motif rule, this construction
appearing twice in the same chapter is forbidden.
**Replacement:** *"The institution had its clock. The procedure had its
window. The boat had filed what the boat could file."* — replaces the
two tautologies with specific-content sentences (had its clock / had its
window) that mirror the closing fact's "had filed what" shape.

**Line 179 — "The wardroom was quiet. The hum was the hum. The boat
had ten days against the chart and the chart was the chart."**
Verdict: **DECORATIVE.** Two "X was the X" constructions in close
sequence ("hum was the hum" / "chart was the chart"). Both close
sentences in a chapter-coda paragraph that should be landing on
forward-motion (the dive imminent).
**Replacement:** *"The wardroom was quiet. The hum was on. The boat
had ten days against the chart. Sync queue empty. Relay closed.
Diving."* — replaces both tautologies with content-bearing flat
statements (was on / against the chart).

### FM2 instances

**Lines 118 (Wanjiru's institutional reasoning) — "She did not, before
she left the wardroom, name the architectural property the cross-check
was running on. She did not say *this is what the forensic substrate
is for*. She did not say *the rival platform cannot do this against us
because they don't preserve the full pre-failure timestream of every
edge device in their architecture*. She did not say *I have been
building the institutional argument against the Helvetia model since
Day 22 and the cross-check is the first instance of the argument's
evidentiary frame*."**
Verdict: **LOAD-BEARING.** The architectural-noun density here is high
but each abstract claim is specific (forensic substrate; pre-failure
timestream; Helvetia model; first instance of the argument's evidentiary
frame). The "she did not say" anaphoric structure is well past the
anaphora cap but the prose is operating in a specific literary mode
(naming what is not-said) that earns its place. Keep.

**Line 190 (chapter close paragraph) — "The forensic property the
architecture preserved had been, on the second day of the second
window, the property the cross-check had run on. The Nansen had supplied
evidence the rival's architecture could not have supplied against
itself."**
Verdict: **LOAD-BEARING.** Each architectural noun is paired with a
specific operational claim (the second day / had supplied evidence
the rival's architecture could not have supplied). The Candidate-4
shape holds.

### FM3 instances

**Line 134 (parenthetical chapter-mid close) — "(Eight kilobytes.
Which is to say: the smallest object on the boat with the largest
institutional surface area, and not, as it turned out, the largest
object I would file before the dive.)"**
Verdict: **LOAD-BEARING.** Bobiverse-style parenthetical aside; lands
on a wry observation with forward-motion ("not, as it turned out, the
largest object I would file"). Keep.

### Plan C insertion risk for Ch 11

Per integration plan, one addition: 150-250 words in the scene where
Wanjiru cross-checks Stefan's PR cycle, noting (without yet pursuing)
the firmware-update-window deviation pattern.

**FM1 risk at insertion:** MEDIUM. The chapter has 4 FM1 hits with 2
of them being the institution-was-the-institution / procedure-was-
the-procedure twin tautologies. The drafter will be tempted to add
another such pair in the new prose. **Cap the new prose at ZERO "the X
was the X" instances.**

**FM2 risk at insertion:** HIGH. The new prose names the firmware-
update-window deviation pattern, which is architectural-noun-dense by
genre. The drafter MUST ground the pattern in a specific physical
referent. Candidates: a specific consortium-archive query Wanjiru runs
(the procurement officer's release-receipt timestamp panel); a
specific window-deviation number (eight hours past the standing rule);
Wanjiru's cucu-notebook (already a recurring physical anchor in the
chapter). Per integration plan, the addition lands "in the back of the
chapter's institutional-substrate register, not at its foreground" —
that calibration is correct; this audit adds: the addition needs at
least one physical referent that the reader will see, not just one
that Wanjiru sees abstractly.

**FM3 risk at insertion:** LOW. The new prose lands mid-chapter, not
at chapter close. The drafter should NOT close the new prose paragraph
on a Wanjiru-institutional-aphorism. The new prose should close on a
forward-motion (she logs the question / she sets it aside / she
returns to the cross-check) — exactly what the integration plan
already directs.

---

## Ch 12 — *Beginning of the End — Segment 3 Dive*

**Live-grep FM1 count:** 6 hits across 228 lines.

### FM1 instances

**Line 13 — "The thermocline at one hundred and forty meters had
stratified harder than the model said it would, which is the polite way
of saying the model was wrong and the water was the water."**
Verdict: **LOAD-BEARING.** "The water was the water" lands as Anna's
wry-aside register on the model-vs-physical-reality moment. The
construction is doing irony-content work: the model is precise; the
water is itself. Keep.

**Line 97 — "(Which is the closest Priya gets to telling you something
is worth your attention - she names the next test, at the cadence at
which it will run, and the absence of further commentary is the
commentary.)"**
Verdict: **LOAD-BEARING.** Parenthetical aside; the closer ("the
absence of further commentary is the commentary") is the chapter's
canonical observation on Priya's voice and it earns the chiastic shape
because it names a specific informational property of her silence.
Keep.

**Line 129 — "She said: *the work is on the consortium's side now. The
boat is the boat.*"**
Verdict: **LOAD-BEARING.** This is Wanjiru's voice. "The boat is the
boat" in Wanjiru's mouth lands as her institutional-discipline closer
— same construction as Diego's "el barco es el barco" but in Kenyan-
English idiom (cucu's-language register). Keep.

**Line 131 — "I said: *the boat is the boat.*"**
Verdict: **LOAD-BEARING.** Anna echoes Wanjiru's closer. The echo IS
the content — the relay-operations officer and the mission director
landing the same operational frame. Keep both lines.

**Lines 195 / 197 — "I said: *the second-week resupply was at sixteen
days into a fifty-six-day mission. The tea is the tea we are now
drinking for the back forty.*" / "She said: *yes. The tea is the tea.*"**
Verdict: **LOAD-BEARING.** Anna and Sabina (presumably; verify in
context) doing tea-resupply banter at the wardroom; the construction is
the wry-register closer. Both instances earn their place — they're in
dialogue, in established character-voices. Keep.

### FM2 instances

The chapter's structural register is bridge-watch operational — running
on observation and short directive exchanges. Architectural-noun-density
is appropriately low. No FM2 flags.

### FM3 instances

**Line 208 — "The body took the tightening in before the conscious part
of me did, in the way the body had marked the difference between
Surface 1 and Surface 2 on the morning of Day 37. The tightening was
not the tightening of new-segment unease. It was the tightening of
last-leg work, which is a tightening I have carried before, on other
boats, and which has a known shape and a known cost. I noted it. I did
not soften it. The boat had ten days."**
Verdict: **MIXED. LOAD-BEARING but with one FM1 inside that wants
flagging.** The paragraph runs three "the tightening" constructions
(was not the tightening of / was the tightening of / a tightening I have
carried before). The third pulls back into specificity (last-leg work
on other boats); the first two are doing rhythmic build-up.

The closer ("the boat had ten days") is forward-motion. Keep. But:

**Replacement (tighten the build-up):** *"The body took the tightening
in before the conscious part of me did, in the way the body had marked
the difference between Surface 1 and Surface 2 on the morning of Day
37. The tightening was not new-segment unease. It was last-leg work,
which has a known shape and a known cost; I had carried it on other
boats. I noted it. I did not soften it. The boat had ten days."* —
collapses the three-fold tightening into a single named recognition
(last-leg work); preserves the closer.

### Plan C insertion risk for Ch 12

Per integration plan, one addition: ~150-250 words of a Diego micro-
scene at the polar-operations console — leather mate-cup, half-share with
Anna, the personal cadence beat, bathymetry reading. The integration
plan flags this as the highest-risk Wave-2 addition (the chapter is
already doing heavy Diego-foreshadowing work and the risk is over-
loading).

**FM1 risk at insertion:** MEDIUM-HIGH. The chapter has 6 FM1 hits, all
of which are LOAD-BEARING per audit. The construction is part of the
chapter's voice texture. The new Diego micro-scene will be tempted to
land its closer on "the cup was the cup" or "the bombilla was the
bombilla" or "the watch was the watch" — exactly the construction Anna
reaches for at moments of restraint. **Cap the new prose at ZERO "the X
was the X" instances.** The scene is short (150-250 words) and the
construction adds nothing.

**FM2 risk at insertion:** LOW. The scene names physical objects
(leather mate-cup; bombilla; bathymetry feed) and a personal cadence
(Diego's voice register). Architectural-noun-density will be naturally
low.

**FM3 risk at insertion:** EXTREME. Per Plan C anti-pattern 6 (Diego's
death is not thematically justified), the Diego micro-scene cannot
foreshadow the death. The scene is character-typical Diego doing
Diego-things. The chapter close must NOT reach for "the cup was what
Diego had brought" or "the cadence was the cadence" or any aphoristic-
mush close. Acceptable: scene closes on a specific action (Diego sets
the cup back; Diego returns to the console; the watch continues).

The integration plan flags the risk explicitly ("the beat must not
telegraph the death; it must be a beat that earns its place in the
chapter's existing structure"). This audit adds: the close of the new
micro-scene must be drafted FIRST, pinned to an action, and the rest
of the scene built back. The action-close protocol from Ch 14 applies
here in miniature.

The leather-mate-cup detail and the bombilla detail are physical
anchors that will appear in Ch 14 (Diego at the console during the
cascade and post-cascade), Ch 16 (Diego at the polar-operations console
during ascent), Ch 18 (the cup goes to María Elena per Plan C). The Ch
12 micro-scene establishes them; the later chapters carry them. The
PHYSICAL ANCHOR is the load-bearing content; the construction reflexes
are decorations.

---

# Section 3 — Wave 3 chapters (reframing)

## Ch 15 — *The Compromised Relay Holds*

**Live-grep FM1 count:** 11 hits across 398 lines. Second-highest in
target set after Ch 14.

This chapter is Wanjiru's chapter. Wanjiru's register runs deliberately
flat — she is the volume's institutional-discipline character; her voice
in dialogue is direct and short. Anna's narration on Wanjiru runs in
register-by-mimicry, which is why FM1 fires so often here.

### FM1 instances

**Line 171 — "I sat at the comm node. The proverb was not the kind of
proverb I narrated. The proverb was the kind of proverb that surfaced
when the body needed it and receded when the body had taken it in."**
Verdict: **LOAD-BEARING.** Second "proverb" sets up a specific
descriptive clause (kind that surfaced when the body needed it). Keep.

**Line 179 — "The case had been the case of a SIM-swap pattern that
had been operating against agent-side identity verification..."**
Verdict: **LOAD-BEARING.** Second "case" sets up the SIM-swap pattern
content. Keep.

**Line 185 — "She had said the documented path was the path."**
Verdict: **LOAD-BEARING.** Wanjiru's voice (recalled by Anna). The
construction in Wanjiru's mouth lands as her institutional-discipline
register. Keep.

**Line 191 — "I sat at the comm node for the duration of the
surfacing. The hum had not resumed. The body had noted. The position
was the position."**
Verdict: **DECORATIVE on closer.** "The position was the position"
closes a paragraph that has already established Anna's stillness at the
comm node twice (sat for duration / hum had not resumed / body had
noted). The closer is rhythmic-only.
**Replacement:** *"I sat at the comm node for the duration of the
surfacing. The hum had not resumed. The body had noted. I held the
position."* — replaces tautology with active verb (held).

**Line 221 (Wanjiru's voice) — "The rule has been in the consortium's
standing documentation since 2024. The rule was the rule against which
I reviewed the consortium's procurement chain at the pre-mission
verification..."**
Verdict: **LOAD-BEARING.** Wanjiru's voice; second "rule" sets up the
relative clause naming what she reviewed against the rule. Keep.

**Line 239 — "She said the sentence at the rate she said sentences
when the sentence was the sentence she had been carrying since 0323 the
previous night and had not yet said. The hum was not on. Her body was
still. Her eye contact was direct."**
Verdict: **LOAD-BEARING.** Second "sentence" sets up a specific time-
referent (since 0323 the previous night). Keep.

**Line 247 (Wanjiru's voice) — "She said: *the discipline applies to
the operator at the moment the operator most wants to skip it. I am the
operator. The moment is the moment. The discipline applies.*"**
Verdict: **LOAD-BEARING.** Wanjiru's voice; the construction "The
moment is the moment" lands as her institutional-discipline statement
(naming the operational present). The closer "The discipline applies"
is content-bearing (echoes the rule from M-PESA 2014). Keep.

**Line 249 — "I read her face. The face was the face the face was."**
Verdict: **DECORATIVE.** Triple "face" in seven words; this is the
construction collapsing into stutter. The intended content is Anna
recognizing Wanjiru's face had settled into its operational state.
**Replacement:** *"I read her face. The face had settled."* — drops
the tautology; the content (face had settled) is direct.

**Line 297 (Joel's voice via relay) — "He said: *acknowledged. Transit-
north. We will run the joint analysis on laptop-class compute at the
rate laptop-class allows. We will not pursue cause-of-deviation tonight.
The question is the question. The question is at the post-incident
review.*"**
Verdict: **LOAD-BEARING.** Joel's voice; the construction lands as his
nuclear-Navy flat-affect. Keep.

**Line 331 — "The list of *queries to run when we surface* grew. The
list at the end of Day 48 had thirteen items. The list would have
twenty-two items by Day 56 against the chart. The list would carry to
surfacing. The system would answer the items at the consortium-port
when the boat surfaced and the relay filled. The architecture would
close the gap at surfacing. The architecture had built the gap into its
specification. The gap was the gap the architecture had been honest
about."**
Verdict: **MIXED. LOAD-BEARING on most; DECORATIVE on closer.** "The
gap was the gap the architecture had been honest about" sets up
specific content (the architecture had been honest), but it's stacked
on top of two prior "architecture" sentences and reads as the
construction-as-default closer.
**Replacement:** *"The list of *queries to run when we surface* grew.
The list at the end of Day 48 had thirteen items. The list would have
twenty-two items by Day 56 against the chart. The list would carry to
surfacing. The system would answer the items at the consortium-port
when the boat surfaced and the relay filled. The architecture would
close the gap at surfacing. The architecture had built the gap into the
specification it had been honest about since the morning of Day 7."*
— collapses three architecture sentences into two; preserves all
content; specifies the day (Day 7).

**Line 333 — "The crew did not narrate the adaptation. The adaptation
was on tempo. The tempo was the tempo."**
Verdict: **DECORATIVE on closer.** "The tempo was the tempo" is the
third "X was the X" closer in close proximity (positions 297 / 331 /
333). The cap-1 motif rule is decisively exceeded.
**Replacement:** *"The crew did not narrate the adaptation. The
adaptation was on tempo. The boat made its bearing."* — replaces
tautology with physical action (boat making bearing).

**Line 363 (diary inset) — "*The architecture has now been exercised
against three threat models... The pattern is the institutional
discipline at the operator's moment. The pattern is the procedure for
the case where you most want to skip it. The pattern is the
architecture's defense against the architecture being misused.*"**
Verdict: **MIXED.** Three "The pattern is..." sentences forming anaphoric
inventory; the third repeats "the architecture" within itself ("the
architecture's defense against the architecture being misused"). This
is FM2 + FM3 overlap — architectural-noun-parade closing a diary inset
on aphoristic recognition.
**Replacement:** *"The architecture has now been exercised against
three threat models. Wanjiru did not narrate this in my cabin at
sixteen-forty-eight. She narrated the metadata question and the
institutional discipline and the carrier and the clean-mode confirmation
pass. She did not narrate the pattern that the metadata question made
when she put it next to the cascade and the post-cascade. The pattern
is the institutional discipline at the operator's moment. The pattern
is the rule Wanjiru learned in 2014 in a room two blocks off Kenyatta
Avenue. The architecture's defense against misuse is Wanjiru. That is
the recognition of tonight."* — collapses the three "The pattern is..."
sentences into two specific content-bearing claims (institutional
discipline / Wanjiru's rule from 2014); cuts the architectural-recursion
closer; lands on a specific human recognition (Wanjiru is the defense).

### FM2 instances

**Line 350 — "The architecture was at the operational tempo at reduced
capability. The hub was offline. The per-laptop held. The canonical
record was at the per-laptop. The hub had been capability, not source-
of-truth. The architecture had been built so that the hub's loss would
be capability loss, not preservation loss. The architecture was
operating at the case the architecture had been built for. The
architecture was operating as the architecture was specified."**

Verdict: **DECORATIVE noun-parade.** Eight sentences, five with "The
architecture" or "The hub" or "The per-laptop" as opener. The first
four sentences land specific content; the last four are increasingly
abstract recursions of the same claim (the architecture was running as
specified). This is the chapter-scale Candidate-3 vice.

**Replacement:** *"The architecture was at reduced capability. The hub
was offline. The per-laptop held. The canonical record was at the per-
laptop. The hub had been capability, not source-of-truth. Joel had
built it that way. He had been right."* — collapses four recursive
architecture-claims into a two-sentence specific-content close (Joel
built it that way / he had been right) that names a person (Joel) and
attributes the architectural property to a human decision.

### FM3 instances

**Line 376 — "The relay held. Wanjiru held. The architecture held what
we asked it to hold."**
Verdict: **LOAD-BEARING.** Three short specific-content sentences;
parallelism doing work; closer names the contract (what we asked it to
hold). Keep exactly — this is the chapter's load-bearing structural
close.

**Line 390 (diary inset) — "*The relay holding was the relay holding.
The architecture's defense against the architecture being misused was
Wanjiru's discipline. The two are the same thing at different
layers.*"**
Verdict: **DECORATIVE on opener; LOAD-BEARING on rest.** "The relay
holding was the relay holding" is pure tautology and adds nothing the
prior chapter-close sentence ("The relay held") has not already
established.
**Replacement:** *"*The relay held tonight because Wanjiru held. The
architecture's defense against the architecture being misused is the
operator's discipline at the operator's moment. The two are the same
thing at different layers.*"* — drops the tautology; preserves the
recognition; names the operator (Wanjiru / the operator).

**Line 392 — "*The day's account will be set down in the record. The
pattern will not. The pattern is what the reader will register from
what Wanjiru does and does not do. The pattern is what the reader will
carry.*"**
Verdict: **LOAD-BEARING.** Forward-motion close on a specific informational
claim (reader will register / reader will carry). Note: "register"
appears here as verb — register-overuse audit (ANNA-VOICE.md
anti-pattern #9) may flag. Cross-reference with that audit.

### Plan C insertion risk for Ch 15

Per integration plan, the chapter undergoes multiple reframing edits
under Wave 3. The most fragile is Edit 1 — extending Wanjiru's
three-threat-models recognition to FOUR, where the fourth is "the
threat the architecture could not protect against — the threat of the
person being mortal."

**FM1 risk at insertion:** MEDIUM. Wanjiru's interior runs heavy on
construction; the new fourth-recognition will reach.

**FM2 risk at insertion:** EXTREME. The fourth recognition is a meta-
abstract claim about what the architecture cannot do. The drafter MUST
ground the recognition in a SPECIFIC operational referent. Per the
integration plan: "the fourth recognition is named once, at low altitude,
in Wanjiru's interior; it does not become the chapter's thesis." This
audit endorses and adds: the naming must NOT be in the form *"the
fourth threat is the threat of [abstract noun]"* — that's the
Candidate-3 shape. The naming should be Wanjiru noting a specific gap.
Candidate: *"Wanjiru did not name it. She wrote, in the cucu-notebook
at the relay-operations station: 'The three threats. And the case the
three cannot reach. The compartment.' She closed the notebook."* —
names the recognition as a notebook entry; "the compartment" is the
specific concrete referent (where Diego died); no abstraction.

**FM3 risk at insertion:** EXTREME. Per integration plan: "The drafter's
check: read the chapter aloud; if the fourth-recognition addition reads
as the chapter's thesis, revise." This audit adds: the recognition must
NOT close on an aphorism about mortality, fragility, the limits of
architecture, the cost of progress, the inevitability of loss, the
nature of preservation, OR any related universal claim. The recognition
must close on a specific physical or actional referent (the notebook
closes; Wanjiru returns to the station; the hum resumes).

The integration plan also flags Edit 2 (the forensic-queries weight)
and Edit 3 (the chapter-close diary extension by ~50-80 words) as risks.
For Edit 3 specifically: the existing chapter close is *"*The boat is
at depth. The list is at thirteen. The cycle holds.*"* — exactly the
forward-motion close ANNA-VOICE.md requires. Plan C wants 50-80 words
added between this close and the current paragraph. **PAO recommendation:
do not add the extension at the chapter close.** The chapter's existing
close is the right close. Add the Diego-shadow content one paragraph
earlier (in the prior diary-inset paragraph) so the chapter still closes
on the boat-is-at-depth / list-is-at-thirteen / cycle-holds beat.

Edit 4 (Diego references becoming empty-chair references) is the lowest-
risk reframing and the audit endorses the integration plan's
calibration ("do not over-narrate the empty chair").

---

## Ch 16 — *Final Ascent*

**Live-grep FM1 count:** 16 hits across 227 lines. Highest density per
line in the target set.

The chapter is short (4,579 words) and structurally a denouement. The
construction-density is high because Anna's narration in denouement
register is reaching for closing weight at every paragraph. This is
where the cap-1 motif rule is most decisively violated.

### FM1 instances

The chapter has so many FM1 instances that listing each individually is
not productive at audit scale. The summary verdict is: **roughly 6
LOAD-BEARING (specific-content relative clauses); roughly 10
DECORATIVE (rhythmic closers that need to come down to roughly 2)**.

The DECORATIVE instances cluster at:

- **Lines 19, 27 (procedure / gap)** — "The procedure was the procedure." /
  "The gap was the gap the architecture had built into its specification."
- **Line 31 (cup / patina)** — "The cup was where the cup was." / "The
  patina was the patina."
- **Line 35 (decision / retirement)** — "The decision was the decision.
  The retirement was the retirement."
- **Line 39 (queue / handoff)** — "The queue was the queue. The handoff
  was the handoff."
- **Line 51 (pot)** — "The pot was the pot."
- **Line 61 (architecture / forensic substrate / discipline / cycle)** —
  "The architecture had held what the architecture had been specified to
  hold." (FM2 collapses into FM1.) "The architecture had run as Joel
  had specified it."
- **Line 67 (discipline / case)** — "The discipline was the discipline.
  The case was the case. The discipline had held."
- **Line 81 (card)** — "The card was the card."
- **Line 91 (wardroom)** — "The wardroom was the wardroom."
- **Line 103 (queue / list)** — "The queue was the queue."
- **Line 113 (notebook / questions)** — "The notebook was at the desk.
  The notebook was open... The questions were on the page. The questions
  were the questions."
- **Line 153 (list / gap)** — "The list was the list. The list at the
  desk was at the rate the architecture's reduced capability had built
  the gap. The gap was the gap..."
- **Line 187 (Drake / horizon)** — "The Drake was the Drake at the
  September afternoon standing sea-state. The horizon was the horizon."

This is FM1 at the chapter-default-cadence scale. The chapter cannot
hold all of these. Per cap-1 motif rule, the chapter is permitted ONE
chapter-load-bearing instance + perhaps ONE secondary instance, for a
total of two. Currently there are 16. The reduction requires roughly 14
cuts.

**General replacement strategy for Ch 16:**

The chapter's denouement function is to register reduced-capability and
the boat's approach to Punta Arenas through Anna's narration of the
crew at routine tempo + Anna at the desk doing the writing. The
construction has become the chapter's default register for everything
that "just is." The replacement strategy: replace each tautology with
either (a) a specific physical detail; (b) a verb (held / continued /
ran / went on); (c) a forward-motion transition.

**Worked examples:**

- Line 31 "The cup was where the cup was. Diego had drunk from it..."
  → "The cup sat at the position it had been at since Belgrano-II.
  Diego had drunk from it..." — replaces tautology with naming the
  position-origin.
- Line 31 "The patina was the patina."
  → "The patina was old. The bombilla had not been polished." —
  replaces with two specific physical statements.
- Line 35 "The decision was the decision. The retirement was the
  retirement."
  → "He had decided. He was going home." — replaces with action.
- Line 39 "The queue was the queue. The handoff was the handoff."
  → "Diego had readied the queue. Hiroshi would take it forward." —
  replaces with attribution.
- Line 51 "The pot was the pot."
  → "The pot was Sabina's last reserve before the Punta Arenas
  resupply." — replaces tautology with the content beat already
  established in the sentence before (which then becomes redundant
  and can be cut).
- Line 67 "The discipline was the discipline. The case was the case.
  The discipline had held."
  → "The discipline had held. The case had been the case Joel had
  built it for." — collapses three to two; second sentence carries the
  content via relative clause.
- Line 81 "The card was the card."
  → "The card was old; I did not name it aloud." — replaces with
  specific (old) and forward-motion (did not name).
- Line 91 "The wardroom was the wardroom."
  → "I sat in the empty wardroom for the duration of my tea." —
  replaces with action + sensory (empty).
- Line 113 "The questions were on the page. The questions were the
  questions."
  → "The questions were on the page. I did not read them." — replaces
  with action.
- Line 187 "The Drake was the Drake at the September afternoon
  standing sea-state. The horizon was the horizon."
  → "The Drake at the September afternoon ran its standing sea-state.
  The horizon ran north." — replaces both with action verbs (ran).

### FM2 instances

**Line 67 — "The architecture's correctness depended on Joel having
handled the engineering at the rate he had handled it. He had spent
twenty-five years on it - the Navy's nuclear-reactor-supervision
discipline against the back fourteen years of distributed-systems work
against the four years of the Sunfish project's pre-mission rewrite
cycle."**
Verdict: **LOAD-BEARING.** Architectural claim grounded in specific
biography (twenty-five years / Navy / fourteen years distributed /
four years pre-mission). The Candidate-4 shape. Keep.

**Line 69 — Joel-reading-log paragraph — "The reading was Joel's
reading... The reading was not a celebration. The reading was the
reading. Joel had carried the Navy's bearing from the *Sunfish* SSN-649
across the back two and a half decades..."**
Verdict: **DECORATIVE on "The reading was the reading."** The
construction in the middle of a paragraph that has otherwise been
naming the reading specifically (Joel's reading / not a celebration /
the engineer's reading) collapses into tautology.
**Replacement:** *"The reading was Joel's reading... The reading was
not a celebration. Joel was reading what he had built. Joel had carried
the Navy's bearing from the *Sunfish* SSN-649 across the back two and
a half decades..."* — drops tautology; preserves content.

### FM3 instances

**Line 161 (Uzbek-melon paragraph close) — "I had taken in the taste.
I had taken in the geography. I had returned to the work."**
Verdict: **LOAD-BEARING.** Three short flat-affect sentences; closer is
forward-motion (returned to the work). Keep.

**Line 187 — "I went to the rail. I looked west. The Drake was the
Drake at the September afternoon standing sea-state. The horizon was
the horizon. The Punta Arenas approach was in sight at the standing
transit rate. Two days. The boat would dock against the consortium's
standing handshake at 0441 local on Mission Day 56."**
Verdict: **MIXED. LOAD-BEARING on forward-motion (Two days / The boat
would dock) but DECORATIVE on the construction-density mid-paragraph.**
**Replacement (per FM1 fix at line 187):** *"I went to the rail. I
looked west. The Drake at the September afternoon ran its standing
sea-state. The horizon ran north. The Punta Arenas approach was in
sight at the standing transit rate. Two days. The boat would dock
against the consortium's standing handshake at 0441 local on Mission
Day 56."* — keep the forward-motion close; replace the
construction-density.

### Plan C insertion risk for Ch 16

Per integration plan, the chapter undergoes Wave-3 reframing — Edit 1
(reference changes from Diego-grounded to Diego-absent), Edit 2 (queries
list expanded with bereavement-related items), Edit 3 (chapter-close
extended by 150-250 words at Anna's interior).

**FM1 risk at insertion:** EXTREME — but the primary risk is the
EXISTING prose, not the new prose. The Wave-3 reference changes have
to be applied to a chapter whose default cadence is FM1. The drafter
will be reframing sentences like "Diego had the polar-operations
console" (Plan C: the polar-operations console was at standing position;
the chair was empty) and the reframings will FREQUENTLY land back in
the construction ("the chair was the chair" / "the position was the
position" / "the empty was the empty"). **The Wave-3 reframing pass on
Ch 16 must be paired with a comprehensive FM1 reduction pass.** This is
not just a reference-change exercise; it is a register-discipline
exercise.

**Volume-wide priority:** Ch 16 is the chapter where the FM1 reduction
work is most urgent and most extensive. It should be authored as a
single combined pass (reframing + FM1-reduction) rather than as two
separate passes.

**FM2 risk at insertion:** MEDIUM. The queries-list expansion under
Edit 2 will name institutional items (María Elena notification; IAA
bereavement; consortium-logistics-van timing; Diego's Filchner-Ronne
paper; the chief-scientist-billet; the polar-operations-billet). The
drafter should NOT list these as a parade; the integration plan's
existing directive ("the list is what it is — a paper artifact at the
cabin desk, growing at the rate Anna can write items on it") is correct.
This audit endorses.

**FM3 risk at insertion:** HIGH. The chapter-close extension under
Edit 3 (~150-250 words of Anna's interior at low altitude) is in
ANNA-VOICE.md's most-aphoristic-risk zone. Per the integration plan:
"the naming is operational: María Elena's notification will happen at
the Punta Arenas surface handshake; the IAA's institutional bereavement
procedures will run at the institutional level; the boat must make
Punta Arenas at the operational tempo; the work of writing the staff
history continues. The closing image of the chapter is Anna at the
desk having added items to the list and closing the per-laptop for the
night."

This audit endorses the directive and adds: the close MUST land on the
per-laptop-closing action (forward-motion close per ANNA-VOICE.md). The
drafter must NOT close on Anna's interior reflection on what the next
four days will require. The interior reflection IS the body of the
extension; the close IS the action.

---

# Section 4 — Summary punch list

## Per-chapter sizing + FM1 reduction count

| Chapter | FM1 hits | LOAD-BEARING | DECORATIVE / BORDERLINE | Lines flagged | Sizing | Volume priority |
|---|---|---|---|---|---|---|
| Ch 14 | 17 | 8 | 9 | 51, 143, 159, 217 (2nd hit), 277/487, 443, 465, 469, 477 | **L** | **1 (Wave 1 priority)** |
| Ch 17 | 3 | 2 | 1 | 179 | **S** | 4 |
| Ch 18 | 11 | 6 | 5 | 140, 174, 272, 315, 341, 381 | **L (with CIC ruling)** | **2 (Wave 1 priority + CIC override flag)** |
| Ch 01 | 1 | 1 | 0 | (no cuts; OMIT Edit 2 insert) | **S** | 7 |
| Ch 07 | 12 | 6 | 6 | 25, 51 (2nd), 61 (1 of 3), 69, 139-143, 147, 211, 215 | **M** | 5 |
| Ch 10 | 3 | 3 | 0 (existing) | (line 175 close revise) | **S** | 8 |
| Ch 11 | 4 | 0 | 4 | 57, 131, 169, 179 | **S-M** | 6 |
| Ch 12 | 6 | 6 | 0 (existing) | (line 208 build-up tighten) | **S** | 9 |
| Ch 15 | 11 | 6 | 5 | 191, 249, 331 (closer), 333, 350 (FM2 parade), 363, 390 | **M-L** | **3 (heaviest Wave 3)** |
| Ch 16 | 16 | 2-3 | 13-14 | (chapter-wide cadence reduction) | **L (combined with Wave 3 reframing)** | **2/3 tier (paired with reframing pass)** |

## Volume-wide priority order

1. **Ch 14** — Wave 1 load-bearing rewrite + 8-9 FM1 cuts + the diary-
   inset Diego paragraph FM3 protection (compose-close-first). Highest
   risk, highest volume-significance. The chapter that determines whether
   Plan C lands.

2. **Ch 18** — Wave 1 + the FM3 ruling required from CIC on line 272 and
   line 341 (the *"Diego had preserved Diego"* and *"He preserved
   himself"* passages that the integration plan marks PRESERVE EXACTLY
   but this audit flags as reproducing the back-cover Candidate-3 vice).
   Cannot proceed without CIC ruling. Second-highest priority because
   the chapter is the volume's closing artifact.

3. **Ch 16** — Wave 3 reframing must be paired with a comprehensive FM1
   reduction. 13-14 instances need cutting. Cannot ship Plan C with the
   chapter's current FM1-as-default-cadence.

4. **Ch 15** — Wave 3 reframing + 5 FM1 cuts + the four-threat-models
   recognition risk (FM2 + FM3) at insertion. The diary inset at line
   388-394 needs the architecture-recursion close cut.

5. **Ch 17** — Wave 1 + 1 FM1 cut + the Joel admission paragraph's
   FM3-extreme-risk site (compose-close-first protocol; *"The cost is
   in the compartment."* preserved exactly; no follow-up Anna paragraph).

6. **Ch 07** — Wave 2 + 6 FM1 cuts. The chapter has 12 hits because
   Joel's voice runs flat-affect; the cuts focus on cumulative density
   (3-stacks and 5-stacks). The Plan C addition needs its own ZERO-
   tautology discipline.

7. **Ch 11** — Wave 2 + 4 FM1 cuts (two pairs of "institution was the
   institution / procedure was the procedure" within 40 lines — cap-1
   motif rule violated). Plan C addition is ZERO-tautology.

8. **Ch 01** — Wave 2 + OMIT of Plan C Edit 2 (the *"I helped where I
   could help. I did not always know which moments would be the ones I
   could not."* aphoristic-close violation per ANNA-VOICE.md anti-pattern
   #1). Edit 1 lands cleanly; Edit 2 is the optional addition the
   integration plan flagged and this audit confirms should be cut.

9. **Ch 10** — Wave 2 + 1 FM3 close revise at line 175. The chapter is
   strong in its executed state; the Plan C addition needs FM3 discipline
   at the close (compose-close-first; pin to present-tense diary register;
   no counterfactual aphorism).

10. **Ch 12** — Wave 2 + line 208 build-up tightening. The chapter is
    the cleanest of the heavy-Diego-foreshadowing chapters. The Plan C
    Diego micro-scene addition needs ZERO-tautology discipline.

## CIC ruling required

**Item 1:** Ch 18 line 272 — *"Diego had preserved Diego"* closing
sentence. Integration plan §18 Item 6 marks PRESERVE EXACTLY. Audit
flags as reproducing back-cover Candidate-3 vice. PAO recommends the
replacement *"He made the rest of it himself."* Ruling needed.

**Item 2:** Ch 18 line 341 — diary-inset Diego paragraph. Integration
plan §18 Item 8 prescribes target text containing *"He preserved
himself in the moment his body chose to go to the failure point"*. Audit
flags as Plan C anti-pattern 6 violation (Diego's death thematically
justified). PAO recommends the replacement that closes on *"The
architecture has nothing to say about that."* Ruling needed.

**Item 3:** Ch 01 Edit 2 — *"I helped where I could help. I did not
always know which moments would be the ones I could not."* Integration
plan flags as optional with PAO read-aloud required. Audit recommends
OMIT (aphoristic-close violation per ANNA-VOICE.md anti-pattern #1).
If CIC overrides OMIT, audit provides a replacement landing on
forward-motion rather than recursive subordinate clause.

## Cross-volume calibration check

The Candidate 4 back cover's specific moves that this audit applied as
rubric:

1. **Concrete things the architecture caught**, not "what the architecture
   was built to catch": *the pre-failure timestream / the
   firmware-update signature / the vendor's name on the procurement
   paperwork*. — Applied throughout. Replacements favor specific named
   artifacts over recursive architecture-of-architecture claims.

2. **Joel's role physical**, not abstract: *pushed me aside at the top
   of the ladder before either of us had cognitively decided he was
   going down*. — Applied at Ch 14 (the push beat survives), Ch 17
   (Joel's admission must land on physical fact "the cost is in the
   compartment" not on aphoristic statement of regret).

3. **Aphoristic close cut**: Candidate 3's *"He preserved himself, in
   the way one preserves oneself by being the person one is"* — exact
   move flagged at Ch 18 lines 272 and 341 above.

4. **Dual-reader frame at load-bearing position**: *Only one of those
   documents serves the architecture. The other serves Diego.* —
   Applied at Ch 18 close. The audit endorses the existing chapter
   close beat that lands the dual-reader frame at the diary inset
   (the architecture serves the consortium; the letter serves María
   Elena). The construction must survive Plan C unchanged.

5. **One-word structural pivot**: Candidate 4's *His.* — Joel's
   admission landing as a single-word answer to a structural question.
   Applied at Ch 17 — Joel's *"The cost is in the compartment."* is the
   structural-pivot landing. The drafter must preserve the sentence
   exactly as the integration plan specifies; no softening, no
   follow-up.

## Drafter discipline summary (cross-chapter)

Three rules apply to every Plan C insertion site across the 10 chapters:

1. **Compose the close FIRST.** Pin every insertion-site paragraph's
   final sentence to either a physical referent, an action, a forward-
   motion transition, or a specific question — BEFORE composing the
   body of the paragraph. This is the single best defense against FM3
   aphoristic-mush at insertion.

2. **Cap "the X was the X" constructions per insertion site.** Cascade-
   core rewrite (Ch 14): two instances total, non-adjacent. All other
   insertion sites (Ch 17 admission paragraph, Ch 18 replacement scenes,
   Ch 01 Edit 1, Ch 07 addition, Ch 10 addition, Ch 11 addition, Ch 12
   addition): ZERO instances. The construction is the chapter's existing
   voice signature; the new prose must not amplify it.

3. **Pair every architectural noun with a physical referent.** Per
   Candidate-4 rubric, abstract claims must be anchored to specific
   things the reader can see. The drafter should not write more than
   two consecutive architectural-noun-sentences without dropping into
   a physical or sensory anchor.

End of audit.

— PAO subagent (dispatched), 2026-05-21T13:30Z (Opus 4.7, xhigh)
