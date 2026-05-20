# Model weights (Anchor model)

**Plain replacement:**
- *model weights* → *the model file* · *the trained model's parameters* · *the model's learned numbers*
- *Anchor model* → *the on-device model* (already covered by `anchor.md` substitution patterns)

**Longer gloss:** *A trained machine-learning model is, at the end of the day, a large file of numbers - millions of them - that the model uses to turn input into output. Those numbers are called the model's weights. They're produced once during training (which takes a long time and a lot of computing power) and then loaded onto the device that needs to use the model. On the boat, the Anchor model is a model the crew uses for on-device queries during the dive; its weights live in the boat's compute hub.* (use at first occurrence in Ch 1 Wanjiru handoff and Ch 14 leak event)

**Audio replacement:**
- *model weights* → *the model file* on first occurrence in scene; *model weights* afterwards
- *Anchor model weights* → already covered by YAML substitution (*on-device model weights*)
- *the integrity-keys for the Anchor model* → already covered by YAML substitution

**Keep when:**
- Engineer dialogue (Wanjiru, Joel, Priya) - engineer voice marker.
- Anna's filed log entries.

**Mistaken for:**
- *Weights* (gym weights, postal-package weights, scale weights) - none of these. The technical sense is *the trained-parameter values inside a machine-learning model*.
- *Model* (fashion model, model student, scale model) - the technical sense is *a trained ML model*; the listener may need the longer gloss.

**Feynman test:** *Could a 10-year-old picture this?* Yes - "imagine a robot that's been taught to recognize handwriting by looking at thousands of examples. After all that learning, the robot's brain is just a giant file of numbers - millions of them - that it uses to make its guesses. The model weights are that file." The robot-learning-handwriting image is the workshop entry's load-bearing element.
