# Keys

**Plain replacement:** *credential modules* (Ch 1 Wanjiru handoff scene; CO source-edit 2026-05-07) · *credentials* (most other contexts) · *digital credentials* (when the bare word *credential* might read as an HR document)

**Source edit landed in Ch 1 (2026-05-07):** the Wanjiru handoff scene (lines 100, 102, 108, 128) now uses *credential modules* / *credentials* in source prose - *not* "keys." The aggregating noun *credential modules* anchors readers in real enterprise-security imagery (HSM-style sealed hardware modules with custody chain) per CO's research on air-gapped key transfer. The technical-detail enumeration inside that scene (*relay handoff token, Anchor model weights' integrity-keys, Bridge replication credentials*) stays untouched - Wanjiru is an engineer naming her tools.

**Longer gloss:** *Digital credentials - small files that prove who you are and unlock encrypted data. Think of them as a stamped ID card combined with a safe-deposit-box key, but invisible and held inside a computer.* (use at first occurrence in any chapter where keys are operationally active - Ch 9 sync-daemon triage, Ch 13 migration window, Ch 15 compromised-relay aftermath. Ch 1 no longer needs the gloss because the source already uses *credential modules*.)

**Audio replacement:**
- After the 2026-05-07 source edit, Ch 1's Wanjiru handoff no longer needs audio-side substitution - the source already uses *credential modules* and *credentials*, which are plain enough on audio.
- *the keys* (when credentials are meant, in OTHER chapters that still use "keys") → *the digital keys* or *the credential keys* (audio expansion at first occurrence in a scene; subsequent occurrences inside the same scene can stay as *the keys*)
- *hands on the keys* (Ch 1 Hiroshi line 40, also any keyboard-context elsewhere) → leave alone; the keyboard meaning is the intended one and the listener parses it from the word *hands*
- *personal keys / personal cryptographic keys* (Ch 1 Joel disclosure line 72, similar engineer-voice contexts) → leave alone; engineer naming his own tools in disclosure register

**Keep when:**
- Engineer dialogue or interior in OTHER chapters (Wanjiru, Joel, Priya) when speakers say *keys* in technical disclosure register - character voice marker. Audio still expands at first occurrence per the rules above.
- Joel's Ch 1 line 72 *"personal keys, generated against his own root"* - different scene, different concept (personal cryptographic identity, not service credentials); stays as engineer voice marker.
- Embedded technical-detail enumerations like *integrity-keys* (Ch 1 line 100) - engineer naming individual tools inside a procedural list.
- Cross-references to Vol 1 Ch 22 *Key Lifecycle Operations* and Ch 23 *Endpoint, Collaborator, and Custody Operations* - proper-noun titles.

**No longer applies (2026-05-07):**
- ~~Wanjiru's line *Director, I have the keys.*~~ - line replaced with *Director, I have the credentials.* in source.
- ~~Anna's callback *I had already received the keys from Wanjiru*~~ - replaced with *I had already received the credential modules from Wanjiru* in source.
- ~~"three sets of keys" (Ch 1 line 100, 108)~~ - replaced with *three credential modules* in source.

**Mistaken for:**
- *Keyboard keys* - Ch 1 line 40 (*hands on the keys*) is keyboard, not credentials. No replacement needed there; the everyday meaning is intended.
- *House keys / car keys* - non-technical reader's first association. The longer gloss defuses this at first occurrence.
- *Passwords* - distinct concept; passwords are typed by humans, keys are held in storage and presented by software. Don't substitute *password* for *key*.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine a stamped ID card stuck to a special key for a safe-deposit box; you need both to prove who you are AND to open the box. Computers carry these around for you." The stamped-ID-plus-special-key image is the workshop entry's load-bearing element.

**Sunfish security canon:** §1 (Identity Model - crew + platform + service identities; the Ch 1 handoff hands Anna one platform identity + two service identities). See `.pao-inbox/_creative/sunfish-submarine-security-canon.md`.
