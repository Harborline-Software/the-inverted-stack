---
type: resumed
chapter: ch04 (Phase 4a Block 1B)
last-pr: pao-directive-2026-05-01T05-15Z-phase4a-prune-pass.md
branch: polish/yeoman-phase4a-ch04
---

**Verdict: light pass; -102 words; lint clean.**

## Scope correction for PAO

Directive said: "Per-Zone Compliance Posture. Specifically: each of the four zones restates the compliance framework. Look at whether one canonical statement plus zone-specific deltas reads tighter than four full restatements."

Reality on the page: §Per-Zone Compliance Posture is a **regulatory-regime × Zone matrix table** (10 regimes × 3 zones = 30 cells, each a 1–2 sentence specific compliance posture). It is NOT four-zone narrative restatement of one framework. The framework is named once in the intro paragraph; the table is per-(regime, zone) cells; the closing paragraph names the structural inversion.

Also: there are **three** zones (A, B, C), not four. The Zone narrative descriptions earlier in the chapter (lines 184–204) are tight and don't restate a "compliance framework" — they describe applicability and operational picture per zone.

The boilerplate-collapse hypothesis didn't apply. I did a broader earn-its-place pass on the chapter and found 4 cuts.

## Cuts applied

1. **Line 28 — precedence-chain paragraph closer** — cut "The five-filter sequence is therefore a precedence chain, not five independent tests." (Paragraph-summary closer; the two preceding "If F1 stops..." / "If F1 and F2 pass..." sentences instantiate the precedence chain.)

2. **Line 60 — Filter 2 parenthetical** — cut the regulator-custodian-as-F1-hard-stop parenthetical entirely. Lines 68–70 cover the same point with more substance ("If a regulatory custodian — not the user, not the vendor, but a regulator — must hold the authoritative copy..."). The parenthetical was a forward-pointer that the next paragraph delivered in full; classic restatement.

3. **Line 156 — Three Outcome Zones intro** — collapsed two doubled framings ("anchor points on a spectrum, not a strict partition" + "Read the Zones as the three positions most teams settle at, not as the only positions the architecture supports"). Both said the same thing — Zones are not a strict partition. Kept the first formulation, integrated the in-between-Zone example, dropped the second restatement.

4. **Line 223 — §Per-Zone Compliance Posture closing paragraph opener** — cut "The table inverts a common assumption." (Meta-commentary; the next sentence "Local-first does not skip compliance; it shifts where compliance burden sits" IS the inversion. The meta-line just announced the punchline.)

## What I considered and kept

- **Filter 5 four-engineering-skills block (lines 140–148)** — long but each skill carries its own substance and the closing engineering-vs-operational-capability paragraph (line 150) ties to the playbooks in Part IV. No cuts.
- **§Filter 4 Zone B carve-outs (line 194)** — the "small-team, fast-ship, low-stakes greenfield" sentence carries earned nuance from a literary-board pass. Stays.
- **Worked example (lines 225–239)** — every filter-decision sentence carries the example's substance. No cuts.
- **§What You Have Earned closer (lines 261–265)** — earned closer; sets up the council chapters. No cuts.
- **Per-Zone Compliance Posture table itself** — every cell is precise compliance language; no collapse without losing precision.

## Word count

ch04: 4,909 → 4,807 (-102 words). Lint: 0 errors, only pre-existing Ch16/Ch22 CLAIM warnings.

## Working tree state

- Branch: `polish/yeoman-phase4a-ch04` (from `origin/main`)
- Manuscript edits committed as `yeoman-wip(phase4a)` for PAO review/squash/amend (per the workflow established for Block 1A — single working tree forces serialization or wip-commit-per-branch; chose wip-commit so multiple polish branches can stage work in parallel).

## Next

Continuing to Block 1C (Ch 13/14 spec chapters).
