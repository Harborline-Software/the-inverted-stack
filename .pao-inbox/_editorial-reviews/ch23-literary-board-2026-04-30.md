---
type: literary-board-review
chapter: ch23-endpoint-collaborator-ops
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (6.7/10 board consensus)
---

# Literary Board Review — Ch23 (Endpoint, Collaborator, and Custody Operations)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 7/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 6/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 8/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 6/10 | NEEDS REGIONAL CONTEXT |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 8/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 5/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 6/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 5/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 5/10 | NEEDS CIS CONTEXT |
| **Board consensus** | **6.7/10** | **POLISH** |

## Strengths to preserve

- **§47a protected/not-protected/residual-risk table** (lines 194–200) — Webb, Nakamura, Osei, Barker independently named it as the chapter's strongest single artifact.
- **Honesty disclosures** (lines 53, 90, 217, 223, 243, 304, 317) — British-pragmatic + German-rigour test passes; do not soften.
- **Chapter chapeau** (lines 12–14) — macro-narrative pivot lands; Ch22 ↔ Ch23 pairing reads natural, not arbitrary.
- **Five-fold structural pattern** (primitive → sub-patterns → FAILED conditions → kill trigger) — form-stability across sections is the right specification-voice scaffolding.
- **Yjs/Loro identifier-collision argument** (lines 157–159) + **max-register CRDT framing** (lines 377–380) — Osei: technically sound; structural-defense argument is the right framing.
- **Dashcam scenario opener** at line 262 — regionally portable, narratively effective; use as model for §Offline Node opener rather than removing.
- **Three named cadences** Halvorsen flagged: line 90 ("does not claim to delete those bytes"), 184–188 (network-vs-endpoint adversary antithesis), 349 ("logbook with extra ceremony").
- **OAuth/OCSP/CRL/eIDAS/RFC-3161/Crosby-Wallach/CT citation chain** — analyst-grade prior-art positioning.
- **Sub-pattern numbering** (45a–f, 47a–f, 9a–c, 10a–e) — operationally useful for security-review reference.

## Priority PAO action items (in priority order)

### 1. Extend regulatory citations to global parity

8 critics flagged the same gap from different regions (same as Ch22). Add to existing US/EU citations:
- Krishnamurthy: DIFC DPL 2020 + India DPDP + RBI circular
- Reyes: Brazil LGPD + Mexico LFPDPPP
- Tanaka: Japan PIPA + China PIPL + MLPS 2.0 + South Korea PIPA
- Barker: **Schrems II** (CJEU C-311/18) — strongest European compliance lever, missing from chapter
- Diallo: NDPR + POPIA + Kenya DPA
- Volkov: Federal Law 242-FZ + CIS analogues

Locations: trustee-residency-equivalent paragraphs around lines 130, 167, 362.

### 2. Name the 2022 SaaS service terminations as case study

Volkov's flag — chapter's central thesis (vendor dependency) has its largest documented demonstration in 2022 CIS-region service terminations; chapter does not reference it. Add callout in §47f or chapter chapeau. (Same as Ch22 polish item 4.)

### 3. Strengthen openers + add chapter-level closer

Chase, Webb, Hollis converge:
- §Offline Node Revocation (line 18) opens at mechanism rather than scenario; promote dashcam-style scenic register
- Chapter ends without returning to the macro-thesis (line 414 ends on §10's FAILED conditions); add a 60–100-word closer that hands off to next chapter

### 4. Tighten 3 Osei-flagged claims + lead §10a with contrast

- Line 138: OCSP/CRL "same trade-off" elides synchronous-validation difference; soften to "similar trade-off"
- Line 207: "substantially better field record" undocumented; either cite or soften to "have not accumulated a comparable academic-attack record to date"
- Line 381: "principal novelty" overstated (max-register itself is not new — Roh et al., Shapiro et al.); restate precisely as "the application of max-register to a security-metadata field with delivery-side access-control re-evaluation under partial replication"
- Lead §10a with the Purview/Macie/DLP contrast (Webb + Nakamura concur)

### 5. Add accessibility property + state-access threat model

- Reyes: name once that the architecture preserves assistive-technology operation across connectivity loss because the local data source never disappears
- Volkov: name state-mandated infrastructure access as a distinct threat model in §47a, identify which mechanisms address it (E2EE with local key management, no relay plaintext access)

## Voice-pass-pending items (CO seat — Stage 6, not PAO-actionable)

- **§Collaborator Revocation** — extension #45 awaits human anecdote at departure-moment scene + Sinek calibration
- **§Endpoint Compromise** — extension #47 voice-pass-pending
- **§Chain-of-Custody** — extension #9 voice-pass-pending
- **§Event-Triggered Re-classification** — extension #10 voice-pass-pending

Halvorsen's score of 6 reflects voice-pass gap; structural craft beneath is sound.

## Other findings (not priority-ordered)

- **Chase:** chapter title ("Endpoint, Collaborator, and Custody Operations") doesn't include re-classification (5th section); consider unifying frame ("External-Trigger Operations"). Comment at line 5 says "Target ~7,000 words" but live count ~8,581 — reconcile.
- **Webb:** §10e (Schema-evolution non-interaction) is six lines saying "this doesn't interact with that" — could be footnote.
- **Halvorsen:** Receipt-fields enumeration (lines 100, 165, 297) → bulleted breakouts where >4 items. Split §10a paragraph (lines 374–380) into three.
- **Nakamura:** Add footnote to "principal novelty" claim naming closest prior work + gap. Add paragraph in §45e acknowledging closest prior partition-work in distributed systems literature.
- **Krishnamurthy:** §47d MDM list (Intune/Jamf/Google) needs SOTI MobiControl + IBM MaaS360 for GCC. §9c LADOT-MDS naming: add UAE Central Bank/SAMA regulatory streams.
- **Hollis:** §Offline Node opener vs §Chain-of-Custody opener register-uniformity. Audit-trail composition cross-references (167, 360, 405) could be elevated from instruction to analytical observation.
- **Reyes:** Acknowledge intermittent connectivity is baseline (not edge case) for major LATAM markets in §Offline Node Revocation.
- **Tanaka:** Generalize §9c's LADOT-MDS to category ("regulatory streaming feeds — LADOT-MDS in US, METI's connected-vehicle spec in Japan, etc."). In §45f or §9b, note audit-trail framing satisfies SIer-mediated procurement requirements.
- **Barker:** Add German BSI cloud-security requirements in §47b. Reference EU Trust List of QTSPs in §9b.
- **Diallo:** Reframe §Offline Node Revocation: offline windows are baseline operating cadence for African field operations, not edge case. §47b acknowledge lower-tier-Android fleets without hardware enclaves are typical in Global South.
- **Volkov:** Acknowledge import substitution (импортозамещение) requirements alignment.

## Note on scope

The board reviewed the post-Ch23-split chapter (5 sections relocated from original Ch22). The voice-pass-pending sections are the same ones that made Ch22 unmanageable pre-split — the Phase 4 prune (deferred to post-voice-pass) will land here when #45/#47/#9/#10 voice-pass completes.

The 3 Mermaid diagrams (Offline reconnect sequence + Collaborator departure trust boundary + Chain-of-Custody multi-party transfer) earned their place per the board's structural review.

---

**End of review.** PAO will apply priority items 1–5 in a polish PR; voice-pass items wait for CO Stage 6.
