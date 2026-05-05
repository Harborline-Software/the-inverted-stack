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

Joel Reyes was the second name on the list and the only one whose paper I had read end to end three times. I had read it the first time at a kitchen table in St. Petersburg in November, in the week after my mother's hospital admission, when I was already going to need the paper to be true and was prepared to be disappointed by it. I was not disappointed. The kitchen was warm; the table was the table my father had built; my mother was in a hospital fourteen blocks away; the paper was on a tablet I had borrowed from the institute because my own had stayed at the office. I read it through once and then read the lease layer twice more before I went to bed.

I read it the second time on the flight back from Bremerhaven in early December, with a printout I had marked up in the margins, looking specifically for the places where the argument went thin. The places were not where I had expected them. I read it the third time in late January, after the council review had landed and the BLOCK on Joel's lease protocol was a matter of public record. The third reading was not for the architecture. The third reading was for what Joel had done after the BLOCK.

Klett had written the verdict in the prose he saves for people he thinks should know better. The shape of the BLOCK was simple enough to hold in one image: under sustained partition, two nodes could both believe they owned the same truth, and the protocol had no way to stop them. The lease holder lost connectivity mid-write; the lease expired; a new lease holder accepted writes; on reconnect, the architecture had no fence to prevent the second write from landing on top of the first. For the class of records the lease protocol existed to protect — sequential identifiers, unique constraints, the records the user trusts the system never to quietly lie about — that absence was a data-corruption scenario waiting for the first long partition.

That was the BLOCK. Klett named the gap precisely and did not propose a fix.

What Joel had done after the BLOCK was the thing I read the paper for the third time to understand. The Round Two submission cleared with fifteen conditions, none of them on the lease layer. The lease protocol in Round Two was a different protocol. The fence was specified. The two-record-class distinction Klett had asked for was specified. Klett had read it more carefully than I could and had cleared it.

What I wanted to know was what had happened in Joel's head between the BLOCK and the rewrite. The paper did not tell me. The Round Two submission did not tell me. The council review did not tell me.

I needed to ask him.

I didn't need another clever protocol. I had the protocol. I needed to know what kind of man wakes up the morning after Klett tells him he's wrong. The architecture would only ever be as trustworthy as the architect's response to being told he had built it wrong. If the response was defense, or context, or quiet repositioning, the architecture would carry that response into every future failure. If the response was the rewrite, the architecture would carry that instead. The technical questions I was about to ask him were not technical questions. They were the test.

---

I spent the morning of the call reading. I had asked the system, the night before, to pull the Round One verdict, the Round Two submission, and the diff between the two lease protocols, and to set them where I would find them on the screen at the desk in the morning. I had also asked it to pull every public note Joel had attached to a Sunfish commit during the week between the verdict and the rewrite. There were three notes. One of them was the message he had sent back to Klett with the corrected protocol. The other two were operational — a build-system fix, a documentation update — and were not relevant to the interview. I read them anyway.

I asked the system to pull my own selection file next. I had been adding to the file for four months. The system pulled it without asking which version I wanted, because there was only one version on my node and the version on my node was the one I had been writing. I read what I had written about Joel. I had written the same thing in three different ways across the four months. The third way was the one closest to what I actually thought, which was that he was the candidate the prior failure made me pick.

I closed the file. I asked the system to start the call at fourteen-thirty local. The call would route through the consortium's secured channel and the recording would land in the selection-archive automatically, signed at capture, hash-chained to the rest of the file. I did not have to do anything to make the recording happen. The architecture I was about to interview Joel about was the architecture that was going to record the interview. I noticed the symmetry. I did not name it aloud. I made tea.

The video call was scheduled for a Tuesday afternoon St. Petersburg time, which made it five in the morning where Joel was, which I had not known until he sent me a calendar acceptance with a note: *I will be on. Coffee will already be made.* The note had arrived at 02:18 his time. I had read it the next morning and registered, without being sure I was registering it, that Joel had answered the calendar request the same night I had sent it and that he had answered without negotiating the time. I had sent a 5am-his-time slot deliberately. I wanted to see whether he would push back. He did not push back. He confirmed.

That was the first piece of evidence, before the call had even started.

I took the call from my office at AARI. The office is small and has a window that faces the back of another institute building and a desk that I have used for eighteen years, and the camera angle the laptop produces flatters no one. Joel's camera angle was worse than mine. He was at a kitchen table in what looked like a single-story house in a coastal-American somewhere, with a window behind him that was beginning to lighten. He had the coffee. He had a notebook. He had a printed copy of the council review on his left and what looked like a printout of his own paper on his right, both of them annotated. He had the kind of haircut a man has when he has stopped caring what his haircut looks like. He had the exact register of a senior engineer who has been called in for an interview with a customer he has been hoping to work with, who has not slept poorly, who has not over-prepared, and who has read every document I would have wanted him to read.

He said good morning. He said it in English, not in Russian — he had reading Russian and conversational basics from the OSS collaboration but did not pretend to more than that, and he was correct not to. I said good morning back. We exchanged the names of our institutional affiliations. I told him this would be a long call and that he should drink the coffee while it was still hot. He said the coffee had been hot when he sat down. I let two seconds pass. He waited. I got to three before he answered. The waiting was the second piece of evidence. I have learned over the years to count the time before a man fills silence; men who have spent careers in environments where silence has procedural meaning fill it on a different clock than men who have not.

I asked him to walk me through the architecture as if I had not read the paper. He asked whether he should start with the data layer or with the sync daemon. I said the data layer. He started with the data layer.

He spent thirty-five minutes on it. I am not going to reproduce the explanation here because the explanation is in his paper and the paper is the document that became the artifact, and a staff-history account of a recruitment interview is not the place to recapitulate the public record. What I will record about those thirty-five minutes is what I was watching for and what I saw.

I was watching for the places where his explanation diverged from his paper. Architects who have written something and walked away from it explain it differently the second time; architects who are still in the architecture explain it the same way. Joel explained it the same way. The vocabulary was identical. The structural moves were identical. He used the same example I had highlighted in my second reading — the multi-region team running through a thirty-day partition with a single node generating operations in isolation — and he used it for the same purpose, which was to install in the listener's mind that the local store is the durable buffer and that operations are not lost during extended offline periods because the architecture's assumption is that offline periods are unbounded. I had marked the example in my margin with a small star. He hit the star without looking at the page.

He reached for the printout of his own paper twice in the first ten minutes. Each time, his hand moved toward the page; each time, the hand stopped before it landed; each time, he gave the answer without consulting it. By minute fifteen he had stopped reaching. The paper sat at his right hand for the remainder of the call as a reference he no longer needed.

I was also watching for the moments where he reached for vocabulary that did not appear in the paper. Senior implementers always reach for vocabulary that did not make the paper, because papers are compressed and the implementations are not. Joel reached for *trust-but-verify* twice. He reached for *single-failure mode* once. He reached for *the gauge in front of you* in the context of cloud telemetry. None of the three phrases were academic vocabulary. All three of them were operational vocabulary. I made a note. I would ask about the note later.

When he finished the data-layer walkthrough I asked him to do the sync daemon. He did the sync daemon. He took twenty minutes on it. He used the same example each time he needed an example: a node offline for ninety-five days reconnecting to a mesh whose other peers had compacted their operation history past day ninety-five. *Snapshot when history is gone* — that was the move. The example mapped exactly to the case I had asked the consortium's technical advisory group about during the architecture-selection phase. I had asked the question because I wanted to know what the architecture did when a partition outlasted the GC retention. Joel had been answering my question for twenty minutes without my having asked it.

I had a question about the GC policy. I had been waiting to ask it. I asked it now.

I said: *The three-tier GC policy. A peer reconnects at ninety-five days. The originating node has compacted past the peer's last sync point. What happens?*

He reached for the printout on his right and then set it aside without looking at it. He said: *Vector clock is older than the GC horizon. The sync daemon detects that at capability negotiation. It abandons incremental sync and initiates a full-state snapshot transfer. The peer resumes from the snapshot as a new baseline.*

I said: *That's the case Klett raised in Round Two. It's a data-loss case at the operation-log level for business records.*

He said: *Yes. And it is not a data-loss case at the document level, because the document state is preserved. The history is the convenience; the document is the contract. There is a kind of data where history can be GC'd. There is a kind where it must not. Misclassifying a record as business when it should have been compliance is an operator sin, not an architecture bug. Chapter twelve specifies the tier contracts. The fence is the classification. The classification is the implementer's responsibility.*

I got to three before I asked the next one. He had walked me to the edge of data loss and then shown me where the fence actually stood.

I asked one more question on the GC policy, which was about the relay's role during a stale-peer reconnect — specifically the relay's policy not to retain plaintext snapshots and to participate as a forwarder rather than as a holder. He said it without prompting. He walked through the other partition-recovery edge cases in the same dry, precise way; none of them surprised me as much as the first.

I moved to the lease layer.

He rubbed his eyes once. The room behind him had filled with the kind of light that means morning has arrived without the man in it asking. He had been talking for almost two hours at five in the morning his time, and the only thing he had asked of the call so far was the coffee. He paused before he started the lease layer. Six seconds before he spoke. I was counting. The pause was not nervousness. The pause was the half-second a man takes when he registers that the question he was waiting for has arrived, extended by the time it took him to decide how to begin.

He said: *The lease layer is the layer the council blocked on. I'd rather not walk you through the original protocol, because the original protocol was wrong. I'll walk you through the rewrite. The rewrite is what I would deploy.*

I said: *Walk me through the rewrite.*

He walked me through the rewrite. It took fourteen minutes. He started with the two-record-class distinction Klett had asked for in the Round One verdict — records where post-merge validation was sufficient, and records where two concurrent writes could not be merged at all. Sequential identifiers. Unique constraints. The records the lease protocol existed to protect at the level of the write itself.

For the second class, the rewrite specified the fence. The new lease holder, before accepting the first new write, required acknowledgment from all reachable peers that the previous lease had expired and that no in-flight write was pending from the previous lease holder. The acknowledgment requirement was the load-bearing piece. Without the acknowledgment the new lease could not be granted. The split-write window — the gap the original protocol had not closed — was no longer a gap. It was a closed interval where neither node could write. The closed interval was the fence.

I asked the obvious adversarial case: a peer that holds an in-flight write the original lease holder propagated before losing connectivity. He answered without reaching for the printout. The peer cannot acknowledge the absence of what it holds; the peer's response blocks the new lease; the in-flight write sits in the quarantine queue until the original lease holder reconnects or a configurable timeout expires; on timeout, the queue surfaces it to operations for review; the new lease can then be granted. The deployment chooses the timeout. The architecture does not.

I asked about the wall-clock dependency.

He said: *Wall clock is the worst clock in any distributed system. The original protocol used wall clock for both the holder's self-check and the peer-side confirmation. The rewrite uses monotonic clock for the holder's self-check and a coordinator-mediated tick for the peer-side check. The wall-clock dependency was the assumption I missed.*

His voice on *the assumption I missed* dropped a register. Not regret; not performance. The flat tone of a man stating where the failure had lived. I made a note.

I had wanted to know whether the rewrite was a patch on the original or a different protocol. The answer was that the wall-clock dependency had been the load-bearing assumption of the original; the rewrite was a different protocol because the load-bearing assumption was different. Joel had not patched. He had rewritten.

I asked one more question on the lease layer — the relay's role as quorum participant in the asymmetric-partition case Klett had raised in Round Two as a follow-up condition. Joel walked me through the behavior. Neither endpoint obtained a lease. Both endpoints backed off and retried. CP-class records degraded to no-write; AP-class records continued to converge through gossip.

I asked him whether that was the design or the consequence of the design.

He said it was the consequence. The design was the fence. The fence was the acknowledgment requirement. The asymmetric-partition behavior fell out of the fence by construction — once you required acknowledgment from all reachable peers before granting a new lease, the asymmetric case had no path to a granted lease. The case was not handled because someone wrote a clause for it. The case was handled because the fence eliminated it.

I wrote *fence by construction* in my notebook and underlined it twice. I had made a note three weeks earlier, when I had read the Round Two protocol for the first time, that the protocol read as though someone had stopped trying to handle the failure cases and had started trying to eliminate them. The interview had just confirmed the guess.

I had decided what the next question was going to be three weeks earlier, when I had read the council review for the second time. I had written the question down in the same notebook I was now holding. I had written it in pen so I would not edit it.

I had also written, on the facing page, the answer I would not accept. I had written that one in pen too. *To be fair, the original protocol — .* I had drawn a line through it the day I read it back. The line through it was the test. If Joel reached for that sentence, or any sentence that began the same way, I was going to thank him for his time and end the call within the hour. The consortium would not have known the call had ended on the BLOCK question. The consortium would have known only that I had not extended the offer to the second name on the list. The first three names were ahead of him on the consortium's ranking; only Joel was ahead of him on mine.

I closed the notebook over my pen so I would not look at the page again. I put my hands in my lap. I waited until Joel had finished the lease-layer answer and was looking at me through the camera, expecting the next question.

I asked: *What did you do the night the BLOCK landed?*

---

He took a breath. He did not look away from the camera. The pause was longer than the technical answer required. I let it sit. The pause was the question's actual answer; what came after the pause would be the words that confirmed it.

When he spoke, his voice changed register — flatter, slower, the cadence of a man reading a verdict back to the room rather than explaining a protocol to a recruiter. I noted the shift. I did not name it aloud.

He said:

*I missed it. The original protocol assumed the network would heal within quorum-exhaustion windows. The assumption did not hold under sustained partition. Klett was right. I rewrote it.*

He said it in four sentences. He did not soften any of the four sentences. He did not say *to be fair* or *in defense of the original protocol* or *I think what Klett was getting at.* He did not explain what he had been thinking when he wrote the original. He did not name the constraints that had produced the original assumption. He did not point out — though he could have, accurately — that the original protocol had passed five rounds of internal review before going to the council and that those five rounds had not surfaced the sustained-partition case. He did not minimize. He did not contextualize. He said what was true about the protocol he had written and about the verdict the council had returned, in plain words and in the order the words went.

There was a fifth sentence. He waited about a second after the fourth sentence and then he added it.

He said: *The rewrite is what should have been there the first time.*

The light behind him was full now. He did not reach for the coffee. He did not look down at his notebook. He had said what he had come to say and was waiting for the next question.

I let the silence hold for the count of three. He let it hold with me. The silence was not awkward and was not heavy; it was the silence two people share when one of them has just done something the other has been waiting to see done.

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

The council had raised it as a medium-priority condition in Round Two — a CRDT operation produced by a buggy client could be structurally valid while being semantically wrong, and the architecture's convergence guarantee would propagate the defect faithfully to every peer in the mesh. The property that made the architecture correct was the same property that made the failure difficult to remediate. I had marked the condition in my third reading. I had wanted to know what Joel did with it.

I said: *Walk me through what happens when a peer ships a buggy release and starts producing structurally valid but semantically corrupt operations.*

He answered the easy half first — the schema check at the receiver, the quarantine queue, the receiver-trusts-its-own-schema posture. *The receiver does not trust the sender.* The same machinery handled offline writes pending post-reconnect validation and incoming operations from a peer running a buggy release. Then he stopped, looked at me through the camera, and gave me the harder half.

He said: *The schema check catches structural defects. It does not catch a defect that produces structurally valid output. For that case the architecture has a break-glass procedure documented in chapter fifteen. A compensating-operation pass that overwrites the incorrect content while preserving the operation log's audit integrity. Human-judged. The architecture cannot automate it because the architecture does not know what the correct domain state was.*

I said: *And the tooling exists?*

He said: *The primitives exist. The dashboard does not. If the case occurs during the mission, I will write the code on the boat. If it occurs in a deployment that does not have me on it, the deployment brings in someone who can write the code, or accepts that the response time is the time it takes to bring someone in.*

I wrote *primitives present, tooling pending* and underlined it. I would not have accepted the answer from another candidate. I accepted it from him because *I will write the code on the boat* was the kind of sentence I was going to have to take on faith, and from him in particular I was willing to.

The next area was the operations layer. I asked him about how he ran his own deployments. Not the architecture — the operations. How did he know whether his test deployments were healthy? What did he watch? What did he not trust? I had a specific reason for the question, which was that the failed mission's architect had been in love with his test telemetry and had not understood, until I asked him plainly under operational pressure, how little of the telemetry was running on the platform he was claiming to deploy. I had spent three years deciding I would never again recruit an architect without asking him directly what gauge he watched.

Joel said: *I run independent diagnostics on local sensors only. Cloud telemetry is fine for the metrics it's reporting on. I run the diagnostics on local sensors because cloud telemetry is a service that can decide to stop responding without telling me first. I have worked on platforms that did exactly that. I would rather see the gauge in front of me.*

He used the phrase *the gauge in front of you* twice in one answer. He had used it once during the data-layer walkthrough. I had marked it as operational vocabulary. The third use was not recycling. The third use was the same operational instinct returning to the same architectural question. I asked him where he had picked up the phrase. I asked it in the way you ask a man about a piece of his vocabulary you have noticed: lightly, as though the answer might or might not exist.

He set the coffee down. The set-down was deliberate; not careful, not slow, but considered — the action of a man choosing where his hands would be when he answered a question he had been asked many times in many phrasings.

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

His second question was about the crew. He wanted to know how many of the senior officers had served with me before. He did not ask the question to assess my command authority. He asked it to assess the operational tempo I was likely to run; senior officers who have served with a mission director before learn the director's rhythms, and the rhythms inform what the architecture would have to absorb. I gave him the answer. Four of the senior officers were people I had commanded at least once before. Two more were people I had not commanded but had worked alongside in cross-institutional contexts. The remaining six were people I had selected after reading their work or interviewing them. He asked for the names. I gave him the names.

He said two of them out loud as though tasting them — Priya Iyer's name, and Wanjiru Kamau's. He said Priya's first; he held the second name for a beat. I asked him whether he had read their work. He said he had read all of Priya's published work on schema migration in offline-first systems and had been a reader of Wanjiru's standards-body filings on key revocation since 2023. He said it without performance and without elaboration; he did not name the specific filings, did not characterize Priya's body of work, did not explain what about either had drawn his attention. He answered the question I had asked and did not answer the questions I had not. I made another note, which was that he had read the team I had picked before I had told him who was on it.

His third question was the one I had been waiting for, because it is the question every architect should ask and most do not.

He said: *The architecture has not been deployed in a production environment under sustained partition with a crew whose lives depend on it. You're asking me to be on board the first time it is.*

He said the words without inflecting them as a question. Then he stopped. He had named the thing the call had been built around without naming it directly until that moment, and he had named it in the form of the offer rather than in the form of the objection.

I said: *Yes.*

I let the *yes* stand. I did not elaborate. The architecture's claim under sustained partition was a claim that had not been deployed; my mother's hospital admission was a fact that had been; the consortium's funding cycle was a window that would close; the crew's lives were a load the architecture had not yet carried. All of those facts had been mine before the call. They were now also his. I was going to let him decide what to do with the *yes* I had given back.

He thought for about four seconds. He nodded once. He said: *Yes.*

That was the recruitment. There was paperwork after, and a follow-up call to negotiate his role on the boat versus his role at the OSS project during the mission window, and a conversation with the consortium's technical advisory group to formalize the appointment. None of that mattered. The recruitment had happened in the four seconds between my *yes* and his *yes*, and the substance of the recruitment had happened in the four sentences he had said when I asked him what he did the night the BLOCK landed.

He did not ask me, on the call, why I had selected him. He did not ask, in the months that followed, why I had asked the question I asked when I asked it. He did not behave, in any of the operational meetings between the offer and the boat, like a man who had been given a job. He behaved like a man who had been given an architecture under sustained partition with a crew whose lives depended on it, and who had said yes, and whose work from that moment forward was to make the yes hold. The work began the day after the call and has not stopped since.

*I missed it. The original protocol assumed the network would heal within quorum-exhaustion windows. The assumption did not hold under sustained partition. Klett was right. I rewrote it.*

And the fifth: *The rewrite is what should have been there the first time.*

I had a man who would tell me the truth when it mattered. I had a man whose discipline was not in the public posture but in what he did when the public posture went wrong. I had a man who had been told he was wrong and had not defended; had not minimized; had not explained; had not waited for the council to soften the verdict before acknowledging it; had sat with the verdict and had rewritten the protocol and had sent the rewrite back with a short note that said *you were right, here is the corrected protocol, please review.*

I had read that note in the council's Round Two record. I had read it three times. The note was a public artifact — the council had reproduced it verbatim in their Round Two summary, in the section where they explained why the rewrite was acceptable. The note was the public artifact of the private act. The private act was the night Joel had spent rewriting the protocol after the verdict. I did not need the private act on record. I needed to know the private act had happened. The video call had told me it had happened. The four sentences and the fifth had told me. The two-second pause before he answered the lease question had told me. The pause before he declined to name the project had told me. The way he had registered Priya's and Wanjiru's names had told me. The whole call had told me.

I closed the laptop. I sat in my office for a while. The window faced the back of the institute building across the courtyard; I had looked out of it for eighteen years and never seen weather in it. I was not thinking, exactly. I was registering that the trust I had been waiting five years to extend had a person attached to it now. The registration took the rest of the afternoon.

I called my mother that evening. I did not tell her what I had decided. I told her about the bakery near the office that had changed its hours. She told me about the building across from her flat that the city had finally repainted. We talked about nothing of consequence for forty-five minutes. The Sunfish-1 mission was twelve months from departure. I had time to tell her later. I have told her since.

---

I am back on the boat now. It is Day 14. The tea is cold. The watch I am not standing is Diego's; the boat is humming the way the boat hums under ice — the steady-state hum, not the one with anything in it.

The architecture has been holding. The local store answers every query without ambiguity. The relay is dormant. The gossip protocol has correctly identified itself as dormant rather than as failing. The schema state is stable. The audit log is intact. The architecture is fine; the boat is fine; the man who built the architecture is fine.

None of that is why I am writing tonight.

I am writing because of the rewrite that should have been there the first time. The architectural question was answered four years ago when Joel rewrote the lease protocol; the council's clearance answered it three years ago; my reading of the cleared rewrite answered it two years ago. What is answered tonight is the other question — the one he asked me on the call, the one I said yes to. *You're asking me to be on board the first time it is.* The architecture under the ice is the rewrite, deployed. The proof is happening.

That is why it was him. The load-bearing element is the four sentences and the fifth. The load-bearing element is the man who said them that way without softening them. Tonight, when I queried the local store and it answered me locally because there was nothing else to answer with, the architecture's authority and the architect's discipline registered for me as the same property. They were always going to register that way. I had selected him so that they would.

The next watch is in three hours and I would like to sleep before it. Joel is two compartments aft, on the late shift at the data console, working a routine reconciliation pass with Wanjiru. He does not know I am writing this. He has not known for fourteen days. He knew the call was being recorded. He spoke into the record anyway.

That is the property. He spoke into the record anyway. The architecture is the same property. The boat is on the record about Day 14 of an under-ice partition operating exactly as the rewrite specified. The crew is on the record because I am writing this and I will sign it.

That is why it was him.

I am going to bed.

— A. Y., Day 14, Sunfish-1
