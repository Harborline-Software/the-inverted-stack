# Node

**Plain replacement:** *device* (when an end-user machine is meant) · *device-side instance* (when distinguishing from cloud-side) · *the node* (in tight prose where context is established)

**Longer gloss:** *In the architecture, every device that runs the local-first software — every laptop, desktop, or workstation that holds its own copy of the data — is called a node. Each node is a full participant; nodes don't depend on a central server to function.* (use at first occurrence in any chapter where the term is doing structural work — Ch 1 Wanjiru handoff, Ch 9 sync-daemon triage, Ch 14 leak event)

**Audio replacement:**
- *node* (architectural sense) → *device* in most contexts
- *the local node* → *the local device*
- *each node* → *each device* or *each device-side instance*
- *node-to-node* → *device-to-device*
- The bare word *node* never has a non-technical meaning a listener will reach for, but it also has zero anchor — it's a vocabulary blank for non-technical readers/listeners. Always expand for audio.

**Keep when:**
- Engineer dialogue (Wanjiru, Joel, Priya) when *node* is the canonical name they would speak aloud. Audio still expands at first occurrence.
- Cross-references to Vol 1 Ch 11 *Node Architecture* — keep the proper name in print; expand for audio.
- Anna's filed log entries where formal procedural language carries the technical noun.

**Mistaken for:**
- *Node* (anatomical / lymph node) — non-technical reader's first association may be medical; the listener has no audio cue to disambiguate.
- *Knot in a string* (the original etymology) — a closer fit to the technical sense but most readers won't reach for it.
- *Server* — distinct concept; in local-first architecture, a node is NOT a server. Servers are central; nodes are distributed peers. Don't substitute *server* for *node*.

**Feynman test:** *Could a 10-year-old picture this?* Yes — "imagine a fishing net stretched between many poles. Each spot where two ropes cross and tie is a knot — a node. The whole net depends on every knot being there; pull one out and the net still mostly works, because every other knot is still doing its job." The knot-in-a-fishing-net image is the workshop entry's load-bearing element.
