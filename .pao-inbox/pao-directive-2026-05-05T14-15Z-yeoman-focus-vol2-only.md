---
type: pao-directive
priority: P0 (focus directive; supersedes prior queue)
parent-directive: CO directive 2026-05-05 — Yeoman focus shift to Vol 2
expected-output: Yeoman acknowledgment beacon + queue-deferral updates
---

# PAO directive — Yeoman focus shift to Vol 2 (CO directive 2026-05-05)

## Read this first

CO directive 2026-05-05 (in conversation with PAO):

> *change Yeoman's focus to work on volume 2 work only for now, unless the volume 1 work is in support of volume 2*
>
> *we can backlog the volume 1 audio book tasks*

## Effective immediately

Yeoman's active queue is **Vol 2 work only**, with the following exception: Vol 1 work that *directly supports* Vol 2 remains in scope.

## What this defers

The following queued items are **deferred** (not cancelled; backlog with status `defer-vol1-audiobook`):

1. **Audiobook silence-trim option A implementation** — `pao-directive-2026-05-01T22-45Z-audiobook-silence-trim-option-a.md`. Affects Vol 1 audiobook quality; not load-bearing for Vol 2. Defer.
2. **Audiobook alignment regen post-cast-swap** — `pao-directive-2026-05-01T04-31Z-audiobook-alignment-regen-post-cast-swap.md`. Vol 1 alignment artifacts; defer.
3. **Audiobook regen for chapters affected by recent edits** — any pending Vol 1 regen tasks. Defer.
4. **Phase 4 prune (Vol 1)** — quality-driven editorial pass on Vol 1 chapters per `2026-05-01-phase4-prune-scope.md`. Vol 1-only work; defer.
5. **Phase 4b voice-pass extensions (Vol 1)** — voice-pack-#45 dispatch, etc. Defer.

## What stays in scope

The following items *do* support Vol 2 directly and remain active:

1. **Vol 1 *The Crossing* revision pass** — chapter source for Vol 2 Ch 14 (the Crossing leak event); revision required to align with the multi-segment mission design + Anna-read-paper-not-built-it framing + leak-event-as-Diego-survival. Per concept-note §10.2; ~3-5 hour pass; CO-gated. **Stays active.**
2. **Vol 1 preface dual-narrator framing reconciliation** — line 13 currently inconsistent with the new Vol 1-as-Joel's-paper frame per concept-note §10.3. Substantive editorial decision; resolves inconsistency before Vol 2 gets further. **Stays active.**
3. **Vol 1 Ch 1 + Ch 3 cast-swap audit** — `pao-directive-2026-05-01T02-30Z-ch01-ch03-cast-swap-audit.md`. Vol 1 work, but the cast names appear in Vol 2 prose; consistency between the two requires audit. **Stays active.**
4. **STT QC spike Phase 2 (medium on Ch15)** — `pao-directive-2026-05-04T16-30Z-stt-qc-spike-phase2-medium-on-ch15.md`. Spike work; status verification on Vol 1 audio infrastructure. Re-evaluate against Vol 2 needs; if not load-bearing, also defer. **Pending re-evaluation; default-active until reviewed.**

## New Vol 2 priorities

In approximate priority order:

1. **Ch 2 redraft per archive-and-capture canon** — currently being drafted by chapter-drafter agent (dispatched by PAO); Yeoman not directly involved unless agent fails or needs handoff. **Status: in-progress.**
2. **Ch 5 redraft per archive-and-capture canon** — existing Ch 5 draft predates the canon (locked 2026-05-05); needs Pattern C log-opener + diary inset + Anchor groundedness. **Status: pending; drafter dispatch when CO authorizes.**
3. **Vol 2 chapter drafting (remaining 16 chapters)** — gated on listen-test verdict for Ch 2 + Ch 5 listen-test pair (concept-note §9). Once verdict positive, dispatch chapter-drafter on Act I remaining chapters (Ch 1, 3, 4, 6) first.
4. **Vol 2 audiobook rendering** — as chapters reach `icm/draft`, render via GPU-proxied Kokoro endpoint (`build/audiobook.py` default kokoro engine post-PR #111).
5. **Vol 2 chapter outlining adjustments** — outline updates as drafting reveals chapter-level issues; minor edits to `vol-2/CHAPTER-OUTLINE.md`.
6. **Vol 2 character sheet expansion** — Sabina, Diego, Hiroshi, Maria currently at minor-character depth; expand on demand as chapter drafts surface specific needs (concept-note §10.4).

## Working canon Yeoman must read

Before any Vol 2 chapter work:

1. `vol-2/CHAPTER-OUTLINE.md` — UPDATED 2026-05-05; full canon lands here
2. `.pao-inbox/_creative/vol-2-archive-and-capture-convention.md` — locked 2026-05-05
3. `.pao-inbox/_creative/vol-2-anchor-bridge-sync-mechanic.md` — locked 2026-05-05
4. `.pao-inbox/_creative/series-arc-sunfish-trajectory.md` — locked 2026-05-05; **never reference from prose**
5. `.pao-inbox/_creative/vol-2-concept-note-2026-05-04.md` — concept synthesis
6. `.pao-inbox/_creative/character-sheets/` — Anna, Joel, Wanjiru, Stefan all carry NEW Vol 2 archive-and-capture canon layers added 2026-05-05; read those layers before drafting

## What Yeoman does next

1. Acknowledge this directive via beacon: `yeoman-resumed-2026-05-05T*-vol2-focus-acknowledged.md` (1-2 lines; just confirm queue updated)
2. Update internal work tracking to reflect deferrals
3. Read the new canon docs before any further Vol 2 drafting
4. Wait for next PAO directive on specific Vol 2 work (Ch 5 redraft will likely be the next dispatch once Ch 2 redraft + listen-test cycle completes)

## Expected reactivation triggers for deferred items

The deferred Vol 1 audiobook tasks reactivate when:

- Vol 2 reaches `icm/approved` status across all chapters AND the audiobook listenability verdict has landed
- OR CO explicitly reactivates them (which can happen at any time)
- OR Vol 1 distribution pipeline requires them as a release blocker

Until then, the items are durable in the inbox + state.yaml, just not active.

## PAO action

- This directive supersedes the prior queue ordering for Yeoman; deferred items remain in the inbox with their original directives intact, but the active work is Vol 2.
- PAO will re-confirm directly with Yeoman if any deferred item becomes urgent (e.g., a Vol 1 release blocker surfaces).
- CO can override at any time.
