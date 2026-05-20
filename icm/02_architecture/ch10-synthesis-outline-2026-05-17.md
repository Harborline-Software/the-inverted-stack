---
type: outline
chapter: ch10-synthesis
stage: icm/outline
last-pr: 8
authored-by: yeoman
date: 2026-05-17
---

# Ch10 - Synthesis: What the Council Finally Agreed On
## Outline Draft - PAO Review Required Before Stage 2

---

## The One Claim Ch10 Must Land

> **The five lenses converge on a single architecture because each lens was asking the same question: where does authority live?**

Each council member arrived with a different vocabulary, a different failure mode, and different blocking criteria. But every block and every condition reduces to the same structural concern. Voss asked: who has authority to revoke a node's access? Shevchenko asked: which node has authority to write a CP-class record when the lease is contested? Okonkwo asked: who has authority to know a KEK was compromised, and when? Kelsey asked: who has authority to decide the first customer and the first trigger? Ferreira asked: who has authority to extract their own data from the system, independent of the vendor?

The answer the council ratified - individually and in aggregate - is the same: the architecture places authority at the edge, encodes it cryptographically, and makes it auditable. The relay has no authority over data. The vendor has no authority over keys. The user has authority, bound by role attestation and recoverable through explicit procedure.

The convergence is not a coincidence. It is structural. Part III follows from it.

---

## What Ch10 Does NOT Do

- Does not re-introduce any council member by name or re-establish their credentials.
- Does not re-prove individual lens claims (each chapter already proved them; Ch10 synthesizes).
- Does not preview Part III chapters by number or name ("In Chapter 11, you will see...").
- Does not re-run the Round 1 / Round 2 structure - Ch10 is not a sixth council chapter.
- Does not summarize the five lens chapters (the table in the existing stub does that; Ch10 goes further).

---

## Structural Shape

**Total target: ~2,500 words** (confirmed against book-structure.md)

| Section | Shape | ~Words |
|---|---|---|
| Opening frame | Inverted structure note - Ch10 does not follow R1/R2 pattern | 150 |
| Lens recap × 5 | One short section per lens: single through-line claim | 300 × 5 = 1,500 |
| Convergence section | Where all five claims meet; the authority-residency frame | 650 |
| Pivot paragraph | Bridge into Part III - from evaluation to specification | 200 |
| **Total** | | **~2,500** |

---

## Inverted Structure Note (opening frame, ~150 words)

Ch10 opens by naming what it is not. The five chapters before it followed a two-act structure: a council member identified a failure, the revision addressed it, the verdict followed. Ch10 does not follow that structure. There is no failure to identify, no revision to document. The review is over. What remains is the question of what the review found - not chapter by chapter, but as a whole.

This is a synthesis, not a summary. A summary reports what happened. A synthesis identifies the pattern that connects what happened.

---

## Five Lens Recap Sections (~300 words each)

Each section names the through-line claim each lens landed - not re-argued, just named and located in the architecture.

### Ch05 - The Enterprise Lens (Voss)
**Through-line claim:** Authority over a node's network access belongs to the MDM platform, not the vendor. The architecture earns procurement approval by placing the compliance check at capability negotiation - before data crosses - and specifying the incident response procedure that demonstrates the authority chain when something goes wrong.

Structural placement: MDM compliance check at capability negotiation (not post-auth). SBOM as authority over supply chain provenance. Incident response runbook as authority over the response chain.

### Ch06 - The Distributed Systems Lens (Shevchenko)
**Through-line claim:** Authority over writes to CP-class records belongs to the lease-holder, and the architecture must prove - not assume - that a split-write window cannot produce incorrect results that survive merge. The three-tier GC policy and Flease split-write proof establish the authority boundaries that make the distributed model correct, not merely plausible.

Structural placement: Flease for CP-class records; CRDT merge for AP-class. The split-write proof is the authority declaration. The three-tier GC policy is the authority over what history must be preserved to maintain correctness.

### Ch07 - The Security Lens (Okonkwo)
**Through-line claim:** Authority over encrypted data resides in the key hierarchy, and the architecture must specify what happens when that hierarchy is violated - not just what it looks like in normal operation. The key compromise response procedure is the difference between a security architecture and a security story.

Structural placement: DEK/KEK envelope hierarchy with explicit authority chain from root org key to per-record ciphertext. Compromise response procedure as the authority recovery mechanism. Send-tier data minimization as the authority enforcement point for who receives what.

### Ch08 - The Product & Economic Lens (Kelsey)
**Through-line claim:** Authority over the first transaction belongs to a named customer with a named pain, not to a demographic. The architecture did not become commercially viable when it added a relay pricing model - it became viable when it identified a specific failure mode in a specific industry and built the conversion trigger around that failure.

Structural placement: Construction PM vertical as the first authority over commercial validation. Relay subscription as the authority transfer point from open-source artifact to funded project. The conversion trigger (NAT traversal failure at the relay) as the specific moment authority over the purchase decision activates.

### Ch09 - The Local-First Practitioner Lens (Ferreira)
**Through-line claim:** Authority over user data cannot be asserted architecturally if it cannot be exercised practically. The data portability path - one command producing JSON, CSV, and Markdown from the local node, with no vendor cooperation required - is the only honest implementation of the ownership claim.

Structural placement: Export command as the authority exercise mechanism. Non-technical disaster recovery walkthrough as the proof that authority is recoverable, not just theoretical. Community governance model as the authority transfer structure for the project itself.

---

## Convergence Section (~650 words)

**Title candidate:** "The Question Each Lens Was Asking"

This section does not list the five lenses again. It identifies the pattern.

Each of the five reviewers arrived with a different vocabulary and a different failure mode as their primary concern. Voss cared about procurement. Shevchenko cared about correctness. Okonkwo cared about key compromise. Kelsey cared about commercial survival. Ferreira cared about user custody. The vocabulary is different in every case. The underlying question is the same in every case: **where does authority live, and who enforces it when it is contested?**

The architecture's answer - developed through two rounds of adversarial review - is consistent across all five domains:

1. **Authority lives at the edge.** The node holds the data. The node holds the keys (wrapped, role-scoped, but node-resident). The node enforces capability negotiation. The relay is a forwarder of ciphertext; it holds no authority over plaintext or keys.

2. **Authority is encoded cryptographically, not contractually.** The vendor cannot assert authority over a node's data because the vendor does not hold the decryption keys. The authority enforcement is structural, not legal. A contract can be broken or voided. The key hierarchy cannot be unilaterally revised by the vendor.

3. **Authority is recoverable through explicit procedure.** Voss's incident response runbook. Okonkwo's key compromise re-keying procedure. Ferreira's export path. Shevchenko's stale peer recovery protocol. In every domain, the authority claim requires a specified recovery path. An authority that cannot be recovered when it is violated is not an authority - it is an assumption.

4. **Authority is auditable.** The CRDT operation log is append-only and tamper-evident. The MDM compliance attestation is presented and verified at capability negotiation. The role attestation chain is signed and verifiable at the boundary. The relay metadata is minimized but logged. Every authority assertion leaves a verifiable trace.

The non-negotiable properties the council collectively endorsed are expressions of these four principles:
- Data minimization at the protocol layer (authority over what crosses the relay).
- Subscription filtering at the send tier, not the receive tier (authority over who gets what before it leaves the node).
- MDM compliance check at capability negotiation, not post-auth (authority over who joins the mesh).
- Three-tier CRDT resolution model (authority over which conflict-resolution regime applies to which record class).
- Key compromise response procedure (authority recovery when the cryptographic authority chain is violated).
- Dual-license from day one (authority over the commercial sustainability of the project itself).

The open questions the council did not fully resolve are also expressions of these principles - they are places where authority has not yet been fully specified:
- Relay commoditization moat: if relay authority (the only commercial authority the architecture retains) can be replicated trivially, the project's commercial authority evaporates.
- GDPR Article 17 in CRDT systems: who has authority over deletion when the data structure is designed not to delete?
- Long-term archival format stability: does the user's authority over their data extend to formats that will be readable in twenty years?

These are not failures of the architecture. They are the honest residual of a thorough review. The architecture that emerged from the council is better than the architecture that entered it. The open questions are the ones the council was honest enough not to paper over.

---

## Pivot Paragraph into Part III (~200 words)

**Framing goal:** Part III is not more evaluation. It is the specification that emerges from what the council agreed on.

The pivot does not name Part III chapters by number. It names the architectural shape that the council's agreement demands: a reference architecture that places authority at the edge, encodes it cryptographically, makes it recoverable through explicit procedure, and leaves an auditable trace at every authority assertion. Part III specifies how that architecture is built - the node, the CRDT engine, the schema migration infrastructure, the sync daemon protocol, the security architecture, and the persistence layer beyond the node. Each chapter in Part III answers a question the council forced into specificity. The council finished its work. The specification begins.

---

## Template Adaptation Note

Ch10 uses `chapter-council.md` as its base template but inverts the two-act structure:

- Other Part II chapters: council member introduction → Round 1 failure → what changed → Round 2 verdict → takeaway.
- Ch10: inverted structure declaration (no R1/R2) → five lens recap sections → convergence → Part III pivot.

The section headers in Ch10 do not follow the Round 1 / What Changed / Round 2 pattern. They follow the recap → convergence → pivot pattern specified above. The council voice (specific, evidential, no hedging) applies throughout.

---

## PAO Review Questions

1. **Authority frame:** PAO directive named "where does authority live?" as the convergence claim. Yeoman finds this confirmed by all five lens chapters - every block reduces to an authority question. No adjustment needed unless PAO wants to sharpen the language before Stage 2.

2. **Word count:** Book-structure.md targets ~2,500 words for Ch10. The outline allocates 2,500 across five sections. The draft will likely run 100–200 words over on the convergence section; Yeoman will tighten at Stage 2.

3. **Inverted structure:** The existing Ch10 stub (already in `vol-1/`) opens with a scorecard table and runs through Round 1 / Round 2 structure. The outline above replaces that structure. PAO should confirm before Stage 2 proceeds whether the stub is superseded entirely or whether the scorecard table (which captures the R1 verdicts cleanly) should be retained as an artifact within the new structure.
