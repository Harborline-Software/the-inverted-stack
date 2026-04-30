---
type: literary-board-review
chapter: ch07-security-lens
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.7/10 board consensus — strongest character-as-proof opener in Part II)
council-member: Nia Okonkwo (Security Lens)
---

# Literary Board Review — Ch07 (The Security Lens)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 7.5/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8.5/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 8/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 7.5/10 | GLOBALLY POSITIONED |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 8.5/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 6.5/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 7/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 8.5/10 | GLOBALLY COMPLETE |
| **Board consensus** | **7.7/10** | **POLISH** |

## QC-9 verification

**PASSES.** Two-act structure lands cleanly:
- §Act 1: Round 1 — The Key Compromise Gap (L18–60) with explicit PROCEED WITH CONDITIONS verdict at L56–60 and the "this is a prerequisite, not a condition in the normal sense" framing at L58 that gives the verdict force
- §What Changed Between Rounds (L64–92) — the structural hinge; mermaid key-hierarchy diagram at L70–85 is the chapter's load-bearing technical artifact
- §Act 2: Round 2 — Four Remaining Conditions (L95–181) with PROCEED WITH CONDITIONS verdict at L165–181

The Round 1 axiom at L42 — "Security architectures are evaluated on their failure modes. The normal path is never the problem." — sits at the structural midpoint of Act 1 and may be the punchiest single sentence in any Part II chapter.

## Council member identification

**Nia Okonkwo (Security Lens).** Confirmed at L10, L14, L24, L42, L54, L58, L68, L97, L111, L135, L139, L145, L149, L167, L213. Consistent with Ch10 R2 tensions paragraph reference. Female pronouns. Character-as-proof opener established through past action ("has broken three local-first demos in under twenty minutes").

## Ch15/Ch22 redundancy verification

Ch7 has detectable spec-creep into Ch15 territory in §GDPR Article 17 stretch (L147–163) which respecifies the crypto-shredding mechanism that Ch15 §GDPR Article 17 and Crypto-Shredding (L171–183) already owns at full specification depth. Ch7 should compress to council-finding voice (the conflict is real, the architecture has an answer, see Ch15).

Ch7 does NOT redundantly specify Ch22 territory — the compromise response procedure at L87 is at council-chapter altitude (what the architecture commits to), with the operational lifecycle correctly deferred to Ch22 §Key Compromise Incident Response.

## Strengths to preserve

- **L10 opener** — `strings` on the binary. Sharpest character-as-proof opener in Part II. Five short sentences, past action, specific tool name, specific number. Untouchable.
- **L26 honeypot displacement framing** — "distributing data to endpoints does not eliminate the honeypot problem — it distributes it to the weakest endpoint."
- **L38 senior-administrator-train scenario** — the most actionable threat-model paragraph in Part II
- **L42 Round 1 axiom** — "Security architectures are evaluated on their failure modes. The normal path is never the problem."
- **L58 prerequisite-not-condition framing** — gives the Round 1 verdict structural force
- **L70–85 mermaid key-hierarchy diagram** — correctly placed at the structural hinge
- **L123 Compelled Access paragraph** — bookmark-grade. Schrems II / 242-FZ / DIFC / DPDP/RBI / PIPL alignment in a single passage
- **L189 honeypot displacement reprise** — "a genuine improvement — and a displacement of the problem rather than an elimination of it"
- **L185–207 §Defense-in-Depth coda** — four declarative layers; the chapter's strongest sustained-argument architecture
- **L213–222 Non-Negotiable Security Checklist** — eight ADR-pasteable bullets; HSM/multi-party-ceremony bullet at L218 is operationally rare

## Priority PAO action items (in priority order)

### 1. Compress §GDPR Article 17 (L147–163) by ~150 words; defer mechanism to Ch15

Largest spec-creep into Ch15 territory and the largest contributor to the 4,385/3,500 word overage. Ch15 owns the mechanism specification. Ch7 owns the council finding: conflict is real, resolution is crypto-shredding (named, not specified), metadata residue is a known limitation, see Ch15 for the implementation. Cut from ~360 words to ~200. Multi-jurisdiction sentence at L163 stays — that's the regional-positioning load-bearing passage.

### 2. Close regional regulatory parity gap at L123 (Compelled Access paragraph)

Apply Ch5 / Ch10 polish pattern. Already names DIFC, 242-FZ, DPDP/RBI, Schrems II, PIPL. Add:
- **Diallo:** NDPR, POPIA, Kenya DPA explicitly in body, not parenthetically
- **Reyes:** LFPDPPP, Colombia Ley 1581 explicitly
- **Tanaka:** Japan PIPA (2022) distinct from Korea PIPA; MLPS 2.0 alongside PIPL; ISMS-P
- **Krishnamurthy:** ADGM Data Protection Regulations 2021 alongside DIFC; RBI 2018 BFSI residency requirement explicit
- **Volkov:** Kazakhstan and Belarus parallels alongside 242-FZ
- **Barker:** *Data Protection Commissioner v. Facebook Ireland Limited* (Schrems II, 2020) by case citation; NIS2 Directive Article 21 reference in §Defense-in-Depth coda

Split into three paragraphs by jurisdictional cluster (Western, CIS/Russia, Asia/Middle East/Africa).

### 3. Add 2022 SaaS termination empirical anchor at L123 or L26

Single largest documented demonstration of vendor jurisdictional dependency as a security threat model — missing from the chapter where it is most relevant. ~80-word addition. Add импортозамещение naming alongside.

### 4. Add SaaS-competitor steelman at L123 (BYOK / CMK / Salesforce Shield / Box KeySafe)

Customer-managed keys with Microsoft Purview / Salesforce Shield / Box KeySafe are partial answers — keep customer's key outside cloud provider's direct custody, but data still traverses third-party infrastructure, which makes the provider legally compellable through other means. ~80 words. Ch15 L201 has this paragraph; Ch7 should have its council-altitude version.

### 5. Tighten conditions stretches; add Round 2 landing line; vary cadence

- L46–53 four-question enumeration — pattern fatigue; cut to one paragraph or break parallel
- C1–C6 condition list at L165–181 — needs a Ch5-style landing line at L181
- L66 sentence break — break the four-clause em-dash sentence into two
- L107 softening — Osei: "exactly as designed" reads as snark; soften to "as the protocol specifies"

## Voice-pass status

**Confirmed lencioni voice** (per chapters/voice-plan.yaml line 26). Okonkwo-as-character is established through specific past action; council deliberation reads as scene rather than catalog. The opener (L10) is the strongest character-as-proof opener in Part II to date. Halvorsen's score of 7 reflects paragraph-architecture and copy-edit issues, not voice-pass gap. **No voice re-pass needed.**

## Other findings (not priority-ordered)

- **Webb:** Footnote four-hour and twenty-four-hour intervals at L133 / L217 with threat-model derivation
- **Halvorsen:** Split L123 into three paragraphs by jurisdictional cluster; vary L46–53 cadence; cut "but which must be disclosed" hedge at L159
- **Nakamura:** Add ~40 words at C3 (L173) steelmanning operational value of managed relay before naming self-hosted as metadata-sensitive mitigation
- **Osei:** Cite Halderman et al. 2008 cold-boot paper at L131; footnote crypto-shredding origin at L157 (NIST SP 800-88 Rev. 1); cite Anderson *Security Engineering* (3rd ed.) at L42
- **Krishnamurthy:** Add MDM platform geographic operating model aside at L141; SI-mediated procurement footnote at L38 or L191
- **Hollis:** Visual section-break enhancement at Act 1/Act 2 transitions
- **Reyes:** Add accessibility property paragraph (assistive-tech operation continues through security events) in §Defense-in-Depth coda; forward-reference at L89 to Ch20/WCAG; Argentina Ley 25.326
- **Tanaka:** Forward-pointer at L102–111 to Ch19 §Procurement Conversation for SIer-mediated supply-chain attestation
- **Barker:** EU Cyber Resilience Act at L102 (Supply Chain); BSI C5 at L121 (Self-Hosted Relay); GDPR Article 17(3)(b) procedural exemption at L161
- **Diallo:** African fintech offline-first precedent (M-PESA / MoMo / FarmerLine) at L26 or L189; load-shedding interaction with four-hour interval at L133; sovereignty framing at L121
- **Volkov:** Preserve L218 (domestic HSM equivalents / multi-party key ceremony) verbatim

## Word-count outcome target

Before polish: 4,385 words (125% of 3,500 target).

After priority-5 polish target: ~4,200 words landing (120%, matches Ch5/Ch6 post-polish landing).

Breakdown:
- Item 1 (Article 17 compression): −160 words
- Item 5 (cadence cuts): −150 words
- Item 2 (regulatory parity additions): +120 words
- Item 3 (2022 SaaS anchor + import substitution): +90 words
- Item 4 (SaaS-competitor steelman): +80 words
- **Net: −20 words.** Additional ~150 words from §What Changed Between Rounds compression (in-memory-key-material detail at L91 → forward-pointer to Ch15).

---

**End of review.** PAO will apply priority items 1–5 in a polish PR; voice-pass items wait for CO Stage 6.
