# Chapter 1 - When SaaS Fights Reality

<!-- icm/voice-check -->
<!-- Target: ~5,200 words -->
<!-- Source: v13 §3, v13 Executive Summary, v13 §14.1, v13 §20.4, v5 §1 -->

---

It's two in the afternoon in Pune, and Sunita Kulkarni, the project manager on a $4.2 million hospital-expansion bid, is staring at a browser tab that refuses to load. The bid is due at five. The platform has been down since eleven.

The data isn't lost. It exists on servers in Virginia or Oregon — intact, on a hard drive Sunita will never access, in a building she couldn't find on a map. It's simply inaccessible. The vendor's status page calls it an outage affecting less than 1% of users. On this bid, that 1% is everyone.

This isn't a planning failure. Sunita planned correctly; her team had used the software. The failure is structural: her data resides on infrastructure she doesn't control, and when that infrastructure goes offline, her capabilities go with it.

This scenario repeats wherever deadline-sensitive work runs on cloud infrastructure — the attorney drafting a brief at nine in the evening, the engineer updating safety documentation in the field, the physician accessing records before rounds. The infrastructure fails identically. Only the deadlines change.

---

## The Bundle Nobody Agreed To

The SaaS deal goes like this: give us your data, keep it on our servers, pay us every month. In exchange you get real-time collaboration, multi-device access, and zero maintenance. Most users said yes without fully registering the second half. The first half was the product. The second half was the terms.

The three desirable properties are real. Real-time collaboration is transformative. Multi-device access means your work follows you. Zero maintenance means IT doesn't nurse a server in a closet.

The three conditions on the other side get less attention. Your data lives on vendor infrastructure, which means the vendor can see it, lose it, sell the company that holds it, or shut the service off. Pricing is at the vendor's discretion — the rate at adoption is a starting point, not a commitment. Service continuity is contingent on the vendor's survival.

The acceptance was rational, because the second half wasn't visible at adoption time. The pricing that wins a customer's business isn't calibrated to represent what the platform costs after that customer has built workflows, trained staff, and transferred data. The bundle reveals itself slowly, after switching costs have accumulated.

Users accepted these conditions because the three desirable properties appeared to *require* them. Real-time collaboration required a central server. Multi-device sync required a cloud acting as the authoritative copy. Zero maintenance required that the vendor control the infrastructure. The package looked indivisible because, with the technology of 2010, it largely was.

That is no longer true.

---

## Seven Ways SaaS Breaks in the Field

### The Outage That Takes Your Work With It

Major SaaS providers report 99.9% uptime — roughly 8.7 hours of downtime per year. For a single user, those hours scatter harmlessly across the calendar. For a team of ten, at any given moment somebody is in the middle of something time-sensitive.

Sunita Kulkarni's 8.7 hours found her at 4:47 in the afternoon with thirteen minutes left to submit a subcontractor bid for the Pune hospital expansion. The platform had been slow all afternoon. At 4:47 it stopped responding entirely. She refreshed. Spinning indicator. She called her counterpart who was supposed to countersign; her counterpart couldn't reach the platform either. The platform's single sign-on tied her email to the same provider — her email was locked too. At 5:04 she watched the timestamp move past the deadline. The bid was won by a competitor whose construction-management platform ran on a different vendor whose dependencies hadn't gone down at 4:47.

Sunita kept three tabs open after that. The tic is what she carries from the afternoon she lost the Pune hospital bid. The architecture is what eventually replaces the tic.

The outage the vendor publishes is the one it's willing to call an outage. Incidents affecting partial regions, specific features, or specific customer cohorts surface as "degraded performance" — a phrase that does most of its work by not being the word *outage*. With a clean outage you know to stop trying. With degraded performance you keep trying, and the failure looks like something you did.

Outage risk falls hardest on the moments that matter most. High-stakes work — deadline submissions, live customer sessions, critical handoffs — involves intensive platform use, which means it's more exposed to performance degradation under load. The work that can least tolerate delay tends to be the work with external dependencies: bids due to clients, documents due to regulators, reports due to boards. These are not moments where "try again in an hour" is an option.

The concentration of cloud hosting compounds this. The December 2021 AWS us-east-1 outage hit every product hosted there simultaneously — project management tools, document platforms, file storage, communication tools. Users who had adopted multiple platforms found that all their fallback options went down at the same time. Their vendor SLAs (Service Level Agreements) say nothing about the infrastructure layer beneath their vendor — shared cloud regions, CDN providers, authentication services — none of which the user has any contract with.

Outages hit hardest the users who can least work around them. Assistive technology users — those who rely on screen readers, switch access devices, or voice control — experience SaaS connectivity failure as complete access failure. Degraded performance that a sighted user circumvents by refreshing is inaccessible in a more absolute sense: the screen reader announces a failed load; voice control has no form fields to target. The architecture developed in later chapters keeps the application responsive regardless of network state. For AT users, this is not a usability improvement. It is the difference between accessible and inaccessible software.

### The Vendor That Disappears

In 2015, Sunrise Calendar had a substantial mobile user base and was widely considered the best third-party calendar app for iOS. Microsoft acquired it that year and shut it down in August 2016. Users received a few weeks' notice. The data was exportable in a format no other calendar app read natively.

Sunrise was not exceptional. It was typical of how software products end.

The mechanism changes — acquisition, runway exhaustion, a strategic pivot, the founder taking a job somewhere larger — but the pattern is consistent. The product goes dark. Users who built workflows around it are left with whatever they managed to export before the deadline. Salesforce acquired Quip and deprioritized it; teams that had built workflows around its document structure found the structure was stored in a format only Quip controlled.

When a vendor announces shutdown, it typically offers an export. What that export contains, what format it uses, and whether any other software can consume it are highly variable. For project management data, the export is typically a CSV of the task list — without comments, without attachment history, without the relationship structure that made the tool useful. For document collaboration, most platforms offer a PDF export, which preserves the appearance but none of the editability.

The risk has a name that undersells it. *Vendor shutdown* sounds like a rare catastrophe. Thousands of SaaS products shut down every year. Most are small enough that their shutdowns don't make news; their users find out through an email or a banner. The shutdowns that do make news — Google Reader's termination in 2013 despite millions of active users, the steady stream of products acquired into enterprise platforms and starved of investment — are notable for scale, not for being unusual.

### The Connectivity That Wasn't There

Construction sites operate at the edge of mobile coverage. A superintendent in a concrete frame building can't get a signal three floors underground. Rural professional service firms operate on connectivity that drops daily. Hospital clinical environments restrict wireless devices near sensitive equipment. Air-gapped facilities — manufacturing, defense, government — can't connect to any external network by policy.

For these users, offline capability is not a feature request. It is the baseline requirement.

The SaaS vendor's marketing page says "works on mobile," which is true when there's a signal. The application is a thin client rendering views from a remote database. Remove the remote database and the client has nothing to render.

Most SaaS platforms offer some form of "offline mode." In practice this means a read-only cache of recently viewed data, with form submissions that queue locally and attempt upload when connectivity returns — with uncertain success rates and no visibility into what actually synced. You can view the last-synced version of a document. You cannot create new records, run reports, or access data you haven't recently viewed.

Sabina Rahman is a microfinance loan officer for a Grameen-affiliated branch in rural northern Bangladesh. She covers eleven villages twice a week on a company motorbike, processing loan applications, KYC documentation, and repayment ledgers on a SaaS platform her bank standardized on the year of her hire. The platform is unreachable from her branch for an average of four hours a day.

The day she stopped trusting it was a monsoon-relief disbursement morning. Forty-seven applicants in queue by 8:00 a.m. The platform took submissions until 11:14. Then it went down. Sabina processed the remaining nineteen applications by hand, into a carbon-copy ledger she called *shotti'r khata* — the truth book — with the borrowers' thumbprints on the carbons. The platform came back at 16:32. None of the nineteen hand-processed applications appeared in it. The bank's compliance system flagged them as missing; the audit team flagged her as the failure. It took six weeks to enter all nineteen retroactively, with documentation explaining why the timestamps didn't match the borrowers' submissions.

Tariq Hassan works the other end of the spectrum, where connectivity fails for different reasons. He is an offshore field engineer on a UAE-operated platform in the Persian Gulf, two hundred and forty kilometers off the coast of Abu Dhabi. The platform's primary uplink is a Ku-band satellite. When weather conditions degrade the satellite — on average twice a month — the platform falls to a microwave backup. When both links drop, the platform is offline.

The day Tariq stopped trusting the cloud's ingestion pipeline was a six-hour double-link outage. The data buffered on the platform's local server. The uplinks returned. The buffer drained. The SaaS application the operator had standardized on was a thin client — it expected the data to be in the cloud already, and the ingestion pipeline rejected six hours of out-of-sequence data as malformed. The data was not lost. The onshore monitoring team was looking at the cloud, and the cloud was missing six hours of a drilling shift on a well that had cost the operator two hundred and ten million dollars to that point. Tariq spent the next ten days writing a manual reconciliation report.

Intermittent connectivity is not a US edge case. Scheduled load-shedding in Nigeria and South Africa cuts power for six to twelve hours daily; connectivity fails with it. Hundreds of millions of enterprise workers plan their workdays around outage schedules, not around the assumption that the network is always on. A SaaS platform that can't function without a persistent connection doesn't have a niche offline problem — it has an architecture that excludes the majority of the world's enterprise users from full functionality.

### The Data You Can't Get Back

Your vendor's terms of service say your data is yours. They are often technically correct — the vendor doesn't claim ownership of the content you create. What the terms don't address is *accessibility*.

Data you own but cannot retrieve is data you don't have.

Four mechanisms make data inaccessible while it technically "belongs" to you. Export rate limits: many platforms allow data export but rate-limit the export API to prevent bulk extraction; a legal firm with ten years of matter history may find that retrieving its own data at the permitted rate takes weeks. Proprietary formats: the export is available, but in a format only the vendor's tools read well — comment threads export as flat text, custom fields export as raw headers without semantic context. Feature-gated access: some platforms require paid subscriptions to access export features, so portability is contingent on continued payment. Account closure timing: access ends when the billing period ends; miss the export window — because you changed jobs, because the notice was unclear — and the data may be gone.

None of these are edge cases. They are the routine operational parameters of vendor-managed data.

### The Price That Changes After You've Committed

Switching costs in SaaS are high because users build workflows around software. Training, integrations, historical data, learned patterns — these represent real investments. Vendors know this.

Pricing is competitive during acquisition, when vendors are winning customers. After adoption, when switching costs are real and rising, pricing pressure relaxes. A company that adopted a project management platform at $8 per seat per month and now faces renewal at $18 per seat confronts a real calculation: pay the new rate, or absorb the migration cost. The migration cost is often large enough that the price increase wins.

Feature paywalls move in one direction. Features available on a given tier at adoption are not guaranteed to remain there. Per-seat models create structural pressure as teams grow — a ten-person team's bill scales to five times that at fifty people, by which point the switching cost has compounded accordingly.

Lock-in compounds when teams use multiple SaaS products that integrate with each other. A project management platform connected to a communication tool, a file storage service, a time tracker, and a billing system creates a dependency web where each integration raises the switching cost of every other platform. The web of dependencies is not a side effect of the SaaS model. From the vendor's perspective, it is a feature of it.

### The Drift You Don't See

The first five modes manifest visibly. The platform stops loading, the vendor announces shutdown, the laptop loses connectivity, the export fails, the price doubles. The user notices because the work stops.

This one doesn't. Two users edit the same record on different devices; a sync conflict resolves silently in favor of one set of changes, the other user's work is gone, and no error fires. A formula recomputes against stale upstream values, propagating a subtly wrong number through downstream cells; the dashboard reports green. A duplicate record gets created when a unique-key constraint fails to enforce across replicas; both records persist, both look authoritative, and the logic that depended on uniqueness produces wrong results until someone notices the second copy.

Silent corruption and silent divergence are the failure modes production engineering teams fear most: not the loud failures, but the quiet ones that surface only when a customer notices a number doesn't add up. SaaS resolves conflicts inside vendor infrastructure with no surfacing primitive; the user only learns about the resolution if it's wrong enough to notice. The architecture developed in later chapters makes the convergence question first-class at the data layer rather than implicit in vendor behavior.

### The Third-Party Veto

The first six failure modes originate inside the service relationship. An external authority — a government, a regulator, a court — can restrict access regardless of what either party wants. The vendor has not failed. The customer has not been negligent. A third party with authority over one or both sides has acted.

In 2022, Western SaaS providers — Adobe, Autodesk, Microsoft, Figma, and dozens of others — suspended service across Russia and CIS markets under sanctions enforcement. Organizations across those markets, accounting for hundreds of thousands of seats built into workflows over more than a decade, found their operations interrupted not because their vendors failed them but because their vendors were directed to stop serving them. In February 2026, the US Defense Secretary designated Anthropic's AI services a national security supply-chain risk [1]. Federal agencies with active Anthropic deployments received direction to cease using them. Anthropic contested the designation legally [2], and a California court enjoined portions of the order for civilian agencies [3]. The Department of Defense exclusion stood [4]. Both Anthropic and its federal customers wanted to continue the relationship. Neither controlled the outcome.

The authority can act on the customer instead. Russia's Federal Law 242-FZ has required since 2015 that personal data of Russian citizens be stored on servers located within Russia; organizations using Western SaaS found themselves structurally non-compliant not because their vendor did anything but because the SaaS architecture can't provide on-premises data residency by design. The European Court of Justice's 2020 Schrems II ruling constrained EU organizations from transferring personal data to US cloud providers without adequate supplemental safeguards. India's DPDP Act 2023 creates comparable obligations for Indian organizations using US-hosted services for Indian residents' personal data.

The structural property that makes this failure mode distinct: data custody determines exposure. Data in vendor infrastructure can be reached by a government action targeted at the vendor. Data on hardware the user controls requires action targeted specifically at the user.

---

## The Work That Doesn't Stop

The seven failure modes above describe what breaks. The work itself continues — that's the part most cloud-dependency arguments miss. Workers reach for whatever still works.

In February 2026, HBO Max's medical drama *The Pitt* devoted two consecutive episodes to this scenario. The fictional Pittsburgh Trauma Medical Center pre-emptively takes its electronic health record system offline after two nearby hospitals are hit with ransomware. Dry-erase boards return to the nurses' station. Paper prescription pads come out of the supply closet. Triplicate forms circulate among medical assistants who have never seen them — felt-tip markers oblivious to the carbon backing. The trauma center keeps operating. The patients get seen. The work doesn't stop.

The episode is fiction. The pattern is not. Maria Santos lived it.

Maria was the IT operations administrator at a 312-bed teaching hospital in Belo Horizonte the morning the ransomware hit. By 9:14 the EHR was unavailable system-wide. By 9:21 the radiology PACS was unreachable. The hospital had forty-seven patients in the OR queue. Without the EHR, that list existed in the heads of the nurses who had read it at 7 a.m. Maria spent the next eleven hours walking the floor with a clipboard, watching triage nurses recreate patient acuity ratings on dry-erase boards, standing next to a charge nurse trying to remember whether a man in Bay 4 had a sulfa allergy or a penicillin allergy because his chart was on a server that wouldn't respond.

The vendor restored access seventy-three hours later. The hospital had not lost a patient. Maria still checks every clinical-data record three times before she signs off on a handoff. Once is procedure. Three times is what she carries from the morning she couldn't tell a charge nurse whether a man's chart said sulfa or penicillin.

Healthcare ransomware incidents have run into the hundreds per year for several years. Healthcare-services research consistently associates EHR downtime with elevated patient-harm metrics. The on-screen chaos in *The Pitt* is not exaggerated — it is documentary realism dressed as drama.

Two observations drive every architecture decision that follows. First: the work continued because human practitioners knew what to do without the digital system. Domain expertise outlasts the software that depends on it. Second: the digital affordances didn't survive. Search disappeared. Pattern detection across patient histories — the analytic work that justified the EHR investment — became impossible until the system came back. The organization's ability to *do* the work survived. Its ability to do the work *better than paper* did not.

When the SaaS project management platform goes down, the construction office runs on whiteboards and printed change-order forms. When the SaaS legal-research platform is unreachable, the law firm sends an associate to the print library. None of these workarounds are the failure of the people. They are the *resilience* of the people. They are also a measurement of how much value the SaaS layer was adding versus how much it was simply mediating.

This is the gap the inverted stack closes. A SaaS outage takes everything digital with it; a local-first node holds the digital affordances on the device the practitioner is already using. The drawer of paper backup forms remains in the supply closet — but the drawer becomes a true backup rather than the only operating mode. When the network returns, the local node syncs. The post-incident overtime drops from days to minutes.

---

## Who Pays the Most

These seven failure modes don't hit every organization equally. The most exposed share a characteristic: they have the least structural leverage to address any of them.

A large enterprise with a skilled procurement team can negotiate. Data portability clauses, SLAs with financial penalties, escrow provisions for source code and data — these are available to buyers with enough revenue to make the vendor's legal team engage. When the vendor gets acquired, the enterprise has attorneys who can enforce contract terms.

Small and medium-sized professional service firms don't have this leverage. The legal practice with eight attorneys signs up through a website. The medical group with four physicians clicks through terms of service nobody reads. The construction firm with two project managers pays by credit card. Their vendor contract is the standard terms of service, unmodified — no SLA, no escrow, no explicit data portability requirement.

These are also the organizations where software failures have direct professional consequences rather than just operational inconvenience. The construction PM missing a bid deadline loses the bid and damages the client relationship. The legal practice unable to access case files has professional responsibility exposure. The medical practice that can't retrieve patient records has regulatory risk. The stakes of availability are not abstract.

And these organizations are the primary addressable market for the products most likely to carry the SaaS risks described above. The large enterprise with the IT team and procurement counsel uses enterprise-licensed software with negotiated protections. The eight-attorney law firm uses the same product tier as the freelancer, under the same standard terms, with the same structural exposure to every failure mode in this chapter.

This is not a coincidence. The SaaS bundle packages its desirable and undesirable properties in a way that affects smaller buyers more severely, because smaller buyers have less ability to negotiate the undesirable half away.

The regulatory dimension compounds this. A legal practice storing client communications in a vendor's cloud carries a professional duty to understand where that data lives. A medical practice has HIPAA obligations. For large enterprises, these get negotiated into vendor agreements with audit rights and data processing addenda. For the eight-attorney firm, the compliance answer is the vendor's standard privacy policy — a document written to protect the vendor, not the client.

The jurisdictional scope is wider than US-centric discussions acknowledge. The EU's Schrems II ruling, India's DPDP Act 2023, China's PIPL (2021), Brazil's LGPD (2018), South Africa's POPIA (2013), Nigeria's NDPR (2019), and Russia's Federal Law 242-FZ each make data residency a compliance mechanism rather than a preference. The full coverage table is in Appendix F. In each of these jurisdictions, an architecture where data lives on the user's own hardware is not merely preferred — in many configurations it is the architecture that makes compliance tractable.

---

## Why Users Have Accepted This

Until recently, they didn't have a choice.

Real-time collaboration required a central server both parties could read from and write to simultaneously. Every other approach — emailing files, shared drives, version control — introduced merge conflicts requiring manual resolution or coordination overhead requiring explicit locking. One copy, everyone editing the same one, solved both.

Multi-device sync required an authoritative copy that all devices agreed on. Without a cloud authority, devices had to figure out among themselves which version was current — and the consumer-grade protocols for resolving concurrent edits across devices reliably, at scale, without user intervention didn't exist.

Zero maintenance required that someone else manage the infrastructure. The comparison to self-hosted software circa 2005 is instructive: a self-hosted email server, a self-hosted project tracker — all theoretically possible, all practically demanding enough that most organizations paid someone else.

Users accepted the SaaS bundle not because they preferred the conditions on the second half but because the technology of the time made those conditions appear to be the cost of the first half. They were not accepting a bargain so much as acknowledging a constraint.

The constraint is removable.

The evidence is commercial, not theoretical. M-PESA has processed financial transactions for hundreds of millions of users across East Africa since 2007; MTN MoMo operates at comparable scale across dozens of African markets. Both are built on offline-tolerant transaction patterns — store-and-forward reconciliation, intermittent-network authorization, operational continuity through connectivity gaps — because the networks they run on require it. Local-first architecture is not a new idea awaiting adoption; it has operated at population scale for nearly two decades in the markets that most benefit from it.

In professional software, Linear demonstrates that a sync engine can run locally even inside a SaaS architecture — clients keep a local SQLite replica, and the cloud is demoted to a relay peer. Actual Budget delivers full personal finance capability with the user's data on local storage and the sync service optional. Anytype extends the pattern with end-to-end encrypted sync over user-controlled storage. These products demonstrate that the desirable half of the SaaS bundle — collaboration, sync, responsive UI — doesn't require vendor data custody to function.

---

## The Dependency That Looks Inevitable

Three independent technology shifts removed the structural necessity of the SaaS bundle: CRDTs (Conflict-free Replicated Data Types) in production at Linear, Automerge, Yjs, and Actual Budget; leaderless replication at the edge — the same family of protocols Cassandra and DynamoDB use at planetary scale, applied at five-machine team scale; and the local-service pattern that tools like VS Code language servers, Docker Desktop, and Tailscale made invisible to users. Each shift solved a problem unrelated to the SaaS bundle. The consequence — that the technical reasons SaaS architectures had to concentrate data at the vendor are gone — followed from those solutions. Chapter 2 develops each in full.

The architecture this book proposes has real costs. They don't disappear; they move. Software that ships to user-controlled hardware needs a helpdesk model, software-bill-of-materials discipline, patch cadence, key custody, schema migration across independently upgrading nodes, and operational telemetry from machines the operator doesn't own. Part III specifies the architecture that absorbs those commitments. Part IV specifies the playbooks that ship and operate it. The trade is vendor dependency for operational discipline. Most readers will conclude the trade is worth making for workloads where data sovereignty, regulatory exposure, or operational continuity rule out the SaaS bundle. Chapter 4 helps you decide.

Sunita's scenario — deadline-critical work held hostage by infrastructure she doesn't control — is the failure mode this architecture addresses first. Her data was never gone. It was inaccessible because the software's design placed it somewhere she couldn't reach. The remaining chapters specify a design where that distinction doesn't exist.

The building blocks are production-proven. What remains is the specific assembly that produces a node — not a smarter cache, not a thicker client, but a first-class local peer that behaves like a cloud application, passes enterprise security review, and treats user data ownership as a structural guarantee rather than a contractual one. Chapter 2 identifies exactly what that requires and where the existing work stops short. Chapter 3 draws the node.

---

## References

[1] Mayer Brown LLP, "Pentagon Designates Anthropic a Supply Chain Risk – What Government Contractors Need to Know," Mar. 1, 2026. [Online]. Available: https://www.mayerbrown.com/

[2] "Anthropic sues the Trump administration over 'supply chain risk' label," *NPR*, Mar. 9, 2026. [Online]. Available: https://www.npr.org/

[3] "Judge grants Anthropic preliminary injunction but Pentagon CTO says ban still stands," *Breaking Defense*, Mar. 26, 2026. [Online]. Available: https://breakingdefense.com/

[4] "Anthropic loses appeals court bid to temporarily block DOD ruling," *CNBC*, Apr. 8, 2026. [Online]. Available: https://www.cnbc.com/
