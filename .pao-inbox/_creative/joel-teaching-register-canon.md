# Joel Reyes Teaching Register - Canon Note

**Date:** 2026-05-07
**Author:** PAO (consolidating CO directive 2026-05-07)
**Status:** Adopted as craft canon. Pilot on Ch 7. Conditional scale.
**Related:** `.pao-inbox/_creative/character-sheets/joel-reyes-principal-architect.md`

---

## What this is

A craft strategy for handling technical-concept exposition in Vol 2 by deepening Joel's existing teaching register, instead of:

- Adding a new boat-resident character (rejected: high craft cost, manifest is locked canon, bends Anna's voice)
- Relying on workshop entries + audio glossary preprocessor + chapter-lightening pass alone (sufficient for ~90% of cases, but doesn't naturalize explanation in the prose)

Joel's teaching register is **already established canon** (Ch 7 *Joel's Sunfish* disclosure, Ch 13 schema-migration scene with Priya, Ch 17 *honest engineering register*). Extending it deepens an existing thread rather than installing a new one. The technique relieves Anna's POV monopoly without breaking the staff-history conceit, because Anna's first-person POV can **register** Joel's teaching rather than narrate it directly.

---

## Strategic posture: pilot first, scale on signal

**v1 deployment:**
- Pilot the technique on **Ch 7 (*Joel's Sunfish*)** as the most natural fit.
- Hold the rest as backup.

**Scale trigger:** initial-reader feedback identifies confusing technical concepts. Don't aggressively extend the technique across multiple chapters preemptively - the audio glossary preprocessor + workshop entries should solve the listener problem on their own. The Joel teaching register extension is a craft upgrade reserved for genuine gaps.

**Reader-feedback signals that would trigger broader deployment:**
- Beta-reader comments noting confusion at specific technical terms or scenes
- Audiobook listen-test feedback (e.g., "I lost the thread at chapter 9")
- Editorial review beacons in `.pao-inbox/co-review-*.md` flagging passages where readers stalled
- Critic / blurb feedback during pre-publication phase

If any of these surface, return to this note and consult the chapter-mapping table (below) to decide which chapters get the extension.

---

## Joel's teaching register - voice characteristics

When the chapter-drafter writes Joel teaching, Joel's voice is:

1. **Calmer than Anna's.** Anna is compressed-deliberate; Joel is methodical-deliberate. Joel pauses where Anna doesn't; he confirms received understanding before moving on; he doesn't accelerate.

2. **Architect-register.** Joel names trade-offs explicitly. He says *"this gives us X but costs us Y"*, not *"this is the right answer."* He owns the decisions his architecture made and the ones it didn't make.

3. **Honest about absence.** Joel has been honest about *what his system has and what his system does not have* for fifteen years before he wrote the paper (per Ch 7 / Ch 17 canon). He volunteers what the architecture cannot do, what it explicitly defers to humans, and where it has known limitations. He doesn't oversell.

4. **Uses concrete analogies.** Joel reaches for everyday images when explaining (the way Anna does NOT - she names directly). His teaching analogies are the load-bearing element; without them, the explanation lands as definition rather than understanding.

5. **Pedagogically patient.** Joel waits. He gives the listener time to assemble the picture before he layers the next piece. This is a register Anna's POV can register but cannot produce on her own - it's specifically Joel's tempo.

6. **Personal-without-being-confessional.** Joel's teaching frequently touches on what he learned, what he got wrong, what he changed his mind about. He does not narrate emotion; he reports decisions and their reasons. The personal content lands as engineering-history, not as feeling.

7. **Filipino-American family register at the margins.** Joel's character sheet (`character-sheets/joel-reyes-principal-architect.md`) establishes a Filipino-American family background that surfaces in tone - periodically he reaches for an analogy from his upbringing or his family's professional history. Use sparingly; not in every teaching beat.

---

## Five techniques for landing Joel's teaching register

The chapter-drafter agent should pick the technique that fits the scene's existing register, not impose one.

### Technique 1 - Reported teaching (Anna observes Joel teaching someone else)

Anna's first-person POV registers Joel teaching another character. Joel's dialogue lands inside Anna's register without bending her voice.

**Example shape:**
> *Joel was at the second workstation, a metre to Priya's right; the screen between them was at the schema-evolution corpus's annotated view. He was naming things. He named the lens layer first. He named the upcaster ordering against the partition. He named the field-map row Priya had circled in red - and then he named what the row would have to absorb if the migration ran without the four-pass cycle. He did not name what would happen if it didn't. Priya named that.*

**Cost:** lowest. Works in any scene Joel + another character are in frame.

### Technique 2 - Direct in-scene briefing

Joel speaks in dialogue; Anna's interior registers tempo, choice of analogy, what Joel elides. Joel can carry technical gloss directly because he's *the architect*; teaching is in-character for him.

**Example shape:**
> Joel said: *the gossip protocol does not promise that everyone agrees right now. It promises that everyone will agree, eventually, if the relays keep talking. The architecture made a choice - fast and eventual, instead of slow and immediate. The choice is wrong for some applications. It is right for ours.*
>
> I logged the architect-register he had just used: *the choice is wrong for some applications.* He had not said *the choice is right.* He had said *the choice is right for ours.* The distinction was the architecture's distinction.

**Cost:** moderate. Requires Joel's dialogue to be in-character; Anna's POV does the registration work after.

### Technique 3 - Quoted text from Joel's paper or technical writing

Anna read Joel's paper three times before recruiting him; the paper is canon and quotable. Direct quotes from Joel's writing land his teaching voice in the prose without requiring scene presence.

**Example shape:**
> *He had written it like this: "A schema migration is an act of refusal of permanent type - a system that cannot evolve its data shape is a system that cannot survive its own success." I had read this sentence on a tablet in Saint Petersburg in November; I had read it again at four in the morning a week before he confirmed; I read it now in the way you read a sentence you have read enough times that it is no longer a sentence in the ordinary sense, but a piece of architecture in your head.*

**Cost:** low. Works in any chapter; doesn't require Joel in scene. Best for register-establishing moments.

### Technique 4 - Recruitment-call flashback

Anna had multiple video calls with Joel before the voyage (Ch 2 establishes this). A brief flashback to a pre-mission call where Joel walked Anna through a piece of the architecture dramatizes his teaching register at concentration without changing manifest or scene.

**Example shape:**
> *On the second of the three pre-mission calls - the one in February, four in the morning Manila time, the one where he had brought up the bunk laptop without naming it - Joel had walked me through the lease-layer reconciliation under partition. He had drawn it on his whiteboard for me. The whiteboard had been visible on the call. The diagram had been four arrows and a box. The box had been labeled "the boat." The arrows had been labeled by what they would and would not do when the boat was unreachable.*

**Cost:** moderate. New scene material; requires careful integration with Ch 2 canon; high explanatory bandwidth per word.

### Technique 5 - Joel's filed audit-log entries

The architecture has signed audit-log entries; Joel files some. Anna reading them in-scene lets Joel's voice land directly without dialogue.

**Example shape:**
> *The audit log carried Joel's signed entry from the morning of Day 39, filed before the dive: "Migration window for the auxiliary-salinity stream's data-class reclassification scheduled at Mission Day 44, 0600 local. Four-pass cycle authorized; rollback path verified; field-map drafted. Conditional preservation under partition holds within the architecture's specification. - J. Reyes, Principal Architect."*

**Cost:** lowest. Limited bandwidth (institutional voice is constrained); useful in chapters where Joel isn't physically present.

---

## Chapter mapping - where Joel's teaching register fits

| Chapter | Existing Joel beat | Extension opportunity | Technique |
|---|---|---|---|
| **Ch 1** *Departure* | Equipment review 10:28-10:35; bunk-laptop disclosure | Joel walks Anna through compute envelope, keys-vs-consortium-keys distinction | T2 direct briefing |
| **Ch 2** *Recruitment Interview* | Recruitment call canonical | Add a teaching beat about a specific architectural property | T4 flashback or T2 current-scene |
| **Ch 7** *Joel's Sunfish* ⭐ **PILOT** | Disclosure scene; Joel teaching is already in spirit | Deepen with Joel showing a specific mechanism on the bunk laptop | T2 direct briefing + T3 paper quotes |
| **Ch 9** *Sync Daemon Under Drift* | Wanjiru triage scene | Joel briefing Wanjiru on a P0/P4 trade-off | T1 reported teaching |
| **Ch 13** *Schema That Should Not Migrate* | Joel + Priya 4 hours in engineering | Already teaching; deepen Anna's POV registration of the exchange | T1 reported teaching |
| **Ch 17** *Transit North* | Joel's honest engineering register established | Deepen with a specific architectural reflection | T2 direct briefing |

Chapters that should NOT take Joel-teaching extensions:

- **Ch 14** *The Crossing* - leak event / cascade; action register; teaching would slow the crisis
- **Ch 18** *Punta Arenas Surfacing* - ending; docking register; teaching unfits the closing tempo
- **Ch 5** *Day Twenty Realization* - Anna's interior chapter; Joel's voice would dilute the inward register
- **Ch 6, 11** *Forsaken Reveal* chapters - Wanjiru-and-press-cycle-driven; Joel's teaching would not fit
- **Ch 15** *Compromised Relay Holds* - Wanjiru's forensic register; Joel's teaching would not fit

---

## Risks to watch in the prose work

1. **Lecture-bot risk.** Joel teaches because he's *briefing*, *debugging*, or *advising* - never because the reader needs to know. The in-scene reason has to be earned. If the chapter-drafter cannot name an in-story reason for the teaching beat, the beat does not belong.

2. **Voice drift risk.** Joel's teaching register is HIS voice (calmer, methodical, architect-y, names trade-offs explicitly), not Anna's voice with Joel's mouth. The chapter-drafter must honor this distinction. When in doubt, read the existing Ch 7 disclosure scene aloud and match Joel's tempo there.

3. **Density risk.** Anna's compressed-deliberate register can absorb only so much teaching before the chapter starts feeling like a tutorial. Joel-teaching beats should be incidents inside Anna's chapter, not the chapter's center of gravity. Rule of thumb: no more than one substantial Joel-teaching beat per chapter.

4. **Pacing risk.** Each Joel-teaching extension adds words. Vol 2's chapter-budget already runs over target on word-count for several chapters (per `CHAPTER-OUTLINE.md` table at lines 462-470). Trimming elsewhere may be necessary if a teaching extension lands.

5. **Coverage risk.** Joel's teaching register can naturally absorb terms that are core to *his* architecture (sync daemon, schema migration, key envelope, gossip protocol, CRDT, lease layer, partition tolerance). It cannot naturally absorb terms that aren't his (operational artifacts like surface window, mission terms like MERIDIAN-7, medical terms, navigation terms). Match the technique to the term.

---

## Pilot scope: Ch 7 *Joel's Sunfish*

**Why Ch 7:** the chapter is structured around Joel's bunk-laptop disclosure to Anna at 22:30 in the wardroom on Day 22. The teaching register is *inherent to the scene* - Joel is showing Anna the architecture he has spent fifteen years building, on a personal laptop he was prepared to lose, because he believed she would not punish him for keeping his work-of-conscience separate from the consortium's chain. The chapter is already a teaching scene in spirit.

**Pilot brief for chapter-drafter:**

1. **Read Ch 7 in its current state.** Identify the existing teaching beats (where Joel speaks; where Anna registers what Joel is showing).
2. **Read the Sunfish Submarine Security & Key Management canon** at `.pao-inbox/_creative/sunfish-submarine-security-canon.md`. Joel's pedagogical content for Ch 7 should specifically lean into:
   - **§1 (Identity Model)** - the three identity types (crew + platform + service); why they're distinct; why a service key's compromise ≠ the platform's compromise. Concrete and useful - Anna handed three credential modules to Wanjiru in Ch 1; Joel can explain *why* there were three, not one.
   - **§2 (Key Hierarchy)** - root CA on shore, intermediate CAs covering fleets, the boat trusts the intermediate; the unified trust root chains everything on board. The hierarchy itself is teachable in plain language.
   - **§4 (Two-Person Rule and MFA)** - TPI for high-impact operations; the dual-control ceremony Wanjiru and Anna already enacted in Ch 1 *is* TPI. Joel can name the principle Anna already practiced. Pays off the Ch 13 schema migration scene (also TPI) with retroactive clarity.
   - **NOT §7 (distress signaling and false codes)** - narrative-restraint applies; do not surface this mechanism in Vol 2 prose, including in Joel's teaching. The canon doc explains why.
3. **Add ONE substantive teaching beat** using Technique 2 (direct in-scene briefing). The beat should:
   - Land at a natural pause in the existing wardroom scene (Day 22 22:30 disclosure context)
   - Cover §1 / §2 / §4 content per the canon - pick the angle that fits the scene's existing register
   - Use Joel's voice (calmer, methodical, names trade-offs, uses an analogy)
   - End with Anna's POV registering what Joel said and what he didn't say
4. **Optionally add ONE Technique 3 paper-quote** elsewhere in the chapter for register-establishment. The quote can reference any of the architectural principles in the canon (§1-§6, §8-§9). Skip §7.
5. **Keep the chapter within ±10% of word-count target.** If the addition pushes over, trim elsewhere. The chapter-drafter knows the existing prose; PAO does not direct cuts.

**Validation criteria after pilot:**

- Read aloud - does Joel's voice sound distinct from Anna's narrator voice?
- Cross-check against `character-sheets/joel-reyes-principal-architect.md` - does the addition honor Joel's character?
- Spot-check audiobook substitutions - does the audio glossary preprocessor handle the new prose cleanly (no abbreviation hazards, no poison chunks)?
- Word-count check - chapter still within target range?

If the pilot lands and CO approves, hold the technique in reserve. Deploy further only on reader-feedback signal per "Strategic posture" section above.

---

## Bonus craft observation - Vol 3 runway

If Joel's teaching register is canonized in Vol 2 prose, **a future volume with Joel as POV character (or alternating Anna/Joel POV) becomes credible** - readers will already know how Joel sounds at length. This is a strategic option for Vol 3 (or whichever future volume), not a constraint or commitment.

---

## How to invoke this canon

When a chapter-drafter / Yeoman / voice-pass agent is working on a Vol 2 chapter and the question "should this technical concept be explained, and how?" arises:

1. Check this note for the chapter's row in the mapping table.
2. If the chapter is approved for extension AND the trigger has fired (reader feedback or pilot phase), pick the technique that fits the scene.
3. Honor the voice characteristics; honor the risks.
4. After the addition, re-validate against this note's pilot-validation criteria.

The chapter-drafter agent should treat this note as primary craft context for any Vol 2 prose work involving Joel.

---

**Filed by PAO. Pilot ready for chapter-drafter when CO greenlights Ch 7 work.**
