# Replication (replicate, replica)

**Plain replacement:** *copying* · *duplicate-copying* · *the copying process* (when the noun is needed) · *replication* (the term is plain enough once defined)

**Longer gloss:** *Replication is the process of keeping copies of the same data in more than one place so that a failure in any single place doesn't lose the data. The architecture replicates important records across multiple nodes — multiple devices — and the copies are kept in step with each other as changes happen.* (use at first occurrence in any chapter where the term is doing structural work — Ch 1 Wanjiru handoff [Bridge replication credentials], Ch 6 first surface [sync-replication-to-Bridge], Ch 9 sync-daemon triage)

**Audio replacement:**
- *replication* → *copying* in most contexts (audio: the technical noun has weak everyday anchor; *copying* is the listener's mental model already)
- *replicate* (verb) → *copy* or *duplicate-copy*
- *replica* (noun) → *the copy* or *the duplicate*
- *Bridge replication credentials* → already covered by YAML substitution (*cloud-side replication credentials*)
- *replication-to-Bridge* / *sync-replication* → already covered by YAML substitution

**Keep when:**
- Engineer dialogue when *replication* is the canonical technical noun.
- Cross-references to Vol 1 Ch 14 *Sync Daemon Protocol* and Ch 16 *Persistence Beyond the Node*.

**Mistaken for:**
- *Replica* (a duplicate object, e.g., a museum replica) — close enough to the right meaning; partial transfer is helpful.
- *Reproduction* (biological / asexual reproduction) — wrong domain entirely; the listener should not reach for this association.
- *Backup* — distinct concept; replicas are *live* copies kept in step with the original; backups are *frozen* copies preserved as archives. Don't conflate.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "imagine a teacher writes the day's homework on three different classroom blackboards instead of just one, and any time the teacher updates the homework on one board, all three boards get updated. If one of the boards gets erased by accident, the homework is still on the other two." The three-blackboards-with-the-same-homework image is the workshop entry's load-bearing element.
