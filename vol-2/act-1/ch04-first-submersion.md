---
title: "First Submersion"
volume: 2
act: 1
chapter: 4
mission-day: 7
icm-stage: icm/draft
word-count-target: 5000
log-opener-pattern: none
primary-rail: mission-as-survival
chapter-version: v1
plants-set:
  - relay-dormant-not-failing
  - partition-loss-case
  - wanjiru-audit-log-design
  - acoustic-mesh-8-percent-faster
plants-paid:
  - wanjiru-attestation-as-discipline
---


<!-- Anna-voice rewrite pass 2026-05-16 (PAO). Bigram-anaphora cascades 16→1 (3× "Each of them" / 4× "The relay layer is" / 3× "They do not log" / 3× "I had asked"); tautological self-equation 7→0 (incl. 3× "The floor was the floor" pile-up); echo-and-confirm 10→2; self_referential_frame 3→1 (galley yellow→green); motif trims ("the morning of Day X" 9→4; "the relay layer is" 7→2; "oh-eight-thirty-seven" 7→4). -->
<!-- Council Tier 2a pass 2026-05-22 (PAO). Restructured per beta-reader finding: the 5,000-word conference-room walkthrough was the named abandonment cliff. Interleaved the architecture exposition with the live descent — Anna in the engineering compartment from 0825 onward, Joel at his rack with the relay-layer + gossip-protocol screens visible, bridge intercom carrying depth callouts. The architecture's transition through active → out_of_contact → dormant happens ON SCREEN as Joel narrates it. Joel's load-bearing dialog preserved verbatim (especially the "dormant — anything else would be a lie" passage); the conference-space frame replaced with engineering-compartment-at-the-rack frame. The descent has prose-time tension because the architecture is being exercised live. Word-count net: ~5300 (was 5090; ~+200 from interleave prose). -->

I went to the engineering compartment at oh-eight-twenty-five.

Joel was at the architecture rack on the port side. He had his rolling stool pulled up to the secondary console, a tablet at his left hand, the printed copy of the council review he had carried since the recruitment call open at his right, and the coffee he drinks when the coffee is for the work. The relay-layer status panel was up on the secondary screen. The gossip protocol's dual-carrier display was up on the primary. He had laid them out the way a man lays out his tools when he expects to need both of them in the next ten minutes and wants them within glance-range without turning his head.

He looked up when I came in.

He said: *Director.*

I said: *Joel. The dive starts in twelve minutes. I want to watch what happens to the architecture from here.*

He nodded. He did not ask why. He moved the stool over half a meter so that I could see both screens without standing in front of him, and reached behind the rack for a second stool against the bulkhead, which he set down where his own had been. He sat back at the new angle. The two screens were between us now. The architecture was between us. He waited.

I sat.

I had been thinking, for the half hour between the morning brief and the engineering compartment, about what kind of question I was about to ask. The question was not the kind I had asked him during the recruitment. Back then I had wanted to know what kind of man he was. On the boat at depth I needed to know what the architecture was doing. The two were not the same question and would not be answered the same way. The recruitment had turned on five sentences. The next hour was going to take longer than five sentences.

I said: *Walk me through what is about to change.*

He took a breath. He set the coffee down at his right hand. He answered.

*The boat's nodes are running in dual-carrier mode right now. The radio relay is the primary path; the acoustic mesh is the secondary, on standby at zero traffic. Every write is going to both carriers, with the radio carrying the consortium-port-side gossip and the acoustic carrying the local mesh. When the dive sequence starts, the radio link is going to thin out as the antenna mast retracts. At about ten meters of depth it goes out of contact. The relay layer notices the out-of-contact condition and switches state from* active *to* dormant. *The gossip protocol on the consortium-port side picks up the* dormant *flag and queues outbound writes against it. The local-mesh side continues running on the acoustic carrier. No data is lost. No state is corrupted. The architecture transitions to under-ice operation on its own clock, against the protocol the rehearsal on Day 6 walked through.*

He said it in six sentences. He said them the way he had said the four sentences on the recruitment call about the lease protocol. The cadence was the same. He did not soften any of the six. He did not preface; he did not stage; he did not build. He named what was about to be true.

I said: *Walk me through each one. Slowly. While it happens.*

I had decided to ask him slowly. The fourteen days ahead would not survive without my having asked the question slowly now, while the architecture was still about to be exercised at depth for the first time on real systems and while Joel still had the cognitive room to walk me through it. I would not get the time again. I was taking it now.

He nodded. He turned his attention to the secondary screen.

---

At oh-eight-thirty-seven the *Nansen* passed below the surface.

The bridge intercom carried the master's call into the engineering compartment at the standing volume Sabina had set for the dive-sequence channel: *bridge, dive sequence at oh-eight-thirty-seven; pumps cycling; trim adjustment in progress.* The deck plates under my boots took on the angle of a vessel ceasing to be a surface vessel and becoming a different kind of vessel. The compartment's overhead light cycle had not changed. The compartment's hum changed: the secondary recirculation came up at the rate the manual specified for sub-surface operation. The mineral trace the boat's scrubbers left in every enclosed space at depth thickened, slightly, in the air at the back of the rack.

The other transition the dive was running was the one Diego was reading off his polar-operations console two compartments aft. The bridge had GPS until the sail submerged. After that the position the boat thought it was at was a position Diego was going to compose. He had been at the polar-operations console since oh-five-thirty, taking the last surface fix into the integration ledger as the dead-reckoning seed — the position the doppler velocity log and the gyrocompass would integrate forward from for the duration of the segment. The consortium's transponder survey from the prior season had laid down nine pairs along the routing; Diego had memorised the sequence in the order the boat would meet them. The bathymetric chart was loaded on his tertiary at the September survey resolution. The chart and the DVL and the gyro were the three things the boat now navigated on. The transponders, when the boat reached them, would correct what the three things had drifted on. I noted that Diego's work was running in parallel to the work on the screen between Joel and me, on its own clock, in its own register, on a different set of consoles two compartments aft.

On Joel's secondary screen the relay-layer status panel was at *active.*

He said: *the antenna is retracting. The boat is at about three meters and descending. The radio link is at the marginal signal-to-noise threshold. The relay layer is still reading* active.

The status line on the screen did not change.

At about a meter past ten the line changed.

*active → out_of_contact* the panel said. The flag was yellow against the panel's standard background. The duration field next to it appeared at 00:00:00 and began incrementing.

Joel said: *the radio is gone. The layer is reading* out_of_contact. *That is a transient state. The protocol waits the configured threshold — sixty seconds — to determine whether the loss is intermittent or persistent. If the radio comes back inside sixty seconds, the layer returns to* active *and resumes. If it does not come back, the layer transitions to* dormant.

The compartment continued to settle. The bridge intercom carried: *fifty meters. Trim holding. Pumps nominal.*

I said: *what does* out_of_contact *do that* dormant *does not do.*

*It keeps the radio-side connection-state machinery in retry-active. Sockets stay half-open. The push queue stays at the boundary, waiting. The layer is not pushing, but the layer also has not committed to* not *pushing.* Dormant *is the commitment. The commitment matters because the gossip protocol on the consortium-port side reads the relay-layer state and decides what to do with outbound writes based on it. While the layer is* out_of_contact *the protocol holds the writes at the relay's edge.* Dormant *moves them to the per-laptop queue.*

I said: *and the difference shows up where.*

*In the audit log. The* out_of_contact *period gets logged as a transient. The* dormant *period gets logged as the operational mode for the duration of the segment. The two are different facts about the same physical reality and the architecture refuses to confuse them.*

The bridge intercom carried: *one hundred meters. Acoustic carrier acquired at the threshold.* The deck officer had not waited for the relay-layer transition to confirm the acoustic mesh; the acoustic console on the bridge ran its own pickup.

On the gossip-protocol primary screen, the local-mesh channel had been quiet against the dual-carrier mode — no writes had needed the acoustic-only path while the radio was up. At one hundred meters the channel lit. The first local-mesh broadcast was visible on the screen: a write-identifier, no payload. A second appeared two seconds later, then a third. The acoustic mesh was finding its rhythm.

Joel said: *the acoustic carrier is up. The local-mesh side of the gossip protocol is broadcasting at the carrier's tempo. Every write on every node is propagating to every other node on the boat. Inward service is active.*

The bridge intercom: *one fifty meters. Trim holding. No anomalous readings.*

At one fifty I noticed I was no longer hearing the wind.

The wind had been part of the boat's audible texture since Punta Arenas. I had taken it in on the rail at six on the morning of Day 0 and at the bridge wing on Day 2 in the Drake and at the marginal zone an hour and a half before the dive. The wind had been a continuous low signal under every other signal the boat made. At one fifty meters of depth the wind was no longer a signal. What replaced it was the boat's own sound — pumps, fans, recirculation, the structural pressure-load redistribution a hull makes when the hull's geometry is being asked to hold a column of ocean above it.

I noted the substitution. I did not name it aloud.

At a moment between one fifty and two hundred the relay-layer status panel changed again.

*out_of_contact → dormant* the panel said. The line went grey. The duration field reset to 00:00:00 and began incrementing.

Joel said: *the sixty seconds expired. The layer has committed. The radio is not coming back at this depth. The protocol now reads* dormant *from the layer. The push queue moved to the per-laptop. Outward service is correctly identified as waiting on the absent transport.*

I said: *dormant — name it for me.*

He set the coffee down again. He had picked it up between the previous answer and this one. The set-down was deliberate.

*The relay layer is not failing. It is not crashed. It is not hung. It is in the operational state the protocol designed for the case where there is no peer to talk to. The state is named, logged, and carries a duration field that increments while we are at depth. It is what the architecture is supposed to do when it cannot reach the consortium. Not a fault condition. An operational mode.*

He paused. He added the sentence I would write down later as the load-bearing piece of the morning's exchange.

*The architecture refuses to manufacture the appearance of mesh participation when no peer is reachable. The relay logs* dormant. *Not* retrying. *Not* intermittent. *Not* degraded. Dormant *is what the layer is. Anything else would be a lie the architecture refuses to tell.*

I said: *acknowledged.*

I had asked him the same question once before, on the recruitment call, in different words — about cloud telemetry that decided to stop responding without telling him first. He had answered with *the gauge in front of you*. The answer this morning was the same answer in a different room. The relay layer was a gauge that did not pretend to read what it could not read. The gossip protocol was a gauge that did read what it could read. The architecture was the discipline that distinguished the two and labelled each correctly.

The bridge intercom: *two hundred meters. Acoustic mesh at full capacity. Gossip protocol within rehearsal envelope.*

I had needed to verify the discipline at depth. The discipline was on the screen in front of me. I had verified it.

The bridge intercom: *two fifty meters. Trim holding.*

The dive continued.

---

*The local store.*

He named it first because it was the thing the architecture stood on. Every other property of the architecture was a property the local store enabled.

*Every node on the boat has a local store. Yours, mine, Wanjiru's, Priya's, Hiroshi's, Sabina's, Diego's, Maria's, the boat's compute hub. Each is the same kind of database, holding the same data discipline - attests at capture, hash-chains, signs every write with the author's keys. On the surface the local stores are propagating to each other through the gossip protocol, and to the consortium through the relay layer. Under the ice they are propagating to each other on the acoustic-only mesh, and not propagating to the consortium because it is not reachable.*

I said: *the gossip protocol on the acoustic mesh - that is operating right now.*

*Yes. It came up at oh-eight-thirty-seven when the radio relay went out of contact. The acoustic carrier is the only carrier we have at depth. The mesh is operating across it. Every write on every node is propagating to every other node on the boat at the carrier's tempo, which is slower than the radio relay and runs a different error profile, but is operating to specification. The rehearsal we ran on Day 6 demonstrated the carrier's behavior matches the protocol's expectation. We are inside the rehearsal's envelope.*

I said: *a write that you make right now - what happens to it.*

*It lands on my local store first. It signs at capture. It chains into my local hash chain. The gossip protocol picks it up on the next cycle. The cycle is one minute on the acoustic carrier, give or take ten seconds depending on what the boat is doing. The protocol broadcasts the write's identifier, not the payload. Nodes that don't have the write request the payload. The payload propagates. By the third or fourth cycle every other node on the boat has the write in their local store.*

I said: *the same write under partition with the relay layer up - what is different.*

*The relay layer would push the write to the consortium ports on its own cadence. The push is a separate code path from the gossip protocol; the protocol moves writes between nodes in the local mesh, the relay layer moves them out to the consortium. Same write. Different transport. The relay layer is a service that propagates outward; the gossip protocol is a service that propagates within. Right now the inward service is running and the outward service is dormant.*

He said *dormant* deliberately. He had said it in the four-sentence answer when I asked the first question. He had said it again now. I noted the repetition.

I said: *dormant - name it for me.*

He set the coffee down again. He had picked it up between the previous answer and this one. The set-down was deliberate.

*The relay layer is not failing. It is not crashed. It is not hung. It is in the operational state the protocol designed for the case where there is no peer to talk to. The state is named, logged, and carries a duration field that increments while we are at depth. It is what the architecture is supposed to do when it cannot reach the consortium. Not a fault condition. An operational mode.*

He paused. He added the sentence I would write down later as the load-bearing piece of the morning's exchange.

*The architecture refuses to manufacture the appearance of mesh participation when no peer is reachable. The relay logs *dormant*. Not *retrying*. Not *intermittent*. Not *degraded*. *Dormant* is what the layer is. Anything else would be a lie the architecture refuses to tell.*

I said: *acknowledged.*

I had asked the same question once before, on the recruitment call, in different words - about cloud telemetry that decided to stop responding without telling him first. He had answered with *the gauge in front of you*. The answer this morning was the same answer in a different room. The relay layer was a gauge that did not pretend to read what it could not read. The gossip protocol was a gauge that did read what it could read. The architecture was the discipline that distinguished the two and labelled each correctly.

I had needed to verify the discipline at depth. I had verified it.

The engineering compartment held the air it had held since the dive completed — pumps at the standing sub-surface cycle, the secondary recirculation at the manual's specified rate, the mineral trace at the back of the rack thicker than it had been at the surface. Joel's coffee sat at his right hand where he had set it down; it had been there since the dive sequence started and I had not watched it go cold, only noticed, now, that it had. The tea I had carried in from the wardroom and set on the second stool was in the same condition.

I moved to the next question.

---

*The gossip protocol.*

I said: *you said the gossip protocol has correctly identified itself as dormant on the consortium-port side. Walk me through that.*

Joel paused for the first time of the morning. The pause was not nervousness. The pause was the half-second of a man deciding how much of the topology to lay out before he answered.

He said: *the gossip protocol has two sides. There is the side that runs between the boat's nodes - the local mesh, on the acoustic carrier, what we have just discussed. That side is active. There is also the side that runs between the boat's mesh and the consortium ports. The second side is what carries our writes, after the relay layer pushes them, into the consortium's gossip mesh on the surface. The two are paired but distinct. The local mesh runs on whatever carrier is available locally. The consortium-port side runs over the relay layer, on whichever physical link is up.*

*The consortium-port side cannot run right now. Not because the protocol is broken. Because the relay layer is dormant. The protocol queries the layer for a usable path; the layer returns dormant; the protocol writes a status line that says it has been told dormant and that it will retry on the next status change. That is all it does. It does not retry on its own clock, exponentially back off, or synthesize a fictional path. It waits for the layer to come back, which it will do when we surface on Day 21.*

He looked at me through the table light. *The protocol is not failing. It is correctly identifying itself as dormant on the consortium-port side. If you query its state right now it will tell you that. If you ask it to push something it will queue the something against the dormant state. When the relay layer announces it has come back, the protocol will dequeue and resume. That is all that will happen.*

I said: *queued writes - where do they live.*

*Local store. Same place every other write lives. The queue is not a separate database. The queue is a flag the protocol attaches to writes whose propagation status is *not yet propagated outward*. The flag does not change the write. The write is the same write. The flag is metadata the protocol keeps so it knows what to push when push is possible.*

I said: *and a write made under partition that the consortium has never seen - when we surface, what does the consortium see.*

*The consortium sees the write. The protocol pushes it. The hash chain attests when the write was created - it carries the attestation from oh-nine-thirty-seven on Day 7 or whenever it was made. The propagation timestamp is separate from the creation timestamp. The consortium learns, at oh-eight-thirty-seven on Day 21, about a write that was made at oh-nine-thirty-seven on Day 7. The fourteen-day gap is visible in the metadata. The architecture does not pretend the gap is not there. The gap is the partition's signature on the record.*

I noted the phrase. I had not heard him use it before. I logged it.

*The architecture is honest about what it has and about what it does not have, including itself,* he said. *That is the discipline. Under partition we do not have the consortium. The architecture does not pretend we do. Under partition we have the boat. The architecture works on what it has.*

I said: *acknowledged.*

The two answers - the relay layer's dormancy and the gossip protocol's dormancy on the consortium-port side - were the same answer in different vocabularies. I had asked them as two questions because I had wanted to know whether Joel would distinguish them. He had distinguished them. The relay layer was the transport. The gossip protocol was the mesh that ran on top of the transport. The transport was dormant. The mesh that ran on top of the transport had taken the dormancy in and waited. Two layers; two acknowledgements of the same fact; both correct.

I had needed to verify the layering at depth. I had verified it.

---

There was a knock at the engineering-compartment hatch. I said: *enter.* Priya came through. She had her tablet in her left hand. She acknowledged Joel at the rack with a half-nod and addressed me directly.

*Director. The schema state checked at the dive transition. Every author's local copy carries the same schema version. The version handshake completed on the acoustic mesh during the seven minutes of the dive sequence. There is no migration scheduled for the segment. The schema is stable. I wanted you to have the confirmation before the morning brief.*

I said: *acknowledged. The handshake completed cleanly.*

*Cleanly. No drift. No deferred upcasters. No outstanding lens registrations. The schema we left the surface with is the schema we are operating on at depth. If anything in the segment changes the schema state, you and Joel will hear it from me before it reaches anyone else.*

She said it in the clipped tone she used when the report was already in her body. I had marked that tone on Day 5 in the lab during the fourth pass. It had not changed. She was not at the lab now; she was at the engineering-compartment hatch on the morning of Day 7; the discipline was the same discipline. She had brought the schema-state confirmation because the dive transition was a thing the schema state could have failed at and had not failed at, and she had verified the not-failing on her own clock and was filing the verification with me before she went back to whatever the next thing on her list was.

I noted the verification. I noted the filing.

She nodded once to Joel. He nodded back. She closed the hatch behind her.

Joel said: *Priya is the migration we are not running today.*

He said it as a fact about the morning's operational state. He said it without elaboration. I logged it the way I had logged Diego's *the boat is good* on the rail at Punta Arenas and Wanjiru's *the handoff is good, Director* at the comm space that same morning. The same kind of sentence. The same kind of bearing. The third such sentence I had collected, on a boat that had just gone under the ice.

---

I said: *the audit log.*

Joel had the answer ready. He had been waiting for me to ask.

*Every write attests at capture. The attestation includes who signed, what they signed, what schema version they signed against, and a hash that chains into the prior write on that author's chain. The chains are per-author. The chains are independent. They cross-attest through the gossip protocol - when my write is propagated to your node, your node receives it as an attested write from me, and your local store records the receipt with its own timestamp and its own counter-signature. The counter-signature is not a re-attestation of my write. The counter-signature is your node's record of having seen my write at that moment. The two are different.*

*Under partition the counter-signatures from the consortium ports are not happening, because those ports are not seeing our writes. The counter-signatures from the boat's nodes are happening on the local mesh. Every write made on the boat is being seen by every other node within the gossip protocol's cycle window. The audit log on each node carries the cross-attestation set for the local mesh. It does not carry the cross-attestation from the consortium because the consortium is dormant. When we surface, its counter-signatures will be retroactively attached to the writes it acknowledges. The write itself will not change. The audit metadata will accumulate a new layer.*

I said: *Wanjiru.*

He nodded. *Wanjiru's design. The audit-log discipline at the layer where the consortium's counter-signatures land is hers. The discipline at the layer where the boat's nodes counter-sign is mine, but the design that makes both layers compose into a single coherent record is hers. She designed the audit log to preserve provenance through partition transitions. Whatever is in the log right now will be in the log at oh-eight-thirty-seven on Day 21 when we surface, with the additional layer from the consortium attaching cleanly over the top. The log does not lose the partition. The log does not flatten the timestamps. The log keeps every layer of every signature in the order each layer arrived.*

I said: *acknowledged.*

This was the moment in the morning's exchange where Wanjiru's hand on the architecture became visible to me at the level the design lived at. I had taken her measure on Day 0 at the comm space when she had walked me through the keys. I had logged her on Day 4 at the rail when she had installed the surface-state baseline. I had caught her, again, in Joel's mouth on the morning of Day 7, in the engineering compartment at three hundred meters, when he had named the audit-log discipline as hers. The architecture had multiple authors. Joel had written the paper. Wanjiru had built the parts of the architecture that turned the paper's claim into the operational record I was about to spend fourteen days under the ice extending into. I had hired both of them. I had not, until this morning, fully understood that I had hired both of them for the same reason.

I turned my attention back to Joel. He was waiting.

---

I had two more questions. I had decided which two on the bridge during the dive sequence. The first was about the failure modes the partition introduced. The second was about Joel.

I asked the first.

*What does the architecture not do under partition.*

He paused. The pause was longer than the previous pauses. He had not pre-loaded the answer. He had been answering questions about what the architecture did. The question about what it did not do required a different kind of answer.

He said: *the architecture does not produce mesh-wide consensus under partition. It cannot. It is not allowed to. There is no protocol that produces consensus across nodes that cannot reach each other; there is no architecture that can produce one without lying. Under partition, the boat's mesh is a self-contained mesh. The boat's mesh has its own consensus, which is local to the boat. The consortium's mesh has its own consensus, which is local to the consortium. The two will reconcile when we surface. They are not reconciled now. Anyone who tells you the two are reconciled now is lying.*

He said it without raising the altitude. He said it the way he had said *I missed it* on the recruitment call, which was the way a man names a constraint without staging it.

*The architecture also does not produce, under partition, the ability for the consortium to see what we are doing. The consortium does not know we have written this morning's brief. The consortium does not know we have countersigned the dive entry. The consortium does not know Priya verified the schema. The consortium will know all of those things at oh-eight-thirty-seven on Day 21. Until then the writes exist on the boat and only on the boat. If the boat is lost, the writes are lost. The architecture does not have a third party to fall back on for the duration of the segment. The boat is the only third party.*

I said: *acknowledged.*

I had wanted him to name the loss case. I had wanted him to name it without staging. He had named it. The boat at three hundred meters held the writes. The writes existed. Whether they would continue to exist depended on whether the boat surfaced. The architecture did not pretend otherwise. I had needed to verify, at depth, that the architecture's honesty extended to its own loss case. I had verified it.

I asked the second question.

*Joel - is anything different at depth from what you expected.*

He thought for some seconds.

He said: *the acoustic mesh is propagating slightly faster than the rehearsal predicted. By about eight percent on the cycle window. I want to watch it for a day before I report anything formal. The acoustic floor is also slightly cleaner than Diego said it would be at the marginal zone, but we are below the marginal zone now. The carrier under sustained ice is going to be different from the carrier at the edge. Both are observations, not concerns. I will know more by Day 9.*

He said it the way an engineer reports observations to a Mission Director who has asked a question whose answer might or might not exist. He had not over-claimed. He had not under-claimed. He had said what he had observed and what he had not yet observed and when he would have more to say.

I said: *acknowledged.*

I added: *I will hear more on Day 9.*

He nodded. He closed the notebook he had not opened.

We had been at the rack for an hour and forty-five minutes, counting from the moment I sat down twelve minutes before the dive.

---

I did not end the meeting immediately. I sat with the bench and the closed notebook and the coffee that was no longer hot, and I let the architecture's morning settle in my mind in the order I had received it.

The local store on every node, operating in partition mode, attesting every write at capture, propagating to the local mesh on the acoustic carrier. The relay layer dormant - not failing; dormant; the operational state the protocol named for the case where there was no consortium to talk to. The gossip protocol's two sides - the local-mesh side active, the consortium-port side correctly identified as waiting on the dormant relay layer. The audit log carrying cross-attestation across the local mesh, accumulating a partition layer that would compose cleanly with the consortium's layer at surface. The schema stable.

I had needed to install all of those things in my own head this morning. The reason was that the segment ahead would not let me ask Joel to walk through them again at this altitude. The morning was the window. The engineering compartment was the room. The dive itself was the demonstration. Only this morning, with the architecture transitioning live on the screen between us, could carry these questions without competing with the next operational concern.

I had asked them. He had answered them. The answers had landed.

I was going to use the answers, in the days ahead, as the floor under every operational decision the boat would make under the ice. It was the floor I had read in his paper four times - the one the council had cleared with fifteen conditions and no hold on the lease layer in Round Two; the one I had spent the morning, at the rack in the engineering compartment, watching transition through itself live while asking him to walk me through it in the language the boat would need it in. It would carry. It was carrying. The boat under my feet was at depth on it.

He picked up the coffee. He drank what was left of it. He stood. He said: *Director.*

I said: *Joel.*

He left.

---

I went forward through the wardroom. Wanjiru was at her station in the comm space, the way she had been on Day 4 at the rail and on Day 0 at the bench when she had handed me the keys. She had the audit-log dashboard up on her primary screen. She had the relay-layer status panel up on her secondary, with the *dormant* state line printed across it in the level grey the architecture used for operational states that were not faults. The duration field next to *dormant* read 0d 01h 24m and was incrementing.

She was humming. The hum was the same Kikuyu fragment. The tempo was unchanged.

She said: *Director.*

I said: *the audit log.*

*Operating to specification. Every write since oh-eight-thirty-seven has cross-attested across the local mesh within the gossip protocol's cycle window. No drops. No retries against missing peers. The dormant flag on the relay layer propagated correctly to the audit log's status panel. The log is not lying about what it has and what it does not have.*

I said: *acknowledged.*

She turned to face her console. The hum resumed. She did not say anything else.

I thought, going back through the wardroom, that Wanjiru's *the log is not lying* was the same sentence Joel had said at the engineering rack about the architecture's refusal to lie. The architecture and the comm officer who carried it were saying the same thing in the same kind of voice. I had hired both of them. I had hired them for the same reason.

I went forward to the bridge.

---

The boat's master was at the wheel. The deck officer was at the dive station. The pumps had not cycled since the dive sequence ended. The trim held. The instrument panel registered three hundred meters of depth, the bottom contour of the under-ice routing as Diego had pre-marked it on the chart, the carrier-acoustic floor under sustained ice at the level Joel had said it would be at by Day 9 if the day-9 observation held.

The polar-operations panel on the inboard bulkhead carried the position the boat believed it was at, in a small triple of numbers Diego maintained: the dead-reckoned position from the DVL and the gyro since the dive seed; the acoustic-triangulated position against the first transponder pair the boat had picked up an hour earlier; and the bathymetric match against the chart, computed by laying the boat's downward sonar reading against the September survey at the resolution the survey supported. The triple was three numbers because no one of them could be the position by itself. The dead-reckoning drifted. The transponders covered some segments of the routing and not others. The bathymetric match read where the chart had been read; the floor under the boat had moved nothing since September and the ice above had moved four metres a day since the chart's survey and the boat had to know which to honour and which not. The three numbers, when Diego had them all to compose, were within a hundred metres of each other on a routing six hundred kilometres long. The position the boat believed it was at was the position three different instruments said it was at, none of which were lying about which one of them they were.

I gave the master the nod I had given seventeen masters at seventeen sailings.

He acknowledged.

I went to the bridge cap's inboard port and looked at the colour of the water that was not water, that was the colour the water turns when the water is above you, with the marginal zone now on the surface I could not see and the southern continent beyond the marginal zone and the consortium ports somewhere beyond the continent and the relay layer dormant and the gossip protocol on the acoustic carrier doing what the gossip protocol on the acoustic carrier was supposed to do.

The architecture was operating. The crew was where the crew should be. The boat was where the boat should be. This morning was the one the segment would be measured against.

I noted it.

I went below.
