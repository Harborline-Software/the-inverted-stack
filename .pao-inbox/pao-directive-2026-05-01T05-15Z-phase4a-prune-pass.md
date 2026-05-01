---
type: pao-directive
chapter: cross-cutting (Phase 4a — voice-pass-unlocked chapters)
priority: P1
parent-decision: .pao-inbox/_decisions/2026-05-01-phase4-prune-scope.md
expected-output: yeoman-resumed-* beacon per chapter passed; edits unstaged on each pass branch; PAO commits
---

# PAO directive — Phase 4a quality-driven prune pass (voice-pass-unlocked chapters)

## Read this first

Open `.pao-inbox/_decisions/2026-05-01-phase4-prune-scope.md` and read the **Methodology** section. The earn-its-place rubric is the only criterion for cuts. There is no target percentage. There is no word-count goal. Length lands where editorial judgment lands it.

If you find a chapter has nothing that fails the earn-its-place test, the right answer is "no cuts" — say so in the resumed beacon and move on. A chapter at 140% of its industry-standard target is fine if every sentence earns its place. A chapter at 105% is wrong if any sentence doesn't.

## Sequencing

Phase 4a runs in this order. Sequencing matters because some chapters interact with already-queued beacons:

### Block 1 — independent of any pending beacon (start with these)

- **Appendix A** (`chapters/appendices/appendix-a-sync-daemon-wire-protocol.md`) — Sync daemon wire protocol. Look for: state-machine narration that duplicates the protocol diagram; transition descriptions that restate the normative spec.
- **Appendix B** (`chapters/appendices/appendix-b-threat-model-worksheets.md`) — Threat-model worksheets. Look for: shared boilerplate across the 6 worksheets that could collapse into a common prelude with worksheet-specific deltas.
- **Appendix C** (`chapters/appendices/appendix-c-further-reading.md`) — Further reading. Look for: the longest annotations (≥4 sentences) where the annotation restates what a reader can find on the linked source.
- **Appendix D** (`chapters/appendices/appendix-d-testing-the-inverted-stack.md`) — Testing-the-stack. Look for: test-case enumeration redundancy with the chapter's framing prose.
- **Ch 4** (`chapters/part-1-thesis-and-pain/ch04-choosing-your-architecture.md`) — Per-Zone Compliance Posture. Specifically: each of the four zones restates the compliance framework. Look at whether one canonical statement plus zone-specific deltas reads tighter than four full restatements.
- **Ch 13** (`chapters/part-3-reference-architecture/ch13-schema-migration-evolution.md`) — Look at illustrative paragraphs that restate the spec's normative claims.
- **Ch 14** (`chapters/part-3-reference-architecture/ch14-sync-daemon-protocol.md`) — Same standard as Ch 13.
- **Ch 6, 7, 8, 9** (council chapters) — Look specifically for Round-2 acknowledgment paragraphs that restate the Round-1 critique already named in the chapter structure. Recent literary-board polish grew these chapters; some of the polish carried doubled passes through the council frame.

### Block 2 — depends on the cast-swap audit beacon

- **Ch 1** (`chapters/part-1-thesis-and-pain/ch01-when-saas-fights-reality.md`) — Hold this until your earlier `pao-directive-2026-05-01T02-30Z-ch01-ch03-cast-swap-audit.md` beacon has been written. The cast-swap audit will surface specific trim candidates. Apply the earn-its-place rubric to Ch 1 *after* the cast-swap audit's edits are in place.

If you process the cast-swap audit beacon before reaching Block 2, fold Ch 1's Phase 4a pass into the same working session — single resumed beacon for both.

## Working pattern (per chapter)

For each chapter:

1. **Branch.** `git checkout -b polish/yeoman-phase4a-<chapter-id>` from main.
2. **Read end-to-end.** First read is structural — what does the chapter argue, where does it go.
3. **Second pass: rubric.** Re-read with the earn-its-place rubric in hand. Mark candidate cuts with `<!-- PRUNE-4A: ... -->` inline (rationale in 1 sentence per cut).
4. **Third pass: defend.** Read the marked passages with the cuts mentally applied. If the chapter still holds together at the level of argument and at the level of voice, apply the cuts. If a cut takes something the chapter genuinely needed, leave the marker as `<!-- PRUNE-4A-CONSIDERED-AND-KEPT: ... -->` and explain in 1 sentence.
5. **Lint.** `python3 build/lint.py` — must remain at 0 errors + only the pre-existing Ch16/Ch22 CLAIM warnings.
6. **Word count.** `python3 build/word-count.py | grep -E "<chapter-id>"` — capture before/after.
7. **Beacon.** Write `yeoman-resumed-2026-05-01THH-MMZ-phase4a-<chapter-id>-complete.md` with: chapter, before/after word count, list of cut categories applied (e.g. "3 paragraph-summary closers, 2 redundant restatements, 1 hedging cluster"), list of `PRUNE-4A-CONSIDERED-AND-KEPT` decisions and reasoning, overall verdict ("clean pass — chapter reads tighter without losing argument" / "minimal scope — 1-2 sentence-level cuts, chapter already lean" / "no cuts — every sentence earns its place").

Do **not** commit. Do **not** push. PAO commits per the 2026-04-29 directive.

If you want to bundle multiple chapters into one branch + beacon (e.g. all four appendices in one `polish/yeoman-phase4a-appendices` pass), that's fine — the resumed beacon should still report per-chapter findings.

## What is out of scope for this pass

Re-read the scope doc's "What is explicitly out of scope" section. Specifically: do not touch material the council R1+R2 / literary board / cast audit asked for; do not touch reference-utility material (Appendix F, Appendix G — which are deliberately not in Phase 4a's chapter list); do not touch council chapter substance below the sentence level; do not touch Part 1 narrative scening beyond redundant phrasing (no reduction in lived altitude).

If you find yourself making cuts that feel large enough to shift the chapter's argument or voice, stop and write a `yeoman-question-*.md` to PAO before proceeding. PAO can adjust scope or have CO weigh in.

## Volume expectation

Phase 4a is light. For most of these chapters the answer will be "small sentence-level cuts" or "minimal scope, chapter already lean". Two chapters likely carry larger surface area for cuts: Appendix B (worksheet boilerplate) and Ch 4 (per-zone restatement). The rest are gentle. If your Block 1 pass turns up large cut volume, double-check the rubric — large prune is a signal that something else is going on, not that you did Phase 4a correctly.

## What this directive is NOT

- Not a Phase 4b directive — voice-pass-locked extension sections (Ch 11/16/20/21/22/23 §extension sections) are explicitly excluded.
- Not a wholesale rewrite — sentence and clause level only.
- Not a reduction-to-target — there is no target.
- Not a re-prosing of council chapters — substance stays.
