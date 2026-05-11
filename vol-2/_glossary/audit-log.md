# Audit log (hash-chain, watch log)

**Plain replacement:** *the action record* · *the chronological log* · *the audit log* (the term is plain enough on second occurrence) · *the tamper-evident record* (when the security property matters)

**Longer gloss:** *Every important action the system takes is written into a chronological record that can't be quietly altered after the fact. Each new entry is mathematically tied to the entry before it, so if anyone tries to remove or rewrite an old entry, the chain breaks visibly. That record is called the audit log.* (use at first occurrence in any chapter where the term is doing structural work — Ch 1 Wanjiru handoff [hash-chained into the local store], Ch 6 first surface, Ch 13 schema-migration filing)

**Audio replacement:**
- *audit log* → *action record* on first occurrence in a scene; *audit log* afterwards
- *hash-chain* / *hash-chained* → *mathematically tied together* or *cryptographically linked* (the listener has no anchor for *hash-chain*; the everyday meaning of *hash* is breakfast food)
- *watch log* → *watch record* (Ch 1 Wanjiru's *watch log*; the technical sense is closer to a ship's watch log than the cryptographic audit log, but the term still benefits from clarification)
- *signed audit-log entries* → *signed entries in the action record*

**Keep when:**
- Engineer dialogue when *audit log* is the canonical noun.
- Anna's filed log entries — formal procedural register carries the technical term.
- Cross-references to Vol 1 Ch 15 *Security Architecture* and Ch 22 *Key Lifecycle Operations*.
- Wanjiru's specific phrasings in Ch 6 (*the audit log accepted the pre-departure-to-Day-20 batch with no reordering and no rejected counter-signatures*) — operational-procedural register.

**Mistaken for:**
- *Audit* (the financial / corporate accounting sense) — partial transfer; the technical sense is broader (any action, not just financial).
- *Hash* (breakfast / chopped) — the cryptographic *hash* is unrelated; the listener has zero anchor.
- *Log* (firewood / a captain's log) — the captain's-log meaning is closer; both are chronological records. Don't fight this association too hard — it's roughly right.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "imagine a notebook where every page is glued to the next page with a special seal that breaks if anyone tears a page out. You can add new pages on top, but you can't remove or change an old page without everyone seeing the broken seal. That's the audit log." The glued-pages-with-a-breaking-seal image is the workshop entry's load-bearing element.

**Sunfish security canon:** §9 (Monitoring, Logging, Audit — the audit log integrity-protects authentication attempts, privilege escalations, key lifecycle events, and panic / distress operations; logs are summarized for shore at surface windows). See `.pao-inbox/_creative/sunfish-submarine-security-canon.md`.
