# State Snapshot - Friday 2026-05-08 windown (prose-telemetry topic locked for Monday)

**Filed:** 2026-05-08 (end-of-day Friday, US Eastern)
**Author:** PAO
**Purpose:** State snapshot for Monday-morning resume. Read this first to pick up cold.

---

## Topic locked for Monday: prose-telemetry platform

CO directive 2026-05-08 (Friday end-of-day): lock the prose-telemetry topic; resume Monday morning.

**Primary artifact to pick up first thing Monday:**
[`.pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md`](.pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md)

This is the architectural decision document. It captures:
- The detector / meter split (CO research-session feedback integrated)
- Three-layer architecture (registry / detectors / aggregator + GPU-tier carve-out via galley/api)
- Galley-resident placement; standalone repo only "if important enough"
- Schema discipline: raw `detected_devices[]` events + normalized `metrics[]` + OTel-style `dimensions`
- OSS leverage: **Freestylo** as primary detector engine; **StyloMetrix** as primary meter; spaCy as foundational NLP
- v1 scope: 8 detector coverage; 3-5 days integration work contingent on Freestylo coverage

**Open questions in the decision doc** for Monday's engineering session:
1. spaCy install location (galley pyproject.toml vs separate venv)
2. spaCy model selection (`en_core_web_sm` vs `_trf`)
3. Threshold-default derivation (automated baseline pass vs hand-set)
4. Vale export schema for VS Code in-editor highlighting
5. Multi-book namespacing confirmation in galley/build/<book>/output/qa/

**Implicit Monday sequencing:**
1. Engineering session evaluates Freestylo coverage of CO's ear-flagged devices (anaphora, tautological self-equation, asyndeton, polysyndeton, tricolon, isocolon, epanorthosis)
2. Confirms whether v1 is composition (Freestylo + custom for tautology only) or hybrid (more custom detectors)
3. Builds Phase 1: detector → meter → JSON exporter pipeline
4. Runs telemetry against all 18 Vol 2 chapters → produces baseline
5. CO reviews baseline + adjusts thresholds
6. Cull-pass directive issued (revised from earlier GG/HH/II plan to be metrics-driven, not blind)

---

## Current task state (as of windown)

| ID | Subject | Status | Notes |
|---:|---|---|---|
| #11 | Pilot Joel teaching register extension on Ch 7 | **pending** | Ready-for-chapter-drafter; canon at `.pao-inbox/_creative/joel-teaching-register-canon.md`; Sunfish security canon §1/§2/§4 specified as natural pedagogical content; awaiting CO greenlight to invoke chapter-drafter agent |
| #15 | Prose telemetry platform - Phase 1 implementation | **pending** | Locked for Monday per CO directive; engineering session pickup |
| #16 | Update voice-towles + anti-ai-tells skills with antipattern catalogs | **pending** | Locked alongside #15 (same topic; CO said "this topic" inclusive of skill updates); Monday-morning task. Could ship in parallel with #15 since it's PAO-scope and doesn't depend on platform |

All other tasks closed today:
- #9 Ch1 final render - completed
- #10 Phase 0 manual QA - completed (`build/output/qa/{ch01-departure.qa.json, SCHEMA.md}`)
- #12 forced-alignment pilot - completed (deprecated; reverted to sentence-level highlighting; `pao-directive-2026-05-08T01-54Z-revert-to-sentence-level-highlighting.md` for Yeoman)
- #13 α-then-β batch (Ch1 re-render + ch02-ch07) - completed (file-evidence-confirmed; ch07 last touched 16:20 today)
- #14 Towles voice pilot Ch 16 - completed (MP3 at `galley/.../vol-2/ch16-final-ascent--towles.mp3`)
- #17 Janeway voice pilot Ch 16 - completed late Friday (MP3 at `galley/.../vol-2/ch16-final-ascent--janeway.mp3`; 24.2% word reduction; antipattern discipline applied - 22-26 anaphora cascades + 14-18 tautologies cut; three-way ear-test now available: original / Towles / Janeway)

Late-Friday addition: the new `janeway_first_person_voice` skill at `~/.claude/skills/janeway_first_person_voice/SKILL.md` was created with project antipattern-discipline baked in (anaphora cap 2, no tautology, no franchise imports). Captain-register designed for first-person command-decision passages; works as an Anna-voice candidate for Vol 2 because Anna's role aligns natively to the register.

---

## Vol 2 audio render state (as of windown)

Per filesystem evidence at `galley/build/the-inverted-stack/output/audiobook/vol-2/`:

| Chapter | Status |
|---|---|
| Ch 1 (Departure) | Re-rendered today with credential-modules edit; final canonical |
| Ch 2-7 | β batch complete today; render under all 5 bug fixes (189/190/191/212/222) |
| Ch 8-15, 17-18 | **Not yet rendered.** Remaining Vol 2 audio gap - would be Phase β2 work after Monday's prose-telemetry decision lands. |
| Ch 16 (Final Ascent) | Towles voice pilot draft in Dropbox; canonical Chatterbox final NOT yet rendered |

**Note on the file naming pattern in galley/:** ch02-ch07 each have multiple suffix variants (`--af_alloy`, `--af_bella`, plus bare-slug). Worth verifying Monday whether all are Yeoman-side experiments or whether the β batch produced unintended duplicate tracks. Bare-slug should be the Chatterbox/ciufi-galeazzi final per canon.

---

## Other open threads (for Monday review)

1. **Sunfish security canon (`.pao-inbox/_creative/sunfish-submarine-security-canon.md`)** - filed today; §7 narrative-restraint advisory locked. Cross-referenced from 5 workshop entries + Wanjiru character sheet + Joel teaching register canon. No action required Monday; canon is active across all future security-scene prose work.

2. **Galley topology** - confirmed Friday: galley/ is the multi-book platform; chapter source + workshop entries + .pao-inbox stay in this repo; audiobook outputs + web reader + build scripts moved to galley/. Cerebrum captures this.

3. **Inference Studio API surface** - confirmed Friday: `/api/v1/health`, `/api/v1/audio/workers/reset`, `/api/v1/audio/transcriptions`, `/api/v1/models`, `/api/v1/music/*`. Cerebrum captures this. Worker-reset endpoint replaces manual server-restart for chunk-poison wedges.

4. **Forced alignment** - pilot complete; sentence-level highlighting chosen over word-level (CO ear-test verdict 2026-05-08); Yeoman directive filed at `.pao-inbox/pao-directive-2026-05-08T01-54Z-revert-to-sentence-level-highlighting.md`. API STT path (`POST /api/v1/audio/transcriptions`) remains the future option if word-level is reconsidered.

5. **QA dashboard architecture** - decision doc at `.pao-inbox/_decisions/2026-05-07-web-app-qa-dashboard-shape.md`; Apple Books only for v1; three QA axes (operational / per-chapter / pre-publication preview); engineering session work. Phase 0 schema validated against Ch 1 (`build/output/qa/{ch01-departure.qa.json, SCHEMA.md}` - note: this lives in this repo for now; should migrate to galley/ when Yeoman implements `build/qa.py`).

---

## Monday-morning quick-start

If picking up cold Monday:

1. Read this snapshot
2. Read `.pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md` end-to-end (architecture)
3. Confirm with CO whether to proceed with engineering-session pickup or PAO-side prep work
4. If PAO-side prep: take task #16 first (skill updates) - it's parallel-safe and doesn't depend on platform; ships in ~30-60 min
5. If proceeding to engineering: first task is Freestylo coverage evaluation per the decision doc's open questions

---

**Filed by PAO. Topic locked. Have a good weekend.**
