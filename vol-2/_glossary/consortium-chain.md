# Consortium chain (procurement chain)

**Plain replacement:**
- *consortium chain* → *the consortium identity chain* · *the consortium key hierarchy* · *the consortium's chain of trust*
- *procurement chain* → *the consortium's vendor and supply chain* · *the procurement and supply chain*

**Longer gloss:** *The consortium chain is the cryptographic hierarchy that proves an action was authorized by the consortium — every action on a consortium asset traces back through a chain of digital signatures to the consortium's root identity. The procurement chain is something different: the trail of vendors and suppliers that built and delivered each piece of equipment on the boat, used to verify that nothing was tampered with along the way.* (use at first occurrence in Ch 1 — Joel's bunk-laptop disclosure surfaces both phrases [*personal keys, generated against his own root, not on the consortium chain* and *under the consortium's procurement chain*]).

**Audio replacement:**
- *consortium chain* → *consortium identity chain* (clarifies it's a key-hierarchy, not a chain-of-custody)
- *procurement chain* → *vendor and supply chain*
- *generated against his own root* → *generated from his own root identity* (clarifies *root* is identity, not plant biology)

**Keep when:**
- Joel's Ch 1 disclosure to Anna — engineer voice marker; he would say *consortium chain* in his procedural register.
- Anna's filed log entries.

**Mistaken for:**
- *Chain of custody* (covered in `custody.md`) — distinct concept; the workshop flagged the chain-of-meanings ambiguity.
- *Supply chain* (the everyday business sense) — closer to the procurement-chain meaning; partial transfer.
- *Blockchain* — irrelevant; the consortium chain is a key hierarchy, not a distributed ledger.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "imagine a school where the principal signs every teacher's authority, every teacher signs every assistant's authority, and every assistant signs every student-helper's authority. To check whether a student-helper is allowed to do something, you trace their permission slip back through assistant, teacher, principal — the chain. The consortium chain is the same idea for digital authority on the boat." The principal-teacher-assistant-helper chain is the workshop entry's load-bearing element.

**Sunfish security canon:** §2 (Key Hierarchy and Authorities — root CA on shore signs intermediate CAs; submarines trust intermediate CAs, never the root directly; everything on the boat chains back to the platform's intermediate CA). §6 (mutual TLS uses this chain to validate platform + gateway certificates). See `.pao-inbox/_creative/sunfish-submarine-security-canon.md`.
