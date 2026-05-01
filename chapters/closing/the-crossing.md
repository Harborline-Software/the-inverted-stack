# The Crossing

<!-- icm/draft -->
<!-- Target: ~5,000 words -->
<!-- Source: design canon at .pao-inbox/_creative/the-crossing-concept-note-2026-04-30.md and character-sheets/ -->

---

I am writing this two months after the boat docked. Most staff histories are written under deadline by people who would rather be anywhere else; this one is written without a deadline by someone who has spent the time since return wanting to write it correctly. The mission was Sunfish-1. The destination was the underside of the Filchner-Ronne ice shelf. The architecture this document carries forward is the architecture this book describes. I held command. We came home with eleven of twelve.

What follows is the operational record. It is also, in places, less than that — and in other places more.

---

## Act I — Departure

Rustam Karimov, my classmate from the Tashkent gymnasium and now a Russian Navy captain by actual commission rather than civilian courtesy — *kapitan 1-go ranga*, the rank my civilian title only gestures at — sent his Telegram at 04:17 the morning of departure. *Don't lose the boat, fake captain.* He had sent some version of that message before every research voyage since I was thirty-two. I had read every one of them with the same dry tolerance — until that morning. I opened the gymnasium classmates group, where the joke had run for fifteen years and where forty-seven of us still spoke, half about children, half about each other's shortcomings. I typed a goodbye. *I am leaving for the ice today. Do not wait for me. The mission is enough work for the time I have.* I left the group. The thread disappeared from my list. I put my phone down. I did not look at it again before the boat left port.

I helped build this architecture. That morning I was about to command a boat carrying it three hundred meters under the ice. I had been afraid since the briefing. I will not pretend otherwise.

We departed Punta Arenas at 06:42 local time, fifteen minutes ahead of the tide table. The crew was twelve scientists, three engineers, a vessel master, and a small support detachment from the consortium's Norwegian co-funder. The mission was multinational — UAE-led, with Indian, Brazilian, French, and Norwegian co-funders, plus the CIS-region scientific contribution the consortium had specifically wanted me to lead. I had spent eighteen years at the Arctic and Antarctic Research Institute in St. Petersburg getting to a position from which I could be selected for this. I had also spent those eighteen years building the cross-institutional relationships that made the selection feasible — the postdoctoral years at AWI Bremerhaven and the Norwegian Polar Institute, the careful work of keeping those relationships alive after 2022 when other Russian colleagues' relationships went silent. The selection was the credential the consortium chose to recognize. The relationships were the work that made the recognition available. The mission was the next work after that.

The crew, briefly. Maria Santos, our medical officer, recruited because she had designed the offline-first medical-records system the boat carried; Maria had survived a hospital ransomware morning in Belo Horizonte some years before and had built her career to make sure no other administrator's morning looked like hers. Priya Iyer, our lead instrumentation engineer, who had designed the modular ice-shelf monitoring sensors we were here to deploy; Priya had lost a Pune hospital bid one afternoon in her twenties and had not built a system since that did not assume the network would go dark. Lakshmi Reddy, our logistics and procurement officer, who had spent twelve years in rural Indian banking with carbon-copy ledgers on hand for the days the platform did not respond; Lakshmi did not trust networks she could not see, and she would say so. Joel Reyes, our submarine life-support engineer, who had spent his thirties running parallel local data captures on offshore platforms in the Gulf because the cloud's ingestion pipeline had once dropped six hours of a drilling shift on a two-hundred-million-dollar well; Joel had brought his habits onto the boat with him. Étienne Marchand, our chief scientist, French, Sorbonne-trained glaciologist, thirty years of Antarctic work, the calmest man on the manifest. Wanjiru Kamau, our communications and data officer, who had cut her professional teeth on East African mobile-money infrastructure where offline-first was not a movement but a precondition; Wanjiru hummed under her breath when she concentrated, and after the first week I had stopped registering it. And Lars Bergmann, our senior technical specialist, Norwegian polar veteran, fifty-nine years old, fifty deployments to one pole or the other across thirty-five years of work, the person every other senior officer on the boat deferred to on questions of polar conditions. Lars had told me on departure night that this would be his last mission. He had told his wife the same thing. He had said he wanted to see the Filchner-Ronne ice shelf from the underside one time before the climate made it impossible. He had brought his cameras.

We dove at 11:18 the first day. The boat went silent in the way submarines go silent — not absence of sound but a different one, the sound of a sealed environment under pressure, the air system breathing in a register the body learns to forget within an hour. The mission began.

---

## Act II — Submerged Transit

What follows is the procedural record of two weeks under polar surface. Watch rotation. Meals. Instrument calibration. Surface windows at predetermined intervals — every seventh day the boat would ascend to periscope depth, the relay would open, the queue would move, the next dive would begin. The architecture's design assumed exactly this rhythm. The boat's design assumed exactly this rhythm. The crew adjusted to it within ninety-six hours. By the end of the first week, none of us were thinking about the surface except as an operational appointment.

I observed Maria's tic on the third day. Before her watch handoff in the medical bay, I watched her run the medical-records consistency check three times. Once would have been procedure. Three times was something else. I made a note in my log and did not raise it with her. I had read enough about Belo Horizonte to know what the third check was for. I would observe it again, several times, before the chapter of this story we are now coming to.

Priya ran calibration on the instrumentation modules every other day during transit. The modules would not be deployed until we reached the ice shelf, but Priya did not trust calibration that had not been verified three times. She did not call it a tic. She did not have to.

Joel ran independent life-support diagnostics on local sensors only. He did not trust cloud telemetry. The boat's cloud telemetry was, in his terms, *just another service that could decide to stop responding without telling me first.* He ran his diagnostics from a laptop in his bunk that he had reformatted to a Linux distribution the consortium's IT department had not been informed about. I knew about the laptop because Joel had told me about it in his first watch handoff, blunt and unprompted, in the manner of a man who would rather you know than discover. I had thanked him for the disclosure and asked him to keep doing it.

I had a moment, sometime in the second week, where I thought about the bakery in St. Petersburg where I have bought the same dark rye for fifteen years. I do not know what triggered it. The boat's mess produced perfectly adequate bread, and the bread was not the connection. It was the bakery itself — the *bulochnaya* on Liteyny Prospekt, the woman behind the counter who has known me since I was a postdoctoral fellow, the smell of the warm loaves at six in the morning when I have woken up too early before a flight. Bakeries are how I catalog cities. The boat is not a city. The memory was a moment of warmth that lasted twenty seconds and then I went back to reading the day's instrument calibration report.

The mid-mission disruption arrived at the second week's surface window. Wanjiru came to my cabin at 0814 local time with her tablet and the kind of measured calm that meant something operational had broken. The consortium's primary cloud SaaS provider — a Western vendor whose services had backed our administrative coordination since procurement — had terminated services on jurisdictional grounds. The notification cited regulatory pressure from a jurisdiction the vendor's parent company operated under, plus a sanctions-enforcement update we had been tracking. The termination affected approximately four hundred consortium projects worldwide and was effective immediately.

By 0830 the architecture had already redirected the relay endpoints to the consortium's in-region infrastructure. By 0900 the only thing changed was the routing table. Wanjiru had the failover ready before the consortium notification finished arriving — she had been watching the relevant news for three weeks and had pre-staged the alternative endpoints. Lakshmi had the consortium's procurement notifications redirected within forty-five minutes; she had kept paper backups of every signoff for twelve years and was not going to be caught flat-footed by a jurisdictional decision she had been preparing for since rural BFSI. Joel ran life-support diagnostics in the same hour, independently, on local sensors only, just to confirm that the operating envelope had not shifted while the administrative layer was being reconfigured. He had never trusted cloud telemetry on the platforms. He did not trust it on the boat.

The mission continued. The architecture absorbed the disruption without strain. The relay was never the data store; the cloud was never load-bearing. I wrote it that way in my log because that was how it looked from inside the boat. I am writing it that way here because that was how it actually was.

That was the easy disruption.

---

## Act III — The Death

Lars Bergmann was on bridge watch at 03:17 local time, day eighteen of the mission, three hundred meters under the Filchner-Ronne ice shelf. Joel was the watch officer. He was the one who registered first that something was wrong.

What follows I will write in the present tense, because I have read what I wrote at the time and the past tense flattens it.

---

It is 03:17. The bridge is at night-watch lighting, red, low. Lars is standing at the navigation console reviewing the latest sonar return from the ice shelf above us. Joel is at the watch desk eight meters away, running a routine life-support check on his tablet. The boat is making four knots on a north-northeast bearing toward the next instrumentation deployment site. The air system is breathing in its usual register.

Lars does not say anything. His hand goes to the console rail. His knees go. Joel sees him fall in his peripheral vision and is on his feet before Lars hits the deck.

Joel calls medical at 03:18. *Bridge, medical, now.* That is the entire transmission. Maria arrives at the bridge in fifty-eight seconds, which is the time it takes to traverse the boat at a controlled run from the medical bay aft. She has her bag. She is in her pajamas. She does not register that she is in her pajamas.

I am called from my cabin at 03:19. I arrive at the bridge at 03:21. Maria is already on the deck with Lars. Joel is holding the sonar console steady because the boat is making four knots and the bridge does not pause for medical events. Étienne arrives behind me and takes operational command of the boat without being asked, because that is what the chief scientist does when the Mission Director needs to be elsewhere.

Maria runs the resuscitation protocol. CPR. Defibrillator. Pulse check. CPR. The medical records on her tablet update in real time as she works, signed with her Ed25519 device key, queued for the next surface window. She does not ask me to leave the bridge. I do not leave.

I am watching her hands. Her hands are precise. Her hands are exactly as precise as the hands of a woman who has practiced this protocol every six weeks for twenty years on training mannequins because the protocol is the only thing she trusts to be the same in every instance.

At 03:39 she stops compressions and runs a final pulse check.

At 03:42 she pronounces him.

At 03:42 she checks the medical records on her tablet three times. The boat is still making four knots. The air system is still breathing in its usual register. Lars is on the deck. The medical record shows the time of death as 03:42, the cause as preliminary cardiac event pending postmortem, the attending as Dr. Maria Santos. Maria checks it three times. She is not checking for errors. She is checking for the thing she has been checking for since Belo Horizonte, which is that the record exists, that the record will survive, that the record will reach the people who need to know what it says.

Joel and Étienne move Lars's body to the medical bay at 03:51. The body is in the medical bay until 04:14. At 04:14 the body is moved to the freezer behind the dogged door at the aft end of the lower deck, because the boat has another twenty-three days of transit before landfall and there is no other operational option. The procedure is one I have never had to authorize and have read about in three different operations manuals across my career. I authorize it at 04:14.

---

The past tense resumes here.

I walked back to my cabin at 04:23 through corridors lit by the same night-watch red. I passed the freezer door. I did not open it. I would not open it for the remaining twenty-three days of the transit, and I would know what was behind it for every shift I stood until landfall.

I wrote the death notification in my cabin at 04:38. I did not sleep again that night. The notification carried Lars Bergmann's mission logs through the previous shift, his photographs from the descent four days earlier (he had photographed the underside of the ice shelf from the periscope position; the photographs were what he had wanted to see), his observation records on basal melt rates from his unfinished paper, his handoff documentation for any successor on the observation runs, and a personal letter from me to his wife that I composed in three drafts and finalized at 06:14. I attached the letter to the notification. I queued the notification for the next surface relay window. The next surface window was in six days.

I did not write the standard staff-history entry that morning. I wrote that entry six days later, after the surface window did not give us what we expected.

---

## Act IV — The Window That Doesn't Come

The boat surfaced at 14:00 local time on day twenty-four. We had timed the ascent to coincide with the predicted opening of the relay's nearest in-region endpoint. The procedure was routine. Wanjiru opened the uplink at 14:04. The relay did not respond.

She tried the secondary endpoint at 14:09. The secondary endpoint did not respond.

She tried the tertiary endpoint, which was the Norwegian Polar Institute's research relay that had been added as a cross-consortium fallback, at 14:14. The tertiary endpoint did not respond.

By 14:30 we had cycled through all configured endpoints and confirmed that the failure was not local to our uplink hardware. Joel ran independent diagnostics on the radio stack. The radio stack was operating within specification. We were transmitting. We were not receiving acknowledgment.

We held at periscope depth for thirty-two minutes. The relay did not respond.

I authorized the dive at 15:02. The boat returned to depth. The next scheduled surface window was three days away.

What I write next is the part of this staff history I have not been able to write until now.

I sat in my cabin between 15:02 and 23:00 that day. I did not eat. Maria came at some point with a tray and left without speaking. Wanjiru came at 19:30 and reported that the relay was still not responding from any endpoint we could observe through the periscope-depth transient signal we had left running. Lakshmi came at 21:14 and reported that the consortium's redundant administrative endpoints were also not responding, which was a different system but suggested an upstream regional event the in-region infrastructure had not been built to absorb. None of this mattered for the next three days because we were going to be at depth.

The death notification was in the queue. The notification carried Lars Bergmann's last shift, his last photographs, his last unfinished paper, his last handoff documentation, and the letter I had written to his wife. The queue had accepted the notification six days earlier and had been holding it through six days of transit. The queue would continue to hold it for as long as the relay did not respond. The architecture was operating exactly as designed.

The architecture was failing at the moment it mattered most.

I have spent most of my life believing that if I prepared enough, the silence would not arrive. The silence had arrived anyway. I had built a system that was failing at the moment it mattered most. I had built the next family's locked iPhone. I had built the call I could not answer. There is a Russian word for the silence on a phone line that arrives when you are waiting for news. There is also an Uzbek word. Neither word translates. I will not write either one here. The preparation was for what happens after.

I did not know whether the relay was going to come back. I did not know whether the next surface window would receive us. I did not know whether Lars Bergmann's wife was going to find out about her husband's death from an institution other than mine. I did not know whether the architecture I had spent my career helping build was going to be remembered as the system that delivered, or as the system that did not.

We dove for three days. The boat made nine knots on a north bearing toward the next surface window. The air system breathed in its usual register. The freezer behind the dogged door held what it held. Maria checked the medical record three times every watch. Wanjiru kept the radio stack warm and ran a passive listen on the next-window endpoints during her shifts, in case the relay came back early. The relay did not come back early.

The next surface window opened at 11:42 local time, three days later. Wanjiru opened the primary endpoint at 11:46. The relay responded.

The queue moved. The queue moved for forty-seven minutes. Twenty-three days of accumulated mission data, including the death notification and Lars's photographs and his unfinished paper and the letter I had written to his wife, transmitted in priority order. At 12:33 the queue cleared. Wanjiru closed the uplink. The boat dove again.

The notification reached Aino Bergmann at 14:42 Norway local time, eleven days after her husband's death. She received the death notification, the personal letter from me, Lars's mission logs, his photographs from the descent, his unfinished observation records, and his handoff documentation. The Norwegian Polar Institute confirmed receipt by relay acknowledgment at 14:53.

The architecture did not bring Lars back. The architecture delivered what he had done.

I am writing the difference between those two sentences as the work of this entire mission.

---

## Act V — Return

The instrumentation deployment proceeded on day twenty-nine. Priya ran calibration three times before each module went over the side, and three times after. Étienne supervised the scientific protocol. Joel ran life-support diagnostics during every deployment because that was what he had always done and because it was the kind of redundancy a Filipino offshore engineer brings to a polar submarine without being asked. The deployment took four days and went without incident. The instruments are on the underside of the Filchner-Ronne ice shelf as I write this, transmitting basal-melt-rate observations to the consortium's archive, in the configuration Priya designed and the position Lars had identified before he died. He had picked the position from the photographs he took on the descent. The position is correct. The instruments are doing what they were built to do.

We surfaced for the final time on day thirty-three, transmitted the full data set, and began the homeward transit. Lars's body remained behind the dogged door for twenty-three more days, because that was the operational reality of the boat and there was no other option. I did not open the door. I do not believe anyone else opened it either. I did not ask.

I wrote the closing pages of this staff history during the homeward transit, in my cabin, the boat still under the ice for the first nine days of the return and on surface routing for the last fourteen.

What I have learned, in the months since the boat docked, is the resolution I am about to write. I am writing it because I owe it to the next architect who reads this document, in whatever century the next architect is reading it, with whatever architecture has replaced the architecture this book describes.

The architecture does not solve mortality. The architecture queues against mortality. Built today, intended to outlast its conditions, knowing the conditions will eventually outlast it. The system that runs in 2090 will not be this one. I write it anyway, because the principle has to survive the system that taught it. We learned this in 2022, in a way most of the scientists who will read this book did not have to learn it. We learned it again on the underside of the Filchner-Ronne ice shelf in the third week of Sunfish-1, between 14:00 and 15:02 local time on day twenty-four. We will learn it the next time. I would prefer the next time be later. I would prefer my colleagues' work to outlast the moment that takes the architecture down.

Lars Bergmann's daughter is six years old. She received four thousand and seventeen photographs from her father's last mission, including the photographs he took of the underside of the Filchner-Ronne ice shelf on the descent four days before he died. She will not remember him in the way the photographs will let her see him. The architecture did not save him. The architecture delivered what he saw. I am writing this so that the difference between those two sentences is the document she finds when she is old enough to read it.

Maria Santos still checks the medical records three times before every watch handoff. She has not stopped. She will not stop. I have stopped looking for the day she stops. Some scars are the shape of work that finished. Some scars are the shape of work that did not. Maria's scar is the second kind. Her competence still costs her. The architecture has not healed her, and I do not think it should.

I have a fear I will name here because the staff history has to carry it forward. I am afraid the historical pattern is going to win, despite everything I have helped build. I am afraid the next family is going to make the same call somewhere I cannot reach. I am afraid that the architecture will not last, and I am afraid I will not last, and I am afraid that the locked iPhone — the one I have spent my career trying to prevent for somebody else's family — is going to be the device my family eventually finds in my office, twenty years from now, with a passphrase I never wrote down and a photograph collection my own daughter, if I have one by then, will not be able to retrieve. I have not made that document yet. I should. I am writing this knowing I have not.

The boat docked at Punta Arenas at 04:41 local time on day fifty-six. Lars Bergmann's body returned home to Norway by air freight three days later. His wife and his daughter and his three colleagues from the Norwegian Polar Institute received him at Tromsø airport, and the photographs he took on the descent had reached them four weeks earlier, and the difference between the two arrivals was the difference this entire mission was built around. I did not attend the funeral. I sent a letter.

I submit this staff history to the consortium's archive on the date below my signature. The next mission's commander will inherit the document, the architecture, the procedures, and the obligations the procedures imply. I will not command another submarine. I have done the work I was selected to do. I will continue at the institute, training the people who will be selected for missions after Sunfish-1, helping build whatever architecture replaces this one when this one is no longer adequate.

Rustam has not heard from me since the morning I left the group. He will, eventually, when I have something to say to him that is not the pattern we ran for fifteen years. The bakery on Liteyny Prospekt is still there. I went the day after I got home. The woman behind the counter has known me since I was a postdoctoral fellow. She did not know where I had been. She gave me the same dark rye she has given me since 2009. I carried it home in a paper bag. I ate it for breakfast for four days. The architecture queues against silence; the bakery queues against the same thing in a different way; some things you leave; some things you carry.

This is the staff history of Sunfish-1.

— Anna Yusupova
Mission Director
Arctic and Antarctic Research Institute, St. Petersburg
