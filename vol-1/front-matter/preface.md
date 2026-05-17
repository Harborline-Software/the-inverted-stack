# Preface

<!-- icm/prose-review -->
<!-- Target: ~1,300 words -->
<!-- Source: source/local_node_saas_v13.md preface, source/inverted-stack-v5.md §1 -->

This dissertation has one argument. The architecture described in Part III satisfies it. Part IV demonstrates it is implementable. The committee in Part II tested it and approved it under conditions I have since met.

The argument is this: SaaS tenancy is a dependency. Dependencies can be withdrawn. A local-first, self-hosted architecture is the only vendor-independent design that survives that withdrawal at scale — commercially, operationally, and across the regulatory jurisdictions where this problem is not academic.

The gap this work addresses is not a gap in research. The local-first ideals — offline operation, real-time collaboration without a central authority, data portability, user ownership — date to Kleppmann et al.'s 2019 essay [1]. The distributed systems components that make those ideals technically achievable — CRDTs (Conflict-free Replicated Data Types), gossip protocols, envelope encryption, distributed leases — are production-proven in individual systems. The gap is a blueprint. A single resource that specifies how to compose those components into production software: software that survives contact with enterprise IT, adversarial security review, and the commercial reality of building a business on top of it.

In 2022, offline briefly became the condition for entire regions of Western enterprise workers. Adobe, Autodesk, Microsoft, and Figma suspended or restricted service across Russia and the CIS (Commonwealth of Independent States), leaving organizations locked out of their own data on infrastructure they had paid for. Seventeen thousand documented cases: researchers, engineers, and institutions losing access to their own work overnight. That event — documented at continental scale — is the clearest empirical evidence the architectural thesis needs. I watched colleagues lose access to years of work. I kept writing.

## Why I Wrote This

I spent three years designing a local-node architecture. Then I subjected it to the kind of adversarial review that standard academic publishing does not provide. The committee — five domain experts representing enterprise IT, distributed systems research, security, product management, and the local-first community — reviewed the architecture twice. The first round produced two BLOCK verdicts. The architecture failed on CRDT (Conflict-free Replicated Data Type) garbage collection, distributed lease correctness, key compromise incident response, commercial viability, and data portability — simultaneously.

Reading those verdicts was not a comfortable afternoon. The distributed lease protocol I had specified in confidence handled the happy path cleanly and the partition-recovery path not at all — a Flease-family protocol needs a quorum reduction rule under partition, and mine did not have one. The key compromise response had no test of whether a revoked device could still decrypt ciphertext already in transit. The commercial model assumed community adoption as a plan. None of those were cosmetic findings. They required a partial rewrite of Part III, a new chapter on security incident response, and an honest commercial model that did not depend on goodwill as economic substrate.

What emerged from Round 2 was an architecture that cleared all five domain reviews under fifteen documented conditions the epilogue names honestly. Not a perfect architecture — the open questions are genuine — but one that had earned its claims through a process that tried to find the failure modes before the first production deployment did.

The committee told me, in Round 1, that local-first plus self-hosting was a preference, not a contribution. I disagreed. The rewrite was my argument.

This dissertation is the result of that process, written to be the resource I needed when I started.

## Who This Book Is For

**Software architects and senior engineers** building or evaluating local-first systems will find a complete distributed systems specification in Parts III and IV: CRDT engine selection and GC policy, schema migration for mixed-version fleets, sync daemon protocol, security key hierarchy, and the full Sunfish (`github.com/ctwoodwa/Sunfish`) package reference. The technical sections are precise enough to implement from.

**Enterprise evaluators, IT architects, and technical decision-makers** will find a governance-first design in Chapters 5, 7, 15, and 19: named MDM (Mobile Device Management) policies, SBOM (Software Bill of Materials) toolchain specification, compliance framework mappings, and an incident response runbook written to answer procurement questions directly. The regulatory scope is explicitly global — anchored by the EU's Schrems II ruling, India's DPDP (Digital Personal Data Protection) Act 2023, and the UAE's DIFC (Dubai International Financial Centre) DPL (Data Protection Law) 2020, with the full coverage matrix (GCC (Gulf Cooperation Council), APAC (Asia-Pacific), African, and Americas frameworks) in Appendix F. Chapter 19 covers code signing, MDM deployment (Intune, Jamf, SOTI MobiControl, IBM MaaS360, Ivanti), and air-gap operation as first-class requirements, not afterthoughts.

**Open-source contributors, technical founders, and product teams** will find a viable project model in Chapters 8, 10, and 16: relay economics modeled at 10/100/1,000 teams, a first-customer archetype with an acquisition channel, a dual-license strategy, and a governance model that does not rely on "community adoption" as a plan.

## How to Read This Book

Part I convinces. It establishes the failure modes of centralized SaaS — not as abstractions, but as specific, domain-grounded scenarios — and introduces the architecture that addresses them. If you finish Chapter 4 unconvinced that the local-node architecture is worth the implementation complexity for your use case, the selection framework there will tell you why, and Parts III and IV are not for you.

Part II stress-tests. Five domain experts challenged the architecture across two rounds of adversarial review. Each chapter presents one lens, one set of objections, one verdict. You need not agree with every committee member's conclusion. Understand what each raised — because the same objections will come from your own enterprise customers, security auditors, and commercial partners.

Five composite characters — each a faithful stand-in for a domain that had every reason to dismantle this architecture — read the paper twice. The people are invented. The objections are not. What broke, broke for real reasons. What changed, changed because the reasons were good.

Parts III and IV are reference material. Part III specifies the architecture component by component — read it when you are ready to build, or when you need to understand why a design choice was made. Part IV provides the minimal path to a working implementation — read it when you are ready to run something.

## A Note on the Reference Implementation

The software described in this dissertation began on a laptop. It now has a name: Sunfish (`github.com/ctwoodwa/Sunfish`). I built it to validate the argument — not as an illustration, but as a test. If the architecture I was describing could not be implemented, the architecture was wrong.

Sunfish is the open-source ERP product developed alongside this work, built on the Shipyard platform. The patterns here are stack-agnostic. Sunfish is the .NET realization — the Zone A local-first desktop accelerator, built on .NET MAUI (.NET Multi-platform App UI) Blazor Hybrid, and the Zone C comms mesh accelerator, built on .NET Aspire and Blazor Server — but the architectural contracts translate directly to Java, Rust, or Go implementations. This book references Sunfish by package name (`Sunfish.Kernel.Sync`, `Sunfish.Foundation.LocalFirst`) rather than by class API (Application Programming Interface). The package contracts are stable; the method signatures in pre-1.0 software are not. The CRDT engine is pluggable through `ICrdtEngine`; Chapter 12 specifies both the current YDotNet implementation (the .NET CRDT engine port of Yjs ([github.com/yjs/yjs](https://github.com/yjs/yjs)) via Rust FFI (Foreign Function Interface)) and the Loro ([github.com/loro-dev/loro](https://github.com/loro-dev/loro)) aspirational target, and treats the choice as reversible by design.

I am honest about what Sunfish can and cannot do. The open questions are named in the epilogue. The pre-1.0 disclaimer applies. What works, works. What does not, does not yet.

At the end of this book you will have four things you do not have now. One: a production-calibrated specification for an architecture that has been stress-tested across five adversarial reviews and cleared fifteen documented conditions. Two: a credibility framework — named objections, named responses — for defending the architectural choice to enterprise customers, security auditors, and engineering leadership. Three: a commercial model that does not depend on community adoption as economic substrate. Four: a compliance posture that speaks to sovereignty requirements across GDPR (General Data Protection Regulation), Schrems II, UAE DPL, DPDP, POPIA (Protection of Personal Information Act), NDPR (Nigeria Data Protection Regulation), PIPL (Personal Information Protection Law), Japan PIPA (Personal Information Protection Act), and the jurisdictions this book names explicitly.

The reader who finishes Chapter 20 will be able to do something practical that the reader who opens Chapter 1 cannot: build a local-first application that an enterprise procurement committee will buy, that a European data protection authority will clear, that a practitioner in Lagos or Mumbai or Santiago can actually run on the connectivity they have, and that will still serve its users if the vendor disappears.

— Joel Reyes, Seattle, May 2025
