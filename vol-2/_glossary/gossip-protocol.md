# Gossip protocol

**Plain replacement:** *the rumor-style sync* · *the peer-to-peer catch-up* · *the rumor-style protocol*

**Longer gloss:** *A rumor-style way for servers to keep each other up to date. Each one periodically shares what it knows with a few others until everyone has the same picture.* (use at first occurrence in any chapter where the term is doing structural work - Ch 9 sync-daemon triage, Ch 14 leak event, Ch 15 compromised-relay aftermath)

**Audio replacement:**
- *gossip protocol* → *peer-to-peer catch-up protocol* or *rumor-style sync protocol*
- The bare word *gossip* in technical contexts → *peer-to-peer rumor* (audio expansion essential - the listener will hear "gossip" and picture wardroom small-talk before they picture distributed systems)
- When *gossip* appears in non-technical contexts (Anna noting that Maria caught wardroom gossip, etc.) - leave alone; the everyday meaning is intended.

**Keep when:**
- Wanjiru's or Joel's technical dialogue when one engineer is briefing another - engineer voice marker. Audio still expands.
- Cross-references to Vol 1 Ch 14 *Sync Daemon Protocol* or Ch 16 *Persistence Beyond the Node* where *gossip protocol* is the canonical name.
- The audit-log artifact voice in Anna's filed entries - formal procedural register may carry the technical name verbatim.

**Mistaken for:**
- *Office gossip* / *wardroom gossip* - the non-technical reader's first association is social. Strong collision risk; both the print and audio passes need to defuse it at first occurrence.
- *Rumor* (in a derogatory sense - unreliable information) - the technical sense is *information that propagates by hop-by-hop sharing*; reliability is a property of the protocol, not the rumor metaphor.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine kids on a playground passing news around: each kid tells two friends, those friends tell two more, and pretty soon everyone knows the same thing." The playground image is the workshop entry's load-bearing element.
