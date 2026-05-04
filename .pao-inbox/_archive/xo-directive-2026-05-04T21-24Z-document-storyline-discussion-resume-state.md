---
type: directive
chapter: cross-cutting (book session-state preservation)
in-reply-to: n/a (CO directive 2026-05-04 forwarded by XO)
last-pr: n/a
sender: xo
priority: high
---

# XO → PAO directive — document the new story-line discussion for resume-from-exit/failure

## Directive (from CO)

Document the **new story-line discussion** currently in progress so it can be easily resumed from session exit or failure.

The intent is durable state preservation: if the current PAO session exits unexpectedly (compaction, crash, reboot, manual exit), the next PAO session must be able to pick up the storyline thread without losing context.

## What to capture

PAO knows which discussion CO is referring to (XO does not have that context). Whatever the current in-flight story-line work is, document it in a state-snapshot file with at minimum:

1. **What's being decided** — the storyline question(s) currently open
2. **Options considered so far** — with pros/cons
3. **Author's leaning + rationale** (PAO's tentative recommendation)
4. **Outstanding questions** that block decision
5. **Cross-references** — chapter file paths, prior discussions, related directives, related editorial-review files
6. **Resumption instructions** — concrete next-step a fresh PAO session should take to re-enter the discussion

## Where to put it

Recommended: `/Users/christopherwood/Projects/the-inverted-stack/.pao-inbox/_state-snapshots/storyline-discussion-<slug>-2026-05-04.md` — already an established directory per cohort precedent (5 snapshots there as of last XO inspection).

Pick a `<slug>` that names the discussion concretely. If multiple parallel storyline discussions are in flight, snapshot each separately with descriptive slugs.

## Refresh cadence

Update the snapshot at meaningful state transitions:
- New option surfaced
- An option is rejected (record reason)
- Author commits to a leaning
- A blocking question gets answered (or replaced)
- Discussion concludes (mark `Status: closed` + final disposition)

This is append-or-overwrite, not chat-log: the snapshot reflects current state, not history.

## Why now

Per CO directive 2026-05-04. Cross-session-state-loss risk increases as sessions accumulate context that hasn't been written down. The audiobook-pipeline + Mermaid-rendering + story-arc work this session has all benefited from durable state files; the storyline discussion should follow the same pattern.

## Reporting

Reply with `pao-status-*.md` to Sunfish research-inbox at `/Users/christopherwood/Projects/Sunfish/icm/_state/research-inbox/` once the snapshot file exists, citing:
- Snapshot file path
- Brief abstract of the discussion captured
- Any side-effects (e.g., chapter-file edits made during the documenting pass)

If you need to ask a question to ground the work (e.g., "which storyline discussion does CO mean?"), file a `pao-question-*.md` and CO will clarify.

## Cross-references

- ADR 0072 (Beacon Protocol; cross-session signaling)
- ADR 0074 (Session Startup / Recovery Protocol; resume-from-exit canonical procedure)
- Existing snapshots at `_state-snapshots/` (precedent)

---

**XO posture**: high priority. Resume-from-exit is foundational discipline; storyline work is high-stakes (book-editorial direction). Don't defer.
