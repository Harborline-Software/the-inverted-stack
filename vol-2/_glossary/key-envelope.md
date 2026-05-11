# Key envelope (KEK / DEK / envelope encryption)

**Plain replacement:** *the master key and data key* (when both halves are in play) · *the master key* (when only the wrapping key is referenced) · *the data key* (when only the inner key is referenced)

**Longer gloss:** *Our information is encrypted with a data key; that key is then locked by a separate master key, giving your data two layers of protection.* (use at first occurrence in any chapter where keys are operationally active — Ch 1 Wanjiru handoff, Ch 9 sync-daemon triage, Ch 13 migration window, Ch 15 compromised-relay aftermath)

**Audio replacement:**
- *KEK* → *key encryption key* (first occurrence in audio) · *master key* (subsequent)
- *DEK* → *data encryption key* (first occurrence) · *data key* (subsequent)
- *key envelope* / *envelope encryption* → *the two-layer key system* or *the master-key-and-data-key system*
- Never let the listener hear the bare letters *K-E-K* or *D-E-K*; the listener has no anchor for them.

**Keep when:**
- Engineer dialogue between Wanjiru, Joel, or Priya — engineer voice marker; they would say *KEK rotation*, not *master-key rotation*. The audio pass still expands *KEK* even inside dialogue, because the listener can't see the proper-noun framing.
- Cross-references to Vol 1 Ch 15 *Security Architecture* or Ch 22 *Key Lifecycle Operations* — the technical names are the cross-reference targets.
- Anna's filed log entries (refusal-of-record, yes-with-conditions) when the artifact's procedural voice requires the formal term.

**Mistaken for:**
- *KEK* (the laughter abbreviation) — non-technical readers under 40 will hit this. Audio expansion fixes it.
- *Envelope* (the paper kind) — the metaphor is intentional but a non-technical reader may take it literally and look for an actual envelope. The longer gloss pre-empts this.
- *Two-factor authentication* — distinct concept; 2FA is about logging in, envelope encryption is about how stored data is protected. Don't conflate.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "your data has a small lock on it; that small lock has a bigger lock around it; you need both keys to open it." The two-layer image is the workshop entry's load-bearing element.

**Sunfish security canon:** §1 (service identities have scoped key pairs; data-encryption keys are scoped to encryption only, not signing); §3 (service private keys live in tamper-responsive hardware where possible). See `.pao-inbox/_creative/sunfish-submarine-security-canon.md`.
