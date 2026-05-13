"""Reference-corpus comparison for prose-telemetry.

Phase 3 of the architecture: "Run detectors against reference texts (Towles,
Hemingway, etc.); establish empirical thresholds; threshold-driven cull-pass
guidance per chapter."

Pipeline:
  1. Place reference texts (`.txt` or `.md`) in a corpus directory.
     Recommended structure:
        corpora/
          bobiverse/
            sample1.txt
            sample2.txt
          towles/
            sample1.txt
          hemingway/
            ...
  2. Run `compute` to measure every reference text:
        python build/prose_telemetry_corpus.py compute corpora/bobiverse/
  3. The aggregated baseline is written to
     `corpora/<name>/baseline.json` with per-detector mean/stdev/p50/p90
     across the corpus. Per-1k-token normalization makes lengths comparable.
  4. Run `compare` against a chapter:
        python build/prose_telemetry_corpus.py compare \\
            ch01-departure \\
            corpora/bobiverse/baseline.json
     Shows where this chapter sits in the corpus distribution per detector
     (z-score and percentile).

The corpora directory is gitignored (the texts are usually copyrighted);
contributors source their own reference samples.

Note: this tool reads reference texts as raw text. For full strip-to-prose
behavior (HTML comments, fenced code), pre-process the texts to plain
prose before placing them in the corpus.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

# Import the measure function from the handcount module.
sys.path.insert(0, str(Path(__file__).parent))
from prose_telemetry_handcount import measure  # noqa


def measure_text_file(path: Path) -> dict:
    """Measure a single reference text file (treats it as a chapter)."""
    # The measure() function reads markdown and strips it; for plain .txt files
    # the strip is a no-op. Both formats work.
    return measure(path)


def compute_corpus(corpus_dir: Path) -> dict:
    """Walk a corpus directory and compute per-detector statistics across
    every reference file. Returns a baseline dict suitable for `compare`."""
    files = sorted(list(corpus_dir.glob("*.txt")) + list(corpus_dir.glob("*.md")))
    files = [f for f in files if f.name != "baseline.json"]
    if not files:
        sys.exit(f"No .txt or .md files in {corpus_dir}")

    print(f"Measuring {len(files)} reference text(s) in {corpus_dir.name}...")
    per_file = []
    for fp in files:
        try:
            m = measure(fp)
            per_file.append({
                "file": fp.name,
                "word_count": m.get("document_metrics", {}).get("word_count", 0),
                "metrics": {met["device"]: met for met in m.get("metrics", [])},
                "lexical_diversity": m.get("lexical_diversity", {}),
                "sentence_starter_diversity": m.get("sentence_starter_diversity", {}),
                "attribution_variety": m.get("attribution_variety", {}),
                "document_metrics": m.get("document_metrics", {}),
            })
            print(f"  ✓ {fp.name}  ({per_file[-1]['word_count']} words)")
        except Exception as e:
            print(f"  ✗ {fp.name}: {e}")

    if not per_file:
        sys.exit("No reference texts measured successfully.")

    # Aggregate per detector: collect per_1k values, then compute mean/stdev/p50/p90.
    all_devices: set[str] = set()
    for pf in per_file:
        all_devices.update(pf["metrics"].keys())

    per_detector = {}
    for dev in sorted(all_devices):
        values = [pf["metrics"].get(dev, {}).get("count_per_1k_tokens", 0) for pf in per_file]
        per_detector[dev] = {
            "samples": len(values),
            "mean_per_1k": round(statistics.mean(values), 3),
            "stdev_per_1k": round(statistics.stdev(values), 3) if len(values) > 1 else 0.0,
            "median_per_1k": round(statistics.median(values), 3),
            "p90_per_1k": round(sorted(values)[int(0.9 * (len(values) - 1))], 3) if values else 0.0,
            "max_per_1k": round(max(values), 3),
            "min_per_1k": round(min(values), 3),
        }

    # Aggregate document-level + lexical-diversity metrics.
    def _agg(key, sub):
        vals = [pf[key].get(sub) for pf in per_file if pf[key].get(sub) is not None]
        vals = [v for v in vals if isinstance(v, (int, float))]
        if not vals:
            return None
        return {
            "mean": round(statistics.mean(vals), 4),
            "stdev": round(statistics.stdev(vals), 4) if len(vals) > 1 else 0.0,
            "median": round(statistics.median(vals), 4),
        }

    aggregates = {
        "ttr": _agg("lexical_diversity", "ttr"),
        "mattr_1000": _agg("lexical_diversity", "mattr_1000"),
        "sentence_starter_entropy": _agg("sentence_starter_diversity", "entropy"),
        "attribution_entropy": _agg("attribution_variety", "entropy"),
        "said_share": _agg("attribution_variety", "said_share"),
        "sentence_length_p50": _agg("document_metrics", "sentence_length_p50"),
        "sentence_length_p90": _agg("document_metrics", "sentence_length_p90"),
    }

    baseline = {
        "_schema_version": 1,
        "corpus_name": corpus_dir.name,
        "files_measured": len(per_file),
        "total_words": sum(pf["word_count"] for pf in per_file),
        "per_detector": per_detector,
        "aggregates": aggregates,
    }
    out = corpus_dir / "baseline.json"
    out.write_text(json.dumps(baseline, indent=2), encoding="utf-8")
    print()
    print(f"Baseline written: {out}")
    print(f"  Files: {baseline['files_measured']}")
    print(f"  Total words: {baseline['total_words']:,}")


def _zscore(value: float, mean: float, stdev: float) -> float:
    return (value - mean) / stdev if stdev > 0 else 0.0


def compare_chapter(chapter_stem: str, baseline_path: Path, qa_dir: Path) -> None:
    chapter_metrics_path = qa_dir / f"{chapter_stem}.prose-metrics.json"
    if not chapter_metrics_path.exists():
        sys.exit(f"No metrics at {chapter_metrics_path}. Run prose_telemetry_handcount first.")
    chapter = json.loads(chapter_metrics_path.read_text(encoding="utf-8"))
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))

    print(f"COMPARE: {chapter_stem}  vs  corpus: {baseline['corpus_name']}")
    print(f"  Chapter: {chapter.get('document_metrics', {}).get('word_count', 0):,} words")
    print(f"  Corpus:  {baseline['total_words']:,} words across {baseline['files_measured']} files")
    print()

    # Per-detector comparison.
    chapter_metrics = {met["device"]: met for met in chapter.get("metrics", [])}
    per_det = baseline.get("per_detector", {})
    print(f"{'detector':<32s} {'chapter':>10s} {'corpus_mean':>12s} {'stdev':>8s} {'z':>6s}  flag")
    print(f"{'-' * 32} {'-' * 10} {'-' * 12} {'-' * 8} {'-' * 6}  ----")
    for dev in sorted(per_det):
        ch_val = chapter_metrics.get(dev, {}).get("count_per_1k_tokens", 0)
        b = per_det[dev]
        z = _zscore(ch_val, b["mean_per_1k"], b["stdev_per_1k"])
        flag = ""
        if abs(z) >= 2:
            flag = "★★ outlier" if z > 0 else "★★ low"
        elif abs(z) >= 1:
            flag = "★  high" if z > 0 else "★  low"
        print(f"{dev:<32s} {ch_val:>10.2f} {b['mean_per_1k']:>12.2f} {b['stdev_per_1k']:>8.2f} "
              f"{z:>+6.2f}  {flag}")

    # Aggregate comparison.
    print()
    print("AGGREGATE METRICS  (chapter | corpus mean ± stdev | z)")
    aggregate_map = [
        ("ttr", ("lexical_diversity", "ttr")),
        ("mattr_1000", ("lexical_diversity", "mattr_1000")),
        ("sentence_starter_entropy", ("sentence_starter_diversity", "entropy")),
        ("attribution_entropy", ("attribution_variety", "entropy")),
        ("said_share", ("attribution_variety", "said_share")),
        ("sentence_length_p50", ("document_metrics", "sentence_length_p50")),
        ("sentence_length_p90", ("document_metrics", "sentence_length_p90")),
    ]
    for name, (section, sub) in aggregate_map:
        ch = chapter.get(section, {}).get(sub)
        b = baseline["aggregates"].get(name)
        if ch is None or b is None:
            continue
        z = _zscore(ch, b["mean"], b["stdev"])
        flag = "★ high" if z > 1 else ("★ low" if z < -1 else "")
        print(f"  {name:<32s} {ch:>8.3f}  |  {b['mean']:.3f} ± {b['stdev']:.3f}  |  z={z:+.2f}  {flag}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("compute", help="Compute a corpus baseline from reference texts")
    c.add_argument("corpus_dir", type=Path)
    cmp = sub.add_parser("compare", help="Compare a chapter against a corpus baseline")
    cmp.add_argument("chapter_stem")
    cmp.add_argument("baseline_path", type=Path)
    cmp.add_argument("--qa-dir", type=Path,
                     default=Path("/Users/christopherwood/Projects/SunfishSoftware/galley/build/the-inverted-stack/output/qa"))
    args = ap.parse_args()
    if args.cmd == "compute":
        compute_corpus(args.corpus_dir)
    elif args.cmd == "compare":
        compare_chapter(args.chapter_stem, args.baseline_path, args.qa_dir)


if __name__ == "__main__":
    main()
