# Vol 2 - Bobiverse-pull voice tuning

**Date:** 2026-05-13
**Author:** PAO (with CO directives, this session)
**Status:** Locked. Applied to `vol-2/ANNA-VOICE.md`, ch01-departure.trial.md, ch02-recruitment-interview.trial.md.
**Code commit:** `2cc80df` (note: parallel-session sweep - commit message names only the Vol-1 dissertation refactor; the Bobiverse-pull tuning landed in the same commit as a side effect of `git add -A`. This decision doc is the audit-trail correction.)

---

## What surfaced

CO listen-tested the Kokoro renders of ch01 and ch02 (Filchner / Anna-voice trial chapters) and reported: *"the Janeway voice filter is still looping too much. when I listen to the Bobiverse there are no looping patterns used."*

The current Anna voice as drafted mixed Bobiverse moves with Janeway moves in roughly equal measure. The Bobiverse moves (parenthetical asides, "which meant…" inference chains, dry technical confidence) are working. The Janeway moves are the looping. The Bobiverse register is to dominate going forward; Janeway stays in *bearing* (command posture, ethics, crew loyalty) and not in *rhetoric*.

## Five looping patterns identified

1. **Aphoristic packaging.** *"Composure is not a quality. Composure is the residue of decisions you made twenty years ago."* / *"We are all of us, in our small ways, getting away with something."* / *"There are things you do not pass on. That is one of mine."*
2. **Anaphoric inventories.** *"She had a niece. She had a husband. She had a man named Joel."* / *"I had decided… I had written… I had written…"* / *"He did not soften… He did not say… He did not name…"*
3. **Parallel-structure tricolons used as rhythm rather than function.** *"composure, ethics, command"* / *"coffee, news, planning, organizing her thoughts."*
4. **Recurring motif phrases.** *"what it claimed to be"* (3× ch02) and *"noted and did not yet ask about"* (3× across chapters) - both stop reading as character verbal tics and start reading as authorial devices.
5. **Statement-then-reversal closures.** *"From any other candidate the same sentence would have read as bravado. From him it read as the operating cost of being on the boat."*

## CO's explicit decisions (2026-05-13)

1. **Retire *"what it claimed to be"* entirely.** Verbal tic phased out. Replaced in-place: kuchen line dropped to direct technical evaluation; paper rephrased to operational verdict ("the architecture in the paper was the architecture I was going to deploy"); Diana's drawing close lands on the image alone (*"The moon is wearing a hat. I have not asked her to explain the hat."*).
2. **Lighten the staff-history frame.** *"I am writing this here so you know"* and similar staff-history meta-frames capped at one use per chapter, applied only where actively load-bearing.
3. **Keep the "He did not" run-of-six in ch02** as the single explicit held line - the chapter's load-bearing rhetorical climax. Documented as the *only* approved anaphora exception in the volume. Will be honored by the prose-telemetry platform's future `held_lines` schema addition.

## Seven anti-patterns added to ANNA-VOICE.md

The voice doc now carries an explicit "what Anna's narrator does NOT do" section with seven concrete prohibitions:

1. No aphoristic paragraph closes
2. No anaphoric inventories (max_run = 2 except the held line)
3. No statement-then-reversal closures
4. No parallel-structure tricolons used for rhythm
5. No motif phrases repeated more than once per chapter
6. No more than one staff-history meta-frame per chapter
7. No commentary on Anna's own narration habits (no Anna-on-Anna meta)

Plus a "paragraph endings - explicit OK landings" section listing what Anna *can* end paragraphs on: concrete physical detail, forward-motion transition, wry observation, specific image, real or non-aphorizing question, short sentence that doesn't try to mean too much. And a matching "may NOT end on" list.

## What this cost (lines previously protected, now cut)

- *"Composure is not a quality. Composure is the residue of decisions you made twenty years ago…"* - cut
- *"We are all of us, in our small ways, getting away with something."* - cut
- *"There are things you do not pass on. That is one of mine."* - softened to operational statement
- *"What it claimed to be"* in all four prior occurrences (kuchen, paper, vatrushka, Diana's drawing) - removed
- *"You may notice, in this account, that I keep doing this. I will not pretend I do not know that I keep doing it."* - Anna-on-Anna meta, cut
- *"She had / She had / She had"* anaphoric inventory - rewritten with varied openings

Preserved per CO directive:
- *"The feeling was correct, and the feeling was also useless."* - observational, not aphoristic
- *"The Strait of Magellan in February is the color of the inside of a slate and is not, contrary to what every consortium pamphlet I have ever read insists, beautiful."* - keeps
- *"I told them, with a directness I did not soften, that nobody was going to die on this mission if I could help it, and that I was going to help it."* - keeps
- The **"He did not"** run-of-six in ch02 - explicit held exception

## Telemetry after the tuning

| Chapter | Words | Verdict | Anaphora max_run | Tricolons |
|---|---|---|---|---|
| ch01-departure.trial.md | 4,705 | green | 3 (briefing catalog) | 9 (down from 11) |
| ch02-recruitment-interview.trial.md | 6,226 | red (held exception only) | 6 (the *He did not* exception) | 6 |

Both chapters re-rendered on Kokoro (af_alloy @ 0.92x). ch01 22:53; ch02 31:30. Both shorter than the prior renders by ~30 seconds each - consistent with the Bobiverse-pull cuts.

## Engineering follow-on

The prose-telemetry platform's `held_lines` schema annotation (proposed in `icm/01_discovery/02-prose-telemetry-phase-1/ch02-redo-notes.md`) is now empirically required, not just nice-to-have. Without it, the ch02 verdict will permanently read red on a held exception that has been formally approved. Phase 2 of the platform should land it.

## Process note

Two parallel Claude Code sessions worked in this repo today (a Vol-1 dissertation refactor session and this Vol-2 voice-tuning session). The Vol-1 session ran `git add -A && git commit && git push` which swept this session's in-flight work into commit `2cc80df` under the Vol-1 commit message. No work was lost, but the audit trail required this follow-up decision doc to reconstruct what *actually* shipped in that commit.

Recommendation: when multiple sessions work in the same repo simultaneously, the first session to reach a commit point should announce its scope (e.g., via `.pao-inbox/_locks/<session>.lock` or `git stash` etiquette) so parallel sessions know to either wait or commit only their own files (`git add <specific paths>` rather than `git add -A`). This pattern will recur as galley/ + the-inverted-stack/ + Sunfish/ multi-repo work expands.
