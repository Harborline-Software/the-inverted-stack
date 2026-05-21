# Relay (Sunfish managed relay)

**Plain replacement:** *the message-relay server* (first occurrence) · *the relay server* · *the message-passing helper* · *the relay* (in tight prose where the meaning is established)

**Longer gloss:** *A relay is a small helper service that passes messages between devices that can't reach each other directly - for example, when one device is briefly offline and needs to leave its updates somewhere safe until the other device wakes up and can collect them.* (use at first occurrence in any chapter where relays are doing structural work - Ch 1 Wanjiru handoff [the relay handoff token from Helsinki], Ch 9 sync-daemon triage, Ch 14 leak event, Ch 15 *Compromised Relay Holds*)

**Audio replacement:**
- *relay* (technical sense, first occurrence in scene) → *the message-relay server* or *the relay server*
- *relay layer* → *the message-relay layer*
- *relay queue* → *the message-relay's waiting list* or *the relay's waiting list*
- *relay handoff token* → *the relay-server handoff key*
- *the compromised relay* (Ch 15) → *the compromised message-relay server*
- *the relay holds* → *the message-relay holds* or *the relay server holds* - the listener needs the modifier here because the chapter title (*Compromised Relay Holds*) is itself an audio collision risk (sounds like *relay holds*, the verb phrase, rather than *relay holds*, a server holding firm under attack)

**Keep when:**
- Engineer dialogue (Wanjiru especially - relays are her domain) - engineer voice marker; she would say *the relay*, not *the message-relay server*. Audio still expands at first occurrence per the rules above.
- Anna's filed log entries where formal procedural language carries the technical noun.
- Cross-references to Vol 1 Ch 14 *Sync Daemon Protocol* and Ch 16 *Persistence Beyond the Node* where *relay* is the canonical name.
- Ch 15 chapter title (*Compromised Relay Holds*) - title is canonical; chapter-internal references can be replaced after the title sets the term. Audio narrator should pace the title carefully so the listener registers *Relay* as a noun and *Holds* as a verb.

**Mistaken for:**
- *Baton relay* / *passing the baton* - the dominant collision; non-technical reader/listener will picture a track race. The longer gloss reframes immediately.
- *Electrical relay* (the switching component in circuits) - distinct technical sense; engineers may conflate. Sunfish relay is a software service, not a hardware switch.
- *Press relay* / *the news relayed* (the verb sense) - close in meaning but distinct usage; the technical noun is a piece of infrastructure, not an act of passing along.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine two friends who can't see each other directly because one is in math class and the other is in art class. They give a kid in the middle their notes; that kid hangs onto each one until the other friend comes by, then hands it over. The relay is the kid in the middle." The kid-in-the-middle-with-notes image is the workshop entry's load-bearing element.
