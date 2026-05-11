# ICM — Iterative Chapter / Content Manufacturing Pipeline

The `icm/` directory is the story-change pipeline for this repo. Every new chapter, revision, or cross-format adaptation moves through transparent stages, with artifacts landing in predictable places. This file is the orientation doc; each stage folder carries its own `README.md` describing its inputs, outputs, and exit criteria.

## Why this exists

The repo holds two volumes plus their cross-format productions (ebook, audio, web, print). Without a pipeline, decisions and drafts scatter across chapter folders, planning docs, and inbox beacons, and the same discovery work gets repeated each session. `icm/` is the durable workspace where in-flight changes live until they land in canon (`vol-1/`, `vol-2/`) or in production (`_production/`).

## Pipeline stages

| Stage | Folder | Purpose | Exit criterion |
|---|---|---|---|
| 0 | `00_intake/` | New requests, briefs, change proposals enter here | Triaged into a numbered work item |
| 1 | `01_discovery/` | Research, source-paper grep, prior-art notes, conformance scoring | Discovery brief committed |
| 2 | `02_architecture/` | Structural decisions: outline shape, chapter placement, arc impact | Architecture note approved |
| 3 | `03_package-design/` | Per-chapter design: scene list, beats, citations plan, voice plan | Design doc ready for scaffolding |
| 4 | `04_scaffolding/` | Skeleton drafts, outline expansion, section headers, code snippet stubs | Scaffold reviewed |
| 5 | `05_implementation-plan/` | Drafting plan: who/what/when, agent assignments, gates | Plan locked |
| 6 | `06_build/` | Active drafting and revision artifacts | Draft hits target word count |
| 7 | `07_review/` | Technical review, prose review, council/board reviews, voice check | All reviews PASS |
| 8 | `08_release/` | Final assembly, format export, audiobook regen, web publish | Released to canon + production |

`pipelines/` holds reusable pipeline definitions (YAML/JSON) and scripts that drive items through these stages.

## Naming convention

Work items use a numeric prefix and a slug: `NN-short-slug/` inside each stage folder. The same item keeps its number as it moves between stages — e.g., `12-ch15-security-split/` flows from `00_intake/12-ch15-security-split.md` through `07_review/12-ch15-security-split/` to `08_release/12-ch15-security-split.md`.

## Relationship to existing structure

- **`vol-1/`, `vol-2/`** — canonical prose. ICM produces changes; canon receives them.
- **`_production/`** — format outputs (audiobook, web, ebook, print). Release stage hands off here.
- **`_series/`** — shared world bible, long arcs, cross-volume continuity. Discovery and architecture consult here.
- **`.pao-inbox/`** — short-form coordination beacons. Long-form artifacts live in `icm/`.
- **`docs/book-update-plan/working/`** — predecessor of `icm/06_build/`. Existing work items will migrate as they touch the pipeline; no bulk move.

## How to start

1. Drop a brief into `00_intake/` describing the change.
2. Run discovery into `01_discovery/` (or invoke the relevant skill — `local-first-properties`, `inverted-stack-conformance`).
3. Promote through stages as gates pass.
4. Release lands the change in `vol-*/` and triggers `_production/` regeneration.
