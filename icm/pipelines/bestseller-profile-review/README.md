# Bestseller Profile Review — ICM Pipeline

Per-chapter UPF (Universal Planning Framework) evaluation against two orthogonal rubrics, dispatched in parallel via Sonnet subagents, consolidated by a PAO orchestrator. Read-only against the prose. Writes only state-snapshot reports.

**Use when:** you want to grade a volume (or a subset of chapters) for literary craft + commercial readiness without touching the prose. The output is a volume-wide grading matrix + a prioritized edit list, not a set of prose changes.

**Established:** 2026-05-20, from the first volume-wide vol-2 dispatch. See `icm/pipelines/bestseller-profile-review.yaml` for the canonical machine-readable pipeline definition.

---

## The two rubrics

### Literary devices checklist
1. Clear, consistent POV serving the story's emotional core.
2. Distinct tone and diction that fit genre and character voice.
3. Effective imagery that engages multiple senses, not just sight.
4. Metaphors and similes that are fresh, precise, and advance theme or character — not just decorative.
5. Symbolism or motifs that recur meaningfully and don't feel forced or unexplained.
6. Foreshadowing that sets up payoffs without telegraphing twists.
7. Irony (situational or verbal) used to deepen meaning or tension, not just as a joke.
8. Occasional structural devices (flashback, frame, time jumps) that clarify and enrich rather than confuse.

### NYT bestseller-profile checklist
1. High-concept premise summarizable in one punchy line a browser would instantly get.
2. Protagonist readers can see themselves in, with clear desire, flaws, and room to grow.
3. Strong, credible antagonist or opposing force that actively drives conflict.
4. Escalating external stakes that keep getting harder to ignore or avoid.
5. Fast, clean pacing: scenes start late, end early, most pages move plot or deepen character.
6. Very readable line-level writing: clear sentences, concrete language, minimal clutter.
7. Emotional payoffs that feel earned and tie back to the protagonist's central want.
8. Title and subtitle short, memorable, easy to spell, promising a clear benefit or experience.
9. Launch potential: concept and package look marketable to a wide audience, not just niche.

---

## Pipeline at a glance

```
00_intake    → scope review request (volume / act / chapter set)
01_discovery → confirm canon docs + chapter files current
02 (SKIP)
03_package   → author per-chapter prompt template (rubric + UPF stages)
04 (SKIP)
05_plan      → dispatch plan (N targets, model assignment, output paths)
06_build     → parallel fan-out (1 Sonnet subagent per chapter, background)
07_review    → orchestrator consolidates → grading matrix + top-N edits
08_release   → executive summary + optional follow-up intakes
```

---

## Why Sonnet 4.6 medium for the fan-out

Per `.claude/rules/effort-policy.md`: per-chapter UPF against a **fixed rubric** is execution-density work — apply the same rubric N times in parallel. Sonnet 4.6 at medium effort:

- Has full prose-analysis capability when the rubric is the framework
- Costs ~⅙ what Opus xhigh would for the same fan-out
- Preserves Opus xhigh budget for the **consolidation pass** at Stage 07, where genuine synthesis judgment matters (clustering edits by theme, prioritizing for volume-wide lift)

Reserve Opus xhigh for the orchestrator role only.

---

## Dispatch shape

All N subagents go in a **single batched Agent-tool message** so they run concurrently. With `run_in_background=true` the orchestrator's heartbeat / inbox monitor keeps running while the fan-out builds. Notifications arrive as each subagent completes.

Each subagent prompt is **self-contained** (cold-start safe — the subagent doesn't see the parent conversation):

1. Memory-read prefix per fleet-conventions subagent dispatch protocol.
2. Chapter file path + canon doc references (SPINE, CHAPTER-OUTLINE, canon.yaml, ANNA-VOICE).
3. Both rubrics in full.
4. UPF Stage 0 / 1 (5 CORE) / 2 (literary 21-anti-pattern + Cold Start) — adapted to literary analysis.
5. Output report target path (under `.pao-inbox/_state-snapshots/`).
6. Return contract: ≤400-word executive summary with:
   - Top 3 strengths (with rubric-item citations)
   - Top 3 weaknesses (cited + actionable fixes)
   - Literary-devices grade (A–F)
   - NYT-profile readiness (green / yellow / red, one-sentence verdict)
   - Single highest-leverage edit
7. Constraints: no chapter modifications, no further subagent spawning.
8. **Live-grep mandate** (added 2026-05-21, see below).

### Live-grep mandate

**Why this exists:** the 2026-05-20 vol-2 dispatch surfaced three false-positive BLOCKERs (ch14 "10+ register instances," ch16 "double-register sentence," ch18 "83 register instances"). All three chapters had been brought to compliance by a prior 2026-05-16 PAO rewrite; the audit subagents read embedded HTML-comment rewrite annotations describing the *pre-rewrite* state and reported those counts as current. The Stage 06 Yeoman edit subagents caught the error by running actual greps before editing — but the audit pass wasted attention on phantom blockers.

**The mandate, included verbatim in every per-chapter prompt:**

> Before reporting ANY quantitative metric (instance counts of motif phrases, register-family occurrences, anti-pattern hits, word counts of specific constructions, etc.), you MUST run a live grep against the chapter's BODY PROSE — explicitly excluding:
> - YAML frontmatter (between the leading `---` fences)
> - HTML comments (`<!-- ... -->` blocks, including multi-line rewrite-audit annotations that document past edits)
> - Embedded code blocks unless they are part of the prose
>
> Do NOT trust embedded rewrite-history annotations, frontmatter tallies, prior galley reports, or prior UPF reports as ground truth for current counts. Those annotations describe historical state, not live state. If you cite a count, the count MUST come from a grep you ran THIS pass on the live file body.
>
> Recommended grep recipe (gnu/bsd portable):
> ```
> # Strip ONLY leading frontmatter (anchored via \A), then HTML comments, then grep.
> perl -0777 -pe 's/\A---\n.*?\n---\n//s' <CHAPTER> \
>   | perl -0777 -pe 's/<!--.*?-->//gs' \
>   | grep -ciE 'YOUR_PATTERN'
> ```
>
> **Why perl not sed (added 2026-05-21 after ch03 v2 audit):** chapters may use body `---` lines as Markdown horizontal rules. The naive `sed '/^---$/,/^---$/d'` treats every body `---` as an alternating fence and silently deletes every other body section between them. Ch03 had two body `---` rules at lines 124 + 190; the sed strip ate the Priya + Joel scenes from the grep counts and ch03's v1 register count came back as 1 when it was actually 3 (at cap). The perl `\A` anchor only matches start-of-file, so the strip touches frontmatter only.
>
> Report the raw count from THIS grep, alongside any qualitative finding. Where a count differs from a historical annotation in the file, note the discrepancy explicitly so the orchestrator can update the annotation.

**Stage 06 gate addition:** orchestrator spot-checks at least 2 reported quantitative metrics against a fresh grep before accepting Stage 07 input. Catches subagents that silently dropped the mandate.

---

## Consolidation (Stage 07)

The PAO orchestrator session (Opus 4.7 + xhigh) collects all N executive summaries and produces three artifacts:

| Artifact | What it captures |
|---|---|
| `volume-grading-matrix.md` | Chapter × rubric grades; spot weakness clusters |
| `highest-leverage-edits.md` | Top 3–5 edits that would most lift the volume; scope-sized |
| `rubric-drift-analysis.md` | Trend vs prior reviews if any; regressions flagged |

Each top-N edit may be promoted to its own chapter-update pipeline intake (`icm/00_intake/`) for execution.

---

## Cost envelope

| Component | Model | Approx cost |
|---|---|---|
| Per-chapter UPF subagent (fan-out) | Sonnet 4.6 + medium | $0.10–0.30 |
| Orchestrator consolidation | Opus 4.7 + xhigh | $1–3 |
| **Total for vol-2-class (18 chapters)** | | **$3–8** |

A full Opus-xhigh fan-out would have been ~$15–25 for the same volume. The Sonnet-for-fan-out + Opus-for-consolidation split is the dominant strategy for any rubric-driven review pipeline.

---

## Failure modes + recovery

- **A single subagent fails:** orchestrator re-dispatches just that chapter (do not re-run the whole fan-out).
- **Orchestrator session dies mid-consolidation:** Stage 06 reports persist on disk; a fresh PAO session resumes from there.
- **Rubric amended mid-pipeline:** bump rubric version + restart from Stage 03; prior reports remain valid against the prior version and should be archived, not overwritten.

---

## Related pipelines

- `icm/pipelines/chapter.yaml` — chapter authoring (this pipeline's downstream beneficiary; top-N edits become chapter-update intakes there)
- `icm/pipelines/book-update-loop/` — volume-wide iteration loop

## Related rubric-style pipelines

This pipeline can be cloned and re-pointed for other rubrics:
- Verne-influence audit (executed 2026-05-20)
- Volume-level UPF (executed 2026-05-19)
- Register-family vary sweep (executed 2026-05-20)

Each followed the same fan-out-then-consolidate shape; this pipeline formalizes it.
