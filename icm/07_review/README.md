# Stage 7 — Review

All adversarial passes against a completed draft. Multi-track and iterative.

**Input:** Draft that meets Stage 6 exit criteria.

**Tracks (run as needed):**
- `NN-short-slug/code-check-report.md` — Stage 3 of CLAUDE.md ICM
- `NN-short-slug/technical-review-report.md` — Stage 4
- `NN-short-slug/prose-review-report.md` — Stage 5
- `NN-short-slug/council-review-round-N.md` — Kleppmann Council (`council-reviewer` agent)
- `NN-short-slug/literary-board-report.md` — Literary Board (`literary-board` agent)
- `NN-short-slug/voice-check-report.md` — author's voice-check (Stage 6, human-only)
- `NN-short-slug/vol2-chapter-review.md` *(vol-2 only)* — `vol2-chapter-reviewer` agent

**Tools:** `/review-cycle` orchestrates iterative passes until PUBLISH or escape; individual reviewer agents can be invoked directly.

**Exit criterion:** All in-scope tracks return PASS / PUBLISH. Open action items either resolved or explicitly deferred with a follow-up intake brief filed.
