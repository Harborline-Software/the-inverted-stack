# Pipelines

Reusable pipeline definitions and orchestration scripts that drive items through the ICM stages.

**Intended contents:**
- `chapter.yaml` — default pipeline for a new chapter (intake → discovery → architecture → design → scaffold → plan → build → review → release)
- `revision.yaml` — shorter pipeline for revisions to a shipped chapter (intake → discovery → build → review → release)
- `errata.yaml` — minimal pipeline for typo/factual fixes (intake → build → release)
- `adaptation.yaml` — cross-format adaptation (intake → architecture → build → review → release into `_production/`)
- `scripts/` — Python/shell drivers that promote items between stages

Pipelines are declarative descriptions of which stages an item visits and which agents/skills/gates apply at each stage. They do not replace the per-stage READMEs — they reference them.

This folder is intentionally a stub for now; populate as pipelines are formalized.
