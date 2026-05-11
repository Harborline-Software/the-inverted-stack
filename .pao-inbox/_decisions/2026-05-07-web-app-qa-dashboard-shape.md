# Web App QA Dashboard — Architectural Shape

**Date:** 2026-05-07
**Author:** PAO (consolidating CO directive 2026-05-07T14-27Z + follow-up brainstorm)
**Status:** Proposal for CO engineering session
**Supersedes:** none
**Related:** `.pao-inbox/co-session-2026-05-07T14-27Z-web-reader-enhancements.md`

---

## Context

CO has built a web reader at `localhost:3080` covering: chapter reading, sticky audio player with whispersync, multi-track support, editorial-review toolbar that submits comments to `.pao-inbox/`, and a Chatterbox render queue UI with active-log-tail.

CO has now reframed the app's purpose: **not just a reader — a QA tool for book artifacts**, including operational dashboard surfaces and a pre-publication preview pane. The reader UX is one of three axes, not the whole app.

This decision document consolidates the three QA axes — **operational, per-chapter, pre-publication** — into one coherent design so the engineering session has a single planning artifact.

---

## Goal

A unified web app where CO can:

1. **Read and listen** to any chapter (current capability).
2. **See the artifact-generation pipeline's health and progress** at a glance.
3. **Find broken artifacts** — chapters that fail QA — without running ad-hoc CLI checks.
4. **Preview final pre-published artifacts** (EPUB, M4B, per-format submission packages) before sending to Audible / Kindle / Apple Books / Kobo / Leanpub.
5. **Route any QA finding** to PAO / Yeoman as a structured beacon, with click-to-fix for common cases.

Success: CO can decide *"this chapter is publish-ready"* or *"this chapter needs work, here's the routed task"* entirely from the web app, without dropping to terminal.

---

## Three QA axes

### Axis 1 — Operational dashboard (live pipeline visibility)

**Purpose:** When something in the rendering pipeline is broken, CO sees red within seconds. Today, the chunk-90 wedge took several hours to detect.

**Surfaces:**
- Server-health dot (top-right of every page) — green / yellow / red based on gateway reachability + last-success age.
- Pipeline status strip (top of every page) — queue depth, active render's chunk progress, ETA.
- Active-log-tail panel (already exists; extends).
- Render history with retry / poison markers.

**Signals:**
- Gateway alive (`HTTP 200` on `/v1/audio/voices`)
- Last-fresh-inference age (RED if > 5 min since last successful synth)
- Queue: pending count, active count, recently-failed count
- Chunk progress: N/M, character count, rolling chunk-time average → ETA
- Cache hit rate (sub-second chunks vs fresh-inference chunks)
- Retry count per chunk; 4+ retries flags a yellow marker; 8/8 fail flags red

### Axis 2 — Per-chapter QA card (artifact health)

**Purpose:** Every chapter has multiple artifacts; each can be broken independently. CO sees per-chapter status in the sidebar without opening each one.

**Surfaces:**
- Sidebar chapter card extends from current voice-track-color dot to a multi-chip status row.
- Click chapter → detail view shows full QA breakdown.

**Per-chapter chips:**
- **Prose** — word-count vs target (±10%), ICM stage, open editorial reviews count.
- **Voice / style** — voice-pass status (Pass 1 / Pass 2 / final), style-enforcer pass, anti-AI-tells flag count.
- **Audio render** — chunks N/M complete, retry markers, poison flags.
- **Audio quality** — loudness (LUFS, true peak vs spec), duration vs (words ÷ 150 WPM) sanity.
- **Audio glossary** — substitutions applied count vs expected; flags missing-coverage chapters.
- **Alignment** — staleness (mtime drift), word-count drift between MD and alignment JSON.
- **Cross-references** — broken citations, missing Appendix entries.

**Color semantics:**
- Green: passes the gate
- Yellow: passes but with warnings (e.g., loudness within ACX spec but at the edge)
- Red: fails the gate (action required)
- Gray: not yet rendered / not yet measured

### Axis 3 — Pre-publication preview (per-format submission readiness)

**Purpose:** Before submitting to an external platform (Audible, KDP, Apple Books), CO needs to verify the final artifact in the format that platform will receive — not the source markdown.

**Surfaces (new routes):**

| Route | Renders | Checklist |
|---|---|---|
| `/preview/epub` | Final EPUB via embedded `epub.js` reader | epubcheck output, file size vs per-target limits, TOC depth, cover dimensions, metadata, mermaid render success, embedded font list |
| `/preview/audiobook` | M4B in HTML5 player with chapter-marker navigation | Per-chapter loudness, duration sanity, M4B chapter-marker count, embedded cover, total runtime, file size |
| `/preview/whispersync` | Side-by-side audio scrub + text-follow | Per-chapter parity, alignment coverage %, drift visualizer |

**Active submission target: Apple Books** (CO directive 2026-05-07, narrows from earlier multi-target list)

| Target | Format | Spec source |
|---|---|---|
| **Apple Books — EPUB** | EPUB 3 | `build/specs/apple-books-epub.yaml` (file-size limit 2 GB; SVG support; embedded-font policy; cover dimensions; iTunes Producer-compatible metadata) |
| **Apple Books — Audiobook** | Per-chapter MP3 + manifest | `build/specs/apple-books-audiobook.yaml` (per-chapter MP3 with chapter-marker metadata, cover art ≥1400×1400; total runtime; total file size; iTunes Producer-compatible metadata) |

**Future targets (deferred — flagged here so the spec system remains generalizable):** Kindle (KDP), Kobo, Leanpub, Audible (ACX). These can plug in later by adding new `build/specs/<target>.yaml` files; the dashboard's target-switcher accommodates new targets without architectural change.

**No switcher in v1** — single active target = no UI complexity. Switcher returns when a second target is approved.

---

## Architecture

### Writer-side (audiobook.py / m4b.py / build_overlays.py / verify_acx.py)

The web app is mostly view-binding. The harder work is on the writer side, emitting structured metrics files the web app reads.

**New / extended files:**

1. **`build/audiobook.py` — JSONL events stream**
   Replace ad-hoc log-line parsing with structured events written alongside the MP3:
   ```
   build/output/audiobook/_logs/<chapter>-<ts>.events.jsonl
   ```
   Row examples:
   ```jsonl
   {"type":"chunk_done","n":79,"of":258,"ms":33214,"cache_hit":false,"chars":140}
   {"type":"substitution_fired","pattern":"St. Petersburg","replacement":"Saint Petersburg","count":1,"workshop_entry":"__abbreviation-hazard"}
   {"type":"retry","n":90,"attempt":4,"backoff_ms":16000,"reason":"timeout"}
   {"type":"chapter_done","total_chunks":258,"total_ms":7912000,"cache_hits":78,"fresh":180}
   ```
   Web app reads JSONL line-by-line via 1s file-watch; never grep.

2. **`build/audiobook.py` — per-chapter metrics file**
   Emitted at chapter render completion:
   ```
   build/output/audiobook/<vol>/<chapter>.metrics.json
   ```
   Schema:
   ```json
   {
     "chapter_slug": "ch01-departure",
     "render": { "engine": "chatterbox", "voice": "ciufi-galeazzi", "preset": "ciufi-galeazzi", "speed": 1.0, "mode": "per-sentence" },
     "audio": { "duration_sec": 1842, "lufs": -16.2, "true_peak_db": -1.4, "bitrate_kbps": 128, "size_mb": 28.7 },
     "alignment": { "json_path": "...", "alignment_word_count": 5277, "source_word_count": 5289, "drift_pct": 0.23 },
     "substitutions": [
       { "pattern": "Bridge replication credentials", "count": 3 },
       { "pattern": "Anchor model weights", "count": 3 },
       { "pattern": "St. Petersburg", "count": 1 },
       { "pattern": "MERIDIAN-7", "count": 6 }
     ],
     "render_completed_at": "2026-05-07T13:42:11Z"
   }
   ```

3. **`build/verify_acx.py` — ACX submission scorecard (extends `verify_loudness.py`)**
   Runs per-chapter ACX-spec checks, writes:
   ```
   build/output/audiobook/<vol>/<chapter>.acx.json
   ```
   Schema:
   ```json
   {
     "chapter_slug": "ch01-departure",
     "passes": ["loudness", "true_peak", "bitrate", "opening_silence"],
     "fails": ["closing_silence_too_long"],
     "warnings": [],
     "details": { "loudness_lufs": -19.1, "loudness_target": -19.0, "loudness_tolerance": 1.0, ... },
     "verified_at": "2026-05-07T13:50:00Z"
   }
   ```

4. **`build/m4b.py` — M4B with chapter markers + cover + metadata**
   Embed:
   - Chapter markers (one per chapter, with title)
   - Cover art (2400×2400 for ACX)
   - Title, author, narrator, copyright
   - Total runtime
   Emit final-build metrics file:
   ```
   build/output/audiobook/the-inverted-stack.m4b.metrics.json
   ```

5. **`build/build_epub.py` — EPUB build metrics + per-target spec validation**
   Run epubcheck, validate against the selected target-format spec, emit:
   ```
   build/output/the-inverted-stack.epub.metrics.json
   build/output/the-inverted-stack.epub.<target>.scorecard.json
   ```

6. **`build/specs/<target>.yaml` — per-target spec definitions**
   Declarative, machine-readable, version-controlled. Web app reads these to render per-target checklists.

7. **`build/qa.py` — per-chapter QA aggregator (NEW)**
   Reads all the per-chapter metrics + alignment + ICM + word-count + substitutions and writes a single rollup:
   ```
   build/output/qa/<chapter>.qa.json
   ```
   Schema:
   ```json
   {
     "chapter_slug": "ch01-departure",
     "prose": { "word_count": 5289, "target": 4500, "delta_pct": 17.5, "icm_stage": "icm/draft" },
     "voice": { "pass_status": "final", "anti_ai_tells_flags": 0 },
     "audio": { "render_status": "complete", "duration_sec": 1842, "lufs": -16.2 },
     "alignment": { "stale": false, "word_drift_pct": 0.23 },
     "open_reviews": 2,
     "open_beacons": 0,
     "overall_status": "yellow",
     "blockers": [],
     "warnings": ["word_count over target by 17.5%"]
   }
   ```
   Web app reads this single file per chapter for the per-chapter card. One file per chapter, atomically written.

### Web-side (transport)

- **File-watch with 1s poll** (CO-confirmed acceptable latency): polls `_logs/`, `_chunk_cache/` size, `*.metrics.json`, `*.qa.json`, `*.events.jsonl`, `_alignments/*.json`, `.pao-inbox/`.
- No server-sent events, no fs.watch / inotify (over-engineered for this latency target).
- Same mechanism CO already built for active-log-tail; extends to all signals.

### Server-health endpoint (added 2026-05-07 from API spec discovery)

The Inference Studio API at port 8881 exposes a real `/api/v1/health` endpoint that returns:

```json
{"status": "ok", "model_loaded": true, "queue_depth": 0, "vram_used_gb": 2.99}
```

The dashboard's server-health dot **binds directly to this endpoint** rather than the earlier "probe `/voices` + measure last-success-age" workaround. The local Node server polls `/api/v1/health` every few seconds with the Bearer token; the dashboard reads the cached response. Real green/yellow/red:

- **Green:** `status === "ok" && model_loaded === true && queue_depth < 4`
- **Yellow:** `model_loaded === false` (warmup) OR `queue_depth >= 4` (saturated)
- **Red:** endpoint unreachable OR `status !== "ok"`

VRAM usage is bonus context for an ops-curious viewer.

### Worker reset endpoint (added 2026-05-07 from API spec discovery)

`POST /api/v1/audio/workers/reset` — replaces manually restarting Chatterbox on the Windows GPU box when the inference worker wedges (the chunk-90 cascade pattern). The dashboard exposes a **"Reset workers"** button that hits this endpoint; the wedge-recovery cycle drops from ~5-10 min of context-switching to a single click. This is the cleanest action affordance the QA tool can offer — most operational, highest payoff per UI element.

### Web-side (routes)

```
/                          — chapter sidebar with per-chapter QA dots
/read/<chapter>            — current reading view + audio player + editorial review toolbar
/ops                       — render queue, server health, chunk progress, log tails, history
/qa/<chapter>              — full per-chapter QA breakdown (drilldown from sidebar)
/preview/epub              — EPUB preview + per-target checklist
/preview/audiobook         — M4B preview + ACX scorecard
/preview/whispersync       — alignment drift visualizer
/inbox                     — open .pao-inbox/ files; submit beacons; resolve
```

Persistent UI across all routes:
- Server-health dot (top-right)
- Pipeline status strip (top)
- Notification bell for `.pao-inbox/` updates

### Action affordances

Every QA finding is actionable. The dashboard isn't useful if CO has to context-switch to terminal. Buttons (calling local Node server endpoints that shell out to make / python):

- `Re-render audio` → `./build/render-chapter.sh <slug>`
- `Verify loudness` → `python3 build/verify_acx.py --chapter <slug>`
- `Re-align` → `python3 build/audiobook.py --only <slug> --alignment-only --force`
- `Rebuild EPUB` → `make epub`
- `Rebuild M4B` → `make m4b`
- `Run full QA` → `python3 build/qa.py --chapter <slug>`
- `File beacon to PAO` → templated `co-review-*.md` with the QA finding pre-filled
- `Open editorial review session` → existing capability

---

## Sequencing

**Phase 0 — schema validation against Ch 1** (immediate, when Ch 1 render lands)
- Manual QA stack run on Ch 1: word-count, ICM stage, loudness, duration, substitutions, alignment freshness, open reviews. This produces the SCHEMA for `*.qa.json`.

**Phase 1 — per-chapter QA card** (highest payoff)
1. Add `build/qa.py` aggregator. Runs against every chapter; writes `*.qa.json`.
2. Web side: extend chapter sidebar to read `*.qa.json` and render multi-chip status row.
3. Add `/qa/<chapter>` drilldown route.

**Phase 2 — operational dashboard** (depends on writer-side events stream)
1. Add JSONL events emission to `audiobook.py`.
2. Add server-health endpoint to the local Node server (backed by `curl` to TTS server).
3. Web side: build `/ops` route with queue, log tails, chunk progress, server-health dot.

**Phase 3 — pre-publication preview** (Apple Books only; independent of Phase 1-2)
1. Add `build/specs/apple-books-epub.yaml` and `build/specs/apple-books-audiobook.yaml`.
2. Add `build/verify_apple_books_epub.py` and `build/verify_apple_books_audiobook.py`.
3. Web side: build `/preview/epub`, `/preview/audiobook`, `/preview/whispersync` routes — single-target rendering, no switcher.
4. (Deferred — when a second target is approved): add `<target>.yaml` + `verify_<target>.py`; reintroduce target-format switcher.

**Phase 4 — action affordances**
1. Local Node server endpoints for each "fix" button.
2. Templated `co-review-*.md` generators per finding type.

---

## Open questions

1. **Authoring vs publishing tools:** the web app started as a reader. As QA-tool scope grows, does it remain consumer-facing (CO uses it) or become an authoring tool the team uses? If the latter, multi-user state, login, per-user editorial sessions become questions.
2. **Local Node server's shell-out boundary:** the action-affordance buttons assume the web app can shell out to `make` / `python3` / `./build/render-chapter.sh`. This is fine on CO's machine. If anyone else ever runs the dashboard, the boundary becomes a security question.
3. **Pre-publication preview formats:** ~~the proposal lists Kindle / Apple Books / Kobo / Leanpub / Audible.~~ **RESOLVED 2026-05-07: Apple Books only for v1** (.epub + per-chapter audiobook MP3s). Other platforms deferred. The spec system stays generalizable so adding Kindle / Kobo / Audible later is additive (new YAML in `build/specs/`), not a rewrite.
4. **Audio re-render trigger granularity:** when CO clicks "re-render this chapter," the wrapper handles cache. Should there be a "re-render only chunks that changed" mode that diffs the current script against the alignment JSON and only re-renders changed chunks? (Probably yes, for fast iteration.)
5. **Deletion / retraction:** if a chapter's audio fails QA, the M4B build inherits the failure. Should the web app gate the M4B rebuild on all chapters passing audio QA?

---

## Recommendation

CO engineering session reads this document end-to-end and decides:
- Confirm the three-axis architecture
- Confirm the writer-side metrics file emissions
- Confirm Phase 0 — Ch 1 manual QA run produces the schema before any UI work
- Decide phase ordering vs CO's editorial calendar (if Vol 2 publication is the hot path, Phase 3 may jump priority; if Vol 1 audiobook is being actively re-rendered, Phase 2 may jump)

Once confirmed, this document becomes the planning artifact for the next engineering session.

---

**Filed by PAO. Ready for CO review.**
