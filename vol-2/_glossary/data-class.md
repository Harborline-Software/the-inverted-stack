# Data class (instrumentation-data-class, failure-mode flag, field-map)

**Plain replacement:** *data category* · *data type* · *data class* (the term is plain enough once defined) · *category-3 data* (when the specific class number is meant)

**Longer gloss:** *Every stream of readings on the boat is sorted into a category - class 1, class 2, class 3 - that says how the system should treat it. The class governs how often a reading is sent, how much it costs in bandwidth, what happens if it gets lost, and what level of human review it needs.* (use at first occurrence in any chapter where the term is doing structural work - Ch 9 sync-daemon triage, Ch 13 schema-migration crisis [auxiliary-salinity stream's emergency reclassification])

**Audio replacement:**
- *data class* → *data category* (audio always; the technical sense of *class* has no everyday anchor for a non-technical listener; the social-class association is wrong-direction)
- *instrumentation-data-class-3* (and other class numbers) → *category-3 instrumentation data* - already covered by YAML substitution `\binstrumentation-data-class-(\d+)\b` → `data class \1`. Audio narrator speaks *data class three* naturally.
- *data-class-2* / *data-class-3* (without the *instrumentation-* prefix) → *category-two data* / *category-three data*
- *failure-mode flag* → *failure-indicator field* (the *flag* metaphor is technical; the listener may picture a literal flag)
- *field-map* / *field map* → *field-by-field map* (clarifies the *map* metaphor)

**Keep when:**
- Priya's Ch 13 dialogue and Anna's Ch 13 filed log entries - engineer voice marker; *data class* and *failure-mode flag* are the procedural-formal register Priya and Anna both speak.
- Cross-references to Vol 1 Ch 7 *The Security Lens* and Ch 11 *Node Architecture* where *data class* governs storage / transmission policy.

**Mistaken for:**
- *Class* (social class, school class, character class) - none of these. The technical sense is *category* or *type*; the closest everyday analogue is *postal class* (first-class mail, second-class mail) - same idea, different domain.
- *Field* (sports field, agricultural field) - the technical *field* means *a single piece of information inside a larger record*; the listener may need the longer gloss to land.
- *Flag* (national flag, signal flag) - the technical *flag* is a marker on a record indicating a specific condition. The listener will picture a literal flag without intervention.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine the school cafeteria sorts every lunch tray into category one, category two, or category three depending on how careful the kitchen has to be with it. The category tells the kitchen how to handle the tray - how often to check it, what to do if it spills, who has to sign for it. The data class is the same idea for streams of readings on the boat." The cafeteria-tray-sorting image is the workshop entry's load-bearing element.
