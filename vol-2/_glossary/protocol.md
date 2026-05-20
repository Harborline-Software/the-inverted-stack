# Protocol (procedural vs technical)

**Plain replacement (technical sense only):** *the agreed-upon rules* · *the message format* · *the network protocol* (when network-protocol meaning is the precise sense)

**Longer gloss:** *In the architectural sense, a protocol is a set of agreed-upon rules for how two systems talk to each other - what messages are valid, what order they go in, what each system should do when it receives one. The architecture has several distinct protocols: the sync daemon protocol, the gossip protocol, the schema-version handshake protocol.* (use at first occurrence in any chapter where the technical sense is doing structural work - Ch 9 sync-daemon triage, Ch 13 schema-version handshake)

**This entry is half a Keep-when entry.** Vol 2 uses *protocol* in two distinct senses, and the workshop's main job is to disambiguate them, not to substitute the term globally:

**Sense A - procedural / human:** *my verification protocol* (Ch 13 Anna's filing), *the operational protocol*, *protocol I have*, *standing protocol*. This is Anna's procedural register: the rules-of-conduct she follows as Mission Director. **NEVER substitute these.** They are character voice and procedural artifacts.

**Sense B - technical / network:** *gossip protocol*, *sync daemon protocol*, *schema-version handshake protocol*. **Substitute on first occurrence in audio** to give the listener context.

**Audio replacement (technical sense only):**
- *gossip protocol* → already covered by `gossip-protocol.md` substitution
- *sync daemon protocol* → already covered by `sync-daemon.md` substitution
- *schema-version handshake protocol* → already covered by `schema-migration.md` substitution
- Bare *protocol* (technical sense, when not in a known compound) → leave untouched in v1 (too risky to globally substitute given Sense A overlap; the chapter-lightening pass adds an explicit modifier inline where needed)

**Keep when (Sense A - procedural / human):**
- *my protocol* / *the protocol I have* / *standing protocol* (any first-person possessive) - Anna's procedural register; never touch.
- *protocol* in dialogue or filed log entries when the speaker means *rule of conduct* rather than *network protocol* - character voice.
- *the protocol exists for the case where you most want to skip it* (Ch 6 Anna's interior callback) - load-bearing aphorism; never touch.

**Mistaken for:**
- *Protocol* (diplomatic / etiquette) - closer to Sense A than Sense B. The listener will reach for this association first; the technical sense (Sense B) requires the longer gloss to land.
- *Protocol droid* (Star Wars) - a non-technical reader/listener may anchor here; harmless mishearing.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine two kids who want to trade Pokémon cards have to follow a set of rules: each says what card they want, then each says what card they're offering, then both nod, then both swap. The rules are the protocol. Without them, one kid might hand over a card and the other kid runs off without trading. The protocol is the agreement that makes the trade fair and complete." The Pokémon-trading-rules image is the workshop entry's load-bearing element for Sense B.
