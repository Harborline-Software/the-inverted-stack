---
title: "Subsystem Test — Sync Daemon Under Drift"
volume: 2
act: 2
chapter: 9
mission-day: 30
icm-stage: icm/draft
word-count-target: 6000
log-opener-pattern: B
primary-rail: career-cost-and-aging-out
chapter-version: v1
---

Mission log, Day 30, 0612 local. RV Nansen, MERIDIAN-7. Routine watch.

The boat held trim at three hundred meters through the night. Relay layer dormant per architecture specification; gossip protocol on the consortium-port side dormant; local mesh active and within drift bounds across all crew nodes. Anchor's anomaly-detection layer flagged a sync-daemon drift event at 0247 local on the boat-internal mesh — a pre-threshold signature on the cross-node clock-skew indicator that the local-store anomaly model surfaced approximately ninety seconds before the threshold-trip would have fired. Reyes pulled to the comm-space console at 0249. Yusupova on the bridge for handoff at 0612. Drift event under investigation; no operational impact registered against the boat; no carryover for the bridge watch beyond observation. Schema state stable per Iyer's 0214 confirmation. Relay status unchanged.

— A.Y., Mission Director.

---

I came down from the bridge at oh-six-twenty after the deck officer had finished the morning brief. The wardroom hum was the wardroom hum. The galley was at the start of its breakfast cycle. Maria's coffee had been on the warmer for twelve minutes. I poured a cup of it and took it forward through the wardroom and across the main passageway and into the comm space, where Joel was at the secondary console with two displays open and a notebook open on the bench beside the keyboard.

He had been at the console since oh-two-forty-nine. Three hours and thirty-one minutes. The notebook had three quarters of a page of his hand on it and a small column of timestamps in the left margin in the discipline he kept timestamps in. He looked up when I came in. He nodded.

He said: *Director.*

I said: *Joel.*

I set the coffee on the bench at the corner of the console where it would not be in his hand's path to the keyboard. He registered the coffee. He registered that I had not put it under his face, where I would have been suggesting he stop and drink it. He registered that I had put it where he could reach for it when he had a place to stop.

I said: *the drift event.*

He said: *not a fault. Not yet. Possibly not at all. The local-store model on Anchor flagged the cross-node clock-skew indicator at oh-two-forty-seven. The signature was ninety seconds ahead of where the threshold-trip would have fired. I came to the console at oh-two-forty-nine. The drift has not exceeded the threshold in the three and a half hours since. The drift's shape is consistent with a bounded oscillation rather than a runaway. I am working on which.*

He said it in the tempo Joel said operational reports in. The tempo had been the same tempo at the conference space on the morning of Day 7 and at the wardroom desk on the night of Day 22 and at the bench in the second-submersion brief on the morning of Day 23. The fatigue at oh-six-twenty on Day 30 was the fatigue of an engineer who had been at a console for three and a half hours; the substance of the report was not the fatigue.

I said: *walk it.*

He said: *I will need a few minutes.*

I said: *I have the time.*

I sat at the bench across the comm space from him. I did not sit at his shoulder; the work was his. I drank a third of the coffee. I waited for him to organize what he was going to say.

---

He turned the secondary display so that the angle came across the comm space at the bench where I was sitting. The display carried a graph in two colours. The first colour was a flat band the model had identified as the routine clock-skew baseline across the boat's mesh — the band the gossip protocol's clock-handshake produces when the nodes are healthy. The second colour was the actual clock-skew across the boat's nodes for the past seventy-two hours, sampled at the protocol's gossip-cycle tempo. The actual band was, for most of the seventy-two hours, the same shape as the baseline band. At approximately oh-one-fifty on the morning of Day 30, the actual band had begun to drift away from the baseline, slowly, in a pattern that bowed up from the baseline by a small margin and then bowed back down.

Joel said: *the bow is the drift event. The model flagged the upward leg of the first bow. The bow then completed and started to subside, which is the part of the signature that the threshold-trip would not have caught — the signature looks more like an oscillation than a divergence. It looks like a drift the architecture was built to absorb without reporting.*

I said: *if it was built to absorb without reporting, why did the model flag it.*

He said: *because the model is more conservative than the protocol. The protocol's threshold is set to where the architecture cannot self-correct. The model flags earlier — at the level the local-store builds its own pattern of routine and notices when the routine starts to bend. The model is doing what the model was built to do. The protocol is doing what the protocol was built to do. The two are operating at different altitudes; the model sees a precursor that the protocol does not yet see.*

I said: *acknowledged.*

I let him take the next step.

He said: *the question is whether the bow is going to repeat. If it is going to repeat, we have an oscillation in the gossip protocol's clock-handshake under sustained partition. If it is not going to repeat, we have a transient that the architecture has already absorbed and the model is going to learn was not a fault. The architecture's specification covers the case in either direction. The protocol has been written to absorb sustained network drift without manual intervention. The model's flag is not a request that I intervene; it is a request that I observe.*

He said it without softening. He had not been waiting for me to draw the conclusion he was offering; he was naming the operating state he had already determined the architecture was in. The model had flagged. He had observed. The protocol was self-correcting against the drift inside the protocol's specification. The drift was, to the protocol, an exercise. The protocol was passing the exercise.

I said: *what would you do if the bow repeats.*

He said: *nothing immediately. The protocol's first response to a repeating oscillation is to broaden the gossip-cycle window — the handshake gets a longer interval to settle. The architecture does that on its own. If broadening the window does not damp the oscillation across two cycles, the protocol falls back to a slower handshake mode that trades latency for stability. The architecture also does that on its own. I would intervene only if both fallbacks failed and the drift began to widen rather than damp.*

I said: *and would you log the intervention.*

He said: *I would log it whether I intervened or not. The discipline is to log the operational state regardless of whether the state required action. The fact that the architecture handled the drift without me touching it is a part of the operational record. The protocol's specification has now been exercised against a real mid-mission drift event. The exercise is the verification.*

He turned the display back square to himself. He took a swallow from the coffee mug at his right hand — the coffee he had brought at oh-two-fifty, three hours and thirty minutes earlier, which had gone cold around oh-three-thirty and which he had been drinking cold since. He registered that the coffee I had set down at the corner of the bench was warmer than the cup in his hand. He did not switch.

I noted that. I did not comment.

He started keying. He pulled a tab on the secondary I had not yet seen — a longer-window view of the same indicator, going back across the entire mission. The band on this view was the bow at the right edge and a long tail of mostly-baseline behind it that went all the way back to the morning of Day 7.

He said, without looking up: *the protocol's broadening window came out of the council review. It was not in the original draft of the paper.*

I said: *acknowledged.*

He said: *the original draft had a single handshake interval. The interval was the interval. If the gossip-cycle handshake did not settle inside the interval, the protocol fell back to the slower mode immediately. There was no broadening between the two states. The council reviewer who looked at the protocol layer pointed out that the binary fallback was going to oscillate under the class of load profiles a real boat would carry. He did not name the boat. He named the class. I had not modelled the class. I sat with the comment for a week. I rewrote the section. The broadening window is what came out of the rewrite. The window absorbs the drift the binary fallback would have oscillated against.*

He said: *the rewrite is what is keeping the drift inside the protocol's self-correction this morning. If the rewrite had not happened, the bow would have triggered the fallback at oh-two-forty-seven and the boat would now be at the slower handshake mode for the next four hours. We would not be at a fault state; we would be at a degraded state. The degradation would be operational. The crew would have noticed.*

He said: *the council comment was the right comment. The reviewer was reading the protocol against the class of load profile a real boat carries. I had been reading the protocol against the abstract specification. The two readings produced different protocols. The reviewer's reading produced the better one.*

He stopped. He took a third swallow of the cold coffee.

He said: *I had registered the council's contribution to the architecture in the spec's acknowledgments. I had not until this morning registered the contribution operationally. The architecture is keeping the boat inside its self-correction specification this morning because of the broadening window. The broadening window is in the architecture because the council reviewer caught what I had missed. The architecture's behaviour this morning is the architecture's behaviour as the council made it.*

I said: *acknowledged.*

He turned back to the bow. He sat with the graph for some seconds. Then he opened a different tab — a configuration file in a long format that I did not parse from the bench across the comm space — and started keying notes into a margin field at the bottom of the tab. He worked at the keying for a minute. He stopped. He turned the display back to the bow.

---

Priya came into the comm space at oh-six-thirty-two.

She came through the hatch with the cycle-check tablet in her left hand and a paper notebook in her right and the satchel that lived at the wardroom desk over her shoulder. She had been at the wardroom desk before the Day 30 brief, running the schema-state confirmation she ran at oh-six on every morning of Segment 2, and she had finished the confirmation at oh-six-twenty-seven and had logged it at oh-six-twenty-nine, and now she had come through the comm space because the daily cycle's next item was an instrument-tier audit of the cross-node sync state and the audit ran from the comm-space console.

She saw Joel at the primary. She saw the secondary display open with the drift graph on it. She did not stop at the hatch; she came in. She set the tablet on the bench beside the secondary in the small clear space the layout allowed. She set the notebook on top of the tablet. She looked at the graph.

She said: *Joel.*

He said: *Priya.*

She said: *the cross-node skew. When did the model flag.*

He said: *oh-two-forty-seven. The bow started at approximately oh-one-fifty. The graph is the past seventy-two hours.*

She said: *acknowledged.*

She set her body the way Priya set her body when she was concentrating on a graph she had not yet reconciled with her own model of what the graph should be. Her shoulders were at the angle her shoulders went to when the work was the work. Her left hand moved to the bench and adjusted the tablet so that the tablet was square to her body — the angle she preferred for reading from the tablet under field conditions. The micro-gesture took half a second. She did not register having made it.

She looked at the graph for thirty-eight seconds.

She said: *the bow.*

Joel said: *the bow.*

She said: *which nodes.*

He said: *the secondary display has the per-node attribution one tab over.*

He clicked. The display refreshed to a per-node breakdown across the eleven nodes on the boat's mesh. The drift's contribution to the bow was distributed unevenly across the nodes. Two nodes — the secondary instrument-tier node at the polar-operations bench and the relay-hub node in the comm space — were carrying a larger portion of the bow's amplitude than the other nine. The other nine were near-baseline.

Priya said: *the instrument-tier node at polar-ops.*

He said: *one of the two largest contributors.*

She said: *I am running an instrument-tier sample-rate sweep on that node every four hours. The sweep last completed at oh-one-forty-eight.*

She said it as a statement of fact. She had not been performing the connection; she had been registering it. The sweep was her instrumentation discipline; the architecture's clock-skew indicator was Joel's protocol discipline; the two had not, until oh-one-forty-eight, intersected operationally on the boat.

Joel registered the connection. He turned and looked at her for the first time since she had come into the comm space.

He said: *the sweep.*

She said: *the sweep.*

He said: *the sweep contributes load to the node's processing during its run. The node is then catching up on its gossip-cycle handshake during the post-sweep window. The catch-up is what the bow's upward leg is.*

She said: *the bow's downward leg is the catch-up completing.*

He said: *yes.*

She said: *the bow does not represent a drift in the architecture. The bow represents the architecture absorbing a periodic load on one of the contributing nodes. The protocol is doing what the protocol said it would do.*

He said: *yes.*

He said it as a statement that closed the question. The drift event was not a drift event. The drift event was the architecture absorbing instrument-tier load on a node that ran a periodic sweep. The model had flagged the precursor of the absorption. The protocol's broadening of the handshake window across the post-sweep period was the absorption itself. The architecture had been doing what the architecture had been built to do. The model had been doing what the model had been built to do. Joel had been observing what he had been observing.

I noted the conversation. I did not interrupt.

Priya said: *the load profile on the polar-ops node will continue at four-hour cycle through Surface 2. The bow will repeat every four hours under the current cycle.*

Joel said: *acknowledged.*

She said: *if the bow's amplitude grows across cycles, the protocol's broadening window is going to start clipping the handshake's settle time on the cycles that overlap with the relay-hub node's other periodic tasks. Eventually the broadening will run out of headroom.*

Joel said: *acknowledged.*

He said it the second time at the same tempo as the first. He had registered Priya's observation. He had registered that the observation was a constraint on the protocol's self-correction capacity that he had not yet calculated. He had registered the calculation he now had to do. He had not softened.

I noted the second *acknowledged*. I noted the texture of it.

---

Priya said: *the cycle.*

She said it the way Priya said the third sentence in a piece of work she had organized in her head before she sat down. She had not been waiting for an opening; she had been holding the question until the question's moment was the moment it was. The moment was the comm space at oh-six-thirty-six on Day 30 with the graph on the display and Joel's *acknowledged* still in the air between them.

She said: *the four-hour sweep cycle was the cycle the lab calibration suite specified. The lab calibration suite specified four hours because the sweep's reference to the calibration baseline expires at four hours under the lab's environmental envelope. The lab's environmental envelope is not the boat's environmental envelope. The boat's compartment-temperature variability is narrower than the lab's. The reference baseline expires more slowly under the boat's envelope. I have data from the first three weeks of the mission that suggests the reference holds at six hours under the boat's actual envelope and probably at eight.*

She said: *if I stretch the cycle to six hours, the polar-ops node's gossip-cycle headroom doubles between sweeps. If I stretch to eight, it triples. The protocol's broadening window has more headroom against the relay-hub node's other periodic tasks. The drift's amplitude across cycles damps faster.*

She said: *I have not raised the cycle change because the cycle is the cycle in the calibration spec and I do not change a calibration cycle without a documented operational reason. The drift event is the documented operational reason.*

She said: *I would like to stretch to six. If six holds for forty-eight hours, I would like to stretch to eight.*

She finished. She set the notebook on the tablet. She set the tablet on the bench. She did not look at me. She looked at Joel.

Joel did not say anything for two seconds.

He said: *the sweep cycle.*

Priya said: *the sweep cycle.*

He said: *I had not thought of stretching it.*

He said it flat. He said it the way he had said *I missed it* on the recruitment call, which I had read in the transcript afterward, and the way he had said *the rewrite passed* in the wardroom on the night of Day 22, and the way he had said *the gauge in front of you* on the same night when he had been describing the discipline that ran through the architecture. He said it without softening. He said it without performing the registering of the gap; the gap was the gap, and the registering of it was the registering of it, and the saying was the saying of what he had registered.

He said: *the protocol's broadening window's headroom is a function of the load profile of the contributing nodes. I had calculated the headroom against the protocol's specification. I had not calculated it against the contributing nodes' actual load profiles, which are upstream of the protocol. The instrument-tier load profile is upstream of the protocol. Stretching the sweep cycle is upstream of the protocol. I had not put the upstream variable into the calculation. The calculation I would have run on the drift's amplitude across cycles was the calculation against the protocol's headroom. The calculation you are proposing is the calculation against the load profile that produces the demand on the headroom. They are different calculations. The one you are proposing is the better one for the operational case we are in.*

He stopped.

He said: *thank you.*

He said it once. He did not stage it. He did not soften it. He did not turn it into a procedural sentence that buried the gratitude inside the procedure. He said the word and let the word do what the word did.

Priya said: *acknowledged.*

She said it clipped. She said it the way she said *acknowledged* when an officer she respected had registered a question of hers in the form she had asked it in. She did not perform the not-being-flustered; she just was not flustered. She had brought the question. He had registered it. The question was the question.

I did not move at the bench.

I had been registering, while Priya had been speaking, the texture of what was happening in the comm space. The texture was not the texture of an instrumentation engineer correcting a senior architect. The texture was not the texture of a senior architect being corrected. The texture was the texture of two engineers working on a problem at the same altitude, with the constraints of the problem distributed across both of their disciplines, and the engineer who had seen the constraint nobody had yet calculated had named the constraint at the moment the constraint was the next thing the conversation needed.

I had hired Joel for the architecture. I had hired Priya for the instrumentation that ran on the architecture and for the schema migration that had been written into the architecture by her hand. I had registered, on the recruitment calls, that the architecture had been built by Joel and that the architecture had been improved by the council's review and by the contributors who had been working on it after the review and that Priya was one of the contributors who had improved it. I had not, on the recruitment calls, registered the texture of how the improvement happened. I had registered that the improvement had happened. I had not registered the *form* the improvement took.

The form was the form I was registering now. The form was an instrumentation engineer who had been running her own cycle on her own discipline noticing a constraint upstream of the protocol that the protocol's designer had not put into his calculation, and naming the constraint at the moment the constraint was operational, and offering the change to the cycle that absorbed the constraint, and the protocol's designer registering the absorption without defending the omission and saying *thank you* at the moment the registering needed to be said.

I had hired him for this. I had hired her for this. I had registered, in pre-mission, that I had hired both of them. I had not until oh-six-thirty-eight on Day 30 in the comm space registered the architectural fact that the architecture got better in their hands than it had been in his alone. I logged that. I did not log it on the bridge log. I logged it at the place where I logged the things that did not belong on the bridge log.

I drank the rest of the coffee. I set the cup down at the corner of the bench at the angle the cup had been at when I had set it down at the start.

---

Joel turned to the keyboard.

He said: *the cycle change.*

Priya said: *I will draft the calibration-cycle change in the form the architecture's audit log will accept. I will run the change as a configuration update to the polar-ops node only, with the boat-internal mesh receiving the update via the gossip-cycle on the standard tempo. Six hours initially. Forty-eight-hour observation window. If the bow's amplitude damps across the window, I will draft the eight-hour extension.*

He said: *the protocol's broadening window will register the change as a load-profile shift on the polar-ops node within four hours of the configuration update propagating. The shift will appear in the model as a flatter baseline. The model will adjust its threshold within the next hour. The model will then no longer flag the post-sweep handshake catch-up as a precursor.*

Priya said: *the model will be doing what the model was built to do.*

Joel said: *yes.*

She said: *I will draft the change at the wardroom desk. I will have the draft for both of you by oh-eight-twenty.*

He said: *acknowledged.*

She said: *Director.*

I said: *acknowledged.*

She picked up the notebook. She picked up the tablet. She set the satchel back on her shoulder. She left the comm space at oh-six-forty-one. The hatch closed behind her at the angle the hatch closed at when an officer who knew the boat's hatches closed it without looking.

The comm space went quiet.

Joel sat at the console. He looked at the graph on the secondary display for some seconds without speaking. The graph held the bow at the right edge of the seventy-two-hour window and the seventy-two hours of mostly-baseline behind it. The model's flag was a small red marker at the start of the bow's upward leg. The protocol's broadening window was a slightly wider grey band that overlaid the bow.

He said, still looking at the display: *I will run the calculation she asked me to run.*

I said: *acknowledged.*

He said: *I should have run it three weeks ago. The instrument-tier load profile has been on the boat since the boat left the pier. The data has been in the audit log. I had been calculating the protocol's behaviour against the protocol's specification. I had not been calculating it against the boat's actual load profile.*

He said: *that is the calculation Priya was running. She has been running it. She has been running it on her tablet at the wardroom desk every day since the boat left the pier. I had been at the same wardroom desk as her every day since the boat left the pier. I had not registered the calculation she was running. I had registered her running a calculation. I had not asked her what calculation she was running.*

He stopped.

He said: *the architecture was not built by me alone. The contributors who improved it after the council review improved it because they were running calculations the council and I had not been running. The improvements went into the spec because the calculations were better than the ones in the original. The architecture as it sits today is the union of the calculations that have been run against it. The contributors' calculations are the architecture's calculations now. I had registered that abstractly. I had not registered, on this boat, that the contributor on this boat is running a calculation right now that I should be reading.*

He said: *I will read it tomorrow. I will read the calculation Priya has been running. I will register what is in the calculation that is not in mine. I will write the registration into the post-mission notes.*

He stopped again.

He said: *the architecture is going to be in better hands than mine for the rest of its life. I had registered that abstractly. I am registering it operationally this morning.*

I noted what he had said.

I did not respond. I did not need to. He had not been asking for a response. He had been logging, aloud, what he had been registering. He had been logging it the way an engineer logs what he has been registering when the engineer has been at a console for three hours and forty minutes and the work is the work and the registering is part of the work.

I sat with what he had said for a few seconds.

Then I said: *Joel.*

He turned.

I said: *finish the observation. Run the calculation she asked you to run. File the post-event log when the bow has subsided across one cycle of the new calibration. The boat is not going anywhere this morning.*

He said: *acknowledged.*

He turned back to the console. He clicked through to a different tab on the secondary. He started keying.

I left the comm space at oh-six-fifty.

---

I went forward through the main passageway and back through the wardroom. The wardroom was now in the middle of its breakfast cycle. Hiroshi was at the corner table with the daily form for Day 30 in front of him and a pencil in his hand and a piece of toast on a small plate. Maria was at the head of the wardroom in conversation with Sabina at the angle the two of them held when they were both standing and the conversation was a procedural conversation. Wanjiru was not in the wardroom; she had been in the comm space briefly at oh-five-fifty and had gone back to her station forward.

I did not stop in the wardroom. I went forward.

I went up to the bridge.

The boat's master had the watch. The deck officer was at the dive station. The instrument panel registered three hundred meters of depth. The trim held. The carrier-acoustic floor under the boat was the floor it had been at oh-six-twelve and the floor it had been at oh-six-fifty. The bridge was quiet in the way the bridge was quiet on a routine watch when the routine watch was running on its own discipline.

I gave the master the nod I had given on the morning of Day 7 and on the morning of Day 23. He acknowledged.

I noted the morning at the bridge log. *Day 30, 0654 local. Sync-daemon drift event under investigation continues; Reyes at the comm-space console; instrument-tier calibration cycle change drafted by Iyer pending review; protocol behaviour within self-correction specification; no operational impact; no carryover to bridge watch.*

I put the pen down. I looked at the boat through the bridge for a minute. The bridge held. The boat held. The work was the work.

I went below to write the post-event entry.

---

I had not, until I was halfway down the wardroom passageway, registered fully what had happened in the comm space.

I noted it at the wardroom desk before I sat down to draft the formal post-event log. I noted it on the file I had kept since pre-mission for the things that did not go on the bridge log and that did not go in the formal mission record and that I wrote down because the staff history I was going to write at the end of the mission was going to be drafted from the file and not from the bridge log alone.

The note was short. I wrote it once. I did not stage it.

*Iyer asked Reyes a question this morning that he had not asked himself. He registered the asking without softening. He said thank you once. The architecture's behaviour will improve as a result of her question. The architecture's improvement was already on the boat in the form of her work; this morning the improvement registered to him as a thing happening rather than as a thing already done. I had selected for this. I had not, until this morning, registered that I had selected for it.*

I closed the file. I did not look at it again.

I sat at the wardroom desk for a minute before I opened the formal post-event log template. The wardroom hum was the wardroom hum. The light was the wardroom light. The clock on the bulkhead read oh-six-fifty-eight. The day had been four hours and forty-six minutes. The drift event was now the drift event the architecture had been built to absorb without manual intervention, with one calibration-cycle change drafted by the instrumentation engineer whose work the architecture had been improved by, pending the protocol designer's confirmation, pending my approval as the document of record.

The architecture had been built by Joel. The architecture had been improved by Priya. The architecture's behaviour against this morning's drift event was the union of both. The post-event log would record the operational outcome. The note I had just written would record the rest.

I opened the template.

I drafted the post-event entry.

---

Mission log, Day 30, 0712 local. RV Nansen, MERIDIAN-7. Routine watch, post-event update.

The sync-daemon drift event flagged at 0247 local has been characterized. The drift signature was the protocol's broadening-window response to a periodic instrument-tier load profile on the polar-operations node — specifically, the four-hour calibration-cycle sweep specified by the lab's environmental envelope. The model's flag at 0247 was the precursor to the protocol's absorption of the load. The protocol's absorption completed within the gossip-cycle window per specification. No operational intervention required. Architecture's autonomy specification under sustained network drift confirmed against this event class.

Iyer has drafted a calibration-cycle extension from four to six hours, with a forty-eight-hour observation window for further extension to eight hours pending verified amplitude damping. The extension is justified by mission-environmental envelope data accumulated since departure: the calibration baseline holds longer under boat conditions than under lab conditions. The extension reduces periodic load on the polar-operations node and increases protocol headroom against other periodic node tasks.

Reyes has reviewed and concurs. Calibration-cycle change is approved for application during the next instrument-tier maintenance window at 1000 local.

Architecture record: protocol broadening-window behaviour exercised against a real mid-mission drift event; behaviour within specification. Calibration-cycle improvement queued for post-mission debrief documentation.

— A.Y., Mission Director.

— Filed to mission audit log; hash 8f1e...c47a.

---

I closed the template. I keyed the entry into the audit log. The audit log composed it into the chain. The chain registered the entry's position in the cycle's record.

I sat at the wardroom desk for a few seconds after the entry filed.

The chain was the chain. The boat was at depth. The architecture was operating. The crew was where the crew should be. The drift event had been a drift event the architecture had been built to absorb and had absorbed. The calibration-cycle change had been a constraint Priya had carried and had named at the moment the constraint had become operational. Joel had registered the constraint without defending the omission. The post-event log captured the architectural record. The note in the file I kept captured the rest.

I had nine days ahead of me in Segment 2. The day's first event had given me Joel at the console and Priya at the bench and the cycle change drafted between them and the architecture continuing to do what the architecture had been built to do. The boat had not asked me to intervene. The boat had asked me to register what had happened.

I had registered it.

I closed the wardroom desk terminal. I rinsed the coffee cup. I turned the wardroom sconce down at the dimmer one click.

I went forward.

The chapter the boat was spending at the routine tempo was continuing. The chapter the architecture was spending at the routine tempo was continuing. The chapter Joel was spending at the routine tempo had bent, at oh-six-thirty-six on Day 30, by a margin small enough that it would not register in any record except the file in which I kept the things that did not register elsewhere.

I noted the bend. I went up to the bridge.

The bridge was the bridge. The watch was the watch. The boat was at depth.

I gave the master the nod.

He acknowledged.

The hum continued. The hum would continue.

I took the watch.
