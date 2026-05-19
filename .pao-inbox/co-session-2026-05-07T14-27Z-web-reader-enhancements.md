---
type: co-session-summary
scope: web-reader-tooling
session: 2026-05-07T07:00–14:27Z
last-pr: n/a (web/ tooling - not book content)
---

CO engineering session: web reader tool (web/) rebuilt end-to-end. No book content was changed. Summarised here so PAO can update Yeoman's working context and wire in the new editorial review channel.

## What was built

### Audio pipeline
- **ID3 metadata in MP3s** - `audiobook.py` now embeds TTS engine, preset, voice, speed, and mode as TXXX frames on every render. Server reads these as ground-truth; sidecar `.meta.json` and `manifest.json` are fallback.
- **Multi-track support** - multiple voice variants (`{slug}--{voice}.mp3`) coexist per chapter; player shows a track-selector strip. Sidebar dots distinguish draft (Kokoro, lavender) from quality (Chatterbox, green) from planned (amber).
- **Resumable Chatterbox queue** - sequential job queue with always-`--force` so the chunk cache makes every render resumable after a crash. UI shows active log tail, pending list, history, and a batch-add form with chapter checkboxes filtered by "No quality track" or "No audio".

### Reader UX
- **Sticky audio player** - the player row sticks to the top of the chapter viewport on scroll. Keyboard shortcuts: `Space` play/pause, `← →` ±10 s, `Shift+← →` ±30 s, `↑ ↓` volume ±10%.
- **Session persistence** - chapter selection, volume tab, audio position (saved every 5 s), and scroll position (debounced 500 ms) are stored in `localStorage` and restored on page refresh.

### Text-audio synchronisation (Whispersync-style)
Three-layer highlighting driven by per-chapter alignment JSON files at `vol-1/_voice-drafts/_alignments/{slug}.json`:
- **Paragraph** - 7% lavender tint + accent left border on the active `<p>`.
- **Sentence** - 16% tint on the estimated current sentence (only when paragraph has ≥2 sentences; degrades gracefully to paragraph-only for single-sentence paragraphs and mixed-HTML elements).
- **Word** - 42% fill on the estimated current word via linear interpolation across the chunk duration.

Alignment staleness detection: if the MP3 is more than 1 hour newer than its alignment JSON, the sticky player shows `⚠ sync stale - re-render to fix`. Currently only `ch01-departure` is stale (audio regenerated 2026-05-07; alignment from 2026-05-05).

**Fix for ch01-departure:**
```bash
python3 build/audiobook.py --only ch01-departure --force
```
Re-concatenates from chunk cache and rewrites alignment JSON. No re-synthesis needed.

### Editorial review system
CO can now conduct a chapter review session entirely inside the web reader:
1. Select text → floating toolbar → choose type (EDIT / FLAG / NOTE / QUESTION) → type comment → Save.
2. Comments accumulate across multiple chapters in a persistent session (survives page refresh via `build/output/review-session.json`).
3. Click **Submit to PAO Inbox** → writes a structured Markdown file to `.pao-inbox/co-review-{timestamp}Z.md`.

## Actions for PAO

**Brief Yeoman**: CO editorial comments now arrive in `.pao-inbox/` as `co-review-*.md` files with frontmatter `type: co-editorial-review`. Body groups comments by chapter with type badges. Action verb by type:
- `EDIT` → implement the change directly
- `FLAG` → fix the style or quality issue
- `NOTE` → consider, act if clear
- `QUESTION` → answer inline; implement if answer is obvious

**No book content was modified in this session.** The reader tooling is internal only; no chapter files, no PRs, no ICM-stage changes. Yeoman's current work queue is unaffected.

## Current reader tool state

- Served at `http://localhost:3080` via LaunchAgent (`com.inverted-stack.reader`), auto-restarts on crash and at login.
- `npm run build` from `web/` to deploy any future frontend changes; `launchctl kickstart -k "gui/$(id -u)/com.inverted-stack.reader"` to reload the server.
- 50 alignment files exist covering all chapters. 49/50 in sync. 1 stale (`ch01-departure` - see above).
