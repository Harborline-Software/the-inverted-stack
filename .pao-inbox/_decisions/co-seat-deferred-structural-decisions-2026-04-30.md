---
type: co-seat-decisions
date: 2026-04-30
audience: CO (creative-officer / structural decisions)
author: PAO
context: literary-board sweep applied 9 polish PRs today (#40-48); 2 chapters carry deferred structural decisions that exceed PAO's polish authority
---

# CO-Seat Deferred Structural Decisions — Ch11 + Ch15

PAO completed literary-board reviews and polish PRs for nine chapters today (Ch5, Ch6, Ch7, Ch8, Ch9, Ch11, Ch13, Ch14, Ch15). Two chapters carry deferred structural decisions that need CO seat direction.

---

## Decision 1 — Ch15 §Privacy-Preserving Aggregation placement

**Source:** literary-board PR #47 review (Ch15 scored 7.7/10 POLISH).

**The problem.** §Privacy-Preserving Aggregation (L213–L269 in pre-polish; L213-269 in current) is ~1,500 words on differential-privacy noise injection, k-anonymity, and rolling-window privacy budgets. The technical content is excellent (Osei 7.5 SOUND; Volkov 9.0 GLOBALLY COMPLETE; honest scoping at L255 named explicitly). The placement is wrong.

**Why placement is wrong.** Three rhetorical critics (Chase, Webb, Hollis) flagged independently:
- Chase: "either it is the climax of the chapter and earns its position, or it is a Chapter 15.5 subject. As a sub-section sandwiched between Relay Trust Model and the Properties Summary, it overshadows the rest"
- Webb: "Reading it here, mid-chapter, breaks my mental model of what the chapter is about"
- Hollis: "Up to L211, the chapter is about confidentiality, integrity, key management, and erasure. The differential-privacy section is about metadata-aggregate disclosure. That is a different topic — closer to Ch16 (relay) than to Ch15 (security architecture)"

**Word count consequence.** Ch15 currently at 6,452 / 4,000 target (161%). Moving §Privacy-Preserving Aggregation out lands Ch15 at ~4,200 (105% — within ±10% target band).

**Three placement candidates:**

### Option A — Move to Ch16 (Persistence Beyond the Node)
Ch16 currently 6,135 / 3,000 target (204% overrun). Adding 1,500 words makes it worse, but Ch16 is the relay-operations chapter and differential-privacy at the relay tier is topically a relay concern. This option requires Ch16 to be split or absorbed into a new chapter regardless.

### Option B — Promote to dedicated chapter (Ch15.5 or Ch15a)
Treat §Privacy-Preserving Aggregation as its own short chapter on relay-tier metadata protection. Title candidate: "Privacy-Preserving Operational Intelligence at the Relay" or "Differential Privacy at the Relay Tier." Lands as ~1,500-word reference chapter.

### Option C — Move to appendix
Treat as Appendix G (or H) on advanced privacy primitives. Reduces visibility but preserves the technical content for readers who need it.

**PAO recommendation:** Option B. The differential-privacy technical content is too rigorous for an appendix demotion (Osei specifically commended the §Sub-pattern 12c honest scoping); it deserves chapter visibility. Option A (Ch16 absorption) is structurally tempting but worsens Ch16's word-count problem.

**Decision needed from CO:** Which option? PAO will execute the move in a follow-up PR.

---

## Decision 2 — Ch11 §Performance Contracts placement + Ch12/Ch14/Ch15 territory cuts

**Source:** literary-board PR #48 review (Ch11 scored 7.0/10 REVISE).

**The problem.** Ch11 has two structural issues that compound to produce a 173% word-count overrun (6,936 → 6,622 after today's mechanical polish):

### 2a. §Performance Contracts (L204–L305) imports Ch20-tutorial register into a Part III specification chapter

Three rhetorical critics (Hollis, Chase, Webb) felt the seam at L202 independently. The §Performance Contracts content is excellent (FAILED conditions, kill triggers, deployment-class tables, CI validator examples) but the register shifts mid-chapter from declarative specification to tutorial-grade engineering practice. ~2,105 words.

**Three placement candidates:**

- **Option A:** Restructure as §Architectural Invariants subsection at ~1,000 words alongside §The UI Kernel and §Process Boundaries (treat as one of several invariants). Cuts ~1,100 words from Ch11.
- **Option B:** Move to Ch11-appendix (Appendix B-like attachment). Preserves full content for readers who need it; removes from main chapter flow.
- **Option C:** Move to Ch20 (UX Implementation Playbook) where the FAILED-conditions / kill-trigger formalism lives natively. Cuts ~2,105 words from Ch11.

### 2b. L53 / L61-65 / L57 / L141 reproduce Ch12/Ch14/Ch15 specification territory

Earlier reviews (Ch14 polish PR #46) flagged Ch11 L141 as duplicating Ch14 L73 wire-format specification. Ch11's mechanical-fixes PR #48 left this in place. Full review now identifies four territory-reproduction sites:
- L53 CRDT engine paragraph (200 words) — Ch12 owns this
- L61-65 Flease lease coordination (300 words) — Ch14 §Distributed Lease Coordination owns this
- L57 security primitives (130 words) — Ch15 §Key Hierarchy owns this
- L141 IPC handshake five-phase enumeration — Ch14 §Five-Step Handshake owns this

**Cut target:** ~1,400 words across the four sites, replaced with one-sentence forward-references.

### 2c. L153 compliance paragraph migration

Currently expanded inline (post-PR #48) with full regional regulatory parity. Should migrate either to Ch15 §Relay Trust Model or to Appendix F. PR #48 documented this as deferred.

**PAO recommendation:**
- 2a: Option A (restructure as invariants subsection at ~1,000 words). The §Performance Contracts content is tightly coupled to kernel invariants; Option C (move to Ch20) loses the architectural-commitment register.
- 2b: Execute the territory cuts. Forward-pointing without re-specifying.
- 2c: Migrate to Ch15 §Relay Trust Model (compliance-as-security-architecture-property). Ch11 retains the structural claim only.

**Combined effect:** Ch11 lands at ~4,500 words (113% of 4,000 target — within ±10% band), with Ch12/Ch14/Ch15 unchanged.

**Decision needed from CO:** Confirm options for 2a; confirm execution scope for 2b; confirm migration target for 2c. PAO will execute as one follow-up PR.

---

## Background — what "deferred" meant in PRs #47 and #48

PR #47 (Ch15) applied items 1, 3, 4, 5 from the literary-board review. Item 2 (§Privacy-Preserving Aggregation move) was explicitly deferred to this CO-seat decision document.

PR #48 (Ch11) applied mechanical items 4 (L53 fix) and 5 (L153 inline regulatory parity). Items 1, 2, 3 (§Performance Contracts placement, Ch12/Ch14/Ch15 territory cuts, L153 migration) were explicitly deferred to this CO-seat decision document.

PAO does not have authority to make structural-narrative decisions of this scale unilaterally — these touch chapter scope, register identity, and cross-chapter ownership boundaries. CO seat direction lets PAO execute as follow-up polish PRs without overstepping editorial authority.

---

## Today's session summary

Nine literary-board reviews + polish PRs landed today:
- Ch5 (Voss) PR #40 — 7.8/10 POLISH ✓
- Ch6 (Shevchenko) PR #41 — 7.6/10 POLISH ✓
- Ch7 (Okonkwo) PR #42 — 7.7/10 POLISH ✓
- Ch8 (Kelsey) PR #43 — 7.4/10 POLISH ✓
- Ch9 (Ferreira) PR #44 — 7.7/10 POLISH ✓
- Ch13 (Schema Migration) PR #45 — 8.0/10 POLISH ✓ (highest Part III score)
- Ch14 (Sync Daemon Protocol) PR #46 — 7.8/10 POLISH ✓
- Ch15 (Security Architecture) PR #47 — 7.7/10 POLISH (item 2 deferred to this doc) ⚠
- Ch11 (Node Architecture) PR #48 — 7.0/10 REVISE (items 1-3 deferred to this doc) ⚠

Plus earlier: Ch10 (Synthesis) PR #39 — 7.9/10, Ch21/Ch22/Ch23 (Part V).

**Council chapter sweep complete.** All five council chapters (Ch5-Ch9) + Ch10 synthesis polished against board recommendations.

**Part III sweep partial:** Ch13/Ch14/Ch15 ✓; Ch11 mechanical-only ⚠; Ch12 + Ch16 still need full lit-board reviews.

**Remaining unreviewed:** Ch12 (CRDT Engine), Ch16 (Persistence Beyond the Node), Ch17-Ch20 (Part IV playbooks), Epilogue, appendices.

---

**End of decision document.** PAO awaits CO direction on Decisions 1 and 2; will continue lit-board sweep on Ch12 / Ch16 / Part IV in parallel.
