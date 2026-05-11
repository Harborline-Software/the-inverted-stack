---
type: convention-doc
volume: 2
audience: chapter-drafter, technical-book-writer, future contributors
status: canonical (locked 2026-05-05; CO directive)
related:
  - .pao-inbox/_creative/vol-2-archive-and-capture-convention.md
  - .pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md
  - chapters/book-2/CHAPTER-OUTLINE.md
---

# Vol 2 — Anchor / Bridge Sync Mechanic

> **What this is:** how the boat-local Anchor archive reaches long-now durability via the consortium-port Bridge across the multi-segment under-ice mission. Includes the bandwidth-bounded surface windows as a structural plot device, Wanjiru's sync-triage role as a chapter-load mechanism, and the conditional-preservation property that makes the leak event in Ch 14 weightier than a simple operational incident.

> **Why it matters:** the architecture's preservation promise is real but **conditional on the boat surfacing.** This is not a metaphor. Anna's diary entries, the Stefan-cross-check observations, the bulk sensor archive — none reach long-now durability until the Bridge receives them. An Anchor entry that never reaches the Bridge is contingent on its own node's survival. The book's Long Now thread is grounded in this operational reality, not just architectural philosophy.

---

## 1. The two-tier topology

| Tier | Where | Role |
|---|---|---|
| **Anchor (boat)** | Each crew node + central boat node + sensor heads | Captures everything (per opt-in). Local LLM runs here. Hash-chained, KEK-encrypted local store. Crew interacts via Anchor for all comms, search, documentation. |
| **Anchor-replication-internal** | Across the boat's nodes during the mission | CRDT replication between crew nodes during submersion. Boat-internal redundancy. Survives a single-node failure. |
| **Bridge (consortium ports)** | Punta Arenas, Helsinki ground station, and other consortium-affiliated facilities | Long-term durability. Federated across ports (Wanjiru's domain). Receives surfaced replication batches. Holds the long-now record. |
| **Anchor → Bridge sync** | Surface windows only; bandwidth-bounded | Bandwidth-bounded transfer of the on-boat archive to the Bridge. Window length and bandwidth determine what reaches durability per surfacing. |

The Bridge is the **only path to long-now durability** for the mission record.

## 2. The mission timeline and surface windows

Per the locked boat-power decision (`.pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md`): three under-ice segments separated by two surface windows, plus departure transit and final return transit.

| Phase | Days | Sync activity |
|---|---|---|
| Transit south | 1-7 | Surface — full bandwidth. Boat-state continuously synced to Bridge as routine. No archive backlog. |
| **Segment 1 (under-ice)** | 7-21 | **No sync.** Archive accumulates on Anchor; replicated across crew nodes for boat-internal redundancy; cannot reach Bridge. |
| **Surface 1** | 21-23 | **2-day window.** Wanjiru triages what reaches the Bridge. Mission-record voice + decisions first; sensor streams second; cross-check observations of rival mission third; bulk archive last, opportunistic. |
| **Segment 2 (under-ice)** | 23-37 | **No sync.** Backlog from Surface 1 (whatever didn't make it) carries forward. New capture accumulates. |
| **Surface 2** | 37-39 | **2-day window.** Higher-priority targeted sync — Stefan's mission has just concluded; cross-check evidence becomes time-critical. The political contest's window for the architectural-truth to land before the corporate narrative gels. |
| **Segment 3 (under-ice)** | 39-49 | **No sync.** Includes the leak event (Day 47) and the post-leak compute degradation. The operational record sits on the boat. **There is no Surface 3.** |
| Transit north | 49-56 | **Limited surface bandwidth** (Drake Passage; weather-dependent). Boat is surfaced but not at port; some sync resumes as conditions allow. |
| Final docking | Day 56, 04:41 local, Punta Arenas | **Full bandwidth + multi-day duration.** The bulk catches up. The Bridge finally receives the rest. Architecture's preservation promise completed. |

## 3. Bandwidth realities (2026-grounded)

- Surface bandwidth = Iridium / LEO-equivalent (Starlink-class) → realistically **5-50 Mbps depending on conditions, weather, satellite geometry**
- 2-day window × 30 Mbps avg ≈ ~600 GB potential transfer (best case; less in degraded conditions)
- Boat archive after 14 days under-ice = potentially **several TB** (raw sensor streams + voice transcripts + compartment video + LLM-derived index + per-author personal stores)
- **Conclusion: prioritization is required and the choice is operational.**

This is the **disconnected-signal artifact** — bandwidth scarcity as a structural plot device, not a backdrop.

## 4. Wanjiru's chapter-load: active sync-triage

In a traditional submarine, the comms officer manages the link. In the Nansen, **Wanjiru triages what reaches durability.** This is an upgrade in agency from passive comms-management to active institutional decision-making, and it's a chapter-load mechanism.

### 4.1 Her priority hierarchy during a 48-hour surface window

| Tier | Content | Why |
|---|---|---|
| **P0** | Mission-record voice transcripts of decisions; safety-critical incident records; signed audit-log entries | The institutional record's load-bearing slice |
| **P1** | Sensor streams critical to ongoing mission state; surface-window observations of any rival mission; regulatory-relevant cross-check evidence | What lands quickly enough to matter for the political contest |
| **P2** | Bulk operational logs; routine watch entries; non-critical sensor streams | Background record; can wait for next window |
| **P3** | Personal capture (per author consent); diary entries (encrypted; lower priority by author choice); compartment-camera video | Private + bulk; opportunistic |
| **P4** | Bulk multimedia (video; voice raw audio); documentation indices; LLM-derived analytical artifacts | Largest data class; usually carries forward to next window |

Within a 600 GB window, P0+P1 typically fits with bandwidth to spare. P2 partially. P3-P4 rarely complete. **Carryover across windows compounds.**

### 4.2 The political dimension

Wanjiru's prioritization is not neutral. Specific operational beats:

- **Surface 1:** Stefan's mission is still under way; cross-check observations are partial; Wanjiru holds them for Surface 2 when the rival mission has concluded and the Nansen's full surface-window-1 observation is available. Mission record + safety-critical lands.
- **Surface 2:** Stefan's PR cycle is fresh; his official report is days old; the consortium's institutional response window is narrow. Wanjiru pushes the cross-check evidence — even at the cost of deferring some bulk operational records to Surface 3 (which doesn't come). **The political contest's clock is the bandwidth window's clock.**
- **Final docking:** the bulk catches up. The Bridge accumulates the rest. Wanjiru's final consortium filing draws on the full archive — including the Stefan cross-check and the sensor-head forensic finding.

### 4.3 What the chapter-drafter writes

Wanjiru's chapters (especially Ch 11, Ch 15, Ch 17) include scenes where she is making prioritization decisions in real time. She is not just at a console; she is making *which truths reach durability when* decisions. The reader should register the agentic weight of this without the prose turning didactic.

## 5. Conditional preservation — the Long Now thread, grounded

Anna's question — *what will happen to these memories when I die?* — has, on Day 14 of the mission, the answer: *they survive only if the boat does.*

The architecture's preservation promise is real but conditional:

| Data class | Preservation status during submersion | Status after surfacing reaches Bridge |
|---|---|---|
| Mission-record voice + decisions | On boat-internal Anchor replication; survives single-node failure | Long-now durable on Bridge; replicated across consortium ports |
| Sensor archive | Same | Same; bulk catches up over multiple windows |
| Compartment camera video | Same; consent-gated | Often carried in P3-P4; may not reach Bridge until final docking |
| Anna's personal diary | Encrypted under her KEK; on her node + boat-internal replication | Long-now durable IF Wanjiru prioritizes; often P3 |
| Joel's engineer's notes | Same | Same |
| Wanjiru's institutional drafts | Higher-priority by her own role | P0-P1; reaches Bridge faster |

**Until final docking, the entire emotional record of the mission is contingent on the boat returning.** The architecture preserves what reaches the Bridge. What doesn't reach the Bridge is contingent on individual nodes surviving.

This is what the leak event in Ch 14 puts at stake. **The boat almost didn't surface.** If a different fault had finished what the leak began, none of Anna's diary, none of Joel's later thinking, none of the operational record beyond Surface 2 would have reached durability.

## 6. The convergence at docking — capability + preservation together

Two threads converge at Day 56 Punta Arenas:

| Thread | Resolves at docking |
|---|---|
| **Preservation** | The bulk archive reaches the Bridge. Diary entries, sensor archive, video — all become long-now durable. Anna's question's literal answer: *they reached the Bridge; they will survive.* |
| **Capability** | The Bridge's compute (full GPU racks; petabyte-scale storage) restores the heavy-RAG, full-archive-query, multimodal-tagging, real-time-translation capabilities the post-leak laptop-class fallback could not provide. |

**Day 56 is not just the political ending; it is the architectural ending.** The boat surfaces; data flows; queries that have been waiting (Anna's accumulated paper-list of *things to ask the system*) get answered; the institutional preservation promise is finally fulfilled.

This is the chapter Ch 18 quietly closes on, before the cumulative Forsaken reveal lands the political contest. Anna writes the staff history with full system support. The book the reader is finishing is the artifact being authored on-page.

## 7. Carryover scenes — concrete chapter beats

How the sync mechanic surfaces in chapter prose:

### 7.1 Ch 6 (First Surface, First Forsaken Reveal)

Wanjiru explains the prioritization to Anna in dialogue. Reader installs the constraint. *Forty-eight hours, thirty Mbps if we're lucky, two terabytes accumulated. We push the mission record first. The sensor archive carries forward.* The chapter ends with the boat re-submerging; Wanjiru has triaged successfully; some of what she would have liked to push (early observations of rival mission preliminary results) carries to Surface 2.

### 7.2 Ch 11 (Second Surface, Second Forsaken Reveal)

The race chapter. Stefan's mission has concluded. His PR cycle is fresh. Wanjiru has 48 hours to push enough cross-check evidence that the consortium can interrogate his report. The chapter is partly a clock — bandwidth, time, what fits, what doesn't. Anna registers Wanjiru's institutional weight forming. *She is choosing what becomes record.*

### 7.3 Ch 12 (Beginning of the End — Segment 3 Dive)

Anna's narration: *And now everything we record for the next ten days is on the boat alone until we surface in Punta Arenas.* Plants the conditional-preservation stake before the climax.

### 7.4 Ch 14 (The Crossing — leak event)

The boat almost didn't surface. The chapter's emotional weight is what is *almost* lost — not just life, not just the mission, but the entire post-Surface-2 record of the architecture. Anna's diary entry from this chapter is among the most-conditional records in the mission; if the boat had not surfaced, it would have been lost with the boat.

### 7.5 Ch 16-17 (Final Ascent + Transit North)

Limited surface bandwidth as the boat returns. Some sync resumes; targeted records (the operational damage report, the forensic findings) prioritize. Anna's accumulated query list waits.

### 7.6 Ch 18 (Punta Arenas Surfacing)

Full-bandwidth catch-up. The bulk reaches the Bridge. The forensic filing reaches consortium institutions. The architectural-political contest enters its full-data phase. The chapter quietly notes the moment the architecture finishes its work — *the system answered the things I had been waiting to ask*.

## 8. Drafter discipline rules

1. **Surface windows are real** — the prose registers them as bounded windows, not as continuous communication. Phrases like *while we had the link* or *before the boat dove again* keep the constraint operational.
2. **Triage is agentic, not automatic.** Wanjiru chooses. The chapter shows her choosing. Don't write her as a router; write her as the institutional decision-maker she is.
3. **Carryover compounds.** Data that didn't make Surface 1 + new accumulation arrives at Surface 2. The boat's local archive grows. The Bridge's hold-state lags.
4. **Conditional preservation is real and registered.** When Anna writes the staff history later, she knows which records made it off the boat at which window. The book is informed by *which durability these records have at which point in the mission*. Some of the staff history's later quoting acknowledges *we did not know at the time whether this would reach durability*.
5. **Final docking restores both capability and preservation.** Don't write Punta Arenas as just the political ending. It is the architectural fulfillment. Both threads land together.

## 9. Cross-references

- **Capture model + 2026 stack + degradation:** `vol-2-archive-and-capture-convention.md`
- **Series trajectory:** `series-arc-sunfish-trajectory.md`
- **Boat-power decision + multi-segment timeline:** `.pao-inbox/_decisions/2026-05-04-vol2-boat-power-option-c-locked.md`
- **Per-chapter sync-mechanic beats:** `vol-2/CHAPTER-OUTLINE.md`

---

## Status

- **Locked 2026-05-05** per CO directive.
- **Wanjiru's character sheet** updates to reflect active sync-triage as a load-bearing chapter role.
- **Pre-existing chapter drafts may not yet reflect this convention**; Ch 5 and Ch 2 v1 predate this doc.
