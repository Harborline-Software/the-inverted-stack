# Sunfish Submarine Security & Key Management — Canon

**Date filed:** 2026-05-07
**Author:** PAO (filing CO directive 2026-05-07)
**Status:** Adopted as security canon for Vol 2 + future volumes
**Authority:** This document is canon for any chapter prose, voice-pass, or chapter-drafter work that touches identity, keys, authentication, panic / zeroization, or distress signaling.

---

## How to use this document

When the chapter-drafter, voice-pass, or any prose-revision agent is working on a scene that touches security, identity, key handoff, panic, or distress signaling, this canon is the **primary reference**. The framework here governs:

- Who has which keys (§1 Identity Model)
- The hierarchy keys descend from (§2 Key Hierarchy and Authorities)
- How keys arrive on the boat and where they live (§3 Generation, Provisioning, Storage)
- What ceremonies are required for high-impact ops (§4 Access Control + Two-Person Rule)
- How the boat operates during partition (§5 Local-First Operation)
- What happens at surface windows (§6 Satellite Sync)
- **Distress signaling and false codes (§7 — narrative-restraint applies; see below)**
- Panic levels (§8)
- Audit and monitoring (§9)

**§7 narrative-restraint advisory:** distress signaling, false codes, and the dedicated distress-only key (§7) are HOT canon for future-volume plot. They are *operationally present* in Vol 2 (the audit log signs distress fields when they fire; Wanjiru would know to look for them) but **must remain narratively un-named in Vol 2 prose**. Surface them only in Vol 3 or later. Reasons: (a) they are load-bearing for a future plot device that deserves to land fresh; (b) Anna's compressed-deliberate register doesn't naturally name covert-protocol details; (c) Wanjiru's forensic recognition (Ch 15) is more powerful when the reader doesn't yet know what she's recognizing.

If a chapter-drafter is tempted to name the distress mechanism explicitly (e.g., "the false-code field in the audit log"), the right move is to imply rather than state — Wanjiru sees something in the log, registers it, and decides her next move; the reader feels the weight without knowing the mechanism. This restraint is not optional.

---

## §1 Identity Model

Three categories of cryptographic identity exist on the boat. They are not interchangeable.

### Crew identities

- Every crew member has a unique cryptographic identity: certificate + key pair, bound to their role (Mission Director, Principal Architect, Lead Instrumentation Engineer, Relay Operations, Medical Officer, Operations Lead, etc.).
- Private keys reside on **controlled hardware** — smartcards, secure elements, hardware tokens.
- A second factor (PIN or passphrase) protects each crew identity.
- Crew identities are bound to the role at issuance; a Mission Director's identity does NOT grant the Lead Instrumentation Engineer's permissions.

### Platform identity (the vessel)

- The submarine has one or more **platform identities** used for:
  - Satellite communications (mutual TLS to shore on surface windows)
  - Sunfish sync to the Bridge service
  - Inter-system authentication between onboard services
- Platform private keys live in **hardened hardware** (HSM or dedicated crypto module).
- Platform keys are NEVER in application configuration files, NEVER in plain text on disk.
- The platform identity is what the consortium-side trusts; impersonating the platform = impersonating the boat.

### Service identities

- Each Sunfish service (sync daemon, audit log, key-management service, telemetry, schedule, etc.) has its **own** key pair + certificate.
- Service certificates chain back to the **platform CA** (per §2).
- Keys are scoped: a signing key signs and only signs; a TLS key authenticates a TLS handshake and only that; a data-encryption key encrypts data at rest and only that.
- A compromised service key compromises only that service, not the platform and not other services.

**In Vol 2 prose:** the three credential modules Wanjiru hands Anna in Ch 1 map to this triad. The relay handoff token from Helsinki = platform identity (for satellite-sync mutual TLS). The Anchor model weights' integrity-keys + the Bridge replication credentials = two service identities, scoped to their respective subsystems.

---

## §2 Key Hierarchy and Authorities

### Root and intermediate CAs

- A **root CA** lives offline on shore. The root CA never travels. The root CA signs intermediate CAs (one or more per fleet or per command).
- Submarines do NOT trust the root directly. They trust intermediate CAs.
- Each intermediate CA covers a fleet or a command — multiple submarines share an intermediate.

### Per-vessel and per-service keys

- Each submarine receives a unique **platform certificate + key pair**, issued by a fleet/command intermediate CA.
- Sunfish services on that submarine receive **service certificates** signed by the platform's certificate (chain: service cert → platform cert → intermediate CA → root CA on shore).
- Crew identities issued to that crew chain back to the same intermediate CA.
- The unified trust root for the boat = the intermediate CA. Everything on board chains there.

### Revocation and validity

- Every certificate has an explicit **lifetime** sized to cover patrol durations with margin.
- Shore systems maintain **revocation lists**; updates are downloaded and applied during satellite sync (§6).
- A revoked crew identity, platform identity, or service identity stops being trusted at the next revocation-list sync; if the boat is currently submerged, revocation lands on the next surface window.

---

## §3 Key Generation, Provisioning, and Storage

### Generation

- Long-term keys (root CA, intermediate CAs, platform identities, core service identities) are generated either:
  - In dedicated **HSMs on shore**, OR
  - Directly in **onboard HSMs** during controlled provisioning events at port.

### Provisioning to the submarine

- Keys + certificates are loaded onto the boat **only while the vessel is in port and under tight physical control**.
- Material is transported as:
  - **Encrypted key bundles on dedicated, sanitized media** (the consortium-issue holders Anna registers in Ch 1), OR
  - **Direct HSM-to-HSM transfers** using vendor key-loading procedures.
- All transfers follow strict **media transfer protocol**: hashing, scanning, inventory checks, custody chain.

### Onboard storage

- Platform and service private keys live in **tamper-responsive hardware** wherever possible.
- Crew private keys live ONLY on personal tokens (smartcards / secure elements). Sunfish uses them via standard interfaces (PKCS#11, smartcard APIs); Sunfish does NOT read raw key material.
- A laptop is never a key store. (Joel's bunk-laptop in Ch 1, Ch 7 holds his *personal* keys generated against his own root, not consortium-chain keys — explicitly outside this hierarchy.)

---

## §4 Access Control and Authentication

### Multi-factor authentication

- High-impact actions require at least two factors:
  - Something the user **has** (smartcard, token, secure element)
  - Something the user **knows** (PIN or passphrase)
- This is the canonical "secondary authentication" the prose can describe in concrete terms when needed.

### Role-based access control (RBAC)

- Permissions are tied to crew roles, not crew names. A Mission Director's identity gets the Mission Director's permissions; a swap of personnel mid-mission re-binds permissions to the new identity, not the old one.
- Permissions are defined centrally on shore but **cached and enforced locally** on the boat to support offline operation (§5).
- Examples:
  - Only Engineering can change critical equipment parameters
  - Only Command can approve route changes
  - Only the Mission Director + Principal Architect together can authorize a high-risk schema migration (§4 TPI; surfaces in Ch 13)

### Two-Person Rule (TPI)

- Critical security operations require **two authorized crew members present, authenticating independently**:
  - Re-keying external comms
  - Panic / zeroization (§8)
  - Applying high-risk configuration changes (e.g., schema migrations on streams that require partition-tolerant rewrites)
  - Issuing new platform certificates
- Keying material containers and crypto-modules are managed under **two-person integrity** wherever practical.

**In Vol 2 prose, TPI ceremonies the reader sees:**

- **Ch 1 Wanjiru handoff** — Wanjiru as key-bearer; Anna as second authenticator signing in the watch log. The signature attestation + hash-chain + replication makes the dual-control durable.
- **Ch 13 schema migration** — Anna files a refusal-of-record then a yes-with-conditions. Joel executes; Anna supervises. *Anna's hands do not touch the keyboard during the migration window.* This IS a TPI ceremony; the conditions she filed are the dual-control protocol.
- **Ch 14 cascade (leak event)** — depending on what panic level is reached (§8), TPI may apply.

---

## §5 Local-First Operation

### Offline-first design

- Sunfish must operate fully offline for extended periods (under-ice operations, weeks).
- All critical policies, role mappings, and key material are **cached onboard at port**.
- Authentication, authorization, and local encryption do **NOT** depend on live connectivity.

### Short-lived tokens from long-lived keys

- Sunfish issues **short-lived tokens** (e.g., JWTs, session tokens) derived from long-lived service and crew credentials.
- Token validation is entirely local — the boat does not need to call shore to know whether a token is valid.
- This is what makes the architecture's "fully itself under the ice" property real: the architecture's verification machinery doesn't degrade when the partition closes.

---

## §6 Satellite Sync and External Communications

### Mutual authentication

- Satellite-sync sessions use **mutual TLS** (or equivalent):
  - The submarine presents its **platform certificate** to shore.
  - Shore presents its **gateway certificate** to the submarine.
  - Both ends validate each other against trusted intermediate CAs provisioned during dockside setup.

### Data types exchanged

**Upstream (submarine → shore):**
- Encrypted telemetry, logs, Sunfish data changes
- Signed audit summaries
- *(Operationally present, narratively un-named in Vol 2: optional distress / false-code indicators per §7)*

**Downstream (shore → submarine):**
- Signed policies
- Signed configuration updates
- Signed revocation lists (per §2)
- Signed software content + data packages

### Integrity and confidentiality

- All data encrypted with modern, approved algorithms + strong key sizes.
- All commands and updates from shore are **signed**; Sunfish applies them only if signatures + versioning checks pass.

**In Vol 2 prose:** Ch 6 first surface and Ch 11 second surface are the canonical satellite-sync scenes. Wanjiru's audit-log validation of the consortium-side counter-signatures (Ch 6 line 17 — *"the audit log accepted the pre-departure-to-Day-20 batch with no reordering and no rejected counter-signatures. Provenance through the partition transition is intact"*) is exactly the integrity property §6 specifies.

---

## §7 Distress Signaling and False Codes — NARRATIVE RESTRAINT

⚠ **§7 is HOT canon for future-volume plot. It is operationally present in Vol 2 but must remain narratively un-named in Vol 2 prose.** ⚠

### What §7 actually is

- **Explicit distress flags:** application-level encrypted fields in Sunfish messages may carry distress status — *under duress*, *compromised*, *restricted communication only*. Visible only to shore systems that can decrypt + interpret Sunfish payloads.
- **Covert false-code signaling:** specific combinations of otherwise-normal fields and message types are interpreted by shore as distress / compromise signals but appear routine to an observer. Fully authenticated; indistinguishable from normal traffic without knowledge of the agreed semantics.
- **Distress-only keys:** a dedicated, limited-scope key signs distress indicators / false codes, allowing shore to distinguish them from ordinary traffic. Access to this key is controlled separately and may require TPI.

### Why it stays implicit in Vol 2

1. **Plot runway protection.** §7 is load-bearing for a future-volume plot device. Naming the mechanism in Vol 2 burns its reveal moment.
2. **Anna's voice.** Compressed-deliberate; Anna names what she touches. She doesn't catalog covert-protocol details unless they're operationally on her bench right now. They aren't, on this mission.
3. **Wanjiru's forensic register lands harder when implicit.** When Wanjiru recognizes something in the audit log in Ch 15, the reader feels the recognition without yet knowing the vocabulary. That weight depends on the reader not having seen the vocabulary in Ch 1.

### What chapter-drafters can do (operationally implicit)

- Wanjiru *can* check the audit log, register that something is consistent / inconsistent, decide her next move — without naming the field.
- The audit log *can* sign and replicate distress-adjacent metadata — without the prose explaining what the metadata is.
- A character *can* feel the weight of a procedure without explaining the procedure.

### What chapter-drafters cannot do in Vol 2

- Name "false-code signaling" or "distress-only keys" by their canonical names.
- Have Anna or any character explicitly explain the dual-meaning protocol to another character.
- Surface the dedicated distress-only key as a separate physical object on the bench.

This restraint applies to all Vol 2 prose, voice-pass, and chapter-drafter work.

---

## §8 Panic, Zeroization, and Compromise Response

### Panic controls

- Sunfish + associated crypto hardware provide **panic mechanisms** that rapidly zeroize selected secrets:
  - External-comms keys + satellite-sync credentials
  - Optional local service keys + data-encryption keys (per doctrine)

### Graduated responses

Panic actions are **layered**:

- **Level 1:** Disable / revoke external communications. Prevents impersonation to shore. The boat keeps operating internally; shore just stops trusting the boat-side until re-provisioning.
- **Level 2:** Restrict local access to minimal safe operation. Most service identities revoked; only safety-critical paths remain.
- **Level 3:** **Full cryptographic wipe.** All keys, all credentials, all encrypted data — gone. This is the irreversible step.

Panic levels are ordered by severity. Higher levels are not skipped *up*; the boat moves through L1 → L2 → L3 only as the situation escalates. TPI applies to Level 2 and Level 3 transitions; Level 1 may be authorized by the Mission Director alone in operational urgency.

### Post-compromise handling

- Shore uses revocation lists + out-of-band procedures to mark platform / crew identities as compromised.
- After recovery, the submarine is **re-provisioned in port from clean images and fresh keys**. Previous secrets are NEVER reused.

**In Vol 2 prose:**
- Ch 14 cascade may approach L1 (disable external comms) under specific failure modes. Whether the chapter-drafter surfaces this explicitly depends on the scene's pacing.
- Ch 15 *Compromised Relay Holds* engages the post-compromise framing. The relay holds despite compromise = an L0 / pre-panic state; the architecture is functioning in degraded mode while the compromise is investigated. Wanjiru's forensic recognition is the trigger that decides whether to escalate.

---

## §9 Monitoring, Logging, and Audit

### Local monitoring

The audit log integrity-protects the following events:
- Authentication attempts (success + failure)
- Privilege escalations
- Key lifecycle events (issuance, rotation, revocation, expiry)
- Panic / distress operations

Logs are reviewed periodically onboard and **summarized for shore** at surface windows.

### Secure log export

During satellite sync, Sunfish exports:
- Encrypted + signed log summaries
- Integrity checksums

Shore-based monitoring systems consume these for cross-boat correlation.

### Regular audits

- Periodic security + compliance audits verify:
  - Key inventories (everything that should exist does; nothing extra exists)
  - Access controls (RBAC mappings are still correct)
  - Log completeness (no gaps in the audit log)
  - Adherence to procedures (TPI was followed where required)

**In Vol 2 prose:** the audit log is a recurring narrative artifact. Wanjiru manages its operational integrity. Anna files into it (Ch 1 watch log signature; Ch 13 refusal-of-record + yes-with-conditions; Ch 6 / Ch 11 surface-window filings). The hash-chain integrity property is what makes Wanjiru's forensic recognition (Ch 15) credible — she can prove what happened, in what order, without ambiguity.

---

## Cross-references

- **Joel-teaching-register canon** (`.pao-inbox/_creative/joel-teaching-register-canon.md`) — Joel can teach §1 (identity model), §2 (key hierarchy), §4 (TPI / MFA) in Ch 7's pilot. The pilot brief is updated to point at this canon for natural pedagogical content.
- **Wanjiru character sheet** (`.pao-inbox/_creative/character-sheets/wanjiru-kamau-security-policy.md`) — Wanjiru is the operational owner of §1 (identity issuance), §2 (revocation list management), §6 (satellite sync), §7 (distress recognition; restraint applies), §8 (panic authority alongside Mission Director), §9 (audit-log review and shore export).
- **Workshop entries** that reference this canon:
  - `keys.md` — §1 (crew + platform + service identities)
  - `key-envelope.md` — §3 (storage), §1 (service identities)
  - `audit-log.md` — §9 (monitoring, logging, audit)
  - `custody.md` — §3 (provisioning + media transfer protocol), §9 (audit)
  - `consortium-chain.md` — §2 (key hierarchy), §6 (mutual authentication)

---

## Sources informing this canon (CO-supplied 2026-05-07)

The canon synthesizes principles from: NIST glossary on two-person integrity, ITU radio regulations on distress communication, vendor / industry guidance on air-gapped deployment + key management best practices, public reference material on root CA hierarchies + revocation. The Sunfish-specific application (submarine deployment, mutual TLS to shore on surface windows, three-tier identity model bound to the boat's intermediate CA) is project canon.
