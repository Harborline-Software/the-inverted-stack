# Chapter 2 Redo — Notes & Telemetry

**Date:** 2026-05-12
**Source chapter:** `vol-2/act-1/ch02-recruitment-interview.trial.md` (rewritten this session)
**Source-of-redo:** `vol-2/act-1/ch02-recruitment-interview.md` (v4, listen-test approved)
**Telemetry artifact:** `galley/build/the-inverted-stack/output/qa/ch02-recruitment-interview.trial.prose-metrics.json`

## Redo strategy applied

**Source-mining, not clean-slate.** Per the policy locked after ch01: only the trial chapter is clean-slate; subsequent chapters preserve plot/character/research and re-register the voice. The original ch02 v4 was structurally excellent; the issue was register drift — it sat in literary techno-thriller register while the locked SPINE places Vol 1 of the Anna arc in Bobiverse-with-Janeway register.

## What was preserved exactly

- Staff-history selection-archive frame (April 2026, hash-chained)
- The four-sentences-plus-fifth recruitment moment ("I missed it… The rewrite is what should have been there the first time")
- The five-year backstory (prior mission, undisclosed schema-migration limitation, "technically true and operationally a lie")
- The mother subplot (St. Petersburg, hospital admission, kitchen-table reading, evening call)
- The "gauge in front of you" / military-discipline reveal
- The Sunfish naming withheld for in-person disclosure
- Priya and Wanjiru named by Joel during crew questions
- "I will write the code on the boat" Byzantine-operations beat
- Day-14 closing return
- The closing two-word ledger: *yes / yes*
- Diego watch reference at the close

## What was added (register, motif, and series-arc work)

- **Bobiverse parentheticals + asides** throughout: "as it turned out," "which is to say," dry self-interjections
- **The mother-wound made explicit** — the neighbor's daughter in Lyon, the comparison standard, the stroke-then-silence reframing. Anna names the wound without resolving it.
- **Bakery culture threaded** — the *vatrushka* at the bakery near the institute; postcard from that bakery to Diana the next morning
- **"What it claimed to be" planted twice** — about the paper (after the third reading) and about Diana's drawing (close)
- **Diana installed** — call to brother in Voronezh after the mother call; the moon-shape observation; the *vatrushka* postcard; the drawing taped to the bulkhead in the Day-14 close
- **The "noted and did not yet" motif extended** — Anna noting Joel's not-naming of the institution and explicitly flagging the pattern to the reader ("you may notice, in this account, that I keep doing this")
- **Crew-reading reveal** — Joel had read Priya and Wanjiru's published work before sitting in the wardroom with them. Anna writes this *with the awareness* that those two names will land on the betrayal logs. This is staff-history retrospection making the present read differently to the reader.

## Telemetry verdict — intentional red

| Device | Raw count | per 1k | Sent cov | Max run | Verdict | Note |
|---|---|---|---|---|---|---|
| anaphora | 3 | 0.47 | 2.8% | **6** | ⚠ at-threshold | Run-of-6 is intentional |
| tautological self-equation | 1 | 0.16 | 0.2% | — | ✅ | The "what it claimed to be" frame |
| asyndeton | 48 | 7.56 | 11.0% | — | ✅ | Register feature |
| polysyndeton | 1 | 0.16 | 0.2% | — | ✅ | Modest |
| literal tricolon | 6 | 0.94 | 1.4% | — | ✅ | Modest |
| epanorthosis | 6 | 0.94 | 1.4% | — | ✅ | Modest |

**Document-level:** 6,350 words, 436 sentences, 110 paragraphs. Median sentence 11 words; p90 = 31; longest = 67.

**Word-count vs target:** Target 6,000 (per frontmatter); actual 6,350 (+5.8% over). Inside tolerance.

### Why max_run=6 is held, not fixed

The detected run is the paragraph beginning *"He did not soften any of the four sentences"* — six consecutive sentences cataloging what Joel did NOT do. This is the chapter's rhetorical climax. It's the moment the reader sees the totality of Joel's restraint as one cumulative block, not as six separate observations. Compressing the run destroys the climax.

When the prose-telemetry platform reaches Phase 2 (dashboard binding + threshold drift), the schema should support a `held_lines` annotation that lets the author mark specific cascades as intentional and overrides the verdict to yellow rather than red. For now, the red verdict on this chapter is **a known false positive** and the discovery memo serves as the override record.

This pattern is exactly what the architecture doc anticipated:

> Cutting blind risks over-cutting load-bearing anaphora (chapter-close ritual cataloging, dramatic peaks) or under-cutting decorative anaphora.

The "He did not" cascade is *exactly* a dramatic peak. The platform did its job: it flagged the cascade so the author could decide. The author (CO, by proxy through PAO) decides: held.

### What the other three anaphora runs are

1. **"He had" (3) — Joel's desk objects.** Coffee, notebook, council review. Cataloging. Acceptable at threshold; doesn't load-bear elsewhere.
2. **"He had" (3) — Joel's GC answer behavior.** Named it / walked me / had not pretended. Sequential observation. Acceptable at threshold.
3. **"He did" (6) — the held line.** See above.

### Unintentional cascades removed during this pass

Three additional "I had" and "I will" cascades flagged by the first measurement were unintentional voice slips and got rewritten:
1. The "I will not / I will write / I will further write" mug-giving paragraph rewritten with varied openings
2. The "I had decided / I had written / I had written / I had also written / I had written" notebook-prep paragraph compressed to three sentences with fragments
3. The "I had wanted / I had specified / I had not put / I had said" structural-inverse paragraph rewritten with subject variation

These are exactly the kind of voice-drift the platform exists to catch and the author exists to fix. Net effect: anaphora raw count dropped from 6 to 3 in one pass.

## Recommendation for engineering session

The need for a `held_lines` override mechanism is now empirically demonstrated. Add to Phase 2 scope. Without it, every dramatic chapter will trip the verdict, and authors will start ignoring the dashboard — which is the death of any observability platform.

Proposed schema addition:

```jsonc
{
  "held_lines": [
    {
      "device": "anaphora",
      "at": { "start_char": 12044, "end_char": 12612 },
      "reason": "Chapter rhetorical climax — six 'He did not' sentences cataloging Joel's restraint. Compressing destroys the dramatic peak.",
      "approved_by": "CO",
      "approved_at": "2026-05-12T00:00:00Z"
    }
  ]
}
```

A finding whose span falls inside any `held_lines[].at` range is excluded from verdict computation (still shown in the dashboard with a "held" badge so the data isn't lost).
