---
type: literary-board-review
chapter: ch13-schema-migration-evolution
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (8.0/10 board consensus - strongest Part III specification chapter)
---

# Literary Board Review - Ch13 (Schema Migration and Evolution)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 8/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 9/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 8/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 8/10 | GLOBALLY POSITIONED |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 8/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 7/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 8/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 9/10 | UNIVERSALLY RELEVANT |
| Aleksei Volkov (CIS/Eastern Europe) | 8/10 | NEEDS CIS CONTEXT |
| **Board consensus** | **8.0/10** | **POLISH** |

## Voice register verification

**SPECIFICATION VOICE HOLDS.** No bleed into council narrative voice (no scene work, no R1/R2 act structure) or tutorial voice (no "you" address). Single localized wobble at L173–L188 (runbook headings tipping toward imperative tutorial register) - easy to fix in polish. Ch17 will own the tutorial walk-through; Ch13 specifies the surface Ch17 references.

## Cross-reference verification

- **Ch6 CAPABILITY_NEG schema-version negotiation** (Ch6 L88, L155) → **RESOLVES CLEANLY** at Ch13 L94. Wire format owned by Ch14 L73; schema-graph resolution owned by Ch13 L94. Clean ownership split.
- **Ch7 GDPR Article 17 crypto-shredding tension** (Ch7 L155) → **RESOLVES PARTIALLY**. Ch13 L147 defers to Ch15 for mechanism (correct ownership). Ch11 L153 incorrectly forward-points to Ch13 for crypto-shredding - fix to point to Ch15.

## Cross-chapter consistency

Boundaries are clean. Ch11 owns ISchemaVersion (referenced at L48); Ch12 owns CRDT operations + schema-validation gate at store entry; Ch14 owns HELLO/CAPABILITY_NEG wire format; Ch15 owns crypto-shredding mechanism. Ch13 builds on each without duplication.

## Strengths to preserve

- **L10 opening scenario** - cleanest specification-chapter opening in the book; "four people on the latest release, six on the previous release, and two on a release that is two minor versions old - one of whom has not connected to the network in six weeks"
- **L12 three-mechanism map** - reader has the spine of the chapter before reading another line
- **L131–L133 Couch Device Problem framing** - "routine operational condition... typical rather than pathological" with regional catalog (Sub-Saharan African / rural Indian BFSI / rural Brazilian and Mexican / GCC). Diallo: strongest single sentence in the chapter for the African market.
- **L137 quarantined-offline-edits handling** - "Automatic merging of arbitrarily old operations across an epoch boundary is not safe, and the architecture does not attempt it"
- **L193 "What Cannot Be Migrated" section** - negative-space discipline that earns reader trust permanently
- **L88 Cambria attribution** - honest positioning of reference design vs. current implementation
- **L147 Schrems II citation** - strongest single compliance argument for European market in the entire book

## Priority PAO action items (in priority order)

### 1. Split L147 into two subsections + close regulatory parity gap

Currently a 200-word paragraph welding GDPR Article 30 + Schrems II + 242-FZ + DIFC + DPDP + RBI + lens-bidirectionality runtime check together. Split into:
- **"Compliance properties of schema history"** - regulatory anchors. Existing: GDPR Article 30, Schrems II, 242-FZ, DIFC DPL, DPDP+RBI. Add per Ch5–Ch9 polish pattern:
  - **Tanaka:** Japan APPI 2022, South Korea PIPA, China PIPL, MLPS 2.0
  - **Diallo:** NDPR (re-enacted 2023), POPIA, Kenya DPA 2019
  - **Volkov:** Kazakhstan and Belarus parallels alongside 242-FZ
  - **Barker:** Schrems II case citation as CJEU C-311/18
  - **Krishnamurthy:** RBI 2018 BFSI data localization circular sentence specifically connecting archival epoch stream retention
- **"Lens bidirectionality runtime check"** - technical assertion as separate subsection

### 2. Specify epoch-quorum-stall recovery + add split-brain row

Webb: what evidence triggers administrator override of quorum wait when peers are permanently offline-but-not-decommissioned, and what audit trail the override produces. Add row to L208 failure-modes table for "Epoch coordinator role transfer attempted while quorum partition exists" - split-brain risk under role transfer is real and not currently addressed.

### 3. Add upcaster/lens distinction + lens-composition lemma + SaaS-comparison steelman

- **Osei:** One paragraph distinguishing upcasters (forward-only, applied on read of the local event log) from lenses (bidirectional, applied on the wire between peers); state lens-composition lemma where L86 currently asserts version distance is performance-not-correctness
- **Nakamura:** Add SaaS-comparison steelman paragraph between L10 and L12 - name the alternative ("schedule a coordinated upgrade window") and explain why the local-first constraint forecloses it

### 4. Rephrase runbook step headings at L173–L188

Per Hollis: from imperative ("Announce", "Deploy", "Open expand phase") to specification register ("Announce phase", "Lens deployment", "Expand phase open"). Preserves Part III/Part IV register boundary that Ch17 will rely on.

### 5. Fix cross-reference asymmetry at Ch11 L153

Ch11 L153 forward-points to Ch13 for "crypto-shredding at the storage layer" but Ch13 L147 defers to Ch15. Update Ch11 L153 to point to Ch13 for stream compaction and to Ch15 for crypto-shredding. Add Schrems II case citation (CJEU C-311/18) to Ch13 reference list (Barker audit-acceptability requirement).

## Other findings (not priority-ordered)

- **Chase:** L36 compatibility-window prose, L64 filler sentence, L88 Cambria paragraph trim opportunities; audit L37/L133 catalog duplication (one use only)
- **Halvorsen:** L20 "schema vN" repetition - try "Node A has upgraded. Node B has not."; break L127 into three paragraphs along its three controlling ideas
- **Nakamura:** Strengthen L42 contract-phase justification with one-line reason no soft mode exists
- **Reyes:** One sentence in L137 on quarantine-resolution UI as accessibility-critical surface; one sentence in runbook (L173+) on administrator-console accessibility obligations under EN 301 549 / Section 508
- **Tanaka:** Optional sentence on SIer-mediated deployments (Japan, Korea) where epoch coordinator role is held by SIer's deployment team
- **Barker:** Specify whether non-bidirectional lens registration permits any degraded-mode boot or whether startup halt is unconditional
- **Volkov:** One sentence in L147 noting local-only archival property addresses state-mandated-infrastructure-access threat model specified in Ch15 (pointer, not duplication)

## Word-count outcome target

Before polish: 3,857 words (110% of 3,500 target).

After priority-5 polish target: 3,550 words (101% of target).

~250–350 words compressible (Chase identified candidates) without losing structural strengths. Regional regulatory parity additions (~100 words) recover some of the cuts. Net: lands at ~3,550–3,700.

---

**End of review.** PAO will apply priority items 1–5 in a polish PR. No voice-pass required - Part III specification register holds throughout (single localized wobble in item 4 fixes voice-register at the same time).
