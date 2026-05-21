---
type: upf-evaluation
chapter: ch03-drake-passage-ice-edge
date: 2026-05-21
evaluator: PAO
rubrics: [literary-devices, nyt-bestseller-profile]
pass-number: 2
baseline: 2026-05-20-upf-ch03-drake-passage-ice-edge-bestseller-profile.md
edits-applied: wave-7-uPF-recommendations
overall-grade: A-
nyt-readiness: yellow
highest-leverage-edit: discipline-motif-still-overruns-in-joel-scene
---

# UPF v2 — Ch03 "Drake Passage and the Ice Edge"

## Live-Grep Mandate Results

**NOTE: The standard `sed '/^---$/,/^---$/d'` frontmatter-strip command is WRONG for this chapter.**
The chapter body contains two literal `---` horizontal rules (raw lines 124 and 190). The sed command treats them as frontmatter delimiters, silently deleting body text between lines 124 and 190. This drops the entire Priya lab scene + Joel scene from the strip. Correct command: `perl -0777 -pe 's/^---\n.*?---\n//s'` (strips only the first frontmatter block).

All counts below are verified against the corrected strip.

### Confirmed counts (body only, frontmatter + HTML comments stripped)

| Pattern | Live count | Cap / threshold |
|---|---|---|
| `register` (all forms) | **3** | ≤3/chapter (ANNA-VOICE AP9) |
| `\bdiscipline\b` (all instances) | **8** | no hard cap; motif-overuse judgment |
| `\bthe discipline\b` | **4** (see breakdown) | AP5: no motif phrase >1/chapter in close proximity |
| Wanjiru tricolon close ("That is what the architecture is") | **0** | Wave 7 cut — confirmed |
| Both of them took it | **1** (line 156) | Wave 7 varied — confirmed |
| She didn't come up for him | **1** (line 158) | Wave 7 varied — confirmed |
| Joel post-rehearsal compression | **1 sentence** (line 192) | Wave 7 compressed — confirmed |
| Aphoristic closures | **0** | Clean |
| "We are all of us..." universals | **0** | Clean |

### Discipline breakdown by scene

1. **Wanjiru scene** (lines 112, 114 × 2): "The discipline ran through both of them." + "The architecture's discipline was Wanjiru's discipline made portable." — 3 instances across two adjacent paragraphs.
2. **Priya close** (line 166): "The discipline was where it belonged." — 1 instance. Wave 7 fix confirmed: "The discipline took both" → "Both of them took it" and "The discipline did not lift for him" → "She didn't come up for him."
3. **Joel callback** (line 188): "recognize the discipline I am describing here. It is the same discipline that produced the four sentences on the call. It is the same discipline that produced the rewrite of the lease protocol" — 3 instances in consecutive sentences.
4. **Diana/ice-edge** (line 204): "against my discipline" — 1 instance. This is adverbial, not the motif sense.

**Verdict on discipline:** The Priya scene overrun is fixed (3 instances → 1). Two new clusters now carry the risk: (a) Wanjiru's adjacent "The discipline / The architecture's discipline / Wanjiru's discipline" run (3 in two paragraphs) is a borderline AP5 case — the double instance in "architecture's discipline was Wanjiru's discipline" is a single-sentence semantic comparison, not a rhetorical loop, which mitigates it; (b) Joel's three "the discipline / same discipline / same discipline" in consecutive sentences is the new highest-risk cluster. ANNA-VOICE AP5 caps motif phrases at one per chapter; this run of three is within a single paragraph and is intentional (the callback structure needs the phrase to land thrice), but it reads as close to the line as the Priya overrun did in v1.

### Register breakdown by instance

1. **Wanjiru** (line 114): "said the same sentence in the human register" — noun-as-tone, load-bearing architectural comparison.
2. **Joel intro** (line 170): "the title was a register-marker, not a deference" — noun compound, character observation.
3. **Joel callback** (line 188): "in its operational register" — noun-as-tone, callback to Bobiverse pilot insertion.

Count = 3. Exactly at the ≤3 cap from ANNA-VOICE AP9. No violation, but there is no headroom. Any future edit that adds a "register" instance breaks the cap.

---

## Stage 0: What Changed (v1 → v2)

Wave 7 edits applied 2026-05-20 per UPF v1 recommendations:

1. **Wanjiru tricolon close cut.** "That is what the architecture is. That is what Wanjiru is. That is why I had picked them both." → "I went below and logged it in those words." Confirmed in body (0 matches for "That is what the architecture is").

2. **Priya discipline motif varied.** "The discipline took both" → "Both of them took it" (line 156). "The discipline did not lift for him, or for the Mission Director either" → "She didn't come up for him, or for the Mission Director either" (line 158). "The discipline was where it belonged" kept (line 166). Confirmed in body.

3. **Joel post-rehearsal paragraph compressed.** ~120-word confirmation paragraph → one sentence: "The rehearsal held. Joel briefed me at sixteen-forty and confirmed the comparison was now a recorded fact." (line 192). Confirmed in body.

---

## Stage 1: Scene-by-Scene Re-Grading

### Scene 1: Drake crossing (opening)

GRADE: **B+** (unchanged from v1)

No edits applied. The "now as the woman in command" opener still carries faint self-consciousness against ANNA-VOICE's "she's past that" principle. This is the chapter's most persistent unresolved note and is sub-threshold for a required fix.

### Scene 2: Sabina

GRADE: **A-** (unchanged from v1)

The three-beat "Sabina did the work. I logged it. I returned to the deck." close remains. It is not technically a rhythm-tricolon (three functional actions, not parallel abstractions) and the v1 judgment holds: borderline but within spec.

### Scene 3: Diego

GRADE: **A** (unchanged from v1)

No relevant edits. Still the chapter's model crew scene.

### Scene 4: Hiroshi

GRADE: **B** (unchanged from v1)

"Hiroshi's calm is contagious in the way other officers' anxiety is contagious" remains. The symmetric structure (calm/anxiety as parallel contagions) is still the chapter's closest brush with AP4 (parallel-structure tricolon), though it is a two-part comparison, not a three-part. Unchanged; still within spec; still the thinnest scene.

### Scene 5: Wanjiru

GRADE: **A-** (upgraded from B+)

The tricolon close removal is the single largest improvement in the chapter. "The architecture's discipline was Wanjiru's discipline made portable. I went below and logged it in those words." — the concrete physical close ("logged it in those words") is exactly the ANNA-VOICE-compliant ending the v1 analysis called for. The architectural claim is made; it is not over-made.

Remaining note: the double "discipline" in "The architecture's discipline was Wanjiru's discipline" is a single sentence comparing two entities. This is functional, not rhetorical — the sentence earns both uses. The broader Wanjiru scene now has 3 "discipline" instances across two paragraphs (the Wanjiru-discipline double + "The discipline ran through both"), which is dense but not the AP5 shape (AP5 targets motif-phrase repetition as a rhetorical device, not semantic reference). Within spec.

### Scene 5B: Wanjiru exposition block

GRADE: **B+** (upgraded from C+ shadow in v1)

The "I want to name what that means..." exposition block retains its one genuinely lecture-adjacent sentence: "An attestation is what you say when you cannot afford for the next person to misunderstand the state of the world." This is Anna defining a term for the reader — it is warranted by the architectural load but it is the chapter's most textbook-adjacent sentence. Not a violation; a note.

### Scene 6: Priya

GRADE: **A** (upgraded from A-)

The discipline motif overrun is resolved. The three prior instances collapsed to one ("The discipline was where it belonged"), which is the correct closing beat. The Priya scene is now the chapter's most technically clean scene — character specificity, multi-sensory rendering, Bobiverse-direct address, earned payoff, zero anti-pattern violations.

"She didn't come up for him, or for the Mission Director either" (line 158) — the shift from "The discipline did not lift for him" to "She didn't come up for him" is a real improvement: the new version is action-based, in Anna's functional register, and the subject is Priya-as-person rather than "the discipline" as an abstract force.

### Scene 7: Joel

GRADE: **B** (downgraded from B+ in v1 because the compression reveals a new concern)

**Positive:** The post-rehearsal compression is exactly right. "The rehearsal held. Joel briefed me at sixteen-forty and confirmed the comparison was now a recorded fact." (line 192) is tight and earns the "recorded fact" callback without the procedural stage-direction padding.

**New concern:** The Joel callback paragraph (line 188) contains "recognize the discipline I am describing here. It is the same discipline that produced the four sentences on the call. It is the same discipline that produced the rewrite of the lease protocol" — three "discipline" instances in consecutive sentences, two of which share the "It is the same discipline" construction. This is not the AP4 shape (parallel tricolon for rhythm) but it IS an anaphoric run: "It is the same discipline... It is the same discipline..." is a two-instance anaphora (ANNA-VOICE permits runs of 2; 3 would be a violation). The run is exactly at the allowed limit.

Additionally, the Joel callback paragraph uses "discipline" THREE times, and the chapter already uses it 5 other times across Wanjiru and Priya/Diana. Total chapter body count: **8**. This is not technically a capped count, but it is a frequency that a careful reader may notice as a recurring word. The word "discipline" is now the chapter's most prominent cross-scene motif — it connects Wanjiru (attestation discipline), Priya (calibration discipline), and Joel (architecture discipline). This is thematically coherent, but the 8-count makes it feel authored rather than natural.

**Register count:** At 3/chapter, exactly at cap. "In its operational register" (Joel) is the most exposed instance because it's the Bobiverse pilot insertion's explicit callback construction ("You are watching it now in its operational register") — it works in context but it is the instance most likely to land as constructed prose for an attentive reader. Not a violation; noted.

### Scene 8: The Edge — Day 7

GRADE: **A-** (unchanged from v1)

No relevant edits. Diana/Liteyny interlude remains the chapter's highest-leverage emotional beat. The "I went below" close continues to be correct (ANNA-VOICE short-sentence close) and continues to be slightly anticlimactic after the extended inventory. The final inventory ("The relay was up. The gossip protocol was current...") reads as a checklist on the page but should serve well at audiobook pace — the rhythmic accumulation works better spoken than read. Unchanged judgment.

---

## Stage 2: Literary Anti-Pattern Scan (updated)

| AP | v1 status | v2 status | Change |
|---|---|---|---|
| AP4 (parallel-structure tricolon) | WARN (Wanjiru close) | CLEAR | Tricolon removed by Wave 7 |
| AP5 (motif phrase overuse) | WARN (discipline ×3 Priya) | BORDERLINE (discipline ×3 Joel consecutive) | Priya fixed; Joel now the exposure |
| AP5 (motif phrase overuse) | — | NEW NOTE (discipline 8× chapter-wide) | Frequency rather than local cluster |
| AP13 (confidence without evidence) | BORDERLINE (Wanjiru) | CLEAR | Concrete close replaces tricolon statement |
| AP1 (serial dependency) | FLAG | unchanged | Inherent to volume structure |

**Net AP posture:** v2 clears the v1 violations. One new borderline (Joel discipline run). No new violations introduced.

---

## Verification (Pass/Fail, updated)

**Literary Devices Rubric:**

| Item | v1 Grade | v2 Grade | Delta |
|---|---|---|---|
| Clear, consistent POV | PASS | PASS | — |
| Distinct tone and diction | PASS | PASS | — |
| Effective multi-sense imagery | PASS/WARN | PASS/WARN | — |
| Fresh metaphors/similes | PASS | PASS | — |
| Symbolism/motifs | PASS | PASS | — |
| Foreshadowing without telegraphing | PASS | PASS | — |
| Irony deepening meaning | PASS | PASS | — |
| Structural devices | WARN | WARN | section headers + `---` dividers unchanged |

**Overall Literary Devices Grade: A-** (upgraded from B+)
The Wanjiru tricolon removal and Priya discipline fix are both real improvements that push the chapter from the B+ range. The remaining notes (Joel discipline run, Hiroshi contagious-symmetry, discipline 8×-chapter-wide) are sub-threshold.

**NYT Bestseller Profile Rubric:** unchanged from v1. YELLOW.

---

## Delta Verdict: Did May 20 Edits Land?

**Yes, substantively.** The three Wave 7 edits all landed correctly in the body:

1. Wanjiru tricolon → concrete close: **landed cleanly.** The close is now the chapter's strongest architectural moment: the action (attestation exchange) + the explanation (exposition block) + the physical anchor ("I went below and logged it in those words") work as a complete three-part movement. AP13 borderline is resolved.

2. Priya discipline overrun → varied: **landed.** "Both of them took it" and "She didn't come up for him" are better prose in both cases — more functional, more in character, less rhetorical. The remaining "The discipline was where it belonged" is the correct instance to keep.

3. Joel compression: **landed cleanly.** The single sentence is tighter and the "recorded fact" callback lands without padding.

**One new finding from the live-grep audit:** the Joel callback paragraph's triple "discipline" run was not visible in the v1 analysis because the standard sed frontmatter strip was silently deleting the paragraph (body `---` dividers were being parsed as frontmatter delimiters). This is a **new finding in v2** that was missed in v1. The Joel paragraph is clean for AP-purposes (anaphora of 2, not 3; no rhythm-tricolon), but it does add to the chapter-wide discipline frequency (8 instances total), and the "same discipline × 2" construction is the chapter's most explicit rhetorical marker.

---

## Top 3 Strengths (re-cited for v2)

**1. Wanjiru scene is now the chapter's best technical payoff.** With the tricolon removed, "The architecture's discipline was Wanjiru's discipline made portable. I went below and logged it in those words." is a clean, concrete, Anna-register close that delivers the architectural claim without over-delivering it. The action → explanation → anchor three-part movement is the chapter's most disciplined structural execution.

**2. Priya scene is the chapter's most technically clean scene post-Wave-7.** Character specificity (audible weight, counting under breath), Bobiverse-direct address ("You will hear, in the months that come..."), earned payoff, the "naming is for the staff history — you are the reason it exists" close — all present, no anti-pattern violations, the discipline overrun resolved.

**3. Diego remains the chapter's model character scene.** Unchanged from v1. The bridge-wing setting, four-boat backstory, Otago transducer anecdote, and Day 28 plant are collectively the cleanest crew scene in the first three chapters.

---

## Weaknesses (v2 residuals)

**1. Joel callback paragraph discipline density.** "It is the same discipline... It is the same discipline" — a two-instance anaphoric run is permitted by ANNA-VOICE spec, but at the chapter's 8th and 9th uses of the word it lands as a device rather than a character observation. Fix if needed: replace "It is the same discipline that produced the four sentences on the call" with "The four sentences on the call came from the same place." Reduces by 1 instance, breaks the anaphoric run.

**2. Hiroshi scene sensory deficit (unchanged).** The scene is appropriately thin but "Hiroshi's calm is contagious in the way other officers' anxiety is contagious" still reads symmetrically constructed. The watch cadence close ("The watch ran on his tempo") is correct but the penultimate sentence remains the chapter's closest AP4 brush.

**3. "Register" at cap with no headroom.** Three instances (human register / register-marker / operational register) exactly at the ANNA-VOICE ≤3/chapter cap. Any future edit that adds a fourth instance — including a revision to any of the five scenes that currently don't use it — would push into violation territory. Not a fix now; a flag for future chapter revisions.

---

## Literary Devices Grade: v1 vs v2

| Version | LD Grade | Notes |
|---|---|---|
| v1 (baseline 2026-05-20) | B+ | Wanjiru tricolon (AP4), Priya discipline overrun (AP5), Joel flatness |
| v2 (post-Wave-7 2026-05-21) | A- | AP4 clear, AP5 Priya clear; new Joel discipline density note; no violations |

---

## NYT Readiness: v1 vs v2

| Version | NYT Readiness | Notes |
|---|---|---|
| v1 | YELLOW | Structural position (crossing chapter, not hook chapter) |
| v2 | YELLOW (unchanged) | Wave 7 edits improve prose craft; don't change the chapter's commercial profile |

The commercial caution is structural, not craft-level. Priya and Diana/Liteyny remain the two strongest excerpt candidates.

---

## Single Highest-Leverage Edit (v2)

**Reduce Joel discipline anaphora.** Replace one of the two "It is the same discipline that produced X" sentences with a non-"discipline" construction. Suggested: "The four sentences on the call came from that same place. It is the same discipline that produced the rewrite of the lease protocol after the council placed the hold." (removes one "discipline" instance and breaks the anaphoric doubling while preserving the callback's function). Cost: one sentence rephrase, ~10 words.

This is the chapter's only remaining technically addressable weakness. The Hiroshi scene thinness and "register at cap" are acknowledged but sub-threshold for required fixing.
