# Plot-grid tool — UPF v1.2 plan

- **Date:** 2026-05-14
- **Author:** PAO (planning session; no implementation)
- **Status:** PROPOSED — awaiting CO approval before any code lands
- **Scope:** new tool `galley/lib/plot_grid` + new artifact `vol-2/_series/plot-grid.yaml`
- **Self-graded quality rubric:** **A** (5 CORE + Stage 0 + FAILED conditions + Cold Start + sparring + Reference Library + Knowledge Capture + replanning triggers)
- **Recommended approach (one sentence):** Author and maintain a small `plot-grid.yaml` (threads × chapters, beats as cells) co-located beside `canon.yaml` in `vol-2/_series/`, and build a thin Python CLI in `galley/lib/plot_grid` (mirroring `story_canon`'s layout) that validates the grid against `canon.yaml`, renders it to markdown, and emits JSON — populating ch01–ch03 from existing prose and outline as the validation set.

---

## Stage 0 — Discovery & Sparring

### 0.1 Existing work

- **`vol-2/CHAPTER-OUTLINE.md` is already half the tool.** Lines 88–107 contain a per-chapter primary-rail / secondary-rail table — effectively a 2-row × 18-column proto-grid. Lines 64–82 list sync-mechanic threads, forensic-substrate threads, and capability-degradation threads with explicit chapter membership (Ch 6 / 11 / 12 / 14 / 16–17 / 18, etc.). The taxonomy of threads exists; the seed beats per chapter exist; what is missing is a structured, machine-readable representation and a way to render it as a grid.
- **`vol-2/_series/canon.yaml`** owns timeline, characters, objects, places, mission, events — but does not own *thread × chapter beats*. `events:` is sparse (4 entries for ch01) and indexed by event-id, not by chapter or by thread. There is no overlap of *purpose*: canon = locked facts; plot-grid = narrative-shape working view.
- **`galley/prose/lib/story_canon`** (Python 3.11, uv venv, click-less `argparse`-based CLI, pyyaml-only, hatchling build, `validate` + `extract` subcommands, JSON output flag, auto-detection by walking up to `_series/canon.yaml`) is the directly transferable template. ~700 LOC including extractors and validator. Schema is "intentionally loose; the validator only consults the keys it knows."
- **`galley/prose/lib/prose_telemetry`** is the older sibling — `lib/X` Python tool with venv reuse instructions. Same shape.

### 0.4 Better alternatives (the load-bearing tradeoff)

Three candidates were considered:

**(A) Extension of `story_canon`** — add a `grid` subcommand that reads/writes thread-beat data inside `canon.yaml`. **Rejected.** Conflates "locked facts" with "narrative working surface." Canon's purpose is to be the immutable spine that prose is checked against; the grid is a *mutable, opinionated authoring view* that will churn during drafting. Mixing them risks the validator yelling about thread-beat drift the way it currently yells about date drift — wrong signal.

**(B) Derive the grid entirely from `canon.yaml` + per-chapter front-matter** — no separate authored YAML; the "grid" is a projection. **Rejected as primary path, kept as Phase F extension.** Two reasons: (1) chapters ch04–ch18 don't yet exist as prose, so there is nothing to project from; the outline blueprint is the only source. (2) The rail taxonomy in `vol-2-software-as-gravity.md` is curatorial — what *belongs* on a thread row is an editorial judgment that the author wants to express explicitly, not infer from heuristics. Pure derivation would either echo the front-matter (zero added information) or guess wrong (false confidence).

**(C) Authored `plot-grid.yaml` + thin validator/renderer.** **Recommended.** Grid lives in `vol-2/_series/plot-grid.yaml`, hand-authored from the outline, cross-validated against `canon.yaml`'s timeline and characters. Tool lives in `galley/lib/plot_grid`. Two artifacts, two purposes, one cross-check.

### 0.9 AHA effect

**The grid is small.** Six threads × 18 chapters = 108 cells. Each cell is a one-or-two-sentence beat or empty. The entire authored YAML is realistically 200–400 lines. The renderer is a markdown table; the validator is "does every `chapter_ref` resolve in `canon.yaml`, does every `date` agree with `canon.timeline`, does every `character` named in a beat exist in `canon.characters`?"

This is **~300–500 lines of Python** plus a YAML file. It is not a Plottr clone. It is a structured outline view with a cross-check. The framing "Plottr-equivalent" risks scope-creeping into scene-level beats, color coding, drag-and-drop semantics, and a web GUI. The author's actual need is: *can I scan one thread across all chapters and see the arc, and can the tool tell me when my grid contradicts canon.*

### Official docs / reference checks

- **Plottr data model** (from public docs): book → series → plotlines (threads) → scenes-per-chapter (cells); each cell has title + description + tags. The 2D rendering is plotlines-as-rows, chapters-as-columns. We adopt the row/column convention; we do not adopt scenes-as-cells (one beat per chapter is sufficient for our register-and-rail purpose).
- **Markdown tables**: Pandoc's pipe-table syntax supports cells with line breaks via `<br>` or via the `multiline_tables` extension. For 18 columns this is wide; the renderer will emit a **transposed** view (chapters as rows, threads as columns) for readability in the book's pandoc build, plus an optional `--orientation=plottr` flag for the row-per-thread original.
- **Mermaid Gantt** is *not* a fit. Gantt encodes time intervals on a continuous axis; threads in this book are discrete-per-chapter, not date-ranged. Considered and rejected.
- **CHAPTER-OUTLINE.md confirmed** to contain chapter-by-chapter detail (4500-word target for ch01 with full beat list including the canonical bunk-laptop disclosure scene; per-chapter primary/secondary rail; log-opener pattern; verification gap). Not act-level summary.
- **canon.yaml `events:` confirmed** to be a flat list of `{id, date, time, location, description?}` records. The plot-grid validator will use `canon.timeline.*` for date sanity and `canon.characters.*` for character existence; it will **not** try to bidirectionally sync `events:` ↔ grid beats (one-way: grid reads, canon stays authoritative).

### Factual verification

- Confirmed: `story_canon` uses argparse not click (the user's prompt said click-based; this is incorrect — `story_canon/cli.py` line 11 imports `argparse`). Plot-grid will mirror argparse for consistency.
- Confirmed: `story_canon` dependency footprint is `pyyaml >=6` only. Plot-grid target: same single-dependency footprint.
- Confirmed: galley root has `lib/` (Python tools), `apps/web/` (web reader), `services/book-server/`, `turbo.json`. Adding a third Python sibling under `lib/` follows precedent.

---

## Stage 1 — The Plan

### 1. Context & Why

The author needs a thread-by-chapter scan-view of *The Filchner Dark* to detect (a) threads that go dark for too many chapters, (b) chapters carrying too much load, and (c) drift between the working blueprint and the locked story canon. The existing per-chapter rail table in `CHAPTER-OUTLINE.md` proves the 2D mental model is already in use but cannot be queried, cross-checked, or rendered as an artifact. A small authored YAML plus a thin Python CLI closes that gap without standing up Plottr.

### 2. Success Criteria

**Pass (all required for "done"):**

- **SC-1** `vol-2/_series/plot-grid.yaml` exists, defines ≥6 named threads, covers ch01–ch18, validates as well-formed YAML and against an in-tool schema check.
- **SC-2** ≥3 chapters (ch01, ch02, ch03) have a beat on every applicable thread (a beat may be the explicit string `__dark__` meaning "thread intentionally absent this chapter" — `null` / missing is treated as authoring-incomplete and flagged).
- **SC-3** `plot-grid validate` cross-checks the grid against `canon.yaml` and catches a deliberately seeded inconsistency (test fixture: a beat dated 2026-02-15 when `canon.timeline.chapter_date` for that chapter is 2026-09-15) with a clear error message naming the chapter and the date conflict.
- **SC-4** `plot-grid render --format md` outputs a pandoc-compatible markdown table that compiles cleanly through the book's existing `make draft-pdf` toolchain. Visual review by author confirms the rendered table is scan-readable.
- **SC-5** `plot-grid` package installs with `uv pip install -e .` against the prose_telemetry venv following the same instructions as `story_canon`'s README.
- **SC-6** Test suite (pytest) covers extractor, validator, and renderer with ≥80% line coverage on the core modules; fixtures include a minimal canon + grid pair.

**Phase F (gated, not required for initial done):**

- **SC-7** `services/book-server` exposes `GET /plot-grid` returning the rendered grid JSON; `apps/web` displays it as a navigable view. Gated on author approval after Phases A–E land.

**FAILED conditions (kill triggers):**

- **KILL-1 — Timeout.** If Phases A–E take more than **4 calendar working days** of focused effort (estimate is 1.5–2 days), pause and re-evaluate scope. The tool is not load-bearing for chapter drafting; if it is consuming more time than the chapters it serves, it is the wrong investment.
- **KILL-2 — Schema churn.** If the `plot-grid.yaml` schema is rewritten more than twice during Phase E (populating ch01–ch03 from prose), the schema is wrong. Stop, return to Phase A, redesign.
- **KILL-3 — Author disuse.** If the author does not consult the rendered grid for editorial decisions within 14 days of Phase E completion, the tool failed regardless of code quality. Archive the package; keep the YAML as a static reference; do not ship Phase F.
- **KILL-4 — Validator false-positive storm.** If the validator emits >5 spurious cross-check errors per `validate` run against a hand-authored, author-believed-correct grid, the cross-check rules are too strict. Disable cross-check by default; demote to opt-in `--strict` flag.

### 3. Assumptions & Validation

| Assumption | VALIDATE BY | IMPACT IF WRONG |
|---|---|---|
| **A1 — Thread taxonomy:** the six rails from `vol-2-software-as-gravity.md` are the right unit for "threads." Plus the three structural-device threads (sync-mechanic, forensic-substrate, capability-degradation) for 9 total. | Phase A: list all 9 candidate threads; for each, can the author write a one-line answer to "what does the arc of this thread look like across the book?" If yes → real thread. If no → cosmetic. | Wrong taxonomy → grid is unusable for scan-readability. Recoverable at low cost (edit YAML); high cost only if downstream consumers (web reader) hardcode thread IDs. Mitigation: thread IDs are author-chosen strings, not enum'd in code. |
| **A2 — Grid vs derived:** authoring is the right primary path, with derivation as Phase F extension. | Phase E: populate ch01 from existing prose AND from outline; compare. If outline-only suffices for grid quality, lean derivation-first in Phase F. If prose adds nontrivial information, authoring stays primary. | If derivation would have sufficed, we wrote 300 lines of Python and a YAML schema we didn't need. Cost of being wrong: ~1 day of effort + a YAML file that becomes documentation. Acceptable. |
| **A3 — Integration with canon:** `canon.yaml` stays authoritative; plot-grid reads canon, never writes it; cross-check is one-way. | Phase C: validator opens `canon.yaml` read-only; tests assert canon file mtime unchanged after validation runs. | If grid ever writes back to canon, we lose the locked-facts guarantee that `story_canon` depends on. High-cost-to-recover (audit canon for unintended drift). Hard contract: plot-grid is a consumer of canon, never a producer. |
| **A4 — Cell granularity:** one beat per (thread × chapter) is sufficient. Not scene-level. | Phase E: try to express the ch01 dockside scenes on the "Trust + prior betrayal" thread as a single beat. If it requires splitting into 2+ beats for fidelity, granularity is wrong. | Wrong granularity → either too coarse (loses authorial intent) or too fine (Plottr-clone scope creep). Recoverable by allowing optional `scenes:` list inside a beat as an array; default stays single-string. |
| **A5 — Pandoc renderability:** a 9-column or 18-row markdown table fits the book's pandoc build. | Phase D: render and feed through `make draft-pdf` against a smoke chapter. | If pandoc chokes on wide tables, fall back to per-thread sub-tables or a JSON-only output with the markdown render being an optional convenience. Acceptable downgrade. |

### 4. Phases (binary gates)

Each phase has a PASS/FAIL gate. No phase enters until the prior phase passes. Scope-based, not time-based.

#### Phase A — Schema design (BOOK REPO)

- **Scope:** create `vol-2/_series/plot-grid.yaml` with header comment, threads block, and chapter block skeleton for all 18 chapters (cells empty). Lock the top-level shape.
- **Files touched:** 1 new (`vol-2/_series/plot-grid.yaml`)
- **Gate (PASS):** YAML parses; all 18 chapters present; ≥6 threads named; schema documented in the file's header comment; author signs off on the shape.

#### Phase B — Package skeleton (GALLEY)

- **Scope:** create `galley/lib/plot_grid/` mirroring `story_canon` layout — `pyproject.toml` (pyyaml only), `README.md`, `src/plot_grid/{__init__.py, cli.py}`. CLI has stub subcommands `validate`, `render`, `extract` that all print "not implemented" and exit 0.
- **Files touched:** 5 new
- **Gate (PASS):** `uv pip install -e .` succeeds against the prose_telemetry venv; `plot-grid --help` works; `plot-grid validate <path>` exits 0 with stub message.

#### Phase C — Parse + validate

- **Scope:** implement schema-load (`load_grid`), structural validation (well-formedness, required fields, thread-id resolution), and cross-canon validation (chapter dates match `canon.timeline`, character references exist in `canon.characters`). Add `__dark__` sentinel handling. Implement `--json` flag. Pytest fixtures: minimal canon, minimal grid, deliberately-broken grid for the SC-3 negative test.
- **Files touched:** `src/plot_grid/{validator.py, schema.py}` (new); `tests/` directory with ≥3 test files.
- **Gate (PASS):** SC-3 negative test passes (validator catches the seeded inconsistency); validator runs against the real `plot-grid.yaml` from Phase A with zero errors on empty cells; pytest line coverage ≥80% on validator module.

#### Phase D — Markdown renderer

- **Scope:** implement `render` subcommand. Two orientations: `--orientation=chapters-as-rows` (default, pandoc-fit) and `--orientation=plottr` (threads-as-rows). Wrap long beats with explicit line breaks. Render `__dark__` as a visual marker (e.g., `·`). Emit to stdout or `--out <path>`.
- **Files touched:** `src/plot_grid/renderer.py` (new); update CLI.
- **Gate (PASS):** rendered markdown compiles cleanly through `make draft-pdf` against a smoke fixture; author visually approves scan-readability on a printed page or web preview.

#### Phase E — Populate ch01–ch03

- **Scope:** author (with PAO assistance) fills cells for ch01, ch02, ch03 across all applicable threads. Use ch01-departure.md + ch02-recruitment-interview.md prose where landed; use CHAPTER-OUTLINE.md entries for ch03 (not yet drafted). Beats where a thread is intentionally absent: `__dark__`. Run `plot-grid validate` after each chapter — must exit 0.
- **Files touched:** `vol-2/_series/plot-grid.yaml` (edited, not re-shaped — if Phase A was right, edits are pure cell fills).
- **Gate (PASS):** ch01–ch03 have a beat on every thread; validator clean; author scans the rendered grid and confirms it tells him something he didn't already know (e.g., a thread that goes dark for an uncomfortable stretch). If the grid surfaces nothing, KILL-3 triggers.

#### Phase F — Web-reader integration (GATED)

- **Scope:** add `GET /plot-grid` endpoint in `services/book-server/server.js` returning rendered JSON; add a view in `apps/web/` that displays the grid with chapter-link navigation.
- **Gate:** author approval after Phase E. Not entered automatically.

### 5. Verification

**Automated:**

- **Tests:** pytest suite in `galley/lib/plot_grid/tests/`. Coverage target ≥80% on `validator.py` and `renderer.py`. CI hook follows `story_canon`'s pattern (if one exists; if not, manual `pytest` before commit).
- **Schema check:** the validator's well-formedness pass runs on every commit that touches `plot-grid.yaml` (pre-commit hook, optional).
- **Cross-canon check:** `plot-grid validate vol-2/_series/plot-grid.yaml` exit 0 enforced in the book repo's `make lint` target (low cost; add one line).

**Manual:**

- **Visual review:** author scans the rendered markdown grid after each Phase E chapter population. Failure mode looked for: a thread that says nothing useful, or a chapter row where every cell looks similar (suggests the thread taxonomy is wrong).
- **Cold scan:** at end of Phase E, a fresh reader (PAO without recent context) reads the grid and reports what arcs they see. If the reported arcs match the author's intent, the grid works. If they don't, the taxonomy or beat-granularity is wrong.

**Ongoing observability:**

- **Drift signal:** every PR that touches a chapter file in `vol-2/act-*/` triggers a manual checklist item: "did this chapter touch a thread? If yes, is `plot-grid.yaml` updated?" This is a process control, not a code control — automation would be over-engineering at this stage.
- **Validation history:** after each `plot-grid validate` run that surfaces a real issue (not author-intended), append a one-line entry to `.wolf/memory.md` per OpenWolf convention.

---

## Selected Conditional Sections

### Risk Assessment

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| Thread taxonomy wrong → grid useless | Medium | High | Phase A gate: author signs off; thread IDs are strings, not enum'd in code; renaming a thread = sed across one YAML file. |
| Schema drift between grid and canon during prose drafting | High | Medium | Cross-canon validation in Phase C catches it on every `validate` run; add to `make lint`. |
| Validator false-positive storm | Medium | Medium | KILL-4 demotes cross-check to opt-in `--strict`; default validate only checks well-formedness. |
| Tool becomes vanity artifact author never consults | Medium | High | KILL-3 timeout (14 days post-Phase-E); accept early archival as a real outcome, not a failure mode to fight. |
| Scope creep toward Plottr-clone (scenes-per-cell, drag-drop) | High | Medium | Explicit non-goals listed in README; Phase F is the only feature-extension lane and is gated. |
| Schema lock blocks chapter-drafter iteration | Low | High | Schema is intentionally loose (story_canon precedent); validator ignores unknown keys; chapter-drafter agents can add free-form notes without breaking validation. |

### Rollback Strategy

Rollback is trivial: `git rm vol-2/_series/plot-grid.yaml && git rm -rf galley/lib/plot_grid`. No external state, no migrations, no dependencies on other tools. Acceptable to archive the YAML file even if the tool is removed — it remains a useful working-notes document for the author.

### Resume Protocol

If this plan is paused mid-execution and resumed in a fresh session, the resuming agent should:

1. Read this plan document (`.pao-inbox/_decisions/2026-05-14-plot-grid-tool-plan.md`).
2. Check `git log --oneline -- galley/lib/plot_grid vol-2/_series/plot-grid.yaml` to determine the most recent phase landed.
3. Verify phase gate for the most recent phase before proceeding. If the gate cannot be re-verified, treat that phase as in-progress and re-run the gate check.
4. Re-read `galley/prose/lib/story_canon/{README.md, src/story_canon/cli.py, src/story_canon/validator.py}` for the package convention.
5. Continue from the next un-landed phase.

### Reference Library

- **Plottr docs** — public site at plottr.com (data model only; we do not adopt the GUI semantics).
- **Pandoc markdown tables** — pandoc-pipe-tables and multiline_tables extension. The book repo's pandoc build is the canonical target.
- **`galley/prose/lib/story_canon/`** — the package this one mirrors. Read first.
- **`vol-2/_series/canon.yaml`** — the cross-check target. Schema documented inline.
- **`vol-2/CHAPTER-OUTLINE.md`** — lines 88–107 (rail table), 64–82 (structural-device threads), 130+ (per-chapter detail). Seed material for cell population.
- **`.pao-inbox/_creative/vol-2-software-as-gravity.md`** — canonical six-rail taxonomy (referenced; do not duplicate in this plan).

### Learning & Knowledge Capture

On completion of Phase E, the author / PAO should append to `.wolf/cerebrum.md`:

- **Key Learning:** the derive-vs-maintain decision and its outcome — did authored cells add information over outline-only derivation, or not?
- **Decision Log:** the thread taxonomy chosen and the one rejected alternative (e.g., if "Mission as survival" got split into two threads during Phase A).
- **Do-Not-Repeat (if applicable):** any schema field that turned out to be unused or harmful.

A short `.pao-inbox/_creative/plot-grid-taxonomy.md` companion note may capture the thread-by-thread rationale if Phase A surfaces non-obvious editorial choices.

### Replanning Triggers

Replan this document if any of these fire:

- Phase A schema churns more than twice.
- Phase C validator emits >5 spurious errors per run (KILL-4).
- Phase E reveals that the six rails are wrong unit-of-grouping (e.g., character-arcs map better than rails do).
- Author requests Plottr GUI features → that is a new project, not an extension of this one.

---

## Stage 1.5 — Hardening Log (adversarial sparring)

| Adversary | Finding | Resolution in plan |
|---|---|---|
| **Outside Observer** | "Who reads the grid? Is this vanity?" The author is the sole reader. The web-reader integration is speculative. | KILL-3 makes "author disuse within 14 days" an explicit kill criterion. Phase F is gated. Plan accepts archival as a real outcome. |
| **Pessimistic Risk Assessor** | "Schema-drift between grid and canon — chapter dates will diverge silently as the canon is edited and the grid lags." | Phase C cross-canon validation; `make lint` integration enforces it; SC-3 is the gating negative test. |
| **Pedantic Lawyer** | "What does 'populated' mean? Every cell filled, or only meaningful ones?" Ambiguity in SC-2. | SC-2 amended: every applicable thread has either a beat or the `__dark__` sentinel. `null` / missing flags as incomplete. Lawyer satisfied. |
| **Skeptical Implementer** | "TDD setup for cross-canon validation — fixture overhead will dwarf the actual code. You need both a minimal canon and a minimal grid for each negative test." | Plan reuses the structure of `story_canon`'s test fixtures (a single small canon + a single small grid in `tests/fixtures/`); each negative test mutates one field of a known-good grid. Fixture overhead bounded to ~50 lines of YAML across all tests. |
| **The Manager** | "This is the third `lib/X` Python tool in galley. When does the shared abstraction get extracted?" | Not yet. Three is the minimum needed to see the pattern. Plan notes (in Knowledge Capture) that after Phase E lands, a brief retrospective should compare boilerplate across `prose_telemetry`, `story_canon`, `plot_grid` and decide whether a `galley/lib/_common/` package is justified. Premature extraction explicitly avoided. |
| **Devil's Advocate** | "Just maintain a markdown table by hand. No tool, no YAML, no validator. The author already maintains the rail table in CHAPTER-OUTLINE.md." | Honestly considered. The rail table is 2 rows × 18 columns and has not drifted. **But** it does not cross-check against canon, does not render alternate orientations, does not support the structural-device threads (sync-mechanic, forensic-substrate, degradation) without becoming unreadable, and offers no way to scan one thread across the book. The tool earns its place only if it does the cross-check and the alternate orientation. If Phase C validation is dropped, the tool is not worth building — and the devil's-advocate path (hand-maintained markdown) wins. **Phase C is the load-bearing phase**; if it cannot be implemented cleanly, abandon the project. |

---

## Stage 2 — Meta-Validation

| Check | Status | Notes |
|---|---|---|
| **1. Delegation strategy clarity** | PASS | All phases land via PAO + author; chapter-drafter agent not involved; technical-reviewer not needed (no Sunfish API claims). |
| **2. Research needs identified** | PASS | Plottr data model (skimmed; non-load-bearing); pandoc-pipe-tables (known); no further research blocks execution. |
| **3. Review gate placement** | PASS | Each phase has a binary gate; Phase D has explicit visual-review gate; Phase E has cold-scan gate. |
| **4. Anti-pattern scan (21 patterns)** | PASS — see below | |
| **5. Cold Start Test** | PASS | A fresh agent given (this plan + `story_canon` source + `canon.yaml`) can execute Phase B without further context. Phase A requires author input on thread taxonomy and is correctly placed as the author-gated step. |
| **6. Plan Hygiene** | PASS | No TBDs in core sections; success criteria measurable; kill triggers concrete with numeric thresholds. |
| **7. Discovery Consolidation** | PASS | AHA finding (the grid is small; 108 cells) is recorded explicitly in §0.9 and shapes Phase A's scope decision. |

### Anti-pattern scan (21 patterns)

- **1. Unvalidated assumptions** — captured in A1–A5 with validation steps.
- **2. Vague phases** — each phase has scoped files-touched and a binary gate.
- **3. Vague success criteria** — SC-1 through SC-7 are measurable.
- **4. No rollback** — addressed (`git rm`).
- **5. Plan ending at deploy** — Phase E ends with cold-scan and 14-day usage check.
- **6. Missing Resume Protocol** — included.
- **7. Delegation without contracts** — N/A (single-agent execution path).
- **8. Blind delegation trust** — N/A.
- **9. Skipping Stage 0** — Stage 0 ran; AHA effect surfaced and reshaped the plan.
- **10. First idea unchallenged** — three alternatives evaluated (A/B/C); C chosen with reasoning.
- **11. Zombie projects** — KILL-1 / KILL-3 timeouts defined.
- **12. Timeline fantasy** — explicit "1.5–2 days estimated; 4-day kill trigger."
- **13. Confidence without evidence** — every claim about story_canon and canon.yaml verified by Read before plan written.
- **14. Wrong detail distribution** — Phase C carries the most detail (load-bearing); Phase F is one paragraph (gated, may not happen).
- **15. Premature precision** — no line-count estimates for individual files; only package-level scope.
- **16. Hallucinated effort estimates** — calendar bounds only, with explicit "estimate is 1.5–2 days."
- **17. Delegation without context transfer** — Resume Protocol covers this.
- **18. Unverifiable gates** — every gate is a binary check on file existence, test pass, or author sign-off.
- **19. Missing tool fallbacks** — pandoc renderability assumption (A5) has a fallback (per-thread sub-tables).
- **20. Discovery amnesia** — Discovery section preserved at top of document.
- **21. Assumed facts without sources** — Plottr data model annotated as "from public docs"; every concrete claim about story_canon / canon.yaml / CHAPTER-OUTLINE cites file paths and line ranges where verified.

---

## Notes

- **OpenWolf compliance:** anatomy.md was consulted before file reads. No new files created in this planning session beyond this plan document. cerebrum.md update is deferred to Phase E completion (entries to add are listed in §Learning & Knowledge Capture).
- **No `_decisions/MEMORY.md` index exists** in this repo, and creating one is out of scope for this planning session (it would be a separate inventory task across ~50 decision files). This plan is discoverable via filename date-prefix convention.
- **Implementation explicitly out of scope** of this session per the prompt's constraints. No code written. No `plot-grid.yaml` written. No edits to `canon.yaml`, `CHAPTER-OUTLINE.md`, or any chapter prose.
