# Encrypted (encryption, decrypt)

**Plain replacement:** *encrypted* (the term is familiar enough; light entry) · *scrambled with a key* (when more clarity is needed) · *locked with a key*

**Longer gloss:** *Data is encrypted when it has been mathematically scrambled in a way that can only be reversed by someone holding the right key. To anyone without the key, encrypted data looks like meaningless noise. The architecture encrypts data both while it's stored (so a stolen device can't be read) and while it's traveling (so anyone listening on the network can't read it).* (use at first occurrence in any chapter where the term is doing structural work - Vol 2 surfaces *encrypted* in security-critical scenes; mostly Ch 1, Ch 14, Ch 15)

**Audio replacement:**
- *encrypted* / *encryption* / *decrypt* - leave alone. The everyday anchor (*encrypted messages*, *the message was encrypted*, *I can't decrypt this handwriting*) is mostly correct, even for non-technical listeners.
- *envelope encryption* / *key envelope* → already covered by `key-envelope.md` substitutions.
- *AES-256-GCM* and similar cipher names - Vol 2 doesn't surface these in body prose; if they appear, the chapter-lightening pass should add a phrase like *the standard encryption used everywhere*.

**Keep when:**
- ALL occurrences. The everyday meaning of *encrypted* is close enough to the technical meaning for non-technical readers.

**Mistaken for:**
- *Encrypted* (in the loose colloquial sense - *his handwriting was encrypted*) - partial transfer; close enough to be helpful.
- *Cipher* / *code* - adjacent technical concepts; readers may conflate. The longer gloss is sufficient if more precision is needed.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine you write a note to a friend in a secret language only the two of you know. Anyone else who reads the note sees gibberish; only your friend can turn it back into English. Encryption is the same idea, except the secret language is a mathematical scramble and the key is the rule for un-scrambling." The secret-language-with-a-friend image is the workshop entry's load-bearing element.
