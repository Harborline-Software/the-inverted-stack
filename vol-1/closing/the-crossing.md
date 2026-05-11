# The Crossing

<!-- icm/draft -->
<!-- Target: ~5,000 words -->
<!-- Source: design canon at .pao-inbox/_creative/vol-2-software-as-gravity.md, vol-2-archive-and-capture-convention.md, series-arc-sunfish-trajectory.md, and character-sheets/ -->

---

I am writing this two months after the boat docked. Most staff histories are written under deadline by people who would rather be anywhere else; this one is written without a deadline by someone who has spent the time since return wanting to write it correctly. The mission was MERIDIAN-7. The boat was the RV Nansen. The destination was the underside of the Filchner-Ronne ice shelf. The architecture this document carries forward is the architecture this book describes; I read the paper in the spring and recruited its principal author on the strength of it. I held command. We came home with all twelve.

What follows is the operational record. It is also, in places, less than that — and in other places more.

---

## Act I — Departure

Rustam Karimov, my classmate from the Tashkent gymnasium and now a Russian Navy captain by actual commission rather than civilian courtesy — *kapitan 1-go ranga*, the rank my civilian title only gestures at — sent his Telegram at 04:17 the morning of departure. *Don't lose the boat, fake captain.* He had sent some version of that message before every research voyage since I was thirty-two. I had read every one of them with the same dry tolerance — until that morning. I opened the gymnasium classmates group, where the joke had run for fifteen years and where forty-seven of us still spoke, half about children, half about each other's shortcomings. I typed a goodbye. *I am leaving for the ice today. Do not wait for me. The mission is enough work for the time I have.* I left the group. The thread disappeared from my list. I put my phone down. I did not look at it again before the boat left port.

I had read Joel Reyes's paper on the architecture in the spring. I had recruited him in May on the strength of what the paper showed me about the man who had written it. That morning I was about to command a boat carrying his architecture three hundred meters under the ice. I had been afraid since the briefing. I will not pretend otherwise.

We departed Punta Arenas at 06:42 local time, fifteen minutes ahead of the tide table. The crew was twelve scientists, three engineers, a vessel master, and a small support detachment from the consortium's Argentine co-funder. The mission was multinational — UAE-led, with Indian, Brazilian, Japanese, and Argentine co-funders, plus the CIS-region scientific contribution the consortium had specifically wanted me to lead. I had spent eighteen years at the Arctic and Antarctic Research Institute in St. Petersburg getting to a position from which I could be selected for this. I had also spent those eighteen years building the cross-institutional relationships that made the selection feasible — the postdoctoral years at AWI Bremerhaven and the Norwegian Polar Institute, the careful work of keeping those relationships alive after 2022 when other Russian colleagues' relationships went silent. The selection was the credential the consortium chose to recognize. The relationships were the work that made the recognition available. The mission was the next work after that.

The crew, briefly. Maria Santos, our medical officer, recruited because she had designed the offline-first medical-records system the boat carried after surviving a hospital ransomware morning in Belo Horizonte some years before. Priya Iyer, our lead instrumentation engineer, who had designed the modular ice-shelf monitoring sensors we were here to deploy and had also rewritten the architecture's schema-migration mechanism after a council review surfaced a defect; Priya had lost a Pune hospital bid one afternoon in her twenties and had not built a system since that did not assume the network would go dark. Sabina Rahman, our logistics and procurement officer, twelve years in rural Bangladeshi microfinance, who had inherited the Grameen Bank discipline that had made population-scale offline-first banking work in her country since 1976, and who did not trust networks she could not see and would say so. Joel Reyes, our principal architect and on the boat our submarine life-support engineer, who had spent his thirties running parallel local data captures on offshore platforms in the Gulf and his earlier years on the USS *Sunfish* SSN-649 where casualty drills had become reflex deeper than choice; he had brought both sets of habits onto the boat. Hiroshi Nakamura, our chief scientist, Japanese, NIPR-affiliated glaciologist with thirty years of JARE deployments to Showa Station going back to his graduate years in the 1990s, the calmest man on the manifest. Wanjiru Kamau, our communications and data officer, who had cut her professional teeth on East African mobile-money infrastructure where offline-first was not a movement but a precondition; Wanjiru hummed under her breath when she concentrated, a Kikuyu lullaby fragment she did not know she was humming, and after the first week I had stopped registering it. And Diego Vargas, our senior technical specialist, Argentine polar veteran from the Instituto Antártico Argentino, fifty-nine years old, fifty deployments to one pole or the other across thirty-five years of work, the person every other senior officer on the boat deferred to on questions of polar conditions. Diego carried the institutional memory of the IAA, which had operated continuously occupied Antarctic stations since 1904 — older than aviation. He did not announce it. He did not need to. He had told me on departure night that this would be his last mission. He had told his wife the same thing. He had said he wanted to see the Filchner-Ronne ice shelf from the underside one time before the climate made it impossible. He had brought his cameras.

We dove at 11:18 the first day. The boat went silent in the way submarines go silent — not absence of sound but a different one, the sound of a sealed environment under pressure, the air system breathing in a register the body learns to forget within an hour. The mission began.

---

## Act II — Segment One, Segment Two

The mission ran in three segments. Segment One was a twenty-one-day transit-and-deployment leg under the outer Weddell Sea ice; Segment Two was a sixteen-day instrumentation-deployment leg under the Filchner-Ronne shelf proper, with a surface window between them; Segment Three was the inner-shelf observation leg with the final ascent at Punta Arenas at Day fifty-six. The architecture's design assumed exactly this rhythm. The boat's design assumed exactly this rhythm. The crew adjusted within ninety-six hours.

I observed Maria's tic on the third day. Before her watch handoff in the medical bay, I watched her run the medical-records consistency check three times. Once would have been procedure. Three times was something else. I made a note in my log and did not raise it with her. I had read enough about Belo Horizonte to know what the third check was for. I would observe it again, several times, before the chapter of this story we are now coming to.

Priya ran calibration on the instrumentation modules every other day during transit. The modules would not be deployed until we reached the ice shelf, but Priya did not trust calibration that had not been verified three times. She did not call it a tic. She did not have to. She set objects down with audible weight — a coffee cup on the wardroom table, a clipboard at the lab compartment console — the way her body had learned to mark the discipline.

Joel ran independent life-support diagnostics on local sensors only. He ran them from a laptop in his bunk that he had reformatted to a Linux distribution the consortium's IT department had not been informed about. I knew about the laptop because Joel had told me about it in his first watch handoff, blunt and unprompted, in the manner of a man who would rather you know than discover. I had thanked him for the disclosure and asked him to keep doing it.

I had a moment, sometime in the second week, where I thought about the bakery in St. Petersburg where I have bought the same dark rye for fifteen years. I do not know what triggered it. The boat's mess produced perfectly adequate bread, and the bread was not the connection. It was the bakery itself — the *bulochnaya* on Liteyny Prospekt, the woman behind the counter who has known me since I was a postdoctoral fellow, the smell of the warm loaves at six in the morning when I have woken up too early before a flight. Bakeries are how I catalog cities. The boat is not a city. The memory was a moment of warmth that lasted twenty seconds and then I went back to reading the day's calibration report.

Surface One arrived at the end of Segment One — Day twenty-one, periscope-depth ascent, relay opening, queue moving, dive again. The procedure was routine. Wanjiru opened the uplink; the queue cleared in fifty-eight minutes; the boat dove again. Twenty-one days of accumulated mission data, signed at capture, replicated to the consortium-port mirror at Punta Arenas. The architecture absorbed the rhythm without strain.

The first disruption arrived three days into Segment Two. Wanjiru came to my cabin at 08:14 with her tablet and the kind of measured calm that meant something operational had broken. The consortium's primary cloud SaaS provider — a Western vendor whose services had backed our administrative coordination since procurement — had terminated services on jurisdictional grounds. The termination affected approximately four hundred consortium projects worldwide and was effective immediately.

By 08:30 the architecture had redirected the relay endpoints to the consortium's in-region infrastructure. By 09:00 the only thing changed was the routing table. Wanjiru had the failover ready before the consortium notification finished arriving; she had been watching the relevant news for three weeks. Sabina had the procurement notifications redirected within forty-five minutes. Joel ran life-support diagnostics in the same hour on local sensors only, to confirm the operating envelope had not shifted while the administrative layer was being reconfigured.

The mission continued. The relay was never the data store; the cloud was never load-bearing. I wrote it that way in my log because that was how it looked from inside the boat.

That was the easy disruption.

Segment Two closed at Day thirty-nine. Surface Two opened the next morning at 11:42. The queue moved for forty-seven minutes — Priya's deployment data, Diego's underside photographs from the descent, Hiroshi's basal-melt observations, the cross-instrument cross-checks Wanjiru had been running through the segment. The boat dove again at 14:08 and began Segment Three.

---

## Act III — The Eleven Minutes

The leak alarm fired at 03:17 local time on Day forty-seven, three hundred meters under the inner Filchner-Ronne ice shelf, eight days into Segment Three. I had been asleep. The cabin alarm repeater carried the lower-deck-aft annotation and the three-pulse pattern the boat used for breach-class events — the alarm I had read in the manual every week of my training and had never expected to read against an active casualty.

What follows I will write in the present tense, because I have read what I wrote at the time and the past tense flattens it.

---

It is 03:17. I am on my feet before I have named what woke me. The corridor outside my cabin is at the same red night-watch lighting the bridge will be at. I go up the corridor toward the bridge. I register Joel before I register the corridor. He is coming the other direction, not running, moving at the deliberate pace I read on his recruitment-interview videoconference five months before the boat sailed when he described, in flat clauses, what he would do in a casualty event. *You move toward the source. You do not run. You arrive in a state in which you can think.*

He is moving toward the leak. I am moving toward the bridge.

We converge at the lower-deck access ladder. The corridor at the foot of the ladder is narrow enough that two crew members can pass only with a turn. I have not been thinking about the corridor's width. I have been thinking about the bridge.

He pushes me aside.

The contact is a hand at my shoulder, firm, brief, and specific. The push is the push of a man whose body has decided to be at the leak before any cognitive part of him has caught up with the decision, and whose body has registered me as an obstacle in the path the body has decided to take, and whose hand has moved me out of the path without his face changing. I step back. I do not stumble. My hand finds the bulkhead rail; I am at the rail beside the ladder before I have registered that I have been pushed.

He does not look at me. He does not stop. He goes down the ladder.

I go up to the bridge.

Diego is at the polar-operations console. He has been on the standing eight-to-four watch — eleven minutes left on it — and the alarm has fired and he has not relinquished the console. The polar-operations console is where the sensor-head telemetry comes in. Diego has the diagnostic view up. The diagnostic view shows a register-shift in the starboard sensor head's pre-failure acoustic signature at 03:16:30. The firmware had logged the event at the watchword level thirty seconds before the breach-class alarm fired. The firmware had known. The Anchor archive had registered. The first event was already in the record.

Diego says, without looking up: *Director.*

I say: *Engineer, the situation.*

He says: *Starboard sensor head, compartment two-bravo, lower deck aft. Pre-failure acoustic at oh-three-sixteen-thirty. Leak alarm at oh-three-seventeen. Reyes is en route to the compartment. Watch officer at the bridge has the boat at four knots on the bearing. Trim is holding.*

He pauses for one breath. He says: *The sensor head is collateral to whatever this is. The collateral is the compute hub in the same compartment.*

I say: *Acknowledged.*

The watch officer at the bridge is Hiroshi. He has been at the bridge for the standing handoff. He has registered me at entry. He has not relinquished the helm. The bridge needs a helm; the helm is Hiroshi's; the Mission Director's standing is a different kind of standing. I go to the standing position at the rail behind the watch console — visible to the watch officer, the polar-operations specialist, the comm node, and any crew member who comes up to the bridge during the duration of the event. The position is the command-watch position. I stand at it.

I say: *Bridge, hold trim. Two-up on starboard plane.*

Hiroshi says: *Acknowledged. Trim two-up starboard plane.*

He executes. The boat's trim adjusts. The cascade window — the period during which the boat's trim could compound a compartment-isolation event into a depth excursion — is opening. Diego, without looking up: *Director, recommend depth hold. Recommend ventilation hold on compartment-two-bravo's adjacent ducting until isolation is declared.* I acknowledge. The depth holds. The ventilation holds.

I have not seen Joel dog the bulkhead door. I was at the lower-deck access ladder when the dogging happened.

I have seen the look.

Joel turned at the compartment door after he had dogged it. He faced me through the porthole window. The light on his side was the compartment's emergency red. The light on my side was the corridor's night-watch red. The two reds were the same red.

He looked at me.

The look held for a duration I did not measure. It was longer than any look I had registered between us across five months of mission preparation and forty-seven days of sea time. The look was the look I had not registered until the look happened.

The look said what the discipline had prevented him from saying since the recruitment interview.

I had read the discipline. I had recruited him for the discipline. The discipline had held for five months and for forty-seven days at sea. It had not held against the alarm. The body had moved, and the body had moved through me on the way to the leak, and the body had dogged the door, and the body had turned. The turn was the part of the sequence the procedure had not required. The turn was choice.

I received the look. I did not change my face.

The bridge behind me was at the standing register. Every crew member was watching the Mission Director. The Mission Director's face was the face the mission required. The face did not change.

Then he turned away and went to work.

---

The eleven minutes ran at 03:42 to 03:53.

What was inside the compartment was Joel and the failed instrument and the compute hub and the rising water and the smoke. The compartment cameras were on the consent-gated capture register; both crew members in two-bravo at the time of the alarm had consented to compartment-camera capture as part of the standing mission consent. Reyes was the only crew member in the compartment now. The capture was preserved. The capture was not for the bridge to watch in real time. The capture was for the record.

What I knew about the compartment from outside was what the bridge could know. Joel was working the leak. The leak was at the sensor head — an off-the-shelf vendor-supplied unit the consortium had integrated three years before the mission because the OSS budget had not allowed custom-firmware development. The unit's firmware had been updated three weeks before the mission against a vendor-supplied patch; the patch had been signed and cleared by procurement. The unit had operated at the standing register through Segment One and Segment Two and forty-six days of Segment Three. It had failed at 03:16:30 on Day forty-seven. Instrument-malfunction. The cause of the malfunction was a question the post-incident review would carry; the damage report I would file would log instrument-malfunction-under-investigation. The report would not carry an accusation of cause beyond that.

The compute hub shared the compartment. Coolant ingress had begun at its heat-exchange manifold within the first minute of the leak; smoke followed when Joel began cutting against the failed sensor's mounting bracket. The hub would not survive. The architecture had been built so that the hub's loss would be capability loss, not preservation loss. The canonical record was the per-laptop archive across the crew nodes; the hub had been capability, not source-of-truth. The architecture was operating at the case the architecture had been built for.

I stood at the standing position. I did not look at the door indicator. I did not check the comms log. I watched the casualty-board.

These were the worst minutes of my mission. I had just registered, definitively, what Joel felt — through a physical touch I had not consented to and through a look I could not rationalize away. I had just registered, definitively, what I felt — because the look had made denial impossible and because the touch had made the discipline impossible to maintain. And he was in a sealed compartment with active water ingress.

If something went wrong — if the instrument failed harder, if the leak accelerated beyond his containment, if the sealed compartment became a place from which he did not come out — I would have to live with the fact that the recognition arrived at the moment he might die.

The bridge was watching me. The face did not change.

At 03:53 the comms light up. *Bridge, two-bravo. Leak source isolated. Residual water drained. Smoke ingress contained. Compartment atmosphere within breathable specification. Compartment-clear declaration. Ready to open.*

I give the order. The lock disengages. He emerges under his own power. He is wet. He is smoke-streaked. There is a smudge of coolant residue at his cheek. The shoulder seam of his coverall is scorched where he took heat from the sensor head's casing. He is breathing at the rate Joel breathes when he has been working in confined access at sustained exertion. He is upright. He is steady.

He says: *Mission Director, casualty contained.*

I say: *Acknowledged.* I say: *Reyes, to medical.* He nods once. He goes to medical.

The crew sees a senior engineer who acted on instinct and competence and contained a leak in eleven minutes. Maria treats him at the lower-deck access ladder for a wrist abrasion he sustained reaching against the mounting bracket in the confined access at the back of the compartment. There is no other injury. He is medically fine.

Only Joel and I know what the door meant.

---

The past tense resumes here.

I filed the operational damage report at 04:38 in my cabin. The report carried the cascade at the operational register: 03:17 alarm; 03:19 cabin-to-bridge transit; 03:21 assessment; 03:42 compartment isolation order issued; 03:53 compartment-clear; cause of failure logged as instrument-malfunction-under-investigation; sensor head pre-failure timestream preserved in the Anchor archive; firmware-update history preserved in the audit log; command-and-response between control plane and the failed instrument preserved across crew nodes. No accusation of cause beyond instrument-malfunction at this filing. The forensic substrate was intact. The post-incident review would run after Punta Arenas, on laptop-class compute, between Wanjiru and Joel during the transit-north leg.

I did not sleep that night. I added an item to the list of things I would write at a different file under different access controls. The item was the eleven minutes. I would write the entry two nights later, at 23:47 on Day forty-nine, in a private file encrypted under my own KEK, where it would not be read until I read it again, if I read it again.

---

## Act IV — Diego's Letter

Diego came to my cabin at 21:12 the same day. He sat down across the desk from me. He had brought his leather mate-cup, his grandfather's, made in a San Martín de los Andes workshop sometime in the 1960s — the leather patinated dark, the silver bombilla unpolished. He usually kept it in his console drawer on the bridge.

He said: *Director, I will write a letter tonight. I want to write the letter on the per-laptop register against the canonical authored-content archive. The letter will not transmit until Punta Arenas. The letter is for my wife. I am writing the letter on the boat because I want the boat to be where the letter was written.*

I said: *Acknowledged. The letter is at the canonical authored-content archive. The letter does not require Mission Director authorization. The letter is for your wife. I will not read it.*

He said: *The letter is mine.*

I said: *The letter is yours.*

He said: *I am also writing the letter because I have decided. After Punta Arenas, I am going home to San Martín de los Andes. María Elena and I have been talking about this for three years. The Nansen was the mission we agreed I would do before I went home. I will announce it at Punta Arenas. I am telling you now because I want you to have time to decide what the polar-operations specialist's billet looks like for the consortium's next mission.*

I said: *Acknowledged. I will hold the announcement at the standing register until Punta Arenas. The mission has been your mission as much as it has been mine. María Elena and the dogs and the autumn light at the lake are your retirement. I am glad the Nansen is what we have been doing.*

He said: *I am glad too.*

He stood. He did not say anything else. He went out.

I sat at the desk. I added an item to the list. The item was: *consortium notification on Diego's retirement; polar-operations recruiting timeline; institutional handoff for the IAA's contribution at the Nansen mission record.*

The list grew.

---

Diego wrote the letter that night at his cabin desk on his per-laptop. The archive was per-author, signed at capture under his KEK, access-controlled by him. He wrote in Spanish first and a parallel English translation second — the register the IAA's institutional records had used since their first collaboration with the British Antarctic Survey in 1942.

I do not have the full letter. The letter is Diego's. The fragment I have is what Diego sent me three months later in Buenos Aires, when the consortium archive published the staff history's preliminary draft and he wrote asking whether it had captured what the boat had been like for him.

The fragment, in his Spanish:

*Mi amor — el barco es el barco. Las luces son rojas a esta hora; el aire huele al sistema; la cama es estrecha. Estoy bien. Estoy entero. Esta noche he visto algo que no voy a describir bien aquí; lo describiré mejor cuando esté en la mesa de la cocina contigo. He decidido que voy a casa. Después de Punta Arenas. He hablado con la directora de misión esta tarde; ella ha entendido. Voy a casa.*

*Echo de menos tu cocina. Echo de menos los perros. Echo de menos la luz de otoño en el lago. Echo de menos a nuestros nietos. He estado en el mar treinta y cinco años. Es tiempo.*

*Volveré.*

*— D.*

The letter sat at the canonical authored-content archive, signed at capture under Diego's KEK. It would reach María Elena at Buenos Aires when the boat surfaced. The letter did not require a relay window; it required surfacing. The boat would surface. The letter would deliver.

The autumn light at the lake at San Martín de los Andes is in March and April. The boat would surface on Day fifty-six, the second week of November. The autumn had ended six months before he would get home; the autumn would be back in four months. Diego would be there for the autumn after the autumn.

I added an item to the list: *transmit Diego's letter at the first surface window at Punta Arenas; carry it at the priority register; verify delivery; close the loop.*

The list grew.

---

## Act V — Return

Segment Three ran another nine days. Priya completed the inner-shelf instrumentation deployment; the modules went over the side at the positions Diego had identified, in the configuration Priya had designed. The instruments are on the underside of the Filchner-Ronne ice shelf as I write this, transmitting basal-melt-rate observations to the consortium's archive.

The compute hub was offline. The per-laptop nodes were operational. The crew adapted. Multilingual conversation that used to be native-language fluid became halting English in places where the heavy-LLM had been doing translation work; some queries we just didn't ask. Joel's schema-related work got done with laptop-class only — slower, more careful, more verification by hand. Wanjiru's surface-window sync-triage happened with diminished LLM assistance; she did more of the prioritization manually. My queries against the archive accumulated as a written list of *things to ask when we surface.* The list grew to twenty-two items by Day fifty-six. The crew did not narrate the adaptation. The architecture was at the operational tempo at reduced capability. The architecture was at the standing register.

We surfaced at Punta Arenas at 04:41 on Day fifty-six. The queue moved at the priority register Wanjiru had configured. Diego's letter transmitted at 05:18; María Elena read it at her kitchen table in Belgrano at 06:51 Argentina local. The damage report, the cascade captures, the schema-migration audit trail, the per-laptop archives — all moved through the queue in priority order. The architecture absorbed the surfacing without strain.

Diego told me at the gangway before the press detachment arrived. He said: *Directora, voy a casa.* I said: *I know.* The institutional filing followed within forty-eight hours.

Joel and I have not spoken of the look. We will not speak of the look on the boat. We will speak of it at some point. The point will be after Punta Arenas. The point will be after I have decided what to do with the point. I am writing this knowing the point is not yet at the point.

I wrote the closing pages during the administrative weeks at Punta Arenas, the flight back to St. Petersburg, and the first weeks at AARI after I returned. The list of things to ask when we surface is closed; some items resolved at Punta Arenas, some at the post-incident review during transit-north, some at the institutional debrief in Buenos Aires. Some are still open. The architecture does not close every loop. It preserves the loops that are open.

I am writing what follows because I owe it to the next mission director who reads this document.

The architecture does not solve mortality. The architecture queues against silence. Built today, intended to outlast its conditions, knowing the conditions will eventually outlast it. We learned this in 2022, in a way most of the scientists who will read this book did not have to learn it. We learned it again at 03:17 on the underside of the Filchner-Ronne ice shelf, between the alarm and the compartment-clear. The architecture absorbed what it was built to absorb: the loss of the compute hub, the loss of the sensor head, the eleven minutes during which a man worked an active leak behind a sealed door. It preserved the operational record. It preserved Diego's letter at the per-laptop register under his own key, where it sat for nine days until the boat surfaced and delivered it. It preserved the look at the porthole window at the consent-gated capture register, where I have not played it back and probably will not.

The architecture did not prevent the leak; it is not built to. The vendor-supplied sensor head was integrated because the consortium's OSS budget did not allow custom-firmware development. The architecture has always been honest about that constraint. Its job is to detect what cannot be prevented and to preserve what reaches durability. The forensic substrate is intact. The post-incident review is Wanjiru's and Joel's; it is institutional work; it will continue past my command of any boat.

Maria Santos still checks the medical records three times before every watch handoff. She has not stopped. She will not stop. I have stopped looking for the day she stops. Some scars are the shape of work that finished. Some scars are the shape of work that did not. Maria's scar is the second kind. Her competence still costs her. The architecture has not healed her, and I do not think it should.

I have a fear I will name here because the staff history has to carry it forward. I am afraid the architecture will not last, and I am afraid I will not last, and I am afraid that the locked iPhone — the one I have spent my career trying to prevent for somebody else's family — is going to be the device my family eventually finds in my office, twenty years from now, with a passphrase I never wrote down and a photograph collection my mother, if she is still alive, will not be able to retrieve. I have not made that document yet. I should. I am writing this knowing I have not.

Diego is in San Martín de los Andes. He sent me a photograph in March — the autumn light at the lake exactly the way he had described it on the boat the night he wrote the letter to María Elena. His granddaughter Sofía is six years old. She has the photographs her grandfather took of the underside of the Filchner-Ronne ice shelf on the descent, and she has the man who took them at the kitchen table when she asks. The architecture is one reason for that. It is not all of them.

Joel and I will speak at some point. The point is not yet. The work in front of us is enough work for the time we have.

I submit this staff history to the consortium's archive on the date below my signature. The next mission's commander will inherit the document, the architecture, the procedures, and the obligations the procedures imply. I will continue at the institute, training the people who will be selected for missions after MERIDIAN-7, helping build whatever architecture replaces this one when this one is no longer adequate.

Rustam has not heard from me since I left the group. He will, eventually, when I have something to say to him that is not the pattern we ran for fifteen years. The bakery on Liteyny Prospekt is still there. I went the day after I got home. The woman behind the counter has known me since I was a postdoctoral fellow. She gave me the same dark rye she has given me since 2009. I ate it for breakfast for four days. The architecture queues against silence; the bakery queues against the same thing in a different way; some things you leave; some things you carry.

This is the staff history of MERIDIAN-7.

— Anna Yusupova
Mission Director
Arctic and Antarctic Research Institute, St. Petersburg
