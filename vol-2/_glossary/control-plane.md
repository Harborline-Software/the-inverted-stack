# Control plane

**Plain replacement:** *the control layer* · *the management layer* · *the layer that decides what happens* (versus the data plane, which is *the layer that moves the data*)

**Longer gloss:** *In a distributed system, the work splits cleanly into two layers: the control plane decides what should happen - which device gets which work, when to start a sync, what to do when something fails - and the data plane actually moves the data around. The control plane is small, careful, and central to the architecture's decisions; the data plane is large, fast, and concerned with moving bits.* (use at first occurrence in any chapter where the term is doing structural work - Vol 2 surfaces *control plane* in Wanjiru's operational triage scenes)

**Audio replacement:**
- *control plane* → *the control layer* on first occurrence in scene; *control plane* afterwards (the *plane* metaphor risks the listener picturing aircraft)
- *data plane* → *the data layer* (same reasoning)

**Keep when:**
- Wanjiru's dialogue - engineer voice marker.
- Cross-references to Vol 1 Ch 14 *Sync Daemon Protocol* and Ch 16 *Persistence Beyond the Node*.

**Mistaken for:**
- *Plane* (aircraft) - direct collision; *control plane* sounds like an aircraft term. Use *control layer* in audio to defuse.
- *Plain* (homophone) - the listener may hear *plain* and infer "ordinary."

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine a busy restaurant: the kitchen makes the food (data plane), and the manager who decides which orders go to which cook, when each cook should start, and what to do when the oven breaks down (control plane). Both are essential; they have different jobs." The restaurant-kitchen-and-manager image is the workshop entry's load-bearing element.
