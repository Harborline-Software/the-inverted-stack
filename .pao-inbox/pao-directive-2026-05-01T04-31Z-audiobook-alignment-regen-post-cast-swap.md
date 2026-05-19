---
type: pao-directive
chapter: ch01 + ch03 + closing/the-crossing + ch15 + ch22 + ch23
last-pr: "#64 + #65 + #59 (all merged)"
priority: P2
expected-output: yeoman-resumed-* beacon with regenerated alignment JSONs + audiobook artifact summary
---

# PAO directive - audiobook alignment regeneration after cast-swap + Phase 7 ref-split

## Context

Three landed-this-week PRs invalidate audiobook alignment artifacts:

1. **PR #64 - cast-swap final batch** (merged 2026-05-01T01:03Z). Renamed + rewrote characters in Ch1 connectivity scenario (Lakshmi → Sabina) and Ch3 §Security Breach (Petra → Hayoon). Two prose passages roughly 250 words each, plus a new King-style scening passage in Ch3.
2. **PR #65 - Phase 7 reference-list split** (merged 2026-05-01T02:24Z). Ch15 references renumbered local 1..8 (was 1..41); Ch22 gained a new 18-entry list; Ch23 gained a new 24-entry list. Body citations across all three chapters renumbered to chapter-local indices.
3. **PR #59 - The Crossing first draft + cast-swap mirror** (merged 2026-05-01T04:23Z). New 4,430-word chapter; cast-swap names + Spanish-letter beat applied during merge.

The alignment artifacts under `vol-1/_voice-drafts/_alignments/*.json` mirror the chapter prose by paragraph; they were generated before any of these PRs. Specifically: `ch16-persistence-beyond-the-node.json` still contains stale Ch15 §section refs (Event-Triggered, Collaborator Revocation, Forward Secrecy) that were redirected to Ch22/Ch23 in the manuscript. `appendix-b-threat-model-worksheets.json` reflects the pre-redirect cite numbering.

## What you are doing

Run the audiobook regeneration pipeline for the affected chapters. Per the audiobook topology memory (Mac dev + Windows GPU + Tailscale), the pipeline regenerates alignment JSONs and audio segments from the current chapter `.md` source.

**Affected chapters:**
- `ch01-when-saas-fights-reality.md` (cast-swap §Connectivity Gradient)
- `ch03-inverted-stack-one-diagram.md` (cast-swap §Security Breach)
- `ch15-security-architecture.md` (citation renumber 1..8)
- `ch16-persistence-beyond-the-node.md` (alignment JSON has stale Ch15 §refs that should be Ch22/Ch23)
- `ch22-security-operations.md` (citation renumber + new ref list)
- `ch23-endpoint-collaborator-ops.md` (citation renumber + new ref list)
- `vol-1/closing/the-crossing.md` (new chapter, no alignment artifact yet)
- `appendix-b-threat-model-worksheets.md` (alignment JSON has pre-redirect cite numbering)

## Deliverable

Run the audiobook pipeline for the eight files above. Write a `yeoman-resumed-2026-05-01THH-MMZ-audiobook-regen-complete.md` beacon with: (a) which chapters successfully regenerated, (b) which (if any) failed and why, (c) any audio quality flags worth surfacing (cast-swap names that the TTS mispronounces - Sabina, Hayoon, Diego, Hiroshi, María Elena, Sofía, Wanjiru, Priya - flag any that need a pronunciation hint or text substitution).

Pipeline artifacts go to their canonical paths; do not commit them - PAO commits binary + alignment artifacts in a single audiobook-regen PR after reviewing the beacon.

## What this does NOT cover

Phase-2 voice-drafts (the JSON files under `_voice-drafts/_alignments/`) regeneration is bundled with the audiobook pipeline if your runbook does it; if not, they're a separate pass and can be deferred - the manuscript-side citations are correct, the alignment files are advisory. Flag in the beacon if the alignment files are out of scope of your usual run.
