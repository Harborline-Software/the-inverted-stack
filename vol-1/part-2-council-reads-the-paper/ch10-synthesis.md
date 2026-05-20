# Chapter 10 - Synthesis: What the Council Finally Agreed On

<!-- icm/draft -->

<!-- Target: ~2,500 words -->
<!-- Source: R1, R2 -->

This chapter does not follow the structure of the five that preceded it. Each of those chapters had two acts: a council member identified a failure, the revision addressed it, the verdict followed. That structure served the evaluation. The evaluation is over.

What remains is a different question - not what each reviewer found, but what they all found. Not the five separate verdicts, but the one pattern running through all of them. A summary reports what happened. A synthesis identifies the pattern that connects what happened.

The pattern is this: every block and every condition the council produced, across two rounds and five domains, reduces to the same structural concern. Where does authority live, and who enforces it when it is contested?

---

## The Enterprise Lens - Voss

Dr. Voss arrived representing the procurement officers, the MDM administrators, and the compliance teams that approve what runs on their endpoints. Her domain is not architecture for its own sake. Her domain is architecture that can be defended in a procurement review, where the question is never about elegance and always about demonstrable control.

Her through-line claim: authority over a node's network access belongs to the MDM platform, not the vendor. The architecture earns procurement approval by placing the compliance check at capability negotiation - before data crosses the boundary - and by specifying the incident response procedure that demonstrates the authority chain when something goes wrong.

The MDM compliance check at capability negotiation is not a configuration option. It is the enforcement point. A compromised non-compliant node is rejected before it touches data, not detected after. The SBOM gives the enterprise authority over supply chain provenance - the ability to name every component and its origin before the software is admitted to a managed device fleet. The incident response runbook closes the loop: when the authority chain is tested under a real failure, the runbook specifies who acts, in what order, with what tools.

Enterprise procurement requires exactly this. Not a promise of control, but a specified mechanism for exercising it.

---

## The Distributed Systems Lens - Shevchenko

Prof. Shevchenko held the architecture to a standard that most distributed systems proposals never reach: prove it, do not assume it. A gap in a correctness argument is not a known risk to be managed - it is an unanswered question about whether the system behaves correctly at all.

His through-line claim: authority over writes to CP-class records belongs to the lease-holder, and the architecture must prove - not assume - that a split-write window cannot produce incorrect results that survive merge. The three-tier GC policy and the Flease split-write proof establish the authority boundaries that make the distributed model correct, not merely plausible.

The split-write proof is the authority declaration. Two nodes cannot simultaneously hold write authority for a CP-class record without the architecture specifying what happens when their writes collide. The Flease lease coordination resolves that ambiguity: the lease-holder is the authority, the authority is contested only during a bounded lease-expiry window, and the write semantics during that window are formally specified. The three-tier GC policy is the authority over history: which operation log entries must be preserved to maintain correctness across merge, and which can be discarded when they are no longer needed.

Shevchenko's score dropped in Round 2 not because the architecture weakened but because he took it more seriously. An architecture reviewed as a conceptual proposal gets one set of questions. An architecture reviewed as an implementation guide gets harder ones. The harder questions arrived. The architecture was in a position to answer most of them.

---

## The Security Lens - Okonkwo

Nia Okonkwo's concern was not the key hierarchy in normal operation. Any architecture that handles keys in normal operation can look correct. Her question was the failure case: what happens when the hierarchy is violated, who knows, and what do they do?

Her through-line claim: authority over encrypted data resides in the key hierarchy, and the architecture must specify what happens when that hierarchy is violated - not just what it looks like in normal operation. The key compromise response procedure is the difference between a security architecture and a security story.

The DEK/KEK envelope hierarchy places authority in a verifiable chain: root org key, role key encryption keys, per-node wrapped keys, per-record data encryption keys. Each layer's authority is bounded. A compromised role KEK exposes only the records that key could decrypt - not other roles' records, not forward records after rotation. That scoping is the authority enforcement at rest.

The compromise response procedure is the authority enforcement under failure. Detection, re-keying, notification, audit trail. An architecture that specifies the key hierarchy but not the recovery procedure has specified the normal-operation claim without proving it holds when the authority chain is broken. Okonkwo required the proof. The revision provided it.

---

## The Product and Economic Lens - Kelsey

Jordan Kelsey's block was not about the technology. It was about the claim. An architecture that cannot name who pays first, for what, and how, has not written its business case. The technology proves the architecture is possible. The business case proves the architecture can survive long enough to matter.

His through-line claim: authority over the first transaction belongs to a named customer with a named pain, not to a demographic. The architecture did not become commercially viable when it added a relay pricing model - it became viable when it identified a specific failure mode in a specific industry and built the conversion trigger around that failure.

The construction project manager who needs field sync to work when the cell tower drops is not an archetype. She is the first paying customer, and the architecture works because it solves her specific problem in a way no SaaS relay can. The relay subscription is the authority transfer point from open-source artifact to funded project. The conversion trigger - NAT traversal failure at the relay - is the specific moment when the pain is acute enough to become a transaction.

Commercial authority requires specificity. A general-purpose platform proposition defers the authority question to some future customer who will understand the value. A named vertical closes the question now.

---

## The Local-First Practitioner Lens - Ferreira

Tomás Ferreira's objection was philosophical before it was technical. A paper arguing for data ownership that does not specify how a user exports their data in an application-independent format does not deliver data ownership. It delivers data custody under better conditions. Custody and ownership are not the same word.

His through-line claim: authority over user data cannot be asserted architecturally if it cannot be exercised practically. The data portability path - one command producing JSON, CSV, and Markdown from the local node, with no vendor cooperation required - is the only honest implementation of the ownership claim.

The export command is the authority exercise mechanism. A user who cannot retrieve their data in a form that any other application can read has a theoretical ownership claim with no practical enforcement. The non-technical disaster recovery walkthrough closes the second gap: authority is recoverable, not just theoretical. A non-technical user who loses their device can restore their complete data without calling support. The community governance model specifies the third layer: authority transfer for the project itself, so the architecture does not become vendor-dependent at the governance layer after establishing independence at the data layer.

Ferreira's unconditional PROCEED in Round 2 - from the strictest local-first practitioner on the council - is the single most meaningful verdict in the entire review.

---

> **Round 2 Scorecard**
>
> | Member | Domain | R1 Avg | R2 Avg | Delta | Verdict |
> |--------|--------|--------|--------|-------|---------|
> | Dr. Voss | Enterprise Infrastructure | 7.1 | 7.2 | +0.1 | PROCEED WITH CONDITIONS |
> | Prof. Shevchenko | Distributed Systems | 7.1 | 6.8 | −0.3 | PROCEED WITH CONDITIONS |
> | Nia Okonkwo | Security | 7.3 | 7.0 | −0.3 | PROCEED WITH CONDITIONS |
> | Jordan Kelsey | Product | 5.5 | 6.8 | +1.3 | PROCEED WITH CONDITIONS |
> | Tomás Ferreira | Local-First | 7.0 | 7.6 | +0.6 | PROCEED - NO CONDITIONS |
> | **Overall** | | **6.8** | **7.1** | **+0.3** | **PROCEED WITH CONDITIONS** |

---

## The Question Each Lens Was Asking

The five reviewers arrived with different vocabularies and different failure modes as their primary concern. Voss cared about procurement. Shevchenko cared about correctness. Okonkwo cared about key compromise. Kelsey cared about commercial survival. Ferreira cared about user custody. Five domains. Five sets of blocking criteria. Five distinct definitions of what success required.

The underlying question was the same in every case: where does authority live, and who enforces it when it is contested?

This is not a coincidence. It is structural. The architecture that emerged from two rounds of adversarial review is an architecture because it resolved this question consistently across all five domains. The consistency is the synthesis.

The architecture's answer has four components.

**Authority lives at the edge.** The node holds the data. The node holds the keys - wrapped and role-scoped, but node-resident. The node enforces capability negotiation. The relay is a forwarder of ciphertext. It holds no authority over plaintext or keys. Every council member, from a different starting point, arrived at the conclusion that centralized authority was the failure mode they were protecting against. Voss's MDM compliance check, Shevchenko's lease holder, Okonkwo's key hierarchy, Ferreira's export path - all of them locate authority at the edge, not at the center.

**Authority is encoded cryptographically, not contractually.** The vendor cannot assert authority over a node's data because the vendor does not hold the decryption keys. The enforcement is structural. A contract can be voided. A key hierarchy cannot be unilaterally revised by the vendor after deployment. Okonkwo's DEK/KEK envelope, Ferreira's portable export format, Shevchenko's lease-holder protocol - all encode authority in a structure that cannot be overridden by vendor policy.

**Authority is recoverable through explicit procedure.** Voss's incident response runbook. Okonkwo's key compromise re-keying procedure. Ferreira's export path. Shevchenko's stale peer recovery protocol. In every domain, the council required not just a stated authority but a specified recovery path. An authority that cannot be recovered when it is violated is not an authority - it is an assumption. The procedures are the proofs.

**Authority is auditable.** The CRDT operation log is append-only and tamper-evident. The MDM compliance attestation is presented and verified at capability negotiation. The role attestation chain is signed and verifiable at the boundary. Every authority assertion leaves a verifiable trace. Kelsey's dual-license structure is auditable authority over commercial terms: the user can verify what license applies and what that license permits. Ferreira's export path is auditable authority over data custody: the user can verify what they own by exercising the export.

The six non-negotiable properties the council collectively endorsed are expressions of these four principles. Data minimization at the protocol layer: authority over what crosses the relay. Subscription filtering at the send tier: authority over who receives what before it leaves the node. MDM compliance check at capability negotiation: authority over who joins the mesh. Three-tier CRDT resolution model: authority over which conflict-resolution regime applies to which record class. Key compromise response procedure: authority recovery when the cryptographic chain is violated. Dual-license structure from day one: authority over the commercial sustainability of the project itself.

The open questions the council did not fully resolve are also expressions of these principles. They are the places where authority has not yet been fully specified.

Relay commoditization: if the only commercial authority the architecture retains - the managed relay - can be replicated at infrastructure cost by any cloud provider, the project's commercial authority evaporates. The architecture names the threat. It does not yet fully specify the moat.

GDPR Article 17 in CRDT systems: who holds authority over deletion when the data structure is designed not to delete? Crypto-shredding renders data cryptographically inaccessible. It does not erase it. No data protection authority has issued a binding opinion on whether these are equivalent. The architecture specifies a path; the legal authority to declare it sufficient has not yet been established.

Long-term archival format stability: does user authority over their data extend to formats readable in twenty years? An export today in a format that becomes opaque in a decade is not full data authority. The architecture does not yet address this.

These are not architectural failures. They are the honest residual of a thorough review. An architecture that papers over its open questions is not more complete - it is less honest. The council was rigorous enough to name what it could not resolve. That rigor is part of the result.

---

## The Specification Begins

Part II was a procedure. A proposal was submitted, reviewed, blocked, revised, and cleared under conditions. The five preceding chapters documented that process in the sequence it happened. The reader witnessed the architecture being argued for, defended, and refined against objection. The Flease lease coordination, the send-tier subscription filter, the DEK/KEK rotation policy are not arbitrary choices. They are specific answers to specific blocks.

Part III is not a continuation of that process. It is its output.

The council's PROCEED with fifteen conditions is a green light to build with a specific list of things to get right. Those fifteen conditions are distributed across Part III - addressed where they are architecturally relevant. The stale peer recovery protocol belongs with the GC policy, because the GC policy creates the condition that makes stale peer recovery necessary. The key compromise procedure belongs with the security architecture, because the key hierarchy is the thing it recovers. The plain-file export belongs with persistence, because persistence is where the ownership claim is either honored or abandoned.

The voice shifts here by design. Part II's register is narrative: events happened, reviewers reacted, positions changed. Part III's register is specification: the component does this, the invariant holds for this reason, the failure mode presents as this. A specification that performs uncertainty undermines the thing it is specifying. Part III is written with the confidence of an architecture that has already survived adversarial review. Because it has.

The architecture the council allowed to proceed places authority at the edge, encodes it cryptographically, makes it recoverable through explicit procedure, and leaves an auditable trace at every authority assertion. Part III specifies how that architecture is built - the node, the CRDT engine, the schema migration infrastructure, the sync daemon protocol, the security architecture, and the persistence layer beyond the node. Each chapter in Part III answers a question the council forced into specificity.

The council finished its work. The specification begins.

---

## References

[1] M. Kleppmann, A. Wiggins, P. van Hardenberg, and M. McGranaghan, "Local-first software: You own your data, in spite of the cloud," in *Proc. ACM SIGPLAN Int. Symp. New Ideas, New Paradigms, and Reflections on Programming and Software (Onward! '19)*, Athens, Greece, Oct. 2019, pp. 154–178, doi: 10.1145/3359591.3359737. [Online]. Available: https://www.inkandswitch.com/essay/local-first/
