# Sync daemon

**Plain replacement:** *the background sync helper* (most contexts) · *the catch-up program* (when *background* would over-explain) · *the catch-up helper* (in tight prose)

**Longer gloss:** *A background helper program that quietly keeps two copies of the same data in agreement - one copy on the boat, one copy on shore - by sending only the changes back and forth whenever a connection is available.* (use at first occurrence in any chapter where the term is doing structural work - Ch 9 *Sync Daemon Under Drift*, Ch 14 leak event, Ch 15 compromised-relay aftermath)

**Audio replacement:**
- *sync daemon* → *background sync helper* (audio always expands; the listener has zero anchor for *daemon* in its technical sense and the bare word evokes mythology)
- *daemon* alone (technical sense) → *background program* or *background helper*
- *the sync* (technical noun) → *the catch-up* or *the sync-up*
- *sync queue* → *catch-up queue* or *waiting list of changes*
- *sync window* → *catch-up window*
- *sync* as ordinary verb (*they sync up at the bench*) - leave alone; everyday usage is intended

**Keep when:**
- Ch 9 chapter title (*Subsystem Test - Sync Daemon Under Drift*) - title is canonical; chapter-internal references can be replaced after the title sets the term.
- Wanjiru's interior or dialogue - engineer voice marker; she names her tools. Audio still expands per the rules above.
- Cross-references to Vol 1 Ch 14 *Sync Daemon Protocol* - keep the proper name in print; expand for audio.
- Anna's filed log entries where the formal procedural register requires the technical noun.

**Mistaken for:**
- *Daemon* (mythological / sinister) - non-technical readers and listeners both flinch at the word. Audio expansion eliminates the problem entirely; print's longer gloss defuses at first occurrence.
- *Sync* as in *happen at the same instant* - actual meaning is *eventually bring two copies into agreement*. Avoid phrasings that suggest real-time mirroring.
- *Backup program* - not a backup; a sync maintains two live copies, not an archive. Don't substitute *backup* for *sync*.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine a helpful kid who runs back and forth between two friends' houses with a notebook, telling each one what the other has written, so both notebooks end up matching by the end of the day." The helpful-kid-with-a-notebook image is the workshop entry's load-bearing element.
