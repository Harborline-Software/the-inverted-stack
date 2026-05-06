---
title: "The Schema That Should Not Migrate"
volume: 2
act: 3
chapter: 13
mission-day: 43-44
icm-stage: icm/draft
word-count-target: 10000
log-opener-pattern: B
primary-rail: class-region-institutional-politics
secondary-rail: career-cost-and-aging-out
chapter-version: v1
---

*Engineer's notes — Iyer, P., Lead Instrumentation. Mission Day 43, 1942 local. RV Nansen, MERIDIAN-7.*

*Filing this entry against the migration window scheduled for Mission Day 44 at 0600. I have refused this migration on operational grounds and am filing my refusal of record before the entry that describes how I will run it anyway. Both are required.*

*The refusal: the auxiliary-salinity stream's emergency reclassification — from instrumentation-data-class-3 to instrumentation-data-class-2 with the failure-mode-flag field added — requires a schema migration on a stream that is currently producing readings at one Hz against a probe whose firmware was updated four days ago and whose mid-segment behaviour has not yet completed the standard fourteen-day post-update observation window. The migration also requires a partition-tolerant rewrite of the schema-version handshake at the contraction phase, which under the current single-window-closed-against-Punta-Arenas operational state means there is no third party available for read-confirmation across the ten remaining mission days. The contraction-phase safety property in the architecture's specification requires three-party read-confirmation. The boat has the boat.*

*The refusal is on the record at this filing.*

*The yes-with-conditions: the operational requirement exceeds my verification protocol. I will authorize the migration under three conditions. First, Reyes executes; I supervise; my hands do not touch the keyboard during the migration window. Second, the boat is at minimum operational tempo for the duration of the window; no concurrent writes from other systems while the migration is in flight. Third, if the third pass surfaces a single read-skew event, the rollback is automatic; no human-in-the-loop authorization to roll forward. Conditions accepted by the Mission Director at this filing. Standing four-pass cycle replaces the standard three-pass cycle for this migration only — the fourth pass is the delayed read-confirmation cycle that surfaces clock-skew faults the first three cannot.*

*The migration window opens at 0600 local on Mission Day 44. Rollback path verified. Field-map drafted; cross-check against the historical schema-evolution corpus pending; the local LLM index is current to the last consortium-port pull. Estimated transition window: forty to ninety minutes against the schema's complexity. I will not start without the Director's confirmation at the window.*

*— P. Iyer, Lead Instrumentation Engineer. Filed; hash 7b1c...d4e2.*

---

I had been on the bridge through the routine afternoon watch when Maria came up at eighteen-forty-seven and said Priya had been in the engineering compartment with Joel for four hours and had not surfaced for the wardroom tea at sixteen hundred and had not surfaced for the pre-dinner ration at seventeen-thirty either. Maria did not frame the report as a medical concern. She framed it the way Maria framed things when she was not making it a medical concern but was registering, at the medical-officer's register, that someone on the boat had been on a problem long enough that the body's intake schedule had become information.

I said *acknowledged*.

I did not leave the bridge immediately. The bathymetry was running the half-degree south against the consortium model the way it had run since Day 39 and Diego was at the polar-operations console and the second-watch officer was reading the indications and the routine was the routine. I stood the routine for the next eleven minutes against the hand-off at nineteen hundred. I signed the half-watch at eighteen-fifty-eight. I went down to the engineering compartment.

The compartment was at the lower-deck register I had registered Priya at across Segment 1 and Segment 2 — the calibration hardware racked along the inboard bulkhead, the deployment-rated sensor heads in the steel cradles forward, the workstations along the outboard bulkhead. The lab section ran into the engineering compartment at the bulkhead aft. Priya had set up at the lab-engineering bulkhead. She was at the workstation directly against the bulkhead. Joel was beside her at a second workstation set perpendicular to hers, a metre to her right. A third workstation was up at the bulkhead opposite — the larger screen that ran the local LLM's indexing output, set to read distance for both of them. The screen was up at the schema-evolution corpus's annotated view. The annotation showed the old-schema-to-new-schema field mapping in the two-column layout the corpus rendered at, with the local-LLM's annotations against each field-map row in the third column.

Priya was at her station with three sub-windows open. Pass log. Deviation plot. Schema-version handshake transcript. She was not running passes yet. She was reading. She was reading at the rate at which she read when she was working a problem against the discipline. She had set a clipboard down on the bench beside her at the audible weight she sets things down with; the clipboard was the printed field-map, draft three. She had a coffee on the workstation to her left. The coffee had been there long enough that the ring had darkened on the thermal mug.

Joel had a printed standing-procedure on his workstation and the small engineering laptop beside it. The laptop was open at his standing-watch log. He was reading too. He was at the rate Joel read when he was reading something he was about to operate against. He did not look up when I came into the compartment.

Priya did. She turned her head when I came in. Her shoulders were set. Her jaw was tight. The set was the set I had registered in the lab at Day 5, in the four-pass-signature scene, and again at the segment-boundary anomaly on the morning of Day 39. The set was the set the body held when the discipline was being held.

She said: *Director.*

I said: *engineer.*

She said: *the filing went up at nineteen-forty-two. The conditions are on the filing. Confirmation pending.*

I said: *I will read the filing. I will return.*

She did not say *acknowledged*. She nodded once. She turned back to her workstation. Joel had not yet looked up.

I went to my desk in the wardroom corner. The filing was in the audit log against the engineer's-notes header at the timestamp Priya had named. I read it twice. I read it a third time. The filing's structure was the structure I had read in three of Priya's prior filings on the boat — the refusal of record, the conditions, the safety net, the rollback path — but the load was different. The conditions were tighter. The safety net was tighter. The rollback path was specified at a level of granularity I had not seen Priya specify before. The fourth pass was new.

I closed the filing. I went back to the engineering compartment.

I came in at nineteen-fourteen. Priya turned again. Joel did not. The local LLM screen had shifted — the corpus-annotation view had paged forward by one in the time I had been gone. Joel had paged it. He had been reading the corpus's annotations against the field map at the rate he read against operational documentation, and he was now into the third page of the corpus's record on the contraction-phase rewrite Priya had filed in 2023. The page was the one Priya had written.

I said: *Priya. Walk me through it.*

Priya put the clipboard down. She put it down at the audible weight. She turned her chair half-toward me without leaving the workstation. Joel turned his chair fully. He did not stand. He did not announce. He turned and waited.

Priya said: *the data class is changing. The auxiliary-salinity stream from the starboard probe has been at instrumentation-data-class-3 since deployment. The class assumes nominal probe behaviour and a continuous-reading mode. The starboard probe firmware update on Day 39 — Joel verified the manifest signature; the manifest is in the audit log — included a new failure-mode reporting field at the firmware level. The field is now producing values at the firmware boundary. The values are not propagating into the instrumentation stream because the canonical schema for the auxiliary-salinity stream does not have a place for them.*

She paused. She moved the clipboard a centimetre. She continued.

She said: *the values not propagating is the failure case. The failure-mode field is what the firmware reports when the probe's internal diagnostics catch a state the firmware classifies as anomalous. The field is the early-warning indicator. Right now the indicator is being produced and is being dropped at the schema boundary because the schema does not preserve the field. The probe is currently reporting nominal at the conventional reading. The probe is also currently reporting two anomalous-state events per twenty-four hours at the firmware-diagnostic field. We have not seen the events because the schema is not preserving them.*

I said: *the rate is not nominal.*

She said: *the rate is not nominal. Two events per twenty-four hours is at the threshold the firmware documentation says is the watchword. Five per twenty-four is the firmware's own escalation threshold. We are at two. We could be at five tomorrow. We could be at zero tomorrow. The firmware diagnostic is the early-warning system the firmware was designed with. The schema is suppressing the early warning.*

I said: *the operational case.*

She said: *we have ten days against the chart. The probe is one of two redundant probes on the auxiliary-salinity reading. If the starboard probe fails entirely, we have the port probe; the redundancy holds. If the starboard probe drifts — fails in the way the firmware's anomalous-state events would warn us about, with the schema's current configuration not surfacing the warnings — we will not know about the drift until the cross-check between starboard and port readings exceeds tolerance. By the time the cross-check exceeds tolerance, we have run partial data on a drifting probe for some interval. The interval could be hours. The interval could be days. The data corruption would not be caught at the segment boundary because the segment boundary check works at the schema level, not at the cross-instrument-cross-check level, and the schema currently looks clean.*

I said: *the migration is the only path.*

She said: *the migration is the only path that surfaces the firmware's early-warning field at the instrumentation-stream level. The field has to be at the canonical schema. The canonical schema has to be migrated. The migration has to happen on a stream that is currently producing readings at one Hz under a closed surface window with no third party available for read-confirmation. The architecture's specification says you do not migrate a stream under those conditions.*

Joel had not spoken yet.

He spoke now.

He said: *I read the spec at the contraction-phase clause this afternoon. The spec is the spec. The condition the spec assumes is three-party read-confirmation across the partition. The condition the boat is in is single-party — the boat alone. Priya's rewrite of the contraction-phase mechanism in 2023 was specifically against the case where two parties under partition could each migrate independently and converge with non-identical canonical schemas. The case the boat is now in is one step worse than the case Priya rewrote against. The boat does not have a second party at all. The boat is alone.*

He paused.

He said: *the four-pass cycle Priya is proposing is what the spec would say to do if the spec accommodated the single-party case. It does not. The spec does not contemplate this case. Priya is extending the spec to cover it. She is doing it correctly.*

I said: *the failure modes.*

Priya answered. She did not look at Joel before answering. She had answered the question in her own head before I had asked it. She said: *three failure modes I am sized for. First, read-skew under load — the migration runs the read-confirmation cycle while the stream is still writing at one Hz, and the read-confirmation reads a value that is being concurrently written, and the read returns a stale or torn value that I confuse for the canonical value. The mitigation is the minimum-operational-tempo condition — you suspend the concurrent writes during the migration window. Second, cascade of partially-written records if the migration interrupts mid-pass — pass two writes the new-schema records, pass three reads them back to confirm; if the boat takes a power blip between pass two and pass three on a record, the record is in the new-schema state but the rollback is not yet committed. The mitigation is checkpoint after every pass — the rollback path becomes deterministic at every checkpoint, and we never have more than one record between checkpoint and rollback. Third, identity loss if the rollback is invoked between pass two and pass three. The records have been written at the new schema; the rollback has to know whether to roll back to the old schema or to commit to the new schema; if the rollback path is wrong, the records are lost in a way that the audit log's hash chain does not reconstruct, because the rollback decision was made under partition. The mitigation is the rollback-direction lock — the rollback direction is set at pass one, before pass two writes anything, and the lock is unmovable until the migration completes or fails. The lock direction is rollback-to-old-schema. We do not roll forward at any failure case.*

She finished. She did not soften. She did not negotiate. She had named three failure modes the way she names failure modes — at the level of specificity that demonstrates she had reproduced them in her local mesh before she filed the conditions. She had brought the failure modes the way she had brought the four-pass calibration on Day 5: as facts.

I had heard the shape of this once before, in a session I had read about in the council-review record but not seen in person. The R1 near-BLOCK on the schema-migration mechanism. Three weeks of work, alone in her home office, building the test cases that exercised the third-party-read pattern. The fix had been a constraint added to the spec. The constraint added partition-time. The constraint had been the right constraint; the constraint was now in the audit-log's evolution corpus on the screen across the compartment from us; the constraint was what the boat was now operating under.

I had selected her for this. I had selected her because the schema-migration mechanism was hers, because the careful-conservative-precision was hers, because the body-of-work that arrived at the contraction-phase rewrite was hers. I had not anticipated that the architecture would put her in the case her rewrite did not contemplate. Neither had she.

I said: *the no.*

She said: *the no is on the filing. The conditions are on the filing. The yes is conditional on your acceptance of the conditions.*

I said: *I accept the conditions. All three.*

She said: *acknowledged.*

She did not soften the acknowledgement. The conditions were the conditions. The acceptance was the acceptance. The migration would run at 0600 of Day 44. She would supervise. Joel would execute. The boat would be at minimum operational tempo for the window. The rollback was automatic at the third pass on a single read-skew. The fourth pass was the delayed-read-confirmation cycle. The conditions were now the conditions of record.

I said: *the local LLM.*

Priya said: *operator-tool. It cross-checks the field map against the historical schema-evolution corpus. It annotates the migration steps as they are run. It flags divergence from the corpus pattern. It does not commit. It does not authorize. It does not run a step on its own. Joel runs the keyboard. I supervise. The LLM is the third reader. It is a third reader the way I would have liked to have a third party for the read-confirmation, except it is reading the corpus, not a partition peer. The reading is useful. It is not a substitute for the partition peer the spec calls for. We are not pretending it is.*

I said: *acknowledged.*

She said: *I will be at the workstation at oh-five-thirty-five. Joel will be at his workstation at oh-five-forty. The compute hub is set to suspend RAG indexing at oh-five-fifty against the minimum-tempo window. The boat's master has been advised of the operational-tempo condition through the second-watch officer at nineteen-thirty; I will confirm with him at the morning brief. Wanjiru's relay is dormant; that is the operational state already. Diego will hold the bathymetry refresh at the lower routine rate during the window; he has been advised. Maria will hold the medical bay at routine. The minimum-tempo window is a forty-to-ninety-minute window starting at oh-six-hundred. The boat's master has the window. I will not start without your confirmation at oh-six-hundred.*

I said: *I will be at the bridge at oh-five-fifty.*

She said: *acknowledged.*

I said: *Joel.*

Joel said: *Director.*

I said: *the keyboard is yours during the window.*

He said: *acknowledged.*

He did not embellish. He did not affirm Priya's plan. He had read the spec; he had read the corpus; he had read the field map. He was at the level he stood watch at. He had not yet stood the migration; he would stand it at 0600. The standing was the standing.

I left the compartment at nineteen-thirty-six. The compartment was the compartment. The bulkhead screen carrying the corpus annotation paged forward as I left; Joel had paged it. He was reading.

---

I went to my desk. I had thirty-eight minutes before the second-watch handoff at twenty-fourteen. I sat at the desk. I did not open the terminal. I sat at the desk and held what had been said in the engineering compartment.

Priya had said no. She had said no at the filing. She had said no in the way Priya says no — not as resistance to the work, not as a refusal to engage, but as a refusal to authorize without the conditions that made the work survivable. She had said no on the record. She had said no in writing. The no had gone to the audit log at nineteen-forty-two and was now in the audit log permanently, in the same way the eleven-minute fourth-pass calibration on Day 5 was in the audit log permanently — as a fact of record about how Priya had run her work on this boat.

I had not overridden the no.

I had not wanted to override the no. I had registered, sitting at my desk in the wardroom corner at nineteen-thirty-eight on Day 43 with the second-watch handoff thirty-six minutes away, that I had not even briefly contemplated overriding the no. The no had arrived at the filing; the no had been correct; the conditions had been correct; the yes-with-conditions had been correct. The architecture I had spent the back half of my career running other people's data through had taught me the shape of a refusal-of-record long before I had ever been the recipient of one. I had been the filer of refusals-of-record in my postdoctoral years on the Norwegian Polar Institute side, on the AWI side, on the AARI side. I had filed three I could remember at the level I could remember them, each one against a senior researcher who had wanted to push a deployment past a calibration window I had not been ready to certify. Two of the three had accepted my conditions. One had overridden the conditions and proceeded; the deployment had failed in the way I had said it would fail; the senior researcher had not filed against me afterwards, but I had learned, on that one, that the override had been the failure. The override had been the failure before the deployment had been the failure. The deployment failure had only confirmed it.

I had been on the receiving end of that lesson at thirty-one. I was on the giving-of-it end at fifty-four. I was on the giving-of-it end because Priya had filed her no and I had read the no and I had read the conditions and I had not, at any point in the reading, considered the override. The architecture had Priya's caution built into it as a constraint already; the architecture had the constraint because Priya had filed the original constraint at the council two years before the mission; the architecture's behaviour at 0600 on Day 44 would only hold because the constraint was already in it. If I overrode Priya now, I was not just overriding Priya. I was overriding the architecture's response to the case the architecture had already learned about. I was overriding myself, by way of the protocol I had selected the engineer for.

The selection had been the selection. I had selected her for the migrations she would run on the boat. The selection was what was now operating.

I noted this in my command log at the personal-reflection register. *I am the precondition for the safety net. If I do not respect the no, the yes-with-conditions does not exist; the safety net does not exist; the architecture's response to this case becomes a thing the boat does not have access to. The discipline that holds the migration is procedural. The procedure depends on the command authority respecting the procedure's refusals. I am that authority. The respect is the operational requirement, not the personal courtesy.*

I closed the entry. I did not file it. I marked it as personal-reflection, encrypted under my key, access self-only. The entry would not enter the staff history's main thread. The entry would enter the staff history if and when I chose to surface it, in the curation that would happen after the mission, in the writing that would happen after the writing began.

I went to the bridge at twenty-twelve. I stood the second-watch handoff at twenty-fourteen. I went to my rack at twenty-two-forty-one. I did not sleep until the early hours.

---

I had read the council-review record on Priya's R1 near-BLOCK before I had recruited her. I had read it again at the recruitment meeting in Bengaluru three months before departure. I had carried what I had read in the way one carries the senior context on a senior crew member — in the way the reading shapes the recruitment without surfacing in the recruitment conversation.

The reading. Priya had filed her R2 fix at her home office in Bengaluru, late evening, after three weeks of work. The R1 council had surfaced a near-BLOCK on her schema-migration mechanism: under contraction-phase with an unhealed partition, two nodes that had each migrated independently could converge with non-identical canonical schemas, undetected until a third-party read tried to reconcile them. The original assumption had been that two-party schema-version handshake was sufficient. The discovery had been that two parties could each handshake successfully with the same third party at different times, and the third party would then see inconsistent canonical schemas without an indication of the divergence.

Priya had reproduced the failure mode in her local mesh. She had not patched the code first. She had built the test case. She had run the test case. She had verified the failure. Then she had designed the fix.

The fix had been the explicit-three-party read-confirmation handshake at the contraction phase. The mechanism became more complex. The new constraint required additional partition-time before contraction could complete. Priya had filed the fix with a reproduction case and a test that failed before the fix and passed after. The R2 council had accepted the fix. The constraint had entered the spec.

The reviewer who had signed the R2 conditions was the council's principal reviewer for the schema-migration mechanism. The reviewer was not Joel. The reviewer was the council member whose review had surfaced the original near-BLOCK.

The reviewer had recommended Priya, at the close of the R2 session, as the most reliable schema-migration contributor on the project — *not because her code is the cleanest, but because her temperament is the temperament the architecture's hardest discipline requires*. The recommendation had entered the council's session record. The session record had been one of the documents I had read when I was selecting senior contributors for the Nansen.

I had read the recommendation. I had read the temperament-line specifically. I had registered the line at the level a Mission Director registers a recommendation about a senior crew member from a council reviewer — at the level that says, *this is the sort of recommendation that gets people on boats; this is not the sort of recommendation that gets people taken off them*. I had not held the line in active memory afterwards. The line had landed in the substrate. It was now coming back to the surface — at twenty-two-forty-three on Mission Day 43, ninety hours from Punta Arenas surfacing, with the migration scheduled for 0600 of Day 44 — at the level the substrate brings things back up when the substrate has decided the things are now operationally relevant.

The reviewer's recommendation had been correct. The temperament-line had been the correct line. The architecture I was about to run a migration against was the architecture Priya's temperament had built the constraint into. The constraint was the constraint that the boat would now operate under. The constraint existed because of who Priya was. The case the boat was now in — single-party migration, no third party available — was a case the spec did not contemplate; Priya was extending the spec; she was extending it correctly because the temperament that had filed the original constraint was the temperament that was now filing the four-pass extension.

The protocol existed in this form because Priya's caution had been built into it as a constraint. The constraint had become the spec. The spec was now the architecture. The architecture was now the boat's only protection against the case the boat was now in. The chain ran the way the chain ran. The chain ran because the temperament was what the temperament was. I had selected for the temperament. The selection was now operating.

I noted the recognition. I did not file it. I held it. I went to sleep.

---

I came onto the bridge at oh-five-fifty on Day 44.

The boat's master was at the bridge. He had been advised at the second-watch handoff and again at the morning watch. He confirmed the minimum-operational-tempo window: oh-six-hundred to oh-seven-thirty as the outer envelope, oh-six-hundred to oh-six-forty-five as the expected interior. The boat would hold trim against the standard operational depth on bearing two-three-seven. The acoustic floor would be allowed to lay down at the routine register; the bathymetry refresh at the polar-operations console would drop to the standard rate; Diego had agreed at the morning brief at oh-five-thirty. The compute hub had suspended RAG indexing at oh-five-fifty against the indexer's standing-suspension procedure. Wanjiru's relay was dormant; the comm watch was at minimum register; the second-watch officer in the comm space had been advised. Maria was at the medical bay at routine watch.

The boat was the boat at minimum tempo. The conditions were the conditions Priya had set.

I went down to the engineering compartment at oh-five-fifty-five.

Priya was at her workstation. She had been at her workstation since oh-five-thirty-five. She had run the rollback-path verification one more time at oh-five-forty-eight against the standing rollback procedure; the verification had cleared at oh-five-fifty-two. She had set up the third workstation's screen with the local-LLM corpus-annotation view paged to the contraction-phase entry. She had a clean clipboard on the bench beside her. She had a fresh coffee. The fresh coffee had a ring on the thermal mug from the night's earlier coffee that she had not finished.

Joel was at his workstation. He had been at his workstation since oh-five-forty. His standing-watch log was open. His engineering laptop was on the workstation to his right. He had a printed copy of the migration field-map at the top of his console, set at the angle he set printed procedures at. He had a printed copy of the rollback procedure beside the field-map. The printed copies were the printed copies. He had read both at the rate he read operational procedures at. He had read both twice.

The compartment was quiet. The engineering compartment's hum was the hum the compartment carried. The bulkhead screen with the corpus-annotation view was up. The local-LLM was running at the index-only profile; it had not been issued any prompts since oh-five-thirty. The third reader was the third reader. It was reading.

Priya turned when I came in.

She said: *Director.*

I said: *the conditions hold. The boat is at minimum operational tempo. Authorization confirmed at oh-six-hundred.*

She said: *acknowledged.*

She turned to Joel.

She said: *Reyes. Pass one.*

Joel said: *acknowledged. Pass one. Loading old-schema definition from the canonical record at the segment-boundary state. Confirmed. Loading new-schema definition from the migration-version registry. Confirmed. Field map version is draft three from the night filing. Confirmed against the corpus-annotation view. Loading.*

He typed. The pass log on Priya's workstation registered the entry. The pass log read *PASS 1 — INITIATED — 0600:14*.

Priya watched the pass log. Her shoulders were set. She was counting. Her hands did not move.

Joel said: *old-schema fields read. Confirmed eighteen fields. New-schema fields ready. Confirmed nineteen fields — the firmware-failure-mode field is the new addition. Field-map application loading.*

The pass log registered *FIELD MAP APPLY — INITIATED — 0600:42*.

Joel said: *applying. Field one — timestamp-of-record. Mapping unchanged; old field name to new field name; type preserved; serializer preserved. Apply confirmed at the application-side. Reading at the canonical record.*

The pass log registered the field-one entry. Priya's deviation plot updated. The first row registered green at the apply column; the read-back column did not yet populate.

Joel continued. Field two — instrument-id. Field three — reading-value. Field four — reading-units. Field five — measurement-confidence. Field six — sensor-state-at-capture. He read each field as he applied it. The pass log registered each entry. The deviation plot's apply column populated row by row. The read-back column lagged by the read-confirmation latency the architecture's pass-one cycle required. The read-back column began to populate at field three; by field eight, the read-back column was within four fields of the apply column.

Pass one continued. The cycle lasted six minutes and eleven seconds against the field-map's eighteen-to-nineteen field expansion. The local-LLM annotation registered a single divergence at field eleven — the auxiliary-state-flag field — where the corpus annotation flagged a serializer change in the corpus's reference implementation that the field map's draft three had not picked up. Priya read the annotation. She paused the pass at field eleven. She conferred with Joel. The corpus had picked up a serializer change from a 2024 patch series that the boat's field map had not pulled because the boat's field map had been generated against the consortium's published schema-evolution corpus as of the last consortium-port pull, which was before the patch series had landed. The serializer change was non-substantive at the boat's reading; the field's wire format was identical in both old and new serializer versions. Priya verified the equivalence at the wire format. Joel verified it independently at the standing-procedure level. The local LLM confirmed the equivalence against the corpus's annotation on the patch series. Priya signed off the field-eleven application against the wire-format equivalence note. Joel applied. The pass log registered.

Pass one cleared at oh-six-twelve-thirty-eight. All eighteen fields applied; all nineteen new-schema fields populated; read-back confirmed against the canonical record. The deviation plot was clean. The first checkpoint committed at oh-six-twelve-fifty-one. The rollback-direction lock held at rollback-to-old-schema.

Priya said: *pass one clear. Proceeding to pass two. Pass two is the read-confirmation cycle at the standard latency.*

Joel said: *acknowledged. Pass two.*

He started pass two.

The pass log registered *PASS 2 — INITIATED — 0613:14*.

Pass two read the new-schema records from the canonical record and compared the values against the old-schema-mapped expectations. The cycle ran at the read-confirmation latency the architecture's pass-two procedure specified — slower than pass one's apply cycle, with each read pulling against the canonical record's full hash-chain segment to confirm the entry's commit state. The cycle progressed field by field. The pass log registered each field's read-confirmation. The deviation plot's read-confirmation column populated.

Pass two cleared field one — timestamp-of-record — and registered the read-back value against the apply value.

The deviation plot showed a one-millisecond difference.

Pass-one's apply had read the timestamp-of-record at *2026-09-14T14:32:18.441Z*. Pass-two's read-confirmation read the same field at *2026-09-14T14:32:18.442Z*.

Priya said: *stop.*

Joel stopped.

The pass log registered *PASS 2 — HOLD — 0613:42*.

Joel said: *one millisecond on field one. Within tolerance at the consortium spec. Within tolerance at the firmware spec. Within tolerance at the schema spec. The drift is at the millisecond on a single field.*

Priya said: *the drift is at the millisecond on a single field. The drift is also a drift. We do not commit on a drift.*

Joel said: *acknowledged.*

He waited.

Priya read her workstation. She read the deviation plot. She read the pass log's first-pass entry against the second-pass entry. She read the corpus-annotation view on the bulkhead screen. She read for forty-six seconds. The compartment was quiet. The local-LLM was running at index-only. Nobody else spoke.

She said: *the drift could be a single-frame artifact. The drift could be a clock-domain boundary I have not characterized. The drift could be the canonical record's hash-chain serializer reading the timestamp at a different precision than the new-schema's serializer reads it at. I want a tighter-window read. Run pass two again on field one only at the tighter read window.*

Joel said: *acknowledged. Tighter-window read on field one.*

He set up the tighter-window read. The window was a hundred-microsecond window against the standard millisecond read.

He ran the read.

The pass log registered the tighter-window read.

Pass-one's apply had read the timestamp at *2026-09-14T14:32:18.441Z*. Pass-two's tighter-window read read it at *2026-09-14T14:32:18.4416Z* — a six-hundred-microsecond drift against pass one, on the tighter window.

Priya read the result.

She said: *the drift is recurring. It is not an artifact. The drift is a drift.*

She put her hands on the workstation. She set them down at the audible weight. She did not move them after she set them down. She read the corpus-annotation view at the bulkhead screen. She paged the screen. She paged it twice. She landed on a page that showed a 2025 patch entry against the timestamp serializer in the old-schema canonical implementation.

She said: *the timestamp-of-record on the canonical record was serialized through a clock-domain boundary I had not characterized in the field map. The probe's firmware at the time of the original entry was reading the timestamp from one clock domain — the firmware's internal clock. The canonical record's serializer was committing the timestamp through a different clock domain — the boat's master clock. The two clocks are within tolerance at the millisecond level for nominal operations; they drift at the sub-millisecond level under specific firmware-state transitions. The old schema had been tolerating the drift at the millisecond level because the old schema's read-back was reading the timestamp at millisecond precision and the drift was below precision. The new schema's read-back is reading the timestamp at sub-millisecond precision because the new schema's serializer is the post-2025-patch serializer that exposes the sub-millisecond state. The drift is now exposed.*

Joel said: *the failure case.*

Priya said: *the failure case is that under partition the millisecond drift could compound. I have not characterized the compounding pattern under partition because I had not seen the drift at sub-millisecond precision. If the migration committed against the new schema with the drift in place, and the boat then operated through a partition recovery, the schema's read-confirmation procedure could traverse the timestamp-of-record across multiple schema-migration layers, and the sub-millisecond drift could compound across the layers. The compounded drift could exceed millisecond tolerance after three or more traversals. The exceedance would manifest as a schema-version-handshake failure at the contraction phase, against a record that the schema would treat as inconsistent across the partition. The architecture would then roll back the record. The rollback would be procedural; the architecture would do what it does. But we would have committed a record that the architecture would have to discard later, and the discard would happen during a partition recovery, when the discard's cost is highest.*

She paused.

She said: *the migration cannot commit field one as currently mapped. I rewrite the field-map for field one. The rewrite captures both the firmware-clock timestamp and the master-clock timestamp. The new-schema record carries both timestamps as separate fields. The new-schema's read-confirmation reconciles at read time, not at write time. The reconciliation is deterministic at the read because both clocks are recorded.*

Joel said: *the field count goes from nineteen to twenty.*

Priya said: *correct. The field count goes from nineteen to twenty. The field-map's draft becomes draft four. The corpus-annotation view will need to confirm the twenty-field structure against the corpus.*

Joel said: *acknowledged. Roll pass two back to the checkpoint. Reset the field map to draft four. Reload the new-schema definition. Re-run pass one with the new field map.*

Priya said: *acknowledged. Confirm the rollback-direction lock holds.*

Joel verified. The rollback-direction lock held. The lock was rollback-to-old-schema. The lock was unmovable.

He rolled pass two back to the pass-one checkpoint at oh-six-twelve-fifty-one. The checkpoint held; the deviation plot reset; the pass log registered the rollback at oh-seventeen-twelve. He reset the field map to draft four — the twenty-field version with the dual-timestamp capture for field one. He reloaded the new-schema definition. He re-ran pass one.

Pass one re-ran in five minutes and forty-eight seconds. The dual-timestamp capture applied at field one; both clock readings were preserved against the canonical record; the read-back confirmed both fields populated. The local-LLM corpus-annotation view picked up the field-map's twenty-field structure and registered a divergence at field one — the dual-timestamp capture was not in the corpus's reference implementation, because the corpus had only encountered the single-timestamp pattern. The annotation flagged the divergence as a *novel field-map pattern*. Priya signed off the divergence note. The architecture would carry the dual-timestamp capture as an architecture-extension at the boat's local mesh; the extension would be filed against the corpus at the next consortium-port pull when the boat surfaced. The extension was the boat's adaptation to the case the boat was in.

Pass one re-cleared at oh-twenty-four-eleven. Pass two ran clean against the dual-timestamp field. The drift was reconciled at read time per the rewrite. The deviation plot was clean. The second checkpoint committed at oh-thirty-one-fourteen.

Priya said: *pass two clear. Proceeding to pass three.*

Joel said: *acknowledged. Pass three.*

---

Pass three was the delayed read-confirmation cycle. The cycle ran at a deliberate ninety-second wait between the canonical record's commit and the read-confirmation's first read. The wait was the architecture's mechanism for surfacing read-skew faults that the standard-latency cycles could not catch — the kind of fault that emerges only when the canonical record has had time to settle through any deferred-commit operations, any background hash-chain consolidations, any cross-node replication latencies. On a boat operating under closed surface window with no peer nodes, the cycle was running primarily against the boat-internal hash-chain consolidation. The wait was still ninety seconds. The wait was the wait.

Joel set the timer.

The compartment was quiet. The hum was the hum. The local-LLM bulkhead screen registered the pass-three initiation at oh-thirty-one-fifty-eight. The screen's annotation column waited for the read-back results.

Joel watched his timer. Priya watched her workstation. Neither spoke. The boat's master clock advanced.

At ninety seconds, the cycle ran the read-back. The pass log registered each field's read-back. The deviation plot's pass-three read-back column populated.

Field one — the dual-timestamp capture. Read-back confirmed both timestamps. Clean.

Field two through field seventeen. Read-back confirmed across all sixteen fields. Clean.

Field eighteen — the auxiliary-state-flag field.

Joel read the value: *zero*.

Priya read the value: *null*.

The deviation plot showed the divergence. The local LLM's annotation flagged the divergence at the read-back column.

Priya said: *stop.*

Joel said: *acknowledged. Pass three hold at field eighteen.*

The pass log registered *PASS 3 — HOLD — 0033:42*.

Joel said: *I read zero. The deviation plot reads my read at zero. The new-schema's canonical record at field eighteen is reading zero at my workstation.*

Priya said: *I read null. The deviation plot reads my read at null. The same canonical record is reading null at my workstation. The local LLM's annotation reads null in the corpus-aligned reading.*

Joel said: *the canonical record is one record. The two reads should be identical.*

Priya said: *the two reads are not identical. One of the two is wrong. I want to characterize the divergence before I commit either reading.*

She read her workstation. She read the deviation plot. She read the local-LLM's annotation. She read for fifty-eight seconds.

She said: *the two values represent the same thing in the new schema. Field eighteen is the *measurement-not-reported* indicator — the field that records whether the firmware reported a measurement on this entry or whether the firmware did not report a measurement. The old schema did not have this field; the new schema added it. The field-map for field eighteen, in draft four, defaulted the field to zero on every legacy record where the field had not been reported by the firmware — because the legacy records did not have the field, and the migration default has to be deterministic. Joel's workstation is reading the migration-default value. My workstation is reading the new-schema's read-back value at the canonical record level — which is null, because the legacy record did not have the field, and the new schema treats the absence as null at read time, before the migration default applies.*

Joel said: *the migration default applies after my read.*

Priya said: *correct. The migration default applies at write commit. The default is zero at write commit. The read-back at my workstation is reading the canonical record at the storage layer, before the default applies. Your workstation is reading at the application layer, after the default applies. The two readings are correct at their respective layers. The two readings are also semantically different. Zero means the firmware reported a measurement and the value was zero. Null means the firmware did not report a measurement. We have committed records under the new schema where the firmware did not report a measurement, and we have set those records' field-eighteen to zero by default. We have lost the *did-not-report* state.*

She paused.

She said: *the failure case is downstream. If a future migration treats null as field-never-written but the application-layer treats zero as field-written-with-default, the next architecture upgrade silently loses data. The data lost is the *did-not-report* state — the firmware diagnostic state we are running this migration to capture. The migration is currently configured to suppress the very state the migration is supposed to surface. We do not commit field eighteen at the current configuration.*

Joel said: *acknowledged. Pass three hold at field eighteen.*

Priya said: *invoke partial rollback. Field eighteen only. Roll back to checkpoint two. Re-run pass three on field eighteen with explicit-not-default semantics. The migration default at field eighteen becomes null instead of zero. The legacy records read null because the firmware did not report; the new firmware-reporting records read zero only when the firmware reports zero. The read-back at the canonical-record layer and the application layer are both null on legacy records and zero on new records. The semantics are explicit.*

Joel said: *acknowledged. Rolling back to checkpoint two on field eighteen. Re-running pass three with explicit-not-default semantics on field eighteen.*

He invoked the partial rollback. The rollback procedure ran. The pass log registered the rollback at oh-thirty-six-forty-two. He reconfigured field eighteen with explicit-not-default semantics. He re-ran pass three on field eighteen.

The cycle ran the ninety-second wait. The cycle ran the read-back.

Joel read field eighteen — the application-layer read. The read returned null on the legacy records and zero on the new firmware-reporting records.

Priya read field eighteen — the canonical-record-layer read. The read returned null on the legacy records and zero on the new firmware-reporting records.

The two reads were identical. The semantics were explicit. The local LLM's annotation flagged the explicit-not-default pattern as a corpus-divergent pattern; Priya signed off; the boat would carry the divergence as an architecture-extension at the local mesh.

Pass three cleared at oh-forty-one-twenty-eight on field eighteen. The pass three cycle continued through field nineteen and twenty. Both fields cleared clean at the standard read-confirmation. Pass three cleared at oh-forty-six-fifty-three.

Priya said: *pass three clear. Proceeding to pass four — the delayed read-confirmation at the long-window latency.*

Joel said: *acknowledged. Pass four.*

---

Pass four ran at the four-minute wait. The wait was longer than pass three's ninety-second wait by design — the four-minute window covered the boat's full hash-chain consolidation cycle and any deferred-write commits that could surface in that window. The wait was the wait Priya had specified at the conditions filing the night before.

Joel set the timer. The compartment was quiet. The compartment had been quiet for the better part of ninety minutes. The local LLM's bulkhead screen carried the corpus-annotation view at the field-map's twenty-field structure with the architecture-extension flags on field one and field eighteen.

I had been at the door of the compartment since oh-thirty-five. I had come down from the bridge at oh-thirty after the boat's master had reported the trim was holding clean against the routine register and the bathymetry refresh was at the standard rate and the boat was at the operational tempo Priya had specified. I had stood at the door because I could not contribute to the work. I had stood at the door because I wanted to be in the compartment when the migration cleared or did not clear. I had stood at the door because I was the command authority and the command authority's standing was the standing the work was operating under. Priya had registered me at the door at oh-thirty-six during the field-eighteen rollback. She had not nodded. She had not said anything. She had registered me. The registration was the registration.

The four-minute wait ran. I watched the timer. Joel watched the timer. Priya watched her workstation. The boat's master clock advanced.

At four minutes, the cycle ran the read-back. The pass log registered each field's read-back. The deviation plot's pass-four read-back column populated.

Field one — dual-timestamp capture. Both clocks read clean. The deviation plot showed the dual-timestamp values reconciled at the read time.

Field two through field seventeen. Read-back confirmed across all sixteen fields. Clean.

Field eighteen — explicit-not-default semantics. Read-back returned null on legacy records and zero on new firmware-reporting records. Clean.

Field nineteen — the firmware-failure-mode field. Read-back confirmed against the firmware's diagnostic state at the entry's capture timestamp. Clean. The field showed two anomalous-state events on the back twenty-four-hour window — the events that the old schema had been suppressing. The events were now in the canonical record. The field was capturing what the field had been migrated to capture.

Field twenty — the second timestamp from the field-one rewrite. Read-back confirmed. Clean.

Pass four cleared at oh-fifty-two-eleven.

Priya read the deviation plot. She read it at the rate at which she read deviation plots when the deviation plot had cleared. She read it for thirty-one seconds. She read every column. She read every row.

She said: *pass four clear. Migration complete. Canonical record committed at oh-fifty-two-eleven. The canonical schema for the auxiliary-salinity stream is now version four-point-one-point-zero. The field count is twenty. The legacy records carry the dual-timestamp capture and the explicit-not-default semantics on field eighteen. The new firmware-reporting records carry the firmware-failure-mode field at field nineteen. The architecture-extension flags on field one and field eighteen are filed against the local mesh. The extensions will be filed against the consortium corpus at the next consortium-port pull at Punta Arenas.*

Joel said: *acknowledged.*

Priya said: *the rollback-direction lock releases. The migration is committed.*

Joel said: *the rollback-direction lock releases.*

He released the lock.

The pass log registered the lock release at oh-fifty-two-twenty-six.

Priya said: *the boat returns to operational tempo at the routine register. The minimum-tempo window closes at oh-fifty-three.*

She turned to me at the door.

She said: *Director. Migration complete.*

I said: *acknowledged.*

I went to the bridge. I advised the boat's master at oh-fifty-three. The minimum-tempo window closed. The boat resumed routine. The bathymetry refresh returned to the high rate at oh-fifty-six. Diego was at his console; he had stood the window at the lower refresh; he returned to his standing tempo without comment. Wanjiru's relay returned to comm-watch routine. The compute hub resumed RAG indexing at oh-fifty-eight. Maria stood the medical bay at routine. The boat was the boat.

---

I came back down to the engineering compartment at oh-eight-fifteen.

Priya was at her workstation, filing. Joel was at his workstation, also filing. The local LLM's bulkhead screen had returned to index-only profile. The compartment was at the post-operational register — the register a compartment carried in the half-hour after a procedure had cleared, when the operators were running the closing entries and the muscle memory of the procedure was still in the body.

I had not interrupted. I had come down because I wanted to register the close.

Priya looked up when I came in.

She said: *Director.*

I said: *engineer.*

She said: *the post-migration filing is in draft. The audit-log entry will close at the four-pass-clear timestamp. The corpus-extension filing is queued against the next consortium-port pull at Punta Arenas. The starboard probe's firmware-failure-mode field is now surfacing at the instrumentation-stream level; the back twenty-four hours of suppressed events is now in the canonical record; the events are below the firmware's escalation threshold but above the watchword threshold. I will run the standard cross-instrument-cross-check between starboard and port at the noon brief. If the cross-check holds, the migration's purpose has been served and the probe is now adequately monitored. If the cross-check shows divergence beyond tolerance, the redundancy holds — port carries the auxiliary-salinity reading at the canonical level, and starboard moves to backup until we can verify the firmware state at Punta Arenas surfacing.*

I said: *acknowledged.*

She said: *the migration is committed. The rollback-direction lock has released. The architecture has done what the architecture was specified to do. The four-pass cycle was the right cycle.*

I said: *acknowledged.*

She said: *I will file the post-migration log entry by ten hundred.*

I said: *acknowledged.*

She returned to her workstation. Joel returned to his.

I stood in the compartment for another forty-six seconds. Joel was filing his standing-watch entry at the pass-by-pass register. He read the entry at the rate he filed engineering-watch entries at. He paused at the field-eighteen entry. He looked over at Priya.

He said: *the field-eighteen catch. I would have committed the field at zero. I read the new-schema record at the application layer. The application layer was reading zero. I would have signed off on it.*

Priya said: *that is why I am here.*

He nodded.

He said: *acknowledged.*

He returned to the entry.

I had heard the shape of the exchange before. I had heard it in Joel's recruitment interview — *I had not thought of it that way until you said it* against my question on the lease protocol, in Bengaluru, with the printed paper across the table. I had heard it across Segment 2 in the wardroom — Joel and Priya at the same table, Priya correcting an assumption Joel had made about the schema-version handshake's behaviour under contraction; Joel reading the correction; nodding; saying *acknowledged*. The shape of the exchange was the shape of the exchange. The shape was honest engineering at the level of engineers who knew that the work was the work, and that the work could not be done by either of them alone, and that the discipline that caught what the discipline caught was a property of two minds reading the same record at different layers, not of one mind reading at a higher level.

I had registered the shape twice before. I registered it now in the compartment at oh-eight-seventeen on Mission Day 44, ninety minutes after a migration that I had been five minutes from authorizing without the conditions Priya had filed. The migration would have cleared without the conditions because the architecture's specification was the architecture's specification; the migration would also have committed field one with the millisecond drift uncharacterized, and field eighteen with the *did-not-report* state silently mapped to zero, and the boat would have run for ten days against a probe whose early-warning state was being suppressed at a different layer than the original suppression layer, and the next migration on this boat or any other boat that had pulled the corpus at the consortium-port would have either lost the data or recovered the data through additional partition-time at the consortium's clock.

The architecture was now extended. The extensions were filed. The extensions had been filed because Priya had filed the conditions; the conditions had been filed because Priya had said no; the no had been filed because Priya was Priya.

I left the compartment.

---

*Engineer's notes — Iyer, P., Lead Instrumentation. Mission Day 44, 0954 local. RV Nansen, MERIDIAN-7.*

*Filing the post-migration log entry against the migration window of Mission Day 44 0600 local. The migration cleared at oh-fifty-two-eleven. The four-pass cycle held. Two near-failures during the read-confirmation cycles were caught and rolled back. Closing the engineer's-notes thread on this migration.*

*Pass two surfaced a sub-millisecond drift on field one — timestamp-of-record. The drift originated at a clock-domain boundary in the old-schema serializer that had not been characterized in the field map's draft three. Rolled pass two back to the pass-one checkpoint; rewrote field-map for field one to capture both firmware-clock and master-clock timestamps; reconciliation moved to read time. Migration committed against draft four field-map with twenty fields.*

*Pass three surfaced a divergence at field eighteen — auxiliary-state-flag. Application-layer read returned zero (migration default); canonical-record-layer read returned null (legacy absence). The migration default at field eighteen had silently mapped the firmware-did-not-report state to zero, suppressing the diagnostic information the migration was intended to surface. Invoked partial rollback to checkpoint two; reconfigured field eighteen with explicit-not-default semantics; re-ran pass three. The new configuration preserves the *did-not-report* state at null and the firmware-reported-zero state at zero. Semantics explicit at both layers.*

*Pass four cleared at oh-fifty-two-eleven against the four-minute delayed read-confirmation. All twenty fields confirmed. Architecture-extension flags filed at field one (dual-timestamp capture) and field eighteen (explicit-not-default semantics) against the local mesh. Both extensions queued for filing against the consortium corpus at the next consortium-port pull at Punta Arenas surfacing.*

*The four-pass cycle was the right discipline. The standard three-pass cycle would have caught field one at pass two and would have rolled back; the standard cycle would not have caught field eighteen at pass three because the application-layer read and the canonical-record-layer read divergence required the delayed read-confirmation to surface. The fourth pass was the surface.*

*Migration committed. Canonical schema version four-point-one-point-zero. Cross-instrument-cross-check between starboard and port probes scheduled at the noon brief. Standing engineering watch resumed at the routine register at oh-fifty-three.*

*— P. Iyer, Lead Instrumentation Engineer. Filed; hash 9e3a...82f1.*

---

I read the post-migration filing at ten-oh-three. I read it twice. The filing closed the thread.

I went to the wardroom corner. The boat had returned to operational tempo across the back two hours; the routine had reasserted; Diego had filed the half-degree south on the cross-section read at the noon brief. Priya's cross-instrument-cross-check between starboard and port had cleared at twelve-fourteen against tolerance; the migration's purpose had been served; the starboard probe's firmware-failure-mode field was now surfacing the diagnostic state the firmware had been generating since Day 39; the back twenty-four hours had registered four anomalous-state events, two below the watchword threshold and two at the watchword threshold; none had reached the firmware's escalation threshold; the probe was operating within the firmware's specified behaviour. The cross-check had confirmed the redundancy. The boat's auxiliary-salinity reading was now adequately monitored against the firmware-state the original schema had been suppressing.

I sat at the desk. I read both filings — Priya's pre-migration filing from the night before, and Priya's post-migration filing from the morning. I read them at the staff history's register, which is the register I now read filings at when the filings have closed a thread the staff history will carry.

The two filings were the same engineer's filings. The two filings were not the same in tone. The pre-migration filing was conditional. The pre-migration filing was a refusal-of-record under a yes-with-conditions. The pre-migration filing carried the weight of an engineer who had filed the no first because filing the no was the discipline, and had filed the yes-with-conditions second because the yes was conditional on the no being filed first. The pre-migration filing was the filing of an engineer who knew that her conditions were the conditions the architecture would operate under, and that her conditions had to be on the record before the migration could be on the record.

The post-migration filing was past tense. The post-migration filing was clean. The post-migration filing carried the weight of an engineer reporting two near-failures the discipline had caught. The near-failures were not framed as catastrophes averted. The near-failures were framed as discipline operating as discipline. The four-pass cycle was named as having been the right cycle. The architecture-extensions were filed at the level the extensions would be filed at. The next migration's reader at the consortium corpus would read the extensions and would understand them; the corpus would carry forward.

The differential between the two filings was where the chapter lived. The pre-migration filing was the filing of an engineer holding her work against a case the architecture had not contemplated. The post-migration filing was the filing of an engineer who had run the work and confirmed the architecture's response. The two filings were both her filings. The two filings together were what the staff history would carry. Neither filing alone would have been adequate.

I noted the differential. I held it.

The architecture had behaved as specified. The architecture had also been extended in two places. The behaviour and the extension were both Priya. The behaviour was Priya's filing of the original constraint at the council two years before the mission. The extension was Priya's filing of the conditions at nineteen-forty-two on Mission Day 43 and the dual-timestamp capture at oh-twenty-four-eleven and the explicit-not-default semantics at oh-thirty-six-forty-two. The architecture I had selected the engineer for had Priya's caution built into it as a constraint. The architecture had then asked Priya to extend the constraint into a case the original constraint had not contemplated. The extension had been the filing she filed. The filing had been the work. The work had been the work.

I had not overridden the no. The no had become the yes-with-conditions. The yes-with-conditions had become the migration. The migration had cleared. The architecture had held because the architecture had Priya. The architecture had Priya because I had selected for the temperament that the council reviewer had recommended at the close of the R2 session. The selection had been the operational requirement. The respect of the no had been the operational requirement. The architecture's response to the case had been the operational requirement. The chain ran the way the chain ran.

The architecture had behaved as the architecture was specified. The chapter the architecture was operating in was the chapter Priya's caution had built into it as a constraint, not the chapter the mission was following her caution as a rule. The constraint and the rule were not the same shape. The constraint was structural. The rule was personal. I had spent the morning watching the structural constraint operate. I had spent the morning watching it operate because Priya had filed her work against the constraint, and because I had not overridden the filing, and because the architecture had been built to receive a filing of that shape.

I closed the filing. I noted, at my command log at the personal-reflection register: *the architecture worked because Priya's caution was built into it as a constraint, not because the mission followed her caution as a rule*. I marked the entry encrypted under my key, access self-only, like the prior night's entry. The entry would enter the staff history if and when I chose to surface it.

I did not surface it now. I went to the bridge for the afternoon watch.

The hum was the hum. The bathymetry was running at the high refresh. Diego was at his console at the standing tempo. The boat had ten days against the chart minus one. The boat was the boat.

The wardroom evening tea was the tea we were drinking for the back forty.
