---
type: resumed
chapter: closing/the-crossing
last-pr: "#59 (chore/pao-the-crossing-first-draft, head: 30ac7a0)"
in-reply-to: pao-directive-2026-05-01T02-31Z-pr59-chapter-draft-self-review.md
---

**Verdict: PASS on all 5 passes. No edits applied. Chapter draft holds together at King-style craft after the cast swap; ready for CO review.**

## Pass 1 - Tail-reference scan ✓

`grep -nE "Lars|Étienne|Aino|Lakshmi|Bergmann|Marchand|Reddy|Norwegian|Tromsø|Bergen|Lofoten|Norway"` returned exactly **one hit**: line 21, "the postdoctoral years at AWI Bremerhaven and the Norwegian Polar Institute" - Anna's intentional postdoctoral biography per your directive. Zero residue from the cast swap. Mechanical mirror was clean.

## Pass 2 - Diego thread continuity ✓

Diego appears ~20 times across the chapter. Institutional anchor reads consistently:
- IAA (Instituto Antártico Argentino): named at line 23 ("the institutional memory of the IAA, which had operated continuously occupied Antarctic stations since 1904 - older than aviation"), reinforced at line 85 ("not for the Instituto Antártico Argentino's communications office"), line 97 ("Instituto Antártico Argentino's research relay"), line 149 ("his three colleagues from the Instituto Antártico Argentino").
- Belgrano family home: line 85 ("María Elena Vargas at her kitchen table in Belgrano").
- Buenos Aires Ezeiza arrival: line 149.
- Sofía at six: line 143 ("Diego Vargas's granddaughter Sofía is six years old"), reinforced at line 149.

**On your San Martín de los Andes question:** the location does not appear anywhere in the chapter prose. It may be in the character sheet but was not pulled into the narrative. Not an inconsistency (since there's no second phrasing to clash with) - but if you intended it to anchor a specific scene, it didn't make it in.

**Sofía introduction order:** correct. Line 143 first introduces her as "Diego Vargas's granddaughter Sofía is six years old" - full noun-phrase + name + age in one beat. Line 149 reinforces with "his granddaughter Sofía." Order is right.

## Pass 3 - Spanish letter beat ✓

Line 85: *"I wrote it in Spanish, because it was for María Elena Vargas at her kitchen table in Belgrano, not for the Instituto Antártico Argentino's communications office."*

The beat lands. The kitchen-table-vs-communications-office antithesis is the craft move - Spanish-language detail compounds with both halves (right register for both contexts; the kitchen table earns the language; the communications office is where Spanish would have been institutional). Not over-engineered. Composes with Anna's Russian biography (line 21) cleanly: both language beats are about which institutional context the speaker is bringing.

Note: Joel's Tagalog and Diego's porteño English aren't actually mentioned in the chapter prose - only in character sheets. This is fine; the Spanish letter beat doesn't need to be one of three in a series.

## Pass 4 - Crew-intro paragraph cadence ✓ (with note)

Per-character word-count in line 23 paragraph (rough):
- Maria Santos: ~50 words
- Priya Iyer: ~40 words
- Sabina Rahman: ~50 words
- Joel Reyes: ~50 words
- Hiroshi Nakamura: ~30 words ("the calmest man on the manifest")
- Wanjiru Kamau: ~40 words
- Diego Vargas: **~95 words** (close-position; longest entry)

Diego's clause is **2× the others, not 3×**. Per your "3× threshold" the trim isn't warranted. The extra length is justified narrative-architecturally:
- Closer position weight (the paragraph builds to him)
- IAA institutional setup ("since 1904 - older than aviation") needed for the IAA references later
- Retirement-mission framing ("told his wife the same thing") that pays off in Act III
- "He had brought his cameras" - load-bearing for Sofía's photographs at line 143

**No trim recommended.** The cadence-asymmetry is doing rhetorical work.

## Pass 5 - King moves audit ✓

Every timestamp + numerical specific you listed survived the cast swap intact:

| Item | Location | Survived? |
|---|---|---|
| 0317 bridge watch | line 53 | ✓ |
| 0319 cabin call | line 65 | ✓ |
| 0321 bridge arrival | line 65 | ✓ |
| 0342 time-of-death | line 75 | ✓ |
| 0414 freezer | line 77 | ✓ |
| 0614 death notification finalized | line 85 | ✓ |
| Queue accepted six days earlier | line 109 | ✓ |
| 12:33 queue cleared | line 121 | ✓ |
| 14:42 Argentina local time read | line 123 | ✓ |
| Eleven days after death | line 123 | ✓ |
| 4,017 photographs | line 143 | ✓ |
| Sofía at six | line 143 | ✓ |

Plus additional timestamps preserved that you didn't list but are King moves:
- 03:51 body to medical bay (line 77)
- 04:38 notification written (line 85)
- 14:14 tertiary endpoint failure (line 97)
- 04:41 Punta Arenas arrival on day 56 (line 149)

## What was edited directly

**Nothing.** All five passes returned PASS. Working tree on `chore/pao-the-crossing-first-draft` is unchanged.

## What was left alone and why

- Diego's longer crew-intro clause (Pass 4): 2× others is justified by closer-position weight and downstream IAA references. Trimming would weaken Act III's IAA institutional anchor.
- The single Norwegian Polar Institute reference (Pass 1 hit at line 21): you flagged it as intentional. Confirmed.
- San Martín de los Andes: doesn't appear in chapter prose, no inconsistency to fix; flagged in case it should be added to anchor a specific scene.

## Overall verdict

**The chapter draft holds together at King-style craft after the swap.** The mirror was mechanically clean (zero tail residue), the institutional anchors read natural, the timestamps + numerical specifics all survived, the cadence works. The Spanish letter beat earns its place. Ready for CO review without a structural pass.

The one item I'd flag for editorial consideration (not blocking): **San Martín de los Andes**. If your character sheet has Diego retiring there and you intended it to anchor a specific scene, it should appear somewhere in the chapter - probably the crew-intro paragraph (e.g., "fifty deployments to one pole or the other across thirty-five years of work, last summer he had told his wife he was retiring to the small house in San Martín de los Andes"). If the omission is deliberate (the chapter is told from Anna's POV and she might not know that level of biographical detail), then leave it out.

## Switching back

I'll switch back from `chore/pao-the-crossing-first-draft` to my prior branch + restore the .wolf/* stash after committing this beacon.
