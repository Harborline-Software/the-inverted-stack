# _series - Shared series bible

Cross-volume canon: world rules, long arcs, character continuity, recurring locations, technology canon, and naming conventions. Anything that must stay consistent across `vol-1/`, `vol-2/`, and future volumes lives here.

## Intended sub-layout

| Folder | Purpose |
|---|---|
| `world/` | Physical and political world: geography, organizations, regulatory regimes |
| `tech-canon/` | Sunfish architecture canon, protocol conventions, CRDT engine choices, security model - what the in-universe technology is and is not |
| `characters/` | Character sheets, voice registers, arc trackers (currently in `.pao-inbox/_creative/character-sheets/`; candidate to migrate) |
| `arcs/` | Long-running narrative arcs spanning multiple volumes |
| `chapter-registry.yaml` | Authoritative map of chapter IDs → titles → file paths → volume/part/act → status |
| `glossary.md` | Cross-volume glossary (Vol 1 and Vol 2 each maintain their own; this is the union) |
| `style/` | Cross-volume style guide overrides (per-volume guides live under `docs/style/`) |

## Why centralize

- Continuity errors are the most expensive bugs in a multi-volume work. A single canon location lets reviewers and AI agents check against one source of truth.
- New volumes inherit from `_series/` rather than re-deriving world rules.
- The chapter registry replaces ad-hoc filename conventions for cross-references.

## Status

This folder is a scaffold. Existing canonical content lives in `book-structure.md`, `.pao-inbox/_creative/`, and chapter-local notes; migration is incremental and tracked as ICM intake items.
