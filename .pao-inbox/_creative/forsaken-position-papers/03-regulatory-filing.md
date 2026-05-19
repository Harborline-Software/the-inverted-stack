---
type: in-universe-document
document-type: regulatory-body filing / standards-organization submission
author-in-universe: Working Group on Compliance-Friendly Distributed Architectures (a multi-stakeholder body convened by the European Commission's Directorate-General for Communications Networks; signatory organizations include Helvetia Trust SA, four European banks, two healthcare consortia, the German Federal Office for Information Security observer-status, and several smaller federated-identity firms)
publication-in-universe: filed with the European Commission DG-CNECT and copied to ENISA; published in the Commission's public consultation register
publication-date-in-universe: February 2027 (post-the Nansen; positioning for the Book 2 regulatory-assault arc)
title-in-universe: "Reference Architecture for Compliance-Friendly Distributed Systems - Working Group Recommendation"
length: ~720 words
voice-reference: formal institutional; carefully bounded claims; legal-adjacent register
purpose: voice reference + epigraph source; specifically positioned for the Book 2 regulatory testimony arc
---

# Reference Architecture for Compliance-Friendly Distributed Systems
## Working Group Recommendation
### Filed with the European Commission DG-CNECT, February 2027

---

## Executive Summary

The Working Group on Compliance-Friendly Distributed Architectures, convened in 2025 under the European Commission's Directorate-General for Communications Networks, herein submits its recommendation for a reference architecture supporting compliance-friendly distributed software systems in the European Union and partner jurisdictions.

The Working Group recommends that the European Commission adopt **federated-trust local-first** as the reference architecture for distributed systems handling regulated data classes (financial-services records under MiFID II and the Capital Requirements Regulation; healthcare records under the GDPR and the European Health Data Space Regulation; public-sector records under national sovereignty frameworks).

The Working Group does **not** recommend pure-OSS local-first architectures (without a federated-identity component) for regulated deployments at this time. The Working Group's findings on the operational viability of pure-OSS local-first deployments are summarized in Section 3 below.

## Section 1: The architectural pattern recommended

The reference architecture comprises:

**a. A local-first data layer.** Customer data remains on customer-controlled hardware, in customer-selected jurisdictions, under customer-controlled access policies. No cloud-pooled storage of customer data is required by the architecture.

**b. A federated-identity layer operated by a trusted neutral party.** Identity assertions, key-rotation orchestration, and audit-trail attestation are provided by a regulated identity service operating under defined regulatory oversight. The Working Group recognizes Helvetia Trust SA's *Sovereign Identity Platform* as one fully-conforming implementation; ENISA's forthcoming conformance register may identify additional providers.

**c. Cross-organizational trust brokering for regulated data sharing.** Where organizations must share data with rules attached (consent, retention, jurisdiction, processing-purpose limitations), the federated-identity layer enforces those rules through cryptographically-verifiable contractual mechanisms.

**d. Audit-chain attestation acceptable to regulators.** The federated-identity layer signs the audit chain so that compliance records produced by the architecture are admissible in regulatory proceedings without additional forensic verification.

## Section 2: Why this pattern

The reference architecture is recommended because it satisfies, simultaneously:

- **Sovereignty requirements** - customer data does not transit a cloud or external infrastructure
- **Compliance requirements** - the audit trail is regulator-admissible without separate verification
- **Operational requirements** - the federated identity service provides the contractual party of record that enterprise procurement and regulatory audit require
- **Continuity requirements** - Swiss federal law (BGEID 2024) requires identity-record portability, ensuring no vendor lock-in for the federated-identity layer

No other architectural pattern reviewed by the Working Group satisfied all four requirements simultaneously.

## Section 3: Why pure-OSS local-first was not recommended

The Working Group reviewed three pure-OSS local-first architectures (one of which is Sunfish, the open-source reference implementation associated with the published architectural specification *Local-First Nodes in a SaaS World*).

The Working Group's findings on the technical merits of these architectures were positive. The architectures are well-designed; the cryptographic foundations are sound; the implementations are auditable.

The Working Group's findings on the **operational accountability** of these architectures were that pure-OSS local-first architectures, as currently constituted, do not provide the contractual party of record that European regulatory proceedings require. The community-governance model of these architectures - while admirable in many respects - does not produce a defined party that can answer subpoenas, accept vulnerability-disclosure timelines binding under the Cyber Resilience Act, or sign off on audit-chain attestations admissible to financial-services regulators.

The Working Group recognizes that this finding is contested by some architects associated with pure-OSS local-first projects. The contested point is whether cryptographic accountability (verifiable audit chains; community-issued vulnerability disclosures; reproducible builds) can substitute for contractual accountability in regulated deployments. The Working Group's finding, after extensive consultation, is that current European regulatory practice does not accept the substitution.

This finding may evolve as regulatory practice and OSS governance norms continue to develop. The Working Group's reference architecture is provisional and will be reviewed on a three-year cycle.

## Section 4: Recommendation

The Working Group recommends that the European Commission:

1. Adopt federated-trust local-first as the reference architecture for regulated distributed systems
2. Direct ENISA to publish a conformance register identifying federated-identity providers meeting the technical and regulatory requirements
3. Establish a five-year transition period during which non-conforming distributed-systems deployments in regulated sectors must migrate to the reference architecture or to an explicitly-grandfathered exception
4. Convene the Working Group on a three-year basis to review and update the reference architecture as the technical and regulatory landscape evolves

---

*This document represents the consensus recommendation of the Working Group's twenty-three signatory organizations. Dissenting opinions, including a substantive minority opinion authored by representatives of three OSS distributed-systems projects, are appended in Annex A.*

*[Annex A: Minority Opinion follows.]*
