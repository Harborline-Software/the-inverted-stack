<!-- Trial draft. Source-mined from ch02-recruitment-interview.md (v4 listen-test-
     approved), rewritten in the Filchner / Anna-voice register locked at
     vol-2/SPINE.md and vol-2/ANNA-VOICE.md. Sits beside the v4 draft until
     the register passes the listen-test with the primary listener. Do not
     assemble; do not promote. -->

# Chapter 2 — The Recruitment Interview

*Pre-departure record, dated 2026-04-02T14:42Z. Yusupova, Mission Director-designate. RV* Nansen*, MERIDIAN-7.*

*Selection of Principal Architect closed this date. Joel Reyes accepted the offer at 16:47 local on the closing call. Vetting interview conducted that afternoon by secured channel; recording filed to selection-archive per consortium convention. Technical questions and protocol-layer responses summarized in Annex C of the selection file. The exchange that determined the offer turned on Reyes's account of his Round-1-BLOCK rewrite of the lease protocol; the exchange is reproduced below from my recollection. The verbatim recording is on file. The version that follows is what I remember.*

*— Filed to selection-archive; hash f3a4...90c2*

---

I had the consortium's shortlist in late spring. There were six names on it. The shortlist had been compiled by the consortium's technical advisory group; my job was not to choose the architecture — I had already chosen the architecture, and the consortium had already accepted my choice — my job was to choose the architect, which is, in my view and against what the consortium believes, the harder of the two.

Joel Reyes was the second name on the list and the only one whose paper I had read end to end three times.

I had read it the first time at a kitchen table in St. Petersburg in November, in the week after my mother's hospital admission, when I was already going to need the paper to be true and was prepared to be disappointed by it. I was not disappointed. The kitchen was warm. The table was the table my father had built. My mother was in a hospital fourteen blocks away. The paper was on a tablet I had borrowed from the institute. I had brought the tablet to the kitchen the way I had brought a book to a hospital waiting room when I was twenty-three: not to read it, but to have something in my hand that was not the thing in my mind.

I read the lease layer twice more before I went to bed.

I am going to write something about my mother here that I have not, to date, written down. The kitchen-table reading was the first hour, in four months, that I had not been measuring myself against the version of me my mother had once told me the neighbor's daughter was becoming. The neighbor's daughter was a perfectly nice woman who ran a translation business in Lyon and had never, to my knowledge, written a paper about anything. My mother had decided, in 2003, that the neighbor's daughter was the comparison standard for who I had failed to be, and the decision had held with the kind of consistency I have learned to respect in operational adversaries. The hospital admission had been a stroke. The stroke had not, in the end, killed her. It had not, on the other hand, restored to her the part of the personality that had been making the comparisons. I had a mother in a ward fourteen blocks away who could no longer find the words for the comparison she had spent thirty years making. The kitchen was the first place I had sat in four months that was not adjacent to either the ward or the silence she now occupied instead of speaking. I read the paper because the paper was the only thing in the kitchen that did not require me to feel what I was, in the kitchen, finally and unwillingly feeling.

I do not know what I expected of the paper. I do not, looking back, think I had expectations. I had a tablet, a kitchen, a hospital, a mother who was no longer making comparisons, and one hundred and twelve pages of architectural writing on a problem I had been carrying for five years. By the time I closed the tablet the second time I had registered, without yet trusting the registration, that this was the paper that was going to carry the next mission. The trust came later. The recognition came at the kitchen table.

I read it the second time on the flight back from Bremerhaven in early December, with a printout I had marked up in the margins, looking specifically for the places where the argument went thin. The places were not where I had expected them. The places were where I had wanted them not to be. I marked them with the small red star I reserve for paragraphs that I will need to ask the author about face-to-face, which is the star I had not used for any other paper in three years.

I read it the third time in late January, after the council review had landed and the BLOCK on Joel's lease protocol was a matter of public record. The third reading was not for the architecture. The third reading was for what Joel had done after the BLOCK.

Klett had written the verdict in the prose he saves for people he thinks should know better. The shape of the BLOCK was simple enough to hold in one image: under sustained partition, two nodes could both believe they owned the same truth, and the protocol had no way to stop them. For the class of records the lease protocol existed to protect — the records the user trusts the system never to quietly lie about — that absence was a data-corruption scenario waiting for the first long partition. Klett named the gap precisely. He did not propose a fix. That is also Klett.

The Round Two submission cleared with fifteen conditions, none of them on the lease layer. The lease protocol in Round Two was a different protocol. Klett had read the rewrite more carefully than I could and had cleared it.

What I wanted to know was what had happened in Joel's head between the BLOCK and the rewrite. The paper did not tell me. The Round Two submission did not tell me. The council review did not tell me. They could not. The thing I wanted to know was not in any of those three documents because the thing I wanted to know was not the kind of thing that goes in documents. I needed to ask him.

By the third reading, the architecture in the paper was the architecture I was going to deploy.

The architect was the other question. The architecture would only ever be as trustworthy as the architect's response to being told he had built it wrong. If the response was defense, or context, or quiet repositioning, the architecture would carry that response into every future failure. The rewrite was the response I needed; the technical questions I was about to ask him were not technical questions. They were the test.

---

I spent the morning of the call reading. I had asked the system, the night before, to pull the Round One verdict, the Round Two submission, and the diff between the two lease protocols, and to set them where I would find them on the screen at the desk in the morning. I had also asked it to pull every public note Joel had attached to a Sunfish commit during the week between the verdict and the rewrite. There were three. One was the message he had sent back to Klett with the corrected protocol. The other two were operational and were not, strictly, relevant to the interview. I read them anyway. Operational notes are how you find out whether a man's discipline lives at the protocol layer or further down.

I asked the system to pull my own selection file next. I had been adding to it for four months. I read what I had written about Joel. I had written the same thing in three different ways across the four months. The third way was the one closest to what I actually thought, which was that he was the candidate the prior failure made me pick. I am going to say more about the prior failure further down this page. I am putting it off until I have set up the rest of the call, because the prior failure is not the kind of fact that survives being introduced in the middle of a paragraph.

I closed the file. I asked the system to start the call at fourteen-thirty local. The recording would land in the selection-archive automatically, signed at capture, hash-chained to the rest of the file. The architecture I was about to interview Joel about was the architecture that was going to record the interview. I noticed the symmetry. I did not name it aloud. I made tea.

There was also, on the kitchen counter, a small white bag from the bakery near the office, which I had stopped at on the way in. The pastry inside the bag was a *vatrushka*, which is a thing the bakery did on Tuesdays. The *vatrushka* had been correct — short crust, the curd set without being grainy, no soggy bottom — and I had eaten half of it standing at the counter at 09:11 and put the other half in the bag for later. I had decided, by the time I walked into the office, that *later* meant *after the call*. I had been keeping the pastry available to myself as a small private after-action reward of a kind my mother would have judged me harshly for needing, and which I had decided, in the last twelve months, that I was going to give myself anyway.

I am writing the *vatrushka* into this account because the *vatrushka* was on the counter when Joel said the four sentences that determined the offer, and the *vatrushka* was, accordingly, the last thing in the room that did not yet know.

---

The video call was scheduled for a Tuesday afternoon St. Petersburg time, which made it five in the morning where Joel was. I had not, when I sent the calendar invite, looked up his time zone — I had set the slot at 14:30 St. Petersburg because that was when my afternoon was clear, and the consortium dossier had not flagged a residence — and his calendar acceptance had arrived at 02:18 his time with a one-line note: *I will be on. Coffee will already be made.*

The note had three pieces of information. The first was that he had absorbed the slot without negotiating it, which I had set at 14:30 deliberately *only* in the sense that I had not bothered to adjust for him. The second was that he was awake at 02:18. The third was that he was telling me he would be ready, which is the kind of thing a man says when he expects to be examined for whether he was, in fact, ready. I noted all three pieces of information. I did not yet draw a conclusion from any of them. The conclusion was the call's job.

I took the call from my office at the institute. Joel's camera angle was worse than mine. He was at a kitchen table in what looked like a single-story house in a coastal-American somewhere, with a window behind him that was beginning to lighten. He had the coffee. He had a notebook. He had a printed copy of the council review on his left and what looked like a printout of his own paper on his right, both of them annotated, and he had a small dark-green ceramic mug that was not the kind of mug a man buys for himself.

I will not, here, write down where I had given him that mug. The fact of the giving will go on the page. Whether he had kept it was, until this moment on the call, a question I had been carrying for five months without raising it to a question. It had now been raised. I made a note — three letters; I will spare you the letters.

He said good morning. He said it in English, not in Russian — he had reading Russian and conversational basics from the OSS collaboration but did not pretend to more than that, and he was correct not to. We exchanged the names of our institutional affiliations. I told him this would be a long call and that he should drink the coffee while it was still hot. He said the coffee had been hot when he sat down.

I let two seconds pass.

He waited.

I got to three before he answered. I have learned over the years to count the time before a man fills silence; men who have spent careers in environments where silence has procedural meaning fill it on a different clock than men who have not. Joel's clock was the right clock. That was the second piece of evidence, after the calendar acceptance. The third would arrive in twenty minutes. The fourth — the one that mattered — would arrive in about two hours.

I asked him to walk me through the architecture as if I had not read the paper.

He spent thirty-five minutes on the data layer. I am not going to reproduce the explanation here; the paper is the document that became the artifact, and a staff-history account of a recruitment interview is not the place to recapitulate the public record. What I will record is what I was watching for and what I saw.

I was watching for the places where his explanation diverged from his paper. Architects who have written something and walked away from it explain it differently the second time. Joel explained it the same way. The vocabulary was identical. The structural moves were identical. He used the same example I had highlighted in my second reading — a node offline for ninety-five days reconnecting to a mesh whose other peers had compacted their operation history past day ninety-five — and he used it for the same purpose, which was to install in the listener's mind that the local store is the durable buffer and that operations are not lost during extended offline periods. I had marked the example in my margin with a small star. He hit the star without looking at the page.

He reached for the printout of his own paper twice in the first ten minutes. Each time, his hand moved toward the page; each time, the hand stopped before it landed; each time, he gave the answer without consulting it. By minute fifteen he had stopped reaching. The paper sat at his right hand for the remainder of the call as a reference he no longer needed.

I made a note of three phrases that did not appear in his paper. *Trust-but-verify.* *Single-failure mode.* *The gauge in front of you.* All three were operational vocabulary. None were academic. I would come back to one of them.

There was a GC-policy question I had been waiting to ask, and I asked it.

He answered without reaching for the printout. He said: *There is a kind of data where history can be GC'd, and a kind where it must not. Misclassifying is an operator sin, not an architecture bug. The classification is the implementer's responsibility.*

He had answered the question I had not asked — whether he would name operator responsibility instead of hiding it inside the architecture. He had named it without prompting. He had walked me to the edge of data loss and then shown me where the fence actually stood. He had not pretended the architecture solved a problem the architecture had handed to its operators. Three letters in the notebook. I did not need more.

The note was the kind of note I had wanted to make in the after-action report on the prior mission and had not. I am, as I warned a few paragraphs ago, about to return to the prior mission. I am still putting it off. The next paragraph is the lease layer.

---

I moved to the lease layer.

He rubbed his eyes once. The room behind him had filled with the kind of light that means morning has arrived without the man in it asking. He had been talking for almost two hours at five in the morning his time, and the only thing he had asked of the call so far was the coffee. He paused before he started. Six seconds before he spoke. The pause was not nervousness. The pause was the half-second a man takes when he registers that the question he was waiting for has arrived, extended by the time it took him to decide how to begin.

He said: *The lease layer is the layer the council blocked on. I'd rather not walk you through the original protocol, because the original protocol was wrong. I'll walk you through the rewrite. The rewrite is what I would deploy.*

I said: *Walk me through the rewrite.*

He walked me through it. The fence was the load-bearing piece — the acknowledgment requirement that closed the split-write window. He explained it once and did not explain it again. His voice did not change between the technical clauses and the place where the original assumption had failed. He had not looked at his notes since minute six. When I asked the obvious adversarial case, he answered without reaching for the printout. When I asked about the wall-clock dependency, his voice dropped a register on *the assumption I missed* — not regret; not performance; the flat tone of a man stating where the failure had lived. My note read: rewrite, not patch.

What I was watching, while he talked, was not the protocol. I was watching the way his face did not change between the sentence in which the rewrite worked and the sentence in which the original had not. The two sentences cost him the same amount. A man who had cost the original protocol differently than he cost the rewrite would have shown the differential in his face. Joel did not. He had finished costing the original protocol four years earlier, on the night Klett's verdict had landed, and what was left now was the rewrite and the work of explaining it.

I was satisfied with the lease-layer answer before he had finished giving it. I let him finish anyway. I owed him the question I had been holding for three weeks, and I was not going to ask it before he had earned the right to be asked it.

I closed my notebook over my pen so I would not look at the page again. The next question had been decided three weeks earlier, when I had read the council review for the second time. The question lived in the same notebook. In pen, so I would not edit it.

On the facing page was the answer I would not accept. Also in pen. *To be fair, the original protocol — .* I had drawn a line through it the day I read it back. The line through the sentence was the test.

I put my hands in my lap. I waited until Joel had finished the lease-layer answer and was looking at me through the camera, expecting the next question.

I asked: *What did you do the night the BLOCK landed?*

---

He took a breath. He did not look away from the camera. The pause was longer than the technical answer required. I let it sit. The pause was the question's actual answer; what came after the pause would be the words that confirmed it.

When he spoke, his voice changed register — flatter, slower, the cadence of a man reading a verdict back to the room rather than explaining a protocol to a recruiter. I noted the shift. I did not name it aloud.

He said:

*I missed it. The original protocol assumed the network would heal within quorum-exhaustion windows. The assumption did not hold under sustained partition. Klett was right. I rewrote it.*

He said it in four sentences. He did not soften any of the four sentences. He did not say *to be fair* or *in defense of the original protocol* or *I think what Klett was getting at.* He did not explain what he had been thinking when he wrote the original. He did not name the constraints that had produced the original assumption. He did not point out — though he could have, accurately — that the original protocol had passed five rounds of internal review before going to the council. He did not minimize. He did not contextualize. He said what was true about the protocol he had written and about the verdict the council had returned, in plain words and in the order the words went.

There was a fifth sentence. He waited about a second after the fourth and then he added it.

He said: *The rewrite is what should have been there the first time.*

The light behind him was full now. He did not reach for the coffee. He did not look down at his notebook. He had said what he had come to say and was waiting for the next question.

I let the silence hold for the count of three. He let it hold with me. The silence was not awkward and was not heavy; it was the silence two people share when one of them has just done something the other has been waiting to see done.

I made a note in my book. I wrote one word, in pen, and I underlined it. The word was *yes*.

---

I am going to say something here that I have not said in print before. I am going to say it because the staff history is the place where you say things plainly or you do not say them at all, and this is the version of the staff history that says things plainly.

The man who failed me on my last mission did not say what Joel said. He named a schema-migration limitation only after the limitation manifested under partition and we had lost the operational window the limitation had cost us. He named it then in the form of an explanation for what we had just lost — *under these specific conditions, the migration can produce* — as though the conditions were the news rather than his prior knowledge of them. The schema-migration limitation had been known to him for months. The conditions had been documented in his project's internal notes for longer than the mission had existed. He had not disclosed any of it during the engineering review I had run before we sailed, which had included a question about exactly the class of conditions the limitation manifested under, which he had answered by describing what the system did under nominal conditions and letting the absence of partition discussion stand as an absence rather than as an answer. The answer he gave was technically true and operationally a lie. We sailed on the technically-true answer. We came home on the operationally-a-lie.

I did not write any of that into the after-action report at the time. I wrote *engineering pre-mission review did not surface the issue,* which was technically accurate and operationally a lie of the same shape his had been. I wrote it because I could not yet write the longer version, and because the longer version would have ended a man's career. The five years between then and now are the years it took to be sure I had wanted neither.

I had wanted the next mission's architect to be the structural inverse of the man who had not disclosed. The consortium had been told this in writing — not, you understand, in those terms. What I had said was that I wanted an architect who had handled a public failure in a way that the public failure was the basis for trusting him rather than the basis for not trusting him. The consortium's technical advisory group had pulled together the shortlist. By the third reading of his paper I had decided that the right name was Joel's. The video call was the verification.

The verification arrived at four sentences. Then the fifth.

I had what I needed.

---

I could have ended the call there. I did not end the call there. The directness Joel had just demonstrated did not exempt him from the rest of the interview; if anything, it raised the standard. I knew now that he could meet a higher bar; I was going to ask him questions that required him to.

I asked him about Byzantine operations — a CRDT operation produced by a buggy client, structurally valid, semantically wrong, propagating through the mesh on the architecture's correctness guarantee. The council had raised it as a medium-priority condition in Round Two. I had wanted to know what Joel did with it.

He answered the easy half first — the schema check, the quarantine queue, the receiver-trusts-its-own-schema posture. Then he stopped, looked at me through the camera, and gave me the harder half. The architecture had a break-glass procedure. The primitives existed. The dashboard did not. *If the case occurs during the mission, I will write the code on the boat.* He answered in the register of a man stating an operating cost rather than making a promise.

I would not have accepted *I will write the code on the boat* from another candidate. I accepted it from him because he had already shown me, twenty minutes earlier, what he did when he found out he had written code wrong. The pattern was the same pattern. A man who had absorbed the prior failure the way Joel had was a man whose offer to write the code on the boat was an offer the architecture's discipline would carry with it. The same words, from anyone else, would have been a young man's bravado. I noted it.

The next area was the operations layer. I asked him how he ran his own deployments. Not the architecture — the operations. What did he watch? What did he not trust? I had a specific reason for the question, which was that the failed mission's architect had been in love with his test telemetry and had not understood, until I asked him plainly under operational pressure, how little of the telemetry was running on the platform he was claiming to deploy. I had spent three years deciding I would never again recruit an architect without asking him directly what gauge he watched.

Joel said: *Cloud telemetry is fine for the metrics it's reporting on. I run independent diagnostics on local sensors because cloud telemetry is a service that can decide to stop responding without telling me first. I have worked on platforms that did exactly that. I would rather see the gauge in front of me.*

He used the phrase *the gauge in front of you* twice in the answer. He had used it once during the data-layer walkthrough. The third use was the same operational instinct returning to the same architectural question. The phrase was not vocabulary he had picked up to impress me; it was vocabulary that had been carrying his work since before this call existed.

I asked him where he had picked up the phrase. I asked it lightly, as though the answer might or might not exist.

He set the mug down. The set-down was deliberate; not careful, not slow, but considered — the action of a man choosing where his hands would be when he answered a question he had been asked many times in many phrasings.

He said: *Old job. The kind of job where you don't run the system on a single sensor and you don't trust a remote indication if you have a local one. The phrase was muscle memory by the time I was thirty.*

I waited. He waited. He added: *I came up through a discipline that had been worked out on platforms where the failure mode of trusting a remote indication you should have read locally was specific and bad. The discipline did not transfer one-for-one to civilian distributed systems, but most of it transferred. The phrase came with it.*

I did not press for more. He had named the shape of the institutional past without naming the institution. The not-naming was deliberate; he was not going to tell me on the call. I noted the not-naming. I did not yet ask about it.

I moved to the third area, which was the project's name.

I asked him: *Why Sunfish?*

He paused longer this time. About three seconds. The pause was a different register of the same not-volunteering-the-past register I had just observed on the operations question.

He said: *The name is private to me. I named it after something. I'd rather tell you what I named it after on the boat than on a video call. If you select another candidate, I'll tell you anyway. But I'd rather tell you in person.*

I did not press. The architecture's name had a weight in the paper that did not seem to be public-facing weight. The weight came from somewhere. He had told me, in the register he had told me with, that he would tell me when he was ready. I respected that.

I had what I needed on the technical interview. I had been on the call for a little over two hours.

---

I asked him whether he had questions for me.

He had three.

His first was about the consortium's regulatory framework — which co-funder's data sovereignty rules the mission would be assessed under. The question was technically a procurement question and operationally a sovereignty question and architecturally the question that determined what fence the architecture would have to live under. I told him the answer in layers and asked the system to push him the consortium charter after the call. He thanked me.

His second was about the crew. He wanted to know how many of the senior officers had served with me before. Not to assess my command authority. To assess the operational tempo I was likely to run; senior officers who have served with a director before learn the director's rhythms, and the rhythms inform what the architecture would have to absorb. I gave him the answer. He asked for the names. I gave him the names.

He said two of them out loud as though tasting them — Priya Iyer's name, and Wanjiru Kamau's. He held the second one for a beat. I asked him whether he had read their work. He said he had read all of Priya's published work on schema migration and had been a reader of Wanjiru's standards-body filings since 2023. He said it without performance and without elaboration. He had read the team I had picked before I had told him who was on it.

I noted that, too. The two names he held that morning are the two names that will, eleven months later, register on the rack-power log and the survey-line ledger. The architect was reading the survey lead and the chemist before they sat in the same wardroom with him. I did not know then what the reading was. I know now.

His third question was the one I had been waiting for, because it is the question every architect should ask and most do not.

He said: *The architecture has not been deployed in a production environment under sustained partition with a crew whose lives depend on it. You're asking me to be on board the first time it is.*

He said it without inflecting it as a question. He had named the thing the call had been built around without naming it directly until that moment, and he had named it in the form of the offer rather than in the form of the objection.

I said: *Yes.*

I let the *yes* stand. The architecture's claim under sustained partition was a claim that had not been deployed; my mother's hospital admission was a fact that had been; the consortium's funding cycle was a window that would close; the crew's lives were a load the architecture had not yet carried. All of those facts had been mine before the call. They were now also his.

He thought for about four seconds. He nodded once. He said: *Yes.*

That was the recruitment. There was paperwork after, and a follow-up call to formalize the appointment. None of that mattered. The recruitment had happened in the four seconds between my *yes* and his *yes*, and the substance of the recruitment had happened in the four sentences he had said when I asked him what he did the night the BLOCK landed.

I closed the laptop. I sat in my office for a while. I was not thinking, exactly. I was registering that the trust I had been waiting five years to extend had a person attached to it now. The registration took the rest of the afternoon.

I ate the second half of the *vatrushka* at 17:04.

I called my mother that evening. She was, by then, six months past the stroke. She could speak in short sentences. She could find the words for *yes* and *no* and *the building across from my flat,* and she could not find the words for the comparisons that had been the structure of every prior conversation she and I had had. I had been telling myself, for months, that the absence of the comparisons was a kind of grief and not a kind of relief. I had been telling myself this because the alternative felt disloyal, and because the loyalty I owed her had outlasted the speech she had used to demand it. I told her about the bakery near the office that had changed its hours. She told me about the building across from her flat that the city had finally repainted. We talked about nothing of consequence for forty-five minutes. The MERIDIAN-7 was twelve months from departure. I had time to tell her later. I have told her since. She has, since I told her, said the words *I am glad* twice. Twice is what she has been able to give me. I have accepted it.

I called my brother in Voronezh afterward. Diana was four. She came on the line and told me, with the seriousness of a child who has just discovered the word, that the moon had been *exactly the same shape* two nights in a row, which she had confirmed by going to the window each night and looking. I told her that this was a careful observation and that the next time it changed shape she should write down what it changed to. She said she would. I sent a postcard to Voronezh the next morning from the bakery near the office. The postcard had a photograph of a *vatrushka* on the front. I wrote on the back: *Watch the moon. — Auntie.* I did not, in the postcard, mention that I had selected an architect that afternoon. The postcards I send Diana are not about my afternoons. They are about hers.

---

I am back on the boat now. It is Day 14. The tea is cold. The watch I am not standing is Diego's; the boat is humming the way the boat hums under ice — the steady-state hum, not the one with anything in it.

The architecture has been holding. The local store answers every query without ambiguity. The relay is dormant. The gossip protocol has correctly identified itself as dormant rather than as failing. The schema state is stable. The audit log is intact. The architecture is fine; the boat is fine; the man who built the architecture is fine.

None of that is why I am writing tonight.

I am writing because the architectural question was answered four years ago when Joel rewrote the lease protocol; the council's clearance answered it three years ago; my reading of the cleared rewrite answered it two years ago. What is answered tonight is the other question — the one he asked me on the call, the one I said yes to. *You're asking me to be on board the first time it is.* The architecture under the ice is the rewrite, deployed. The proof is happening.

That is why it was him. Tonight, when I queried the local store and it answered me locally because there was nothing else to answer with, the architecture's authority and the architect's discipline registered for me as the same property. They were always going to register that way. I had selected him so that they would.

Joel is two compartments aft, on the late shift at the data console, working a routine reconciliation pass with Wanjiru. He does not know I am writing this. He has not known for fourteen days. He knew the call was being recorded. He spoke into the record anyway.

He spoke into the record anyway. The architecture does the same — speaks into the record whether or not the consortium is listening. Tonight the boat is operating exactly as the rewrite specified, on Day 14 of an under-ice partition, and I am writing this and I will sign it.

Above my desk, taped to the bulkhead, Diana's most recent drawing has a moon in it. The moon is wearing a hat. I have not asked her to explain the hat.

I am going to bed.

— A. Y., Day 14, the *Nansen*
