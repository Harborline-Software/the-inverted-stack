# Vol-2 Finalization Checklist

**Status:** WORKING CHECKLIST 2026-05-25 (PAO). Tracks what must close before Vol-2
can be ratified `icm/approved` AND before Vol-3 can reach `icm/draft`.

**Author:** PAO 2026-05-25
**Predecessor docs:**
- `vol-2/SPINE.md` (RATIFIED 2026-05-21 — Plan C1+C7)
- `vol-2/_reviews/2026-05-22-council/INDEX.md` (5-critic council review, 2026-05-22)
- `.pao-inbox/_state-snapshots/2026-05-21-plan-c-integration-plan.md` (Plan C waves 1–4)

## What this document is

A checklist of remaining Vol-2 finalization items derived from (a) Plan C1+C7
integration-plan close-out, (b) the 5-critic council review at
`vol-2/_reviews/2026-05-22-council/`, and (c) the post-2026-05-21 audit-trail of
interventions that have not yet executed.

This is NOT a plan for the interventions themselves (the council review carries
detailed-recommendation prose for each); it is a tracker for which items have closed
and which remain open.

## Council intervention queue (5-critic verdicts from 2026-05-22)

Per `vol-2/_reviews/2026-05-22-council/INDEX.md`, the council surfaced 5 convergences
+ multiple single-critic findings. Status as of 2026-05-25:

### Tier 1 (urgent, line-level continuity)

- [ ] **Ch 17 Diego-living continuity bug** — Plan C ch14 has Diego dying Day 47
      at 0408; ch17 currently has Diego at the polar-ops console on Day 53 + sealing
      the letter on Day 55 + bringing it to Anna at 2147 Day 55. canon.yaml already
      specifies the letter was sealed posthumously by the crew; the prose just
      needs to render that. **Lines flagged:** ch17 lines 40, 50, 56, 216–236
      (technical-substrate critic) + frontmatter Diego-at-console reference
      (bestseller-profile critic). **Owner:** PAO via chapter-drafter subagent
      dispatch. **Effort:** ~30–45 min single-chapter pass.

### Tier 2 (load-bearing register adjustments)

- [ ] **Ch 14 porthole-moment register** — Currently uses anaphoric procedural
      euphemism ("The look said... The look said... The look said...") which
      ANNA-VOICE.md bans. Recommendation: render with at least one concrete
      physical detail through the glass (Joel's hand, his eye, the coolant smudge).
      **Lines flagged:** ch14:189–203 (literary critic). **Owner:** PAO or
      chapter-drafter subagent. **Effort:** ~30 min focused-prose intervention.

- [ ] **Ch 14 opener relocation** — Currently frontloads ~1,200 words of
      institutional damage report; reader is told Diego is dead on page one
      instead of living the eleven minutes behind the bulkhead in prose-time.
      Recommendation: move or omit the opener so the reader doesn't know whether
      Joel comes out alone until Joel walks out alone (thriller-genre critic).
      **Owner:** PAO judgment — restructure decision before drafting.
      **Effort:** ~1h PAO + ~30 min chapter-drafter execution.

- [ ] **Ch 14 EAB-mask procedural failure** — Joel enters a coolant-and-smoke
      compartment without an EAB mask because the medical-rated breathing
      apparatus was at the medical bay two decks above (technical-substrate
      critic). Currently the book treats this as inevitable; the indictment
      reading the critic surfaced is that the book should INTERROGATE the
      procedural failure, not excuse it. **Owner:** PAO judgment — is this
      a Plan-C-aligned addition (Joel admits the procedural-failure-was-his
      AS WELL AS the funding-decision-was-his) OR is this a different structural
      register (the consortium's procedural lapse, not Joel's)? Surface to CIC
      for ruling. **Effort:** ~15 min CIC consult + ~1h prose work depending on
      ruling.

### Tier 3 (volume-level register problems)

- [ ] **Architecture-walkthrough drag** — Ch 04 (First Submersion) is a 5,000-word
      conference-room software-architecture walkthrough; beta reader flagged as
      highest-risk abandonment point. Critic-convergence: literary critic +
      thriller-genre critic both flagged voice drift into institutional/architectural
      register in the back third + Le Carré-register-vs-Robert-Harris-promise gap.
      **Recommended interventions:**
      - Ch 04: compress architectural exposition; surface character/scene/conflict
        instead; aim for 30%+ word-count cut; ~3,500 words target instead of
        ~5,000
      - Back-third pass: voice-recanonicalize chapters 13–17 against ANNA-VOICE.md
        baseline; targeted prose-reviewer subagent pass
      **Owner:** PAO + prose-reviewer subagent. **Effort:** ~3–4h
      including Ch 04 restructure + back-third sweep.

### Tier 4 (jacket / marketing alignment)

- [x] **Back cover replacement (Candidate 4 → Candidate 5)** — already committed
      in SPINE 2026-05-22; Candidate 5 ("Joel Reyes ran an AI-agent security
      audit...") supersedes Candidate 4 ("Diego Sá made it nineteen steps...").
      Per bestseller-profile critic's recommendation: AI-agent-not-verified angle
      is the primary commercial hook; closes the back-cover/text mismatch by
      removing the nineteen-steps image (not in executed ch14 prose).

- [ ] **Comparable-titles positioning** — Bestseller-profile critic recommended
      repositioning toward AI-anxiety market. Action items not yet executed:
      pitch-email template using Candidate 5 cover language; comp-titles list
      (*Project Hail Mary*, *Daemon*, *Influx*, *Cryptonomicon*, possibly
      *Klara and the Sun* on the AI-substrate side). **Owner:** PAO + Yeoman
      (book-side marketing). **Effort:** ~1h authoring; not blocking for
      Vol-3 start.

### Tier 5 (light/optional)

- [ ] **Ch 01 retrospective-frame foreshadowing** — SPINE allows adding one
      sentence to Anna's Ch 01 paragraph about helping where she could help:
      *"I helped where I could help. I did not always know which moments would
      be the ones I could not."* Allowed per Plan C anti-pattern discipline if
      it does NOT signal the death. **Owner:** PAO judgment + chapter-drafter
      micro-dispatch. **Effort:** ~15 min. Optional but recommended.

## Plan C wave-by-wave audit

Per `2026-05-21-plan-c-integration-plan.md` and SPINE status (waves landed
2026-05-21T14:15Z–2026-05-21T16:30Z):

- [x] **Wave 1** — Ch 14 cascade with Diego death; Ch 17 Joel admission;
      Ch 18 staff-history desk choice
- [x] **Wave 2** — Ch 01, Ch 03, Ch 08, Ch 12 foreshadowing additions for Diego;
      Ch 07, Ch 11 foreshadowing additions for Joel's firmware admission
- [x] **Wave 3** — Ch 15, Ch 16, Ch 18 reframing of Diego material as posthumous;
      Ch 07 Sunfish-name reveal reframed under firmware-procurement shadow
- [x] **Wave 4** — consequence ripples; Astrid scene at dock under Plan C weight;
      staff-history-vs-diary register reframe; canon.yaml plants updates

But Wave 3 missed Ch 17 (which is the load-bearing tier-1 item above — Diego
references in ch17 are NOT yet posthumous, contradicting canon.yaml and the
Plan-C reframe). **The Wave 3 close-out is incomplete; ch17 needs the
posthumous-reframe pass.**

## Per-chapter UPF + voice-check status

Per `_state-snapshots/2026-05-20-upf-chXX-*` snapshots (2026-05-20), per-chapter
UPF has been executed for all 18 chapters by bestseller-profile critic. Voice-check
status per the council review:

| Chapter | UPF | Voice-check | Plan-C reframe |
|---|---|---|---|
| Ch 01 | done 2026-05-20 | tier-5 recommended addition pending | Wave 2 plant landed |
| Ch 02 | done 2026-05-20 | clean per council | n/a |
| Ch 03 | done 2026-05-20 | clean per council | Wave 2 plant landed |
| Ch 04 | done 2026-05-20 | architecture-walkthrough drag flagged (tier-3) | n/a |
| Ch 05 | done 2026-05-20 | clean per council | n/a |
| Ch 06 | done 2026-05-20 | clean per council | n/a |
| Ch 07 | done 2026-05-20 | clean per council | Wave 2 + Wave 3 firmware-procurement-shadow plants landed |
| Ch 08 | done 2026-05-20 | clean per council | Wave 2 plant landed |
| Ch 09 | done 2026-05-20 | clean per council | n/a |
| Ch 10 | done 2026-05-20 | clean per council | n/a |
| Ch 11 | done 2026-05-20 | clean per council | Wave 2 plant landed |
| Ch 12 | done 2026-05-20 | clean per council | Wave 2 plant landed |
| Ch 13 | done 2026-05-20 | back-third voice-drift candidate (tier-3) | n/a |
| Ch 14 | done 2026-05-20 | tier-2 porthole moment + opener relocation + EAB ruling pending | Wave 1 landed (Diego death) |
| Ch 15 | done 2026-05-20 | back-third voice-drift candidate (tier-3) | Wave 3 posthumous reframe landed |
| Ch 16 | done 2026-05-20 | back-third voice-drift candidate (tier-3) | Wave 3 posthumous reframe landed |
| Ch 17 | done 2026-05-20 | **tier-1 Diego-living continuity bug** | Wave 1 (Joel admission) landed; Wave 3 posthumous reframe MISSED |
| Ch 18 | done 2026-05-20 | back-third voice-drift candidate (tier-3) | Wave 1 (staff-history) + Wave 3 + Wave 4 (Astrid scene) landed |

## Pre-assembly checklist (technical / mechanical)

- [ ] **canon.yaml validation** — full cross-reference between canon.yaml and prose;
      every plant tagged in canon.yaml verified present in prose at the named
      chapter; every prose-reference verified against canon. **Owner:**
      technical-reviewer subagent OR PAO. **Effort:** ~1h.
- [ ] **Held-lines reconciliation** — `vol-2/act-1/ch02-recruitment-interview.held-lines.json`
      indicates held-back lines from ch02; verify whether held lines were
      eventually included or remain held. **Effort:** ~15 min audit.
- [ ] **Hiroshi-character canon firmness** — Hiroshi appears in ch18 notebook moment;
      Vol-3 pays a load-bearing plant on him at the standards-body conference.
      Confirm Vol-2 ch18 establishes enough Hiroshi-canon to carry the Vol-3
      payoff; if not, augment in finalization pass. **Owner:** PAO ruling.
- [ ] **Stefan-Astrid continuity** — Ch 18 has Stefan + Astrid present at dock;
      Vol-3 SPINE has Stefan returning as institutional shadow + Astrid sending
      one written communication to Wanjiru as Vol-3 plant. Verify Vol-2 closeout
      leaves these threads in the right open-state for Vol-3 to pick up.
      **Owner:** PAO ruling at finalization assembly.
- [ ] **Make targets clean** — `make word-count` shows volume within ±5% of
      ~110k–115k target; `make lint` no broken cross-references; `make draft-pdf`
      renders cleanly. **Owner:** Yeoman / PAO. **Effort:** ~30 min if clean;
      iteration time if not.
- [ ] **Citation discipline pass** — IEEE-style references compiled per
      Appendix E rules from Vol-1 (Vol-2 inherits the convention even if it has
      fewer external citations than Vol-1). **Owner:** PAO. **Effort:** ~30 min.

## Voice-check + final reading-aloud pass

- [ ] **Per-chapter prose-reviewer pass** — back-third chapters (13, 14, 15, 16, 17, 18)
      get a focused prose-reviewer subagent pass for voice canonicalization
      against ANNA-VOICE.md (back-third voice-drift is the council-flagged tier-3
      concern). **Owner:** prose-reviewer subagent. **Effort:** ~30 min/chapter
      × 6 = ~3h wall-clock; can parallel-fan-out 2–3 chapters at once.
- [ ] **Read-aloud pass** — author / CIC reads each chapter aloud at audiobook-pace
      to verify voice register holds + diary insets land at correct emotional
      altitude + dialogue carries character-specific cadence. **Owner:** author
      (human only — Claude cannot do this step). **Effort:** ~30 min/chapter
      × 18 = ~9h. Recommend splitting into 3 sessions (act-by-act).

## Audio render readiness

- [ ] **Audiobook pipeline check** — `build/audiobook.py` staged but inert per
      `vol-2/CHAPTER-OUTLINE.md` (was awaiting Arc 1 `icm/draft`; now all 18
      chapters at `icm/approved`-equivalent post-Plan C; pipeline should be
      runnable). **Owner:** Yeoman / PAO. **Effort:** ~1h pipeline smoke-test +
      iteration if broken.
- [ ] **Narrator audition** — Ray Porter / Bobiverse register; audition criteria
      TBD per SPINE. **Owner:** author / external. **Effort:** weeks of
      audition + recording.
- [ ] **Per-chapter audio render** — once narrator is cast, per-chapter audio
      render at 30–45 minute target per chapter. **Owner:** Yeoman with
      Higgs/Kokoro pipeline for draft renders; human narrator for final.

## What blocks Vol-3 from reaching `icm/draft`

Per the Vol-3 plan's halt-condition list, Vol-3 cannot reach `icm/draft` until:

1. **Vol-2 ch17 posthumous reframe** (tier-1 above) executes. **This is the
   single highest-priority Vol-2 finalization item.** Wave 3 missed it; closing
   the wave clears the most visible Vol-3 blocker (Wanjiru's voice canonicalization
   depends on Vol-2's voice register being final, including ch17's voice work).
2. **Ch 14 tier-2 interventions** (porthole register, opener relocation, EAB-mask
   ruling) execute. These are voice-canonical interventions whose outcome calibrates
   the Vol-3 voice differential.
3. **Ch 04 tier-3 architecture-walkthrough cut** executes OR explicit CIC ratification
   that Ch 04 stays as-is (with the understanding that the abandonment risk is
   accepted). Vol-3 outlines benefit from knowing whether the volume-level
   architecture-walkthrough register has been disciplined or whether Vol-3 should
   plan to NOT inherit the same problem.
4. **Volume-level voice-check** completes (read-aloud pass).
5. **canon.yaml + held-lines + Hiroshi + Stefan-Astrid** all reconciled.

Items NOT blocking Vol-3 start:
- Audio render readiness (Vol-3 can be drafted in parallel with Vol-2 audio work)
- Comp-titles positioning (marketing artifact; not narrative)
- Tier-5 Ch 01 retrospective-frame addition (optional)

## Estimated time to Vol-2 ratification

| Workstream | Effort | Owner |
|---|---|---|
| Ch 17 posthumous reframe | ~45 min | chapter-drafter subagent |
| Ch 14 tier-2 interventions (porthole + opener + EAB) | ~2h | PAO + CIC + chapter-drafter |
| Ch 04 architecture cut | ~2h | PAO + chapter-drafter |
| Back-third voice canonicalization (Ch 13–18) | ~3h wall-clock | prose-reviewer subagent fan-out |
| canon.yaml + held-lines + Hiroshi + Stefan-Astrid reconciliation | ~2h | PAO |
| Make targets + citation pass | ~1h | PAO + Yeoman |
| Read-aloud pass (author) | ~9h | author (over 3 sessions) |
| **Total wall-clock to Vol-2 ratification** | **~3-5 days** (with author availability) | |

## Acceptance — Vol-2 ratified

The volume is ratified when:

1. All tier-1 + tier-2 council interventions execute
2. Tier-3 architecture-walkthrough drag is addressed (cut Ch 04 OR CIC ratifies as-is)
3. Back-third voice-drift is addressed (prose-reviewer pass on Ch 13–18)
4. canon.yaml fully reconciled with prose
5. Held-lines reconciled
6. Make targets clean
7. Author read-aloud pass completes
8. CIC reads completion-status beacon and approves
9. ASSEMBLY.md updated with final manifest
10. Audio render either (a) complete OR (b) explicitly deferred to post-ratification
    pipeline work
11. Vol-3 start authorized

— PAO, 2026-05-25
