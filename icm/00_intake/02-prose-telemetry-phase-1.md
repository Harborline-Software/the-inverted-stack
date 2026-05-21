---
id: 02
title: Prose-telemetry platform - Phase 1 (Freestylo + StyloMetrix integration)
type: structural
volume: series
priority: P1
requested-by: CO (C. T. Wood)
opened: 2026-05-12
related:
  - .pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md
---

# Prose-telemetry - Phase 1

Build the v1 detector + meter pipeline in `galley/prose/lib/prose_telemetry/`, per the locked architecture. v1 composes Freestylo (detectors) + StyloMetrix (meters) + spaCy (NLP base) + small custom detectors for what Freestylo doesn't cover.

## What this item covers

1. Evaluate Freestylo's coverage of the v1 detector list (anaphora, tautological self-equation, asyndeton, polysyndeton, tricolon, isocolon, epanorthosis).
2. Evaluate StyloMetrix's meter output against the schema's `metrics[]` shape.
3. Build the integration package at `galley/prose/lib/prose_telemetry/`.
4. Wire a CLI: `python -m prose_telemetry --chapter <slug>` → writes `galley/build/<book>/output/qa/<chapter>.prose-metrics.json`.
5. Run against all 18 Vol 2 chapters to generate the corpus baseline.

## Discovery already in flight

Stdlib-only hand-count pilot at `build/prose_telemetry_handcount.py` validates the v2 schema against the new `ch01-departure.trial.md`. Findings filed at `icm/01_discovery/02-prose-telemetry-phase-1/handcount-pilot.md`.

## Suggested next stage

`02_architecture` - confirm Freestylo's actual coverage from the discovery brief; decide composition vs hybrid; size the integration work.
