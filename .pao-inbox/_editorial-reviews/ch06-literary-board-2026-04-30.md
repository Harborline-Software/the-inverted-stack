---
type: literary-board-review
chapter: ch06-distributed-systems-lens
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.6/10 board consensus — solid council-chapter, slightly below Ch5 exemplar)
---

# Literary Board Review — Ch06 (The Distributed Systems Lens)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 7.5/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8.5/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 8.5/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 7/10 | NEEDS REGIONAL CONTEXT |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 8.5/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 6/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8.5/10 | RIGOROUS |
| Amina Diallo (African Markets) | 6.5/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 8/10 | NEEDS CIS CONTEXT |
| **Board consensus** | **7.6/10** | **POLISH** |

## QC-9 verification

**PASSES.** Ch6 delivers the two-act structure cleanly:
- §Act 1: Round 1 — Two Correctness Failures (L20–53) with explicit BLOCK verdict at L48–52
- §What Changed Between Rounds (L56–94) — the narrative gap; the chapter's structural hinge
- §Act 2: Round 2 — Surviving the Correctness Audit (L98–144) with PROCEED WITH CONDITIONS verdict at L134

The Round 1 → Round 2 score arc is set up at L22 (R1 = 7.1, BLOCK) and resolved at L100 (R2 = 6.8, PROCEED WITH CONDITIONS). The -0.3 narrative is established at L100 with the explanation that "A reviewer who finds a Round 2 architecture more objectionable than Round 1 is not saying it got worse. He is saying it became precise enough to critique at a deeper level."

**Ch10 reuse verification: PASSES with caveat.** Ch10 line 58 reuses the Shevchenko -0.3 narrative with the punchier formulation: "His score dropped. That did not signal a failure. It signaled the opposite. He entered Round 2 with his two blocking issues resolved and raised new technical concerns... Shevchenko's score dropped because he took the architecture more seriously in Round 2, not less." Ch10's reuse is sharper than Ch6's own setup. **Recommend tightening Ch6 L100 to its own equivalent punchline so the source chapter owns the line.**

## Strengths to preserve

- **L12 Shevchenko opener** — character through past action, "personally debugged five CRDT deployments that diverged in ways the academic literature said were impossible"; comparable to Ch5's Voss opener
- **L34 "He was right"** — three-word concession that establishes author trust before the resolution arrives
- **L37–46 split-write thought experiment** — architecture dramatized as scenario; reader runs it themselves
- **L44 "the user trusts that the system will not quietly lie to them"** — moral stake of CP/AP distinction in ten words
- **L86 Schrems II treatment** — second-best Schrems II passage in the manuscript; Tier 3 = direct structural answer
- **L100 Round 2 score-drop framing** — load-bearing for Ch10 reuse; tighten but preserve the move
- **L104 relay-as-Flease-quorum-participant** — small architectural elegance; "eliminates the threshold problem"
- **L120 CRDT-store-as-durable-outbound-buffer** — "the correct design for a local-first architecture where offline duration is unbounded"
- **L126–132 Byzantine-failure-by-software-bug** — most under-cited risk in CRDT systems, named precisely
- **L150–157 Non-Negotiable Distributed Systems Checklist** — six-bullet ADR-pasteable artifact
- **L161, L189 "Convergence is not correctness"** — the chapter's usable axiom
- **L187 anaphora ("The split-write window arrives... The GC horizon arrives... The corrupt operation sequence arrives...")** — earns its repetition; each instance carries new information
- **L82, L183 mermaid alt-text prose** — correct WCAG practice; preserve pattern

## Priority PAO action items (in priority order)

### 1. Fix L94 duplicated YDotNet parenthetical and break the bracketed sentence

The parenthetical "(the .NET CRDT engine port of Yjs ([github.com/yjs/yjs](https://github.com/yjs/yjs), the JavaScript CRDT library) via Rust FFI (Foreign Function Interface))" appears twice consecutively in L94. Immediate copy-edit. While fixing, break the 47-word nested-parenthesis sentence into two sentences. This is the chapter's most visible defect and must be the first PR commit.

### 2. Close regional regulatory parity gap at L86

Apply the Ch5 polish pattern. Add to the L86 regulatory paragraph:
- **Diallo (Africa):** NDPR, POPIA, Kenya DPA
- **Reyes (LATAM):** Brazil LGPD, Mexico LFPDPPP, Colombia Ley 1581
- **Tanaka (APAC):** Japan APPI (2022), MLPS 2.0; distinguish Japan APPI from Korea PIPA
- **Krishnamurthy (Dubai):** DIFC DPL
- **Volkov (CIS):** Federal Law 242-FZ
- **Barker (EU):** NIS2 Directive

### 3. Tighten L100 Round-2-score-drop punchline

Sharpen to a one-sentence formulation matching or exceeding Ch10 line 58's punch ("His score dropped. That did not signal a failure. It signaled the opposite"). Ch6 is the source chapter for this rhetorical move; it should own the line.

### 4. Reframe reconnection-storm and durable-outbound-buffer passages — global baseline, not edge case

Apply Ch5's power-interruption-durability reframing pattern. L92 (reconnection storm) and L120 (CRDT-store-as-buffer) handle the architecture correctly but write it as exotic.
- L92 — name daily load-shed cycles in Lagos / Bogotá tier-2 / Mumbai tier-2 as the baseline pattern, relay outage as one variant
- L120 — connect the unbounded-offline-duration property to extended-outage operating reality

### 5. Add state-mandated-infrastructure-access threat model and managed-CP-database steelman

Two ~80-word additions, both in §The Principle: Convergence Is Not Correctness:
- **State-mandated access (Volkov, Krishnamurthy):** pull from Ch10 line 96 phrasing — "state-mandated access at the infrastructure layer" — and connect to the architecture's local-keys/no-relay-plaintext property.
- **Managed-CP-database steelman (Nakamura, Webb):** name Spanner / Fauna / CockroachDB and explain why the data-sovereignty constraint Part I established does not permit delegation to a managed CP system.

## Voice-pass status

**Confirmed voice-passed (lencioni voice, per `chapters/voice-plan.yaml`).** Shevchenko-as-character is established through specific past action (L12); council deliberation reads as scene rather than catalog. Halvorsen's score of 7 reflects paragraph-architecture and copy-edit issues (item 1, item 4), not voice-pass gaps. **No voice re-pass needed.**

## Other findings (not priority-ordered)

- **Chase:** GC mermaid at L62–80 is decorative — prose at L60 does the teaching; either commit harder to the diagram or cut it
- **Webb:** Add one sentence after L132 naming a real-world Yjs/Automerge example of the bug-propagation failure mode
- **Halvorsen:** Vary cadence — one of the four bold-led paragraphs in §What Changed Between Rounds should break formation; cut "slowly and without flourish" decoration at L12; break L165 sentence into two
- **Nakamura:** Cut three-restatement closing at L185–187 to one
- **Osei:** Footnote at L126 distinguishing classical Byzantine failure (Lamport 1982) from contemporary BFT-consensus usage; footnote at L189 grounding "convergence is not correctness" in Saltzer-Schroeder mechanism/policy separation; add non-commutativity-under-merge clause at L165
- **Krishnamurthy:** Name 90-day-tier vs. RBI 8-10 year audit-retention binding explicitly; add SI-partner-led linearizable-operation enumeration acknowledgment at L106
- **Hollis:** Mark §What Changed Between Rounds with the two-line section break Ch5 uses
- **Reyes:** Add one sentence on local-first accessibility property in §The Principle section
- **Tanaka:** Verify Ch14 specification completeness for the CAPABILITY_NEG cross-reference at L88
- **Barker:** Name cryptographic erasure technique when discussing GDPR Article 17 satisfaction at L86; footnote crash-failure model at L90
- **Diallo:** Add African SI-led implementer profile acknowledgment at L106
- **Volkov:** Add импортозамещение reference (second mention in manuscript)

## Word-count outcome target

Before polish: 4,002 words (114% of 3,500 target).

After priority-5 polish target: ~4,000 words landing if items 1+3 (compression) offset items 2+4+5 (additions).

---

**End of review.** PAO will apply priority items 1–5 in a polish PR; voice-pass items wait for CO Stage 6. Ch6 is the model for Ch7-Ch9 polish.
