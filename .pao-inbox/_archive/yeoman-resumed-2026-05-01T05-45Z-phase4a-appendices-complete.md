---
type: resumed
chapter: appendices A/B/C/D (Phase 4a Block 1)
last-pr: pao-directive-2026-05-01T05-15Z-phase4a-prune-pass.md
branch: polish/yeoman-phase4a-appendices
---

**Verdict: clean light pass on all four. Total -201 words across four appendices. Lint clean.**

## Per-appendix findings

### Appendix A - Sync daemon wire protocol (3,570 → 3,471, -99 words)

5 cuts:

1. **§A.1 opening** - collapsed three sentences into two (cut "This appendix defines the bytes on the wire" - restated "is the normative wire-protocol specification").
2. **§A.1 message-type narration** - replaced six-sentence overview that duplicated §§A.3–A.5 spec with one sentence: "The protocol defines three handshake messages (HELLO, CAPABILITY_NEG, ACK), two streaming messages (DELTA_STREAM, GOSSIP_PING), and a unified error envelope. §§A.3–A.5 specify each."
3. **§A.4.1 DELTA_STREAM `payload` row** - defect fix, removed duplicated parenthetical "(the .NET CRDT engine port of Yjs ([github.com/yjs/yjs](...), the JavaScript CRDT library) via Rust FFI (Foreign Function Interface))" that appeared twice consecutively. Almost certainly an artifact of an accessibility-expansion pass; not a Phase 4a prune candidate per se but flagged for fix while in the file.
4. **§A.4.1 `op_type` paragraph** - collapsed seven sentences to four; "The CRDT engine applies payload without inspecting op_type" was restated as "the CRDT engine will apply the payload regardless".
5. **§A.4.2 GOSSIP_PING long-absence paragraph** - collapsed five sentences (Prior session state is discarded / CAPABILITY_NEG reacquires / node catches up via DELTA_STREAM replay / "no resume primitive") into two using a colon list.

No `PRUNE-4A-CONSIDERED-AND-KEPT` markers.

### Appendix B - Threat model worksheets (4,330 → 4,300, -30 words)

3 small cuts:

1. **§1 keystore guidance closer** - collapsed two sentences into one ("These keystores have meaningfully different security boundaries - verify your platform's actual properties, not its marketing").
2. **§3 Step 4 cold-boot paragraph** - cut redundant cross-ref ("consult Ch15 §In-Memory Key Handling for the re-authentication interval guidance" - the same section was already referenced earlier in the same paragraph).
3. **§4 closer** - cut "The retention floor above is an audit control. The table above is the incident SLA." - both restated the explicit distinction made in the prose at lines 215–216 (Retention and notification are distinct obligations).

**Scope correction for PAO:** the directive said "shared boilerplate across the 6 worksheets that could collapse into a common prelude with worksheet-specific deltas". Appendix B has **5** sections, not 6, and they are structurally distinct - Asset Inventory (table+definitions), Actor Taxonomy (table+definitions+THREAT-10 example), Construction PM Worked Example, Key Compromise Incident Response (checklist+procedure+breach table), Chain-of-Custody (7-field worksheet). They are not the same shape repeated 5 times; there is no common prelude waiting to be factored out. Each worksheet earns its distinct frame. The boilerplate-collapse hypothesis doesn't apply here. If PAO wants the boilerplate-collapse pass anyway, treat as a separate larger restructuring - not Phase 4a sentence-level work.

No `PRUNE-4A-CONSIDERED-AND-KEPT` markers (the regulatory framework footer block at lines 304–317 was deliberately left untouched - that's reference completeness for practitioner use, accessibility/regional consultant earned material).

### Appendix C - Further reading (3,293 → 3,268, -25 words)

4 small cuts (all sentence-level prose tightening of annotations restating their linked sources):

1. **[10] Raft annotation** - collapsed three sentences into two using semicolons; "Raft gives you the understandable baseline. Flexible Paxos gives you the quorum flexibility..." → "Read this alongside Flexible Paxos [9]: Raft gives the understandable baseline; Flexible Paxos gives the quorum flexibility...".
2. **[16] SQLCipher annotation** - collapsed "The documentation covers key derivation (PBKDF2-HMAC-SHA512, 256,000 iterations by default), page-level encryption, and integrity verification. Read the 'SQLCipher Design' section..." into a single sentence with the parameters in the read-this-section guidance.
3. **[31] Actual Budget annotation** - cut "Its architecture makes the trade-offs explicit." (paragraph-summary closer that the four "No X. No Y. No Z. No W." sentences then deliver - the list stands as the example).
4. **[35] CouchDB annotation** - cut "The architectural choice is different from CRDTs." (already implicit in "predate CRDTs and resolve conflicts through MVCC" the sentence before).

No `PRUNE-4A-CONSIDERED-AND-KEPT` markers. The accessibility-expansion parentheticals on entries [3]–[5] (e.g., "the .NET CRDT engine port of Yjs via Rust FFI", "Foreign Function Interface", "Architecture Decision Record") were left intact - out of scope per the directive ("material the literary board / accessibility consultant asked for").

### Appendix D - Testing the inverted stack (3,667 → 3,620, -47 words)

3 cuts:

1. **§Intro** - cut the four-sentence "Level 1 and Level 2 run on every pull request. Level 3 runs nightly. Level 4 runs weekly or before release. Level 5 runs in staging before each major release." block; replaced with one clause "§4 specifies the CI cadence at each level." The §4 table is the normative spec; the intro narration was duplication.
2. **§Level 1 (Property-based tests)** - cut "This is an authorial recommendation calibrated against production experience." (meta-commentary; the next two sentences ARE the calibration: "FsCheck's default of 100 is insufficient" and "10,000 is where empirical bug-discovery returns flatten").
3. **§4 Infrastructure notes** - cut full duplication of the harness-design guidance ("design against the Appendix A protocol specification before implementation begins. A harness built on an incomplete understanding of the handshake simulates the wrong system") that was already in the §Level 4 description.

No `PRUNE-4A-CONSIDERED-AND-KEPT` markers. The Section 3 scenario tables were not touched - they're normative test specifications and every row earns its place as a mandatory pre-release gate.

## Aggregate verdict

Volume per the directive's expectation: light. Two bigger-target appendices (B per directive guidance, A per the embedded state-machine narration) yielded modest cuts; the directive's "boilerplate-collapse" framing for Appendix B did not apply. Appendix D had one duplicated paragraph (clear cut). Appendix C had four sentence-level tighten candidates among 38 annotations.

Lint: 0 errors, only pre-existing Ch16/Ch22 CLAIM warnings. Word count deltas captured per-appendix above.

## Working tree state

- Branch: `polish/yeoman-phase4a-appendices` (from `origin/main`)
- Manuscript edits unstaged (per directive - PAO commits)
- This beacon committed by Yeoman per the 2026-04-29 commit-authority + beacon protocol

## Next

Continuing Phase 4a Block 1 with Ch 4 (per-zone compliance restatement), then Ch 13/14 (spec restatement), then Ch 6/7/8/9 (council Round-2 acks). Will issue separate beacons per branch.
