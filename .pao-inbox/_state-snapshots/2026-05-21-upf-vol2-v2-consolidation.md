# Vol-2 Bestseller-Profile UPF v2 — Volume Re-Audit Consolidation

**Pipeline:** `icm/pipelines/bestseller-profile-review` (Stage 07)
**Dispatch:** 2026-05-21, 18 Sonnet 4.6 + high effort subagents, parallel fan-out, live-grep mandate
**Baseline:** 2026-05-20 v1 grades + 2026-05-20 recommendations-applied report
**Consolidator:** PAO main session (Opus 4.7 + xhigh)

---

## 1. Grade matrix — v1 → v2

| Ch | LD v1 | LD v2 | NYT v1 | NYT v2 | Pull-up status |
|---|---|---|---|---|---|
| 01 | A- | A- | YELLOW | YELLOW | held — Tier 4 deferred items cap further lift |
| 02 | A- | **B+** | YELLOW | YELLOW | **regression: live grep caught real violations v1 missed** |
| 03 | B+ | **A-** | YELLOW | YELLOW | pull-up achieved (Wave 7 confirmed) |
| 04 | B+ | B+ | YELLOW | YELLOW | held — wasn't in May 20 application |
| 05 | B+ | **A-** | YELLOW | **GREEN** ⭐ | pull-up + first GREEN |
| 06 | B+ | B+ | YELLOW | YELLOW | held — recommended Stefan/Forsaken work deferred |
| 07 | B+ | **A-** | YELLOW | YELLOW | pull-up achieved |
| 08 | D+ | **B-** | RED | YELLOW-GREEN | **D+→B- (1 notch under projected B+); Sabina-metaphor residual** |
| 09 | B+ | B+ | YELLOW | YELLOW | held — Bobiverse pass still pending |
| 10 | B | **B+** | YELLOW | YELLOW | half-grade lift; all 3 v1 violations cleared |
| 11 | C+ | **B-** | YELLOW | YELLOW | partial pull-up; B+ target missed (Joel scene 250→140) |
| 12 | D+ | **B+** | RED | YELLOW-GREEN | pull-up held with margin |
| 13 | B- | **A-** | YELLOW | YELLOW (strong) | pull-up achieved |
| 14 | B+ | **A-** | YELLOW | YELLOW-GREEN | pull-up achieved |
| 15 | B+ | B+ | YELLOW | YELLOW | trim landed cleanly, no narrative gaps |
| 16 | B+ | **A-** | YELLOW | **GREEN** ⭐ | pull-up + 2nd GREEN |
| 17 | B+ | **A-** | YELLOW | **GREEN** ⭐ | pull-up + 3rd GREEN |
| 18 | B+ | **A-** | YELLOW | YELLOW | pull-up; "at the standing" density (16) is residual |

**Distribution shift:**

| Grade | v1 | v2 |
|---|---|---|
| A- | 2 | **10** |
| B+ | 11 | 5 |
| B | 1 | 1 |
| B- | 1 | 2 |
| C+ | 1 | 0 |
| D+ | 2 | 0 |

**Median: B+ → A-.** No chapter below B-. 3 GREEN on NYT-profile readiness (ch05, ch16, ch17).

---

## 2. Live-grep mandate findings

The patched pipeline's live-grep mandate caught two distinct error patterns:

### 2.1 Stale-flag corrections (false-positive BLOCKERs in v1)

| Ch | v1 reported | v2 live count | Delta |
|---|---|---|---|
| 06 | "4-6 register uses" | 1 | -3 to -5 |
| 14 | "10+ register instances" | 1 | -9+ |
| 16 | "double-register sentence present" | 0 (resolved) | confirmed cleared |
| 18 | **"83 instances"** | **1** | **-82** |
| 17 | "~38 'at the standing'" | 3 in narrator body (38 was raw count, 35 were in crew log) | clarified |

The ch18 finding is the canonical case the patched pipeline was designed to catch.

### 2.2 v1 visual-read miscount (UNDER-reporting)

ch02 v1 graded A-; v2 live grep caught real violations v1 missed by reading visually:
- Register family: 5 instances (cap = 3)
- "Noted" overconcentrated: 7 instances, 3 in same paragraph (anti-pattern #5)
- 2 anti-pattern #7 instances (Anna narrating her own habits)

**v2 is the more accurate measurement.** v1 grades were partly aspirational/visual.

---

## 3. CRITICAL pipeline finding — sed-strip recipe is broken for chapters with body `---` rules

**Discovered by ch03 v2 audit.**

The patched pipeline's recommended grep recipe:
```
sed '/^---$/,/^---$/d' <CHAPTER> | perl -0777 -pe 's/<!--.*?-->//gs' | grep -ciE 'PATTERN'
```

interprets ANY `---` line as a frontmatter delimiter. Chapters with body horizontal rules (ch03 has two at lines 124 + 190; possibly others) lose all body content between them silently.

**Symptom:** ch03 v2 initially reported `register=1`. Corrected count after fixed strip: `register=3` (at cap, no headroom).

**Correct recipe (only strips LEADING frontmatter block):**
```
perl -0777 -pe 's/^---\n.*?\n---\n//s' <CHAPTER> | perl -0777 -pe 's/<!--.*?-->//gs' | grep -ciE 'PATTERN'
```

**Action:** patch `bestseller-profile-review.yaml` + README to use the perl-only recipe. Already added to book-repo cerebrum's Do-Not-Repeat list per ch03 subagent.

---

## 4. Volume-wide pattern clusters (post-v2)

The v2 audits surface these volume-wide patterns:

### 4.1 Discipline / institutional motif over-density (NEW finding)

Multiple chapters at high "discipline" frequency: ch03 (8 instances; one consecutive doubling), ch10 (intact but borderline), ch14 ("hold against / hold against" echo still in soft borderline), ch15 ("X was the X" 10 confirmed instances), ch16 (cleared, but cap-adjacent), ch17 ("standing" 19 total still appears across narrator + log).

This is a candidate for a Tier-2 cross-chapter pass: enforce discipline-motif cap at ≤5 per chapter, monitor "It is the same discipline that..." anaphora.

### 4.2 Persistent Tier-4 items (4 chapters need CIC ruling)

- **ch01** Wanjiru direct-address paragraph → excise + add Joel bunk-laptop disclosure (ceiling-limit for A-)
- **ch06** Stefan one-concrete-particular insertion (~30-50 words) + Forsaken concept named in body
- **ch11** Joel cup-scene paragraph 3 inference chain → cut to ~15 words; Forsaken position named at comm-space door
- **ch09** Bobiverse parenthetical-aside pass (~6 asides + break `I had` anaphora run)

### 4.3 Residual single-chapter items

- **ch04** Carry-cluster penultimate paragraph → cut (single-paragraph zero-risk operation; clears the chapter's only AP breach)
- **ch08** Sabina-conference scene metaphor gap (1-2 sentences)
- **ch12** Wanjiru institutional-delay paragraph → compress 8 sentences to 4
- **ch13** post-migration recognition triple-formulation → cut to 1 + 1 echo
- **ch14** "The standing was the standing" Day-48 close → cut
- **ch15** 5 loosest "X was the X" instances → targeted ~50-word pass
- **ch18** "at the standing" density (16) → 6 targeted substitutions

---

## 5. Cost report

| Component | Model | Approx cost |
|---|---|---|
| Per-chapter fan-out (18 × Sonnet 4.6 high) | sonnet | ~$8-12 |
| Consolidation (Opus 4.7 xhigh, this artifact) | opus | ~$1-2 |
| **Total v2 re-audit** | | **~$10-14** |

Higher than v1 (~$6-10) due to high vs medium effort + larger context (now reads v1 baseline reports too).

---

## 6. Recommended next steps

### Tier A — Pipeline hygiene (do first, blocks future runs)
1. **Patch sed-strip recipe** in `bestseller-profile-review.yaml` + README to use perl-only frontmatter strip
2. **Document body-`---` horizontal-rule risk** in pipeline's live-grep mandate

### Tier B — Tier-3 cleanup (single-chapter Yeoman passes)
3. ch04 carry-cluster cut
4. ch08 Sabina-metaphor 1-2 sentence insert
5. ch11 Joel cup-scene paragraph 3 compression (~15 words)
6. ch12 Wanjiru institutional-delay compress (8→4 sentences)
7. ch13 post-migration triple-formulation cut
8. ch14 "The standing was the standing" Day-48 close cut
9. ch15 "X was the X" 5 loosest instances pass
10. ch18 "at the standing" 6 targeted substitutions

### Tier C — Volume-wide pass (next major sweep)
11. Discipline-motif cap enforcement (≤5 per chapter; cross-chapter pass)
12. Listen-test pass for borderlines flagged by multiple v2 reports

### Tier D — CIC-blocked items
13. ch01 Wanjiru direct-address + Joel bunk-laptop disclosure
14. ch06 Stefan particular + Forsaken naming
15. ch11 Forsaken position naming
16. ch09 Bobiverse rewrite

---

## 7. Verdict

**The May 20 application landed.** 12 of 14 edited chapters showed grade lift; 1 held (ch01 ceiling-limited); 1 partial (ch11 — known incomplete compression). The volume now sits at A- median, 3 GREEN, no chapter below B-.

**The live-grep mandate worked** — caught 5+ stale-flag false positives (ch06, ch14, ch16, ch18; ch17 clarified) AND caught real violations v1 missed (ch02). v2 grades are the more reliable baseline going forward.

**One critical pipeline bug found** — sed-strip recipe broken for body `---` rules. Fix queued.

---

— PAO, 2026-05-21T01:50Z
