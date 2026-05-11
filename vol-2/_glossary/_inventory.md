# Vol 2 Translation Workshop — Term Inventory

Generated 2026-05-06 by ripgrep across `vol-2/act-{1,2,3}/`. Each term shows total occurrences across the 18 Vol 2 chapters and a classification that drives whether a workshop entry is needed.

## Classification key

| Code | Meaning |
|---|---|
| **W** | Workshop entry needed — technical jargon a non-technical reader will miss or mistake |
| **W-DRAFTED** | Workshop entry already written (pilot set) |
| **K** | Keep-as-is across the book — proper noun, character/place name, mission designation, or canonical product name. No replacement; no workshop entry. |
| **C** | Context-dependent — the word is technical in some contexts and ordinary English in others. Workshop entry needed but with strong *Keep when* rules. |
| **D** | Drop from scope — appears mostly in non-technical senses; not worth a workshop entry. |

## Triage table (sorted by occurrence count)

| Count | Term | Class | Notes |
|---:|---|:---:|---|
| 293 | Bridge | K | Sunfish accelerator proper name + boat structural term. No replacement. |
| 225 | protocol | C | Mostly procedural ("the protocol I have"); rarely the technical sense. Workshop entry should target the technical-protocol occurrences only. |
| 169 | schema | W | Folded into `schema-migration.md`; consider standalone entry if standalone occurrences are heavy. |
| 166 | relay | W | Sunfish-architecture component + ordinary verb. Workshop needed. |
| 143 | migration | W | Folded into `schema-migration.md`. |
| 125 | Punta Arenas | K | Geographic name. |
| 111 | node | W | Heavy technical; non-technical reader has no anchor for the word. |
| 93 | handshake | W | Technical protocol-handshake; non-technical reader will picture two people shaking hands. Disambiguation field essential. |
| 91 | queue | C | Mix of *sync queue* (technical) and *queue* (line of people / waiting). |
| 85 | audit log | W | Compound technical term; both halves familiar but combined sense is jargon. |
| 84 | rail | C | Author voice metaphor (*class-region rail, mission-as-survival rail*) + ordinary ship rail. The author-voice sense is a structural device; document but generally KEEP. |
| 81 | Nansen | K | Boat name. |
| 81 | drift | C | *Ice-drift, clock-drift, sync-drift* (technical) + ordinary drift. Disambiguation by collocation. |
| 76 | gossip | W | *Gossip protocol* (distributed-systems term); non-technical reader will hear social gossip. Strong collision risk. |
| 57 | surface window | W | Vol-2-specific operational term; non-technical reader has no schema. |
| 45 | timestamp | W | Common-enough word but worth a one-line workshop note. |
| 42 | Anchor | K | Sunfish accelerator proper name + boat anchor. Capitalization disambiguates in prose. |
| 36 | stream | C | *Salinity stream, instrumentation stream* (technical) + ordinary stream. |
| 35 | pre-mission | D | Ordinary compound; not jargon. |
| 35 | manifest | W | *Probe firmware manifest, signed manifest* — technical; non-technical reader hears *cargo manifest*. |
| 34 | rollback | W | Technical; non-technical reader may guess but the precise meaning matters in Ch 13. |
| 32 | Sunfish | K | Project name. |
| 31 | replication | W | Technical; *replicate* is also ordinary English so disambiguation matters. |
| 29 | read-confirmation | W | Vol-2 specific operational term; needs entry. |
| 27 | MERIDIAN | K | Mission designation (RV Nansen). |
| 26 | HELVETICA | K | Rival mission designation (Stefan's platform). |
| 23 | push | C | Mostly ordinary verb (*push past, push against*); some git-sense (*push to consortium*). |
| 22 | schema migration | W-DRAFTED | Pilot complete. |
| 22 | pull | C | Mostly ordinary verb; some git-sense (*pull from consortium*). |
| 21 | pass log | W | Vol-2 operational artifact term. |
| 21 | deviation plot | W | Vol-2 operational artifact term. |
| 18 | daemon | W-DRAFTED | Folded into `sync-daemon.md`. |
| 16 | hash chain | W | Folded into a forthcoming `audit-log.md` or stands alone? Decide at draft time. |
| 16 | checkpoint | W | Technical; ordinary reader's guess is roughly right but exact meaning matters. |
| 15 | telemetry | W | Technical; non-technical reader may know it from spaceflight context — partial transfer. |
| 15 | field-map | W | Vol-2 specific (Ch 13 schema migration). Folded into `schema-migration.md` likely. |
| 14 | skew | C | Mostly *clock-skew* (technical); some ordinary *skew*. |
| 14 | Forsaken | K | Vol 2 canon name (Stefan's platform / capability). Proper noun. |
| 13 | field map | W | Spelling variant of *field-map*. |
| 13 | encrypted | W | Technical adjective; non-technical reader has folk understanding. Light entry. |
| 12 | supply-chain | W | *Supply-chain attack, supply-chain compromise* — technical; non-technical reader hears logistics. |
| 12 | quorum | W | Distributed-systems term; non-technical reader may know parliamentary sense — partial transfer but not exact. |
| 12 | compromised | W | *Compromised relay* — security sense. Non-technical reader's *compromise* = political deal. |
| 11 | sync daemon | W-DRAFTED | Pilot complete. |
| 11 | schema-evolution | W | Adjacent to schema-migration; may fold in. |
| 10 | schema-version | W | Adjacent. |
| 10 | hash-chain | W | Spelling variant of *hash chain*. |
| 10 | failure-mode | W | Engineer term (*failure-mode flag, failure-mode reporting*) — non-technical reader will guess but imprecisely. |
| 9 | compromise | W | See *compromised*. |
| 7 | watch log | W | Vol-2 specific artifact term. |
| 7 | procurement chain | W | Vol-2 specific (Ch 1 Joel disclosure). |
| 7 | custody | W | Security custody (Vol 1 Ch 23 cross-reference). |
| 7 | clock-skew | W | Folds into `skew` entry. |
| 6 | KEK | W | Acronym; non-technical reader has zero anchor. |
| 6 | control plane | W | Distributed-systems term. |
| 5 | transcript | C | *Schema-version handshake transcript* (technical) + ordinary transcript. |
| 5 | sync queue | W | Folds into `sync-daemon.md` likely. |
| 5 | snapshot | C | Technical sense + photo sense. |
| 5 | metric | C | Technical metric + ordinary metric. |
| 4 | third-party | C | Technical (third-party read-confirmation) + ordinary. |
| 4 | model weights | W | ML/AI term; non-technical reader has weak anchor. |
| 4 | instrumentation-data-class | W | Vol-2 specific (Ch 13). Probably folds into `data-class.md`. |
| 4 | endpoint | W | Network-protocol sense; non-technical reader has zero anchor. |
| 4 | data-class | W | Vol-2-significant; classification system. |
| 4 | consortium chain | W | Vol-2 organizational term; folds into a `consortium.md` or `chain.md` entry. |
| 4 | class-region | W | Author-voice structural rail (*class-region rail, Ch 13*). |
| 4 | cache | C | Technical cache + ordinary cache (a cache of supplies). |
| 4 | anchor model | W | ML weights for the Anchor instrument; folds into `anchor-model.md` or `model-weights.md`. |
| 3 | three-party | W | Folds into `quorum.md` or `read-confirmation.md`. |
| 3 | replicate | W | See *replication*. |
| 2 | roll forward | W | Folds into `rollback.md`. |
| 2 | manifest signature | W | Folds into `manifest.md`. |
| 2 | local-first | W | The book's title concept; entry essential despite low Vol-2 count. |
| 2 | DEK | W | Acronym; folds into `key-envelope.md`. |
| 2 | credential | W | Already addressed in `keys.md`; consider standalone entry for the bare word. |
| 2 | CRDT | W | Acronym; non-technical reader has zero anchor. Vol-2 surfaces the concept under the name *conflict-free replicated data type* mostly via Joel/Priya dialogue. |
| 2 | commit history | W | Git term; surfaces in Ch 1 Joel disclosure. |
| 1 | two-party | W | Folds into `quorum.md`. |
| 1 | trace | C | Technical trace + ordinary trace. |
| 1 | surface comms | W | Vol-2 operational term. |
| 1 | keys | W-DRAFTED | Pilot complete (counted under exact-match `keys`; the bare word *key* runs much higher and is already covered). |

## Workshop-entry draft queue (priority order)

Priority is **occurrence count × collision risk × story-significance**, not raw count. A high-count proper noun like *Bridge* needs no entry; a low-count term like *quorum* or *KEK* needs one because the reader has no anchor at all.

### Tier 1 — Highest priority (drives the most reader confusion)
1. ~~`keys.md`~~ — DONE (pilot)
2. ~~`sync-daemon.md`~~ — DONE (pilot)
3. ~~`schema-migration.md`~~ — DONE (pilot)
4. `key-envelope.md` (folds in KEK + DEK + envelope encryption + integrity-key)
5. `relay.md` (Sunfish architecture component; high Vol-2 count)
6. `gossip-protocol.md` (strong collision with social gossip)
7. `quorum.md` (folds in two-party / three-party / read-confirmation)
8. `handshake.md` (strong everyday-meaning collision)
9. `node.md` (zero non-technical anchor)
10. `audit-log.md` (folds in hash-chain / hash chain / watch log)

### Tier 2 — Mid priority
11. `data-class.md` (folds in instrumentation-data-class, failure-mode, field-map)
12. `surface-window.md` (Vol-2 operational; folds in surface comms)
13. `manifest.md` (folds in manifest signature)
14. `rollback.md` (folds in roll forward, checkpoint)
15. `replication.md` (folds in replicate, replica)
16. `endpoint.md`
17. `protocol.md` (with strong Keep-when rules; many occurrences are procedural-protocol, not network-protocol)
18. `local-first.md` (the book's name concept)
19. `compromise.md` (folds in compromised, supply-chain)
20. `custody.md`

### Tier 3 — Light / fold-into-others
21. `pass-log.md` + `deviation-plot.md` (Vol-2 artifacts; may fold into a single `mission-log-artifacts.md`)
22. `consortium-chain.md` (folds in procurement chain)
23. `model-weights.md` (folds in anchor model)
24. `crdt.md`
25. `commit-history.md`
26. `control-plane.md`
27. `telemetry.md`
28. `timestamp.md`
29. `encrypted.md`
30. `forsaken.md` *(reader-orientation entry, even though it's a proper noun — readers need to know what the in-universe term refers to)*

### Out of scope
- `Bridge`, `Anchor`, `Sunfish`, `Nansen`, `Punta Arenas`, `MERIDIAN`, `HELVETICA`, `Forsaken` (proper nouns; *Forsaken* gets a brief reader-orientation note only).
- `pre-mission`, `push`, `pull`, `rail`, `drift`, `stream`, `cache`, `snapshot`, `metric`, `trace`, `transcript`, `third-party`, `skew` — most occurrences are ordinary English; the technical occurrences fold into the entries that surround them (e.g., *clock-skew* → `quorum.md` or its own minor entry).

## Estimated effort

- **Tier 1 (7 remaining entries)**: ~90 min, four-field template each.
- **Tier 2 (10 entries)**: ~90 min.
- **Tier 3 (10 entries)**: ~45 min, mostly short entries that fold into Tier 1/2.

Total workshop drafting: ~3.75 hours of focused work.

After workshop is complete, the **chapter-lightening pass** is per-chapter diff work: roughly 30-60 min per chapter × 18 chapters = 9-18 hours of editorial pass-and-review. Diffs ship as PRs CO can accept or reject scene-by-scene.
