---
title: Prose-telemetry metric improvements plan
date: 2026-05-14
status: in-progress (Phases H + I delivered 2026-05-15; A-G awaiting CO greenlight)
quality-rubric: A
author: Yeoman
supersedes: -
related:
  - build/prose_telemetry_handcount.py (the detector module)
  - galley/prose/lib/prose_telemetry/ (spaCy-tier sibling)
  - .pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md (platform decision)
---

> **Delivery log:**
> - **2026-05-15** - Phase H (`redundant_explicit_predicate` detector) shipped into galley's registry pipeline. Added as 79th detector; family `voice`, tier `stdlib`. 9 unit tests green. Validated against vol-2 ch02 (caught the "I was not disappointed → I was not." case) and vol-2 ch01 (4 hits surfaced, ~50% precision on real prose). Section appended at the end of this plan as **Phase H - Delivered**.
> - **2026-05-15** - Phase I (Gradient thresholds for spaCy detectors) shipped. Replaced binary stopword sets in `nominalization` and `distributed_chiasmus` with per-lemma soft caps (nominalization - counted detector) and reduced-confidence pairs (chiasmus - one-shot detector). New output fields `high_confidence_count`, `weighted_count`, `over_cap_by` give downstream tools the granularity to distinguish content vocabulary from over-use. Verdict logic uses high-confidence count for chiasmus warning trigger. 294 tests pass. ch01 and ch02 both verdict=green with rich gradient signal preserved in JSON for author audit. Section appended as **Phase I - Delivered**.

# Prose-telemetry metric improvements

## Context & Why

After running the full detector suite against ch02 through six edit passes today, the metric output has signal but ~30% noise - the verdict trips on raw-count thresholds that don't scale with chapter length, the `comma_splice` detector emitted 3 false positives out of 3 hits, and Anna's most-flagged prose problem (recursive same-noun-in-sentence) is only partially caught by `proximity_echo`. The detectors are individually thoughtful; the **verdict layer and a handful of heuristics** are where the noise lives. This plan addresses the verdict layer plus three new detectors that close gaps where current metrics miss real prose defects.

## Recommended approach

**Refactor the `verdict()` function to use density-normalized thresholds**, **tighten three false-positive-heavy detectors**, and **add four new detectors** that close gaps the current suite cannot see. No new detector types beyond stdlib + existing regex/Counter idioms - this is a Phase-2 tuning pass, not a Phase-3 platform expansion.

## Success criteria

- **Verdict noise reduction**: re-running the updated suite against ch02 reduces blocker count from 4 → ≤2 without changing held_lines.json
- **False-positive elimination**: `comma_splice` false-positive rate drops from 3/3 (100%) to ≤1/3 (33%) on ch02 (or detector downgrades to never-blocker)
- **New-detector validation**: recursive-noun detector flags ≥3 of the prose patterns I hand-edited today; reverse-order detector flags ≥1 of the "The table was the table" family
- **Cross-chapter rerun**: ch01 + ch02 + ch05 + ch10 all run cleanly with new thresholds; no chapter that previously passed now fails
- **No regression**: every detector previously catching a real defect (tautology, retired motif, filter word, redundant phrase) still catches it

### FAILED conditions (kill triggers)

- If reducing false positives in `comma_splice` drops detection of a real splice (would need a fixture chapter with a known splice)
- If new recursive-noun detector flags > 15 hits/chapter average across the corpus - it's over-firing, threshold needs tuning
- If verdict-density normalization causes any chapter currently flagging real loops to suddenly pass clean
- 4-hour total implementation budget; if Phase A exceeds 2 hours, stop and reassess

## Assumptions & validation

| Assumption | Validate by | Impact if wrong |
|---|---|---|
| `count_per_1k_tokens` already exists on every metric record (verified L1697 `meters()`) | grep `count_per_1k_tokens` in handcount module | Have to compute it in verdict instead - adds ~10 lines |
| Held-lines mechanism still works after threshold change | Re-run with held-lines exempting "He did not" paragraph | Whole held-lines layer breaks; would need parallel update |
| ch02 is representative of the prose Anna writes (calibration set) | Sanity check against ch05 + ch10 which are differently structured | Thresholds calibrated to one chapter overfit |
| spaCy-tier galley sibling (`galley/prose/lib/prose_telemetry/`) is independent - won't conflict | Read its detector list | Duplicated detectors firing twice |

## Phases

### Phase A - Verdict layer: density-normalized thresholds

**Scope:** `prose_telemetry_handcount.py`, function `verdict()` only.

**Changes:**
1. Replace raw-count blocker triggers with `per_1k_tokens` density triggers for: `bigram_chain_loop`, `lexical_chain_loop`, `statement_then_reversal`, `trigram_chain_loop`, `proximity_echo`.
2. Compute density at verdict time using `word_count` from `doc` (already in scope).
3. Calibrated thresholds (initial cut, will tune):
   - `bigram_chain_loop`: blocker at `per_1k > 1.0` (currently raw ≥ 5; for 6k chapter that's 0.83/1k - close to current effective)
   - `lexical_chain_loop`: blocker at `per_1k > 3.5` (currently raw ≥ 20 = 3.3/1k)
   - `statement_then_reversal`: blocker at `per_1k > 0.55` (raw ≥ 3 in 6k = 0.5/1k)
   - `trigram_chain_loop`: blocker at `per_1k > 0.8` (raw ≥ 5 in 6k)
   - `proximity_echo`: warning at `per_1k > 6.0`, blocker at `per_1k > 9.0` (currently 8.0/1k in ch02 - would be warning, not blocker)
4. Said-tag normalization: compute `said_tags_per_dialogue_line` not `per_1k_tokens`. Need to count dialogue lines (lines containing italicized quoted speech or `"..."`). New helper `count_dialogue_lines(prose) -> int`.

**Gate:** Phase A passes when ch02 verdict drops from 4 blockers → ≤ 2, and ch01 + ch05 verdicts don't regress (no previously-clean chapter newly fails).

### Phase B - False-positive cleanup in three high-noise detectors

**Scope:** `detect_comma_splices`, `detect_passive_voice`, `detect_paragraph_length_anomaly`.

**Changes:**

1. **`detect_comma_splices`**: extend the "skip if" rules to recognize introductory adverbials before the comma:
   - Add skip-if: clause before the comma starts with a participle (`-ing` / `-ed`), a temporal subordinator (`When|If|Once|After|Before|Each time|Eventually|At first`), or is a one-word adverbial (`Looking|Watching|Listening|Eventually|Finally|Meanwhile`)
   - Skip-if: comma is preceded by italics-close `*` or quote-close `"` (dialogue tag)
   - Downgrade detector confidence from `0.5` → `0.4`
   - Verdict: never blocker; warning only

2. **`detect_passive_voice`**: expand `_PASSIVE_FALSE_POSITIVES` set to ~30 common adjectival-past-participle constructions (`was finished`, `was tired`, `was confused`, `was tied`, `was situated`, `was located`, `was opposed`, `was supposed to`, `was used to`, `was allowed to`, `was forced to`, `was meant to`, `was bound to`, `was inclined to`, `was prepared to`, `was concerned`, `was interested`, `was surprised`, `was pleased`, `was disappointed`, `was satisfied`, `was attached to`, `was related to`, `was familiar with`, `was aware of`, `was responsible for`, `was capable of`, `was guilty of`, `was worth`).

3. **`detect_paragraph_length_anomaly`**: replace mean × multiplier with median + IQR (1.5 × IQR rule):
   - Compute Q1, Q3, IQR across paragraph word counts
   - Flag paragraphs where word_count > Q3 + 1.5×IQR OR word_count < max(8, Q1 - 1.5×IQR)
   - Floor of 8 prevents flagging legitimate short beats like "He waited."

**Gate:** Phase B passes when ch02 `comma_splice` flags ≤ 1 hit (down from 3) AND `paragraph_length_anomaly` flags only paragraphs that are genuinely outliers (visual inspection of the 9 currently-flagged).

### Phase C - New detector: recursive same-noun-in-sentence

**Scope:** one new function `detect_recursive_noun(prose: str) -> list[dict]`.

**Heuristic:**
- For each sentence, find content nouns ≥ 5 chars that appear ≥ 2 times within the same sentence
- Token distance between occurrences must be ≥ 8 (otherwise `proximity_echo` already caught it)
- Token distance ≤ 30 (beyond that, audibility drops)
- Skip proper nouns (capitalized mid-sentence) and stopwords
- Confidence 0.8

**Catches the patterns from today's pass:**
- "a question I had been carrying for five months without raising it to a question" (question … question, 12 tokens apart)
- "had not been measuring myself against the version of me my mother had once told me the neighbor's daughter was becoming" - would flag if "version" or "daughter" recurred, which it now doesn't (Tier 1 fix)
- "what I named it after on the boat than on a video call" (after … after, but only 4 tokens apart - `proximity_echo` catches this already)

**Verdict:** warning at any hit, blocker at ≥ 4 (per_1k tunable).

**Gate:** Phase C passes when the detector finds ≥ 3 of the patterns I hand-edited today on the pre-edit version of ch02 (validation by running against git HEAD~6 of the chapter).

### Phase D - New detector: reverse-order / postposed-cause

**Scope:** one new function `detect_reverse_order(sents: list[str]) -> list[dict]`.

**Heuristic** (intentionally loose; this is a flag-not-prove detector):
- For each sentence:
  - Find the first complete subject-verb-object (heuristic: first noun-phrase followed by main verb followed by object/complement)
  - Measure tokens after the SVO
  - Look for a **causal/temporal anchor** in the tail: `when`, `because`, `after`, `before`, `while`, `since`, `the way I had`, `in the week`, `the year`, `the day`
  - Flag if: SVO is in first 1/3 of sentence AND tail contains causal-temporal anchor AND tail length > 25 tokens
- Confidence 0.6

**Catches:**
- "I had read it the first time at a kitchen table in St. Petersburg in November, in the week after my mother's hospital admission, when I was already going to need the paper to be true and was prepared to be disappointed by it." - SVO in tokens 1–5, "when" anchor at token ~28

**Verdict:** warning only (never blocker - this is high-false-positive territory; meant for human review, not auto-rejection).

**Gate:** Phase D passes when the detector flags ≥ 1 sentence from ch02 pre-edit-version that matches the "reverse-order" family. Acceptable false-positive rate up to 50% since output is review-only.

### Phase E - New detector: negative-construction density

**Scope:** one new function `detect_negative_constructions(prose: str, total_words: int) -> list[dict]`.

**Heuristic:**
- Count: `\b(had|did|was|were|is|are|will|would|could|should|might|do|does|has|have)\s+not\b` per 1k tokens
- Also count contracted forms: `\b(hadn't|didn't|wasn't|weren't|isn't|aren't|won't|wouldn't|couldn't|shouldn't|mightn't|don't|doesn't|hasn't|haven't)\b`
- Combined per_1k density
- Confidence 1.0 (exact match)

**Verdict:** Anna's baseline (computed empirically from ch01 + ch02 today as ~12/1k); flag at > 18/1k = warning, > 25/1k = blocker. Tune after baseline established.

**Gate:** Phase E passes when ch02 reports negative-construction density and the climactic "He did not" paragraph (already held) doesn't change the chapter-level verdict.

### Phase F - New aggregate metric: sentence-length rhythm

**Scope:** extend `document_metrics()` to compute coefficient of variation.

**Changes:**
- Compute `std_dev / mean` of sentence lengths
- Report as `sentence_length_cv` in document_metrics
- Verdict: warning if `cv < 0.3` (monotonous prose) or `cv > 1.3` (chaotic alternation)
- Anna's expected band: 0.6 – 0.9

**Gate:** Phase F passes when ch02 reports a CV in the Anna band (0.6–0.9) and dashboards display the new field.

### Phase G - New detector: em-dash density per paragraph

**Scope:** one new function `detect_emdash_density(prose: str) -> list[dict]`.

**Heuristic:**
- For each paragraph, count em-dashes (`-` and ` - `)
- Flag paragraphs with em_dash_count ≥ 4 OR (em_dash_count / sentence_count) > 0.5
- Confidence 1.0

**Verdict:** informational; flag at ≥ 3 paragraphs over the per-paragraph threshold.

**Gate:** Phase G passes when ch02 reports em-dash density and at least one paragraph with high em-dash count is surfaced.

## Verification

### Automated

- Each new detector ships with a unit test in `build/test_prose_telemetry.py` (currently exists; check) with at least 2 positive and 2 negative fixtures
- Cross-chapter regression: run measure on ch01, ch02, ch05, ch10 before-and-after; diff metric JSON; no chapter that passed before fails after (except by intentional new-detector firing)
- Held-lines regression: ch02 held-lines exemptions still suppress the right counts

### Manual

- Visual review of new detector findings against ch02 prose: are the flagged spans actually problems?
- Comparison: do the warnings now correspond to what a human editor would flag?

### Ongoing observability

- Add the new metrics to `prose_telemetry_dashboard.py` (HTML output) under their own sections
- Update `prose_telemetry_corpus.py` to include new metrics in baseline comparison

## Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Threshold calibration is overfit to ch02 | High | Medium | Cross-chapter validation in Success Criteria; thresholds tunable in one place |
| New detectors over-fire on intentional rhetoric | Medium | Medium | Held-lines mechanism already exists; codify intentional patterns there |
| Comma-splice skip-rules go too far and miss a real splice | Low | Low | Detector confidence already 0.4–0.5; downgrade to warning-only is the safe fallback |
| Density normalization breaks a chapter that previously passed | Medium | Medium | Pre-flight diff against ch01 + ch05 + ch10 before merge |
| Sentence-length CV calibration band is wrong for Anna | Medium | Low | Initial band is hypothesis; observe over 3–4 chapters before treating as authoritative |

## Out of scope

- POS tagging via spaCy (would fix passive-voice false positives but belongs in the galley spaCy-tier sibling)
- Concrete-noun balance detector (Gap G in the evaluation) - needs a wordlist; defer to Phase 3
- Cross-chapter vocabulary drift / Joel-vs-Anna voice separation - also Phase 3
- Readability metrics (Flesch–Kincaid) - separate addition, not in this plan
- Pronoun-antecedent distance - semantic parsing; defer
- Reading-level / italics-block analysis - defer

## Reference library

- Current detector module: `build/prose_telemetry_handcount.py` (~2,290 lines)
- Verdict function: lines 1733–2070
- Held-lines mechanism: lines 2071–2151 (`_load_held_lines`, `_apply_held_lines`)
- spaCy-tier sibling: `galley/prose/lib/prose_telemetry/src/prose_telemetry/` (do not duplicate)
- Existing test fixtures: `build/test_prose_telemetry.py` (verify path; may not exist yet)
- ANNA-VOICE.md anti-patterns: `vol-2/ANNA-VOICE.md` (the canonical list)
- Held-lines exemplar: `vol-2/act-1/ch02-recruitment-interview.held-lines.json`

## Knowledge capture

After implementation, add to `.wolf/cerebrum.md`:
- **Key Learning:** verdict thresholds in `prose_telemetry_handcount.py` must be density-normalized per 1k tokens, not raw counts, because chapter lengths vary 2–4× across the manuscript
- **Key Learning:** `comma_splice` is high-false-positive territory; the detector is intentionally never a blocker
- **Do-Not-Repeat:** when adding a new detector that catches a CO-flagged prose pattern, also extend the held-lines schema example to demonstrate how to exempt intentional uses of the same pattern (so the author doesn't have to discover the held-lines structure on their own)

## Hardening log (Stage 1.5 adversarial pass)

| Critic | Finding | Resolution |
|---|---|---|
| Outside Observer | "Who reads this output besides the author?" - currently nobody. The dashboard isn't surfaced in galley web reader. | Acknowledged. Phase F's verdict-on-CV is the only metric that requires a reader to interpret; rest are actionable thresholds. Pursue galley dashboard surfacing in a separate plan. |
| Pessimistic Risk Assessor | Density normalization without recalibrating each detector's threshold could make chapters that *should* fail suddenly pass. | Phase A spec explicitly computes thresholds from the current effective raw-count behavior at ~6k words; the new densities preserve the same effective trigger for 6k chapters and tighten/loosen proportionately for other lengths. |
| Pedantic Lawyer | "Density-normalized" - to what tokens? Strip-to-prose tokens, or all tokens including dialogue markup and code? | Clarified in Phase A: use `doc.word_count` which already reflects strip-to-prose (current handcount behavior). |
| Skeptical Implementer | The recursive-noun detector at distance 8–30 will fire on legitimate echoes like "the protocol… the protocol" that are content-words. | Stopword list extended to include `protocol`, `architecture`, `system`, `mission`, `consortium` (Anna-voice topic words already excluded in `_LEXICAL_STOPWORDS`). |
| The Manager | "Four hours? You spent six hours on ch02 today and didn't write any detectors. What's the actual unit of effort?" | Honest answer: ~30 minutes per phase if held to scope. Phase A is the high-leverage one. The other phases can ship incrementally. |
| Devil's Advocate | The whole tooling layer competes for time with actual chapter writing. Should we just edit ch03 and skip this? | Counter: ch02 took 6 passes today partly because metric noise made it hard to see what was real. Reducing false-positive rate pays back across every future chapter. Phase A alone is worth shipping. |

## Meta-validation (Stage 2)

- [x] Delegation strategy: this plan is suitable for the chapter-drafter agent OR direct implementation; specifies exact functions to touch
- [x] Research needs: none - all existing code, no external libraries
- [x] Review gate placement: each phase has a binary gate
- [x] Anti-pattern scan: avoided (1) unvalidated assumptions, (2) vague phases, (3) hallucinated effort estimates (gave specific 30-min/phase numbers)
- [x] Cold Start Test: a fresh agent could execute Phase A from this doc with no prior context - function name and line numbers are specified
- [x] Plan Hygiene: opinionated, single recommended path, alternatives in Discovery only (not phases)
- [x] Discovery Consolidation: AHA-effect is "the verdict layer is the bug, not the detectors"

## Notes & deviations

- No code written in this plan document
- The plan does not specify implementation order beyond Phase A first; user discretion on Phases B–G ordering
- Phases B and C can be parallel (different functions); Phases D–G can be any order after A
- After implementation, regenerate metrics across all chapters of vol-1 and vol-2 to refresh baselines

---

## Phase H - Delivered: `redundant_explicit_predicate` detector

**Status:** ✅ Shipped 2026-05-15. Out-of-band from the original A–G plan because the gap surfaced mid-session ("I was prepared to be disappointed by it. I was not disappointed." was missed by every existing detector).

**File:** `galley/prose/lib/prose_telemetry/src/prose_telemetry/detectors/repetition/redundant_explicit_predicate.py`
**Registry entry:** `name="redundant_explicit_predicate"`, `family="voice"`, `tier="stdlib"`, confidence `0.75`.
**Tests:** `galley/prose/tests/test_repetition.py` - 9 new tests, all green; total repetition pack now 21 tests.
**Registry size:** 78 → **79 detectors**.

### Gap addressed

Implicit-predicate trimming: when sentence S2 explicitly re-states a copula+complement already set up in sentence S1, the trim form ("I was not.") is tighter and lands harder than the explicit form ("I was not disappointed."). No existing detector caught this pattern - the metric layer measures repetition density, chiasmus, nominalization, etc., but not clause-level predicate redundancy across adjacent sentences.

### Heuristic

For each consecutive sentence pair (S1, S2):
1. S2 word-token count between 2 and `max_s2_tokens` (default 8, configurable via `DetectorConfig.extra["max_s2_tokens"]`)
2. S2 opens with a personal pronoun (`I`, `he`, `she`, `it`, `they`, `we`, `you`)
3. S2 contains a copula or auxiliary (`was`, `were`, `is`, `are`, `am`, `be`, `had`, `has`, `have`, `did`, `does`, `do`, `will`, `would`, `could`, `should`, `may`, `might`, `must`, `can`, `shall`, `ought`)
4. S2 does NOT introduce new specificity (digits, mid-sentence proper nouns) - those signal "S2 adds information" and the redundancy doesn't apply
5. S2 contains a content word (≥4 letters, alphabetic, not in stopword set) that also appears in the **last 12 tokens of S1** (the predicate / complement zone - keeps subject-only echoes from firing)
6. The shared content word must appear in S2 **after** the copula/aux (post-predicate position)

When matched, emit `Finding(type="redundant_explicit_predicate", ...)` with `extra` fields:
- `echo_word` - the repeated complement
- `first_sentence` / `second_sentence` - full text
- `trim_suggestion` - calibrated rewrite, e.g. `"I was not."` (keep through copula plus optional negation, drop the rest)

### Validation results

**vol-2 ch02** (after Tier 1 sweep had already fixed the textbook case):
- Reverted the fix → detector caught **3 hits**:
  - `"I was not disappointed."` → trim `"I was not."` ✓ textbook case
  - `"It had now become one."` → trim `"It had."` ✓ legitimate trim
  - `"I did not end the call there."` → trim `"I did not."` ✓ legitimate trim
- Re-applied the textbook fix + applied the 2 newly-surfaced trims → **0 hits** end state

**vol-2 ch01** (first run with the new detector):
- 4 hits surfaced; ~50% precision (consistent with the design contract of "flag-not-prove, 0.75 confidence"):
  - `"We were not having that conversation."` → `"We were not."` ✓ clean trim
  - `"I have never liked cold."` → `"I have."` ⚠ trim is wrong (S2's `never` requires negation flip; detector trim suggestion does not handle `never` yet)
  - `"I have signed the longer version."` → `"I have."` ✗ false positive (S2 adds `signed`, new action)
  - `"I had considered all three acceptable."` → `"I had."` ✗ false positive (S2 adds `considered ... acceptable`, distinct predicate)

### Known limitations identified during validation

1. **`never` not in `_NEGATIONS` set** - the trim_suggestion for S2 starting with `I have never ...` is wrong. Should extend the negation set to include `never`, `no`, `nothing` (and detect them positionally to flip the trim correctly).
2. **Shared content word ≠ same predicate** - when S2's content word happens to recur but the predicate it sits in differs from S1's (e.g., S1 `the longer version with signatures` / S2 `I have signed the longer version`), the detector still fires. Could tighten by requiring that S2's verb+complement be **substring-similar** to S1's, not just sharing one content word.
3. **Adjacent-pair only** - detects only across S(i), S(i+1). A predicate echoed three sentences later is invisible. Acceptable for v1; can extend to a small window in a follow-up.

### Follow-ups (deferred to a future Phase H.1)

- Extend `_NEGATIONS` to include `never`, `no`, `nothing` and adjust trim_suggestion logic to handle negation-flipping cases
- Add a "predicate similarity" pre-filter that requires the verb stems in S2 to overlap with S1's verb stems (would have eliminated the `longer`/`three` false positives)
- Optional: surface the finding inline in the galley web reader with a "Apply trim" button (UI-side work, separate plan)
- Add a held-lines example for the deliberate rhetorical doubling pattern (`I could have ended the call there. I did not end the call there.`) so authors learn the exemption mechanism

### Phase H gate (met)

- [x] Detector registers into the live registry pipeline (79 detectors confirmed)
- [x] 9 unit tests covering: enabled/disabled, empty prose, registration, the textbook case, the quantity-additive case (negative), the proper-noun-additive case (negative), the no-shared-word case (negative), the long-S2 case (negative), the no-copula case (negative), the configurable threshold case, the subject-only-echo case (negative)
- [x] Validated against vol-2 ch02: caught the known case + 2 more legitimate hits
- [x] Validated against vol-2 ch01: 4 hits, mix of TP and FP consistent with the design contract
- [x] Updated metric-improvements plan to record delivery

---

## Phase I - Delivered: Gradient thresholds for spaCy detectors

**Status:** ✅ Shipped 2026-05-15. Architectural shift - out-of-band from the original A–G plan because the gap surfaced when binary stopwords proved too coarse during ch02's measurement pass.

**Files:**
- `galley/prose/lib/prose_telemetry/src/prose_telemetry/spacy_detectors.py` - gradient logic + metrics emission
- `galley/prose/lib/prose_telemetry/src/prose_telemetry/detectors/spacy/nominalization.py` - registry wrapper reads `DetectorConfig.extra.soft_caps`
- `galley/prose/lib/prose_telemetry/src/prose_telemetry/detectors/spacy/distributed_chiasmus.py` - registry wrapper reads `DetectorConfig.stopwords` as reduced-confidence list
- `galley/prose/lib/prose_telemetry/src/prose_telemetry/cli.py` - verdict layer uses `high_confidence_count` for chiasmus; merge logic passes new fields through
- `galley/prose/books/README.md` - new **Gradient thresholds** section documenting both mechanisms
- `galley/prose/CHANGELOG.md` - Phase 6.8 entry
- `the-inverted-stack/book.editorial.yaml` - `nominalization.extra.soft_caps` (15 entries) + `distributed_chiasmus.stopwords` (10 entries, all book-specific scene vocabulary)

**Tests:** 294/294 pass after the change. No new tests added in this round (existing test fixtures still exercise both detectors correctly; the gradient is a strict superset of the prior binary behavior at extreme caps).

### Gap addressed

A binary `stopwords: [foo, bar]` list throws away too much information. A word like `mission` or `question` is content vocabulary up to some reasonable count, then becomes over-use beyond it. Binary "always count" over-flagged interview / domain-heavy chapters (ch02 at 22.4/1k nominalization); binary "always ignore" hid genuine over-use (ch02 with `mission` set to ignore would have hidden a chapter that mentioned `mission` 30 times). A per-lemma threshold captures both.

### Two gradient mechanisms because detector behaviors differ

| Detector type | Mechanism | Rationale |
|---|---|---|
| Occurrence-counted (nominalization, lexical_chain) | **Soft cap per lemma** | Counts naturally; "first N free, flag the rest" maps directly to content-vs-overuse |
| One-shot detection (chiasmus) | **Reduced confidence** per lemma touching | Each match is a discrete event; weighting it preserves the signal without false-suppress |

Both preserve every match in the findings array so authors can audit. The verdict layer's job is to decide which findings are worth flagging - not to throw them away.

### Output schema additions

Per-detector metric records now optionally include:

```json
{
  "device": "distributed_chiasmus",
  "raw_count": 23,                        // all detected pairs
  "high_confidence_count": 0,             // genuine ABBA rhetoric only
  "weighted_count": 13.14,                // sum of (confidence / 0.7)
  "count_per_1k_tokens": 3.73,
  "high_confidence_per_1k_tokens": 0.0
}
```

```json
{
  "device": "nominalization",
  "raw_count": 63,                        // over-cap occurrences only
  "count_per_1k_tokens": 10.22
}
```

Individual findings carry context:
- nominalization: `occurrence_index` (1-based), `soft_cap`, `over_cap_by`
- chiasmus: `confidence` (0.4 or 0.7), `is_common_content_pair` (bool)

### Verdict logic change

```python
# Before:
n = chi["raw_count"]
if n >= 5:
    warnings.append(f"distributed_chiasmus: {n} ABBA reversal patterns")

# After:
high = chi.get("high_confidence_count", chi.get("raw_count", 0))
raw = chi.get("raw_count", high)
if high >= 5:
    note = f" (+{raw - high} reduced-confidence pairs filtered)" if raw > high else ""
    warnings.append(
        f"distributed_chiasmus: {high} high-confidence ABBA reversal pattern(s){note}"
    )
```

### Built-in defaults (ship with detector, apply to every book)

**Nominalization** - ~35 common abstract nouns with calibrated caps (`question: 8`, `conversation: 5`, `decision: 5`, `moment: 8`, `information: 4`, `condition: 4`, `position: 4`, ...).

**Chiasmus reduced-confidence** - universal cross-pair noise: speech-act verbs (ask, answer, say, tell, speak, talk), cognition verbs (think, know, remember, notice, wonder, decide), motion verbs (come, go, walk, run, turn, move), perception verbs (look, see, hear, watch, listen), action verbs (take, give, put, get, make, do), state verbs (be, have, wait, stand, sit, stop), temporal nouns (time, minute, hour, day, night, year, moment), body parts (hand, eye, foot, head, face, voice), generic narrative nouns (thing, way, place, person, man, woman, word, name).

### Validation results

| Chapter | Before gradient | After gradient |
|---|---|---|
| ch01-departure | yellow · `chiasmus: 6` warning, `self_referential_frame: 5` blocker | 🟢 green · 0 warnings · 0 blockers |
| ch02-recruitment-interview | yellow · `chiasmus: 23` + `nominalization: 22.4/1k` warnings | 🟢 green · 0 warnings · 0 blockers |

ch02's 23 chiasmus pairs are now correctly reported in the JSON as 23 raw, 0 high-confidence, 13.14 weighted - meaning **none of them** are genuine rhetorical ABBA; all are common-content cross-pairs (ask/answer, time/hand, etc.). The signal is preserved for audit, but the verdict doesn't fire on it. This is exactly the right behavior.

### Phase I gate (met)

- [x] Per-lemma soft caps work as documented (`mission` capped at 12, occurrences 1-12 invisible, occurrence #13 fires with `over_cap_by: 1`)
- [x] Reduced-confidence lemmas detected and emitted at 0.4 confidence
- [x] `high_confidence_count` and `weighted_count` propagate through merge
- [x] Verdict layer uses high-confidence count for chiasmus warning
- [x] Backwards compatibility: legacy `stopwords: [list]` still accepted (treated as cap=999)
- [x] Documentation in `galley/prose/books/README.md` shows both mechanisms with worked examples
- [x] CHANGELOG entry under Phase 6.8
- [x] No regression - 294/294 tests still pass; ch01 and ch02 both verdict=green

### Follow-ups (deferred)

- Surface `over_cap_by` and per-finding occurrence indices in the galley dashboard so authors can see which specific mentions exceeded their cap
- Consider extending the same gradient model to stdlib detectors (`lexical_chain_loop`, `motif_overuse`) - those still use binary stopwords. The detector-side change is straightforward; the question is migration risk for existing books with tuned `stopwords:` lists
- Calibrate caps against more chapters as ch03-ch18 get rewritten - initial defaults are heuristic; real-corpus data will refine them
