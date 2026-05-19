---
type: convention-doc
volume: 2
audience: chapter-drafter, technical-book-writer, future contributors
status: canonical (locked 2026-05-05; CO directive)
related:
  - .pao-inbox/_creative/vol-2-anchor-bridge-sync-mechanic.md
  - .pao-inbox/_creative/series-arc-sunfish-trajectory.md
  - .pao-inbox/_creative/vol-2-concept-note-2026-05-04.md
  - chapters/book-2/CHAPTER-OUTLINE.md
  - .claude/skills/crew-log-style-entry/SKILL.md
---

# Vol 2 - Archive and Capture Convention

> **What this is:** the canonical reference for how Sunfish operates *as a platform* on the MERIDIAN-7 mission, what the prose can and cannot claim about it, and how the archive-as-mechanism shapes Vol 2's voice and structural devices. Read this before drafting any Vol 2 chapter that touches the architecture in operation.

> **What this is not:** a Vol 1 specification. Vol 1 is the architectural paper; this doc is the operational deployment. Where the two disagree, Vol 1's protocol invariants win and Vol 2's prose stays consistent with them.

---

## 1. The premise - Sunfish is the boat's nervous system

In a traditional submarine, communication and capture are bolted onto the boat: 1MC wire intercom (ephemeral), per-console sensor logging (local), formal-log narratives written from memory by the watch officer. The official record is whatever the captain remembers and chooses to write down. Most of what happened on the boat is gone the moment it stops happening.

In the Nansen, **the boat is the archive.** The Anchor application is not "an app the crew uses for some things." It is the operational substrate. Every voice exchange (per opt-in), every sensor reading, every video frame from compartment cameras (per consent), every Anchor-routed message between crew, every command-and-response between control plane and instrument - all routed through Anchor, captured locally on each crew node, hash-chained, signed at capture, KEK-encrypted where appropriate, replicated to Bridge on surface windows.

This is the architectural altitude shift Vol 2 is built on. The book is about **what it means to operate inside an architecture that records itself completely.**

## 2. The two-register voice device

Vol 2 uses two distinct logging registers, both diegetic artifacts on the Sunfish local store, with *different cryptographic statuses*. They are not stylistic variants. They are different kinds of artifact.

### 2.1 Formal log (captain's / engineering)

| Aspect | Detail |
|---|---|
| Audience | Consortium, chain-of-command, post-mission debrief, future record |
| Register | Disciplined, professional, third-person-ish ("Reyes contained the leak; eleven minutes; reported clear") |
| Content | Facts, decisions, observations, carryovers, instrument readings |
| Truth-status | **Authoritative**: signed, sealed, load-bearing for the institutional record |
| Sunfish artifact | Public-readable on the audit log; signed; immutable; replicated to consortium ports per priority |
| Vol 1 in-universe role | Source documents Joel cites in his architecture paper |
| Generator skill | `.claude/skills/crew-log-style-entry/SKILL.md`, tone_bias = `formal_duty_log` or `balanced` |

### 2.2 Personal diary

| Aspect | Detail |
|---|---|
| Audience | Self / future self / no one |
| Register | First-person, interior, mature-honest ("He looked at me through the glass") |
| Content | Doubts, recognitions, unresolved questions, the things that don't go on the record |
| Truth-status | **Honest**: private, off-the-record, emotionally true |
| Sunfish artifact | Encrypted under the author's KEK; access controls; surfaces only on author-controlled disclosure |
| Vol 1 in-universe role | Source for Anna's Vol 2 staff history (sometimes; some entries stay sealed) |
| Generator skill | `.claude/skills/crew-log-style-entry/SKILL.md`, tone_bias = `personal_reflection` |

The two registers' co-existence is what makes the differential device work: the formal log is what Anna *recorded* for the file; the diary is what she *also wrote* but did not publish. The chapter's emotional weight often lands in the gap.

## 3. The chapter-level patterns

Three patterns are canonical for log-opener / log-inset placement. **Used only where they earn their place** - never as formula.

**Pattern A - formal-log opener only.** Chapter opens with the formal log; scene plays; chapter closes without further log artifact. Cheapest. Use for chapters where the orientation is the only structural lift the device adds.

**Pattern B - formal-log frame.** Chapter opens with formal log A (pre-event); chapter closes with formal log B (post-event). The two logs differ in tone - log B knows what log A didn't. The differential is the chapter's quiet emotional arc. Use for routine-tempo chapters where the lived experience changes Anna's procedural assessment.

**Pattern C - formal log + diary inset.** Chapter opens with the formal log (clean, professional). Mid-chapter or end-chapter, a single italic diary entry surfaces. The formal log is what Anna recorded; the diary is what she didn't put on the record. The differential is the chapter's central truth. Use for the heaviest chapters - climactic moments, partition-realization beats, leak event, cumulative reveals.

Per-chapter pattern assignments live in `vol-2/CHAPTER-OUTLINE.md`.

## 4. The 2026-grounded local-LLM stack

Anchor's capabilities must remain **plausibly assemblable today on local-first hardware** - what an actual practitioner in 2026 could build with shipping or near-shipping components. Nothing speculative; nothing requiring "in five years." This is a hard register constraint.

### 4.1 Hardware on the boat

| Class | Hardware | Anchor role |
|---|---|---|
| **Compute hub** (1) | Workstation w/ RTX 6000-Ada or dual RTX 4090s, ~96GB RAM, NVMe RAID. Single point of compute concentration. | Heavy local-LLM models (70B-class for less-common translation pairs); full-archive RAG index; agentic compositions; multimodal video tagging. **Vulnerable to physical damage; loss forces capability degradation.** |
| **Crew nodes** (~10) | Laptops: Mac M3/M4 Pro/Max class, or NVIDIA RTX 4070-class. One per crew member. | Per-author personal RAG index; transcription via faster-whisper; voice command + wake-word; basic translation between common pairs; KEK-protected personal store; signing of capture events. |
| **Sensor heads** (several) | Edge devices on the sensor buses (off-the-shelf vendor products; firmware updateable). | Sensor capture; small-model anomaly detection at edge; signed reading streams. **See § 7 on the supply-chain vulnerability.** |

### 4.2 Software on each node

All real today (2026); all documented elsewhere as shipping or imminent:

| Capability | Stack |
|---|---|
| Voice transcription | faster-whisper / Whisper.cpp on Apple Silicon or NVIDIA - real-time on M-series, near-real-time on RTX 4070-class |
| Translation | NLLB-200 for less-common pairs; local-LLM (Llama 3.x, Qwen 2.5) for common pairs |
| Document indexing | BGE-M3 / Mxbai-embed-large embeddings; LanceDB or FAISS vector store |
| RAG generation | Ollama / LM Studio / vLLM hosting; local-LLM 7B-70B class depending on hardware |
| Wake-word + voice command | Porcupine, OpenWakeWord, Vosk |
| TTS for accessibility | Kokoro, Piper, or XTTS - same family as the project's audiobook pipeline |
| Sensor anomaly detection | PyOD-style classical methods + small specialized models per sensor type |
| Compartment camera tagging | YOLO / CLIP for selective tagging, on-device, only when activated by consent |
| Agentic multi-step actions | LangGraph-style local frameworks bound to Sunfish CRDT store + KEK/DEK access controls |
| Hash-chain integrity | Standard Sunfish protocol primitives from Vol 1; not LLM-dependent |

### 4.3 What Anchor explicitly does NOT do

The prose must respect these boundaries - drift into any of them breaks the 2026-grounded register:

- **No continuous ambient interpretation** of arbitrary background conversation. Capture is opt-in per stream; speakers know when their voice is being transcribed; conversations not flagged for capture are ephemeral.
- **No real-time synthesis of past events as video.** No holodeck-equivalent. Replay is verbatim playback only.
- **No replicator, no warp-core, no faster-than-light anything.** The book is a 2026 technical thriller, not science fiction.
- **No multi-step abstract reasoning at conversational latency** that exceeds what laptop-class compute can deliver. Slow operations are visibly slow in the prose.
- **No cloud uplinks during submersion.** Period. Surface windows are the only path off the boat (see § 5).
- **No "AI-knows-best" override behaviors.** Anchor is a tool. The crew makes decisions. The architecture has opinions about preservation and access; it does not have opinions about mission decisions.
- **No autonomous action against crew preference.** Every captured stream is consented. Every diary entry is the author's choice. Every disclosure is author-controlled.

## 5. Capture is opt-in per stream and per author

The capture model is **not** panoptic. Three protections are canonical:

1. **Opt-in per stream.** Compartment cameras require consent of everyone present. Voice transcription on personal channels can be disabled at the speaker's choice. Sensor streams that touch personal data require author consent.
2. **Access-controlled, not god-mode.** Anna does not have read access to Joel's diary. Wanjiru does not surveil the crew. The mission's audit log records *who reads what*; reads themselves are events. Read access requires explicit grant or institutional warrant.
3. **Disclosure is author-controlled.** Anna's staff history (the book) is *her curation* of what reaches public visibility. The architecture's job is to preserve the option of disclosure; not to publish.

This is the protagonist position the book takes against Helvetia/TrustMesh's selective-corporate-retention model. The architecture's response to "what about surveillance?" is *the captures live on the author's node, encrypted under the author's key, governed by access controls the author sets.* Centralization is not absent because the architecture is naive about power; it is absent because the architecture is designed to make it impossible.

## 6. Graceful degradation under hardware loss

The compute hub is a single point of capability concentration. Sunfish's response to its loss is *graceful degradation* - capabilities scale down by tier rather than failing whole. This is a load-bearing local-first property the leak event in Ch 14 demonstrates operationally.

### 6.1 What degrades when the hub is lost

- Heavy RAG against the full mission archive (the index lived on the hub's NVMe array)
- Real-time translation across all crew languages simultaneously (less-common pairs needed the 70B model)
- Multi-step agentic compositions (slower; smaller models can't reliably chain tool use across many steps)
- Compartment-camera video tagging at any depth (compute-bound)
- Sensor anomaly detection at full coverage - some streams downgrade from continuous to sampled, or fall to threshold-only without LLM-assist
- Voice-cloning / TTS at the Bridge-equivalent quality

### 6.2 What survives on laptop-class

- Per-author personal RAG against each crew member's own indexed subset
- Transcription (faster-whisper runs fine on M-series or 4070-class)
- Wake-word + voice command
- Basic translation between common pairs (English ↔ Spanish, English ↔ Russian, English ↔ Japanese, etc.)
- Hash-chain integrity, KEK/DEK access control, signed audit log
- Anomaly detection on critical sensor streams (sampling reduced from continuous)
- Each crew member's local Anchor agent for personal queries
- Forensic substrate (see § 8) - narrow targeted analysis is feasible on laptop-class even when broad indexing is not

### 6.3 How the prose registers degradation

Anna's narration registers reduced capability without naming components. Not *the local LLM ran a smaller model after the hub died*. Instead: *the system answered slower; some queries we just didn't ask*. *I made notes for what to ask the system once we surfaced. The list grew to twenty-two items by Day 56.* The architecture's reduced state is visible in *what the crew does and doesn't do*, not in technical exposition.

The crew adapts:
- Multilingual conversation falls back to whoever speaks the relevant common language; some exchanges that used to be native-language fluid become halting English (or Spanish via Diego, Russian via Anna, depending on the pair)
- Joel's schema-related work gets done with laptop-class only - slower, more careful, more verification by hand
- Wanjiru's surface-window sync-triage happens with diminished LLM assistance; she does more of the prioritization manually
- Anna's queries against the archive accumulate as a written list of *things to ask when we surface*

## 7. The OSS-funding-asymmetry - the architecture's known weakness

This is the architectural-philosophical contest's hardest honest edge: **OSS architectures cannot vertically integrate.** They can't afford to design custom silicon; they can't afford to build their own sensor heads; they can't afford to maintain their own firmware fork. They source off-the-shelf, integrate, ship.

The vendors they depend on are exactly the entities that well-funded centralizing actors can capture - through co-development partnerships, acquisitions, board-level influence, or supply-chain investments. **Helvetia Trust SA's strategy is to operate at this layer.** Their public-facing positions are about identity and federation; their structural reach is via vendors whose components OSS missions integrate by necessity.

Sunfish's response to this constraint is mature security thinking - defense in depth, not defense in promise:

- The architecture does NOT claim to prevent supply-chain compromise of off-the-shelf components.
- The architecture DOES claim to detect compromise after the fact via the forensic substrate (§ 8).
- Centralized architectures (TrustMesh) cannot detect at all - they don't preserve the full pre-failure timestream of every edge device; their selective-sync model discards the data that would surface tampering.
- The institutional response - vendor-attestation requirements, firmware-transparency rules, supply-chain audit standards small projects can comply with at scale - is the standards-body work Wanjiru takes up after the mission.

This is the **structural reason the Forsaken keep returning** across the series. Capital concentrates. OSS doesn't have equivalent capital. Vendor-capture is always available as an attack surface. The architecture's response is not to claim it has solved the problem; it is to claim *we detect what they cannot detect*.

## 8. The forensic substrate

The Anchor archive is more than preservation. It is an **investigative tool**.

Each capture event - sensor reading, voice transcription, video frame, configuration change, command-response, firmware update - is hash-chained, signed at capture, replicated across crew nodes, KEK-encrypted where appropriate. The archive's properties:

- **Tamper-evident.** Modifying any historical event breaks the hash chain and is detectable.
- **Replicated.** The boat-internal replication keeps the archive surviving single-node failures (including the leak event's compute-hub loss).
- **Queryable across the full timeline.** Any past state can be reconstructed; any pre-failure pattern can be analyzed.
- **Cryptographically attributable.** Signed-at-capture events tie data to the specific node and authority that produced them. Forging an event requires forging the signing key.

When Wanjiru and Joel investigate the sensor head's pre-failure behavior in Ch 17 (Transit North), they have the **full firmware-update history, every configuration change, every command-response between the sensor head and control plane, and the full sensor reading stream - all hash-chained, signed at capture, undeniable.**

TrustMesh missions cannot do this. Their selective-sync, corporate-retention model doesn't preserve the full pre-failure timestream of every edge device. Stefan's mission, if compromised in a similar way, **would not even know.**

The forensic substrate is therefore a load-bearing architectural property that lands in Vol 2's plot:
- Ch 11 (Second Forsaken Reveal): Wanjiru cross-checks Stefan's PR against the Nansen's surface-window observations of his mission; the architecture supplies the cross-check evidence.
- Ch 14 (The Crossing): the leak event captures fully on Anchor; the operational record is intact; the cause of failure remains queryable for post-mission analysis.
- Ch 15 (Compromised Relay Holds): Wanjiru begins forensic queries against the sensor head's pre-failure timestream during the chapter, before the post-leak compute degradation makes the analysis slow.
- Ch 17 (Transit North): Joel + Wanjiru complete the forensic analysis on laptop-class compute, surface the supply-chain pattern, draft the regulatory filing for the consortium.
- Ch 18 (Punta Arenas Surfacing): the regulatory filing reaches the consortium; the architectural-political contest enters its institutional phase.

## 9. Header conventions for log artifacts in prose

Concrete patterns the chapter-drafter uses to render formal-log and diary entries on the page.

### 9.1 Formal log header

Recommended forms (rotate across chapters; never identical twice):

```
Crew log, 2026-04-02T14:42Z. Yusupova, Mission Director-designate. RV Nansen, MERIDIAN-7.

[body - 80-200 words per crew-log-style-entry skill]

- Filed to selection-archive; hash f3a4...90c2
```

Variants:
- `Mission log, Mission Day 14, 0617 local.` - mission-day form
- `Selection file entry, dated 2026-04-02.` - pre-departure record
- `Daily duty log - Reyes, J., Principal Architect - Mission Day 30.` - engineer's log
- `Recovered log - the Nansen archive; Anna Yusupova, Mission Director.` - retrospective recovery (used rarely)
- `Staff history annotation, drafted 2026-12-XX.` - Anna's staff-history-era annotations on prior records

The closing hash signature is **optional** - appears once or twice across Book 1 to install the diegetic-artifact convention; dropped on later chapters once the reader has the pattern. Include for chapters that turn on the artifact's authoritativeness (Ch 14 operational damage report; Ch 17 forensic-finding filing; Ch 18 regulatory filing).

### 9.2 Diary header

Recommended forms (italicized in prose; appears within scene rather than as section break):

```
Personal file, 2026-10-31. Encrypted under author's key. Access: self only.

[body in italics or plain - 80-200 words]
```

Variants - the access-control framing varies slightly per author:
- `Personal file, encrypted under author's key.` - Anna's default
- `Engineer's notes, sealed.` - Joel's engineering-grounded variant
- `Private.` - minimal; for short diary entries

Or fully prose-naturalized (no metadata header):
- `I am writing this in my own file, where it will not be read.`
- `This is for me.`

The metadata-header version installs the diegetic mechanic; the prose-naturalized version is for chapters where the device is already established.

## 10. Drafter discipline rules

Five rules every Vol 2 chapter draft must follow:

1. **The architecture is operational reality; the prose names what crew did, not what models handled it.** Anna says *the system answered without ambiguity*; she does not say *the local LLM ran a RAG query against the document index*.
2. **Capture is consent-gated and access-controlled.** No surveillance-state register. Where capture happens, it happens because someone chose it.
3. **Capabilities scale gracefully when hardware is lost.** After the Ch 14 leak, registers reduced capability through *what the crew does and doesn't do*, not through technical lament.
4. **The forensic substrate is a tool the protagonists use.** Wanjiru's chapter-load beats include forensic queries against the archive. Joel's Ch 17 work is honest engineering at laptop-class.
5. **The OSS-funding-asymmetry is not preached; it is shown.** No character explains it as a thesis. The constraint is operational: they sourced off-the-shelf because that's what they could afford. Joel says it once in Ch 1, in passing. The reader understands the rest.

## 11. Cross-references

- **Sync mechanic + Wanjiru's triage role:** see `vol-2-anchor-bridge-sync-mechanic.md`.
- **Series trajectory (centuries-scale):** see `series-arc-sunfish-trajectory.md`.
- **Chapter-by-chapter pattern assignments:** see `vol-2/CHAPTER-OUTLINE.md`.
- **Generator skill for log + diary entries:** see `.claude/skills/crew-log-style-entry/SKILL.md`.
- **Voice exemplars:** `.pao-inbox/_creative/oss-architects-voices/` (Anna mission-log fragment + Wanjiru Annex A); `.pao-inbox/_creative/forsaken-position-papers/` (Helvetia / Stefan / Working Group voices).
- **Character voice reference:** `.pao-inbox/_creative/character-sheets/`.

---

## Status

- **Locked 2026-05-05** per CO directive (sequence of brainstorming sessions in which the canon was established).
- **Pre-existing chapter drafts may not yet reflect this convention**; expect chapters drafted before this doc landed (Ch 5, Ch 2 v1) to be updated incrementally as voice-pass reaches them, or fully redrafted where structural changes are warranted.
- **No further drafts of new Vol 2 chapters should land without consulting this doc.**
