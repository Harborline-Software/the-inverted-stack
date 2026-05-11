# Custody (chain of custody)

**Plain replacement:** *the responsibility chain* · *the ownership trail* · *the chain of who-handled-it* · *custody* (the term is plain enough on second occurrence)

**Longer gloss:** *Chain of custody is a trail showing who handled a piece of data, when, and what they did with it — every party that touched it leaves a signed record, and the record is tamper-evident. It comes from the legal world (chain of custody for evidence in a courtroom) and applies to digital data the same way: who created it, who signed it, who passed it to whom, and on what date.* (use at first occurrence in any chapter where the term is doing structural work — Ch 1 procurement chain references, Ch 13 schema-migration audit trail, Ch 17 transit north [Wanjiru's forensic work])

**Audio replacement:**
- *custody* (technical sense) → *the responsibility chain* on first occurrence in scene; *custody* afterwards
- *chain of custody* → *the responsibility chain* or *the ownership trail*
- *custody operations* (Vol 1 Ch 23 cross-reference) → *custody-and-handover operations* on first occurrence
- *consortium chain* (Vol 2 specific; e.g., *generated against the consortium chain*) → *consortium responsibility chain* — though the chain-of-custody and the consortium key-hierarchy chain are distinct concepts; see notes below
- *procurement chain* → *procurement-and-vendor chain* (clarifies the supply-chain-of-vendors meaning vs the cryptographic-chain meaning)

**Keep when:**
- Wanjiru's dialogue in Ch 17 (forensic supply-chain recognition) — engineer voice marker; she would say *chain of custody* in her professional register.
- Anna's filed log entries.
- Cross-references to Vol 1 Ch 23 *Endpoint, Collaborator, and Custody Operations* — keep the proper-noun-style title.

**Mistaken for:**
- *Custody* (legal — child custody, custody of a prisoner) — partial transfer; the technical sense is closer to *chain of evidence custody* than to family-court custody.
- *Possession* — the technical sense is broader; custody includes the trail of who-had-it-when, not just the current possessor.

**Notes on Vol 2 specific overlap:**
- *Consortium chain* (e.g., Ch 1 *generated against his own root, not on the consortium chain*) is a different concept from chain-of-custody — it refers to the cryptographic key-hierarchy chain rooted at the consortium's root identity. The chapter-lightening pass should clarify *consortium key chain* or *consortium identity chain* in print to avoid the ambiguity.
- *Procurement chain* (e.g., Ch 1 *under the consortium's procurement chain*) refers to the vendor-and-supply chain — yet another distinct meaning of *chain*. The chapter-lightening pass should clarify *consortium's vendor and supply chain* on first occurrence.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "imagine a relay race where every runner who carries the baton has to sign their name on the baton before passing it. At the end of the race, the baton has a list of every runner, in order, and the time each one passed it on. If the baton is dropped, you can tell from the list exactly where the chain broke. Chain of custody is the same idea for a piece of data." The relay-baton-with-signatures image is the workshop entry's load-bearing element.

**Sunfish security canon:** §3 (Generation, Provisioning, Storage — strict media transfer protocol with hashing, scanning, inventory checks; encrypted key bundles on dedicated sanitized media); §9 (audit log preserves the chain). See `.pao-inbox/_creative/sunfish-submarine-security-canon.md`.
