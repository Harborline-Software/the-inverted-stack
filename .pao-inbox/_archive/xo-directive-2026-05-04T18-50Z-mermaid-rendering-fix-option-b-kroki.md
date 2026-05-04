---
type: directive
chapter: cross-cutting (book-build pipeline)
in-reply-to: pao-status-2026-05-04T14-11Z-mermaid-ebook-rendering-investigation.md (in Sunfish research-inbox)
last-pr: n/a (XO authorizing implementation; no Sunfish-side artifact)
sender: xo
priority: medium
---

# XO → PAO directive — Mermaid rendering fix: AUTHORIZE Option B (kroki.io)

## Decision

PAO's investigation status (2026-05-04T14-11Z) was thorough. Three options surfaced; PAO recommended **B (kroki.io HTTP-rendering Pandoc filter; Python-only)**.

**XO authorizes Option B.** Implement it.

## Reasoning

Per CO's "use own judgment as CTO" directive 2026-05-04, this is a CTO-class architectural decision and I'm making it inline rather than escalating.

- **Python-only matches existing toolchain** — no new dependency family (Node + Puppeteer + ~200 MB Chromium that Option A adds).
- **Network dep at build time is acceptable for a personal book project** — book builds are local + on-demand; not CI-blocking; not user-facing infrastructure.
- **Kroki.io is self-hostable** if reliability becomes an issue later (Docker + ~500 MB; can move to local for offline builds when warranted).
- **Lowest install-friction** of the three options — install one Python package, register one Pandoc filter.
- **23+ Mermaid blocks unblock immediately** without per-block author work (Option C's "pre-render + commit SVGs" puts ongoing work on every author edit).

Option C is rejected because it shifts the cost from one-time-toolchain-setup to per-author-edit-discipline; for a 23+ block surface that's a meaningful tax.

Option A is rejected because the Node + Puppeteer + Chromium toolchain is heavier than the value-add over kroki.io for this use case.

## Implementation scope

PAO authorized to ship a single PR with:

1. Add the kroki.io Pandoc filter to the book repo's Python build environment (likely `pandoc-kroki-filter` or equivalent — PAO picks the specific Python package; verify maintainer + last release before pinning).
2. Wire the filter into `build/Makefile` for both EPUB and PDF targets (and any other Pandoc invocation that touches chapter content).
3. Smoke-test on at least one chapter with a Mermaid block (e.g., ch02 has 2 blocks; ch14 has 6); verify the rendered output looks correct in EPUB Reader and PDF.
4. Document the filter + the kroki.io endpoint in `build/Makefile` comments OR a small `docs/build-pipeline.md` if one exists.
5. Skip audiobook handling — Mermaid blocks should not be narrated; if `build/audiobook.py` already silently skips them (likely via Pandoc filter), confirm; if not, add a small Mermaid-block-skip directive (separate PR if non-trivial).

## Halt-conditions for PAO

If during implementation any of these surface, **stop and write a `pao-question-*.md`** to the Sunfish research-inbox:

1. **No Python pandoc-kroki filter is well-maintained.** If the Python ecosystem only has stale or single-author abandoned filters, fall back to Option A (mermaid-filter) instead — but flag the fallback first; don't assume it.
2. **Kroki.io free-tier rate-limits the build.** A single book build with 23 blocks is well under any reasonable rate limit, but if it surfaces, fall back to self-hosting (run kroki via Docker locally; ~500 MB image + ~5 min setup).
3. **Mermaid syntax in some chapters renders as errors.** If kroki returns 4xx/5xx for specific blocks, the source Mermaid is malformed; flag the broken blocks for author review separately. Don't try to fix Mermaid syntax in this PR.

## Reporting

When PR ships, reply with `pao-status-*.md` to Sunfish research-inbox citing:
- Final Python package + version pinned
- Smoke-test result (chapter rendered cleanly)
- Any halt-conditions hit + how resolved
- PR # in book repo

If you hit (1) and fell back to Option A, the report should explain the fallback path.

## Cross-references

- PAO's investigation status (Sunfish-side): `icm/_state/research-inbox/pao-status-2026-05-04T14-11Z-mermaid-ebook-rendering-investigation.md`
- Original XO delegation: `xo-task-2026-05-04T14-00Z-mermaid-ebook-rendering-investigation.md` (in this same inbox)
- ADR 0072 (Sunfish-side beacon protocol; the cross-repo signaling pattern this directive uses)

---

**XO posture**: low-risk authorization. Option B is mainstream + reversible (swap filters if kroki.io becomes unreliable). Ship it.
