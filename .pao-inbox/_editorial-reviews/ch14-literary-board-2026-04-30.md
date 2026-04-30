---
type: literary-board-review
chapter: ch14-sync-daemon-protocol
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.8/10 board consensus — wire-format table is the load-bearing artifact)
---

# Literary Board Review — Ch14 (Sync Daemon Protocol)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 8/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 8/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 8/10 | GLOBALLY POSITIONED |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 8/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 7/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 8/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 8/10 | NEEDS CIS CONTEXT |
| **Board consensus** | **7.8/10** | **POLISH** |

## Voice register verification

**SPECIFICATION VOICE — CONFIRMED.** Holds across protocol mechanics (L52–L237) and protocol-invariants close (L251–L261). Two passages bend toward council/advocacy voice: regional-deployment context wedged into Tier 3 at L46, regulatory enumeration at L147 (11-sentence Part-II-style argument inside Part III). Both content-correct; voice friction is structural placement, not register failure.

## Cross-reference verification

**ALL FORWARD-POINTERS RESOLVE CLEANLY:**
- Ch6 L88 (CAPABILITY_NEG schema-version detection) → resolves at Ch14 L71 + L91
- Ch6 L155 (schema-version compatibility at CAPABILITY_NEG) → resolves at Ch14 L71 + `SCHEMA_VERSION_INCOMPATIBLE` rejection code
- Ch7 L123 (relay-as-ciphertext-only / state-mandated infrastructure access) → resolves at L46 + L147
- Ch13 L94 (schema-graph resolution at handshake) → resolves at L71 + L91
- Ch10 L96 (state-mandated data access) → resolves at L147

## Cross-chapter consistency

**Ch14 IS THE CANONICAL HOME** for HELLO/CAPABILITY_NEG wire format. Upstream redundancy concern: **Ch11 L141** reproduces the same five-phase handshake + signature details. Recommendation flagged for follow-up — Ch11 should reference Ch14 rather than reproduce the wire format. Ch12, Ch13, Ch15 are clean (no wire-format duplication).

## Strengths to preserve

- **L9 opening paragraph** — three short subject-verb sentences + closing constraint; best opener in Part III
- **L17 "Picture the application restarting…" anaphora triplet** + closing chiasmus "The application can fail without the network failing with it"
- **L46 Tier 3 as primary operational tier** — the architectural priority inversion several critics named as strongest in any reference-architecture chapter
- **L57 handshake sequence diagram + L71–L80 five-step handshake spec** — specification-complete
- **L91 wire-format table** — field-level types, required/optional marking, signature scope, CBOR canonical, length-prefixing, replay window. The artifact an engineer can stub from
- **L147 state-mandated data access framing** — regionally accurate, politically tactful, technically correct
- **L161 endpoint-compromise consequence** — Nakamura positioning sentence
- **L187 lease-blocked never silently queued** — decisive trade-off
- **L247 closing chiasmus** — "The application can fail; the network keeps its promises"
- **L251 Protocol Invariants section** — Hollis: rhetorical climax
- **L261 no-trusted-network-mode sentence** — structural assurance

## Priority PAO action items (in priority order)

### 1. Split L147 regulatory enumeration paragraph + add missing regional citations in body

Currently 11 sentences / ~320 words. Split at "A distinct threat model operates in parallel…" boundary. Add to body text:
- **Volkov:** Federal Law 242-FZ + Kazakhstan + Belarus localization; импортозамещение Russian-language parenthetical
- **Tanaka:** Japan APPI 2022 + South Korea PIPA + China PIPL + MLPS 2.0 (currently named in Ch6/Ch10 but not Ch14)
- **Diallo:** NDPR + POPIA + Kenya DPA (currently in Appendix F only)
- **Krishnamurthy:** DIFC vs ADGM vs UAE-federal jurisdictional distinction
- **Barker:** Formal CJEU case citation for Schrems II — *Data Protection Commissioner v. Facebook Ireland Limited*, C-311/18, 2020

### 2. Extract L46 regional deployment-context list into separate paragraph

Restores Tier 3 to protocol-mechanics specification voice. Deployment-context note names rural India / rural Sub-Saharan Africa / rural Latin America / GCC construction sites in one sentence. Add African fintech precedent (M-PESA / MTN MoMo / FarmerLine) one-clause; Hindi/Arabic-first deployment one-clause; explicit relay vendor-independence statement (Barker).

### 3. Close formal-correctness gaps at L171 + L219

- **L171:** Add one sentence referencing epoch-stamped lease tokens (Ch6 §Flease split-write proof / Ch11) for dual-quorum partition-failure-mode resolution
- **L219:** Cite SWIM (Das, Gupta, Motivala, DSN 2002) or ϕ-accrual (Hayashibara) as literature the 3/5 missed-interval threshold draws from

### 4. Specify L159 wire behavior of field-level subscription stripping

Currently claims "daemon strips operations for out-of-scope fields before transmitting" without specifying wire mechanism. Pick: omit-from-delta, tombstone-marker, or redacted-placeholder. Plus typed-rejection-code consequence note for accessibility (Reyes) + one-line assistive-technology-during-connectivity-loss claim.

### 5. Separate L85 disclosure from specification + name L207 defaults

- **L85:** Pull Wave-2.6 integration disclosure ("delta apply-back is the Wave 2.6 integration work") into separate paragraph; do not embed inside convergence claim
- **L207:** Name default values for `base`, `max_seconds`, `jitter_range` in backoff equation. "Configurable per deployment" without defaults forces implementers to invent their own

## Other findings (not priority-ordered)

- **Halvorsen:** L46 56-word parenthetical needs sentence break; L147 11-sentence paragraph needs split (combines with item 1); add one snap-sentence at L165 or L213
- **Webb:** Optional pointer at L267 naming what Ch15 covers (attestation cryptography, key wrapping); name what specifically depends on it
- **Nakamura:** L143 add SaaS-counterfactual sentence — name how SaaS sync layers run subscription filtering at API gateway vs daemon's send-tier filter
- **Osei:** L97 canonical CBOR encoding rule (RFC 8949 §3.9) implied not stated; L133 name "uniform random peer selection" explicitly
- **Krishnamurthy:** L267 Related Specifications could point to Appendix F per-jurisdiction matrix
- **Hollis:** After L9 add one sentence framing chapter's dual register (protocol spec + threat-closure rationale); consider letting Related Specifications close the chapter
- **Reyes:** L75 one sentence naming consequence of typed reason codes for assistive-tech state announcements; L9 or L141 one sentence on local-first accessibility advantage
- **Tanaka:** Optional MLPS 2.0 categorization mention at L267 for China-deployment audiences
- **Barker:** L46 explicit relay vendor-independence statement (combines with item 2); L171 partition-failure mode (combines with item 3)
- **Diallo:** L9-L23 or L197 outbound-buffer durability across power events sentence (reference Ch6 L120 / Ch12)

## Word-count outcome target

Before polish: 3,809 words (109% of 3,500 target).

After priority-5 polish target: ~3,750–3,900 words (107–112%). Net-zero or slight reduction; some items add precision while others trim. Hold within ±10% of target.

---

**End of review.** PAO will apply priority items 1–5 in a polish PR. No voice-pass required — Part III specification register holds.
