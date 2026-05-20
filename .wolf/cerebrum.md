# Cerebrum

> OpenWolf's learning memory. Updated automatically as the AI learns from interactions.
> Do not edit manually unless correcting an error.
> Last updated: 2026-04-23

## User Preferences

<!-- How the user likes things done. Code style, tools, patterns, communication. -->

## Key Learnings

- **[2026-05-20] Bobiverse-warmth rewrite recipe (proven on ch03 + ch12).** When UPF flags a chapter as PRE-BOBIVERSE / RED on NYT profile, the rewrite has a small set of high-leverage moves that consistently move D+ → green-galley + B+ projected: (1) install the parenthetical-aside engine at the chapter's emotional fulcrum first (the load-bearing realization, the gut-hit moment) — use opening parenthetical phrasing like `(Which is the kind of thing you know from departure day...)` or `(The year I finished my doctorate. I noted the coincidence. I did not say anything about it...)` to convert procedural reportage into Anna interior; (2) hunt and replace ALL `the X was the X` / `the X is the X` constructions except up to one that genuinely earns it (the tea-line in ch12; the institutional-weight close where the refrain IS the chapter's institutional commentary); replace with one specific sensory or behavioral detail each, or cut entirely; (3) move major character disclosures to the syntactic close of their paragraph + cut the surrounding procedural sentences that explain them — the reader does the work; (4) add one specific physical detail to every prop the chapter introduces (Edison paperback → creased spine + dog-eared chapter + silver-paste thumbprint), or remove the prop; (5) every "I noted X. I did not name it" beat is the right Anna instinct — preserve them, don't proceduralize them; (6) the chapter's final paragraph before the "I went to my rack" / "I closed the laptop" / Anna-register short close should carry ONE genuine emotional note (in ch12: the postcard-to-Diana beat that won't reach her until docking) — not a procedural summary. Cross-check: register-family ≤3 per chapter with no two adjacent, per ANNA-VOICE.md AP#9. Galley verdict after a clean pass is GREEN with 79/79 detectors passing.
- **Project:** the-inverted-stack
- **Description:** A practitioner book for software architects, technical founders, and senior engineers
- **Sunfish package split - schema migration:** `Sunfish.Kernel.Runtime` owns `ISchemaVersion` (upcaster registration only). `Sunfish.Kernel.SchemaRegistry` owns `ISchemaLens`, `LensGraph`, epoch coordinator, copy-transform migrator, and compaction scheduler. These are separate packages; do not attribute the lens engine to Kernel.Runtime.
- **Sunfish.Kernel.SchemaRegistry DI method:** `AddSunfishKernelSchemaRegistry()` (confirmed in ch11 code example).
- **Lens registration API:** `LensGraph.AddLens()` in `Sunfish.Kernel.SchemaRegistry` - not via `ISchemaVersion`.
- **ICrdtEngine real API:** `CreateDocument(string documentId)` and `OpenDocument(string documentId, ReadOnlyMemory<byte> snapshot)` - both synchronous.
- **IPostingEngine real API:** `PostAsync(Transaction tx, CancellationToken ct)` where `Transaction` = `{TransactionId, IdempotencyKey, Postings, CreatedAt}`.
- **loro-cs state:** Very bare bones (v1.10.3), snapshot/delta/vector-clock surface not exposed, multi-week binding effort needed. YDotNet is the default; Loro is aspirational.
- **SyncState component:** Lives in `Sunfish.UIAdapters.Blazor.Components.LocalFirst.SyncState`, not `Sunfish.Foundation`.
- **TFMs:** `net11.0-windows10.0.19041.0` and `net11.0-maccatalyst`.
- **DI registration for CRDT engine:** `AddSunfishCrdtEngine()`.
- **Sunfish.Foundation.LocalFirst IS a valid package** - `packages/foundation-localfirst/` exists in the Sunfish repo; `AddSunfishLocalFirst()` is a real method (takes no parameters). `LocalFirstMode` enum does NOT exist. Earlier session notes incorrectly marked this package as invalid.
- **AddSunfishKernelSync() and AddSunfishKernelSecurity()** take no parameters - do not invent options lambdas. GossipDaemonOptions uses `RoundIntervalSeconds` (int), not `GossipInterval` (TimeSpan). `AntiEntropyEnabled` does not exist.
- **Package names: Sunfish.UICore and Sunfish.UIAdapters.Blazor** are correct per repo PackageId values. Not `Sunfish.UI.Core` or `Sunfish.UI.Adapters.Blazor`.
- **SyncState enum valid values:** `Healthy`, `Stale`, `Offline`, `ConflictPending`, `Quarantine`. Do NOT use Linked, Searching, Fresh, Unknown, Degraded, or Error - none exist.
- **ILocalNodePlugin real members:** `Id` (string), `Version` (string), `Dependencies` (IReadOnlyCollection<string>), lifecycle method `OnLoadAsync(IPluginContext context, CancellationToken ct)`. Not PluginId, DependsOn, or Register(ILocalNodeBuilder).
- **IStreamDefinition real members:** `EventTypes`, `BucketContributions` - NOT DocumentTypes, StreamId as StreamId type, or BucketPolicy.
- **IProjectionBuilder real member:** `RebuildAsync(CancellationToken ct)` - NOT Build(IProjectionRegistry).
- **AddSunfishPlugin<T>()** does NOT exist in Sunfish repo.
- **GenerateFounderBundleAsync real signature:** `GenerateFounderBundleAsync(string teamName, CancellationToken ct)` - no teamId parameter.
- **IssueJoinerAttestationAsync real signature:** `IssueJoinerAttestationAsync(byte[] teamId, byte[] joinerPublicKey, ReadOnlyMemory<byte> founderPrivateKey, ...)` - NOT GenerateJoinerBundleAsync.
- **AttestationBundle:** No version field inside the CBOR payload - flat array of 7-field attestation records.
- **WriteState enum:** Does NOT exist. Do not reference WriteState.Pending, WriteState.Confirmed, or WriteState.Failed.
- **MDM node-config.json schema:** Known fields: schemaVersion, teamId, relayEndpoint, allowedBuckets, dataDirectory, logLevel, updateServerUrl, enterpriseAttestationIssuerPublicKey. `storageEncryption` field does NOT exist.
- **Mac Python on this workstation:** Only `python3` is available - no `python` symlink. `build/Makefile` uses `PYTHON ?= python3` and `$(PYTHON)` in all recipe lines (added 2026-04-28). Override per-call via `make PYTHON=/path/to/venv/bin/python <target>`. Do NOT add a bare `python` recipe back.
- **Audiobook pipeline on Mac (Kokoro daily-driver):** Kokoro-FastAPI runs as Docker container `kokoro-fastapi` on `:8880` (image `ghcr.io/remsky/kokoro-fastapi-cpu:latest`). Health endpoint `/health` returns JSON `{"status":"healthy"}`. The OpenAI-compatible `/v1/audio/voices` lists ~58 voices; `/v1/audio/speech` accepts `{model:"kokoro", voice:"<id>", input:"<text>", response_format:"mp3"}`. Default chapter-map preset for body chapters is `male` (am_michael+am_fenrir, speed=0.92). End-to-end pipeline validated 2026-04-28: render → normalize-acx → output at 192 kbps mono 24 kHz.
- **Sunfish.Kernel.Audit IS a real package** (verified 2026-04-28 by @technical-reviewer at iter-0026) - `packages/kernel-audit/` exists in the Sunfish repo. Earlier extensions (#48 #45 #47 #9) declared it "forward-looking" in their HTML annotation headers; that's incorrect. Treat as in-canon going forward; existing annotation headers in Ch15 should be corrected on next sweep (low-priority cleanup).
- **Sunfish.Foundation.Fleet is FORWARD-LOOKING, not in canon** (verified 2026-04-28 by @general-purpose code-checker at iter-0033) - `packages/foundation-fleet/` does NOT exist on disk. Ch21:8 correctly declares it forward-looking ("Volume 1 extension roadmap, not yet present in the Sunfish reference implementation"). Any chapter referencing `Sunfish.Foundation.Fleet` must declare it forward-looking, not in-canon. #44 draft incorrectly declared it in-canon at Ch16:134; queued for tech-review fix.
- **Audiobook Windows-side engine is original Chatterbox 500M (Resemble AI)**, deliberately chosen over Chatterbox-Turbo for the headline `cfg_weight` + `exaggeration` emotion knobs (Turbo had inline `[laugh]`/`[chuckle]` tags but weaker numeric control; we picked knobs over tags). **Canonical client guide lives at** `/Users/christopherwood/Library/CloudStorage/Dropbox/ideas/notes/the-inverted-stack/mac-client-guide.md` - read it for the authoritative endpoint contract, validation bounds, and recipes. Server at `http://desktop-umt08rn:8881/v1` (Tailscale `100.99.202.114`, LAN `192.168.8.168`), OpenAI-compatible surface, voice-cloning native, NSSM Windows service auto-restart. Auth: `Authorization: Bearer $TTS_API_KEY` (Bearer only; X-API-Key returns 401). Stock catalog has 16 voices but only 4 are narrator-fit (en_man, en_woman, broom_salesman, mabel) - the rest are sitcom characters / child voices / non-English. Persona slots in `PRESETS_CHATTERBOX` (sinek, practitioner, fenrir) require custom reference-clip uploads via `build/voice_upload.py put <id> --audio <wav> --transcript "..."`. The OpenAI Python client passes `api_key=` as `Authorization: Bearer <key>` automatically - no header surgery needed for synthesis.
- **Chatterbox emotion control: V12 dramatic recipe is `exaggeration=0.7, cfg_weight=0.3`** (verified ear-test 2026-04-28 on Ch15 Uncle Charlie passage - produced clearly better pauses than model defaults). This is the documented "expressive or dramatic" preset from the upstream README. Use for narrative-driven chapters (Part I + Epilogue + the personal anecdotes inside spec chapters like Ch15 §Key-Loss Recovery). Use model defaults (omit both fields) for spec chapters (Part III). Wrapper exposure of these params is V12; Mac-side `audiobook.py` consumption is the follow-up patch.
- **Inline paralinguistic tags do NOT work on this server** (verified 2026-04-28): `[sigh]`, `[laugh]`, `[chuckle]`, `[cough]` are Turbo-only features; the deployed original Chatterbox doesn't parse them. Worse, inserting them into V12-tuned prose actively disrupts the pause structure that `cfg_weight=0.3` produces. **Do not use paralinguistic tags in audiobook renders.** If inline tag support becomes required, the path is a model swap to Chatterbox-Turbo, not a wrapper change.
- **`narratable_text()` espeak hacks hurt Chatterbox** (verified 2026-04-28 ear-test on Ferreira/Ch09 trial render). Three preprocessing passes designed for Kokoro's espeak engine - `PROPER_NOUN_FIXES` ("Tomás Ferreira" → "toh-MAHS feh-RAY-rah"), `ACRONYM_FIXES` ("CRDT" → "C-R-D-T"), and em-dash → comma collapse - all produce noticeably worse Chatterbox output. The dashed pronunciations force letter-by-letter enunciation; the comma-replacement removes the rhythmic pauses Chatterbox relies on. `narratable_text()` is now engine-aware via an `engine` parameter; pass `engine="chatterbox"` to skip the espeak passes. `build_script()` and the main() `--scripts-only`/`--dry-run` paths thread it through automatically.
- **Word-like acronyms must be expanded for Chatterbox** (verified 2026-04-29 ear-test on broom_salesman + Ch01 + Ch18 SaaS samples - fix solid). Chatterbox neural model misreads acronyms that look like pronounceable syllables: "SaaS" → "saaars", "IaaS"/"PaaS"/"IoT" same failure mode. `CHATTERBOX_EXPANSIONS` in `build/audiobook.py` handles these via two ordered patterns per term: first-use parenthetical pattern collapses "SaaS (Software as a Service)" → "Software as a Service" (avoids doubled phrasing), then standalone form expands bare "SaaS" → "Software as a Service". Also handles hyphenated forms cleanly (e.g. "SaaS-to-local-first" → "Software as a Service-to-local-first"). Currently covers SaaS/IaaS/PaaS/IoT. **Verified-safe acronyms (no expansion needed):** KEK + DEK confirmed via 2026-04-29 ear-test using `00c-kek-dek-verification.mp3` excerpt - broom_salesman pronounces both letter-by-letter ("kay-ee-kay", "dee-ee-kay") naturally without expansion. HSM/TPM/GDPR/HIPAA/CRDT/CISO/DNS also confirmed via absence of complaint across pre-fix render. The pattern: short acronyms with explicit consonant-vowel-consonant structure (KEK, DEK) get spelled even though they look pronounceable; the SaaS family gets word-pronounced because of the doubled-vowel "aa" pattern that registers as a syllable. If a new acronym surfaces as misread, ear-test before adding to expansions.
- **Per-voice emotion-knob strategy** (verified 2026-04-28 ear-test on cloned RogerioM/Ferreira): **stock voices** (en_man, en_woman, mabel, broom_salesman) benefit from V12 dramatic recipe (exag=0.7, cfg=0.3) - they're trained for neutral/clinical reads and need expressivity added. **Cloned voices** (LibriVox-sourced reference clips like ferreira-trial-rogeriom) already carry the reader's natural pacing and character; layering V12 dramatic on top over-pushes into stilted enunciation. **For cloned voices use neutral params** (omit --exaggeration / --cfg-weight). Future enhancement: per-voice metadata in `PRESETS_CHATTERBOX` could store recommended emotion knobs (or omit-flag) per slot.
- **Engine-aware chunk budget** (added 2026-04-28): `CHUNK_BUDGETS_BY_ENGINE` in `build/audiobook.py` defaults Kokoro to 700 chars (existing) and Chatterbox to 400. Chatterbox's ~100 sec / ~2500 token output cap silently truncates longer chunks to silence, especially under V12 dramatic recipe (slower pacing) or cloned voices (different sample/char ratios). 400 chars is the safe ceiling that keeps every chunk well under the cap. `render_chapter` looks up the engine-specific budget when calling `chunk_text_paired`.
- **Audiobook universal-narrator decision** (set 2026-04-28): the author chose `broom_salesman` (stock Chatterbox, older British male, Ollivander register) as the SINGLE narrator for the entire audiobook - Parts I/III/IV, Epilogue, Preface, AND all Part II council chapters. No per-persona voicing in the production audiobook. `PRESETS_CHATTERBOX` now routes ALL preset slots (male/female/sinek/practitioner/british/fenrir/etc.) to `broom_salesman`. `CHAPTER_PRESET_MAP` is preserved as-is for Kokoro renders; for Chatterbox it's effectively a no-op since every slot resolves identically. The 5 cloned LibriVox voices (`ferreira-trial-rogeriom`, `shevchenko-trial-yakovlev`, `voss-trial-savage`, `okonkwo-trial-klett`, `kelsey-trial-smith`) are PRESERVED on the TTS server and documented in `references/CREDITS.md` for optional per-chapter regeneration via `--voice <id>` CLI override. Sinek-style author-voice search is CANCELED - `broom_salesman` covers that slot too. Stock voice + V12 dramatic recipe (`--exaggeration 0.7 --cfg-weight 0.3`) is the recommended config for narrative chapters; neutral params for specification chapters.
- **LibriVox attribution policy for cloned voices** (set 2026-04-28): per [librivox.org/pages/public-domain](https://librivox.org/pages/public-domain/), all LibriVox recordings are CC0 public domain. Credit is **NOT legally required** but LibriVox "much prefers" it with a link to their site. We standardize on **three attribution layers**: (1) `references/CREDITS.md` is the canonical version-controlled record, one section per voice with persona/book/reader/URLs/license; (2) the TTS server's `notes` field on each uploaded voice carries the same attribution (accessible via `GET /v1/audio/voices/{id}` for verification); (3) the eventual M4B end-credits track will name readers + LibriVox sources verbally. Workflow: when uploading a new LibriVox-sourced voice, add a section to `references/CREDITS.md` AND set the `notes` field with the standardized format ("Source: '<title>' by <author>. Reader: <name>. LibriVox book: <url> | LibriVox reader: <url> | Used §<sec>, <window>. License: Public domain (CC0). Credit preferred per https://librivox.org/pages/public-domain/."). When promoting a trial voice (`*-trial-*` → clean slug), preserve the attribution unchanged; only the voice ID renames.
- **Server contract per canonical client guide (mac-client-guide.md, 2026-04-28):** `max_new_tokens=2500` ≈ ~100 sec audio cap (operator-tunable in `.env`); concurrency 4 (5th request 503); validation `exaggeration ∈ [0.0, 1.5]`, `cfg_weight ∈ [0.1, 1.0]`, `temperature ∈ [0.0, 2.0]`, `speed ∈ [0.5, 2.0]`; `input` 1-4096 chars; up to 60s warmup after restart; default voice `en_woman` if omitted. Quality (not the cap) is the real chunking constraint - degrades past ~60-90 sec contiguous output. `audiobook.py` `CHUNK_CHAR_BUDGET=700` is in the recommended 600-900 sweet spot. Server tolerates `application/octet-stream` MIME by falling back to filename extension, so vanilla `curl -F "audio=@x.mp3"` works without `;type=audio/mpeg`. The earlier "~40 sec cap" finding was wrong - it was either a transient model state or a different `max_new_tokens` setting at probe time.
- **Audiobook concurrency does NOT help on Chatterbox** (tested 2026-04-28). The canonical guide's "4 simultaneous" is a 503-tolerance threshold, NOT GPU parallel throughput. Chatterbox doesn't batch on the GPU; concurrent requests serialize at the model layer. A/B on Ch05 (3 prose chunks): serial 29.2s vs concurrency=4 36.2s (24% SLOWER due to coordination overhead). A/B on Ch06 (2 prose chunks): serial 54.8s vs concurrency=2 55.4s (identical). Implementation was attempted via `ThreadPoolExecutor` (synth phase parallel, write phase serial - chunks finished in correct order, smoke clean) but produced no wall-clock win. **Reverted.** Future sessions: do not re-add `--concurrency` to `audiobook.py` for Chatterbox without server-side batching support. If a different engine (Kokoro local Docker, OpenAI cloud TTS) ever shows GPU parallelism, re-evaluate then.
- **LibriVox sifting workflow** - `build/librivox_browse.py search/sections/preview/extract`. The API at `https://librivox.org/api/feed/audiobooks/?format=json&extended=1` returns books with sections including `listen_url` (archive.org MP3) + per-section `readers[]`. Solo books: every section has the same single reader_id. ffmpeg with `-ss <time> -i <url> -t <length>` does HTTP range requests against archive.org (which supports them) - pulls ~250KB instead of full ~14MB chapter. Default extract is WAV 24kHz mono (matches Chatterbox internals). Skip the first ~1:00 of any LibriVox section to avoid the boilerplate intro ("Section N of <book> by <author>, read by <reader> for LibriVox") and last ~10s for the closing boilerplate.
- **Inference Studio server topology (2026-05-07):** The Windows GPU box runs two services: (1) Inference Studio front-end proxy at port 8881 - routes TTS under `/api/v1/{path}` (NOT `/v1/{path}`); has a hard 30-second upstream gateway timeout to port 8883; serves OpenAPI at `/openapi.json`. (2) Direct TTS backend at port 8883 - same `/api/v1/audio/speech` path; no proxy timeout; can sustain multi-minute requests for long sentences. For `--engine chatterbox` renders use `--base-url http://desktop-umt08rn:8883/api/v1` to bypass the proxy timeout. The `default_base_url` in `ENGINES['chatterbox']` was updated to `http://desktop-umt08rn:8883/api/v1` (bug-189 fix, 2026-05-07). The old `http://desktop-umt08rn:8881/v1` base URL returns 405 on all endpoints.
- **ciufi-galeazzi voice inference throughput (2026-05-07):** The ciufi-galeazzi cloned voice on the Windows GPU box synthesizes at approximately 3-10s for short sentences (<20 words), 20-80s for medium sentences (20-60 words), and >5 minutes for very long sentences (80+ words / 400+ chars). Inference time is highly sensitive to sentence complexity and word count - not just character count. With `--per-sentence` mode and 270 sentences, a full Vol 2 chapter render takes approximately 2-3 hours wall-clock. The per-chunk cache in `synth_chunk` means crashed renders can resume from the last completed chunk.
- **CHAPTER_PRESET_MAP overrides --preset for ciufi-galeazzi Vol 2 renders:** All Vol 2 chapters have `CHAPTER_PRESET_MAP` entries pointing to `female-solo` (draft voice). To use `--preset ciufi-galeazzi` for a final render, ALWAYS pass `--no-chapter-map` to prevent the chapter map from overriding the preset back to `female-solo`/`broom_salesman`. The original render command in the CO directive was missing this flag.
- **Forced alignment toolchain (2026-05-07):** aeneas 1.7.3 is the forced-alignment tool for audiobook whispersync. Install with `AENEAS_WITH_CEW=False python3 -m pip install --user aeneas` (skips espeak C extension build, which requires libespeak that Homebrew can't install due to root-owned /usr/local/share/man/man8). ffmpeg is provided by `static-ffmpeg` Python package (`python3 -m pip install --user static-ffmpeg`); call `static_ffmpeg.add_paths()` before invoking aeneas to put the binary on PATH. macOS TTS (system `say` command) replaces espeak: pass `-r=tts=macos` to the CLI call (NOT in the task config string - that's a runtime config). `tts=macos` in the task config string is silently ignored; `-r=tts=macos` is the correct form. aeneas produces sentence-level timing (257 fragments for Ch 1). Word-level timing is interpolated linearly within each sentence boundary (Option B). Alignment run time: ~5 minutes for a 23-minute chapter on Mac M-series CPU.
- **Multi-track MP3 naming convention (2026-05-07):** The multi-track convention is `{slug}--{voice}.mp3`. `--output-suffix` in audiobook.py appends literally to the stem, so `--output-suffix=--af_bella` produces `ch01-departure--af_bella.mp3`. Passing `--af_bella` as a plain arg (not `=` form) fails because argparse interprets `--af_bella` as a flag. Always use `--output-suffix=--<voice>` syntax.
- **Homebrew blocked on this Mac (2026-05-07):** Homebrew cannot install any formula because `/usr/local/share/man/man8` is owned by root. Cannot fix without sudo (which is unavailable in automated sessions). Workaround for system binaries: use Python packages with bundled binaries (e.g. `static-ffmpeg`). Workaround for library-requiring packages (e.g. aeneas CEW, espeak): install with the C extension disabled (`AENEAS_WITH_CEW=False`).
- **aeneas alignment schema v2 (2026-05-07):** `vol-1/_voice-drafts/_alignments/ch01-departure.json` was upgraded to schema v2. Top-level additions: `alignment_schema_version: "2"`, `alignment_engine`, `alignment_notes`, `audio_chatterbox` (original Chatterbox audio path). Per-chunk additions: `audio_text` (what was spoken), `words[]` array (linear interpolation within aeneas sentence boundaries), `alignment_engine`. Backup of original Chatterbox-era alignment at `_alignments/ch01-departure.chatterbox.json.bak`.
- **narratable_text() YAML front-matter bug (fixed 2026-05-07):** `narratable_text()` was stripping only the `---` delimiter lines of YAML front-matter, leaving all key:value content (title, volume, icm-stage, etc.) as spoken text in the TTS script. Fixed by adding a DOTALL strip of the entire `---\n...\n---\n` block at the function start. ISO 8601 timestamps (`2026-09-15T11:18`) also added to preprocessing - expand to spoken form (`September 15, 2026, at 11:18`) to prevent slow TTS phonemization. Both fixes live in `build/audiobook.py`.

- **Joel teaching-register pilot (Ch 7, 2026-05-16):** The soft case Joel brings to the wardroom is the load-bearing prop for opening the laptop/identity-triad teaching beat. The case appears in the original chapter but Joel never opens it. The pilot opens it mid-scene and closes it, then the chapter-close line about the case is updated to reflect that it was opened. The "three credential modules" from Helsinki (Wanjiru Ch 1 handoff) is the natural retroactive anchor for the §1 identity-triad explanation. Joel naming "I owed you the name of the thing you ran" (not "you should have known") is the character-voice discipline to hold throughout any future teaching beats. Anna's pedagogical-tempo registration ("the sentence that waits" - letting the picture assemble before placing the next piece) should appear ONCE in any teaching extension, not as a recurring beat.
- **Joel teaching-register voice discipline:** Joel's teaching is always earned by an in-scene reason. The reason in Ch 7 is that Joel has owed Anna a full explanation of the architecture's three-compartment identity model since she ran the Helsinki credential ceremony without being told what it was. That debt is specifically architectural, not social. "The debt was his, and the debt was architectural, and naming it was the same discipline he had described for twenty minutes." Hold this pattern in any future teaching beat: the reason comes from the architecture, not from narrative convenience.

- **Repetition fixes obey "no synonym cycling" (2026-05-17):** The book CLAUDE.md style guide forbids synonym cycling ("Name a concept once; use that name everywhere"). When galley flags `proximity_echo` / `bigram_chain_loop` / `lexical_chain_loop` over-density for technical terms (relay layer, gossip protocol, consortium, write), the legal fix moves are: (1) pronoun substitution after first naming ("the relay layer" → "the layer" / "it"), (2) clause restructuring to combine sentences that re-invoke the same subject, (3) cutting redundant re-invocations where pronoun is unambiguous (e.g. "the cross-attestation from the consortium because the consortium is dormant" → "...because it is dormant"). NEVER replace `relay layer` with `link` / `transport` / `uplink` - that's the prohibited move. Verified on ch04 2026-05-17: 5 edits cut proximity_echo 71→64, bigram_chain_loop 47→39, antimetabole 26→16, kept green-on-standard.

- **Anna's postcards are printed on her own desk printer (2026-05-17, canon):** Across the book, Anna prints Diana's bakery photographs herself on a small dedicated card printer she keeps on her desk - never at a post office, never at a print shop. The ritual is hers from start to finish: photograph at the bakery, print on her own desk, address by hand, drop in the mail. Ch01 was corrected 2026-05-17 (was: post office); ANNA-VOICE.md line 219 now states this explicitly. Future drafts must not regress.

## Do-Not-Repeat

<!-- Mistakes made and corrected. Each entry prevents the same mistake recurring. -->
<!-- Format: [YYYY-MM-DD] Description of what went wrong and what to do instead. -->
- [2026-05-17] Do NOT fix repetition by synonym cycling (e.g. `relay layer` → `link` / `transport` / `uplink`). The book CLAUDE.md style guide bans it. Legal fixes are pronoun substitution after first naming, clause restructuring, and cutting redundant re-invocations. See Key Learnings entry.
- [2026-05-17] Do NOT describe Anna's postcards as "printed at the post office" or any third-party print service. Canon (locked in ANNA-VOICE.md): Anna prints them herself on a small dedicated card printer she keeps on her desk.
- [2026-05-07] Do NOT use `--base-url http://desktop-umt08rn:8881/v1` for chatterbox renders - this path returns 405. Use `http://desktop-umt08rn:8883/api/v1` (direct backend, no proxy timeout) or `http://desktop-umt08rn:8881/api/v1` (proxy, 30s timeout). The `default_base_url` in `ENGINES['chatterbox']` is now `8883/api/v1`.
- [2026-05-07] Do NOT run `--engine chatterbox --preset ciufi-galeazzi` without `--no-chapter-map` - CHAPTER_PRESET_MAP overrides the preset to `female-solo` (broom_salesman) for all Vol 2 chapters. Always add `--no-chapter-map` for ciufi-galeazzi final renders.
- [2026-05-07] Do NOT send unprocessed chapter files with YAML front-matter to TTS - `narratable_text()` now strips the entire `---\n...\n---\n` block. If a chapter starts rendering metadata as speech, check that the front-matter strip regex matches the file's exact front-matter format.
- [2026-05-07] Do NOT assume cache-resume + restart is sufficient when a chatterbox render dies mid-chapter. If the same chunk index hangs twice in a row, it is a DETERMINISTIC POISON CHUNK that wedges the inference worker - the queue eventually fills (503), then the endpoint goes fully unresponsive (HTTP 000). Fix path: (1) restart chatterbox-tts on Windows GPU box, (2) bisect the offending sentence (likely punctuation/abbreviation edge case like "St." producing a fragment), edit the script or text, then re-render. Cache resume alone re-poisons the worker. See bug-212 for chunk 90 of ch01-departure (ciufi-galeazzi). Suspect sentences cluster around "I had read the press cycle from St." (1-char fragment after period).
- [2026-04-24] Do NOT attribute `ISchemaLens` or `LensGraph` to `Sunfish.Kernel.Runtime`. They live in `Sunfish.Kernel.SchemaRegistry`. Runtime owns upcasters (`ISchemaVersion`) only.
- [2026-04-24] Do NOT invent ICrdtEngine methods like `OpenOrCreateAsync()`. Real API: `CreateDocument()` and `OpenDocument()` (both sync).
- [2026-05-18] PAO rebrand Wave 2B rules (from CIC ruling admiral-ruling-2026-05-18T03-30Z): DO rename `Sunfish.Kernel.*` → `Harborline.Kernel.*`, `Sunfish.Foundation.*` → `Harborline.Foundation.*`, `Sunfish.UICore` → `Harborline.UICore`, `Sunfish.UIAdapters.*` → `Harborline.UIAdapters.*`, `Sunfish.Compat.*` → `Harborline.Compat.*`. DO rename platform brand "Sunfish" → "Harborline Shipyard" (first mention) / "Harborline" or "Shipyard" by context. DO rename "Anchor" (app/accelerator) → "Sunfish" (ERP product). DO NOT rename code class names like `SunfishNodeHealthBar`, interface names like `ISunfishRenderer`, DI method names like `AddSunfishKernelRuntime()`, or npm package `@sunfish/ui-adapters-react` — flag for Engineering. DO NOT rename filesystem paths like `accelerators/anchor/` — flag for Engineering. URL `github.com/ctwoodwa/Sunfish` is metadata, leave as-is per Wave 2A ch04 precedent.
- [2026-04-24] Do NOT describe loro-cs as "actively maintained with small version lag" - it's very bare bones, multi-week effort to complete bindings.
- [2026-04-24] Do NOT use SyncState.Linked, .Searching, .Fresh, .Unknown, .Degraded, or .Error - valid values are only Healthy, Stale, Offline, ConflictPending, Quarantine.
- [2026-04-24] Do NOT invent plugin API members (PluginId, DependsOn, Register). Use Id, Dependencies, OnLoadAsync.
- [2026-04-24] Do NOT use WriteState enum (Pending/Confirmed/Failed) - does not exist in Sunfish repo.
- [2026-04-24] Do NOT invent MDM config key `storageEncryption: required` - not in node-config.json schema.
- [2026-04-24] Do NOT reference OnboardingState enum - use AnchorSessionService.IsOnboarded (bool) instead.
- [2026-04-24] Do NOT claim AddSunfishKernelRuntime() wires sync daemon, mDNS, gossip, or ICrdtEngine - it only registers INodeHost and IPluginRegistry.
- [2026-04-24] Do NOT claim AddSunfishKernelSecurity() loads/generates keypair or registers onboarding state machine - cryptographic services only.
- [2026-04-24] Do NOT describe Sunfish's CRDT as "working CRDT merge." Current StubCrdtEngine uses total-order replay, not CRDT semantics; real engine (YDotNet) validated in spike 2026-04-22 but not yet integrated into kernel-crdt. Stub file self-marks "DO NOT SHIP TO PRODUCTION."
- [2026-04-24] Do NOT claim GossipDaemon applies deltas back into ICrdtDocument - code comment confirms apply-back "still lands in Wave 2.6." Two nodes can exchange state vectors today, but concurrent edits don't converge without manual intervention.
- [2026-04-24] Do NOT claim full `dotnet build` passes on Sunfish repo - test projects (kernel-lease/tests, local-node-host/tests, blocks-forms/tests) have interface mismatches. Only apps/local-node-host builds cleanly as of 2026-04-24.
- [2026-04-24] Do NOT claim OnboardAsync persists attestation or applies snapshot in Wave 3.x - both are deferred to Wave 4.
- [2026-04-24] SunfishNodeHealthBar lives in Sunfish.UIAdapters.Blazor, NOT Sunfish.Foundation.LocalFirst.
- [2026-04-24] Razor illustrative marker syntax: use @* illustrative - not runnable (pre-1.0 API) *@ not HTML comment syntax inside fenced razor blocks.

## Decision Log

<!-- Significant technical decisions with rationale. Why X was chosen over Y. -->

### 2026-05-13 - Preface narrator change: Joel Reyes replaces Anna Yusupova

**Decision:** Vol 1 is reframed as Joel Reyes's dissertation. Joel is the first-person narrator of the preface (and all vol-1 front-matter passages). Anna Yusupova is NOT the Vol 1 narrator - she may appear in Vol 2 (mission-log frame). The "A Note from the Authors" AI-authorship disclosure and Chris Wood byline are removed from the preface entirely. Sunfish is framed as Joel's prototype, built to validate the argument.

**Joel's voice:** Direct, compressed, analytical. Academic-personal. Names the 2022 SaaS terminations (17,000 documented cases) as the empirical anchor. States the argument first, reasoning follows. No memoir tone; no performed emotion. Sign-off: "- Joel Reyes, Seattle, May 2025."

**What this means for future sessions:** Do not reintroduce Anna Yusupova in vol-1 prose or front-matter. Do not add AI-authorship disclosures to vol-1 chapters. If a first-person passage appears in vol-1, the voice is Joel's.

## Decision Log - 2026-04-25 - Phase 0.0 timing pilot

**Decision: skip Task 2 (MED-tier pilot); proceed to Phase 0 sweep without timing data.**

**Reasoning:** Author has stated the project has no deadline and will take as long as it takes. Real timing data is therefore not load-bearing for the continue/abort decision. Use a conservative estimate as a sanity check rather than a budget.

**Conservative estimate for Phase 0** (assuming Claude does the compression with author review):
- 12 HIGH-severity paragraphs × ~5 min Claude generation + ~5 min author review = 2 hours
- ~30 MED-severity paragraphs × ~3 min generation + ~3 min review = 3 hours
- Appendix F creation (Task 6) = ~4 hours (substantive compilation work)
- Disclosures + verification + commit hygiene = ~2 hours
- **Conservative total: ~11 hours.** Well within the original 24-48h budget; no need to invoke Alternative A or B.

**Decision: CONTINUE with Phase 0 sweep.** Plan Task 3 (the projection gate) is satisfied: projection ≤48h, continue.

## Decision Log - 2026-04-25 - Phase 0.5 result

**Decision: ORIGINAL PLAN stands.** Phase 0.5 methodology test produced a fresh Gladwell pass-1 on cleaned Ch01 (`vol-1/_voice-drafts/pass1/ch01-when-saas-fights-reality.md`, 5,447 words). Author's verdict: "the ch01 reality check looks good" - confirming pass-1 did not regress after Phase 0a; pass-2 (Sinek polish over Gladwell) is still needed for the book's house voice.

**Phase 1 scope unchanged:** tune all six voice agents (sinek + 5 guests). Polish/normalize tier system as planned.

## GitButler state - 2026-04-25 (SUPERSEDED 2026-05-04)

Earlier teardown left `.git/gitbutler` residual + stale workspace/target
refs. **Resolved 2026-05-04** - GitButler.app is running and working;
refs and toml resynced via the synthetic-workspace-commit pattern (see
`bug-160` in buglog and the 2026-05-04 entry below).

## GitButler ref-resync - 2026-05-04

GitButler refs drift over time as origin/main advances. Symptoms:
- `gitbutler/target` ref pointing at unrelated old commit
- `gitbutler/workspace` ref behind main
- `default_target.sha` in `virtual_branches.toml` stale
- `but status` either fails ("Not currently on a gitbutler/* branch")
  or shows wrong base SHA

**Resync recipe** (works with GitButler.app running concurrently):

```bash
git fetch origin main
# Push & PR-merge any unpushed work first; then on local main:
git reset --hard origin/main

# Update toml (sed-style or Edit):
#   default_target.sha = $(git rev-parse origin/main)

# Recreate synthetic workspace commit:
WS=$(GIT_AUTHOR_NAME=GitButler \
     GIT_AUTHOR_EMAIL=gitbutler@gitbutler.com \
     GIT_AUTHOR_DATE="$(date +%s) -0400" \
     GIT_COMMITTER_NAME=GitButler \
     GIT_COMMITTER_EMAIL=gitbutler@gitbutler.com \
     GIT_COMMITTER_DATE="$(date +%s) -0400" \
     git commit-tree $(git rev-parse origin/main^{tree}) \
       -p $(git rev-parse origin/main) \
       -m 'GitButler Workspace Commit

This is placeholder commit and will be replaced by a merge of your virtual branches.

Due to GitButler managing multiple virtual branches, you cannot switch back and')

git update-ref refs/heads/gitbutler/workspace $WS
git update-ref refs/heads/gitbutler/target $(git rev-parse origin/main)

# Verify:
git checkout gitbutler/workspace && but status
# Expect: workspace base shows '[origin/main]' at the current main SHA
```

**Why:** The synthetic "GitButler Workspace Commit" pattern matches Sunfish.
GitButler treats it as the placeholder for virtual-branch merge; with no
active branches, it sits directly on top of origin/main. The toml's
`default_target.sha` and the `gitbutler/target` ref both must equal current
origin/main for the GUI to consider the workspace "up to date".

**Recurring:** This drift happens whenever main advances and the GitButler
GUI hasn't been used to sync. Expect to repeat this fix periodically.

## Phase 1 → Phase 2 transition - 2026-04-25

Phase 1 closed at commit `af4e113`. Six voice agents tuned per the
ORIGINAL PLAN (Phase 0.5 decision):
- voice-sinek: chapter-scale calibration, scene preservation, audiobook
  cadence, register variation, 10% cut, preserve definitions, second
  canonical example (chapter-opening register)
- voice-gladwell, voice-brown: universal tunes (audiobook + preserve
  definitions) + 10% cut
- voice-grant: universal tunes + 10% cut + citation-enumeration guard
  (Grant-specific compounding pattern)
- voice-godin: universal tunes only (existing brevity rule already
  prevents Sinek-style compounding)
- voice-lencioni: universal tunes + preserve-narrative-scenes (fable
  agent needs scene preservation more than others) + scene-safe 10% cut

Per-invocation logging (B3/C9) added to voice-pass.py: every voice-pass
run now writes a JSON audit entry to chapters/_voice-drafts/_log/.

Phase 2 dispatched as background process bzduwnh42 - 4 pilots serial
(Ch04, Ch05, Ch11, Ch01), ~40 min wall-clock. Grading template at
docs/superpowers/specs/2026-04-25-phase2-pilot-grading.md.

In parallel: promote.py (Phase 4 prep) dispatched as subagent - TDD
work, ~20 min, non-overlapping with pilot run.
- **narratable_text() log-opener strip (added 2026-05-07, bug-222):** Vol 2 chapters with `log-opener-pattern: A` metadata have an italicized "filed log" artifact between YAML and main prose (e.g., Ch 1 "Pre-departure record... - Filed to mission-archive"). Bookended below by a `---` horizontal rule. Print convention; not for audio. `narratable_text()` strips this via a second regex: `re.sub(r'\A(?:\s*\*[^*]+\*)+\s*---\s*\n', '', t)` - anchored at \A so only the chapter-opening artifact matches. Mid-chapter italicized passages are unaffected. Verified working on Ch 1, Ch 5, Ch 13.
- [2026-05-07] Do NOT assume YAML strip alone makes Vol 2 chapters audio-clean. Chapters with `log-opener-pattern: A` need a SECOND strip for the italicized log-block between YAML and main prose. Bug-222 fix is in narratable_text(). The next `./build/render-chapter.sh ch01-departure` will produce a re-stripped script and re-render chunks 1-89 fresh (cache-orphaned by the script-text change).
- **Kokoro daily-driver topology corrected (2026-05-07, post-bug-189 restart):** The Windows-side Kokoro-FastAPI now lives at `http://desktop-umt08rn:8880/v1` (same /v1 path as the Mac Docker container; no auth required). The earlier `:8881/v1` config (with Bearer auth) was correct briefly but the Inference Studio proxy topology changed when the server was restarted to fix bug-189; the proxy now requires /api/v1/ prefix. The direct :8880/v1 path bypasses the proxy entirely. Voice catalog: 67 voices (vs. 58 on the Mac Docker), including af_bella for the female-solo preset. Updated `ENGINES['kokoro']` default_base_url + requires_auth=False in build/audiobook.py 2026-05-07. To use the Mac Docker fallback explicitly: `--engine kokoro-local`.
- **Inference Studio API surface (canonical, 2026-05-07):** Unified gateway at `http://desktop-umt08rn:8881` exposes:
  - `GET /api/v1/health` → JSON `{status, model_loaded, queue_depth, vram_used_gb}` - real health endpoint for QA dashboard server-health dot.
  - `GET /api/v1/models` → catalog: `higgs` (Chatterbox), `kokoro`, `tts-1`, `tts-1-hd` aliases.
  - `POST /api/v1/audio/speech` - TTS synth (multipart-style; routes by `model` parameter).
  - `POST /api/v1/audio/transcriptions` - **Whisper STT (multipart/form-data; `file, model, language, response_format`)**. OpenAI-compatible. `response_format=verbose_json` returns word-level timestamps.
  - `GET /api/v1/audio/stt/status` → `{loaded, model}` - reports STT model warmup state.
  - `POST /api/v1/audio/workers/reset` - **resets wedged inference workers**; replaces manual server restart for chunk-90-style wedges.
  - `GET/PUT/DELETE /api/v1/audio/voices/{id}` - voice CRUD.
  - `POST /api/v1/image/generate` + status/view - FLUX/ComfyUI image generation.
  - `/api/v1/music/{browse|import|tracks}/silverman` - Silverman Sound CC BY 4.0 ambient browser + library mgmt for the production-pass music layer.
  - Swagger UIs at `/api/v1/docs` (audio+image+models+music) and `/api/v1/music/docs`.
  - Auth: `Authorization: Bearer $TTS_API_KEY` for all (`/health` and `/audio/voices` work without).
- **Operational implication for QA dashboard:** the dashboard's server-health dot binds to `/api/v1/health` (not probe-based). The "Reset workers" button hits `/api/v1/audio/workers/reset`. Both replace previously-painful workarounds.
- **galley/ is the multi-book platform (clarified 2026-05-08):** website + build scripts + audiobook outputs relocated from `the-inverted-stack/build/` to `/Users/christopherwood/Projects/SunfishSoftware/galley/build/the-inverted-stack/output/`. galley/ has its own .git; supports multiple books namespaced under `build/<book>/output/`. **What stayed in this repo:** chapter source markdown (`vol-2/...`), workshop entries + audio-glossary YAML (`vol-2/_glossary/`), all .pao-inbox artifacts, .wolf/ files. **What moved to galley/:** audiobook output MP3s, alignment JSONs (likely), web reader at localhost:3080, build scripts (likely audiobook.py + render-chapter.sh + verify_loudness.py + qa.py if/when written). The audio-pipeline still reads chapter markdown + glossary from this repo at runtime; only OUTPUT side moved. β render batch (task #13) outputs land in galley/.
- **Implication for QA dashboard work:** `.pao-inbox/_decisions/2026-05-07-web-app-qa-dashboard-shape.md` referenced paths like `build/output/qa/\<chapter\>.qa.json` - these now live at `galley/build/the-inverted-stack/output/qa/...`. The Phase 0 deliverables (`ch01-departure.qa.json`, `SCHEMA.md`) at `the-inverted-stack/build/output/qa/` should migrate to galley/ when Yeoman implements `build/qa.py`. The schema CONTENT is still correct; only the path changed.
- **Vol 1 premise locked (2026-05-13):** *The Filchner Dark* (Vol 1) is Joel Reyes writing his dissertation - three-year argument that local-first + self-hosting is the only vendor-independent architecture that survives political/commercial disruption. The 2022 SaaS terminations are his empirical anchor. Vol 2 is Anna's mission narrative. Back-cover copy approved. Vol 1 refactor complete (2026-05-13 commit 2cc80df).
- **vol-2/_voice-drafts/ is gitignored (2026-05-16):** FFF pilot artifacts and other voice-draft files live here but are NOT committed. Do not attempt `git add vol-2/_voice-drafts/` - use `-f` only if explicitly directed.
- **Nansen-ingestion no-citation rule (2026-05-16):** FFF canon discipline §6: no direct source citations in the narrator's voice. The reader experiences the texture; the source is silent. Anna does not name Nansen or Verne in prose. Canon doc at `.pao-inbox/_creative/nansen-ingestion-canon.md` line 168.
- **Audio staleness false-positive pattern (2026-05-16):** Frontmatter-only and HTML-comment-only commits (`chore(vol-2): tag ch03-ch18 as pre-bobiverse`) make markdown mtimes newer than MP3s without changing the narratable text. Always classify via `git diff <audio-render-commit>..HEAD` before re-rendering - strip everything `narratable_text()` strips and check whether remaining diff is empty.
- **Kokoro default voice changed to af_alloy (CO directive 2026-05-09):** PRESETS_KOKORO["female-solo"] now maps to `af_alloy` voice (was `af_bella`). Speed unchanged at 0.92. Chapter-map entries pointing at "female-solo" all inherit the new default. "female" preset (af_bella+af_nicole blend) unchanged. To use af_bella for a specific render: `--preset female` or `--preset <new>`. Note: this is a Kokoro-only change; Chatterbox PRESETS_CHATTERBOX still routes all slots to broom_salesman per the universal-narrator decision.
