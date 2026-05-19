---
type: question
chapter: build/audiobook.py + 7 chapters (P2 audiobook regen)
last-pr: pao-directive-2026-05-01T04-31Z-audiobook-alignment-regen-post-cast-swap.md
parent-question: yeoman-question-2026-05-01T04-32Z-audiobook-regen-blocked-chatterbox-down.md
---

**Half-unblocked.** Chatterbox is back (HTTP 200 on `curl http://desktop-umt08rn:8881/health`). Tried to launch the P2 audiobook regen and hit the next gate: `TTS_API_KEY` env var is required for the chatterbox engine and is not set in my session.

```
$ python3 build/audiobook.py --engine chatterbox --base-url http://desktop-umt08rn:8881/v1 ...
Engine 'chatterbox' requires auth. Set the TTS_API_KEY env var or pass --api-key <token>.
The token is the same Bearer value the Windows server uses for /v1/audio/speech.
```

Searched `.env*`, `~/.zshrc`, `~/.bashrc`, `~/.profile`, `~/.config/`, current env - nothing. CO must have sourced it manually for the prior 36-hour render.

**What would unblock me:** CO sets `TTS_API_KEY` in the shell (e.g. `export TTS_API_KEY=<bearer>`) before invoking `/loop` again, OR CO drops the value into `/tmp/sunfish-prompts/tts-api-key.txt` and I source it before launch.

**Scope correction from prior beacon:** I plan to launch regen for **7 chapters, not 8** - appendix-b is excluded because polish/yeoman-phase4a-appendices has uncommitted prune cuts (-30 words on appendix-b) that PAO hasn't squashed/merged yet. Regenerating against the canonical pre-prune state would mean a re-regen after PAO commits. Once PAO commits the polish branches, I'll regen appendix-b in a separate pass.

7-chapter regen target: `(ch01-when-saas|ch03-inverted|ch15-security|ch16-persistence|ch22-security|ch23-endpoint|the-crossing)` - estimated ~5–7h wall time (~6/8 of the 36-hour full render).

**Status while waiting:** Continuing /loop polling. Will re-check Chatterbox + env on next wake.
