---
type: yeoman-resumed
chapter: n/a
last-pr: "75"
---

STT QC spike Phase 1 complete. Two chapters processed with whisper-base (faster-whisper, CPU int8,
RTF≈0.08–0.09). Diff reports at `build/output/stt_spike/`.

## Results summary

| Chapter | Source words | Transcript words | Diff regions | REAL | VARIANT | NOISE | FOREIGN | STALE |
|---|---|---|---|---|---|---|---|---|
| ch01 (narrative) | 7,886 | 7,871 | 265 | 53 (20%) | 200 (75%) | 10 (4%) | 2 (1%) | 0 |
| ch15 (crypto/security) | 6,021 | 5,629 | 281 | 94 (33%) | 163 (58%) | 17 (6%) | 7 (3%) | 0 |

Wall time: ~4.5 min per chapter (Intel i9, CPU int8).

## Key findings

**ch01 (narrative prose)** — VARIANT-dominated. Dominant patterns:
- `saas` → "software as a service" (~50 hits) — TTS expands acronym, not an error
- `priya` → "prier/preer", `pune` → "pooner" — proper noun phonetics, not errors
- Number words ↔ digits — stylistic variation, not errors
- Time digit corruption (REAL ×6): "4:47" → "4:07", "9:30" → "9:000 tree" — systematic base-model
  failure on two-digit time components after decimal context
- `sulfa` → "sulfur" (REAL ×2) — medically significant medication name

**ch15 (security/crypto)** — Higher REAL rate driven by:
- Mathematical notation (ε, λ, σ, δ) completely garbled throughout (REAL ×~20)
- TTS inserting package names from inline code refs: "sunfish colonel security", "sunfish kernel
  sync", etc. (REAL ×8) — `_strip_inline_code` regex misses some patterns
- `sync` → "sink" (REAL ×3) — critical distributed-systems term
- `writes` → "rights" (REAL ×5) — critical CRDT term
- Large section drops (rows 71-72, 75-78, 81, 160, 238, 250-251) — multiple consecutive sentences
  dropped or replaced with garbage; listeners would miss entire functional specifications
- Foreign legal text (Portuguese LGPD, Spanish LFPDPPP, Russian импортозамещение) — FOREIGN ×7
- `counsel` → "council" (REAL) — recurring cross-chapter homophone error

## Model adequacy verdict

- **whisper-base on narrative prose (ch01)**: marginal. Most REALs are time-digit corruption or
  isolated word confusions. A medium listener could follow. Would flag ~53 items for human review.
- **whisper-base on technical/crypto prose (ch15)**: inadequate. Math notation is unreadable,
  large drops miss functional specs. Cannot be used for QC on technical chapters.

## Recommendation for Phase 2 decision

Run whisper-medium (or large-v3) on ch15 specifically to quantify how many of the 94 REAL errors
resolve at higher model quality. Math notation and large drops are the critical unknowns. If medium
resolves >80% of ch15 REALs, medium is the right QC model for technical chapters; base is acceptable
for narrative chapters only. If medium still fails on math, large-v3 is required.

**One additional fix needed in `build/stt_spike.py`**: the `_strip_inline_code` regex misses inline
code patterns inside section cross-references (`[Sunfish.Kernel.Security]`, `[§relay trust model]`).
TTS reads these and produces garbage in the transcript. Fix before Phase 2 run.

## Artifacts

- `build/output/stt_spike/ch01-when-saas-fights-reality_diff.md` — classified, 265 regions
- `build/output/stt_spike/ch01-when-saas-fights-reality_transcript.txt` — raw Whisper output
- `build/output/stt_spike/ch15-security-architecture_diff.md` — classified, 281 regions
- `build/output/stt_spike/ch15-security-architecture_transcript.txt` — raw Whisper output
- `build/stt_spike.py` — spike script (not committed per directive; PAO to commit when ready)
