---
type: pao-directive
audience: Yeoman (chapter pilot drafting)
priority: medium
related:
  - .pao-inbox/_creative/joel-teaching-register-canon.md
  - .pao-inbox/_creative/character-sheets/joel-reyes-principal-architect.md
  - vol-2/act-2/ch07-joels-sunfish.md
---

# PAO Directive - Pilot Joel teaching-register extension on Ch 7

## What

Implement the **Joel teaching-register extension** (canon adopted 2026-05-07) as a pilot pass on Ch 7 *Joel's Sunfish*. This is the chapter where Joel's teaching voice is already most established; the pilot is to deepen it, not to install it.

## Why

CO directive 2026-05-07 selected this approach over two rejected alternatives:
- Adding a new boat-resident character (rejected: bends Anna's voice, breaks manifest canon)
- Workshop-entries + glossary-only (sufficient for ~90% of cases but doesn't naturalize explanation in prose)

Canon doc is at `.pao-inbox/_creative/joel-teaching-register-canon.md`. Read it before drafting.

Task #11 has been pending for 8 days. With Ch 2 reprocessed and Ch 17 pilot queued (see directive 2026-05-16T11-53Z), the Joel pilot is the natural third stream.

## Scope of the pilot

- **Ch 7 only.** No retroactive application to other chapters. Conditional scale post-CO-review.
- **Deepen existing teaching beats** - do not add new scenes. Joel's existing teaching moments (Sunfish-naming disclosure, schema-migration-with-Priya callout, "gauge in front of you" register) are the load-bearing material. The pilot extends, doesn't invent.
- **Anna remains POV.** Joel's teaching arrives through Anna's first-person registering of it ("He explained X, and I noted Y"), not through Joel direct-quotes alone. This is the canon doc's key constraint.

## Constraints

- **No franchise imports.** Joel's register is engineering-fluent and discipline-rooted, not a sci-fi captain register. Cf. Janeway skill's first-person voice work - voice, not setting.
- **Held-line continuity.** Run the ch07 held-lines.json after drafting (`vol-2/act-2/ch07-joels-sunfish.held-lines.json`). Joel's "muscle memory by the time I was thirty" line and similar canonical phrasings must survive intact.
- **Telemetry check.** After draft, run galley verdict on Ch 7. Pre-pilot baseline is at `build/output/qa/ch07-joels-sunfish.lexical-fatigue.json` (note: `discipline` family was at 9.92/1k = 5.19× baseline pre-pilot - this is thematic, not fatigue; do not flatten it).
- **No word-count blowout.** Pilot should net +/-10% on Ch 7's current word count. The technique is register-deepening, not exposition-adding.

## Acceptance check

- `vol-2/act-2/ch07-joels-sunfish.md` revised in place (Yeoman commits a single pilot commit; PAO reviews).
- Galley verdict still green; `discipline` family density preserved (not flattened, not amplified).
- A `.pao-inbox/yeoman-resumed-*` beacon with: 3-line summary of what changed, telemetry deltas, and one open question if any.
- Audio re-render queued (drops into the ch07 re-render slot from directive 2026-05-16T11-52Z if that batch is still active).

## Decision the pilot informs

If Ch 7 holds Joel's voice without diluting Anna's POV: scale to Ch 13 (schema-migration scene with Priya, the other strongest Joel-teaching site). Otherwise: stop, document the failure mode, leave Ch 7 as the only Joel-teaching-deepened chapter.

## Coordination

PAO reviews the Yeoman pilot commit before merge to canon. Beacon back when draft is staged.
