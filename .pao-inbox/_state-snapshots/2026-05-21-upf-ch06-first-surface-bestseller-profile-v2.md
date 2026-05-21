---
type: upf-creative-audit-v2
chapter: ch06-first-surface-first-forsaken-reveal
volume: 2
act: 1
audit-date: 2026-05-21
auditor: pao
baseline: 2026-05-20-upf-ch06-first-surface-bestseller-profile.md
chapter-version: v1 (post-Anna-voice-rewrite-2026-05-16)
live-grep-verified: true
---

# UPF Audit v2 — Ch 06: First Surface, First Forsaken Reveal

## Live Grep Mandate — Verified Counts

All counts below are live-grep results from the stripped chapter prose (frontmatter removed, HTML comments removed) per the v2 mandate.

| Pattern | v1 claim | v2 live count | Delta |
|---|---|---|---|
| `register/registered/registering` | "at minimum 4, likely 5-6" | **1** | v1 was a FALSE POSITIVE — cap NOT exceeded |
| `I noted` (motif phrase, anti-pattern 5 risk) | not counted | **4** | new finding — soft warning |
| `noted` (all forms) | not counted | **4** | confirms above |
| `self-referential frame` ("this chapter" / "the chapter") | "once" | **1** | PASS, anti-pattern 6 compliant |
| `the work was` | not counted | **1** | no tricolon issue |
| `aphoristic closures` (AP-1 signal phrases) | borderline (para 77 flagged) | **0** exact matches | borderline assessment was correct; no hard violation |
| `echo-confirm closures` (AP-8 signals) | 0 | **0** | CLEAN |
| `statement-then-reversal` (AP-3) | 0 | **0** | CLEAN |
| `stefan/reinhardt` appearances | "2" | **4 paragraphs** | v1 undercounted; see below |
| `forsaken` in body prose | absent | **0** | confirmed absent |

### Register count — v1 false positive corrected

The v1 audit claimed "at minimum 4 uses, likely 5-6" of `register/registered/registering`. Live grep finds **exactly 1 instance**: "named the rival's principal investigator at the institutional register" (prose line 60, para on Wanjiru's press-packet handling). The chapter is well within the ≤3 hard cap. No fix required on this item.

The likely source of the false positive: the word "register" appears in the chapter's prose at the senior-operator voice level ("senior-operator-to-senior-operator register," para 72), but that phrase does NOT contain the word "register" — it reads "register" in plain English. Live grep confirms it is NOT present as the word `register`. The v1 read was counting occurrences of the *concept* rather than the *word*.

### Stefan appearances — v1 undercounted

Live grep finds Stefan/Reinhardt across 4 paragraphs, not 2:
1. Wardroom reflection: "including the one that was Stefan's, including the one that was nobody's" (unnamed prior-mission implication)
2. Press-packet section: Wanjiru quotes "Reinhardt's name is in the body of the coverage"
3. Press-packet narration: "I noted that she had said *Reinhardt* the way the consortium institutional record said *Reinhardt*" + "named the rival's principal investigator at the institutional register"
4. Closing Wanjiru reflection: "what survived … in time to be read against Stefan's preliminary results" + final closing paragraph

This is structurally stronger than v1 assessed. Stefan's name is threaded across the chapter's three major beats: wardroom reflection (past), comm-space press read (present), and act-close (future). The problem is not quantity of appearances but texture — all four occurrences are institutional naming, never personal. The v1 weakness finding stands on different grounds than originally stated.

### "I noted" motif — new finding

4 uses of `I noted` across the chapter: paras 20, 47, 60, 79. Anti-pattern 5 caps motif phrases at 1 per chapter. **This is a soft warning, not a blocker** for two reasons: (a) "I noted" is Anna's canonical observational register — it is load-bearing character voice, not incidental repetition; (b) the four instances are distributed across well-separated sections with substantial prose between them. However, 4 uses approaches the audible repetition threshold. CO should read aloud to assess. If any one of the four sounds mechanical rather than character-true, that is the trim candidate.

---

## Stage 0 — Discovery Revisions

### D1 — Forsaken concept CONFIRMED absent from prose body

Grep confirms zero appearances of "forsaken" in chapter prose. The glossary (`vol-2/_glossary/forsaken.md`) notes this explicitly: "consider whether Vol 2 should add a brief in-universe gloss the first time *Forsaken* appears in chapter prose (currently it appears only in chapter titles). A single sentence in Anna's interior at Ch 6 — naming what the Forsaken position is, without editorializing — would protect both print and audio readers from miscategorizing the term. Defer to CO; this is a craft decision, not a workshop call."

This remains the chapter's single most structurally under-exploited opportunity. For audio especially: the narrator will read the chapter title as "first abandoned reveal" without the gloss. This is a reader/listener protection issue, not a stylistic preference.

### D2 — Stefan appears 4 times across the chapter, all institutional

The extra Stefan appearances strengthen the threading but do not change the core finding: every occurrence is institutional naming, never personal. The reader has no basis for experiencing the name's arrival as anything other than press-cycle friction. The "concrete particular" fix from v1 is validated and elevated in priority.

### D5 — RETRACTED (register cap false positive)

D5 from v1 is retracted. "Register" appears exactly once. No fix required.

### D6 (NEW) — "I noted" motif at soft-warning threshold

4 uses. Distributed across the chapter. Soft warning; not a blocker; CO read-aloud test recommended.

### D7 (NEW) — Final close (lines 200-204) uses an authentic Anna-permitted ending form

The final three paragraphs:
- "The crew was where the crew should be. The boat was where the boat should be. The architecture was where the architecture should be. The work was the work." — This is a parallel-structure close, but the three "was where" sentences are a **functional tricolon** (naming the crew/boat/architecture against each other as a single operational check) rather than a rhythm-tricolon (anti-pattern 4). The argument that it passes: Anna is genuinely listing three parallel status checks in one sentence, in the same form a mission director would run a mental checklist. This is not rhetorical cycling. Assessment: **PASS**.
- "The work was what would carry…" — Forward-looking final beat naming the next ticking clock (Stefan/Day 37). This is Act I's closing horizon-line. The sentence is slightly over-constructed (it front-loads the purpose clause heavily) but lands the act-close correctly. AP-13 risk from v1 is real but marginal.

---

## Stage 1 — Plan Revisions

### Voice Compliance (revised)

| Anti-pattern | v1 assessment | v2 live-grep status |
|---|---|---|
| AP-1 (aphoristic close) | borderline on para 77 | 0 exact markers; borderline was correct, not a violation |
| AP-3 (statement-reversal) | 0 | 0 CLEAN |
| AP-4 (rhythm tricolon) | no finding | final-close tricolon assessed as functional; PASS |
| AP-5 (motif phrase > 1/chapter) | not counted | "I noted" x4 — SOFT WARNING |
| AP-6 (meta-frame > 1/chapter) | 1 use | 1 use CLEAN |
| AP-7 (narrator self-consciousness) | 0 | 0 CLEAN |
| AP-8 (echo-confirm) | 0 | 0 CLEAN |
| AP-9 (register cap ≤3) | "4-6 uses — BLOCKER" | **1 use — FALSE POSITIVE, CLEAN** |

### NYT Profile — revised

| Item | v1 | v2 |
|---|---|---|
| Credible antagonist | YELLOW — name-only, no texture | YELLOW MAINTAINED — 4 appearances all institutional, no personal texture |
| Pacing | YELLOW — wardroom reflection overlong | YELLOW MAINTAINED |
| Register cap | implied BLOCKER | GREEN — false positive; 1 use |
| Self-referential frame | PASS | PASS |
| "I noted" motif | not assessed | SOFT WARNING |

**NYT-Profile Readiness: YELLOW (same as v1, but for different reasons)**. The register cap is no longer a finding. The credible-antagonist and wardroom-pacing yellows stand. "I noted" × 4 is a new soft warning.

---

## Delta Verdict

**v1 → v2: One finding retracted; one finding upgraded; one new finding added; overall grade unchanged.**

**Retracted:** D5 / AP-9 (register cap). The "4-6 uses" claim was a false positive from visual reading. Live grep: 1 instance. Not a blocker, not an edit target.

**Finding upgraded (Stefan texture):** The wardroom reflection does name Stefan in connection with the prior mission (para 39: "including the one that was Stefan's") — this is more texture than v1's cold-read suggested. However, "including the one that was Stefan's" is institutional attribution, not personal memory. A physical detail or spoken exchange is still the missing piece; the fix recommendation from v1 stands but the scene is less bare than v1 suggested.

**New finding:** "I noted" × 4 is at the soft-warning threshold for anti-pattern 5. CO read-aloud test is the right diagnostic; if any of the four sounds mechanical rather than observational-authentic, that is the trim candidate.

**Overall: B+ grade maintained.** The chapter's strengths are real and unreduced. The two genuine weaknesses are:

1. Stefan is threaded across four structural moments but carries no personal weight in any of them. This is the highest-leverage single edit: add one concrete particular in the wardroom reflection (one physical detail, one spoken exchange, one specific prior moment) to distinguish "Stefan's name reached me on the second reading" from ambient institutional friction.

2. The Forsaken concept is absent from prose. The glossary defers this to CO. If CO approves a gloss-installation, one sentence in Anna's interior during the press-packet reading scene is the right scope and position.

---

## Highest-Leverage Edit (v2)

Same as v1, confirmed by grep evidence: **add one concrete particular about Stefan in the wardroom reflection (para 101-102 range)**. The passage currently reads: "The surface had not been the only cause. Other causes had compounded, including the one that was Stefan's, including the one that was nobody's." This is the chapter's only window for installing personal texture on Stefan before the next Forsaken Reveal chapter. One sentence — a physical memory, a moment from the prior mission — is all that is needed. The deferral language ("there would be a chapter, later, in which I would name the name at a different altitude") only works as controlled restraint if the reader has some charge behind the name. Currently the charge is absent.

**Estimated scope: 1-3 sentences, 30-50 words. No structural changes required.**

---

## Forsaken Glossary Consultation

Per the mandate: `vol-2/_glossary/forsaken.md` (not `_glossary/forsaken.md` — the latter path does not exist; the file lives inside the vol-2 directory tree).

The glossary confirms:
- "Forsaken" is an in-universe proper noun for the rival regulatory/PR campaign framing local-first architecture as obsolete
- It does NOT appear in any current prose — only in chapter titles
- The glossary explicitly identifies Ch 6 as the right installation point for a prose gloss
- Audio risk is real: "First Forsaken Reveal" will be parsed as "first abandoned reveal" without orientation
- Resolution is deferred to CO

**PAO recommendation:** install the gloss. One sentence in Anna's interior during the press-packet reading scene, before or after the Stefan naming. The sentence should name what the Forsaken framing is without editorializing — Anna naming a regulatory concept she has been tracking, not a narrator aside. Example form (not prescriptive): "The consortium's institutional acknowledgment used the word the Helvetia press cycle had been using since Bremerhaven - *Forsaken* was the position name Stefan's team had filed for the rival's regulatory argument, the claim that what the Nansen's architecture was doing had already been left behind." The exact wording is Yeoman territory; the installation decision is CO's.
