# Rollback (roll forward, checkpoint)

**Plain replacement:** *undoing the change* · *reverting* · *backing out* · *rollback* (the term is plain enough on second occurrence)

**Longer gloss:** *If a system is in the middle of a complicated change and something goes wrong, the system needs a way to undo every step it has already taken and return to the way things were before the change started. That undoing is called a rollback. The opposite - completing the change and committing to it - is called rolling forward.* (use at first occurrence in any chapter where the operational sense is doing structural work - Ch 13 schema-migration crisis, Ch 14 leak event, Ch 15 compromised-relay aftermath)

**Audio replacement:**
- *rollback* (noun) → *the rollback* on second occurrence; *the undoing-the-change procedure* on first occurrence in scene if context is unfamiliar
- *roll forward* / *rolled forward* → *committed forward* or *moved forward to the new state*
- *rollback path verified* (Ch 13 procedural register) → *the undoing-procedure verified*
- *automatic rollback* → *automatic undoing*
- *checkpoint* (the noun denoting a saved good state) → *saved good state* or *checkpoint* (the term is plain enough)

**Keep when:**
- Engineer dialogue and Anna's filed log entries.
- Anna's Ch 13 yes-with-conditions (*if the third pass surfaces a single read-skew event, the rollback is automatic; no human-in-the-loop authorization to roll forward*) - formal procedural register.

**Mistaken for:**
- *Rollback* (a price rollback at a store) - partial transfer; the technical sense is more like *undoing every step* than *reducing the price*.
- *Roll back* (the verb phrase, meaning to retreat) - closer to the technical sense; partial transfer.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine you've started rearranging a stack of LEGO blocks and you're halfway done when you realize you've made a mistake. A rollback is putting every block back exactly where it was before you started, in the exact order you took them, so the stack ends up identical to how it began." The undoing-the-LEGO-rearrangement image is the workshop entry's load-bearing element.
