---
title: "The Recruitment Interview"
volume: 2
act: 1
chapter: 2
mission-day: pre-departure (flashback)
icm-stage: icm/draft
word-count-target: 9000
log-opener-pattern: A
---

*Pre-departure record, dated 2026-04-02T14:42Z. Yusupova, Mission Director-designate. Sunfish-1.*

*Selection of Principal Architect closed this date. Joel Reyes accepted the offer at 16:47 local on the closing call. Vetting interview conducted that afternoon by secured channel; recording filed to selection-archive per consortium convention. Technical questions and protocol-layer responses summarized in Annex C of the selection file. The exchange that determined the offer turned on Reyes's account of his Round-1-BLOCK rewrite of the lease protocol; the exchange is reproduced below from my recollection. The verbatim recording is on file. The version that follows is what I remember.*

*— Filed to selection-archive; hash f3a4...90c2*

---

I had the consortium's shortlist in late spring. There were six names on it. Three of them were architectural-paper authors and three were senior implementers from existing local-first projects. The shortlist had been compiled by the consortium's technical advisory group; my job was not to choose the architecture — I had already chosen the architecture, and the consortium had already accepted my choice. My job was to choose the architect.

Joel Reyes was the second name on the list and the only one whose paper I had read end to end three times. I had read it the first time at a kitchen table in St. Petersburg in November, in the week after my mother's hospital admission, when I was already going to need the paper to be true and was prepared to be disappointed by it. I was not disappointed. I read it the second time on the flight back from Bremerhaven in early December, with a printout I had marked up in the margins, looking specifically for the places where the argument went thin. The places were not where I had expected them. I read it the third time in late January, after the council review had landed and the BLOCK on Joel's lease protocol was a matter of public record. The third reading was not for the architecture. The third reading was for what Joel had done after the BLOCK.

Klett's verdict ran to twenty-eight pages. I had read all twenty-eight pages. The objection on the lease protocol was not that the protocol was wrong as drawn. The objection was that the partition-recovery rule was incomplete — that under sustained partition with quorum exhaustion, the rule produced no defined behavior, and that no defined behavior is not safe in a Flease-family protocol where lease decisions can grant write authority that has consequences. Klett had constructed an adversarial scenario in which the original lease holder lost connectivity mid-write, peers could not reach the lease holder to confirm or invalidate the in-flight operation, the lease expired on the wall clock, and a new lease holder negotiated quorum among the remaining peers. Two states existed simultaneously at that moment. The original node, if it had processed the operation locally before losing connectivity, believed it had completed the write. The new lease holder proceeded to accept writes from the remainder of the team. When both nodes eventually reconnected, the architecture had no fence specified to prevent the second write from landing on top of the first, and for the class of records the lease protocol existed to protect — sequential identifiers, unique constraints, the records the user trusts the system to never quietly lie about — that absence was a data-corruption scenario waiting for the first long partition.

That was the BLOCK. Klett wrote it in the prose he uses when he is not interested in being polite, which is most prose. He named the gap precisely. He did not propose a fix. He said the architecture had not proved the window was safe and had not specified a fence that would prevent it, and that he would not pass the protocol until one or the other was true.

What Joel had done after the BLOCK was the thing I read the paper for the third time to understand. The Round Two submission cleared with conditions — fifteen of them, none of them on the lease layer. The lease protocol in Round Two was a different protocol. The fence was specified. The two-record-class distinction Klett had asked for was specified. The new lease holder's acknowledgment requirement was specified. The protocol was correct as far as I could read it, and Klett had read it more carefully than I could and had cleared it.

What I wanted to know was what had happened in Joel's head between the BLOCK and the rewrite. The paper did not tell me that. The Round Two submission did not tell me that. The council review did not tell me that. I had read every public artifact and the artifact I needed was not in any of them.

I needed to ask him.

---

I spent the morning of the call reading. I had asked the system, the night before, to pull the Round One verdict, the Round Two submission, and the diff between the two lease protocols, and to set them where I would find them on the screen at the desk in the morning. I had also asked it to pull every public note Joel had attached to a Sunfish commit during the week between the verdict and the rewrite. There were three notes. One of them was the message he had sent back to Klett with the corrected protocol. The other two were operational — a build-system fix, a documentation update — and were not relevant to the interview. I read them anyway.

I asked the system to pull my own selection file next. I had been adding to the file for four months. The system pulled it without asking which version I wanted, because there was only one version on my node and the version on my node was the one I had been writing. I read what I had written about Joel. I had written the same thing in three different ways across the four months. The third way was the one closest to what I actually thought, which was that he was the candidate the prior failure made me pick.

I closed the file. I asked the system to start the call at fourteen-thirty local. The call would route through the consortium's secured channel and the recording would land in the selection-archive automatically, signed at capture, hash-chained to the rest of the file. I did not have to do anything to make the recording happen. The architecture I was about to interview Joel about was the architecture that was going to record the interview. I noticed the symmetry. I did not name it aloud. I made tea.

The video call was scheduled for a Tuesday afternoon St. Petersburg time, which made it five in the morning where Joel was, which I had not known until he sent me a calendar acceptance with a note: *I will be on. Coffee will already be made.* The note had arrived at 02:18 his time. I had read it the next morning and registered, without being sure I was registering it, that Joel had answered the calendar request the same night I had sent it and that he had answered without negotiating the time. I had sent a 5am-his-time slot deliberately. I wanted to see whether he would push back. He did not push back. He confirmed.

That was the first piece of evidence, before the call had even started.

I took the call from my office at AARI. The office is small and has a window that faces the back of another institute building and a desk that I have used for eighteen years, and the camera angle the laptop produces flatters no one. Joel's camera angle was worse than mine. He was at a kitchen table in what looked like a single-story house in a coastal-American somewhere, with a window behind him that was beginning to lighten. He had the coffee. He had a notebook. He had a printed copy of the council review on his left and what looked like a printout of his own paper on his right, both of them annotated. He had the kind of haircut a man has when he has stopped caring what his haircut looks like. He had the exact register of a senior engineer who has been called in for an interview with a customer he has been hoping to work with, who has not slept poorly, who has not over-prepared, and who has read every document I would have wanted him to read.

He said good morning. He said it in English, not in Russian — he had reading Russian and conversational basics from the OSS collaboration but did not pretend to more than that, and he was correct not to. I said good morning back. We exchanged the names of our institutional affiliations. I told him this would be a long call and that he should drink the coffee while it was still hot. He said the coffee had been hot when he sat down. I let two seconds pass. He waited. The waiting was the second piece of evidence. I have learned over the years to count the time before a man fills silence; men who have spent careers in environments where silence has procedural meaning fill it on a different clock than men who have not.

I asked him to walk me through the architecture as if I had not read the paper. He asked whether he should start with the data layer or with the sync daemon. I said the data layer. He started with the data layer.

He spent thirty-five minutes on it. I am not going to reproduce the explanation here because the explanation is in his paper and the paper is the document that became the artifact, and a staff-history account of a recruitment interview is not the place to recapitulate the public record. What I will record about those thirty-five minutes is what I was watching for and what I saw.

I was watching for the places where his explanation diverged from his paper. Architects who have written something and walked away from it explain it differently the second time; architects who are still in the architecture explain it the same way. Joel explained it the same way. The vocabulary was identical. The structural moves were identical. He used the same example I had highlighted in my second reading — the multi-region team running through a thirty-day partition with a single node generating operations in isolation — and he used it for the same purpose, which was to install in the listener's mind that the local store is the durable buffer and that operations are not lost during extended offline periods because the architecture's assumption is that offline periods are unbounded. I had marked the example in my margin with a small star. He hit the star without looking at the page.

I was also watching for the moments where he reached for vocabulary that did not appear in the paper. Senior implementers always reach for vocabulary that did not make the paper, because papers are compressed and the implementations are not. Joel reached for *trust-but-verify* twice. He reached for *single-failure mode* once. He reached for *the gauge in front of you* in the context of cloud telemetry. None of the three phrases were academic vocabulary. All three of them were operational vocabulary. I made a note. I would ask about the note later.

When he finished the data-layer walkthrough I asked him to do the sync daemon. He did the sync daemon. He took twenty minutes on it. He covered the gossip protocol's anti-entropy cycle, the resource governor that throttles per-tick bandwidth during reconnection storms, the capability negotiation phase where two peers exchange schema versions before exchanging operations, the stale-peer recovery protocol that initiates a full-state snapshot transfer when a reconnecting peer's vector clock predates the GC horizon, and the quarantine queue for operations that fail structural validation at store entry. He used the same example each time he needed an example, which was a node offline for ninety-five days reconnecting to a mesh whose other peers had compacted their operation history past day ninety-five. The example mapped exactly to the case I had asked the consortium's technical advisory group about during the architecture-selection phase. I had asked the question because I wanted to know what the architecture did when a partition outlasted the GC retention. Joel had been answering my question for twenty minutes without my having asked it.

I had a question about the GC policy. I had been waiting to ask it. I asked it now.

I said: *The three-tier GC policy. Ephemeral, business, compliance. The business tier is ninety days. What happens when a peer comes back at ninety-five days and the originating node has compacted away the operations the peer needs to incrementally sync?*

He said: *The reconnecting peer's vector clock is older than the GC horizon. The sync daemon detects that at capability negotiation. It abandons incremental sync and initiates a full-state snapshot transfer. The peer receives the current document state directly — not the operations that produced it — and resumes gossip from the snapshot as a new baseline.*

I said: *That works if at least one online peer holds a snapshot that covers the reconnecting peer's last known state. What happens when no online peer holds a snapshot that covers the reconnecting peer's last known state?*

He said: *That's the case Klett raised in Round Two. It's the case that does not exist for compliance records, because the compliance tier has no GC and the full operation history is always recoverable. It exists for business records, in the specific case where every online peer has applied GC past the reconnecting peer's last sync point. The reconnecting peer can still resume from a current-state snapshot, but the peer cannot recover the operations that occurred between the peer's last sync and the GC horizon. Those operations are gone from the mesh.*

I said: *That's a data-loss case.*

He said: *It is a data-loss case at the level of the operation log. It is not a data-loss case at the level of the document, because the document state is preserved and the document state is what the application reads. The audit trail of how the document arrived at its current state is what is lost. For the business tier the architecture's claim is that the audit trail is not load-bearing for that tier — that's the definition of the business tier — and the operational consequence is that a reconnecting peer who was in fact present during operations that have been GC'd will see the merged result of those operations without seeing the operations themselves. The peer does not produce a wrong answer. The peer does not see the history.*

I said: *Why is that not a fence violation?*

He said: *Because the application semantics for business records do not require the history. The contract for business records is that the document state is correct under merge. The history is a convenience. The contract for compliance records is different. The contract for compliance records includes the history. The compliance tier preserves the history, which is why the compliance tier does not GC. The fence is the tier classification. The tier classification is the implementer's responsibility to make correctly per record class.*

I said: *And if the implementer classifies a record as business when it should have been compliance?*

He said: *Then the implementer has shipped a deployment with a misclassified record. The architecture cannot prevent that. The architecture can document that the classification is the load-bearing decision and can specify what each classification commits to. The paper does specify that. Chapter twelve. There's also a tooling pass we are working on for the Sunfish distribution that runs static analysis against the schema to flag records that look like they should be compliance but have been classified as business. The static analysis is not in the paper because the paper is the architecture and the static analysis is the deployment tool. They are different artifacts.*

I waited. He waited. I asked one more question on the GC policy, which was about the relay's role during a stale-peer reconnect when the relay was the only peer that had retained a snapshot covering the reconnecting peer's last known state. He answered it. The answer included a specific note about the relay's policy not to retain plaintext snapshots and to participate in the snapshot transfer as a forwarder rather than as a holder of the snapshot. I had read the same note in the paper and had wanted to hear him say it without prompting. He said it without prompting.

I moved to the lease layer.

He paused for a second before he started the lease layer. I would not have caught the pause if I had not been counting. The pause was not nervousness. The pause was the half-second a man takes when he registers that the question he was waiting for has arrived.

He said: *The lease layer is the layer the council blocked on. I'd rather not walk you through the original protocol, because the original protocol was wrong. I'll walk you through the rewrite. The rewrite is what I would deploy.*

I said: *Walk me through the rewrite.*

He walked me through the rewrite. It took fourteen minutes. He started with the two-record-class distinction Klett had asked for in the Round One verdict. The distinction was between records where the CP constraint was a domain invariant layered on top of an AP data structure — quantities that were CRDT-merged at the data layer and then validated against the constraint as a post-merge check — and records where two concurrent writes could not be merged at all. Sequential identifiers. Unique constraints. The records the lease protocol existed to protect at the level of the write itself, not at the level of the post-merge validation.

For the second class — the records where merge could not resolve — the rewrite specified the fence. The new lease holder, before accepting the first new write, required acknowledgment from all reachable peers that the previous lease had expired and that no in-flight write was pending from the previous lease holder. The acknowledgment requirement was the load-bearing piece. Without the acknowledgment the new lease could not be granted. Without the new lease the new write could not be accepted. The split-write window — the gap between the original lease holder losing connectivity and the new lease holder beginning to accept writes — was no longer a gap. It was a closed interval where neither node could write. The closed interval was the fence.

I asked: *What if the original lease holder was the only node that had completed a write during its lease, and the original lease holder is now unreachable to all the other nodes? The other nodes cannot acknowledge the absence of an in-flight write because they cannot see the original node's state.*

He said: *In that case the new lease holder cannot obtain the acknowledgment. The acknowledgment requires a positive statement from each reachable peer that no in-flight write is pending. A reachable peer that was a quorum participant during the original lease but has no record of the original write makes that statement on the basis of its local audit log. A peer that has no audit log entry from the original lease holder during the lease window makes the statement on the basis of the absence. The acknowledgment is satisfiable in that case. The case where the acknowledgment is not satisfiable is the case where a reachable peer holds an in-flight write that the original lease holder initiated and propagated to the peer before losing connectivity. That peer cannot acknowledge the absence of an in-flight write because the in-flight write exists. The peer's response blocks the new lease.*

I asked: *And the in-flight write resolves how?*

He said: *The peer holds the in-flight write in the quarantine queue until the original lease holder reconnects or until a configurable timeout expires. On reconnect, the original lease holder either confirms or invalidates the write through its own local audit log. On timeout, the in-flight write is treated as failed; the quarantine queue surfaces it to operations for review; the new lease can then be granted. The timeout is the deployment's choice. For most deployments the right value is short — minutes to hours. For deployments where the network is expected to be partitioned for days at a time, the right value is longer, and the deployment accepts that the lease layer is unavailable for that duration. The architecture does not pick the value. The deployment picks it.*

I asked: *And the wall-clock dependency in the lease-expiry computation?*

He said: *Wall clock is the worst clock in any distributed system. The lease-expiry computation does not depend on wall clock between peers. It depends on local monotonic clock at the lease holder for the purpose of detecting that the holder's own lease has expired, and on a coordinator-mediated tick for the purpose of any peer's confirmation that the lease has expired. The original protocol used wall clock for both. The rewrite uses monotonic clock for the holder's self-check and the coordinator tick for the peer-side check. The two clocks can disagree about milliseconds. They cannot disagree about minutes, because the coordinator tick is observed by every peer as the same event. The disagreement window is bounded by the network latency between any peer and the coordinator. The original protocol's wall-clock dependency was the assumption I missed.*

I made another note. I had asked the question because I had wanted to know whether the rewrite was a patch on the original or whether it was a different protocol. The answer was that the wall-clock dependency had been the load-bearing assumption of the original; the rewrite was a different protocol because the load-bearing assumption was different. The original was a clean draft of a flawed assumption; the rewrite was a clean draft of a corrected assumption. Joel had not patched. He had rewritten.

I asked one more question on the lease layer, which was about the relay's role as quorum participant for two-person teams. The relay was a managed component — one of the few managed components in the architecture, a component that lived on infrastructure the consortium would operate but that the consortium could not control. I wanted to know what happened when the relay was unreachable to one of the two endpoints but reachable to the other. The asymmetric-partition case. Klett had raised it in Round Two as a follow-up condition rather than as a block. I wanted to know what Joel had done with it.

He walked me through it. The behavior was defined. The defined behavior was that neither endpoint could obtain a lease — the endpoint with relay reachability would request quorum and not receive it, because quorum required acknowledgment from both the other endpoint and the relay, and the other endpoint was unreachable; the endpoint without relay reachability would not request quorum at all, because it could not contact a quorum participant. Both endpoints would back off and retry. The architecture would degrade to no-write on the CP-class records until full reconnect. AP-class records would continue to converge through gossip. The system would not produce the split-write the Round One protocol could have produced.

I asked him whether that was the design or whether it was the consequence of the design.

He said it was the consequence. The design was the fence. The fence was the acknowledgment requirement. The asymmetric-partition behavior fell out of the fence by construction — once you required acknowledgment from all reachable peers before granting a new lease, and you required all reachable peers to include the relay where the relay was a configured participant, the asymmetric case had no path to a granted lease. The case was not handled because someone wrote a clause for it; the case was handled because the fence eliminated it.

I made another note. I wrote *fence by construction* and underlined it twice. I had also made a note three weeks earlier, when I had read the Round Two protocol for the first time, that the protocol read as though someone had stopped trying to handle the failure cases and had started trying to eliminate them. That note had been a guess. The interview had just confirmed the guess.

I had decided what the next question was going to be three weeks earlier, when I had read the council review for the second time. I had written the question down in the same notebook I was now holding. I had written it in pen so I would not edit it.

I asked: *What did you do the night the BLOCK landed?*

---

He took a breath. He did not look away from the camera. He said:

*I missed it. The original protocol assumed the network would heal within quorum-exhaustion windows. The assumption did not hold under sustained partition. Klett was right. I rewrote it.*

He said it in four sentences. He did not soften any of the four sentences. He did not say "to be fair" or "in defense of the original protocol" or "I think what Klett was getting at." He did not explain what he had been thinking when he wrote the original. He did not name the constraints that had produced the original assumption. He did not point out — though he could have, accurately — that the original protocol had passed five rounds of internal review before going to the council and that those five rounds had not surfaced the sustained-partition case. He did not minimize. He did not contextualize. He said what was true about the protocol he had written and about the verdict the council had returned, in plain words and in the order the words went.

There was a fifth sentence. He waited about a second after the fourth sentence and then he added it.

He said: *The rewrite is what should have been there the first time.*

I made a note in my book. I wrote one word, in pen, and I underlined it. The word was *yes*.

---

I will say something here that I have not said in print before. I am going to say it because the staff history is the place where you say things plainly or you do not say them at all.

The man who failed me on my last mission did not say what Joel said. The man who failed me on my last mission named a schema-migration limitation only after the limitation manifested under partition and we had lost the operational window the limitation had cost us. He named it then in the form of an explanation for what we had just lost — *under these specific conditions, the migration can produce* — as though the conditions were the news rather than his prior knowledge of them. The schema-migration limitation had been known to him for months. The conditions had been documented in his project's internal notes for longer than the mission had existed. He had not disclosed any of it during the engineering review I had run before we sailed, which had included a question about exactly the class of conditions the limitation manifested under, which he had answered without naming the limitation. He answered the question by describing what the system did under nominal conditions and let the absence of partition discussion stand as an absence rather than as an answer. The answer he gave was technically true and operationally a lie. We sailed on the technically-true answer. We came home on the operationally-a-lie.

I did not write any of that into the after-action report at the time. I wrote *engineering pre-mission review did not surface the issue,* which was technically accurate and operationally a lie of the same shape his had been. I wrote it because I could not yet write the longer version, and because the longer version would have ended a man's career, and because I was not sure in the months after the mission whether I wanted to end his career or whether I wanted to end my own. The five years between then and now are the years it took to be sure I had wanted neither. I had wanted the next mission's architect to be the structural inverse of the man who had not disclosed.

I had specified that to the consortium in writing. I had not put it in those terms. I had said that I wanted an architect who had handled a public failure in a way that the public failure was the basis for trusting him rather than the basis for not trusting him. The consortium's technical advisory group had pulled together the shortlist. The shortlist contained six names. By the third reading of his paper I had decided that the right name was Joel's. The video call was the verification.

The verification arrived at four sentences. *I missed it. The original protocol assumed the network would heal within quorum-exhaustion windows. The assumption did not hold under sustained partition. Klett was right. I rewrote it.*

Then the fifth: *The rewrite is what should have been there the first time.*

I had what I needed.

---

I could have ended the call there. I did not end the call there. I had three more areas to cover and the directness Joel had just demonstrated did not exempt him from the rest of the interview; if anything, it raised the standard for the rest of the interview, because I now knew he could meet a higher standard and I was going to ask him questions that required him to meet it.

I asked him about Byzantine operations.

The council had raised it as a medium-priority condition in Round Two. A CRDT operation produced by a buggy client version could be structurally valid — well-formed CBOR, correct causal dependencies, valid operation type — while being semantically incorrect. A character insertion at the wrong position. A counter increment that wraps incorrectly. A field value set to an impossible state by a client-side validation bug. The CRDT would accept the operation, merge it faithfully, and propagate it to every peer in the mesh. Every node would converge on the same incorrect state. The architecture's correctness guarantee was exactly the property that made the failure difficult to remediate; convergence was consistent, deterministic, and durable, and convergence on a software defect was equally consistent, deterministic, and durable.

I had marked the condition in my third reading. I had wanted to know what Joel did with it.

I said: *Operation validation. Quarantine queue. Walk me through what happens when a peer ships a buggy client release and starts producing structurally valid but semantically corrupt operations.*

He said: *Operation validation gates insertion into the local store. Before an operation is applied locally and queued for gossip, the sync daemon checks it against the current schema definition for the operation's record type. Type, range, structural constraints, referential integrity. If the operation passes the schema check, it goes into the store. If it fails the schema check, it goes into the quarantine queue. The quarantine queue surfaces it to operations for review. The same machinery handles offline writes that need post-reconnect validation. The same machinery handles incoming operations from a peer running a buggy release.*

I said: *Schema check at the receiver. The receiver doesn't trust the sender.*

He said: *The receiver does not trust the sender. The receiver trusts its own schema. The sender's schema may be older, newer, or wrong. The capability negotiation phase exchanges schema versions before the gossip cycle and decides whether the two peers can exchange operations at all. If they can, the receiver applies its own schema check to every incoming operation. If the operation fails the check, the operation goes to quarantine and the sender does not learn the operation was rejected until the next gossip cycle, when the operation does not appear in the receiver's outbound delta.*

I said: *And if the buggy release is producing operations that pass the schema check but encode the wrong domain semantics? The character at the wrong position. The increment that wraps.*

He said: *That's the harder case. The schema check catches structural defects. It does not catch a defect that produces structurally valid output. For that case the architecture has a break-glass procedure. The procedure assumes the defect has been detected — through user-visible incorrect data, through downstream system failures, through the peer producing the bad operations being identified. The procedure is documented in chapter fifteen of the paper. It involves a compensating-operation pass that overwrites the incorrect content while preserving the operation log's audit integrity. The compensating pass is human-judged. The architecture cannot automate it because the architecture does not know what the correct domain state was.*

I said: *And the tooling for that exists.*

He said: *The tooling exists at the level of the procedure being documented and the compensating-operation primitive being implemented. The tooling does not yet exist at the level of an operations dashboard that lets a deployment engineer execute the procedure under production pressure without writing custom code. That tooling is on the roadmap. It is not in the paper. It will not be in the maiden voyage's deployment.*

I said: *So if a buggy operation propagates during the mission, the response is custom code under production pressure.*

He said: *Yes. The architecture has the primitives. The architecture does not have the dashboard. If the case occurs during the mission, I will write the code on the boat. If the case occurs during a deployment that does not have me on it, the deployment will need to either bring in someone who can write the code or accept that the response time is the time it takes to bring in someone who can write the code.*

I made a note. I wrote *primitives present, tooling pending* and underlined it. I would not have accepted the answer from another candidate. I accepted it from him because the answer was honest about what existed and what did not, and because the *if it happens during the mission, I will write the code on the boat* was the kind of sentence I was going to have to take on faith and was going to be willing to take on faith from him in particular.

The next area was the operations layer. I asked him about how he ran his own deployments. Not the architecture — the operations. How did he know whether his test deployments were healthy? What did he watch? What did he not trust? I had a specific reason for the question, which was that the failed mission's architect had been in love with his test telemetry and had not understood, until I asked him plainly under operational pressure, how little of the telemetry was running on the platform he was claiming to deploy. I had spent three years deciding I would never again recruit an architect without asking him directly what gauge he watched.

Joel said: *I run independent diagnostics on local sensors only. Cloud telemetry is fine for the metrics it's reporting on. I run the diagnostics on local sensors because cloud telemetry is a service that can decide to stop responding without telling me first. I have worked on platforms that did exactly that. I would rather see the gauge in front of me.*

He used the phrase *the gauge in front of you* twice in one answer. He had used it once during the data-layer walkthrough. I had marked it as operational vocabulary. The third use was not recycling. The third use was the same operational instinct returning to the same architectural question. I asked him where he had picked up the phrase. I asked it in the way you ask a man about a piece of his vocabulary you have noticed: lightly, as though the answer might or might not exist.

He said: *Old job. The kind of job where you don't run the system on a single sensor and you don't trust a remote indication if you have a local one. The phrase was muscle memory by the time I was thirty.*

I waited. He waited. The waiting did the work the question had not done. He added: *I came up through a discipline that had been worked out on platforms where the failure mode of trusting a remote indication you should have read locally was specific and bad. The discipline did not transfer one-for-one to civilian distributed systems, but most of it transferred. The phrase came with it.*

I did not press for more. I had registered, without yet knowing what to do with the registration, that the phrase belonged to a specific institutional past, and that Joel had not named the institution. The not-naming was deliberate. Senior engineers who do not name their formative employer are usually doing it for one of two reasons: a non-disclosure obligation, or a habit of not explaining the past to people who have not earned the disclosure. I would learn months later that for Joel it was the second reason. I would learn the institutional past on the boat, in a conversation I did not yet know was coming, in a quiet hour during a surface window. The naming would come when he was ready to name it. I respected that he had not named it on the call. I did not press.

I moved to the third area, which was the project's name.

I asked him: *Why Sunfish?*

He paused longer this time. The pause was about three seconds. The pause was again not nervousness. The pause was a different register of the same not-volunteering-the-past register I had just observed on the operations question. I would later understand that I had asked the two questions in the wrong order; if I had asked about the name first, he would have answered it the same way he answered the operations question, which is to say not yet. Asking it second, after he had already declined to name his old discipline, gave him the option of declining to name the project's origin too.

He took the option. He said: *The name is private to me. I named it after something. I'd rather tell you what I named it after on the boat than on a video call. If you select another candidate, I'll tell you anyway. But I'd rather tell you in person.*

I noted that. I did not press. I had asked the question because the architecture's name had a weight in the paper that did not seem to be public-facing weight, and I had wanted to know whether the weight came from somewhere. The weight came from somewhere. I was going to learn what it was. I was going to learn it from him, in person, when he chose to tell me. I respected that too.

I had what I needed on the technical interview. I had been on the call for a little over two hours.

---

I asked him whether he had questions for me.

He said yes. He had three questions.

His first question was about the consortium. He wanted to know which co-funder's regulatory framework the mission's data sovereignty would be assessed under, given that the consortium was multinational and the data we would generate would be subject to overlapping jurisdictional claims. The question was technically a procurement question and operationally a sovereignty question and architecturally the question that determined what fence the architecture would have to live under. I told him the answer. The answer was layered — the primary framework was the consortium-of-record's, with a fall-through to each co-funder's domestic framework for data originating from instruments that co-funder had supplied, with a meta-framework specified in the consortium charter that handled jurisdictional conflicts. He asked me to send him the charter. I told him I would. I asked the system to set a reminder on my own file to push the charter to him after the call closed. The system acknowledged. I returned my attention to Joel.

His second question was about the crew. He wanted to know how many of the senior officers had served with me before. He did not ask the question to assess my command authority. He asked it to assess the operational tempo I was likely to run; senior officers who have served with a mission director before learn the director's rhythms, and the rhythms inform what the architecture would have to absorb. I gave him the answer. Four of the senior officers were people I had commanded at least once before. Two more were people I had not commanded but had worked alongside in cross-institutional contexts. The remaining six were people I had selected after reading their work or interviewing them. He asked for the names. I gave him the names. He said two of them out loud as though tasting them — Priya Iyer's name, and Wanjiru Kamau's. I asked him whether he had read their work. He said he had read all of Priya's published work on schema migration in offline-first systems and had been a reader of Wanjiru's standards-body filings on key revocation since 2023. He said it without performance. I made another note, which was that he had read the team I had picked before I had told him who was on it.

His third question was the one I had been waiting for, because it is the question every architect should ask and most do not.

He said: *The architecture has not been deployed in a production environment under sustained partition with a crew whose lives depend on it. You're asking me to be on board the first time it is.*

He said the words without inflecting them as a question. Then he stopped.

I said: *Yes.*

I let the *yes* stand. I did not elaborate. I was going to let him decide what to do with it.

He thought for about four seconds. He nodded once. He said: *Yes.*

That was the recruitment. There was paperwork after, and a follow-up call to negotiate his role on the boat versus his role at the OSS project during the mission window, and a conversation with the consortium's technical advisory group to formalize the appointment. None of that mattered. The recruitment had happened in the four seconds between my *yes* and his *yes*, and the substance of the recruitment had happened in the four sentences he had said when I asked him what he did the night the BLOCK landed.

*I missed it. The original protocol assumed the network would heal within quorum-exhaustion windows. The assumption did not hold under sustained partition. Klett was right. I rewrote it.*

And the fifth: *The rewrite is what should have been there the first time.*

I had a man who would tell me the truth when it mattered. I had a man whose discipline was not in the public posture but in what he did when the public posture went wrong. I had a man who had been told he was wrong and had not defended; had not minimized; had not explained; had not waited for the council to soften the verdict before acknowledging it; had sat with the verdict and had rewritten the protocol and had sent the rewrite back with a short note that said *you were right, here is the corrected protocol, please review.*

I had read that note in the council's Round Two record. I had read it three times. The note was a public artifact — the council had reproduced it verbatim in their Round Two summary, in the section where they explained why the rewrite was acceptable. The note was the public artifact of the private act. The private act was the night Joel had spent rewriting the protocol after the verdict. I did not need the private act on record. I needed to know the private act had happened. The video call had told me it had happened. The four sentences and the fifth had told me. The two-second pause before he answered the lease question had told me. The pause before he declined to name the project had told me. The way he had registered Priya's and Wanjiru's names had told me. The whole call had told me.

I closed the laptop. I sat in my office for a while. I was not thinking, exactly. I was registering that the trust I had been waiting five years to extend had a person attached to it now. The registration took the rest of the afternoon.

I called my mother that evening. I did not tell her what I had decided. I told her about the bakery near the office that had changed its hours. She told me about the building across from her flat that the city had finally repainted. We talked about nothing of consequence for forty-five minutes. The Sunfish-1 mission was twelve months from departure. I had time to tell her later. I have told her since.

---

I am back on the boat now. It is Day 14. The tea is cold.

The architecture has been holding. The local store has answered every query I have run against it with the kind of plainness Joel's paper said it would, because there is nothing else to answer with under the ice. The relay is dormant. The gossip protocol has correctly identified itself as dormant rather than as failing, the way Joel said it would. The schema state is stable. The audit log is intact. None of those properties are why I am writing tonight, because none of those properties answer the question that was asked of me in the recruitment interview by the man being recruited — *you're asking me to be on board the first time it is.* The properties answer the architectural question. The architectural question was answered by his rewrite of the lease protocol four years before the maiden voyage and by the council's clearance of the rewrite three years before the maiden voyage and by my reading of the cleared rewrite two years before the maiden voyage. The properties are the architecture being itself.

What is being answered tonight, on Day 14, in the late hour after the watch I am not standing, is the other question — the one I asked him about what he did the night the BLOCK landed. The answer to that question has been on the boat since Joel was on the boat. Tonight, when I queried the local store and it answered me locally because there was nothing else to answer with, the architecture's authority and the architect's discipline registered for me as the same property. I had read the paper three times. I had selected the man whose discipline had produced the paper. The discipline is what we have under the ice. The paper is the artifact. The boat is the proof. The proof is happening.

That is why it was him. That is why I am still writing this two hours after I should have been asleep, in a register I do not put in the operational log, in a chapter of the staff history that the consortium will eventually publish without ever quite knowing what its load-bearing element is. The load-bearing element is the four sentences and the fifth. The load-bearing element is the rewrite that should have been there the first time. The load-bearing element is the man who said it that way without softening it.

I will end the entry here. The next watch is in three hours and I would like to sleep before it. The boat is fine. The architecture is fine. Joel is two compartments aft, on the late shift at the data console, working a routine reconciliation pass with Wanjiru. He does not know I am writing this. He has not known for fourteen days that I am writing this. He may eventually read this; he may not. The staff history is a public document and I will write it accordingly. The disclosure of why I picked him does not require his permission, because the picking was mine. The fact of his having said what he said when I asked the question does require his permission, and I have his permission by virtue of his having said it on a recorded interview that the consortium has on file. He knew the call was being recorded. He spoke into the record anyway.

That is the property. He spoke into the record anyway.

The architecture is the same property. It exists on the record. It does not flinch from being on the record. The man who built it is on the record about the night he rewrote the protocol he had been told was wrong. The boat is on the record about Day 14 of an under-ice partition operating exactly as the rewrite specified. The crew is on the record because I am writing this and I will sign it.

That is why it was him.

I am going to bed.

— A. Y., Day 14, Sunfish-1
