---
type: pao-directive
chapter: closing/the-crossing
last-pr: "#59 (open, head: chore/pao-the-crossing-first-draft, last commit: 30ac7a0)"
priority: P1
expected-output: yeoman-resumed-* beacon with audit findings; edits on PR #59 branch (PAO commits)
---

# PAO directive — PR #59 chapter draft King-style self-review post-cast-swap

## Context

PR #59 (`chore/pao-the-crossing-first-draft`) carries the closing chapter "The Crossing" — first draft, 4,430 words, awaiting CO review. After PR #59 was first opened, four cast swaps landed in main (PR #64) and were mirrored onto the PR #59 branch in commit `30ac7a0`: Lakshmi → Sabina Rahman, Étienne → Hiroshi Nakamura, Lars → Diego Vargas, plus the family thread updates (Aino Bergmann → María Elena Vargas, Tromsø airport → Buenos Aires Ezeiza, Norway local time → Argentina local time, granddaughter Sofía locked at six). The mirroring was mechanical — find/replace plus targeted family-thread rewrites — and was not read end-to-end for tail consistency.

## What you are reading for

Switch to `chore/pao-the-crossing-first-draft` and read `vol-1/closing/the-crossing.md` end-to-end as a hostile reader. Five passes, in this order:

1. **Tail-reference scan.** Grep for `Lars`, `Étienne`, `Aino`, `Lakshmi`, `Bergmann`, `Marchand`, `Reddy`, `Norwegian`, `Tromsø`, `Bergen`, `Lofoten`, `Norway` in the chapter file — should return zero hits except for the Norwegian Polar Institute reference at line ~21 (Anna's postdoctoral biography, intentional). Anything else is a bug.
2. **Diego thread continuity.** Diego Vargas is named ~25 times across five acts. Read each appearance and verify the Argentine institutional anchor (IAA, since 1904, Esperanza/Marambio stations, San Martín de los Andes retirement, Belgrano family home, Sofía at six) reads consistently and without continuity errors. Specifically: does the chapter say his retirement house is in San Martín de los Andes (sheet) or "the small house in San Martín de los Andes" (chapter prose) — are the two phrasings consistent? Does Sofía's name appear before or after she's introduced as "granddaughter" — first-introduction order should be "granddaughter Sofía" then "Sofía".
3. **Spanish letter beat.** Anna's letter to María Elena was added to the Act III death-and-notification passage as a one-clause beat ("I wrote it in Spanish, because it was for María Elena Vargas at her kitchen table in Belgrano, not for the Instituto Antártico Argentino's communications office"). Does the beat land — earn its place — or does it read as a graft? Does the Spanish-language detail compose with the chapter's other language beats (Anna's Russian leadership career, Joel's Tagalog, Diego's porteño English)? If the beat is over-engineered, propose tightening.
4. **Sabina/Hiroshi crew-intro paragraph.** Line 23 introduces all eight crew in one long paragraph. After the swaps, the paragraph carries: Maria (Belo Horizonte ransomware), Priya (Pune hospital bid), Sabina (Grameen 1976 lineage, doesn't trust networks she can't see), Joel (GCC offshore), Hiroshi (NIPR, JARE, Showa, calmest man), Wanjiru (East African mobile money, hums), Diego (IAA, since 1904, retirement mission, brought his cameras). Each character gets one to two sentences. Does the paragraph still read at the same cadence after the swaps, or has the Diego clause grown disproportionately? If Diego's clause is now 3× the others, propose a trim.
5. **King moves audit.** The original draft carried specific King moves: 0317 bridge watch, 0319 cabin call, 0321 bridge arrival, 0342 time-of-death, freezer at 0414, death notification finalized 0614, queue accepted six days earlier, queue cleared 12:33, María Elena read at 1442 Argentina local time eleven days after death, four-thousand-and-seventeen photographs reach Sofía. Verify every one of these timestamps + numerical specifics survives the cast swap intact.

## Deliverable

Apply edits directly to the file on the `chore/pao-the-crossing-first-draft` branch. Do **not** commit — PAO commits per the 2026-04-29 directive. Inline `<!-- PAO: ... -->` flags for anything that needs editorial judgment.

Write a `yeoman-resumed-2026-05-01THH-MMZ-pr59-self-review-complete.md` beacon when done. Body: (a) what each pass found, (b) what was edited directly, (c) what was left alone and why, (d) overall verdict — does the chapter draft hold together at King-style craft after the swap, or does it need a structural pass before CO review?

If you find structural issues large enough to warrant restructuring (an act that no longer lands, a death scene that has lost its weight, a closing passage that has gone flat), say so plainly. Better to surface a problem now than to ship a chapter that doesn't earn its closing position.
