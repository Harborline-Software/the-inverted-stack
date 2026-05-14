#!/usr/bin/env python3
"""Lexical-fatigue detector — Phase 0 of the prose-telemetry platform.

Counts hand-curated word-family occurrences per chapter; computes per-1000-word
density; compares to Vol 2 baseline; flags chapters where any family exceeds
1.5x baseline density. Auto-discovery mode uses NLTK POS-aware lemmatization
to surface fatigue candidates beyond the curated YAML.

Phase 0 lives in this repo's build/ directory. Phase 1
(galley/prose/lib/prose_telemetry/) absorbs this as one detector among many in the
full detector / meter architecture per
.pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md.

Usage:
    python3 build/lexical_fatigue.py --all               # all Vol 2 chapters
    python3 build/lexical_fatigue.py --chapter ch14      # one chapter (substring match)
    python3 build/lexical_fatigue.py --rollup            # Vol 2 baseline + per-chapter deltas
    python3 build/lexical_fatigue.py --top-lemmas        # top-30 NLTK-lemmatized stems for discovery
    python3 build/lexical_fatigue.py --discover          # auto-find non-curated high-density lemmas

Output: build/output/qa/<chapter>.lexical-fatigue.json (per chapter)
        build/output/qa/vol-2-lexical-fatigue-rollup.json (Vol 2 rollup)
        build/output/qa/vol-2-lexical-fatigue-discovery.json (auto-discovery candidates)

Setup (one-time, already run):
    python3 -m pip install --user nltk
    python3 -c "import nltk; nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger'); nltk.download('averaged_perceptron_tagger_eng')"

CO directive 2026-05-09.
"""

from __future__ import annotations
import argparse, glob, json, re, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL2_DIR = REPO / "vol-2"
FAMILIES_YAML = REPO / "vol-2" / "_glossary" / "_lexical_fatigue_families.yaml"
OBSERVATIONAL_YAML = REPO / "vol-2" / "_glossary" / "_observational_lemmas.yaml"
OUT_DIR = REPO / "build" / "output" / "qa"

# Three canonical reference texts for stylometric triangulation.
# Per .pao-inbox/_creative/nansen-ingestion-canon.md (CO directive 2026-05-09).
# All from /tmp/gutenberg/ (downloaded via Project Gutenberg). Combined weighted
# canon baseline ≈ 62.87 obs/1k for first-person polar/submarine adventure prose.
CANON_REFERENCES = [
    ("Nansen 1897 (Arctic field diary)",         Path("/tmp/gutenberg/farthest-north.txt")),
    ("Verne 1897 Antarctic Mystery",             Path("/tmp/gutenberg/source-10339.txt")),
    ("Verne 1870 Twenty Thousand Leagues",       Path("/tmp/gutenberg/source-164.txt")),
]
# Backward-compat single-reference alias used by older code paths
NANSEN_REFERENCE = CANON_REFERENCES[0][1]

FATIGUE_THRESHOLD_MULTIPLIER = 1.5  # chapter density > 1.5x baseline → flag
HIGH_DENSITY_THRESHOLD = 5.0        # per-1k cutoff for top-tier "high fatigue" callout

STOP_WORDS = set("""
the a an of to in and that for it as is was were be been being have has had do does did
will would shall should can could may might must i you he she we they them his her my your our their
this these those there here at by from on with not no but or if so than then when where what who which
how why all any some each every other another no one her him me us so just only such been being
""".split())


def load_families() -> dict[str, dict]:
    """Load the curated word-family YAML. PyYAML required; falls back to empty."""
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML not installed. pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    if not FAMILIES_YAML.exists():
        print(f"ERROR: families YAML missing at {FAMILIES_YAML}", file=sys.stderr)
        sys.exit(2)
    data = yaml.safe_load(FAMILIES_YAML.read_text()) or {}
    return data.get("families", {})


def strip_chapter(text: str) -> str:
    """Remove YAML front-matter, log-opener artifact, HTML comments, code fences, tables."""
    text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.DOTALL)
    text = re.sub(r'\A(?:\s*\*[^*]+\*)+\s*---\s*\n', '', text)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'(?m)^\|.*\|\s*$', '', text)
    return text


def tokenize(text: str) -> list[str]:
    """Lowercase whole-word tokens; preserves apostrophes + hyphens."""
    return re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", text.lower())


def per_chapter_metrics(words: list[str], families: dict[str, dict]) -> dict:
    """Compute per-family counts + density per 1000 words for one chapter."""
    word_count = len(words)
    word_counter = Counter(words)
    metrics = []
    for lemma, spec in families.items():
        forms = [f.lower() for f in spec.get("forms", [])]
        excludes = set(f.lower() for f in spec.get("excludes", []))
        count = sum(word_counter[f] for f in forms if f not in excludes)
        per_1k = (count / word_count * 1000) if word_count else 0.0
        metrics.append({
            "lemma": lemma,
            "forms": forms,
            "count": count,
            "per_1k": round(per_1k, 2),
            "note": spec.get("note", ""),
        })
    metrics.sort(key=lambda m: -m["count"])
    return {"word_count": word_count, "metrics": metrics}


def vol2_files() -> list[Path]:
    return sorted(Path(p) for p in glob.glob(str(VOL2_DIR / "act-*" / "ch*.md")))


def chapter_slug(path: Path) -> str:
    return path.stem


def write_json(path: Path, data: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")


def run_per_chapter(chapter_filter: str | None = None) -> list[dict]:
    families = load_families()
    results = []
    files = vol2_files()
    if chapter_filter:
        files = [f for f in files if chapter_filter in f.name]
        if not files:
            print(f"No Vol 2 chapter matches '{chapter_filter}'", file=sys.stderr)
            sys.exit(1)
    for f in files:
        words = tokenize(strip_chapter(f.read_text()))
        m = per_chapter_metrics(words, families)
        result = {
            "_schema_version": 0,
            "_phase": "phase-0-lexical-fatigue",
            "chapter_slug": chapter_slug(f),
            "measured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "word_count": m["word_count"],
            "lexical_fatigue": {
                "families": m["metrics"],
                "vol2_baseline_pending": True,
            },
        }
        out_path = OUT_DIR / f"{chapter_slug(f)}.lexical-fatigue.json"
        write_json(out_path, result)
        results.append(result)
        print(f"  ✓ {chapter_slug(f):60s}  {m['word_count']:>6d} words  →  {out_path.relative_to(REPO)}")
    return results


def run_rollup() -> None:
    families = load_families()
    files = vol2_files()
    per_chapter = []
    for f in files:
        words = tokenize(strip_chapter(f.read_text()))
        m = per_chapter_metrics(words, families)
        per_chapter.append({"slug": chapter_slug(f), "word_count": m["word_count"], "metrics": m["metrics"]})

    # Vol 2 baseline density per family
    total_words = sum(c["word_count"] for c in per_chapter)
    family_totals = {}
    for c in per_chapter:
        for m in c["metrics"]:
            family_totals.setdefault(m["lemma"], 0)
            family_totals[m["lemma"]] += m["count"]
    baselines = {lemma: round(total / total_words * 1000, 2) for lemma, total in family_totals.items()}

    # Per-chapter delta vs baseline + flag chapters where any family exceeds threshold
    flagged = []
    for c in per_chapter:
        chapter_flags = []
        for m in c["metrics"]:
            base = baselines[m["lemma"]]
            if base == 0: continue
            ratio = m["per_1k"] / base if base > 0 else 0
            if ratio >= FATIGUE_THRESHOLD_MULTIPLIER and m["per_1k"] >= 1.0:
                chapter_flags.append({
                    "lemma": m["lemma"],
                    "count": m["count"],
                    "per_1k": m["per_1k"],
                    "baseline_per_1k": base,
                    "ratio": round(ratio, 2),
                    "severity": "high" if m["per_1k"] >= HIGH_DENSITY_THRESHOLD else "medium",
                })
        if chapter_flags:
            flagged.append({"slug": c["slug"], "word_count": c["word_count"], "flags": chapter_flags})

    rollup = {
        "_schema_version": 0,
        "_phase": "phase-0-lexical-fatigue-rollup",
        "measured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "vol2_total_words": total_words,
        "vol2_chapter_count": len(per_chapter),
        "vol2_baseline_density_per_1k": dict(sorted(baselines.items(), key=lambda x: -x[1])),
        "fatigue_threshold_multiplier": FATIGUE_THRESHOLD_MULTIPLIER,
        "high_density_threshold_per_1k": HIGH_DENSITY_THRESHOLD,
        "chapters_with_fatigue_flags": flagged,
    }
    out_path = OUT_DIR / "vol-2-lexical-fatigue-rollup.json"
    write_json(out_path, rollup)

    # Pretty print to stdout
    print()
    print("=" * 70)
    print(f"  Vol 2 lexical-fatigue rollup")
    print(f"  Total words: {total_words:,} across {len(per_chapter)} chapters")
    print("=" * 70)
    print()
    print(f"  {'Lemma':<15s}  {'baseline /1k':>12s}  {'total':>6s}")
    for lemma, base in rollup["vol2_baseline_density_per_1k"].items():
        total = family_totals[lemma]
        print(f"  {lemma:<15s}  {base:>12.2f}  {total:>6d}")
    print()
    print(f"  Chapters flagged (>{FATIGUE_THRESHOLD_MULTIPLIER}x baseline on any tracked family):")
    if not flagged:
        print("    (none)")
    else:
        for c in flagged:
            print(f"    {c['slug']}:")
            for fl in c["flags"]:
                print(f"      {fl['lemma']:<15s} {fl['per_1k']:>5.2f}/1k vs baseline {fl['baseline_per_1k']:.2f} ({fl['ratio']:.2f}x) — {fl['severity']}")
    print()
    print(f"  → rollup written to {out_path.relative_to(REPO)}")


_LEM = None
_TAG_TO_WN = {"V": "v", "N": "n", "J": "a", "R": "r"}


def _get_lemmatizer():
    """Singleton WordNetLemmatizer with auto-download fallback for missing corpora."""
    global _LEM
    if _LEM is not None:
        return _LEM
    try:
        from nltk.stem import WordNetLemmatizer
        from nltk import pos_tag, find
        # Verify corpora present; auto-download if missing
        for corpus, locator in [("wordnet", "corpora/wordnet"), ("averaged_perceptron_tagger", "taggers/averaged_perceptron_tagger"), ("averaged_perceptron_tagger_eng", "taggers/averaged_perceptron_tagger_eng")]:
            try:
                find(locator)
            except LookupError:
                import nltk
                nltk.download(corpus, quiet=True)
        _LEM = WordNetLemmatizer()
        _LEM.__pos_tag = pos_tag  # stash POS tagger as attribute
    except ImportError:
        print("ERROR: NLTK not installed. python3 -m pip install --user nltk", file=sys.stderr)
        sys.exit(2)
    return _LEM


def lemmatize_tokens(tokens: list[str]) -> list[str]:
    """POS-aware lemmatization. Tags + lemmatizes in batch; caches by (token, pos) pair."""
    lem = _get_lemmatizer()
    pos_tag = lem.__pos_tag
    tagged = pos_tag(tokens)
    cache: dict[tuple[str, str], str] = {}
    out = []
    for w, t in tagged:
        wn_pos = _TAG_TO_WN.get(t[:1], "n")
        key = (w, wn_pos)
        if key not in cache:
            cache[key] = lem.lemmatize(w, wn_pos)
        out.append(cache[key])
    return out


def run_top_lemmas() -> None:
    """Print top-30 most-frequent non-stop-word lemmas across Vol 2.
    Discovery tool for finding NEW fatigue candidates the curated YAML doesn't yet cover."""
    files = vol2_files()
    all_tokens = []
    for f in files:
        all_tokens.extend(tokenize(strip_chapter(f.read_text())))

    lemmas = lemmatize_tokens(all_tokens)
    counter = Counter()
    for lem_word in lemmas:
        if lem_word in STOP_WORDS or len(lem_word) < 4: continue
        counter[lem_word] += 1

    total = len(all_tokens)
    print(f"Top 30 non-stop-word LEMMAS (NLTK-WordNet, POS-aware) across Vol 2 ({total:,} total tokens):")
    print(f"  {'lemma':<25s}  {'count':>6s}  {'per /1k':>7s}")
    for lem_word, c in counter.most_common(30):
        print(f"  {lem_word:<25s}  {c:>6d}  {c/total*1000:>7.2f}")


def load_observational_lemmas() -> set[str]:
    """Load curated observational lemmas (action verbs + concrete nouns)."""
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML not installed.", file=sys.stderr); sys.exit(2)
    if not OBSERVATIONAL_YAML.exists():
        print(f"ERROR: {OBSERVATIONAL_YAML} missing.", file=sys.stderr); sys.exit(2)
    data = yaml.safe_load(OBSERVATIONAL_YAML.read_text()) or {}
    return set(data.get("action_verbs", [])) | set(data.get("concrete_nouns", []))


def observational_density(words: list[str], lemma_set: set[str]) -> dict:
    """Lemmatize tokens; count observational lemma hits; return density metrics."""
    word_count = len(words)
    if word_count == 0:
        return {"word_count": 0, "observational_count": 0, "per_1k": 0.0}
    lemmas = lemmatize_tokens(words)
    obs_count = sum(1 for lem_word in lemmas if lem_word in lemma_set)
    return {
        "word_count": word_count,
        "observational_count": obs_count,
        "per_1k": round(obs_count / word_count * 1000, 2),
    }


def run_observational_density() -> None:
    """Compute observational-density per Vol 2 chapter; compare to triangulated canon baseline.

    Three canonical references (per .pao-inbox/_creative/nansen-ingestion-canon.md):
    Nansen 1897 (Arctic field diary), Verne 1897 (Antarctic Mystery), Verne 1870
    (Twenty Thousand Leagues — submarine narrative). Weighted average forms the
    canon baseline. Chapters falling below 50% of weighted baseline are candidates
    for ingestion; chapters falling below 35% flag as high-priority.
    """
    obs_lemmas = load_observational_lemmas()

    # Compute per-source density + weighted canon
    per_source = []
    canon_total_words = 0
    canon_total_obs = 0
    for label, path in CANON_REFERENCES:
        if not path.exists():
            continue
        raw = path.read_text()
        m1 = re.search(r'\*\*\* START OF THE PROJECT GUTENBERG EBOOK[^*]+\*\*\*', raw)
        m2 = re.search(r'\*\*\* END OF THE PROJECT GUTENBERG EBOOK[^*]+\*\*\*', raw)
        body = raw[m1.end():m2.start()] if (m1 and m2) else raw
        body = re.sub(r'\[Illustration[^\]]*\]', '', body)
        tokens = tokenize(body)
        d = observational_density(tokens, obs_lemmas)
        per_source.append({"label": label, "words": d["word_count"], "per_1k": d["per_1k"], "obs_count": d["observational_count"]})
        canon_total_words += d["word_count"]
        canon_total_obs += d["observational_count"]

    canon_per_1k = round(canon_total_obs / canon_total_words * 1000, 2) if canon_total_words else None
    nansen_density = per_source[0] if per_source else None  # Nansen kept as separate ceiling baseline

    # Per-chapter density across Vol 2
    files = vol2_files()
    per_chapter = []
    total_obs = 0
    total_words = 0
    for f in files:
        words = tokenize(strip_chapter(f.read_text()))
        d = observational_density(words, obs_lemmas)
        per_chapter.append({"slug": chapter_slug(f), **d})
        total_obs += d["observational_count"]
        total_words += d["word_count"]

    vol2_baseline_per_1k = round(total_obs / total_words * 1000, 2) if total_words else 0

    # Flag chapters where observational density is < 50% of TRIANGULATED canon baseline
    flagged = []
    nansen_per_1k = nansen_density["per_1k"] if nansen_density else None
    for c in per_chapter:
        if canon_per_1k:
            ratio_to_canon = c["per_1k"] / canon_per_1k
            if ratio_to_canon < 0.5:
                flagged.append({
                    "slug": c["slug"],
                    "per_1k": c["per_1k"],
                    "ratio_to_canon": round(ratio_to_canon, 2),
                    "severity": "high" if ratio_to_canon < 0.35 else "medium",
                })

    rollup = {
        "_schema_version": 0,
        "_phase": "phase-0-observational-density",
        "measured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "canon_baseline_per_1k": canon_per_1k,
        "canon_total_words": canon_total_words,
        "per_source_baselines": per_source,
        "nansen_ceiling_per_1k": nansen_per_1k,
        "vol2_baseline_per_1k": vol2_baseline_per_1k,
        "vol2_total_words": total_words,
        "vol2_total_observational_hits": total_obs,
        "register_imbalance_ratio_vol2_vs_canon": round(vol2_baseline_per_1k / canon_per_1k, 2) if canon_per_1k else None,
        "register_imbalance_ratio_vol2_vs_nansen_ceiling": round(vol2_baseline_per_1k / nansen_per_1k, 2) if nansen_per_1k else None,
        "per_chapter": per_chapter,
        "chapters_below_50pct_canon": flagged,
        "note": "Observational density measures concrete-noun + action-verb hits per 1000 words. Three-source canon baseline averages Nansen 1897, Verne 1897 (Antarctic Mystery), and Verne 1870 (Twenty Thousand Leagues). Chapters below 50% of triangulated baseline are candidates for source ingestion per .pao-inbox/_creative/nansen-ingestion-canon.md.",
    }
    out_path = OUT_DIR / "vol-2-observational-density.json"
    write_json(out_path, rollup)

    # Pretty print
    print()
    print("=" * 84)
    print(f"  Vol 2 observational-density rollup (triangulated canon baseline)")
    print("=" * 84)
    print()
    print(f"  Three-source canon (per .pao-inbox/_creative/nansen-ingestion-canon.md):")
    for s in per_source:
        print(f"    {s['label']:<40s}  {s['words']:>7,} words  {s['per_1k']:>5.2f}/1k")
    if canon_per_1k:
        print(f"    {'Triangulated canon baseline':<40s}  {canon_total_words:>7,} words  {canon_per_1k:>5.2f}/1k")
    print()
    print(f"  Vol 2 baseline:                              {total_words:>7,} words  {vol2_baseline_per_1k:>5.2f}/1k")
    if canon_per_1k:
        ratio = vol2_baseline_per_1k / canon_per_1k
        print(f"  Vol 2 vs triangulated canon ratio:                              {ratio:.2f}× ({'BELOW' if ratio < 1 else 'above'} canon)")
    print()
    print(f"  Per-chapter observational density (sorted ascending — lowest = most candidate for ingestion):")
    print(f"    {'chapter':<55s}  {'words':>6s}  {'obs':>5s}  {'/1k':>6s}  {'vs canon':>10s}")
    for c in sorted(per_chapter, key=lambda x: x["per_1k"]):
        flag = ""
        if canon_per_1k:
            r = c["per_1k"] / canon_per_1k
            flag = f"{r:.2f}x"
            if r < 0.35: flag += " ←HIGH"
            elif r < 0.5: flag += " ←mid"
        print(f"    {c['slug']:<55s}  {c['word_count']:>6d}  {c['observational_count']:>5d}  {c['per_1k']:>6.2f}  {flag:>10s}")
    print()
    if flagged:
        print(f"  Chapters with observational density < 50% of triangulated canon:")
        for c in flagged:
            print(f"    {c['slug']:<55s}  {c['per_1k']:.2f}/1k ({c['ratio_to_canon']:.2f}x of canon) — {c['severity']}")
    print()
    print(f"  → rollup written to {out_path.relative_to(REPO)}")


def run_discover() -> None:
    """Auto-discover non-curated high-density lemmas. Surfaces candidates the curated YAML doesn't cover."""
    families = load_families()
    # Build set of known-tracked tokens (all forms across all curated families)
    tracked_forms = set()
    for spec in families.values():
        for f in spec.get("forms", []):
            tracked_forms.add(f.lower())
        for f in spec.get("excludes", []):
            tracked_forms.add(f.lower())

    files = vol2_files()
    all_tokens = []
    for f in files:
        all_tokens.extend(tokenize(strip_chapter(f.read_text())))

    lemmas = lemmatize_tokens(all_tokens)
    counter = Counter()
    for raw, lem_word in zip(all_tokens, lemmas):
        if raw in tracked_forms: continue   # already covered by a curated family
        if lem_word in STOP_WORDS or len(lem_word) < 4: continue
        counter[lem_word] += 1

    total = len(all_tokens)
    # Filter: lemmas with density >= 2.0/1k and not narratively-essential proper-noun candidates
    PROPER_NOUNS = {"joel", "wanjiru", "priya", "diego", "hiroshi", "maria", "sabina", "anna", "stefan",
                    "punta", "arenas", "saint", "petersburg", "geneva", "tokyo", "tashkent",
                    "bremerhaven", "helsinki", "nansen", "meridian", "helvetica", "drake",
                    "bridge", "anchor", "sunfish", "consortium", "forsaken", "reyes"}
    candidates = []
    for lem_word, c in counter.most_common(50):
        per_1k = c / total * 1000
        if per_1k < 2.0: break
        is_proper_noun = lem_word.lower() in PROPER_NOUNS
        candidates.append({
            "lemma": lem_word,
            "count": c,
            "per_1k": round(per_1k, 2),
            "proper_noun_candidate": is_proper_noun,
        })

    rollup = {
        "_schema_version": 0,
        "_phase": "phase-0-lexical-fatigue-discovery",
        "measured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_tokens": total,
        "tracked_families": list(families.keys()),
        "discovery_threshold_per_1k": 2.0,
        "non_curated_candidates": candidates,
        "note": "Lemmas appearing >= 2.0/1k that are NOT in any curated family. Filter proper nouns manually; remaining lemmas are candidates for new YAML entries.",
    }
    out_path = OUT_DIR / "vol-2-lexical-fatigue-discovery.json"
    write_json(out_path, rollup)

    print(f"Auto-discovery — non-curated lemmas with density >= 2.0/1k across Vol 2 ({total:,} tokens):")
    print(f"  {'lemma':<25s}  {'count':>6s}  {'per /1k':>7s}  {'note':30s}")
    for c in candidates:
        flag = "(proper noun)" if c["proper_noun_candidate"] else ""
        print(f"  {c['lemma']:<25s}  {c['count']:>6d}  {c['per_1k']:>7.2f}  {flag}")
    print()
    print(f"  → {out_path.relative_to(REPO)}")
    print()
    print("  Review proper-noun-flagged lemmas; add the rest to _lexical_fatigue_families.yaml")
    print("  if they represent genuine fatigue candidates (CO ear-test confirms).")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true", help="process every Vol 2 chapter")
    g.add_argument("--chapter", help="process one chapter (substring match against filename)")
    g.add_argument("--rollup", action="store_true", help="compute Vol 2 baseline + flag chapters")
    g.add_argument("--top-lemmas", action="store_true", help="top-30 NLTK-lemmatized stems across Vol 2")
    g.add_argument("--discover", action="store_true", help="auto-find non-curated high-density lemmas (writes JSON)")
    g.add_argument("--observational-density", action="store_true", help="measure observational vocabulary density vs Nansen 1897 baseline (writes JSON)")
    args = ap.parse_args()

    if args.top_lemmas:
        run_top_lemmas()
        return 0
    if args.discover:
        run_discover()
        return 0
    if args.observational_density:
        run_observational_density()
        return 0
    if args.rollup:
        run_rollup()
        return 0
    if args.all:
        run_per_chapter(None)
        return 0
    if args.chapter:
        run_per_chapter(args.chapter)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
