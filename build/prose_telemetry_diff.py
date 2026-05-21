"""Diff two prose-telemetry runs to surface drift.

Workflow:
  1. Snapshot a chapter's metrics under a named tag:
        python build/prose_telemetry_diff.py snapshot ch01-departure.trial pre-edit
  2. Apply edits, re-run prose_telemetry_handcount.py.
  3. Diff against the snapshot:
        python build/prose_telemetry_diff.py diff ch01-departure.trial pre-edit

The diff surfaces +/- changes per detector, document-level metrics, and
aggregate-metric drift (lexical diversity, sentence-starter entropy,
attribution variety). Useful for confirming a cull-pass actually moved
the needle, per the architecture-doc Phase 2 brief:
"Add baseline-drift-detection: compare current metrics to last measurement;
flag improvement / regression."

Snapshots live at galley/build/<book>/output/qa/snapshots/<chapter>.<tag>.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

QA_DIR = Path("/Users/christopherwood/Projects/SunfishSoftware/galley/build/the-inverted-stack/output/qa")
SNAPSHOT_DIR = QA_DIR / "snapshots"


def _metric_path(chapter_stem: str) -> Path:
    return QA_DIR / f"{chapter_stem}.prose-metrics.json"


def _snapshot_path(chapter_stem: str, tag: str) -> Path:
    return SNAPSHOT_DIR / f"{chapter_stem}.{tag}.json"


def cmd_snapshot(chapter_stem: str, tag: str) -> None:
    src = _metric_path(chapter_stem)
    if not src.exists():
        sys.exit(f"No metrics file at {src}")
    dst = _snapshot_path(chapter_stem, tag)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Snapshot saved: {dst}")


def _build_metric_map(m: dict) -> dict[str, dict]:
    return {met["device"]: met for met in m.get("metrics", [])}


def _fmt_delta(before: float, after: float, fmt: str = "{:.1f}") -> str:
    if before == after:
        return "-"
    delta = after - before
    sign = "+" if delta > 0 else ""
    return f"{sign}{fmt.format(delta)}"


def cmd_diff(chapter_stem: str, tag: str, threshold: int = 1) -> None:
    snap_path = _snapshot_path(chapter_stem, tag)
    cur_path = _metric_path(chapter_stem)
    if not snap_path.exists():
        sys.exit(f"No snapshot at {snap_path}. Run `snapshot` first.")
    if not cur_path.exists():
        sys.exit(f"No current metrics at {cur_path}. Run prose_telemetry_handcount.")
    before = json.loads(snap_path.read_text(encoding="utf-8"))
    after = json.loads(cur_path.read_text(encoding="utf-8"))

    print(f"DIFF: {chapter_stem}  ({tag} → current)")
    print(f"  Snapshot: {snap_path.name}  measured_at={before.get('measured_at')}")
    print(f"  Current:  {cur_path.name}  measured_at={after.get('measured_at')}")
    print()

    # Document-level changes.
    before_doc = before.get("document_metrics", {})
    after_doc = after.get("document_metrics", {})
    doc_keys = ["word_count", "sentence_count", "paragraph_count",
                "sentence_length_p50", "sentence_length_p90", "longest_sentence_words"]
    print("DOCUMENT")
    for k in doc_keys:
        b = before_doc.get(k, 0)
        a = after_doc.get(k, 0)
        if b != a:
            print(f"  {k:30s}  {b:>6}  →  {a:>6}    ({_fmt_delta(b, a, '{:+d}')})")
    print()

    # Aggregate metrics.
    print("AGGREGATE")
    for section in ["lexical_diversity", "sentence_starter_diversity", "attribution_variety"]:
        b_sec = before.get(section, {}) or {}
        a_sec = after.get(section, {}) or {}
        for k in b_sec:
            b = b_sec.get(k)
            a = a_sec.get(k)
            if isinstance(b, (int, float)) and isinstance(a, (int, float)) and b != a:
                print(f"  {section}.{k:20s}  {b:>8.4f}  →  {a:>8.4f}")
    print()

    # Per-detector counts.
    bm = _build_metric_map(before)
    am = _build_metric_map(after)
    keys = sorted(set(bm) | set(am))
    print("DETECTORS  (change ≥ threshold; |Δ raw_count|)")
    changes: list[tuple[int, str, int, int, float, float]] = []
    for k in keys:
        b = bm.get(k, {})
        a = am.get(k, {})
        b_n = b.get("raw_count", 0)
        a_n = a.get("raw_count", 0)
        if abs(b_n - a_n) >= threshold:
            changes.append((a_n - b_n, k, b_n, a_n,
                            b.get("count_per_1k_tokens", 0),
                            a.get("count_per_1k_tokens", 0)))
    # Sort: largest reductions (most-negative) first, then largest increases.
    changes.sort(key=lambda x: x[0])
    for delta, k, b_n, a_n, b_per, a_per in changes:
        arrow = "↓" if delta < 0 else "↑"
        print(f"  {arrow} {k:32s}  {b_n:>4} → {a_n:>4}   ({a_n - b_n:+d})   "
              f"per-1k: {b_per:5.2f} → {a_per:5.2f}")

    # Verdict change.
    print()
    print("VERDICT")
    b_v = before.get("rollup", {}).get("verdict")
    a_v = after.get("rollup", {}).get("verdict")
    b_blockers = len(before.get("rollup", {}).get("blockers", []))
    a_blockers = len(after.get("rollup", {}).get("blockers", []))
    b_warnings = len(before.get("rollup", {}).get("warnings", []))
    a_warnings = len(after.get("rollup", {}).get("warnings", []))
    print(f"  {b_v:>8} → {a_v:<8}    blockers: {b_blockers} → {a_blockers}    warnings: {b_warnings} → {a_warnings}")


def cmd_list(chapter_stem: str | None) -> None:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    snaps = sorted(SNAPSHOT_DIR.glob("*.json"))
    if chapter_stem:
        snaps = [s for s in snaps if s.stem.startswith(chapter_stem + ".")]
    for s in snaps:
        try:
            m = json.loads(s.read_text(encoding="utf-8"))
            print(f"  {s.name}  measured_at={m.get('measured_at', '?')}  verdict={m.get('rollup', {}).get('verdict', '?')}")
        except Exception:
            print(f"  {s.name}  (unreadable)")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot", help="Save current metrics as a named snapshot")
    s.add_argument("chapter_stem", help="e.g. ch01-departure.trial")
    s.add_argument("tag", help="Snapshot tag, e.g. 'pre-edit', '2026-05-13-baseline'")
    d = sub.add_parser("diff", help="Diff snapshot vs current metrics")
    d.add_argument("chapter_stem")
    d.add_argument("tag")
    d.add_argument("--threshold", type=int, default=1, help="Min |Δ raw_count| to report")
    l = sub.add_parser("list", help="List available snapshots")
    l.add_argument("chapter_stem", nargs="?", default=None)
    args = ap.parse_args()
    if args.cmd == "snapshot":
        cmd_snapshot(args.chapter_stem, args.tag)
    elif args.cmd == "diff":
        cmd_diff(args.chapter_stem, args.tag, args.threshold)
    elif args.cmd == "list":
        cmd_list(args.chapter_stem)


if __name__ == "__main__":
    main()
