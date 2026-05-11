# _production — Format outputs

Everything about how the canonical prose in `vol-1/` and `vol-2/` becomes a delivered artifact: ebook, audiobook, video, comic, web reader, print. Formats can evolve here without touching the story text.

## Intended sub-layout

| Folder | Purpose |
|---|---|
| `ebook/` | Pandoc EPUB/PDF outputs, Leanpub preview configs, cover assets |
| `audiobook/` | TTS-rendered chapters, forced-alignment artifacts, overlays, mastering chain — produced by `build/audiobook.py` |
| `web/` | Web reader bundle (currently lives at repo root `web/`; candidate to move here) |
| `print/` | Print-ready PDF, typography overrides, ISBN/colophon files |
| `comic/` | Panel scripts, art references for graphic adaptations (Vol 2) |
| `video/` | Video adaptation assets (trailer, chapter recaps) |

Each format owns its own build inputs and outputs. Shared cross-format assets (covers, glossary, character lists) come from `_series/` and `assets/`.

## Status

This folder is a scaffold. Existing production code currently lives in `build/`, `web/`, and `assets/`; migration into `_production/` is incremental and tracked as ICM intake items, not a single big-bang move.
