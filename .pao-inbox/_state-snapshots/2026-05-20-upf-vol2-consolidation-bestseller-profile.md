# Vol-2 Bestseller-Profile UPF — Volume Consolidation (Stage 07)

**Pipeline:** `icm/pipelines/bestseller-profile-review`
**Dispatch:** 2026-05-20, 18 Sonnet 4.6 + medium subagents, parallel fan-out
**Rubrics:** Literary devices (8 items) + NYT bestseller profile (9 items)
**Consolidator:** PAO main session (Opus 4.7 + xhigh)

---

## 1. Volume-wide grading matrix

| Ch | Title | Literary | NYT | Single highest-leverage edit |
|---|---|---|---|---|
| 01 | Departure | **A-** | Yellow | Excise Wanjiru direct-address repetition + add Joel bunk-laptop disclosure to chemistry-rack scene |
| 02 | Recruitment Interview | **A-** | Yellow | Hard paragraph break at "We came home on the operationally-a-lie" |
| 03 | Drake Passage Ice Edge | **B+** | Yellow | Cut Wanjiru tricolon close + vary "the discipline" motif repetitions in Priya scene |
| 04 | First Submersion | **B+** | Yellow | Cut penultimate paragraph of Scene 7 (Janeway-rhetoric omniscient-captain) |
| 05 | Day Twenty Realization | **B+** | Yellow | Fix Scene 5 aphoristic close ("The sentence stands as it is" → forward motion) |
| 06 | First Surface, First Forsaken Reveal | **B+** | Yellow | Add one concrete particular about Stefan to wardroom reflection |
| 07 | Joel's Sunfish | **B+** | Yellow | Cut 3rd sentence of "architecture's discipline" block + vary "shape had been the source" motif (×4 → ×2) |
| 08 | Second Submersion | **D+** ⚠️ | **RED** | **PRE-BOBIVERSE.** Rewrite wardroom reflection in full Anna-register; cut to "the hum would continue" close |
| 09 | Sync Daemon Under Drift | **B+** | Yellow | Bobiverse rewrite pass on lines 32–180 + compress Joel self-assessment lines 256–288 to 60% |
| 10 | Aftermath | **B** | Yellow | Cut "I am, tonight, writing it down for the first time" from section 3 close (resolves AP-6) |
| 11 | Second Surface, Second Forsaken Reveal | **C+** | Yellow | Compress Joel cup-scene interior from ~250 words to ≤80 |
| 12 | Beginning of the End | **D+** ⚠️ | **RED** | **PRE-BOBIVERSE.** Add parenthetical aside to Anna's "no Surface 3" realization (Scene A, paras 56-60) |
| 13 | Schema That Should Not Migrate | **B-** | Yellow | Insert 150-200 word interiority restoring class/region rail between pass-3 and pass-4 |
| 14 | The Crossing | **B+** | Yellow | Tighten porthole-look passage from 7 paragraphs to 3 + register overuse pass |
| 15 | Compromised Relay Holds | **B+** | Yellow | Compress forensic-query timestamp arithmetic from ~700 → ~400 words |
| 16 | Final Ascent | **B+** | Yellow | Cut meta-commentary sentence + replace double-register sentence in Joel scene |
| 17 | Transit North | **B+** | Yellow | Reduce "at the standing [noun]" formula from ~38 → ~15 instances |
| 18 | Punta Arenas Surfacing | **B+** | Yellow | Apply register anti-pattern #9 pass (40-50 substitutions on 83 instances) |

**Distribution:**
- A-: 2 chapters (ch01, ch02)
- B+: 11 chapters
- B: 1 (ch10)
- B-: 1 (ch13)
- C+: 1 (ch11)
- D+: 2 chapters ⚠️ PRE-BOBIVERSE (ch08, ch12)

**Median: B+.** No chapter scores GREEN on NYT-profile readiness; 2 score RED.

---

## 2. Volume-wide pattern clusters

The 18 subagents converge on **7 recurring failure modes** that cross chapter boundaries. These are the high-leverage volume-wide passes:

### Cluster 1 — Register-family overuse (HIGH severity, 5 chapters)

Despite the 2026-05-20 Yeoman sweep that reduced volume-wide instances from ~600 → ~46, several chapters still exceed the ≤3 hard cap:

- **ch18** (83 instances — sweep did not apply, BLOCKER)
- **ch14** (10+ instances)
- **ch07** (4 motif uses of related "shape")
- **ch13** (uncounted; pre-2026-05-20)
- **ch11**, **ch06**, **ch08** at or above cap

**Root cause:** The Yeoman sweep targeted specific chapters; ch18 and ch14 either weren't swept or had material added after. The 2026-05-20 ANNA-VOICE.md anti-pattern #9 needs a second-wave enforcement pass.

**Fix:** Dispatch a Yeoman re-sweep targeting ch11, ch13, ch14, ch18 specifically.

### Cluster 2 — Aphoristic closes (anti-pattern #1, 4 chapters)

Janeway-rhetoric packaged-truth closes recur:
- **ch01** paragraph 4 close + parka paragraph
- **ch05** Scene 5 ("The sentence stands as it is") + Scene 8 ("It will not be rewritten")
- **ch10** self-referential frame doubled (§ 2 and § 5)
- **ch16** meta-commentary "The list was the structural device the record would carry"

**Fix:** Single Yeoman aphoristic-close audit pass across these 4 chapters; substitute forward-motion beats per ANNA-VOICE.md anti-pattern #1.

### Cluster 3 — Pre-Bobiverse chapters (CRITICAL, 2 chapters)

**ch08** and **ch12** flagged D+/RED. Both are competent naval briefs without Anna's parenthetical-aside engine. The structural architecture is sound; the voice is absent.

- ch08: ~5,000 words, 0 parenthetical asides, ~11+ "the way X" motif violations
- ch12: 6 scenes, Anna's wry register absent from 5 of them

**Fix:** Dedicated Bobiverse-warmth pass on ch08 + ch12 (similar to the ch03 pilot). Insert 4-6 parenthetical asides per chapter targeting the moments of highest ironic density. Highest priority volume edit.

### Cluster 4 — "At the standing [noun]" formula saturation (2 chapters)

- **ch17** (~38 instances in 4,963 words)
- **ch18** opening pages (≥14 instances in 5 paragraphs)

**Fix:** Cap to ≤8 per 500 words in institutional-log-register scenes; pass scoped to these two chapters.

### Cluster 5 — Over-explanation of own irony (3 chapters)

Anna narrating the function of her own restraint:
- **ch07** Scene F "The architecture's discipline was the source's discipline" (3-sentence block; cut 3rd)
- **ch11** "Forsaken" never named in body (title promises a reveal not delivered)
- **ch17** "I did not narrate the connection" (which is itself narrating)
- **ch16** "The list was the structural device the record would carry"

**Fix:** Trust the reader; cut the meta-narration sentences. Single-pass audit.

### Cluster 6 — Anaphora / tricolon over-use (3 chapters)

- **ch03** Wanjiru tricolon close ("That is X. That is Y. That is why I had picked them both")
- **ch10** three-inverses section ("Three architectural inverses. One in X. One in Y. One in Z.")
- **ch18** opening "at the standing" run

**Fix:** ANNA-VOICE.md anti-pattern #4 enforcement pass.

### Cluster 7 — Sensory gaps (multi-sense imagery LD-3, 5 chapters)

Chapters running auditory/cognitive only:
- **ch09**, **ch11**, **ch13**, **ch15**, **ch17**

**Fix:** Per-chapter sensory-anchor insertion (1-2 short physical details per chapter). Single Yeoman pass.

---

## 3. Prioritized edit roadmap

Ordered by leverage-per-effort:

### Tier 1 — BLOCKERS (do first)

1. **ch08 Bobiverse-warmth pass** — D+ → B+; single chapter pull-up
2. **ch12 Bobiverse-warmth pass** — D+ → B+; single chapter pull-up
3. **ch18 register sweep (83 instances)** — A-pattern #9 enforcement; chapter pull-up B+ → A-

### Tier 2 — VOLUME-WIDE PASSES (do next, single-pass each)

4. **Register-family re-sweep** (ch11, ch13, ch14, ch18) — close residual gaps from 2026-05-20 sweep
5. **Aphoristic-close audit** (ch01, ch05, ch10, ch16) — anti-pattern #1
6. **Meta-narration audit** (ch07, ch11, ch16, ch17) — cut Anna-narrating-own-irony sentences
7. **Anaphora/tricolon enforcement** (ch03, ch10, ch18) — anti-pattern #4

### Tier 3 — TARGETED PER-CHAPTER (do where time allows)

8. **ch11 Joel cup-scene compression** (250 → ≤80 words)
9. **ch13 class/region rail restoration** (150-200 word interiority insert)
10. **ch14 porthole-look passage tighten** (7 paragraphs → 3)
11. **ch15 forensic-query timestamp compress** (~700 → 400 words)
12. **ch17 "at the standing" reduction** (~38 → ~15)

### Tier 4 — CANONICAL PLANTS (review needed)

13. **ch01 canonical plants** — outline specifies 3 plants currently absent (Joel bunk-laptop disclosure, Wanjiru key-handover, off-the-shelf sensor procurement). Decision: install, defer to vol-3, or accept absence.
14. **ch11 "Forsaken" never named in body** — single sentence at comm-space door beat (line 165). PAO ruling needed.

---

## 4. Per-chapter strengths worth preserving

Chapters with passages flagged as "the volume's best" — protect from over-editing:

- **ch01** chemistry-rack scene + "the correctness was useless" firmware paragraph + "Mikael took two" payoff
- **ch02** Joel four-sentence lease-layer scene + vatrushka close
- **ch03** Diego bridge-wing scene + Priya fourth-pass scene + Diana/Liteyny Prospekt interlude
- **ch04** "Priya is the migration we are not running today" + wind-silence at 150m
- **ch05** Three-recognition escalation + cold-tea motif five-fold work
- **ch06** Wanjiru exception-refusal scene (paras 74-91)
- **ch07** "Acknowledged" triple landing + soft-case structural symbol
- **ch10** Havránek chain sentence + Aytib Qoy
- **ch11** Wanjiru lines 113-117 ("She would say none of these things")
- **ch13** Pattern B log differential + "That is why I am here"
- **ch14** Corridor push + Maria's three-check + Diego's letter ("Volveré.")
- **ch15** 1648 cabin exchange + "I did not mourn the GPU."
- **ch16** "Some questions we asked the system; some questions we wrote down to ask later" + dried Uzbek melon
- **ch17** H.G. Wells convention irony + Diego's letter scene
- **ch18** Diego gangway scene ("The architecture had not preserved Diego. Diego had preserved Diego.") + Wanjiru "the drafting will begin" + Hiroshi's unfinished line

These are the load-bearing passages. Edit *around* them.

---

## 5. Cost report

| Component | Model | Tokens (sum) | Approx cost |
|---|---|---|---|
| Per-chapter fan-out (18 × Sonnet 4.6 medium) | sonnet | ~1.6M (input+output) | ~$5–$8 |
| Consolidation (Opus 4.7 xhigh, this artifact) | opus | ~150k | ~$1–$2 |
| **Total volume UPF (bestseller-profile)** | | | **~$6–$10** |

Within the $3–$8 envelope projected in `bestseller-profile-review.yaml` (slightly over due to ch11/ch15/ch18 running longer than median).

---

## 6. Recommended next step

**Dispatch Tier-1 BLOCKER work first:**

1. Yeoman Bobiverse-warmth pass on **ch08** (model the pass on the successful ch03 pilot)
2. Yeoman Bobiverse-warmth pass on **ch12** (same template)
3. Yeoman register-sweep extension on **ch18** (83 instances → ≤3 cap)

After Tier 1 completes, re-run this pipeline on just the modified chapters to verify pull-up. Tier 2 + Tier 3 can proceed in parallel under Yeoman dispatch.

**Per-chapter full reports:** see `.pao-inbox/_state-snapshots/2026-05-20-upf-{ch}-bestseller-profile.md` for each of the 18 chapters.

---

— PAO, 2026-05-20T22:50Z
