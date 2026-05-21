# Stage 1 - Discovery

Research and prior-art before any structural decision. Pulls from source papers (`source/v13`, `source/v5`), the Kleppmann reviews (`source/R1`, `source/R2`), `_series/` world canon, and existing chapters.

**Input:** Promoted intake item.

**Artifacts:**
- `NN-short-slug/brief.md` - discovery summary: what is true today, what needs to change, what sources support each claim.
- `NN-short-slug/sources.md` - citation list (IEEE numeric per `vol-1/appendices/appendix-e-citation-style.md`).
- `NN-short-slug/conformance.md` *(optional)* - output of `local-first-properties` or `inverted-stack-conformance` skill if relevant.

**Tools:** `research-assistant` agent, `local-first-properties` skill, `inverted-stack-conformance` skill, Grep over `vol-1/`, `vol-2/`, `source/`.

**Exit criterion:** Brief committed; sources verified; the one claim the change must land is named in plain English.
