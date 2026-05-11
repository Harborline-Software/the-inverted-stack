# Stage 8 — Release

Land the change in canon and trigger downstream production.

**Input:** Reviewed draft that has cleared all in-scope review tracks.

**Actions:**
1. Copy or merge `06_build/NN-short-slug/draft.md` into the canonical location in `vol-1/` or `vol-2/`.
2. Update cross-references: `ASSEMBLY.md`, `book-structure.md`, chapter registry, any TOC.
3. Trigger production regen in `_production/`:
   - Ebook: `make epub` / `make draft-pdf`
   - Audiobook: regenerate alignments and overlays for affected chapters
   - Web: rebuild reader bundle
4. Tag the release in `.pao-inbox/_state-snapshots/` if it materially changes book status.

**Artifact:** `NN-short-slug.md` — release note: what landed, where, with which commits, and what production outputs regenerated.

**Exit criterion:** Canon updated, production rebuilt, item closed. Move the item's `06_build/` and `07_review/` folders to `_archive/` under each stage, or leave them as the audit trail (project preference — default: leave).
