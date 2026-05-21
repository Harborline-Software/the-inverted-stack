---
name: crew-log-style-entry
description: Generates concise para-military crew log entries - disciplined, first-person, mission-anchored - from a brief situation description. Use whenever a passage needs the register of a duty log, a staff history fragment, a captain's log, or a restrained personal reflection inside a professional command structure. Especially relevant to Vol 2 (Anna Yusupova's first-person mission narrative of Sunfish-1) where chapters routinely contain staff-history-fragment passages or in-prose log artifacts. Three tone biases - formal_duty_log (objective, procedural), personal_reflection (interior, restrained), balanced (mixed) - let the same skill produce duty entries, mission-log fragments inside character interior, or quoted log-excerpts within scene prose. Output is 80-200 words, expository, narrative-not-dialogue, with a clear log-header opening line.
---

# Crew Log Style Entry - Generator for Mission Log / Staff History Voice

## Why this skill exists

Vol 2 of *The Inverted Stack* is, in-universe, Anna Yusupova's staff history of the Sunfish-1 mission. The first-person register that carries the book's audiobook listenability is the **disciplined, command-mature, log-style voice** - a captain or senior officer narrating events with restraint, technical precision, and ethical weight, but never melodrama.

That register also appears in shorter forms throughout the work:

- The Anna mission-log fragment voice exemplar at `.pao-inbox/_creative/oss-architects-voices/02-anna-mission-log-fragment.md`
- The Vol 1 closing chapter `vol-1/closing/the-crossing.md`
- Inset log-quote artifacts inside other chapters (when a character reads a prior log entry, or when a chapter renders an excerpt of a duty record)
- Future Book 1 chapters where Joel keeps a Navy-style engineer's log; where the consortium ports record official communications; where Wanjiru maintains relay-operations records

Reach for this skill whenever generating any of those.

## When to consult this skill

- Writing a fresh log entry, mission-log fragment, or staff-history passage for any character.
- Generating an inset log artifact inside a scene (a character reading a log entry; a flashback rendered through a recovered log; a regulatory record quoted in prose).
- Drafting **any** Vol 2 passage that needs the captain-narrating-after-the-fact register - which is most of Anna's first-person prose.
- Producing voice-reference samples for non-Anna characters (Joel, Priya, Wanjiru) whose logs would carry their own variant of the same register.
- Building examples for downstream review or for voice-pack auditioning.

## When to skip this skill

- **Live dialogue scenes.** This skill produces narration, not speech. For dialogue exchanges, draft directly from the chapter outline.
- **Pure technical specification.** Part III of Vol 1 is specification voice - clarity beats cadence; logs add register that gets in the way.
- **Voice that explicitly is *not* command/log.** Sabina's bid-disaster King-style victim register, for example, deliberately abandons command discipline; a crew-log voice would erase the failure-mode the chapter exists to demonstrate.

## Inputs

The skill's behavior shifts based on five inputs, only one of which is required.

| Input | Required | Default | Notes |
|---|---|---|---|
| `timestamp` | no | (omit) | A timestamp string for the header - e.g., `Crew log, 2045-06-18T14:32Z.` Mission-day form is also fine: `Crew log, Mission Day 14, 0617 local.` Omit and the header reads simply `Crew log.` |
| `author_role` | no | `Crewmember` | The author's position. Use specific roles wherever possible: `Mission Director`, `Principal Architect`, `Lead Instrumentation Engineer`, `Relay Operations Officer`, `Polar Operations Specialist`, `Medical Officer`. |
| `unit_name` | no | `Unit Alpha` | Ship, mission, or operation name. For Vol 2: `Sunfish-1`, or implicit when the context is established. |
| `situation_summary` | **yes** | - | Brief prose description of what happened, current mission status, key conflict, and any decisions/actions/dilemmas in play. The skill expands this into a log entry - the input does not need to be log-shaped already. |
| `tone_bias` | no | `balanced` | One of `balanced`, `formal_duty_log`, `personal_reflection`. See § Tone biases below. |

## Output shape

Always:

- **First-person**, past tense (or present-perfect for ongoing situations) - never third-person, never future-conditional speculation.
- **Opens with a log header line.** Examples:
  - `Crew log, Mission Day 14, 0617 local.`
  - `Crew log, 2026-09-21T23:42Z.`
  - `Mission log fragment - Anna Yusupova, Mission Director, Sunfish-1.`
  - `Crew log.` (no timestamp provided)
- **80-200 words total.** Concise. Every sentence load-bearing. No throat-clearing, no academic scaffolding (`I would like to note that…`, `It bears mentioning that…`).
- **Narrative, not dialogue.** Indirect speech where someone speaks (`The watch officer reported…`), not quoted exchanges.
- **Mission-anchored.** Every passage either describes mission state, action taken, decision rendered, or observation logged. Even reflective passages stay mission-anchored.
- **Disciplined.** No melodrama. Restraint is the default register; emotion lands harder when it is named at minimum altitude.

## Tone biases

The same situation can produce three meaningfully different entries depending on bias.

### `formal_duty_log` - objective and procedural

- Lead with facts, times, names, instruments, decisions.
- Voice is impersonal-professional: the *logging officer* speaks, not the *person* of that officer.
- Emotion is allowed only as an objective observation about another crew member or a situation, never about the author's interior.
- Closes on next-step or carryover for the next watch's record.

**Example header + opening:**
> Crew log, Mission Day 14, 0617 local. Routine watch. The sensor array's primary spoke went into deferred-maintenance state at 0319 per scheduled procedure. Backup spoke held without intervention. No mission-impact items to forward.

### `personal_reflection` - restrained interior

- Lead with the duty-context anchor (a couple sentences locating the event).
- Add 1-3 sentences of interior - what the author noticed in themselves, what they are sitting with, what they have not yet resolved.
- Reflection stays within the chain of command: doubts about a decision are recorded as *the question I am holding*, not as criticism of a superior.
- Closes on the unresolved or the next-action, not on emotional climax.

**Example header + opening:**
> Mission log, Day 14. The query I sent to the local store came back without ambiguity. I had expected ambiguity - there is none here, because nothing else is reachable. I am writing this down because I want to be honest about the moment I understood what we are operating inside.

### `balanced` - default mixed

- Two sentences of duty-context.
- Two sentences of action or decision.
- One or two sentences of restrained reflection or unresolved consideration.
- Closes on the carryover: what the next watch needs to know, or what remains in the author's holding queue.

## Composition checklist

Before returning a generated entry, verify:

1. **First-person, throughout.** No "the captain" when "I" was meant.
2. **Header line is the first line.** No prose before it.
3. **Total word count between 80 and 200.** Count the words; cut to fit.
4. **Author role appears once** in the entry - either in the header, the opening sentence, or as part of a signature-style closing. Not all three.
5. **Unit name appears once** when given - same rule.
6. **No academic scaffolding.** No `as noted earlier`, `it should be observed`, `for the record I would offer`. Logs do not need to apologize for being logs.
7. **No anti-AI-tells** - consult `.Codex/skills/anti-ai-tells/SKILL.md` if uncertain. (No `delve`, `tapestry`, `underscore`, no significance-puffery, no signposting.)
8. **No genre clichés** - no "stardate", no "captain's log, supplemental" (unless the unit_name explicitly establishes a sci-fi register), no breathless scene-of-action narration. The log is a record, not a screenplay.
9. **Does not break character** by referencing the author as an AI, model, tool, or content generator.

## Worked examples

### Example 1 - formal_duty_log

**Input:**
- `timestamp`: `2026-09-21T23:42Z`
- `author_role`: `Mission Director`
- `unit_name`: `Sunfish-1`
- `situation_summary`: After 7 days submerged, the relay layer is dormant as designed; the local store handled a provenance query for a colleague's prior write without ambiguity. No hardware faults this watch.
- `tone_bias`: `formal_duty_log`

**Output (~110 words):**
> Crew log, 2026-09-21T23:42Z. Sunfish-1, Mission Director Yusupova reporting end of watch. Submerged ops day seven. Relay layer remains dormant per architecture specification; gossip protocol idle and in expected state. The local store responded to a provenance query at 1837 local - Dr. Vargas's calibration notes from 2026-08-12 - with consistent state and no resolution conflict. Hash chain continuous since boat last surfaced. No hardware faults logged this watch. Crew rotation completed at 2200 with one swap from the standard schedule, recorded separately. Forwarding to next watch: routine. End of entry.

### Example 2 - personal_reflection

**Input:**
- `timestamp`: `Mission Day 14, 0617 local`
- `author_role`: `Mission Director`
- `unit_name`: `Sunfish-1`
- `situation_summary`: Anna queried the local store at her desk; got a clean answer; recognized that the boat is now the only place certain records exist. Long Now beat - what will happen to these records when she dies. No operational issue.
- `tone_bias`: `personal_reflection`

**Output (~140 words):**
> Crew log, Mission Day 14, 0617 local. Routine. I queried the local store this morning before brief - Hiroshi's annex from the second pre-departure review, which I had read at the time and wanted to confirm against memory. The system returned the document. There was no conflict to resolve, because there is no second copy to disagree with it. I am writing this down because I want a record of the moment I understood what we are operating inside. Everything we record now exists only here, on this boat, until we surface. The architecture made that fact visible by being unable to do otherwise. I am sitting with the question of what happens to these records if the boat does not surface. I have not resolved it. End of entry.

### Example 3 - balanced

**Input:**
- `timestamp`: (omit)
- `author_role`: `Principal Architect`
- `unit_name`: `Sunfish-1`
- `situation_summary`: Joel walking a younger engineer through why the schema-migration protocol has a three-pass read-confirmation cycle. The conversation surfaced a genuine technical question. Joel's answer was the ordinary architectural answer. He noticed the question was good.
- `tone_bias`: `balanced`

**Output (~130 words):**
> Crew log. Reyes, Principal Architect. Walked Iyer's apprentice through the schema-migration read-confirmation cycle this watch - three passes, not two, with the third pass deliberately delayed to surface clock-skew faults the first two cannot. The apprentice asked why we did not collapse the third pass into a quorum-based shortcut on the second. The honest answer is that the shortcut works on most days and fails on the day it matters; we picked the longer cycle because the boat is one of the days that matter. The question was a good one. I noted it for the post-mission debrief - apprentice instinct toward optimization is healthy and worth listening to before the architecture's safety margins are explained. End of entry.

## Cross-references

- **Voice exemplars:** `.pao-inbox/_creative/oss-architects-voices/02-anna-mission-log-fragment.md` is the canonical Anna-voice reference; consult for register match before drafting an Anna log entry.
- **Character sheets:** `.pao-inbox/_creative/character-sheets/` carries each character's voice register at full depth. Match the log entry's voice to the sheet when drafting non-Anna logs.
- **Anti-AI-tells:** `.Codex/skills/anti-ai-tells/SKILL.md` - consult before finalizing.
- **Literary devices:** `.Codex/skills/literary-devices/SKILL.md` - restraint is the default; devices land harder when the surrounding prose is plain.
