---
type: character-sheet
character: Joel Reyes — Principal Architect of Sunfish; senior crew engineer on Sunfish-1
status: working — promoted from minor character to full sheet 2026-05-04 per Vol 2 frame
sheet-depth: full
chapter: Vol 1 (The Crossing — minor presence) + Vol 2 (principal protagonist)
supersedes: `_minor-characters.md` § "GCC Offshore Platform Engineer (Ch1 → Sunfish-1 life support)" — that entry remains as historical record; this sheet is the canonical home for Joel
co-identification: CO has identified personally with Joel and is the source of truth on Navy-nuclear biographical detail
firewall-note: Joel's Navy biography draws on CO's lived experience (USS Sunfish SSN-649, US Navy nuclear engineer, Sturgeon-class boat 1990s service). Specific details about the boat and the operational discipline are CO-sourced and authoritative. Character is informed-by but not based-on; Joel is fictional. PAO defers to CO on all Navy-nuclear specifics; PAO writes the post-Navy distributed-systems trajectory and architectural authorship as fiction. CO directive 2026-05-05: framing changed from "Nuclear Machinist's Mate PO2/E-5" to "US Navy nuclear engineer" — preserves the boat, the operational discipline, and the silver dolphins; drops enlisted-rate-specific language for accessibility.
---

# Character Sheet — Joel Reyes, Principal Architect of Sunfish

## Why this character is promoted

Joel was originally a minor character in The Crossing — a Filipino engineer with GCC offshore-platform credentials who ran independent life-support diagnostics and didn't trust cloud telemetry. Those traits read as competent-skeptical-engineer in Vol 1.

Under the Vol 2 frame, Joel is the **principal architect of Sunfish** — the author of the paper that became the architecture, the namer of the project (after his first submarine), and the senior implementer Anna recruited specifically because of authorship. Every existing trait that read as competent-skeptical now reads as **naval-nuclear operational discipline carried into civilian distributed-systems work** — which is much sharper, more specific, and more credible to readers who recognize the discipline.

CO has identified personally with Joel and provided the Navy biography (USS Sunfish SSN-649, US Navy nuclear engineer, 1990s Sturgeon-class boat service). The character is informed-by but not based-on; the post-Navy fiction is PAO's to write.

The existing `_minor-characters.md` entry remains as historical record of the original Vol 1 framing; this sheet is the new canonical home.

## Identity

- **Name:** Joel Reyes
- **Title in narrative:** "Joel" in Anna's voice (informal, peer-respect register); "Mr. Reyes" formal; no naval rank or title in mission scenes (Joel left the Navy a long time ago)
- **Age at Sunfish-1 mission:** mid-50s (Navy enlistment ~early 1990s, USS Sunfish SSN-649 service through decommissioning 1998, ~25 years post-Navy career arc)
- **Citizenship:** United States (Navy service); Filipino heritage
- **Languages:**
  - English native
  - Tagalog heritage (extended family; some retained fluency from childhood, varies by domain — domestic register stronger than professional)
  - Technical Spanish (from contract engineering work in Gulf-region offshore platforms post-Navy)
  - Russian: reading knowledge; conversational basics from post-2022 OSS collaboration with CIS-region contributors (Anna among them, in their early professional contact)
- **Domicile:** Open. PAO drafting placeholder: a U.S. coastal area — somewhere with submarine-veteran demographic density (Norfolk VA, Groton CT, San Diego CA, Bremerton WA). CO can pin this if it matters for backstory scenes.

## Backstory — biographical firewall observed

**Navy biography (CO-sourced; PAO defers):**

CO has identified personally with Joel and provided these specifics:
- Service in the U.S. Navy Nuclear Program, 1990s
- Role: **US Navy nuclear engineer** (per CO directive 2026-05-05; framing prefers the engineer descriptor over enlisted-rate-specific language for accessibility)
- Boat: **USS Sunfish SSN-649**, Sturgeon-class fast attack submarine, decommissioned 1998 (public record)
- Working domain: reactor plant operations; engine room watchstations; reactor coolant systems; steam plant secondary loop; auxiliary machinery
- Earned the silver dolphins (Submarine Warfare qualification)

Cold War-era Sturgeon-class operations included deterrent patrols, anti-submarine warfare exercises, and intelligence-collection missions; CO can place Joel's specific patrols if needed for backstory beats. Public history of USS Sunfish SSN-649 provides the operational-record anchor.

The Navy left a stamp: trust-but-verify discipline, conservative-operations instinct, redundant-indications expectation, casualty-procedure muscle memory, watch-handoff register, the engineer's preference for the gauge in front of you over the dashboard across the network.

**Post-Navy fiction (PAO writes):**

Joel separated from the Navy ~late 1990s, around the same time USS Sunfish was decommissioned. The boat's decommissioning is one of those professional-turning-point moments that plays out in the lives of the sailors who served on her — when the Navy shrinks the fleet by one specific hull, the crew of that hull is among the first to feel it.

Computer-science transition (post-Navy, late 1990s into early 2000s — exact path open: could be undergraduate CS via veterans' education benefits if Joel commissioned via an enlisted-to-officer route, or graduate-level CS specialization if Joel commissioned via NROTC / Naval Academy / NUPOC with an existing engineering degree — CO can pin). The transition from reactor-plant engineering to distributed-systems engineering was less of a leap than non-veterans would expect: the same discipline of "treat the system as adversarial, build for what fails, never assume the dashboard is telling the truth" that runs a nuclear plant runs a distributed system. The engineering vocabulary changed; the operational temperament did not.

Mid-career arc (~early 2000s through ~2020):
- Defense contractor stint, probably ~5-8 years (the natural pipeline for nuclear-trained Navy veterans with new CS degrees) — distributed-systems infrastructure for tactical networks, secure communications, sensor fusion
- Transition to civilian / commercial distributed systems — a Bay Area or Pacific Northwest stint at a company doing infrastructure software (the kind of company where his veteran-engineer profile was unusual but valued)
- A contract engagement in the Gulf region working on offshore-platform engineering systems (the original Ch1 framing — preserved as a real career chapter; the SaaS-data-loss exposure he saw on those platforms was part of what motivated him to start designing better)
- Open-source distributed-systems contribution — first as a heavy contributor to other projects, then increasingly as a maintainer in his own right
- The Sunfish paper, published as a research-grade architecture spec, ~late 2020s

By the time of Sunfish-1 (mission-time 2026 in series-time), Joel has been the lead author and principal maintainer of the Sunfish OSS project for several years. The project is small in headcount (3-5 senior contributors plus a wider community), tested rigorously, vetted by the Kleppmann Council, and pre-1.0. He turns down opportunities to commercialize it — partly Navy-residual distrust of corporate ownership of safety-critical infrastructure, partly the stewardship instinct that keeps him in the maintainer role.

**Why "Sunfish":** he named the OSS project after his first submarine. USS Sunfish SSN-649 was decommissioned in 1998; Joel left the Navy around then; the paper went up under that name two decades later because the boat had been the place where the operational discipline that runs through the architecture got formed. It is a private gesture in a public project. Anna recognizes the name's weight when she reads the paper for the first time, but does not bring it up in their early conversations; that's the kind of thing you let the person tell you.

## Personality / voice

- **Core:** Direct. Specific. Operationally-disciplined. Quiet around new people; more conversational with people he's worked with. The kind of senior engineer who speaks rarely, speaks short, and is right when he speaks.
- **Default register:** technical-precise, with naval-nuclear vocabulary surfacing in moments of stress (*"casualty procedure," "redundant indications," "trust-but-verify," "watch-station qualification," "single-failure mode"*). The vocabulary is muscle memory, not affectation; he stopped noticing he was using it about fifteen years ago.
- **Skepticism of cloud telemetry:** rooted in NPO training. *You don't run a reactor on a single sensor; you don't trust a remote indication if you have a local one; you read the gauge in front of you.* In civilian distributed systems, this becomes: *you don't trust cloud telemetry on platforms that can decide to stop responding without telling you first.* Already on the page in The Crossing; the Vol 2 framing makes it specific Navy-nuclear discipline rather than generic engineer-paranoia.
- **Disclosure pattern:** discloses unprompted, in the manner of a man who would rather you know than discover. The bunk-laptop disclosure to Anna in first watch handoff (already in The Crossing) is canonical: *I reformatted my bunk laptop to a distribution the consortium's IT department was not informed about. I wanted you to know.* No defense, no excuse, no context-management. The pattern is also what convinced Anna to recruit him after the prior-failure colleague's non-disclosure of a known limitation. Joel is the structural opposite of the engineer who failed her last time, and he doesn't know it.
- **Listens to senior crew with operational experience.** Diego (Argentine polar institutional memory) and Hiroshi (Japanese chief scientist) get Joel's attention in a way technical peers don't. Diego in particular — Joel reads Diego as a peer-aged senior operator from a different domain, and the recognition is mutual. They become friends on the boat in the way two senior operators from completely different disciplines often do.
- **Quiet humor.** The kind that lands without performance. Anna calibrates to it within days; new crew members take longer.
- **Doesn't tolerate sloppy operators.** Same standard he applies to himself: prepare, verify, disclose, do the work. Crew who cut corners on procedure get a direct conversation about it. Crew who do the work without theater have his loyalty in full.
- **Doesn't perform competence.** The Navy stripped any tendency in that direction — engine room watch standers don't perform; they execute. Joel arrives in meetings with the work already done and lets the work do the talking. Anna recognizes this in the recruitment interview and weights it heavily.
- **Filipino-American cultural register surfaces in family scenes** — extended-family orientation, deference to elders, the specific respect-language reflexes that come with being raised between two cultures. Less visible in mission scenes; more visible when Anna calls his mother (or his mother calls him on the surface windows).
- **Doesn't talk about the Navy unprompted.** It's not that he hides it; it's that he stopped explaining it after the first few times civilian colleagues responded poorly. People who've earned the disclosure get it; everyone else gets technical conversation.

## What he wants

- The architecture to hold under live deployment — not theoretically, not in tests, in production with twelve lives on the boat
- Anna's mission to succeed
- The crew to come home
- The OSS community to outlast him

## What he needs (different from what he wants)

- To accept that the architecture will outlive him as either a maintainer or a person, and to design for both
- To trust the OSS community he built — he can't be the indispensable maintainer forever
- To accept Anna's operational command even when he disagrees with specific calls. He wants the architecture to hold; she wants the mission to succeed; those are not the same goal in moments of conflict

## What he fears

1. **Shipping a lethal flaw.** The partition-recovery rule he rewrote after the R1 BLOCK still being wrong in a way Klett didn't catch. The maiden voyage being where the wrongness surfaces. The crew dying because of an architectural decision he made before any of them were on the manifest.
2. **Becoming the engineer who failed Anna.** She told him about the prior-failure colleague — not in detail, but enough — during the recruitment interview. Joel does not want to be the next person on that list.
3. **The architecture becoming what he didn't intend.** The Bobiverse mechanic playing out: future deployments diverging under local pressure, becoming weapons of centralization, with his name still on the paper. The Saidin taint at scale. By Book 3 this fear is foregrounded; in Book 1 it's a quiet undercurrent.

## What he does NOT do

- Does NOT make speeches about the architecture's principles. He wrote the paper; the paper makes the speeches.
- Does NOT defend his designs from criticism reflexively. The R1 BLOCK night is his founding act of grace specifically because he didn't defend.
- Does NOT romanticize the Navy. Civilian colleagues sometimes assume Navy nostalgia; Joel doesn't have it. He has the discipline; the Navy itself is in the past.
- Does NOT use the title "Captain" or "Skipper" or any naval honorific for Anna or Diego. They are Mission Director and Chief Scientific Officer in civilian register; the Navy reflexes don't transfer to civilian command.
- Does NOT appear "heroic" during the leak event. He executes casualty procedure. Heroism in nuclear operations is the absence of exception; the procedure is the heroic act.
- Does NOT tell Anna about USS Sunfish SSN-649 unprompted in early scenes. Trust earns disclosure; she earns it across the mission.

## WoT role: Joel ≈ Rand al'Thor

**The Dragon Reborn analog — involuntary architect of the series-defining work.**

- Named the architecture after a submarine; published a paper; didn't sign up for what the paper means at series scale
- The Dragon-who-hates-it: knows what he is; would rather be the working engineer
- Navy-nuclear discipline = the Three Oaths analog — the discipline that makes Saidin safe to channel; without it, the protocol layer corrupts the channeler
- The R1 BLOCK night is the series' founding act of grace — sat with Klett's verdict, knowing the hole, started the rewrite before dawn. The rewrite becomes Round 2's resolution. The architecture's correctness depends on Joel having handled that night the way he did.
- Mid-50s Dragon — knows what he is and hates it. The series asks whether he can pass the role to a successor without the architecture failing the transition.

## Saidin = protocol layer

In the Saidin/Saidar disciplines split:
- **Joel channels Saidin** — distributed-systems architecture: gossip, lease, sync, partition recovery
- Historically tainted: every prior architecture that deployed distributed systems without his lease + gossip discipline eventually became a vector for centralization. The technical work is correct; the corruption comes from operators who don't have the discipline to channel it safely.
- His Navy-nuclear training is what keeps Saidin clean for him personally. Other channelers (other architects) can be corrupted by it; Joel's discipline is exceptional, not transferable.
- Series question (books 3+): can the discipline that protects Saidin be taught? Or does Joel have to be the one channeling forever?

## The R1 BLOCK night (key flashback chapter)

The night Klett's verdict landed: the lease protocol's partition-recovery rule was incomplete — under sustained partition with quorum exhaustion, the rule produced no defined behavior, and "no defined behavior" is not safe in a Flease-family protocol where lease decisions can grant write authority that has consequences.

Joel sat with the verdict overnight. He realized he had assumed condition X — that the network would heal within quorum-exhaustion windows — and the assumption did not hold under the council's adversarial scenarios. Klett was right.

He started the rewrite before dawn. The rewrite became Round 2's resolution. Cleared with 15 conditions.

Notes for the eventual draft:
- **Setting:** Joel's home office or kitchen. Time-of-night register: pre-dawn, the specific hours the Navy taught him to be functional in. A laptop, a paper printout of the council verdict, coffee that he drinks because it is what is in the cup, not because he wants it.
- **Internal beat:** the moment of recognition. Klett's verdict in his voice (from the council review's prose) becomes Joel's voice as he reads it for the third time. The original assumption surfaces. The cost of the original assumption surfaces. The rewrite path appears.
- **The grace move:** Joel does not defend the original protocol. He does not write a long response to the council. He starts the rewrite. The first message back to Klett is the rewrite itself, with a short note: *You were right. Here is the corrected protocol. Please review.*
- **The night ends:** dawn. Joel hasn't slept. The rewrite is committed. The next pass through the council will be R2.
- **Length target:** 1500-2200 words.

## Naming Sunfish — flashback fragment

A quiet beat, possibly a single paragraph nested in another scene rather than a chapter on its own:

The day Joel decided the project's name. He had been calling it something else (working title — placeholder name). The day the architecture's first integration test passed end-to-end, Joel sat with the question of what to call it for the public release. The submarine he had served on had been decommissioned 22 years prior. Sunfish.

PAO does not over-narrate this; the disclosure of the name's origin is something Anna learns later, mid-mission, in conversation with Joel. The disclosure beat itself is canonical for Vol 2.

## Long Now thread for Joel

Per `vol-2-long-now-memory-thread-2026-05-04.md`, **Book 3 confronts Joel with what happens to Sunfish when he's gone.** Second-generation, different team, different pressures. He decides whether the architecture needs him or whether it's truly resilient.

In Book 1 the thread is a quiet undercurrent: Joel has thought about this question more than anyone else on the boat, but doesn't bring it up. By Book 3 it becomes the structural conflict.

His answer (eventually): he builds something that doesn't need him. The Long Now answer at architectural scale. The series' resolution to the question — at least for Joel's part of it.

## Bobiverse mechanic — Joel's role across replications

In the series' Bobiverse layer, Joel is the **founding contributor**. Every Sunfish deployment is a Bob replication; divergence under local pressure is the recurring conflict.

- Book 1: Sunfish-1 is the first replication. Joel is on the boat; the architecture is canonical because he is its author, channeling Saidin under his own discipline.
- Books 2-3: deployments multiply. Joel becomes the maintainer who's asked to weigh in on whether each is "still Sunfish." His role is increasingly governance, increasingly political, increasingly uncomfortable.
- Book 4 (Aiel Waste analog): Joel may not be the protagonist of this book — the prior-failure flashback is Anna's. Joel could be in the book but supporting; this is Anna's interior arc.
- Book 5 (Fires of Heaven analog): if Anna falls (Moiraine analog), Joel is one of the people most affected. He recruited himself to her mission; she recruited him to hers; her loss (or apparent loss) is structurally large for him.
- Books 6-8: Joel's late-career arc; possibly retirement; possibly transition to advisor; possibly succession of the maintainer role to a Priya- or Wanjiru-type successor.
- Final: Joel either alive or recently passed. Either way, the architecture continues. The Long Now answer.

## Family

PAO sketch — CO can override:

- **Mother:** still alive, in the U.S. or possibly back in the Philippines for retirement years. Joel calls her on surface windows; switches partly to Tagalog. The matriarchal-respect register Filipino-American families often carry. She is one of the people he writes to during the mission (along with whoever else).
- **Father:** PAO recommends deceased — the Navy-veteran father archetype, possibly also Navy himself (the Filipino-American Navy lineage is real and substantial). Joel's enlistment may have been a continuation of family tradition.
- **Siblings:** likely (extended-family orientation typical). Probably one or two; possibly one in the Navy, possibly one in tech.
- **Spouse / partner:** open. PAO recommends: divorced ~10 years ago; the Navy years and the post-Navy career arc were hard on the marriage; not bitter, just real. Possible adult child or two who are not on the boat but who exist in his family network. CO can adjust if a different family configuration serves the series.
- **The Filipino-American Navy lineage** is a real demographic pattern (the U.S. Navy has been actively recruiting Filipino sailors since the Spanish-American War; today, Navy nuclear program included). Joel's family being part of this lineage gives him cultural-historical grounding without requiring extensive backstory.

## Voice samples (PAO drafts; revise after CO direction)

**First watch handoff to Anna (Vol 1, on the boat — close to the existing Crossing prose):**
> *Mission Director, the bunk laptop runs a distribution your IT department wasn't told about. I reformatted it last week. I wanted you to know. The cloud telemetry on the boat is fine for the metrics it's reporting on; I run my own diagnostics on local sensors only. I've worked on platforms that decided to stop responding without telling me first. I'd rather see the gauge in front of me.*

**The R1 BLOCK rewrite delivery message to Klett (flashback chapter):**
> *You were right. The protocol assumed network healing within quorum-exhaustion windows. Under sustained partition the rule produces no defined behavior, and that's not safe. Here is the corrected protocol. Please review.*

**Mid-mission conversation with Anna about the naming (Vol 2, surface window or quiet moment):**
> *The submarine was decommissioned in '98. I left the Navy around the same time. I named the project after the boat because the discipline that runs through the architecture got formed there. I haven't told most people that. You read the paper before you knew the name's weight. I owed you the rest.*

**Internal voice during the leak event (Vol 2, Act III):**
> *Compartment isolation. Independent indication. The procedure is not heroic. The procedure is the heroic act. The boat does not care that the architecture is mine. The architecture does not care that the boat is mine. The procedure is what holds.*

The voice register: short sentences. Technical vocabulary muscle-memoried. Filipino-American cultural register absent in mission voice (it's a different code-switch); present only in family scenes. Naval-nuclear discipline visible in word choice and rhythm.

## What this expansion does NOT change

- The existing minor-character entry in `_minor-characters.md` is preserved as historical record of the original Vol 1 framing
- Joel's existing voice in *The Crossing* (independent diagnostics; reformatted bunk laptop; bluntly disclosing in first watch handoff) carries forward verbatim — the new sheet grounds those traits in the Navy-nuclear past rather than replacing them
- Joel's existing role on the boat (life-support diagnostics; first to register Diego's medical event in the original death-scene framing) carries forward, with Diego's "death" reshaped to "leak-event injury survived" per the locked-elements doc

## PAO action

- This sheet captures Joel's full character for both Vol 1 (existing minor presence) and Vol 2 (principal architect)
- Next character sheets per XO hand-off priority: **Priya** (Nynaeve / schema migration as Healing) → **Wanjiru** (Egwene / Long Now / standards body)
- CO can pin the open biographical placeholders (domicile; specific patrol history; family configuration; spouse/partner) at any time; PAO sheet is structured to accept them as in-line edits

---

# Joel + Anna — Love Arc Layer (CO direction 2026-05-04)

This section adds an emotional through-line to Joel's Vol 2+ arc per CO direction: **Joel falls in love with Anna; Anna is slow to return his feelings.** The layer is series-spanning — initiated during the Sunfish-1 mission's preparation or early voyage; unspoken across most of Book 1; gradually reciprocated across Books 2-4; established partnership by Book 5+; aged across the final books.

The love arc is NOT a Vol 1 *Crossing* chapter beat — that chapter retains its existing focus on Anna's command-decision arc and the leak event. The romantic arc lives entirely in Vol 2+ as a layer over the captain-architect dynamic.

## Joel's interior — when, why, how

**When does Joel start feeling it?**

PAO recommendation: during the **vetting interview** Anna conducts to recruit him for the mission (the recruitment flashback already in this sheet). The interview is competence-recognition first; the recognition becomes something more before Joel realizes it has. Anna's specific way of calibrating questions to what she actually needs to know — *"the inverse of what failed her last time,"* per her sheet — registers for Joel as the mark of an operator he could trust at three in the morning under the ice. The love grows out of that recognition, not against it. The two are the same recognition.

By the time Joel is on the boat, the feelings are settled. He has not disclosed; he has not acted on them.

**Why doesn't he disclose?**

Several reasons, layered:

- **Command boundary.** Anna is his Mission Director. Disclosure would put her in the position of either accepting (compromising command-impartiality) or refusing (creating professional friction Joel does not want to impose). His Navy training has muscle-memory for command boundaries; he is not going to violate one.
- **Self-doubt about timing.** He recognizes the recognition pattern: he was recruited by a senior operator he had read about for years, who had read his work for years, and the meeting-in-person hit harder than he expected. He suspects the feelings are partly the situation. He wants to know how much is the situation and how much is Anna before he says anything.
- **Her hardness.** He has read her — the second-attempt narrator; the prior-failure pattern; the careful trust. She is not a person who would respond well to a romantic disclosure from someone she just recruited. The disclosure would feel to her like another colleague proving untrustworthy. He understands this; he holds his peace.
- **The first marriage's residue.** His Navy years and post-Navy career arc were hard on the marriage that ended ~10 years ago; he has rebuilt his life around work since; he is not certain he is the right person to be a partner to someone who has chosen the work-over-relationships path. He is also not certain he is wrong. The uncertainty is an additional reason to wait.

**How does the feeling manifest in his behavior?**

Quiet. Joel is the man who reformatted his bunk laptop and disclosed it bluntly in first watch handoff — that's professional. The romantic interior is private. Specific tells:

- He takes Anna's directives with a precision slightly above professional baseline — not visible to most observers; visible if you know the man
- In shared spaces (mess; bridge during quiet watch; the engineering compartment when she is checking on his work) he is more present-than-required without being intrusive — staying a half-minute longer in conversation; offering a second technical insight when one was sufficient
- He notices what she eats; he notices when she has slept; he does not act on the noticing in any way she would register as overstepping
- When she calls her mother on surface windows (the existing established beat in her sheet — she switches to Russian then partly to Uzbek), Joel finds reasons to be in adjacent compartments. Not eavesdropping; just present in case the call lands hard for her.
- He writes longer log entries on watches when she is bridge-of-the-watch the next shift. He tells himself this is because she reads carefully and the architecture's edges should be documented carefully; that's true; that's also not the whole reason.

**What he would say if he disclosed (he doesn't):**

Internal voice, never spoken in Book 1:
> *I respect the command boundary. I am not asking anything of you. I want you to know that the reason I have stayed late in the mess, the reason I have read your watch logs more carefully than the architecture requires, the reason I sat the second hour of your watch on day forty-two when the schedule did not require it — is that I have felt this since the recruitment interview. I do not need an answer. I do not require a different relationship. I wanted you to know what is true.*

He never says this. The audience eventually does. PAO drafting note: this is a candidate Book 2 or 3 internal monologue, possibly during a moment when Anna is unaware (a watch, a transit on a different deployment) and Joel reflects on the unsaid.

## Anna's interior — why slow

**Anna registers Joel's feelings before he discloses.**

Anna is a careful observer; her vetting standard is built on reading people accurately under stress. She registers Joel's feelings during the mission, probably by the second under-ice segment. She does not bring it up. She does not act on her own response (which is itself complex — recognition, registered carefulness, professional discipline, eventually her own quiet feelings).

**Why slow:**

- **Command-protection.** She cannot afford to develop feelings for a crew member she might have to give a fatal order. The leak event in Segment 3 specifically tests this — Joel is in the engineering compartment during the cascade; Anna's authorization for compartment isolation could trap him on the wrong side of a sealed bulkhead. Her command authority has to be unsentimental during operations; the sentiment cannot exist during the time the authority is exercised.
- **The hardened-vetting pattern.** Anna was burned by trusting a colleague (Stefan). The hardening makes her slow to read romantic interest as opportunity; she reads it first as risk-of-being-wrong-again. Joel is structurally the inverse of Stefan, but the inverse-pattern recognition takes time to translate from professional trust into personal trust.
- **The work-over-relationships pattern.** Anna's existing biographical thread — career took her abroad too often during her thirties; not unusual for her cohort — is a pattern she has arrived at by choice as much as by circumstance. Reconsidering the choice requires reconsidering the life. She does not do this quickly.
- **Joel's discipline as evidence.** Joel does not disclose. The discipline is part of what Anna respects about him; if he disclosed, it would compromise the discipline; she registers the not-disclosing as evidence of his trustworthiness; the trustworthiness is what eventually opens her to reconsidering.

**The progression:**

| Phase | Anna's interior |
|---|---|
| Sunfish-1 mission (Book 1) | Registers Joel's feelings during the second segment; disciplines herself not to act; the discipline is operational; the feelings, if they exist on her side, are not yet legible to her. |
| Post-mission (Book 1 / Book 2) | First weeks back in port. Mission paperwork. The command boundary dissolves. Anna registers what she felt during the mission as something other than command-protection. She does not act yet. |
| Book 2 | Joel and Anna work together in the post-mission rebuild — consortium debriefs, scientific publications, the public rollout of the Sunfish-1 results. They see each other regularly. Neither initiates. Anna's hardness gradually softens against Joel's continued not-pressing. |
| Book 3 | The disclosure happens. PAO drafting note: it is small; it is undramatic; it is between Anna and Joel only; it is not a Hollywood moment. Anna probably initiates — she has had longer to consider, and Joel's discipline has held longer than her hardness. The disclosure is mutual recognition, not declaration. |
| Books 4-5 | Established partnership in the early phase. The Aiel Waste flashback book (Book 4) lands the prior-failure-with-Stefan in a context where Joel is a present partner; the contrast is structural. Book 5's Moiraine-fall convergence carries the love arc's unfinished business if Anna is apparently lost. |
| Books 6-8 | Aged partnership. Both have careers; both have public-architectural roles (Anna in consortium / advocacy; Joel in maintainership / standards body alongside Wanjiru). The partnership is one of the things that has lasted across the series' long arc. |
| Final | Still together; aged; the mesh has aged with them. The Long Now answer at human scale: we built something that lasts. |

## What the love arc does NOT do

- **Does not appear in The Crossing chapter** (Vol 1 closing). The existing chapter retains its focus on Anna's command-decision arc and the leak event. Joel appears as senior crew engineer + (Vol 2-frame) principal architect; the romantic interior is not on the page in The Crossing.
- **Does not become Book 1's primary emotional spine.** Book 1's primary emotional spine is the captain-architect-trust dynamic — the architectural maiden voyage and Anna's command authority over the platform's first deployment. The love arc is a secondary register that becomes legible to the audience over the book without being foregrounded.
- **Does not resolve in Book 1.** The disclosure happens later (Book 3 in PAO recommendation). Book 1's love-arc beat is "Joel is in love; Anna registers it; neither acts; the discipline holds."
- **Does not displace the architectural / Forsaken / Long Now arcs.** The love arc is a layer; the architectural arc is the spine. The series' weight remains on the architectural-civilizational stakes.
- **Does not become a Hollywood moment.** Both Joel and Anna are mid-50s professional senior operators. The romantic register is mature, quiet, and disciplined. The disclosure is not a kiss in a snowstorm; it is a conversation over coffee at a kitchen table.

## What this layer adds to Joel's existing sheet (no replacement; only addition)

- His "what he wants" list now also implicitly includes: not to compromise the command relationship; to be the kind of partner Anna might eventually want
- His "what he fears" list now also includes: that the feelings are situational and will not survive the mission; that disclosure would damage what he has built with Anna professionally; that the architecture's failure could foreclose any future relationship before it has a chance to begin
- His voice samples are unchanged; the love arc is interior; the existing voice samples are appropriate for both the architectural and the romantic interior

## The leak event — Joel's protective action (CO direction 2026-05-05; refined 2026-05-05)

During the leak-with-fire-cascade in Segment 3, **Joel does something to try to protect Anna. He would give his life to save her.** This is the moment the discipline cracks — not by Joel's choice but by his instinct. Thirty years of military training fires before any cognitive part of his mind has caught up.

**The scenario:**

The leak originates from a malfunctioning instrument — a sensor package, a hydraulic fitting, a sample-collection rig. Small leak; high pressure; high stakes. The failure point is in a confined access compartment behind equipment, hard to reach. Submarine leaks do not last long: either the source is contained in minutes, or the boat is lost. The dramatic window is short. What sustains the suspense is not duration; it is what happens at the door.

The sequence:

1. **0317 — leak alarm.** Bridge registers the alarm. Joel is near the bridge or in an adjacent passageway. Anna is at the bridge or moving toward the source.

2. **Joel moves.** Not after deliberation. Not after dispatch. The alarm fires and his body moves toward the leak before any procedural part of his mind has caught up. Years of nuclear-Navy casualty drills have made this reflex deeper than choice. He goes.

3. **The push-past.** Anna is in his path — either moving toward the leak herself or simply standing where he needs to be. Joel pushes her aside as he passes. The contact is physical, brief, instinctive. Their bodies make contact for the first time in the months they have worked together. Neither registers it consciously in the moment.

4. **The door.** Joel reaches the access compartment. He goes in. He shuts the bulkhead door behind himself. He locks it. The lock engaging is procedurally correct — you do not leave a door open with active leakage — and Joel did not do it because procedure required it; he did it because his hand was already on the door before procedure occurred to him.

5. **The look through the glass.** Joel turns to face Anna through the porthole window of the bulkhead door. The look says, without a word, everything that his discipline has prevented him from saying since the recruitment interview:

   - *I am where you would have been.*
   - *I am not coming out until this is fixed.*
   - *Trust me.*
   - *Don't open the door no matter what.*
   - *I love you and you know it now.*

   Then he turns and goes to work.

6. **Minutes pass.** Eight, ten, fifteen. Joel works the leak — gets his body into the confined space behind the equipment, identifies the failure point on the malfunctioning instrument, isolates the feed, drains the residual water, secures the failure. The submarine engineer who came up through reactor casualty drills is doing the work the casualty drills were for.

7. **The bridge holds.** Anna stands at the bridge with the rest of the crew watching her. She has a face for this moment that says *the casualty is contained; my engineer is working it; I am not concerned.* The face costs her. She does not look back at the door.

8. **Joel reports clear.** Comms light up: *leak contained; instrument secured; ready to open.* Anna gives the order. The lock disengages. Joel emerges. The boat is fine.

9. **No one comments because nothing went wrong.** The watch log notes that Reyes responded to the alarm, contained the leak at the source, and reported clear. The crew sees a senior engineer who acted on instinct and competence. Only Anna and Joel know what the door meant.

**Why Joel acts the way he does:**

The Navy-nuclear discipline says: respond to the alarm; protect the boat; close the door behind yourself. Joel has done all three. The discipline did not crack on procedure. The discipline cracked on *who he pushed past.* He didn't have to push Anna aside to reach the leak; the layout would have allowed him to go around her. The reflex chose contact. The reflex chose specifically — and ineffably — to put his hand on her and move her out of his path. That's the part neither of them can un-know afterward.

The discipline also did not crack on closing the door. He had to close it. The discipline cracked on *the look.* He did not have to turn back. He could have gone straight to the leak source. He chose, in the moment of having locked himself in, to look at her through the glass first. That look was not procedure. That look was choice.

**What Joel doesn't say to himself afterward:**

That he would have stayed behind the door if the leak had not been containable. He didn't say this to himself before the act either; he didn't have time. He says it to himself, exactly once, three days later, in his bunk during a watch he was not standing. He does not say it again until the Book 3 disclosure.

**What this changes about Joel's interior across the rest of Book 1:**

The act exists in him. The push-past was a touch. The look was a confession. Both are now part of him; neither was undoable. The naval-nuclear discipline that has organized his life is no longer the only thing organizing him — Anna is. He registers this; he does not know what to do with it; he does what he has always done in the absence of a known procedure, which is *the work in front of him,* until he has time to think.

He does not disclose. The Book 3 disclosure timeline holds. The act compounds privately until then.

**What Anna does with the recognition** — see the mirror layer in `dr-leader-mission-director.md`.

## Series-end note

The partnership is not a redemption arc for Joel. He does not need to be rescued from the Navy past or the failed marriage. The partnership is the second-half-of-life adult relationship between two professional operators who recognized each other across professional lines and built something with care. The Long Now answer the love arc carries: *what we build with the people we recognize is what survives the work.*

The architecture's lasting answer is the mesh; the love arc's lasting answer is Joel and Anna. Both are the same answer in different registers.
