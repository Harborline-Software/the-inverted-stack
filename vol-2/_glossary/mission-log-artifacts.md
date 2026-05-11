# Mission log artifacts (pass log, deviation plot)

**Plain replacement:**
- *pass log* → *the run-by-run log* · *the trial log* · *the test-pass record*
- *deviation plot* → *the difference graph* · *the deviation chart*

**Longer gloss:** *During a delicate operation like a schema migration, the engineer running it doesn't just execute the change once and trust it. They run the change in stages — a "pass" — and check after each pass that the data still looks right. The pass log is the chronological record of each pass and what the system was doing at each point. The deviation plot is a side-by-side graph showing where the new data shape diverges from what the old data shape would have produced; ideally the divergence is zero or within a known tolerance.* (use at first occurrence in Ch 13 *The Schema That Should Not Migrate* — Priya's workstation has both up at the lab-engineering bulkhead)

**Audio replacement:**
- *pass log* → *the run-by-run log* (audio always; *pass* alone is too overloaded — football pass, mountain pass, hall pass)
- *deviation plot* → *the difference graph*
- *the third pass* / *the fourth pass* (Anna's Ch 13 yes-with-conditions) → leave alone; ordinal makes operational sense clear

**Keep when:**
- Priya's, Joel's, or Anna's Ch 13 dialogue — engineer voice marker; they would say *pass log* / *deviation plot* in their working register.
- Anna's filed *yes-with-conditions* (*if the third pass surfaces a single read-skew event, the rollback is automatic*) — formal procedural register.

**Mistaken for:**
- *Pass* (football, mountain, hall) — none of these. The technical sense is *one execution of a multi-stage operation*.
- *Plot* (story plot, garden plot) — distinct from *deviation plot*; the technical sense is *graph showing X versus Y*.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "imagine a chef testing a new cake recipe by baking three batches with slightly different timing, then writing down what each batch looked like and drawing a chart showing how each one differed from the recipe's expected result. The pass log is the batch-by-batch diary; the deviation plot is the chart." The chef-testing-three-batches image is the workshop entry's load-bearing element.
