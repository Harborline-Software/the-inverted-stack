---
type: resumed
chapter: ch13 + ch14 (Phase 4a Block 1C)
last-pr: pao-directive-2026-05-01T05-15Z-phase4a-prune-pass.md
branch: polish/yeoman-phase4a-ch13-14
---

**Verdict: very light pass; -37 words across two spec chapters; lint clean. Both chapters were already lean.**

## Ch 13 - Schema migration and evolution (4,363 → 4,346, -17 words)

3 small cuts:

1. **§Three-mechanism intro** - collapsed "Each handles a different class of schema change. The architecture requires all three because no single mechanism covers the full range." into one sentence with a semicolon. The two clauses said the same thing twice.
2. **§Expand Phase** - collapsed three-sentence "No coordination is required... Any node can upgrade. The expand-phase behavior is immediately correct..." into one sentence with a colon list. The trio restated the same property in three forms.
3. **§Contract Phase** - cut "Entering the contract phase is a deliberate operational act, not a timer." (Restated the prior two sentences "The contract phase does not begin automatically when the compatibility window expires. It requires explicit initiation by the epoch coordinator.")

## Ch 14 - Sync daemon protocol (4,240 → 4,220, -20 words)

2 small cuts:

1. **§Gossip Anti-Entropy intro** - cut "The protocol specifies that receiving nodes apply inbound operations to their local CRDT document store and update their vector clock accordingly." This sentence was a normative restatement of §Five-Step Handshake's DELTA_STREAM spec ("the receiver applies operations to its local document store and updates its vector clock accordingly" at line 79). Pure restatement of a spec already established two sections earlier.
2. **§Distributed Lease Coordination quorum-fail paragraph** - collapsed "The daemon does not fall back to a best-effort write" and "A blocked write is never silently queued as though it will eventually succeed" into a single closing clause. The two sentences asserted the same negation twice.

## What I considered and kept

- **Ch 13 §Compliance properties of schema history (lines 151–153)** - long jurisdictional enumeration (CIS, Middle East/South Asia, East Asia, Africa). Reference completeness for practitioners; regional consultant-earned material. No cuts.
- **Ch 13 §Couch Device geographic enumeration** - "Sub-Saharan African field operations, rural Indian BFSI deployments, rural Brazilian and Mexican secondary cities, GCC construction sites" - earned regional accessibility framing.
- **Ch 14 §Process Isolation "Picture the X" triplet** - three illustrative scenes that ground the process-isolation invariant. The rhetorical structure does load-bearing work; trimming would weaken the architectural punchline ("The application can fail without the network failing with it.").
- **Ch 14 §Tier 3 Relay "cannot read / cannot inject / cannot modify" triplet** - partly restates the prior signature-mechanism sentence, but the rhythmic triplet has rhetorical force (and "cannot read content" is novel - covers encryption, not signatures). Skip.
- **Ch 14 §Data Minimization regulatory enumeration** - same regional consultant-earned reference material as Ch 13. Stays.

## Word counts

ch13: 4,363 → 4,346 (-17). ch14: 4,240 → 4,220 (-20). Lint: 0 errors, only pre-existing Ch16/Ch22 CLAIM warnings.

## Aggregate

Both chapters are tight Part III specifications. The directive's "illustrative paragraphs that restate the spec's normative claims" framing turned up exactly two true cases (one per chapter): Ch 13's expand-phase trio and Ch 14's DELTA_STREAM restatement. The rest were either earned content or marginal-cut candidates not worth taking.

## Working tree state

- Branch: `polish/yeoman-phase4a-ch13-14` (from `origin/main`)
- Manuscript edits committed as `yeoman-wip(phase4a)` for PAO review/squash/amend.

## Next

Continuing to Block 1D (council Ch 6/7/8/9 - Round-2 acks restating Round-1 critiques).
