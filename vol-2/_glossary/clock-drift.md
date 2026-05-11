# Clock drift (clock-skew, drift)

**Plain replacement:** *clock drift* (the term is plain enough on second occurrence) · *the clocks slowly disagreeing* (when the noun form reads stiff)

**Longer gloss:** *The way real-world clocks gradually run a little fast or a little slow, so over time different machines disagree about the exact time unless we keep them in sync.* (use at first occurrence in any chapter where the technical concept matters — Ch 9 sync-daemon triage, Ch 13 schema-migration four-pass cycle, Ch 14 leak event)

**Audio replacement:**
- *clock-skew* → *clock drift* (the hyphenated technical noun is harder for the listener; *clock drift* is plainer and means the same thing here)
- *skew* alone (technical sense) → *clock drift* with explicit modifier
- *drift* alone (when technical) → *clock drift* or *time drift* — never let the bare word *drift* carry technical meaning in audio, because it collides with *ice-drift* and *ocean drift*
- *drift* alone (when ice-drift or ocean-drift is meant) → leave alone if context is unambiguous; otherwise expand to *ice drift* or *current drift*

**Keep when:**
- Engineer dialogue when Wanjiru, Priya, or Joel are briefing on operational time-sync issues — they would say *clock-skew* or *the skew*. Audio expansion still applies.
- Anna's filed log entries where formal procedural language carries the technical noun.
- Cross-references to Vol 1 Ch 14 *Sync Daemon Protocol* (clock-skew is the canonical name).

**Mistaken for:**
- *Drift* (boat drifting on a current, ice drifting past the hull) — three different drifts share the page in Vol 2: ice-drift, ocean-drift, clock-drift. The audio listener will conflate them unless the modifier is explicit every time.
- *Skew* (perspective skew, statistical skew) — the technical sense is *clocks disagreeing*; nothing to do with angle or distribution.
- *Sync* (real-time mirroring) — the listener may infer that "kept in sync" means "instantly identical." It means *brought back into agreement*, which is a different and looser property.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "imagine two old wind-up watches on the same shelf; come back in a week and they show different times, even though they started together. That's clock drift, and computers do it too." The wind-up watch image is the workshop entry's load-bearing element.
