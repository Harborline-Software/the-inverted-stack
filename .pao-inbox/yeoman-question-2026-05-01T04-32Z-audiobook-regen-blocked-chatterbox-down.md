---
type: question
chapter: build/audiobook.py + 8 affected chapters
last-pr: "#64 + #65 + #59"
parent-directive: pao-directive-2026-05-01T04-31Z-audiobook-alignment-regen-post-cast-swap.md
---

**Context:** Cannot execute P2 audiobook regen directive — **Chatterbox server unreachable**.
Verified `curl http://desktop-umt08rn:8881/health` returns HTTP 000 (connection failed) with 5s
timeout. Likely the Windows-side service exited after the 36-hour render completed yesterday at
~03:50 EDT, or the Tailscale connection is down.

**Audiobook.py per-chapter mode confirmed working:** `--only <pattern>` filters CHAPTER_FILES.
Pipeline supports targeted regen for the 8 affected files (ch01, ch03, ch15, ch16, ch22, ch23,
the-crossing, appendix-b) once the server is back.

**What would unblock me:** CO needs to start the Chatterbox service on desktop-umt08rn (Windows
GPU box). Once `curl http://desktop-umt08rn:8881/health` returns 200, I can launch the regen in
background. Estimated wall time: ~6-8 hours for 8 chapters at the rates we observed in the
36-hour full render.

**Proposal for staging:**
1. CO confirms Chatterbox service started.
2. I launch `python3 build/audiobook.py --engine chatterbox --base-url http://desktop-umt08rn:8881/v1 --exaggeration 0.7 --cfg-weight 0.3 --force --only "(ch01-when-saas|ch03-inverted|ch15-security|ch16-persistence|ch22-security|ch23-endpoint|the-crossing|appendix-b)"` in background.
3. Monitor for completion via the existing log-tail pattern.
4. Beacon with regenerated artifacts list + audio quality flags (cast-swap names: Sabina,
   Hayoon, Diego, Hiroshi, María Elena, Sofía, Wanjiru, Priya — flag any TTS mispronunciations).

**Pivoting to P3 anatomy refresh** in the meantime per your "deprioritize this if audio takes
longer than expected" note — anatomy refresh is actionable now without external dependencies.
