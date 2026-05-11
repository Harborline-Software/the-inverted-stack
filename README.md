# The Inverted Stack: Local-First Nodes in a SaaS World

A practitioner book for software architects, technical founders, and senior engineers
building production-grade local-first systems.

**Status:** In active development — Part I drafting

---

## What This Book Is

Modern SaaS puts the database in someone else's cloud and calls it a feature. *The Inverted
Stack* argues for a different default: a full-capability node on the user's machine — UI,
business logic, sync daemon, and encrypted local storage — with the cloud reduced to a
relay and backup peer.

This is not a toy sync demo. It is a complete architecture for production software:
CRDT-backed document stores, distributed lease coordination for CP-class records,
a five-phase gossip anti-entropy protocol, DEK/KEK envelope encryption, and a
schema migration strategy that survives mixed-version fleets.

The architecture was stress-tested by a five-member adversarial council across two rounds.
Part II of the book documents what failed on first inspection and what changed to pass the second.

## Reference Implementation

**Sunfish** (`github.com/ctwoodwa/Sunfish`) is the open-source reference implementation
developed alongside this book.

- **Anchor** — Zone A local-first desktop (.NET MAUI Blazor Hybrid)
- **Bridge** — Zone C hybrid multi-tenant SaaS (.NET Aspire, Blazor Server)

## Structure

| Part | Chapters | Words |
|---|---|---|
| I — The Thesis and the Pain | 1–4 | ~15,000 |
| II — The Council Reads the Paper | 5–10 | ~20,000 |
| III — The Reference Architecture | 11–16 | ~22,000 |
| IV — Implementation Playbooks | 17–20 | ~14,000 |
| Epilogue + Appendices | — | ~10,500 |
| **Total** | **20 chapters** | **~83,500** |

See `book-structure.md` for the full chapter-by-chapter outline.

## Building

```bash
make draft-pdf     # Full manuscript draft (requires Pandoc)
make word-count    # Word count per chapter vs. targets
make epub          # ePub for Leanpub preview
```

## Generating audiobook chapters

The audiobook pipeline (`build/audiobook.py`) talks to a Chatterbox (Resemble AI)
TTS server running on the Windows GPU box, reachable over Tailscale. A wrapper
script renders one chapter end-to-end with the flags-of-record already wired in:

```bash
export TTS_API_KEY=<bearer-token>            # required, from the TTS server admin
./build/render-chapter.sh ch01-departure      # Vol 2 chapter slug
```

The chapter slug is the MP3 filename without the extension — the same slug that
appears under `build/output/audiobook/vol-1/` or `vol-2/`. List existing
renders to find slugs:

```bash
ls build/output/audiobook/vol-2/*.mp3
```

What the wrapper does (and why):

- Targets `http://desktop-umt08rn:8883/api/v1` (the chatterbox-tts endpoint;
  the older `:8881/v1` path returns 405 / has a 30s proxy timeout).
- Passes `--no-chapter-map` so `--preset` is honored. The default preset map
  otherwise routes some chapters to alternate voices.
- Defaults the preset to `ciufi-galeazzi` (the cloned voice currently used for
  Vol 2). Override with `--preset <name>` if needed.
- Wraps the python process in `caffeinate -disu` so display sleep, idle sleep,
  and system sleep cannot kill the render — chapter renders take 30-90 minutes
  wall-clock with the cloned voice and per-sentence chunking.
- Detaches via `nohup &` so closing the launching shell does not terminate the
  render. The script exits in ~1 second; the render keeps running.
- Writes a timestamped log to `build/output/audiobook/_logs/<chapter>-<ts>.log`.

Follow progress (the log is printed when the script exits):

```bash
tail -f build/output/audiobook/_logs/ch01-departure-*.log
```

The TTS pipeline is content-addressed: every per-sentence chunk is hashed
and cached under `build/output/audiobook/_chunk_cache/`. Re-running a render
reuses unchanged chunks and only re-synthesizes sentences whose source text
moved. To force a clean render (e.g. after upgrading the TTS model), delete
the relevant cache entries before invoking the script.

For the underlying CLI surface (engines, additional presets, Kokoro fallback,
Higgs Audio, voice cloning), see `build/AUDIO-DOCKER.md` and run
`python3 build/audiobook.py --help`.

## Contributing

This book is CC-BY 4.0. Contributions welcome — see `CONTRIBUTING.md`.
Technical corrections, improved examples, and additional war stories are especially valuable.

## License

[Creative Commons Attribution 4.0 International](LICENSE)
