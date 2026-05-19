---
type: in-universe-document
document-type: minority opinion appended to a regulatory filing
authors-in-universe: signed by twelve OSS distributed-systems architects, including Wanjiru Kamau, Joel Reyes, Priya Iyer, and nine others; principal drafter Wanjiru Kamau
publication-in-universe: filed as Annex A to the Working Group on Compliance-Friendly Distributed Architectures' Recommendation (the document at `forsaken-position-papers/03-regulatory-filing.md`); published in the European Commission's public consultation register
publication-date-in-universe: February 2027 (post-the Nansen; concurrent with the Working Group recommendation it dissents from)
title-in-universe: "Annex A: Minority Opinion - Why Federated Trust Is Not the Reference Architecture for Compliance-Friendly Distributed Systems"
length: ~730 words
voice-reference: institutional-formal; matches the regulatory filing's register; engages the Working Group's argument on its own terms
purpose: voice reference + epigraph source; protagonist-side balance to the Forsaken library
---

# Annex A: Minority Opinion
## Why Federated Trust Is Not the Reference Architecture for Compliance-Friendly Distributed Systems

Filed concurrently with the Working Group on Compliance-Friendly Distributed Architectures' Recommendation, February 2027

---

## Section 1: Scope of the dissent

We, the undersigned twelve architects representing the open-source local-first distributed-systems community, dissent from the Working Group's recommendation that federated-trust local-first be adopted as the European Commission's reference architecture for regulated distributed systems. We offer this minority opinion in the spirit of the consultation process and with respect for the Working Group's labor.

Our dissent is not about whether federated-trust local-first is **a** viable architecture for some classes of regulated deployments. It is. Our dissent is about whether federated-trust local-first should be **the** reference architecture - the architecture that European regulatory practice is asked to adopt as canonical and to which non-conforming deployments are required to migrate within the proposed five-year transition window. We argue it should not.

## Section 2: The Working Group's central claim, restated

The Working Group's recommendation rests on a single architectural claim: that pure-OSS local-first architectures, as currently constituted, do not provide the contractual party of record that European regulatory proceedings require. The Working Group concludes that cryptographic accountability cannot substitute for contractual accountability in regulated deployments.

We agree that the substitution is not currently accepted by all European regulators. We disagree that it cannot be made acceptable. We disagree more strongly that the recommended remedy - adopt federated-trust as canonical and require migration - is the only available path.

## Section 3: Why federated-trust as canonical is the wrong direction

Three architectural concerns, each independent and each sufficient to prevent the recommendation:

**3.1 The reference architecture is recommending a single point of institutional failure.** A federated-identity provider, however regulated, however well-governed, however jurisdictionally insulated, is a centralized component. The European Commission has spent fifteen years building regulatory infrastructure to reduce dependence on single points of institutional failure in cloud computing (Schrems II; the DMA; the CRA; the Data Act). Recommending a single trusted identity provider as the canonical trust layer for all regulated distributed systems reverses that direction. We submit this is not what the regulatory framework intended.

**3.2 The recommendation entrenches a commercial monopoly position.** The Working Group's text references one specific firm by name as a fully-conforming implementation; the firm's principal investors are in the Working Group's signatory list. We do not allege impropriety. We observe that the recommendation, if adopted, will hand a substantial market position to a small number of firms whose interests are aligned with the recommendation. The recommendation should not be adopted without explicit consideration of this structural conflict.

**3.3 The architectural concern about cryptographic accountability is solvable through governance evolution, not architecture replacement.** OSS local-first projects have begun developing governance mechanisms - defined parties of record, vulnerability-disclosure SLAs, audit-chain attestation processes - specifically to address the regulatory accountability gap. These mechanisms are not yet universally adopted across the OSS local-first community. They are advancing rapidly. The five-year transition window the Working Group proposes is the same window during which OSS governance evolution will produce the regulatory-acceptable accountability mechanisms the Working Group asserts cannot exist. We ask the Working Group to reconsider the timing.

## Section 4: Recommended alternative

We propose the European Commission adopt a **dual reference architecture**, recognizing two valid paths:

- Federated-trust local-first, for deployments whose operational constraints require a contractual party of record at deployment time
- Pure-OSS local-first with defined governance mechanisms, for deployments that prefer cryptographic accountability and are willing to participate in (or rely on) OSS-community governance evolution

A dual reference architecture preserves choice for deploying organizations, prevents premature commercial entrenchment, and creates regulatory space for OSS governance evolution to mature. The five-year transition window, if maintained, should apply to both paths - requiring deployments to satisfy *either* architecture's defined accountability requirements rather than requiring migration to one.

## Section 5: Specific procedural request

We request that the Commission's review of the Working Group's recommendation include a public consultation specifically on the dual-reference-architecture alternative, with the OSS distributed-systems community invited to submit governance-mechanism proposals for inclusion in the review.

We thank the Working Group for the opportunity to respond.

---

*Signed by:*
*Wanjiru Kamau (principal drafter; Sunfish OSS security architect)*
*Joel Reyes (Sunfish OSS principal architect; author of* Local-First Nodes in a SaaS World*)*
*Priya Iyer (Sunfish OSS schema-migration co-author)*
*[Nine additional signatories from the OSS distributed-systems community.]*

*Anna Yusupova, Mission Director of the Nansen's maiden voyage on MERIDIAN-7, was invited to sign and declined; her position is that the architectural argument is appropriately the architects' to make. The Working Group has been so informed.*
