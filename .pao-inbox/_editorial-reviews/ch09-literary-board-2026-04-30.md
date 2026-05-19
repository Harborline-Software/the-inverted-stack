---
type: literary-board-review
chapter: ch09-local-first-practitioner-lens
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.7/10 board consensus - strongest opening paragraph in Part II; QC-9 model)
council-member: Tomás Ferreira (Local-First Practitioner Lens), male
voice-pass-status: brown voice assigned per voice-plan.yaml L28; opening + close already in brown register; mid-chapter sections drift to list-voice
---

# Literary Board Review - Ch09 (The Local-First Practitioner Lens)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 8/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 8/10 | FLOWING |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 7/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 8/10 | GLOBALLY POSITIONED |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 9/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 6/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 7/10 | RELEVANT WITH EXPANSION |
| Aleksei Volkov (CIS/Eastern Europe) | 8/10 | NEEDS CIS CONTEXT |
| **Board consensus** | **7.7/10** | **POLISH** |

## Council member identification

**Tomás Ferreira** (Local-First Practitioner Lens), male. Confirmed at L11, L13, L15, L17, L23, L25, L41, L57, L81, L91, L103, L107, L111, L119, L127, L153, L196. Cross-checked against Ch10 L25 (R1 verdict row), L51 (R2 verdict row), L66 (Ferreira/Voss tension on plain-file export vs DIFC/RBI custody constraints).

## QC-9 verification

**PASSES.** Two-act structure lands cleanly:
- §Act 1: Round 1 (L21–59) with PROCEED WITH CONDITIONS verdict
- §What Changed Between Rounds (L63–73) - the structural hinge; each Round 2 fix maps onto a Round 1 condition with specificity
- §Act 2: Round 2 (L77–153) ending in unconditional PROCEED - the only one in the council process

**Ch10 L66 setup verification: PASSES cleanly.** Ferreira's lens claim - *the export button is the proof of the claim* (L190) - is committed to with enough force that Ch10's collision with Voss's enterprise data-governance custody constraints (DIFC DPL 2020, RBI BFSI localization) lands. Don't soften.

## Cross-chapter consistency

- **L129 Production Analogues paragraph** overlaps Ch12 (CRDT engine survey) territory - keep Ferreira's verdict, cut the comparative tour
- **L67 export format specification** approaches Ch16 territory - defer format-level detail to Ch16, keep structural commitment
- **L143 telemetry/analytics ADR** approaches Ch15/Ch20 territory - Ch9 makes the right governance call but should defer the actual ADR
- **L69 disaster recovery walkthrough** is appropriate for Ch9 (practitioner lens claim); Ch20 details the flow
- **L83–99 Seven Ideals checklist** is appropriately Ch9 territory; no overlap

## Strengths to preserve

- **L11 opener** - "He sat in the room while it ran" and "That is the kind of discovery that does not leave you" - Halvorsen rates as strongest paragraph in council chapters
- **L45 thesis sentence** - "Custody is the lesser word. The architecture had to learn the difference." - Hollis suggests as section header / epigraph
- **L29 "Hiding without lying is craft."** and **L57 "Clear is kind."** - compressed brown-register maxims
- **L63–73 What Changed Between Rounds hinge** - QC-9 done correctly
- **L83–99 Seven Ideals walkthrough** - Osei rates as right academic move
- **L163 shared-device deployment recognition** - Krishnamurthy's strongest praise of any council chapter
- **L159 2022 SaaS suspension empirical anchor** - Volkov rates as chapter's single strongest claim for CIS readers
- **L135–143 implementation-drift framing** - Webb's most useful single piece
- **L153 "first unconditional PROCEED is the hardest one to earn"** - sets up Ch10's score table reveal
- **L184–190 export-button-as-proof principle** - load-bearing for Ch10 L66 Ferreira/Voss tension

## Priority PAO action items (in priority order)

### 1. Resolve Round 1 verdict-mechanics inconsistency at L55–58

Ferreira issued PROCEED WITH CONDITIONS per Ch10 L25, but Ch9 currently describes the export gap as "classified as a philosophical and practical blocker" inside that verdict. Pick one - either it was a CONDITION (heaviest of three) or it was the BLOCK that defines the verdict. Flagged by Chase, Webb, Osei, Krishnamurthy, Barker. Cross-chapter consistency requires this to match Ch10 L25.

### 2. Cut 700–900 words to land at ~3,800–4,000

Primary candidates:
- L127–131 Production Analogues paragraph (Ch12 territory) - lead with Ferreira's verdict (Yjs via YDotNet today, Loro aspirational, ICrdtEngine reversibility play), demote comparative survey
- One of two closing summary registers (Practitioner Checklist L171–178 or The Principle L182–196)
- Compress Global Deployment Context (L157–163) to one tight paragraph

### 3. Regional regulatory parity at L161

Apply Ch5–Ch8 polish pattern:
- **Reyes:** LGPD (Brazil), LFPDPPP (Mexico)
- **Tanaka:** PIPL, Japan APPI, South Korea PIPA explicitly (currently gestures at "parallel regimes")
- **Diallo:** NDPR (re-enacted 2023), POPIA, Kenya DPA 2019
- **Volkov:** Kazakhstan + Belarus localization regimes
- **Barker:** Distinguish Schrems II as CJEU 2020 ruling vs GDPR as regulation
- **Krishnamurthy:** Saudi PDPL 2021; Kuwait/Qatar/Bahrain regimes alongside DIFC/ADGM

### 4. Add shared-device disaster recovery walkthrough

Ferreira's recovery walkthrough (L69) is single-user / single-device. Krishnamurthy and Diallo both flag that the actual deployment model in GCC, India, and African field operations is shared-tablet across a team. Add one paragraph after L69 specifying that recovery targets role + workspace, not device + sole user. Sharpen 2022 SaaS suspension framing at L159 to name operational failure mode (Volkov).

### 5. Voice-pass priorities for the brown pass

- Rewrite L129 (Production Analogues) in brown's register rather than comparative survey; lead with Ferreira's verdict
- Replace at least four of seven "Checked." instances at L85–97 with varied verbs (Holds. Confirmed. Settled. Met.)
- Tighten L161/L163 from regulation-list voice to first-person practitioner observation
- Add explicit accessibility paragraph (Reyes): assistive-tech immunity to connectivity loss is the structural advantage no council chapter has yet named

## Other findings (not priority-ordered)

- **Webb:** Lead L129 with verdict (Yjs via YDotNet); convert L161 to first-person practitioner observation
- **Nakamura:** Demote "first unconditional PROCEED is most meaningful" claim - let Ch10 make that claim; cut/reattribute commercial-model verdict at L131 (Kelsey/Ch8 territory)
- **Osei:** Source or soften "hundreds of thousands of organizations" quantitative claim at L159; either cite survey or soften "only commercial model" claim at L131
- **Krishnamurthy:** Add Indian or GCC product analogue (Zoho's offline-capable suite) to Production Analogues
- **Hollis:** Make export-button thesis explicit at chapter open, not just closing section
- **Reyes:** Add ARIA live region reference to sync-status discussion at L105; name local-first's structural accessibility advantage
- **Tanaka:** Acknowledge SIer-mediated deployment model as parallel onboarding context in zero-state first-run section L107–113
- **Barker:** Defer export format specification to Ch16 explicitly at L67; distinguish Schrems II from GDPR; consider EU AI Act mention
- **Diallo:** Mention load-shedding in disaster recovery context (L69 or L163); add M-PESA as African production analogue
- **Volkov:** Add Kazakhstan/Belarus data localization at L161; consider 1С:Предприятие as desktop-software-with-optional-sync analogue at L129; acknowledge Ukraine's distinct local-first relevance

## Word-count outcome target

Before polish: 4,572 words (131% of 3,500 target).
After priority-5 polish target: 3,800–4,000 words (109–114% of target - same band as Ch5/Ch6/Ch7 post-polish).

---

**End of review.** PAO will apply priority items 1–5 in a polish PR; voice-pass items go to CO Stage 6 (brown voice).
