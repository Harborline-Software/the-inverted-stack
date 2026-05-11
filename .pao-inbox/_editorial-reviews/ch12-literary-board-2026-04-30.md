---
type: literary-board-review
chapter: ch12-crdt-engine-data-layer
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.5/10 board consensus — strongest double-entry-ledger sub-chapter in Part III)
supersedes: .pao-inbox/_editorial-reviews/ch12-compression-2026-04-29.md (compression-only review)
---

# Literary Board Review — Ch12 (CRDT Engine and Data Layer)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 8/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 8/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 7/10 | NEEDS REGIONAL CONTEXT |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 8/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 6/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 9/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 7/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 7/10 | NEEDS CIS CONTEXT |
| **Board consensus** | **7.5/10** | **POLISH** |

## Voice register verification

**SPECIFICATION VOICE HOLDS THROUGHOUT.** No lapses into Part I narrative or Part IV tutorial register. L10 opening is most rhetorically active passage and is appropriate for chapter-opener; rest of chapter sustains spec register without slipping.

## Cross-reference verification

- **Ch11 L53 reproduces ~200 words** of YDotNet/Loro/StubCrdtEngine territory that Ch12 L70–80 owns authoritatively. Recommendation: compress Ch11 L53 to one-sentence forward-reference (deferred per CO-seat decisions doc).
- **Ch13 L131, L137** reference Ch12 correctly. Clean.
- **Ch15 L131-141** owns crypto-shredding; Ch12 L150 forward-references. Boundary clean.
- **Ch16 L20, L208** forward-reference Ch12 storage + GC. Boundary clean.
- **Ch20 L28, L54, L75** forward-reference Ch12 AP/CP classification. Boundary clean.

**DEFECT FOUND:** Same duplicated YDotNet parenthetical artifact (the one fixed today in Ch11 PR #48) appears in:
- `vol-1/front-matter/preface.md` L41
- `vol-1/appendices/appendix-a-sync-daemon-wire-protocol.md` L123

These need a separate cleanup PR.

## Cross-chapter consistency

Ch12 owns: ICrdtEngine + YDotNet/Loro/Stub provenance, AP/CP positioning, three-tier GC, five-layer storage, double-entry ledger, posting engine. No redundant specification of Ch13/Ch14/Ch15 territory.

Soft overlap: **Stale Peer Recovery Protocol (L128–140)** specifies sync-protocol behavior arguably belonging in Ch14. Hollis, Webb, prior compression review converge on relocate-to-Ch14.

## Strengths to preserve

- **L10 opening** — three-sentence ascending-stakes lead earns the chapter
- **L18 commutativity/associativity/idempotency triad** — mathematically correct framing
- **L52–58 AP/CP positioning table** — load-bearing reference artifact
- **L74 "CRDT document is a live working surface. Append-only event log is the source of truth"**
- **L80 Automerge exclusion** — Nakamura: model of intellectually honest competitive positioning
- **L112 operator-cost honesty** — "AckVector maintenance, peer-staleness window administration..."
- **L126 named-deployment list** — GCC construction, rural Indian BFSI, Sub-Saharan African field ops as operational baselines
- **L148 Schrems II citation [5]** correct and complete (CJEU C-311/18, 2020)
- **L156–208 double-entry ledger sub-chapter** — Webb: "single best section"
- **L231 Layer 2 durability + load-shedding framing** — Diallo: strongest African-markets signal
- **L243–254 Failure Modes table** — Hollis: right closing artifact
- **L258–268 Sunfish Package Reference table** — Tanaka SIer-readiness signal

## Priority PAO action items (in priority order)

### 1. Close regional regulatory parity gap at L148

Per Ch5–Ch9 polish pattern. Six critics flagged independently (Krishnamurthy, Reyes, Tanaka, Barker, Diallo, Volkov):
- Add UAE Federal DPL 2021 + ADGM 2021 alongside DIFC DPL 2020
- Name RBI 2018 BFSI data localization circular specifically (not just "RBI")
- Saudi PDPL 2021
- Argentina Ley 25.326 + Colombia Ley 1581
- Kenya DPA 2019, Ghana DPA 2012, ECOWAS Supplementary Act
- Kazakhstan PDPL + Belarus alongside 242-FZ
- Distinguish Japan APPI from China PIPL from South Korea PIPA + ISMS-P
- Add MLPS 2.0 (China cybersecurity classification)
- BSI C5 + NIS2 Directive + EU Cyber Resilience Act
- Expand "GDPR Article 30" to also include Articles 28 (processor obligations) + 32 (security of processing)
- Add импортозамещение naming (Russian-language transliteration)

### 2. Move Stale Peer Recovery Protocol (L128–140, ~440 words) to Ch14

Sync-daemon territory belonging in Ch14. Resolves word-count overage and improves cross-chapter boundary discipline. Replace with one-paragraph forward reference.

### 3. Cut L20 redundant restatement + tighten L78 (Loro) + L112 (operational-cost list)

~130 words mechanical compression with no editorial judgment needed.

### 4. Add foundational CRDT GC citation + state-based vs operation-based CRDT distinction at L18

Osei: cite Almeida/Baquero on bounded version vectors; one-clause acknowledgment that Yjs/Loro are operation-based at runtime with state-based snapshots.

### 5. Manuscript-wide cleanup — fix duplicated YDotNet parenthetical in preface.md L41 + appendix-a L123

Same artifact today's Ch11 PR #48 fixed. Follow-up PR scope.

## Other findings (not priority-ordered)

- **Webb:** Cut L18-28 data-layer-types primer by ~40% (over-served for audience)
- **Halvorsen:** Audit acronym expansions chapter-wide (one expansion per part, not per chapter)
- **Nakamura:** One paragraph naming SaaS-database alternative explicitly (PostgreSQL + logical replication) and what local-first complexity buys; steelman "this is just NoSQL with extra steps"
- **Reyes:** Add LATAM regions to L126 named-deployment list (interior Mato Grosso, Amazonas, Chihuahua, Sonora); one sentence connecting offline-first guarantee to assistive-tech continuity
- **Tanaka:** Verify Appendix F per-regime mapping includes APPI cabinet guidelines, MLPS 2.0 categorization, ISMS-P certification
- **Barker:** Schrems II citation [5] correct; verify it's only direct citation needed (Article 17 forward-references to Ch15 — clean)
- **Diallo:** Reference M-PESA or MTN MoMo as African precedent for offline-first architecture in financial services (one sentence)
- **Volkov:** Add Yandex Cloud or VK Cloud as named S3-compatible providers in L233 example list

## Word-count outcome target

Before polish: 5,316 words (133% of 4,000 target).
After priority-5 polish target: 4,400–4,800 (110–120%) — same band as Ch13/Ch14/Ch15 post-polish.

Compression avenues:
- Item 2 (Stale Peer Recovery → Ch14): -440 words → 4,876
- Item 3 (L20/L78/L112 cuts): -130 words → 4,746
- Item 1 (regulatory parity additions): +250 words → 4,996
- Item 4 (Osei citation + clarification): +20 words → 5,016
- Net: lands at ~5,000 (125%) with full items applied; ~4,500 (113%) if Stale Peer Recovery actually moves out

---

**End of review.** PAO will apply priority items 1, 3, 4 in this polish PR. Item 2 (Stale Peer Recovery → Ch14) deferred to follow-up because it requires writing new content in Ch14. Item 5 (preface/appendix-a duplicate fix) deferred to a manuscript-wide cleanup PR.
