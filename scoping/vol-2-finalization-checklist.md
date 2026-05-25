# Vol-2 Finalization Checklist

**Status:** WORKING CHECKLIST 2026-05-25 (PAO). Tracks what must close before Vol-2
can be ratified `icm/approved` AND before Vol-3 can reach `icm/draft`.

**Author:** PAO 2026-05-25 (V1 scoping subagent). Amended 2026-05-25T15:30Z by PAO V2
subagent: Tier-1 ch17 Diego-living item marked CLOSED — current prose verified
canon-compliant against canon.yaml + ch14 0408 Day 47 death-anchor. The original
diagnostic reproduced the 2026-05-22 council critic findings without re-checking
against PR 160 (`1e26a87`), which landed the fix the same day the council reviewed.
See `pao-status-2026-05-25T15-32Z-vol-2-ch17-no-op-verification.md` for the verification
narrative.

**Amended 2026-05-25T16:30Z by PAO V4 subagent:** all three Tier-2 Ch 14 entries
(porthole-moment register, opener relocation, EAB-mask procedural failure) marked
CLOSED — current prose verified to already carry the council interventions, landed
2026-05-22 via PR 161 (commit `f95318d`, "ch14 reframe — Tier 1 council interventions
(3 sub-edits)"). Same diagnostic-error pattern PAO V2 caught with the ch17 item: the
V1 checklist reproduced 2026-05-22 council critic findings without re-reading current
prose three days later. The V1 checklist also mislabeled the council's "Tier 1" as
"Tier 2" — a label-drift unrelated to closure state. PAO V4 also folded a newly-surfaced
ch14↔ch17 letter-sealing Plan-C contradiction (line 402 + 426 still carried pre-Plan-C
"Diego sealed his own letter on Day 46" against ch17 + canon Maria+Anna-seal-Day-55
posthumous canon); resolved 2026-05-25 via PR 201. See
`pao-status-2026-05-25T16-30Z-vol-2-ch14-letter-sealing-and-checklist-refresh.md` for
verification narrative + dispatch context.

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

- [x] **Ch 17 Diego-living continuity bug — CLOSED 2026-05-22 via PR #160**
      (`1e26a87 fix(vol-2): ch17 — Diego-alive continuity bug (Tier 0 council finding)`).
      The council-flagged lines (40, 50, 56, 216–236 + frontmatter) were already
      Plan-C-reframed three days before this checklist was authored. Current state
      verified 2026-05-25T15:30Z (PAO V2 subagent re-read against canon.yaml +
      ch14 0408 Day 47 death-anchor): all surviving Diego references in ch17 are
      posthumous — console reassigned to Nakamura ("the empty seat"; "the watch
      Diego had asked to stand and would not stand"); Maria + Anna sort his
      personal effects at 1410 Day 53; letter sealed by Maria + Anna at 2147
      Day 55 using Diego's bombilla wax ("The seal was Diego's seal. The pages
      were Diego's pages. The hand on the address was Diego's hand. The act was
      ours."); Maria carries the envelope down the gangway at 0728 Day 56 per
      canon.yaml diego.last_letter spec. **Net unblock:** the Vol-2 Tier-1 item
      blocking Vol-3 `icm/draft` was closed three days before the predecessor PAO
      subagent authored this checklist — the diagnostic reproduced the council's
      stale findings rather than re-reading current prose. Vol-3 ch17-blocker
      gate is GREEN.

### Tier 2 (load-bearing register adjustments)

- [x] **Ch 14 porthole-moment register — CLOSED 2026-05-22 via PR 161**
      (`f95318d docs(vol-2): ch14 reframe — Tier 1 council interventions
      (3 sub-edits)`). The V1 checklist flagged anaphoric procedural euphemism
      ("The look said... The look said... The look said...") at ch14:189–203.
      Current state verified 2026-05-25T16:30Z (PAO V4 subagent re-read against
      ANNA-VOICE.md): ch14:170 now renders the porthole moment with concrete
      physical detail through streaked porthole glass — coolant smear, green
      iris, Joel's hand at the bracket — matching the council's literary-critic
      recommendation. **Net unblock:** the V1 checklist diagnostic reproduced
      stale 2026-05-22 council findings rather than re-reading current prose;
      the council ratified the intervention the same day they reviewed and
      PR 161 landed the fix. (The V1 checklist also mislabeled the council's
      "Tier 1" classification as "Tier 2" — label-drift unrelated to closure
      state.)

- [x] **Ch 14 opener relocation — CLOSED 2026-05-22 via PR 161**
      (`f95318d`). The V1 checklist flagged ~1,200 words of institutional
      damage report frontloaded at the chapter opener, telling the reader
      Diego is dead on page one. Current state verified 2026-05-25T16:30Z
      (PAO V4 subagent re-read): ch14:26 now opens "I had been asleep when
      the alarm fired." The damage report has been relocated to inline-at-
      filing-point at ch14:344 (after the cascade plays out in prose-time);
      the reader experiences the eleven minutes behind the bulkhead before
      learning the outcome, matching the council's thriller-genre-critic
      recommendation.

- [x] **Ch 14 EAB-mask procedural failure — CLOSED 2026-05-22 via PR 161**
      (`f95318d`). The V1 checklist flagged the apparatus-protocol question:
      should the book INTERROGATE the procedural failure (Joel entered a
      coolant-and-smoke compartment without an EAB mask) rather than excuse
      it? Current state verified 2026-05-25T16:30Z (PAO V4 subagent re-read):
      ch14:464 now carries the apparatus-protocol indictment paragraph in
      Anna's personal file — "That arrangement was not Joel's. That arrangement
      was not Sá's. That arrangement was the consortium's standing-apparatus-
      protocol-for-coolant-compartments..." The CIC-ruling-required uncertainty
      the V1 checklist flagged was resolved structurally: Anna interrogates the
      procedural-failure as a consortium-level lapse, not as Joel's personal
      negligence — Plan-C-aligned without collapsing into self-recrimination
      register.

### Tier 2 amendments (newly-closed 2026-05-25)

- [x] **Ch 14↔ch17 letter-sealing Plan-C contradiction — CLOSED 2026-05-25 via PR 201**
      (`fix(vol-2): ch14 letter-sealing language to Plan-C posthumous`).
      Ch14:402 + 426 still carried pre-Plan-C wording (Diego sealing his own
      letter on Day 46 at 2147) that contradicted ch17:222 + canon.yaml
      `diego.last_letter.sealed: "2147 Mission Day 55"` (Maria + Anna seal
      posthumously with the bombilla wax). Surfaced by PAO V3 subagent 2026-05-25T15:57Z
      as out-of-scope tail item; resolved 2026-05-25T16:30Z by PAO V4 with a
      2-line minimal-diff distinguishing Diego's KEK-signing-at-capture on Day 46
      (canonical: timestamp at chain) from the physical wax-and-bombilla seal
      Maria + Anna perform on Day 55 (ch17 canon). Net diff: 2 lines, no
      structural change, no register drift.

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

Wave 3 originally missed Ch 17 — surfaced in the 2026-05-22 council review,
fixed same day by PR #160 (`1e26a87`). Wave 3 close-out is now complete across
all back-third chapters. Per-chapter table updated below.

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
| Ch 14 | done 2026-05-20 | tier-2 porthole + opener + EAB CLOSED 2026-05-22 (PR 161); letter-sealing Plan-C CLOSED 2026-05-25 (PR 201) | Wave 1 landed (Diego death); letter-sealing Plan-C cleanup landed 2026-05-25 |
| Ch 15 | done 2026-05-20 | back-third voice-drift candidate (tier-3) | Wave 3 posthumous reframe landed |
| Ch 16 | done 2026-05-20 | back-third voice-drift candidate (tier-3) | Wave 3 posthumous reframe landed |
| Ch 17 | done 2026-05-20 | tier-1 Diego-living continuity bug CLOSED 2026-05-22 (PR #160) | Wave 1 (Joel admission) landed; Wave 3 posthumous reframe landed via PR #160 |
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

1. ~~**Vol-2 ch17 posthumous reframe**~~ — CLOSED 2026-05-22 via PR 160
   (`1e26a87`). Wave 3 close-out complete. This item no longer blocks Vol-3
   `icm/draft`. Verified 2026-05-25T15:30Z by PAO V2 re-read against canon.yaml.
2. ~~**Ch 14 tier-2 interventions**~~ (porthole register, opener relocation,
   EAB-mask ruling) — CLOSED 2026-05-22 via PR 161 (`f95318d`). Verified
   2026-05-25T16:30Z by PAO V4 re-read against ANNA-VOICE.md + canon.yaml.
   The V1 checklist diagnostic reproduced stale council findings without
   re-checking against current prose; the council ratified and PR 161 landed
   the fixes the same day (2026-05-22) the council reviewed.
   ~~**Ch 14↔ch17 letter-sealing Plan-C contradiction**~~ — newly-surfaced item
   CLOSED 2026-05-25 via PR 201 (PAO V3 surfaced; PAO V4 resolved). Ch14 line 402
   + 426 brought into canon shape with ch17:222 + canon.yaml `diego.last_letter`.
3. **Ch 04 tier-3 architecture-walkthrough cut** executes OR explicit CIC ratification
   that Ch 04 stays as-is (with the understanding that the abandonment risk is
   accepted). PAO V3 noted that ch04 was restructured via interleave (PR 162
   commit `71d02c5`, "interleave architecture talk with live descent") per a
   documented author path-(b) choice; further amputation would contradict a
   ratified author decision. Defer to CIC ruling on whether PR 162 interleave
   satisfies the gate (mark CLOSED) OR a stricter amputation pass is required.
4. **Volume-level voice-check** completes (read-aloud pass).
5. **canon.yaml + held-lines + Hiroshi + Stefan-Astrid** all reconciled.

Items NOT blocking Vol-3 start:
- Audio render readiness (Vol-3 can be drafted in parallel with Vol-2 audio work)
- Comp-titles positioning (marketing artifact; not narrative)
- Tier-5 Ch 01 retrospective-frame addition (optional)

## Estimated time to Vol-2 ratification

| Workstream | Effort | Owner |
|---|---|---|
| ~~Ch 17 posthumous reframe~~ | CLOSED 2026-05-22 via PR 160 | n/a |
| ~~Ch 14 tier-2 interventions (porthole + opener + EAB)~~ | CLOSED 2026-05-22 via PR 161 | n/a |
| ~~Ch 14↔ch17 letter-sealing Plan-C contradiction~~ | CLOSED 2026-05-25 via PR 201 | n/a |
| Ch 04 architecture cut OR CIC ratification of PR 162 interleave | ~15 min CIC consult + ~2h prose if amputation ruled | PAO + CIC + chapter-drafter |
| Back-third voice canonicalization (Ch 13–18) | ~3h wall-clock | prose-reviewer subagent fan-out |
| canon.yaml + held-lines + Hiroshi + Stefan-Astrid reconciliation | ~2h | PAO |
| Make targets + citation pass | ~1h | PAO + Yeoman |
| Read-aloud pass (author) | ~9h | author (over 3 sessions) |
| **Total wall-clock to Vol-2 ratification** | **~2-4 days** (with author availability) | |

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
