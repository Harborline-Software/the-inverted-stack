# Prose Telemetry Platform - "OpenTelemetry for Prose"

**Date:** 2026-05-08
**Author:** PAO
**Status:** Architecture approved - CO directives 2026-05-08
**Related:**
- `.pao-inbox/_decisions/2026-05-07-web-app-qa-dashboard-shape.md` (per-chapter QA platform; this telemetry plugs in as another chip)
- `~/.claude/skills/literary-devices/SKILL.md` + `references/devices.md` (device registry - already exists)
- `~/.claude/skills/anti-ai-tells/SKILL.md` (sibling skill catalog; some overlap)

---

## Problem statement

CO ear-tested Vol 2 chapters and identified two over-deployed rhetorical devices: **tautological self-equation** (*"the X was the X"*) at 100+ occurrences and **anaphora cascades** (consecutive sentences sharing 2-word openings) at 699 runs trapping 51% of all Vol 2 sentences. Eyeball-and-ear is the only current measurement; CO has no way to:

- Quantify device density before / after a cull pass
- Compare chapter A to chapter B for over-use
- Set thresholds that flag a chapter as "needs cull"
- Track the effect of a voice-pass on rhetorical-device telemetry over time
- Compare Anna's voice across Vol 2 to a reference corpus (Towles, Hemingway, etc.)
- Guide future drafting / voice-pass agents away from over-density patterns

Without measurement, the cull pass is blind - we'd be cutting on instinct without confirmation that the edit landed.

## OpenTelemetry parallel - the architectural metaphor

The OTel parallel is exact. Same instrumentation pattern, applied to text rather than running code.

| OTel concept | Prose-telemetry equivalent |
|---|---|
| **Span** | Device occurrence: `{device, run_length, prefix, start_char, end_char, text, severity}` |
| **Metric** | Per-device count, density per 1000 words, max-run-length, sentence-percentage-trapped-in-runs |
| **Log / event stream** | JSONL of all device occurrences in document order |
| **Trace** | Device co-occurrence patterns (anaphora cascading into tautology in same passage) |
| **Service map** | Cross-chapter / cross-volume / cross-author comparison heatmaps |
| **Resource attributes** | Chapter slug, volume, voice-pass status, render mode, ICM stage |

Detectors emit spans → aggregator computes metrics → exporter writes structured JSON → dashboard / CLI / web reader consumes.

## Architecture - detector / meter split (revised 2026-05-08 per research feedback)

**Two distinct tools that compose, not one pipeline.** Original draft conflated them as "detectors + aggregator"; the cleaner split - surfaced in CO's research-session feedback - is:

| Tool | Role | What it emits | What it consumes |
|---|---|---|---|
| **Detector** | Marks spans of stylistic devices in source prose | Annotations: `{type, span, offset, confidence, rule_or_model_id}` | Source markdown |
| **Meter** | Converts annotations into observability metrics | Metrics: `{raw_count, count_per_1k_tokens, sentence_coverage, paragraph_dispersion}` + dimensions | Detector annotations + token/sentence/paragraph structure |

**Why this matters:**

- **Detectors and meters evolve independently.** A new detector backend (rule, ML classifier, LLM-assisted) plugs into the same meter; a new meter (drift-over-revisions, co-occurrence, density-trends) consumes the same detector output without detector changes.
- **Multiple meters can compose over one detection pass.** Per-1k-tokens normalization for cross-chapter comparison; per-paragraph for distribution analysis; per-section for rhetorical-arc visualization; over-time for revision drift.
- **Storage discipline:** **raw annotations AND normalized metrics are stored**, not metrics alone. Counts without normalization are misleading across document lengths. The dashboard renders against both.

## Architecture - three layers + GPU-tier carve-out

### Layer 1 - Registry (already exists)

The `~/.claude/skills/literary-devices/SKILL.md` + `references/devices.md` catalog ~30+ rhetorical devices with definitions, cognitive functions, and worked examples. **This IS the OTel "semantic conventions"** - the canonical list of what a span can be. Detectors register against device-IDs from this catalog; no invention needed.

The `anti-ai-tells` skill is a sibling registry - some patterns overlap (tautological self-equation may belong to either). Detectors can register against either skill's device-IDs; the JSON schema flags `source_registry: "literary-devices" | "anti-ai-tells"` per span.

### Layer 2 - Detectors (one per device, varying complexity)

| Tier | Devices | Implementation | Compute | Lives in |
|---|---|---|---|---|
| **Easy** | anaphora, tautological self-equation, asyndeton, polysyndeton, literal-tricolon, sentence-length distribution | Pure Python regex on segmented sentences | CPU; sub-100ms per chapter | `galley/prose/lib/prose_telemetry/detectors/` |
| **Medium** | isocolon (parallel grammatical structure), antithesis, epanorthosis, hyperbaton, distributed-tricolon | spaCy POS + dependency parsing | CPU; spaCy model load adds ~500ms; per-chapter ~2-5s | Same |
| **Hard** | chiasmus (distributed), metonymy, metaphor / simile detection, hypallage | Transformer-based; deferred to research-tier | **GPU required** | `galley/api/` (when added) - same routing pattern as Inference Studio TTS/STT |

**Layered to add capabilities over time** per CO directive 2026-05-08: each detector is a plug-and-play module registered against a device-ID. Adding a new detector = drop a Python file into `galley/prose/lib/prose_telemetry/detectors/<device_id>.py` exposing a standard interface (`detect(doc: spacy.Doc) -> list[Span]`). The aggregator discovers and runs all registered detectors automatically.

### Layer 3 - Aggregator + exporter (revised schema 2026-05-08)

Per-chapter rollup written as `galley/build/<book>/output/qa/<chapter>.prose-metrics.json`, alongside the existing `<chapter>.qa.json`. **Schema separates raw annotations from normalized metrics from dimensions** per CO's research-session feedback (counts alone mislead across document lengths):

```jsonc
{
  "_schema_version": 2,
  "chapter_slug": "ch01-departure",
  "measured_at": "2026-05-08T15:00:00Z",

  // ─── Dimensions (OTel resource attributes) ───
  "dimensions": {
    "volume": 2,
    "act": 1,
    "chapter_number": 1,
    "icm_stage": "icm/draft",
    "voice_pass_status": "draft",
    "author": "anna",
    "genre": "literary-sf",
    "model_version": "freestylo-0.x + stylometrix-0.y + custom-2026-05-08",
    "revision": "2026-05-08T11:20-credential-modules-edit",
    "section": "wardroom-handoff"
  },

  // ─── Raw annotations (detector output; the source-of-truth events) ───
  "detected_devices": [
    {
      "type": "anaphora",
      "run_length": 6,
      "prefix": "I had",
      "start_char": 12044,
      "end_char": 12612,
      "confidence": 1.0,
      "rule_id": "freestylo:anaphora.consecutive_sentence_opening",
      "sentences": ["I had not slept.", "I had not expected to sleep.", ...]
    },
    {
      "type": "tautological_self_equation",
      "head": "pot",
      "start_char": 7732,
      "end_char": 7758,
      "confidence": 1.0,
      "rule_id": "custom:tautological_self_equation.regex",
      "text": "the pot was the pot"
    }
  ],

  // ─── Normalized metrics (meter output; counts → densities → dispersions) ───
  "metrics": [
    {
      "device": "anaphora",
      "raw_count": 47,
      "count_per_1k_tokens": 30.0,
      "sentence_coverage_pct": 48.1,
      "paragraph_dispersion": 0.73,
      "max_run_length": 6,
      "severity": "high"
    },
    {
      "device": "tautological_self_equation",
      "raw_count": 8,
      "count_per_1k_tokens": 1.9,
      "sentence_coverage_pct": 3.1,
      "paragraph_dispersion": 0.42,
      "severity": "medium"
    }
  ],

  // ─── Document-level metrics (orthogonal; from textstat / sentence-segmenter) ───
  "document_metrics": {
    "word_count": 4155,
    "sentence_count": 258,
    "paragraph_count": 87,
    "flesch_reading_ease": 62.4,
    "sentence_length_p50": 14,
    "sentence_length_p90": 38,
    "sentences_over_50_words": 11
  },

  // ─── Thresholds + rollup (consumer-side contract) ───
  "ear_test_thresholds": {
    "anaphora_density_per_1000": 25.0,
    "anaphora_max_run_length": 3,
    "tautology_density_per_1000": 3.0
  },
  "rollup": {
    "verdict": "yellow",
    "blockers": [],
    "warnings": ["anaphora density 30/1000 exceeds 25 threshold; max run 6 exceeds threshold 3"],
    "passes": ["tautology_density", "asyndeton_density"]
  }
}
```

**Schema discipline:**

- `detected_devices[]` is the raw event stream - each detection is a span with offset + confidence + the rule/model that produced it. **This survives schema evolution** - new metrics can be derived later from the same stored events without re-running detectors.
- `metrics[]` is the meter's normalized output - already-denormalized for direct dashboard consumption. Per-1k-token normalization is the canonical default; per-sentence and paragraph-dispersion are alternative views.
- `dimensions` are OTel-style resource attributes - the tags by which corpus-level rollups slice (compare ch01 to ch15; compare draft to voice-passed; compare across revisions; compare Anna's voice to Towles).
- `document_metrics` are orthogonal document-level features (readability, sentence-length distribution) - don't belong inside `metrics[]` because they're not device-specific.

This is the **contract with the QA dashboard.** The web reader's per-chapter card reads this file and renders a "Prose telemetry" chip alongside the existing chips (audio render, alignment, loudness, etc.).

## OSS components - leverage (revised 2026-05-08 with research-session candidates)

### Detector-side OSS

| Tool | Role | Notes |
|---|---|---|
| **Freestylo** | **Open package for stylistic-device detection - extendable with custom detectors.** JOSS peer-reviewed (joss.theoj.org/papers/10.21105/joss.07596). The closest existing tool to what CO wants; closes the gap my prior draft identified. | **Primary detector engine candidate for v1.** Investigate fit before custom-building. |
| **spaCy** | Sentence segmentation, POS, dependency parsing - the foundational NLP layer | Industrial-grade; `en_core_web_sm` model is ~12 MB. Foundational layer that Freestylo and our custom detectors both build on. |
| **proselint** (Python) | Style + grammar linter; plugin-able; some easy-tier detectors could ship as plugins | Secondary; useful if Freestylo doesn't cover specific patterns. |
| **vale** (Go) | Config-driven prose linter; YAML rules | Secondary export - Vale-compatible rules for in-editor (VS Code) highlighting in Yeoman's drafting workflow. Not the primary engine. |
| **UIMA-based rhetorical-device frameworks** | Reference architecture for pluggable detection stages and annotations | Architecture pattern source; not a direct dependency. |

### Meter-side OSS

| Tool | Role | Notes |
|---|---|---|
| **StyloMetrix** | **Produces numeric vectors where each metric quantifies a linguistic feature.** NASK-NLP / ZILiAT. Multi-language. | **Primary meter engine candidate for v1.** "Text → numeric feature vector" is exactly the observability primitive we want. |
| **textstat** | Readability metrics (Flesch, ARI, sentence-length distribution) - orthogonal but free | Parallel metric source; trivially integrated. |
| **stylo** (R) | Stylometric corpus comparison - Anna vs Towles vs Hemingway etc. | Phase 3 (reference-corpus comparison); R-side; defer to post-MVP. |

### Pattern-source OSS

| Project | Pattern lesson |
|---|---|
| **OpenNyAI rhetorical-role baseline** (Legal-NLP-EkStep) | Section-level rhetorical labeling pattern. Not directly reusable for prose telemetry but informs how rhetorical sections (introduction / argument / conclusion) could be identified and used as dimensions for metrics aggregation. |

### Revised gap statement

The original gap statement ("there's no off-the-shelf OSS rhetorical-device detector") **was wrong** - Freestylo exists, is peer-reviewed, and is purpose-built for this. **The correct framing:**

- **Freestylo + StyloMetrix is a viable starting stack.** v1 is composition, not from-scratch construction.
- **What we still build:** the integration layer (detector → meter pipeline), the device-registry binding (mapping our literary-devices catalog to Freestylo's detector taxonomy), the JSON schema that the QA dashboard reads, and any Vol-2-specific detectors not in Freestylo's default catalog.
- **Estimated effort revised down:** v1 is **3-5 days of integration work** rather than 1-2 weeks of from-scratch detector code, contingent on Freestylo's coverage of CO's ear-flagged devices (anaphora, tautological self-equation, asyndeton, polysyndeton, tricolon, isocolon).

## Repo placement - galley vs SunfishSoftware

Per CO directive 2026-05-08:

> *"If we need a GPU we will need to add it under the galley/api or similar unless it is important enough to be its own repo under SunfishSoftware."*

**v1 placement: lives inside galley/** as `galley/prose/lib/prose_telemetry/` (Python package). CPU-tier detectors run in-process within galley's existing build/render pipeline.

**GPU-tier carve-out: routes through `galley/api/`** when needed (transformer-based hard-tier detectors). Same routing pattern as Inference Studio's TTS/STT - galley/api hosts the GPU-bound endpoints; the prose-telemetry pipeline calls them like any other API. This way galley/api becomes the multi-book GPU-compute service over time.

**Promotion to standalone repo** (`SunfishSoftware/prose-telemetry/` or `SunfishSoftware/prosetel/`): reserved for the case where the platform becomes important enough - multiple books / external consumers / community contributions warrant separation. Default is to keep it inside galley/ until that bar is met.

## Naming

Working name candidates: **prosetel**, **rhetel**, **literary-otel**, **rhetorscope**, **devicefinder**. *prosetel* most honestly evokes the OTel parallel; defaulting to that until CO chooses otherwise.

## v1 detector list

Eight detectors covering CO's ear-flagged devices plus obvious neighbors:

1. **anaphora** - consecutive sentences sharing N-word opening (configurable N=2 default)
2. **tautological_self_equation** - `the X was/is the X` and variants
3. **asyndeton** - comma-separated lists missing conjunctions
4. **polysyndeton** - excess conjunctions in series (3+ "and" / "or" within one sentence)
5. **literal_tricolon** - three-element parallel structure within one sentence
6. **isocolon** - parallel grammatical structure across consecutive clauses (medium-tier; needs spaCy)
7. **epanorthosis** - self-correction patterns (*not X - Y*)
8. **sentence_length_distribution** - orthogonal metric: mean, median, p90, sentences > 50 words

These cover ~80% of what CO ear-flagged. Medium-tier devices (isocolon, antithesis) follow in v2. Hard-tier deferred until GPU-tier carve-out is justified.

## Implementation phases

### Phase 1 (v1) - CPU-tier; ships as galley/ Python package; Freestylo + StyloMetrix backbone

**Revised approach 2026-05-08:** start by composing existing OSS rather than from-scratch construction.

- spaCy installed in galley/ environment (foundational NLP layer)
- **Freestylo** evaluated as primary detector engine - confirm coverage of CO's ear-flagged devices (anaphora, tautological self-equation, asyndeton, polysyndeton, tricolon, isocolon)
- **StyloMetrix** evaluated as primary meter engine - confirm it produces per-1k-token + per-sentence + paragraph-dispersion metrics in the schema we want
- **Custom detectors only for devices Freestylo doesn't cover** - likely tautological self-equation (project-specific antipattern), possibly some Vol-2-specific patterns. Each registers against the literary-devices skill catalog's device-IDs.
- Detector → Meter pipeline glue: spaCy `Doc` → Freestylo annotations + custom annotations → StyloMetrix metrics + custom metrics → JSON exporter
- CLI: `python -m prose_telemetry --chapter <slug>` → writes `<chapter>.prose-metrics.json`
- Programmatic API for galley's existing pipeline to call at render time

**Estimated effort: 3-5 days of integration work** (revised down from 1-2 weeks of from-scratch detector code), contingent on Freestylo's actual coverage matching CO's needs. Engineering session evaluates Freestylo first; if coverage is sparse, falls back to custom-detector tier with the original 1-2 week estimate.

**First engineering session task:** evaluate Freestylo's device catalog against CO's ear-flagged devices + Vol 2's literary-devices skill catalog. Report coverage; that determines whether v1 is composition or hybrid.

### Phase 2 - Medium-tier devices + dashboard binding

- Add medium-tier detectors (isocolon, antithesis, etc.)
- Wire `<chapter>.prose-metrics.json` into the QA dashboard's per-chapter card
- Add baseline-drift-detection: compare current metrics to last measurement; flag improvement / regression
- Vale rules export for VS Code in-editor highlighting (Yeoman drafting workflow)

**Estimated effort: 1 additional week.**

### Phase 3 - Reference-corpus comparison + threshold calibration

- Run detectors against reference texts (Towles' *Gentleman in Moscow*; Hemingway; Cormac McCarthy; whatever CO wants as voice references)
- Establish empirical thresholds: "Towles' anaphora density is X/1000; Anna's is Y/1000; target reduction Z"
- Threshold-driven cull-pass guidance per chapter

**Estimated effort: 3-5 days; dependent on access to reference texts.**

### Phase 4 (deferred) - GPU-tier hard devices

- Justified only if (a) Phase 1-3 prove the platform has compounding value and (b) hard-tier devices (chiasmus, metaphor) become a real authorial pain-point
- Routes through galley/api/ following the Inference Studio model
- Decision deferred until Phase 1-3 ship and CO ear-tests the lift

## Integration with QA dashboard

Adds a new "Prose telemetry" chip per chapter in the dashboard:

| Chip color | Trigger |
|---|---|
| **Red** | Any device-density exceeds high-severity threshold (anaphora >25/1000, tautology >3/1000) |
| **Yellow** | Within tolerance but at least one warning fires |
| **Green** | All devices within configured thresholds |
| **Gray** | Not yet measured (no `prose-metrics.json` for this chapter) |

Click-through reveals per-device breakdown + inline-marked passages where each device fires (using spans' start/end char positions to highlight the source text in the web reader's reading view).

**Compounding value:** every voice-pass / cull-pass / chapter edit produces a new measurement. The dashboard shows whether anaphora density dropped after a cull pass - confirming or disconfirming the edit landed. Same loop as performance regression testing for code, but for prose.

## Cull-pass timing - implication of this architecture

The earlier cull-pass plan (`.pao-inbox/_decisions/...` GG/HH/II from the 2026-05-08 voice-issue thread) was set to run on Ch 9 + Ch 10 with manual heuristics. **The prose-telemetry platform changes the right sequencing:**

> Build the measurement device before the cull pass. Cutting blind risks over-cutting load-bearing anaphora (chapter-close ritual cataloging, dramatic peaks) or under-cutting decorative anaphora.

Recommended revised sequence:

1. **Phase 1 ships** (~1 week) - prose-telemetry CLI works against any chapter; produces JSON metrics.
2. **Run telemetry against all 18 Vol 2 chapters** - generates the baseline.
3. **CO reviews per-chapter metrics** - confirms or adjusts thresholds based on what the metrics surface.
4. **Cull-pass directive issued** - Yeoman runs cull on chapters where metrics exceed thresholds, with metrics-driven keep/cut criteria.
5. **Re-measure post-cull** - confirms density dropped to target without over-cutting.

The anti-AI-tells skill update + voice-towles skill revision (GG + II from prior thread) can ship in parallel with Phase 1 - they don't depend on the platform. The cull-pass itself (HH) waits for Phase 2.

## Open questions for engineering session

1. **Where does galley install spaCy?** Existing pyproject.toml + requirements.txt accommodation, or a separate venv for the prose-telemetry package?
2. **Which spaCy model?** `en_core_web_sm` (~12 MB, fastest, sufficient for POS) is the natural pick; `en_core_web_trf` (transformer-based, ~440 MB) only if medium-tier detectors prove insufficient.
3. **Threshold defaults** - are CO's "ear-test thresholds" derivable from an automated baseline pass on Anna's existing prose, or hand-set?
4. **Vale export schema** - if Phase 2 produces Vale rules, what's the rule-format target (regex / scope / level)?
5. **Multi-book namespacing** - galley already namespaces output as `build/<book>/output/`. Prose-telemetry rollups land at `build/<book>/output/qa/<chapter>.prose-metrics.json`. Confirm this schema scales when a second book lands.

## Filed for engineering session

This document drives the next prose-telemetry engineering work. Phase 1 implementation is the first actionable; Phase 2-4 follow as the platform proves itself.

---

**Filed by PAO. Ready for engineering session pickup. Cull-pass plan deferred to post-Phase-1 metrics-driven sequencing.**
