# Chapter 9 - The Local-First Practitioner Lens

<!-- icm/voice-check -->
<!-- Target: ~3,500 words -->
<!-- Source: R1 Ferreira, R2 Ferreira, v13 §13 -->

---

Tomás Ferreira held the local-first practitioner seat on Joel's dissertation committee — not as a theorist, but as someone who had already lived through the failure modes Joel's architecture was trying to prevent.

## Who Is Tomás Ferreira

Ferreira has shipped code to the Automerge repository for three years. Before that, he built a production local-first application for a small legal firm — document collaboration, no server required — and watched users try to restore data from a broken laptop. The restore took four hours because the backup was a Dropbox folder that had not synced correctly. He sat in the room while it ran. He built a second application with a proper backup strategy, then watched a different user delete their container by accident and learn what "no backup" actually means. That is the kind of discovery that does not leave you.

He is not idealistic about local-first software. He knows where it breaks.

His lens on any local-first architecture proposal is not whether it upholds the principles — those are table stakes. His questions are operational. What happens when the user's only device dies? What happens when both peers are behind carrier-grade NAT and the relay is down? What happens when a user wants to leave and take their data somewhere else? Ferreira has sat across from non-technical users who lived through all three of these scenarios. He knows what their faces look like.

When Ferreira reviewed Joel's dissertation in Round 1, he brought that operational history into the room. He commended the places the dissertation got right. He blocked it on the place it got exactly wrong.

---

## Act 1: Round 1 - The Data Portability Failure

### What Ferreira Commended

Ferreira's Round 1 scorecard opened at 9 out of 10 for CRDT library selection. Yjs for JavaScript environments and Loro for Rust-native performance are both correct choices, well-suited to their respective contexts. The three-tier resolution model — when to apply CRDT merge versus user-arbitrated resolution — is the most honest treatment of CRDT applicability he had encountered in any architecture proposal outside published academic literature.

The multi-device onboarding flow — install, scan a QR code, sync in the background — solved the bootstrapping problem that breaks most naive local-first architectures. The usual failure mode is chicken-and-egg: joining a workspace requires credentials, credentials require an existing peer, and a peer requires the network at exactly the right moment. The QR-based attestation bundle transfers everything the new node needs to authenticate and begin gossip in a single out-of-band step.

He also commended the container cold-start solution. A Podman container starting from scratch on first open creates a pause that signals something is wrong — that the software is not, in fact, running locally, but waiting for something remote. The architecture's answer — a persistent background service that keeps the container running, fronted by a health-check gate that holds the UI until the daemon is ready — hides the implementation detail without deceiving the user. Hiding without lying is craft.

Alignment with the Kleppmann et al. local-first ideals [1] scored an 8 out of 10. The dissertation understood the ideals and implemented most of them faithfully. The Ink and Switch essays on Pushpin and Backchat were not cited, which left it vulnerable to community criticism. Community governance scored a 5 out of 10: an MIT or Apache 2 license is stated, but who controls the roadmap, who approves breaking changes, and what the contribution model looks like — none of it specified. Both were conditions, not blocks.

Then Ferreira got to data portability.

### The Blocking Issue: No Export Path

The paper's thesis is data ownership. The proof is the local node: because data lives on the user's machine in a local encrypted database, the user owns it structurally. The vendor cannot take it away. A SaaS subscription cannot gate access to it.

Ferreira agreed with the thesis and blocked on the execution.

If a user wants to leave the application — switch tools, transfer data to a new platform, or preserve records in a format still readable in twenty years — how do they do it? The paper specified the backup target: rclone with a user-controlled object storage account. But rclone backup preserves the internal data format. It does not export records in a form any other application can read. It gives no JSON file, no CSV of tabular data, no folder of Markdown documents. It gives a copy of the encrypted local database, readable only by the application that created it.

Ferreira named the philosophical contradiction precisely: a paper arguing for data ownership that does not specify how a user exports their data in a durable, application-independent format does not deliver data ownership. It delivers data custody under slightly better conditions. Custody is the lesser word.

He also flagged the non-technical disaster recovery path as a condition. The architecture specified rclone backup to user-controlled object storage — correct — but never walked through what a non-technical user does when their laptop dies and they need to restore. Step one: buy a new laptop. Step two: install the application. Step three: what? The architecture knew the answer but never wrote it down.

The symmetric NAT scenario was a third condition. When two peers are both behind carrier-grade NAT and the relay is unavailable, direct communication is impossible. The paper described mDNS for LAN discovery and relay for WAN — but did not acknowledge that carrier-grade NAT can defeat both if the relay is down. The failure mode exists. The paper did not document it.

### Round 1 Verdict: PROCEED WITH CONDITIONS

Ferreira's domain average was 7.0 out of 10. He issued PROCEED WITH CONDITIONS — three items, with the absent export path as the heaviest.

His rationale was direct: the paper cannot argue for data ownership and omit the export button. Until the architecture specifies how a user retrieves their data in a form that does not require the original application to read it, the ownership claim is hollow. The condition would block alpha implementation if unaddressed before the second review.

The paper returned with Ferreira's data portability issue alongside five others: two from Shevchenko (CRDT GC and Flease split-write), two from Kelsey (no customer archetype and no conversion mechanism), and one from Okonkwo (key compromise response). Shevchenko and Kelsey issued formal BLOCK verdicts. The revision had to address all six before any member would begin a second review.

---

## What Changed Between Rounds

Four months passed between the Round 1 verdict and the Round 2 submission. Joel addressed all six blocking issues.

The export path is now specified. One command produces a directory with three artifacts: a JSON file containing all user records in application-independent structure, CSV files for every tabular data type, and a folder of Markdown documents for long-form content. No vendor cooperation required. No active subscription required. No internet connection needed. Any application that can ingest JSON or CSV can ingest the output.

The non-technical disaster recovery walkthrough now exists step by step. The scenario is a laptop destroyed beyond recovery. Step one: acquire a new laptop. Step two: install the application, which installs the container runtime and stack silently. Step three: enter a recovery code generated during initial setup, or scan a QR code from a team member's device. Step four: enter the BYOC backup target — the Backblaze bucket, the S3 path, the rclone destination configured during original setup. Step five: full restore runs in the background. The user can work immediately on data in eager sync buckets; remaining records populate as background sync completes. No technical knowledge required at any step.

The walkthrough adds a shared-device variant for deployment models common in GCC, Indian BFSI, and African field operations: a single tablet rotated across a team of field workers, where the device belongs to the workspace and recovery targets the role, not any individual identity. Step three authenticates the team's role rather than a personal identity; the device picks up the role's attestation bundle from the relay or a peer device. Step four restores from the role-scoped BYOC backup target. This is what disaster recovery looks like for the deployments that need local-first the most.

The symmetric NAT failure mode is now documented honestly. When both peers are behind carrier-grade NAT and the relay is down, direct peer-to-peer communication is impossible. The paper names the condition rather than papering over it. For organizations where relay availability is itself a concern, self-hosting a relay instance on a cloud VM with a public IP eliminates the symmetric NAT problem by giving both peers a fixed reachable endpoint.

Community governance now has a three-stage model: the author serves as BDFL for version 1, a contributor council of five elected members takes over for version 2, and a foundation structure for version 3 provides independent governance once the community has grown enough to sustain it.

---

## Act 2: Round 2 - An Unconditional Pass

### Seven Ideals Compliance: The Full Checklist

Ferreira opened his Round 2 review by applying the Kleppmann et al. checklist [1] directly. He had done this in Round 1 and found gaps.

**No spinners, no waiting.** The local node holds the authoritative data copy. The UI reads from local storage. No round-trips to a remote server for reads. Holds.

**Your work is not trapped on one device.** CRDT sync across peers ensures data written on one device propagates to all authorized peers. The gossip daemon handles distribution. Confirmed.

**The network is optional.** The architecture is explicitly offline-first. The node operates at full fidelity without network connectivity. Degraded UX modes apply only to CP-class data requiring freshness guarantees. Settled.

**Seamless collaboration with your colleagues.** CRDT merge handles concurrent edits without coordination. The conflict inbox and bulk resolution UX surfaces the edge cases that require human judgment. Checked architecturally — with a practitioner's honesty note: the reference implementation's CRDT backend integration is the open work that will let this check mark move from architectural commitment to field-proven behavior. Ferreira has written enough CRDT code to know the distinction matters.

**The long now.** The compliance CRDT tier with no garbage collection preserves the complete operation history. Records in this tier cannot be lost to compaction. Met.

**Security and privacy by default.** Subscription scoping at the sync daemon layer enforces data minimization at the protocol layer — nodes receive only the data their role authorizes. End-to-end encryption means the relay handles ciphertext only. Checked.

**You retain ultimate ownership and control.** BYOC backup to user-controlled object storage. AGPLv3 license. Self-hostable relay. Plain-file export. The ownership is structural, not contractual, and the export path now makes it operationally real. Checked.

This was the first version of the dissertation where Ferreira could work through the checklist without pausing. All seven ideals satisfied, without reservation. Score: 10 out of 10.

### The Zero-State First-Run Problem

With the blocking issue cleared and the checklist passed, Ferreira turned to what the revision had not addressed.

The UX section substantially improved on Round 1. The sync status indicator design is correct — three persistent but unobtrusive indicators in the status bar, escalating from silent to informative to persistent-banner as conditions degrade. The conflict resolution UX addresses the most common usability failure in collaborative local-first applications: the overwhelming, undifferentiated list of conflicts that most systems surface when two offline nodes reconnect. Grouping by record type and cause, auto-resolving the cases where predefined rules clearly apply, and offering resolve-all-similar for everything else brings the conflict inbox from anxiety-inducing to manageable.

The gap Ferreira identified as the primary 30-day abandonment risk is the zero-state first-run experience: what a brand-new user sees after installation, with no prior data and no existing peers.

The paper describes multi-device pairing and team onboarding. It does not describe what a single user, installing for the first time with no prior data and no colleague nearby, actually sees.

This is where most users leave — not when sync breaks, not when a conflict surfaces, but at the beginning, when the screen is empty and the application has no obvious first action. A brand-new user who opens the application and sees a blank state without guidance for the first thirty seconds is a user who closes it. Not because the architecture failed. Because the first-run experience gave them no foothold. Ferreira has watched this happen with promising local-first software repeatedly.

The paper must specify the zero-state experience: what the user sees, what action they take, how the application walks them from empty state to first project, first backup configuration, first invite. This is a product question, not an architecture question. Local-first architectures that do not answer it fail before the architecture gets a chance to prove itself.

### Backup and Recovery UX

The backup status model in the revised paper is correct. Three states — Protected, Attention, At Risk — with escalating visual treatment: subtle for Protected, amber badge for Attention, persistent non-blocking banner for At Risk. The dismissal with explicit acknowledgment respects user agency without hiding the problem.

The dissertation describes the backup status display. It does not describe the recovery experience with comparable care.

If a user's only device is destroyed and they initiate a restore from backup, what do they see? Does the application walk them through reconnecting to their backup target the same way it walked them through configuring it? Does restore progress surface as a background sync indicator, using the same three-state model flipped into a restore context? Or does the user face a technical interface — a rclone path, a bucket URL — at exactly the moment when they are already stressed about lost work?

The architecture's backup infrastructure is solid. The recovery UX needs the same design attention. *Your backup is protected* earns user trust only if the restore works without calling support.

### Production Analogues and CRDT Selection

The architecture's analogues table cites Figma, Linear, Obsidian, and PowerSync — correct references demonstrating that each subsystem of the inverted stack has production validation somewhere. Ferreira, with Automerge and Ink and Switch adjacency, adds a practitioner's verdict on the CRDT library choice: pick Yjs via YDotNet today. Broadest production adoption, battle-tested merge semantics, documented wire format. Automerge 3.0 (2025) is now production-viable; Loro is the aspirational target once C# bindings mature. Zoho's offline-capable suite — hundreds of thousands of paying users in India and the GCC — is the regional analogue Western surveys miss. 1С:Предприятие is the closest CIS commercial analogue, with tens of millions of users on a desktop-software-with-optional-server model. The `ICrdtEngine` abstraction is the single best architectural decision the dissertation makes: it keeps the engine choice reversible while the field continues to evolve.

One structural accessibility advantage no council chapter had yet named explicitly: assistive technology — screen readers, switch controls, voice input — operates against local data and survives connectivity loss without cascading failures. A user running JAWS, NVDA, or VoiceOver on intermittent connectivity does not experience the application timeouts that cloud-dependent assistive technology produces. Sync status surfaces through ARIA live regions; recovery flows respect the same cognitive-accessibility framing applied to non-technical users. This is the strongest accessibility argument for local-first that any practitioner has put on paper, and it lives here because Ferreira's operational lens — *what the user actually experiences* — is what makes accessibility legible as an architectural property rather than an afterthought.

### Implementation Drift Risk

Ferreira's final observation is the one that will matter most in year two of production: implementation drift.

The Kleppmann et al. paper [1] warns about this directly. Local-first architecture erodes under pressure — one reasonable-sounding decision at a time. A team adds a server-side feature flag check, then a server-side A/B test, then product analytics, then a server-side model for something the local CRDT cannot handle efficiently. Each decision is defensible in isolation. Collectively, they re-centralize the architecture until the local node is a thick client again and the server is load-bearing.

The paper addresses this for business logic — it explicitly prohibits feature gating via server-side checks — but leaves the analytics and observability layer unaddressed.

Modern product teams expect product analytics. In a local-first architecture, those signals cannot be collected server-side because there is no server-side session. The options are: opt-in telemetry that users explicitly enable; aggregate statistics piped through the relay, privacy-preserving and metadata-only; or no analytics at all.

The paper must specify which model it adopts. Leaving it unspecified guarantees that the first product manager who wants a funnel report will add a server-side analytics endpoint — the first stone on the re-centralization path. The reference implementation adopts opt-in telemetry disabled by default, with aggregate-through-relay statistics as the only permitted centralized collection, mapped to GDPR Article 25 privacy-by-design. An ADR documenting the decision makes it defensible under future pressure.

### Round 2 Verdict: PROCEED

Ferreira issued PROCEED in Round 2. No conditions. No blocking issues.

His four observations — the zero-state first-run gap, the recovery UX, the backup UX parity gap, and the telemetry model — carried specific recommendations, not conditions. He filed them as non-blocking guidance, not as gates on implementation.

Practically: the architecture proceeds to alpha implementation without resolving these items. Structurally: Ferreira is the first council member across both rounds to issue an unconditional PROCEED. The enterprise architect issued PROCEED WITH CONDITIONS. The distributed systems researcher issued PROCEED WITH CONDITIONS. The security practitioner issued PROCEED WITH CONDITIONS. The product manager issued PROCEED WITH CONDITIONS. Ferreira, the practitioner who knows where the bodies are buried, looked at the revised architecture and found nothing that blocked it.

That verdict is not a formality. It is the hardest one to earn.

---

## Global Deployment Context

Ferreira's unconditional PROCEED is calibrated against empirical evidence the other council members had to assert. In 2022, Adobe, Autodesk, Microsoft, Figma, and dozens of other Western SaaS vendors suspended service across Russia and CIS markets under sanctions enforcement — hundreds of thousands of organizations lost access with days of notice. An architecture that survives vendor suspension is not a theoretical improvement. It is the architecture that already proved necessary once.

The regulatory envelope extends well past GDPR. The 2020 Schrems II ruling constrains transfers of EU personal data to US cloud providers without adequate supplemental safeguards. India's DPDP Act 2023 and RBI 2018 BFSI localization circular make local-first compliance mandatory for financial data. UAE's DIFC and ADGM data protection rules may legally prohibit foreign cloud storage for free-zone-licensed firms. Saudi Arabia's PDPL 2021, Japan's APPI (2022 revision), South Korea's PIPA, China's PIPL, Brazil's LGPD, and Russia's Federal Law 242-FZ each impose localization or processing constraints that local-first deployments satisfy structurally. The full coverage matrix sits in Appendix F. In each jurisdiction, the architecture where data lives on the user's own hardware is the architecture that makes compliance tractable.

Intermittent connectivity is the operational baseline for hundreds of millions of enterprise workers across Sub-Saharan Africa, South and Southeast Asia, and rural Latin America — not a carrier-grade NAT edge case. CRDT subscription scoping at the sync daemon handles the intermittent-connectivity baseline. Local key management answers the state-mandated compelled-access threat model that CIS deployment contexts face as a first-order consideration. The architecture answers these conditions structurally, not contractually. The practitioner's unconditional PROCEED is easier to issue because the markets where the architecture is most needed are also the markets where alternatives have already failed.

---

## The Non-Negotiable Practitioner Checklist

- **Export path is a first-class shipping requirement, not a future feature.** JSON, CSV, or Markdown — durable, application-independent formats. The export button is the proof that the ownership claim is real.
- **Disaster recovery walkthrough ships with the product.** A non-technical user, after complete device failure, must restore from backup in under thirty minutes. Specify for single-device and shared-device deployments. A backup that cannot be restored is not a backup.
- **Telemetry model is decided before the first product-analytics request.** Opt-in telemetry, aggregate-through-relay privacy-preserving statistics, or no analytics at all. Naming the model prevents implementation drift toward server-side re-centralization.
- **Zero-state first-run experience is specified as a product requirement.** What a new user sees at the blank screen, the first action the application guides them to, the path from empty state to first project, first backup, first invite.
- **Recovery UX receives the same design attention as backup status.** Non-technical restore flow, progress indication, no rclone paths at the moment the user is already stressed.
- **CRDT engine choice is kept reversible behind a stable abstraction.** `ICrdtEngine` or equivalent. Yjs today, Automerge or Loro tomorrow, without rewriting the application layer.
- **Honesty about offline-only failure modes is non-negotiable.** Symmetric NAT plus relay outage is one example; extended partition beyond the GC horizon is another. Name them, document the fallback, resist the temptation to pretend they cannot occur.
- **Global deployment context is part of the product specification.** Load-shedding durability, shared-device recovery, non-GDPR regulatory envelopes, intermittent connectivity as operational baseline — these are product requirements for the markets where local-first is most valuable.

---

## The Principle: Data Ownership Requires the Export Button

Ferreira's Round 1 block reduced to a single principle: you cannot claim to give users ownership of their data if you do not give them a way to take it somewhere else.

The local node solves the access problem. Data on the user's machine is accessible when vendor servers are down; data in the local encrypted database cannot be held hostage by a subscription paywall. But access is not portability. A user who wants to move to a different application needs an export — JSON, CSV, Markdown — in formats that any competent software can ingest.

The export button is not a nice-to-have. It is the proof of the claim.

The same logic extends to disaster recovery. *Your data is backed up* is not sufficient. *Your data can be restored by a non-technical user in under thirty minutes after complete device failure* is the claim that actually serves users. A backup that cannot be restored is not a backup. It is a simulation of safety.

Honesty about failure modes is what separates production local-first software from a persuasive demo. Every architecture has connectivity scenarios it cannot handle. Carrier-grade NAT plus relay outage produces a failure mode where two peers cannot communicate — and documenting it, with the self-hosted relay as the fallback, is the work that earns the architecture production credibility.

Ferreira has shipped production local-first software. He recognized the difference. He PROCEED'd when he saw it.

---

## References

[1] M. Kleppmann, A. Wiggins, P. van Hardenberg, and M. McGranaghan, "Local-first software: You own your data, in spite of the cloud," in *Proc. ACM SIGPLAN Int. Symp. New Ideas, New Paradigms, and Reflections on Programming and Software (Onward! '19)*, Athens, Greece, Oct. 2019, pp. 154–178, doi: 10.1145/3359591.3359737. [Online]. Available: https://www.inkandswitch.com/essay/local-first/
