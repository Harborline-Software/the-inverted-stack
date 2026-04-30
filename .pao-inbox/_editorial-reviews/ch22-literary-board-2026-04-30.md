---
type: literary-board-review
chapter: ch22-security-operations
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.5/10 board consensus)
---

# Literary Board Review — Ch22 (Key Lifecycle Operations)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 7.5/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8.0/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7.0/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8.0/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 8.0/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 8.0/10 | GLOBALLY POSITIONED |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 7.0/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 6.5/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7.0/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8.0/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 7.0/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 8.5/10 | NEEDS CIS CONTEXT (mild) |
| **Board consensus** | **7.5/10** | **POLISH** |

## Strengths to preserve

- **Uncle Charlie iPhone passage** (lines 53–59) — rhetorical centerpiece of the chapter and possibly of Part V. Voice-pass-complete; do not edit during polish beyond grammar.
- **Deployment-class table** (lines 79–83) + Mermaid flowchart that mirrors it — both earn their place; redundancy is intentional cognitive-path coverage.
- **§Boundaries six-failure-mode discipline** (lines 200–214) — most honest passage; silent-decay quarterly-liveness-ping is operational specificity that wins skeptical CTOs.
- **Four threat-model patterns** (lines 188–196) + closing honest limitation "It does not bound it to infinity" (line 198) — voice that earned itself.
- **Trustee-residency paragraph** (line 124) names DPDP, DIFC DPL, ADGM, GDPR Chapter V, 242-FZ, POPIA Section 72 in one paragraph — extension is polish, not rewrite.
- **§Implementation Surfaces event-contract list** (lines 218–224) — exactly the level of specificity Webb (CTO target reader) wants more of.

## Priority PAO action items (in priority order)

### 1. Add a Schrems II sentence in trustee-residency paragraph (line 124)

**Highest-leverage edit.** Strongest European compliance argument for local-first in the entire book; chapter currently leaves the lever on the table. Single-paragraph add.

### 2. Cut line 14 disclaimer + rewrite chapter chapeau (lines 12–14)

Chapter opens with administrative orientation rather than intent. Three critics (Chase, Hollis, Halvorsen) flagged identically. Rewrite as single energetic paragraph that is the chapter's first idea.

### 3. Extend regulatory list at line 124 + deployment-class table "Regulated" row

Add to trustee-residency paragraph: PIPL (China), Japan PIPA, South Korea PIPA, NDPR (Nigeria), Kenya DPA, LGPD/LFPDPPP (LATAM).

Add to deployment-class table "Regulated" row: DPDP, DIFC DPL, PIPL, 242-FZ.

Five critics (Krishnamurthy, Tanaka, Diallo, Volkov, Reyes) flagged the same edit.

### 4. Add a paragraph on 2022 SaaS service termination event

Single highest item from CIS reviewer (Volkov). Documented case of vendor-unreachability as recovery scenario distinct from user-side key loss. Lands in §Why this matters or §Boundaries.

### 5. Tighten §Recovery State-Machine Convergence ~30% + inline Argon2id parameters at line 142

Convergence-mechanics paragraph compresses; Argon2id cross-reference inlined as parenthetical. Webb + Osei + Tanaka + Barker (4 critics) flagged together.

## Voice-pass-pending items (CO seat — Stage 6, not PAO-actionable)

- **§Forward Secrecy and Post-Compromise Security** awaits human anecdote insertion + Sinek calibration. Hollis suggests journalist/source-confidentiality framing — what is the human stake in PCS? Probably the journalist whose source's identity must remain confidential after the journalist's device is compromised.
- **Sub-pattern 46e Cohn-Gordon citation** — deferred to Phase 7 reference-list work; inline-by-name interim is correct (confirmed by Osei).

## Other findings (not priority-ordered)

- **Webb pushback:** §Recovery State-Machine Convergence asymmetric design rationale stays; partition-window mechanics could move to appendix or compress by 1/3 (covered by item 5).
- **Webb pushback:** Sub-pattern 46d (sealed sender) is a metadata-graph protection, not a key-lifecycle operation; might belong in a metadata-protection chapter elsewhere.
- **Halvorsen:** §Forward Secrecy (lines 230–303) has the most assembled feel; voice-pass will catch this.
- **Halvorsen:** Watch the "X is the property that..." construction at lines 230–237 — three definitions in two paragraphs starts to chant.
- **Nakamura:** Add one paragraph in §Forward Secrecy steelmanning the case for *not* requiring PCS, then answer it.
- **Osei:** Add one sentence at line 292 specifying the test harness for conformance assertions ("a deterministic key-injection harness in the kernel test suite").
- **Reyes:** Confirm Mermaid renderer emits `<title>` and `<desc>` for accessibility; if not, add prose alt-descriptions.
- **Reyes:** §Implementation Surfaces GracePeriodObserver tick events drive accessible progress announcements (`role="status"`, `aria-live="polite"`) — name this explicitly.
- **Tanaka:** Custodian-held framing could name SIer-mediated custody (NTT Data, Fujitsu, Accenture Japan) as a Japanese deployment shape.
- **Diallo:** Consider field-operations / intermittent-connectivity case in §Recommended Deployment Combinations (SMS over MTN/Safaricom networks with regional outages).
- **Volkov:** Consider naming import substitution (импортозамещение) explicitly in §Custodian-held.
- **Hollis:** Consider closing paragraph after §FAILED conditions returning to chapter's human stake.
- **Hollis:** Consider whether §Forward Secrecy should land before §Key-Loss Recovery (chronologically: in-session compromise precedes lost-key recovery; current order ends on theoretical material).

## Non-polish observations

- **Cross-chapter coherence:** chapter functions as standalone operational document. Cross-references appropriate context, not load-bearing dependencies. Reader can follow Ch22 without re-reading Ch15.
- **Diagrams:** Ch22 has 2 Mermaid blocks (KCIR state machine + deployment-class flowchart). Both earn their place. Note: my pre-staged proposal had 5 diagrams total — 2 in Ch22 + 3 in Ch23. The board reviewed Ch22's 2; the 3 in Ch23 are awaiting separate review.
- **Prose register:** consistent with Ch15's slimmed architectural register. Uncle Charlie passage is the one departure and it is the right departure.

---

**End of review.** PAO will apply priority items 1–5 in a polish PR; voice-pass items wait for CO Stage 6.
