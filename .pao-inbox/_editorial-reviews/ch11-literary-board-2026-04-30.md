---
type: literary-board-review
chapter: ch11-node-architecture
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (structural decisions), PAO (mechanical action items)
verdict: REVISE (7.0/10 board consensus - structural seam at L202 + Ch12/Ch14/Ch15 territory reproduction)
supersedes: .pao-inbox/_editorial-reviews/ch11-compression-2026-04-29.md (compression review)
---

# Literary Board Review - Ch11 (Node Architecture)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 6.5/10 | REVISE |
| Marcus Webb (CTO / Target Reader) | 7/10 | SKIM |
| Ingrid Halvorsen (Prose Editor) | 6/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 7/10 | ADEQUATE |
| Dr. Amara Osei (Academic Reviewer) | 7/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 7.5/10 | NEEDS REGIONAL CONTEXT |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 6/10 | EPISODIC |
| Sofia Reyes (Accessibility/LATAM) | 8/10 | INCLUSIVE |
| Yuki Tanaka (East Asia/APAC) | 7/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 7/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 8/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 7/10 | NEEDS CIS CONTEXT |
| **Board consensus** | **7.0/10** | **REVISE** |

## Voice register verification

Specification voice holds through first eleven sections (L1–L200). **Seam at L202**: §Performance Contracts and Main-Thread Isolation imports Ch20-tutorial register (FAILED conditions, kill triggers, deployment-class tables, CI validator examples) into structural overview chapter. Three rhetorical critics (Hollis, Chase, Webb) felt the seam independently.

## Cross-reference verification

L153 forward-references correct after PR #45 fix. Other forward-pointers (L51 Ch14, L53 Ch12, L55 Ch13, L57 Ch15, L61 Ch14, L131 Ch20, L149 Ch14, L246 Ch12, L256 Ch20, L287 Ch20, L303 Ch20) all point cleanly to chapter-owners. Problem is that Ch11 also **reproduces material those owners specify in detail.**

## Cross-chapter territory reproduction (recommend deferral)

- **L53 CRDT engine paragraph (200 words):** YDotNet/Loro provenance + three-tier resolution model. Ch12 owns this.
- **L61–L65 Flease and asymmetric partition (300 words):** full lease grant mechanics, epoch-stamped tokens. Ch14 §Distributed Lease Coordination L173–L189 owns this.
- **L57 security primitives (130 words):** key hierarchy from root through KEK to wrapped DEK. Ch15 §Key Hierarchy L54–L83 owns this.
- **L141 IPC handshake five-phase enumeration:** HELLO, CAPABILITY_NEG, ACK, DELTA_STREAM, GOSSIP_PING. Ch14 §Five-Step Handshake L54–L85 owns this - same redundancy concern flagged in Ch14 review.
- **L153 regulatory survey:** Appendix F owns this; Ch15 §Relay Trust Model owns the compliance argument.

## Strengths to preserve

- **L7–L9 opening** - one of the cleanest Part III openers in the book; "the kernel changes slowly, and domain code changes independently"
- **L21 third-party-equality commitment** - "the kernel cannot distinguish a domain block built by the node operator from one built by a vendor integration"
- **L65 trade-off naming** - "this is the architecturally accepted cost of CP positioning"
- **L83–L102 SchedulingPlugin illustrative example** - smallest example that conveys the contract
- **L131 Accessibility as Tier 1 Contract** - structural commitment, not checklist (Reyes: highest single score in any council/Part III chapter on accessibility)
- **L137 daemon-as-OS-service framing** for Lagos / rural East Africa / rural India offline-baseline markets
- **L151 relay-as-optional disclosure** - "a relay outage ... does not affect local data"
- **§Plugin Contracts L69–L104** as a whole
- **§Performance Contracts FAILED conditions / kill trigger pattern (L295–L301)** - formalism is excellent, problem is placement not content

## Priority action items

### CO-seat structural decisions (defer to follow-up PR after CO direction)

1. **§Performance Contracts placement** - keep at ~1,000 words restructured as §Architectural Invariants subsection, OR move to Ch11-appendix / new short chapter. Current placement creates register seam at L202.
2. **L153 compliance paragraph migration** - keep structural claim ("relay holds ciphertext only") in Ch11; move regulatory anchoring to Ch15 §Relay Trust Model or Appendix F.
3. **Cut Ch12/Ch14/Ch15 territory reproduction** (~1,400 words) - §Kernel Responsibilities CRDT engine detail (defer to Ch12), Flease detail (defer to Ch14), security primitives detail (defer to Ch15), L141 handshake phase enumeration (defer to Ch14).

### PAO-applicable mechanical items (this PR)

4. **Copy-edit L53 duplicated YDotNet parenthetical** - ships verbatim twice in same sentence.
5. **L153 regulatory parity additions** - until full migration decision, close the Ch5-Ch9 polish-pattern parity gap inline:
   - **Krishnamurthy:** Distinguish DIFC DPL 2020 / UAE federal 2022 / ADGM 2021; distinguish RBI (physical residency) from DPDP (consent-based); add Saudi PDPL 2021
   - **Barker:** Add NIS2 Directive Article 21 + EU Cyber Resilience Act; correct BSI / CNIL roles; Schrems II case citation form (CJEU C-311/18, 2020)
   - **Tanaka:** Distinguish Japan PIPA / Korea PIPA; add MLPS 2.0 + ISMS-P
   - **Diallo:** Add Ghana DPA 2012, ECOWAS Supplementary Act
   - **Reyes:** Add Argentina Ley 25.326
   - **Volkov:** Add Kazakhstan + Belarus localization regimes; add импортозамещение transliteration
6. **L131 accessibility paragraph split** - extract into discrete subsection; add SyncState-to-ARIA-live-region mapping (Healthy: silent; Stale: polite; ConflictPending: assertive; Offline: polite; Quarantine: assertive).
7. **L264 representative-hardware definition** - name test fleet hardware classes for the CI conformance test.

## Word-count outcome

Before polish: 6,936 words (173% of 4,000 target).

PAO-applicable mechanical items net target: ~7,050 (+114 - regulatory parity additions outpace L53 fix). Items 1-3 (CO-seat structural decisions) would land Ch11 at ~3,600–4,800 depending on §Performance Contracts disposition.

## Other findings (not priority-ordered)

- **Webb:** Cut Lagos/VSAT framing at L137 - by Ch11 reader is bought in
- **Halvorsen:** Trim parenthetical glosses where term has appeared earlier
- **Nakamura:** Distinguish ratified-vs-roadmap commitments in §Performance Contracts outside HTML comments; one paragraph on when microkernel/plugin separation does NOT pay off
- **Osei:** L63 in-chapter justification of three-tier model (don't require Ch10 reading); L212/[4] specific benchmark configuration; "limitations" sub-paragraph naming what budgets do not cover (cold start, first-load projection rebuild, post-migration replay)
- **Krishnamurthy:** L283 deployment-class table add "field-tablet (lower-end ARM)" row
- **Reyes:** L131 accessibility split into discrete subsection (combines with item 6)
- **Tanaka:** Name SIer/operations-team deployment pattern at L135 - daemon-as-OS-service is structural fit for Japanese enterprise procurement
- **Diallo:** L137 reframe intermittent connectivity as baseline not edge case; L283 add constrained-hardware deployment class; L151 explicit zero-foreign-relay operation support
- **Volkov:** L153 acknowledge state-mandated infrastructure access threat model; consider whether L137 should reference 2022 SaaS service terminations

---

**End of review.** PAO will apply mechanical items 4–7 in this polish PR. CO-seat structural decisions (items 1–3) require direction before follow-up restructuring PR.
