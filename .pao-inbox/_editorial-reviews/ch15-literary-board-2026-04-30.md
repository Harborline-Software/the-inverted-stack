---
type: literary-board-review
chapter: ch15-security-architecture
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.7/10 board consensus — split landed cleanly; structural overrun localized to §Privacy-Preserving Aggregation)
---

# Literary Board Review — Ch15 (Security Architecture)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 7.5/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 7.5/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 8/10 | GLOBALLY POSITIONED |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 7/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 7/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7.5/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8.5/10 | RIGOROUS |
| Amina Diallo (African Markets) | 7.5/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 9/10 | GLOBALLY COMPLETE |
| **Board consensus** | **7.7/10** | **POLISH** |

## Voice register verification

**SPECIFICATION VOICE HOLDS** for §Threat Model, §Four Defensive Layers, §Key Hierarchy, §Role Attestation Flow, §In-Memory Key Handling, §Supply Chain Security, §GDPR Article 17, §Relay Trust Model (mostly), §Security Properties Summary.

**Voice drifts** in two locations:
- Compelled-access paragraph (L201) shifts to argument/essay register — defensible but should be named, not hidden
- §Privacy-Preserving Aggregation (L213–269) carries academic register heavier than surrounding spec voice

§Break-glass corrupt-sequence recovery subsection (L205) drifts into Ch14/Ch22 territory.

## Cross-reference verification

**ALL FORWARD-POINTERS RESOLVE CLEANLY:**
- Ch7 L155 → Ch15 §GDPR Article 17 and Crypto-Shredding (L171–181)
- Ch11 L153 → Ch15 (crypto-shredding mechanism) + Ch13 (stream compaction) — split correct after today's polish
- Ch13 L147 → Ch15 §GDPR Article 17 (L171–181)
- Ch14 L147 (state-mandated-access) → Ch15 L201 (resolves but should also surface in §Threat Model at L10)
- Ch15→Ch22 deferrals (Key Compromise IR, Key-Loss Recovery, Forward Secrecy) — all resolve to Ch22 sections with matching titles
- Ch15→Ch23 deferrals (Offline Node Revocation, Collaborator Revocation, Endpoint Compromise, Chain-of-Custody, Event-Triggered) — all resolve to Ch23 sections with matching titles

## Split verification (Ch15→Ch22, Ch15→Ch23)

**Split landed cleanly at section-title level.** All seven deferral pointers resolve. Only Ch22/Ch23 territory bleeding back into Ch15: §Break-glass corrupt-sequence recovery (L205) — sync-daemon operational territory, should move.

Other concern is structural: six consecutive single-line deferral stubs (L99, L105, L111, L117, L123, L145, L165, L185) read as navigation skeleton inside chapter body.

## Strengths to preserve

- **L12 opening hook** — "Distributing data to endpoints does not eliminate the honeypot problem. It distributes it." Two-sentence pivot
- **L22–48 §Four Defensive Layers** — exemplary specification voice; each layer with controlling sentence + mechanism + invariant
- **L73 envelope encryption mechanics** — concrete primitive specification (256-bit DEK, AES-256-GCM, 96-bit random nonce, KEK rotation re-wraps DEKs not bodies)
- **L75 Argon2id parameters** — explicit OWASP baseline citation, tiered for regulated industry
- **L57–71 Mermaid key hierarchy diagram** — concrete, scannable
- **L179 crypto-shredding honesty** — "The architecture makes content erasure technically possible. Legal counsel determines whether residual metadata satisfies the specific data subject's request"
- **L201 CMK-vs-local-first competitive distinction** — unique, CTO-grade
- **L203 2022 SaaS terminations empirical anchor** — converts structural argument to documented historical reference
- **L255 honest scoping in §Sub-pattern 12c** — "The rolling-window budget is a practical engineering heuristic, not a formal solution to temporal differential privacy"
- **L263–269 §FAILED conditions** for privacy-aggregation primitive — explicit kill triggers
- **L277–283 closing Properties Summary table + L285 administrator-trust-anchor honesty**

## Priority PAO action items (in priority order)

### 1. Resolve the six operational-deferral stubs

L99, L105, L111, L117, L123, L145, L165, L185 — collapse eight single-line deferrals into one consolidated "Operational lifecycle map" paragraph at chapter close that names topics in prose and points to Ch22/Ch23. Currently reads as navigation skeleton inside spec body. (Chase, Webb, Hollis converge)

### 2. Decide the fate of §Privacy-Preserving Aggregation (L213–269)

Either move to Ch16 / a dedicated chapter / an appendix, or promote structurally to peer of §Four Defensive Layers. Current placement weakens chapter arc and accounts for ~1,500 words of the 142% overrun. Removing it lands the chapter at 105% of target. (Chase, Webb, Hollis converge)

**PAO recommendation: move to a future Ch15.5 or appendix; do not delete content.** The differential-privacy material is technically excellent (Osei 7.5; honest scoping at L255) but topically belongs adjacent to relay operations (Ch16) rather than security architecture (Ch15).

### 3. Tighten compelled-access paragraph (L201) + close regulatory parity gap

- Cut "It answers..." anaphora chain to four beats (Halvorsen)
- Update Schrems II citation form to "CJEU Case C-311/18, 2020" for Ch13 consistency (Barker)
- Disambiguate "PIPA" as "South Korea PIPA" wherever it appears (Tanaka)
- Add ADGM Data Protection Regulations 2021 alongside DIFC (Krishnamurthy)
- Add Kazakhstan + Belarus parallel localization regimes (Volkov)
- Add Colombia Ley 1581 + Argentina Ley 25.326 (Reyes)
- Add Ghana DPA 2012 + ECOWAS Supplementary Act (Diallo)
- Add NIS2 Directive Article 21 + BSI TR-02102 anchor for Argon2id high-security tier (Barker)
- Add импортозамещение transliteration matching Ch14 L153 (Volkov)

### 4. Surface state-mandated-access threat model in §Threat Model at chapter opening

Currently named only at L201 inside §Relay Trust Model. Per Ch10 L96 / Ch14 L153, this is a distinct threat model that should be framed at the top of the chapter alongside honeypot/role-scope/forward-secrecy properties. (Volkov, Hollis)

### 5. Move §Break-glass corrupt-sequence recovery (L205) out of Ch15

Sync-daemon operational territory belonging in Ch14 or Ch22, not the security architecture chapter. The only material remaining in Ch15 that should have moved during the split. (Chase, Webb, Hollis)

## Other findings (not priority-ordered)

- **Halvorsen:** Calibrate §Privacy-Preserving Aggregation register to match §Four Defensive Layers; lower L265–269 prose temperature
- **Nakamura:** Name administrator operator-error as failure mode separate from administrator-device compromise; address warrant-served-on-administrator scenario; quantify CMK-vs-local under specific Schrems II language
- **Osei:** Specify what attacker with SQLCipher key but no role keys actually sees; cite Ch14 for send-tier filtering invariant proof
- **Krishnamurthy:** Promote RBI 2018 BFSI circular from parenthetical to first-class anchor like Schrems II; one sentence on India Atmanirbhar Bharat / Make in India
- **Reyes:** One paragraph on accessibility advantage (assistive tech continues during connectivity loss); WCAG 2.1 SC 3.3.5 implications for re-authentication interval (FIDO2 may be more accessible than typed-passphrase)
- **Tanaka:** Clarify MLPS 2.0 as cybersecurity classification regime (parallel to NIS2), not data-localization regime; ISMS-P required (not optional like ISO 27001) for Korean financial services
- **Barker:** Cite eIDAS Article 41 in body where RFC 3161 timestamps referenced
- **Diallo:** Note in §Four Defensive Layers Layer 4 that offline-write quarantine is daily-operational mode for African field deployments not edge case; one paragraph on re-authentication interval interaction with load-shedding power events

## Word-count outcome

Before polish: 5,701 body words (142% of 4,000 target — improved from 159% pre-split).

After priority-5 polish target:
- Item 2 (move Privacy-Preserving Aggregation): -1,500 words → 4,200 (105%)
- Item 1 (collapse deferral stubs): -80 words
- Item 3 (tighten anaphora) + Item 5 (move break-glass): -200 words
- Items 1+2+3+5: -1,780 words gross
- Regulatory parity additions (item 3) + state-mandated-access surfacing (item 4): +250 words
- **Net: -1,530 words → ~4,170 (104%) — within ±10% target band**

---

**End of review.** PAO will apply priority items 1, 3, 4, 5 in this polish PR. Item 2 (move §Privacy-Preserving Aggregation) requires a separate PR with destination decision (appendix vs new chapter vs Ch16 absorption). Item 2 deferred for follow-up.
