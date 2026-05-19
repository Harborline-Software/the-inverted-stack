---
type: literary-board-review
chapter: ch05-enterprise-lens
date: 2026-04-30
author: literary-board subagent (12 critics)
audience: CO (final voice-pass), PAO (action items)
verdict: POLISH (7.8/10 board consensus - strong council-chapter exemplar)
---

# Literary Board Review - Ch05 (The Enterprise Lens)

## Board scores

| Critic | Score | Verdict |
|---|---:|---|
| Eleanor Chase (Executive Editor) | 7.5/10 | POLISH |
| Marcus Webb (CTO / Target Reader) | 8/10 | READ |
| Ingrid Halvorsen (Prose Editor) | 7/10 | SERVICEABLE |
| Jerome Nakamura (Technology Analyst) | 8/10 | COMPELLING |
| Dr. Amara Osei (Academic Reviewer) | 7.5/10 | SOUND |
| Meera Krishnamurthy (Dubai/India) | 9/10 | GLOBALLY POSITIONED |
| Prof. Raymond Hollis (Narrative & Rhetoric) | 8.5/10 | COHESIVE |
| Sofia Reyes (Accessibility/LATAM) | 6/10 | PARTIALLY ACCESSIBLE |
| Yuki Tanaka (East Asia/APAC) | 7/10 | TRANSLATES WITH ADAPTATION |
| Dr. Imogen Barker (European) | 8/10 | ADEQUATELY SUBSTANTIATED |
| Amina Diallo (African Markets) | 9/10 | RELEVANT |
| Aleksei Volkov (CIS/Eastern Europe) | 9/10 | GLOBALLY COMPLETE |
| **Board consensus** | **7.8/10** | **POLISH** |

## QC-9 verification

**PASSES.** Ch5 delivers two-act structure cleanly:
- §Act 1: Round 1 - The Architecture Fails Procurement (Voss scores, blocking issue, conditions, verdict)
- §What Changed Between Rounds (the narrative gap - what authors did about the blocking issue)
- §Act 2: Round 2 - Conditional Passage (re-scored sections, revised verdict)

The blocking-issue arc (no incident response procedure → companion runbook with regulatory enumeration → re-scored at 8) is the chapter's load-bearing rhetorical move. Provides the template Ch6-Ch9 inherit.

## Strengths to preserve

- **Opening passage L13–23** - Voss as composite character with shorthand pattern; "Three times she has watched a promising rollout collapse" is the strongest character-as-proof opener in Part II
- **2022 SaaS suspension case study at L21** - establishes the chapter's empirical anchor and binds Ch5 to the Ch10 synthesis (same incident named as canonical for chapters where vendor jurisdictional dependency is the central thesis)
- **"Drawer" metonym at L51** ("The two artifacts live in different drawers") - the most economical articulation of audit-trail-vs-runbook distinction in the manuscript
- **Runbook regulatory enumeration at L73** - GDPR Art. 33 + HIPAA + DPDP/PIPA/PIPL/NDPR/POPIA/LGPD/242-FZ + Schrems II procedural layer; Krishnamurthy and Volkov independently named it as the strongest multi-jurisdiction passage in the chapter
- **Podman WSL2 vs Hyper-V passage at L103–106** - analyst-grade specificity that no procurement document discusses; Webb and Nakamura concur
- **MDM regional parallel structure (L37, L155)** - same six platforms named identically in Round 1 commendation and final checklist; Diallo and Krishnamurthy verified
- **Import substitution at L169** - Volkov: "the only place in the manuscript where импортозамещение is named explicitly"
- **Act 1 / Act 2 explicit section headers** - Hollis: rare and effective; the structural scaffolding does not get in the way

## Priority PAO action items (in priority order)

### 1. Tighten conditions stretches; decide on closing artifact

Halvorsen and Chase converge: §Act 2's five-condition enumeration (C1–C5) runs ~600 words and reads as catalog rather than narrative. Tighten by ~150 words. The §Non-Negotiable Enterprise Checklist coda (eight items) restates the C1–C5 catalogue at higher altitude - keep the checklist as coda but don't let the C1–C5 stretch dilate it.

### 2. Close regional precision gaps

Reyes, Tanaka, Krishnamurthy, Diallo flagged absent regional regulatory anchors:
- **Reyes (LATAM):** Ch5 names LGPD only inline - add Mexico LFPDPPP, Colombia Ley 1581 explicit
- **Tanaka (APAC):** Distinguish Japan PIPA from Korea PIPA (chapter conflates as "PIPA"); add China MLPS 2.0
- **Krishnamurthy (Dubai/India):** DIFC DPL named at L169 but state-mandated foreign-cloud access threat is implicit; make it explicit
- **Diallo (Africa):** Add Kenya DPA alongside NDPR/POPIA

### 3. Make state-mandated-data-access threat model explicit

Volkov, Krishnamurthy, Tanaka: Ch10 contains the canonical paragraph (L104) on state-mandated infrastructure access as a distinct threat model that local-first architecture addresses through E2EE + local key management + no relay plaintext access. Ch5 references the 2022 sanctions enforcement case at L21 as a jurisdictional failure mode but does not connect it forward to the threat-model framing that Voss's lens implies. Add a forward-reference paragraph.

### 4. Vary cadence + cut decoration

Halvorsen flagged three specific prose issues:
- **L57–65 conditions stretch:** monotone three-condition enumeration; vary cadence
- **L31 antimetabole** ("Voss does not issue scores generously. When a section earns an eight from her, it has earned it the way a document earns it") - cut second clause; first clause carries the weight
- **L143 soft abstraction** ("scores redistributed across the stronger governance narrative") - replace with concrete sentence

### 5. Add ~100 words comparing architecture's incident-response posture to SaaS competitor

Webb, Nakamura: chapter establishes incident response runbook as load-bearing artifact but does not benchmark against equivalent SaaS competitor (M365 / Salesforce / ServiceNow) incident response. Add ~100 words showing why local-first incident response is structurally different from SaaS-vendor incident response (where customer is bystander to vendor's investigation). Also tighten L145 thesis ("The architecture cleared the review. The conditions govern how it is packaged, licensed, and operated.") - strong but isolated; integrate into preceding paragraph as load-bearing landing.

## Voice-pass status

**Confirmed voice-passed (lencioni voice).** Voss-as-character is established; council deliberation read as scene rather than catalog. Halvorsen's score of 7 reflects cadence variability concerns addressed in item 4, not voice-pass gap.

## Other findings (not priority-ordered)

- **Chase:** chapter target says ~3,500 words but live count is ~3,912 (112% target) - tightening item 1 brings it closer to target
- **Webb:** condition C5 (AGPLv3 dual-licensing) reads as commercial-strategy aside in a chapter otherwise about IT-deployment; consider footnote
- **Osei:** SBOM at build time (item 1) is correctly named but Syft/Grype lineage could note CycloneDX prior art
- **Krishnamurthy:** L37 lists six MDM platforms - same list at L155 is correct; deepen with one Indian BFSI-specific anecdote
- **Hollis:** §What Changed Between Rounds is the rhetorical hinge; Chase concurs
- **Reyes:** L167 power-interruption durability paragraph is excellent - Halvorsen flagged "load-shedding in Lagos, a grid event in rural Chennai" as best regionally-grounded sentence
- **Tanaka:** SIer-mediated procurement (CTC, Nomura Research Institute) not named - could add to MDM or migration-path section
- **Barker:** EU Cyber Resilience Act named correctly at L39; could reference NIS2 Directive as parallel European regime
- **Diallo:** Power-interruption durability is the most important Africa-relevant addition in this chapter; do not soften
- **Volkov:** "the only place in the manuscript where импортозамещение is named explicitly" - keep at L169 verbatim

## Word-count outcome target

Before polish: 3,912 (112% of 3,500 target). After polish target: ~3,950–4,000 (item 1 tightening offset by item 3 forward-reference paragraph + item 5 SaaS-competitor benchmark).

---

**End of review.** PAO will apply priority items 1–5 in a polish PR; voice-pass items wait for CO Stage 6.
