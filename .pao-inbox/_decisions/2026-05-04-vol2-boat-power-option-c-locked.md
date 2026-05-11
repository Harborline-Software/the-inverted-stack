---
type: decision
date: 2026-05-04
author: PAO (capturing CO directive)
status: locked — CO directive
relates-to:
  - vol-2-concept-locked-elements-2026-05-04.md
  - vol-2-series-arc-wot-bobiverse-2026-05-04.md
  - vol-2-long-now-memory-thread-2026-05-04.md
  - chapters/closing/the-crossing.md (will need revision pass)
---

# Vol 2 — Boat Power Decision: Option C Locked

## CO directive (this session)

> "Go with C. Diesel/AIP multinational research sub, mission redesigned with multiple under-ice segments."

This locks one of the three open items from the locked-elements doc. The remaining two open items (prior-failure framing path B confirmation; unnamed-colleague on/off-frame) are still pending.

## What option C is

The Sunfish-1 boat is a **diesel-electric / AIP (Air-Independent Propulsion) research submarine** operated under the same multinational consortium that funds the mission. Real-world precedent: not nuclear (no precedent for non-Navy nuclear research subs), but operationally credible — modern AIP boats (Type 212/214, Soryu-class, Gotland-class) achieve 14-21 days sustained submerged operation at low speed.

Cooperation model: same precedent shape as IODP (International Ocean Discovery Program) for surface drillships, Antarctic Treaty research stations, CERN. Multinational ownership and governance; member-nation crew; unified mission command. The boat itself becomes a working physical metaphor for Sunfish's architecture: *cooperation across sovereignty without dependence on any single sovereign.*

## Why C over A or B

(Decision rationale captured for future reference; CO ratified after PAO presented A/B/C with trade-offs.)

- **Better audiobook listenability** — multiple shorter partitions with reconciliation events between them maps to sustained listening better than a single 56-day under-ice arc with one resolution
- **Closer to the architecture's design audience** — Sabina's BFSI use case, GCC offshore platforms, polar field stations face *recurring intermittent partitions*, not 56-day continuous partitions. Testing the architecture under conditions closer to its intended use is more meaningful than testing it under maximally extreme conditions a typical user will never face.
- **Politically simpler** — no nuclear sub means no military legacy, no nation-of-origin complications, no extra burden of "explain how this exists." A multinational-consortium AIP research sub is structurally believable in 2026-2030 fiction with mild normalization.
- **More architectural test beats per mission** — each under-ice segment is a partition test; each surfacing is a reconciliation test; each surface event is a "what did the Forsaken do while we were under" beat
- **Cleaner Joel-character mapping** — Joel's NPO biography is strictly biographical (carries forward as discipline) without requiring the boat itself to be nuclear and engage him as nuclear-trained personnel. His expertise transfers without literal reactor proximity.

## Mission redesign — multi-segment under-ice operations

**Overall mission length unchanged: 56 days Punta Arenas → operations → return.** Existing locked beats (departure 06:42 day 1; arrival 04:41 day 56) carry forward.

**Recommended segmentation: three longer segments** — preserves "deep partition" stakes per segment while distributing the architectural test beats and Forsaken-revelation events:

| Phase | Days | Activity |
|---|---|---|
| Transit south | 1-7 | Surface transit Punta Arenas → Drake Passage → ice edge |
| **Segment 1** | 7-21 | First under-ice deployment (~14 days submerged) |
| Surface 1 | 21-23 | Surface for battery recharge + mesh reconnect; 2-day reconciliation window |
| **Segment 2** | 23-37 | Second under-ice deployment (~14 days submerged) |
| Surface 2 | 37-39 | Surface for recharge + reconnect; 2-day reconciliation window |
| **Segment 3** | 39-49 | Third under-ice deployment (~10 days submerged) — mission climax (leak event lands here) |
| Transit north | 49-56 | Surface transit back to Punta Arenas |

Three under-ice segments totaling ~38 days under ice. Two intermediate surface windows (each ~2 days). Mission climax in Segment 3 — the longest single period at the deepest mission objective; the leak-with-fire-cascade lands during this segment, when the architecture has been under live test for the longest cumulative time and the crew is at their most fatigued.

**Alternative segmentation considered** — five shorter segments of ~7 days each (more partition events, more reconciliation beats, but each beat is smaller). PAO recommends the three-segment design unless XO / CO want denser cycling.

## Implications for narrative beats

### What stays
- Departure 06:42 day 1 from Punta Arenas — preserved
- Arrival 04:41 day 56 at Punta Arenas — preserved
- The leak-with-fire-cascade as the central environmental event — preserved (lands in Segment 3)
- 0317 / 0319 / 0321 / 0342 timestamp sequence for the leak alarm — preserved
- Diego survives, hero of competence, retires to San Martín de los Andes earned through what he did — preserved
- Day-20 partition realization scene as Anna's structural moment — **preserved with adjusted setting**: the Day-20 scene now happens in the middle of Segment 1 (~Day 14 under-ice from departure means Day 14 from boat departure, but the realization itself happens during the first sustained under-ice partition, which under the new design is Days 7-21). Renaming to "Segment-1 partition realization" or keeping "Day-20" as approximate is a CO call; PAO recommends keeping Day-20 since the narrator (Anna) refers to mission-day rather than segment-day.
- 4,017 photographs, Spanish letter to María Elena, all character beats — preserved

### What changes
- "Dive at 11:18 day 1" beat in The Crossing → moves to **Day 7 first dive** (~11:18 some day in the first dive window). Existing chapter prose needs revision pass.
- "We departed... and dove" linear narrative → multi-segment narrative with intermediate surface windows
- **The Forsaken move three times** during the mission, not once. Each surface window reveals what they did while the boat was under. Cumulative effect of all three reveals only legible at final surfacing (Day 56 at Punta Arenas). This is a richer dramatic structure than the single big reveal.
- Anna's retrospective narration acquires three internal "and then we surfaced and the world had changed" beats instead of one
- Each architectural beat (lease coordinator, gossip, schema migration, security/key) can map to a specific segment for testing — the whole architecture isn't proven in one continuous run; it's proven across three live deployments with reconciliation between them, which is closer to how production deployments actually face the architecture
- Priya's "impossible migration" climax beat (her Healing-channel-by-surrender moment) lands in Segment 3 alongside the leak event — high-stakes convergence of the architecture's hardest discipline with the mission's hardest moment

### Existing The Crossing chapter — revision pass needed

The existing closing chapter (`vol-1/closing/the-crossing.md`) currently reads as a single-dive 56-day mission. Under the new multi-segment design, this needs revision. Specific edits:

1. "We dove at 11:18 the first day" → "We dove at 11:18 on day seven, after a week of surface transit"
2. The line "We came home with eleven of twelve" → preserved (still true, just under multi-segment ops; though the death scene is being replaced by leak-survival, so this whole sentence may already be in flux)
3. Existing prose that implies continuous submerged operation needs a revision pass to acknowledge surface intervals
4. The "fifteen minutes ahead of the tide table" detail at departure — preserved
5. The "ascending after 56 days" framing — needs adjustment; ascending happens three times (end of each segment) plus the final transit ascent

This is a **separate PR** when CO is ready to take The Crossing chapter through revision. Not gated on Vol 2 concept-note draft.

### Existing series-arc doc adjustments

`vol-2-series-arc-wot-bobiverse-2026-05-04.md` says: *"Mesh signal lost ~0200 day 2; from here, Sunfish operates in partition. ... Surfacing: Day 56."*

Under the new design: the mesh signal is lost three times across three under-ice segments, with reconciliation events between. The series-arc doc's three-act structure for Book 1 (Acts I/II/III on days 1-14 / 15-42 / 43-56) carries forward but maps onto the segment structure differently:

- Act I (days 1-21): departure + transit south + Segment 1; first under-ice realization (Day-20 scene); first surface and first Forsaken reveal
- Act II (days 22-42): Segment 2 + interim Surface + Segment 3 begins; subsystem-by-subsystem testing through Anna-Joel dialogue; second Forsaken reveal; Sabina's use-case validation; Hiroshi's data work; Diego quietly essential
- Act III (days 43-56): Segment 3 climax (leak + fire cascade) + final ascent + transit home + final reconciliation at Punta Arenas; cumulative Forsaken reveal lands here

## Joel character sheet — implication

Joel's existing sheet (PR #96) noted that his Navy-nuclear past is "biographical only, not engaged by the current boat" if the boat is non-nuclear. Under option C this is now confirmed: the boat is diesel/AIP. Joel's NPO discipline is portable to civilian distributed-systems work; the literal nuclear plant is in his past, not his present. **No edit to Joel's sheet required** — the placeholder phrasing was correct.

A subtle detail PAO can add when drafting Vol 2: Joel on a diesel boat is *outside his Navy-veteran comfort zone in a specific sense.* Different smell (diesel rather than reactor); different rhythms (battery management; AIP plant management); different watchstation patterns. A trained Navy submariner on a non-Navy diesel boat is engaged but not at home. The mild discomfort is a quiet character note for him — adds to his internal landscape during mission scenes.

## Two remaining open items before full concept-note draft

1. **Prior-failure framing** — currently locked as Path B (cut-short mission + colleague's failure of judgment / undisclosed schema-migration limitation). CO confirmation requested.
2. **Unnamed colleague** — does the colleague who didn't disclose appear anywhere in the series, or stay permanently off-frame? Affects the character list for later books and the Book 4 (Aiel Waste analog) flashback chapter.

Once those clear, full concept-note draft begins.

## Status

- **Boat power: LOCKED** (option C — diesel/AIP multinational research sub)
- **Mission timeline: redesigned** (3 under-ice segments + 2 intermediate surface windows + transit windows)
- **Existing The Crossing chapter: revision pass deferred** (separate PR when CO ready)
- **Series-arc doc Act mapping: adjusted in this doc** (operational, not yet in the series-arc doc itself; can be propagated when needed)
- **Joel sheet: no edit required**
- **Other character sheets (Anna, Priya): no edit required** (their material is mission-experience-driven, boat-power-agnostic)
- **Two open items remaining** (path B confirmation; unnamed-colleague disposition)
