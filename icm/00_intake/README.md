# Stage 0 — Intake

Entry point for new work. Anyone — author, editor, reader feedback, errata, format request — files a brief here.

**Input:** A change idea, bug report, errata, new chapter request, adaptation brief, or stakeholder note.

**Artifact:** `NN-short-slug.md` — one file per item, frontmatter + ≤1 page body.

**Frontmatter template:**

```yaml
---
id: NN
title: Short descriptive title
type: chapter | revision | errata | adaptation | structural | research
volume: vol-1 | vol-2 | series | production
priority: P0 | P1 | P2
requested-by: <name or role>
opened: YYYY-MM-DD
---
```

**Body:** Problem statement, motivation, rough scope, suggested next stage.

**Exit criterion:** Triaged. Either rejected (move file to `00_intake/_archive/`) or promoted (a folder `NN-short-slug/` exists in `01_discovery/`).
