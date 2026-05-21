# Vol 2 Translation Workshop

Plain-language replacements for the technical vocabulary used in *Vol 2 - RV Nansen's maiden voyage*. **Workshop, not glossary.** The entries here exist to support two downstream passes: (a) a print-side surgical-replacement pass on chapter prose, and (b) an audio-side preprocessor pass that disambiguates terms the audiobook listener cannot disambiguate visually.

## Why this exists

Vol 2 is a first-person mission narrative whose story is partly told *through* the architecture Anna is operating. That architecture has technical names - *sync daemon, schema migration, key envelope, gossip protocol, KEK / DEK, Bridge, Anchor, Forsaken,* and so on. Some are load-bearing canon and must stay. Others are incidental and can be replaced inline. Several collide with everyday words (*keys* on a keyboard versus *keys* in a credential pouch; *gossip* the protocol versus *gossip* in the wardroom; *bridge* the Sunfish accelerator versus *bridge* the boat's command station).

**The audiobook listener has it worst.** No capital letters, no italics, no hyphenation cues, no rewind-and-look. Every collision the print reader can disambiguate visually, the listener has to disambiguate from context alone. That is why most workshop entries carry an audio-replacement field.

## Audience priority

1. **Audiobook listener** (highest priority) - drives the audio-replacement field and re-prioritized Tier 1.
2. **Non-technical print reader** - drives the plain-language replacement and the *Mistaken for* field.
3. **Technical print reader** - protected by the *Keep when* rules; their reading experience should not regress.

## Entry format (five fields)

Each workshop entry has up to five short fields:

- **Plain replacement** - the short phrase that substitutes inline. Preserves sentence rhythm. Often two variants for different contexts.
- **Longer gloss** - the fuller phrasing used at first occurrence in a chapter, where the prose has room for one extra clause.
- **Audio replacement** - what the listener should hear, even if the print word stays unchanged. Drives the TTS preprocessor pass on `build/audiobook.py`. Acronyms get explicit expansion rules; collision-prone words get explicit modifiers.
- **Keep when** - the contexts where the original term must stay: load-bearing canon, character voice markers, cadence-critical lines, cross-references to Vol 1.
- **Mistaken for** - the everyday words a non-technical reader/listener is most likely to confuse the term with. Skipped when there is no real collision risk.

Each entry closes with a **Feynman test** line: *Could a 10-year-old picture this?* If the answer is no, the entry's plain-language replacement is wrong and needs another pass.

## Voice template

Plain-language replacements should follow CO's worked examples:

- **KEK / envelope encryption** → *"Our information is encrypted with a data key; that key is then locked by a separate master key, giving your data two layers of protection."*
- **Gossip protocol** → *"A rumor-style way for servers to keep each other up to date. Each one periodically shares what it knows with a few others until everyone has the same picture."*
- **Clock drift** → *"The way real-world clocks gradually run a little fast or a little slow, so over time different machines disagree about the exact time unless we keep them in sync."*

The shared shape: **concrete mechanism in everyday vocabulary, no jargon smuggled back in, an image a child can picture.** A workshop entry that needs another technical term to explain itself has failed; rewrite it.

## Workflow

1. **Inventory** (done) - `_inventory.md` lists ~80 candidate terms with occurrence counts and triage classifications.
2. **Workshop** (in progress) - write a workshop entry per Tier 1/2/3 term using the template above.
3. **Audio preprocessor** (planned) - `_audio_substitutions.yaml` ingested by `build/audiobook.py:normalize_text_for_tts()` to apply the **Audio replacement** rules before TTS. Vol 1 unaffected (no glossary file = no substitutions).
4. **Print lightening pass** (planned) - per-chapter diffs that apply *Plain replacement* and *Longer gloss* where *Keep when* does not fire. Diffs ship per-chapter for scene-by-scene CO accept/reject.

## Tier 1 (audio-collision priority)

Re-sorted from print-confusion priority once the audiobook listener became the priority audience.

| # | Entry | Status | Audio collision |
|---:|---|---|---|
| 1 | [`bridge.md`](bridge.md) | DRAFTED | Submarine command bridge |
| 2 | [`anchor.md`](anchor.md) | DRAFTED | Submarine / pier anchor |
| 3 | [`relay.md`](relay.md) | DRAFTED | Baton relay / passing the baton |
| 4 | [`gossip-protocol.md`](gossip-protocol.md) | DRAFTED | Office / wardroom gossip |
| 5 | [`clock-drift.md`](clock-drift.md) | DRAFTED | Ice-drift / current-drift |
| 6 | [`key-envelope.md`](key-envelope.md) | DRAFTED | KEK = laughter abbreviation; bare letters meaningless on audio |
| 7 | [`forsaken.md`](forsaken.md) | DRAFTED | The adjective (*she felt forsaken*); narrative-arc proper noun |

## Tier 2 (print-confusion priority - less audio-critical)

All 14 entries drafted 2026-05-06.

| Entry | Image | Notes |
|---|---|---|
| [`handshake.md`](handshake.md) | Two kids with a secret password | Strong audio collision (people shaking hands) |
| [`node.md`](node.md) | A knot in a fishing net | Zero everyday anchor; always expand for audio |
| [`quorum.md`](quorum.md) | Three keys turned at once | Folds in two-party / three-party / read-confirmation |
| [`audit-log.md`](audit-log.md) | Glued pages with a breaking seal | Folds in hash-chain / hash-chained / watch log |
| [`data-class.md`](data-class.md) | Cafeteria sorting trays into categories | Folds in instrumentation-data-class / failure-mode flag / field-map |
| [`surface-window.md`](surface-window.md) | A submarine that calls home twice a month | Folds in surface comms |
| [`manifest.md`](manifest.md) | Moving truck with a list on the side | Folds in manifest signature; preserves *crew manifest* everyday sense |
| [`rollback.md`](rollback.md) | Undoing a LEGO rearrangement | Folds in roll forward / checkpoint |
| [`replication.md`](replication.md) | Three blackboards with the same homework | Folds in replicate / replica |
| [`endpoint.md`](endpoint.md) | Friend's house with three doors | Vol 1 cross-reference for *Endpoint Operations* |
| [`protocol.md`](protocol.md) | Pokémon-trading rules | Disambiguates Sense A (procedural / human) vs Sense B (technical / network); never substitutes Sense A |
| [`local-first.md`](local-first.md) | Notebook in your pocket vs chalkboard at school | Book's title concept; KEEP-as-is with longer gloss |
| [`compromise.md`](compromise.md) | Secret copy of the house key | Folds in compromised / supply-chain compromise |
| [`custody.md`](custody.md) | Relay baton with signatures | Flags chain ambiguity (custody chain ≠ consortium key chain ≠ procurement chain) |

## Tier 3 (light / fold-into-others)

All 9 entries drafted 2026-05-07 (pass-log + deviation-plot folded into `mission-log-artifacts.md`).

| Entry | Image | Notes |
|---|---|---|
| [`mission-log-artifacts.md`](mission-log-artifacts.md) | Chef testing three batches with a diary + chart | Folds pass-log + deviation-plot |
| [`consortium-chain.md`](consortium-chain.md) | Principal → teacher → assistant → helper authority chain | Disambiguates from chain-of-custody and procurement-chain |
| [`model-weights.md`](model-weights.md) | A robot's giant file of learned numbers | Anchor model already covered in `anchor.md` substitutions |
| [`crdt.md`](crdt.md) | Two notebooks that auto-merge what each friend wrote | C-R-D-T expands at first audio occurrence |
| [`commit-history.md`](commit-history.md) | Story-edit diary in a notebook | Joel's Ch 1 disclosure context |
| [`control-plane.md`](control-plane.md) | Restaurant kitchen + manager | *plane* renamed *layer* in audio (avoids aircraft mishearing) |
| [`telemetry.md`](telemetry.md) | Fitness watch reporting vital signs | Partial transfer from spaceflight is roughly correct |
| [`timestamp.md`](timestamp.md) | Photo with invisible date stamp | Light entry; ISO 8601 expansion handled by `narratable_text()` |
| [`encrypted.md`](encrypted.md) | Secret language only two friends know | Everyday anchor is correct; KEEP as-is |

## Pilot entries (template-validation set)

All three retro-fitted with the audio-replacement field and Feynman test line.

- [Keys](keys.md) - digital credentials; not house keys or keyboard keys. Image: stamped ID + safe-deposit-box key.
- [Schema migration](schema-migration.md) - rewriting stored records into a new shape. Image: re-copying every paper form in a filing cabinet while the office is still open.
- [Sync daemon](sync-daemon.md) - background helper for boat/shore catch-up. Image: a kid running between two friends' houses with a notebook.

## Inventory

See [`_inventory.md`](_inventory.md) for the full grep-driven term list, occurrence counts, and triage classifications.
