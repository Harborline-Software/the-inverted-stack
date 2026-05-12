"""Hand-count prose-telemetry detectors against a single chapter markdown.

One-shot stdlib-only implementation of the v1 detector list from
.pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md, used to:

  1. Validate the prose-metrics.json schema against a real chapter.
  2. Produce a ground-truth fixture for the engineering session to validate
     Freestylo / StyloMetrix output against.
  3. Surface a first measurement of Anna's new (Filchner / Bobiverse register)
     trial chapter for comparison against the old Vol 2 baseline.

This is intentionally not the real platform — it's a calibration tool. Real
platform lives at galley/lib/prose_telemetry/ once the engineering session
ships Phase 1. Anything this script flags should also flag in the real
platform; anything the real platform finds that this script misses is
fair game (this script can't do POS-based isocolon, distributed chiasmus,
or any ML-tier detector).

Usage:
  python build/prose_telemetry_handcount.py <chapter.md> [--out <path.json>]
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
from datetime import datetime, timezone
from pathlib import Path

CHAPTER_REPO_ROOT = Path(__file__).resolve().parent.parent


# ─── Source preparation ───────────────────────────────────────────────────

_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_HEADING = re.compile(r"^\s*#+\s.*$", re.MULTILINE)
_HRULE = re.compile(r"^\s*-{3,}\s*$", re.MULTILINE)
_BLOCKQUOTE = re.compile(r"^\s*>\s.*$", re.MULTILINE)
_CODEFENCE = re.compile(r"```.*?```", re.DOTALL)


def strip_to_prose(md: str) -> str:
    """Return body prose only — drop headings, hrules, comments, fenced code,
    block quotes. Keep paragraphs and inline italics/em-dashes as-is."""
    md = _CODEFENCE.sub("", md)
    md = _HTML_COMMENT.sub("", md)
    md = _HEADING.sub("", md)
    md = _HRULE.sub("", md)
    md = _BLOCKQUOTE.sub("", md)
    return md.strip()


# ─── Sentence + token segmentation ────────────────────────────────────────

# Simple sentence-boundary heuristic. Punctuation followed by whitespace and
# an uppercase letter / quote / opening paren. Good enough for hand-count;
# spaCy will replace this in the real platform.
_SENT_BOUNDARY = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"“\(*])")


def sentences(prose: str) -> list[str]:
    flat = re.sub(r"\s+", " ", prose).strip()
    if not flat:
        return []
    raw = _SENT_BOUNDARY.split(flat)
    return [s.strip() for s in raw if s.strip()]


def tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z'-]*", text)


# ─── Detectors ────────────────────────────────────────────────────────────

def detect_anaphora(sents: list[str], n_prefix: int = 2, min_run: int = 3) -> list[dict]:
    """Consecutive sentences sharing the first n_prefix words. Reports runs of
    length >= min_run (a run of 3 = three consecutive sentences with same
    opening, including the first one)."""
    if not sents:
        return []
    findings: list[dict] = []

    def prefix(s: str) -> str | None:
        toks = tokens(s)[:n_prefix]
        if len(toks) < n_prefix:
            return None
        return " ".join(t.lower() for t in toks)

    i = 0
    while i < len(sents):
        pref = prefix(sents[i])
        if pref is None:
            i += 1
            continue
        j = i + 1
        while j < len(sents) and prefix(sents[j]) == pref:
            j += 1
        run_len = j - i
        if run_len >= min_run:
            findings.append({
                "type": "anaphora",
                "run_length": run_len,
                "prefix": " ".join(tokens(sents[i])[:n_prefix]),
                "sentences": sents[i:j],
                "confidence": 1.0,
                "rule_id": "handcount:anaphora.consecutive_sentence_opening",
            })
        i = j
    return findings


_TAUT_RE = re.compile(
    r"\bthe\s+(\w+)\s+(?:was|is|were|are|had been|has been)\s+the\s+\1\b",
    re.IGNORECASE,
)


def detect_tautology(prose: str) -> list[dict]:
    """`the X was the X` and grammatical variants."""
    findings = []
    for m in _TAUT_RE.finditer(prose):
        findings.append({
            "type": "tautological_self_equation",
            "head": m.group(1).lower(),
            "start_char": m.start(),
            "end_char": m.end(),
            "text": m.group(0),
            "confidence": 1.0,
            "rule_id": "handcount:tautological_self_equation.regex",
        })
    return findings


def detect_asyndeton(sents: list[str], min_items: int = 3) -> list[dict]:
    """Comma-separated list of >= min_items with no 'and'/'or' before the last
    element. Conservative: only flags clear cases."""
    findings = []
    for s in sents:
        # Find longest comma-separated run of word groups without and/or
        # immediately before the final group.
        if "," not in s:
            continue
        # Heuristic: tail of sentence with no ", and " or ", or " before the last clause.
        # Count commas; if 2+ commas and no "and "/"or " in the last 30 chars before period.
        commas = s.count(",")
        tail = s.rstrip(".!?").rsplit(",", 1)[-1].strip()
        if commas >= (min_items - 1) and not re.match(r"^(and|or|nor|but)\b", tail, re.IGNORECASE):
            findings.append({
                "type": "asyndeton",
                "commas": commas,
                "sentence": s,
                "confidence": 0.6,  # heuristic; flag-not-prove
                "rule_id": "handcount:asyndeton.comma_run_no_conjunction",
            })
    return findings


def detect_polysyndeton(sents: list[str], min_conjunctions: int = 3) -> list[dict]:
    """3+ 'and'/'or' within one sentence."""
    findings = []
    for s in sents:
        ands = len(re.findall(r"\band\b", s, re.IGNORECASE))
        ors = len(re.findall(r"\bor\b", s, re.IGNORECASE))
        total = ands + ors
        if total >= min_conjunctions:
            findings.append({
                "type": "polysyndeton",
                "and_count": ands,
                "or_count": ors,
                "sentence": s,
                "confidence": 0.8,
                "rule_id": "handcount:polysyndeton.conjunction_density",
            })
    return findings


def detect_literal_tricolon(sents: list[str]) -> list[dict]:
    """Heuristic: exactly two commas with no 'and'/'or' between the first two
    items and an 'and'/'or' before the third (classic A, B, and C)."""
    findings = []
    for s in sents:
        # Look for "X, Y, and Z" or "X, Y, or Z" patterns
        m = re.search(r"(\b\w[\w' -]{2,40}),\s+(\b\w[\w' -]{2,40}),\s+(?:and|or)\s+(\b\w[\w' -]{2,40})", s)
        if m:
            findings.append({
                "type": "literal_tricolon",
                "items": [m.group(1).strip(), m.group(2).strip(), m.group(3).strip()],
                "text": m.group(0),
                "confidence": 0.75,
                "rule_id": "handcount:literal_tricolon.serial_comma_pattern",
            })
    return findings


_EPANORTH_RE = re.compile(
    r"\bnot\s+[^,.;:—-]{2,60}\s+[—–-]\s+[A-Za-z]",
    re.IGNORECASE,
)


def detect_epanorthosis(prose: str) -> list[dict]:
    """*not X — Y* self-correction patterns."""
    findings = []
    for m in _EPANORTH_RE.finditer(prose):
        findings.append({
            "type": "epanorthosis",
            "text": m.group(0),
            "start_char": m.start(),
            "end_char": m.end(),
            "confidence": 0.7,
            "rule_id": "handcount:epanorthosis.not_X_em_Y",
        })
    return findings


# ─── Document-level metrics ───────────────────────────────────────────────

def document_metrics(prose: str, sents: list[str]) -> dict:
    word_lens = [len(tokens(s)) for s in sents]
    if not word_lens:
        return {}
    p50 = int(statistics.median(word_lens))
    sorted_lens = sorted(word_lens)
    p90 = sorted_lens[int(0.9 * (len(sorted_lens) - 1))]
    return {
        "word_count": sum(word_lens),
        "sentence_count": len(sents),
        "paragraph_count": len([p for p in prose.split("\n\n") if p.strip()]),
        "sentence_length_p50": p50,
        "sentence_length_p90": p90,
        "sentences_over_50_words": sum(1 for w in word_lens if w > 50),
        "sentences_over_30_words": sum(1 for w in word_lens if w > 30),
        "longest_sentence_words": max(word_lens),
    }


# ─── Meters (normalization) ───────────────────────────────────────────────

def per_1k(n: int, total_words: int) -> float:
    if total_words == 0:
        return 0.0
    return round(n * 1000 / total_words, 2)


def sentence_coverage(annotations: list[dict], total_sents: int, key: str) -> float:
    """Approximate sentence-coverage for run-bearing devices."""
    if total_sents == 0:
        return 0.0
    if key == "anaphora":
        trapped = sum(a.get("run_length", 0) for a in annotations)
        return round(100 * trapped / total_sents, 1)
    return round(100 * len(annotations) / total_sents, 1)


def meters(annotations_by_type: dict[str, list[dict]], doc: dict) -> list[dict]:
    out = []
    total_w = doc.get("word_count", 0)
    total_s = doc.get("sentence_count", 0)
    for dev, anns in annotations_by_type.items():
        m = {
            "device": dev,
            "raw_count": len(anns),
            "count_per_1k_tokens": per_1k(len(anns), total_w),
            "sentence_coverage_pct": sentence_coverage(anns, total_s, dev),
        }
        if dev == "anaphora" and anns:
            m["max_run_length"] = max(a["run_length"] for a in anns)
        out.append(m)
    return out


# ─── Verdict / rollup ─────────────────────────────────────────────────────

DEFAULT_THRESHOLDS = {
    "anaphora_density_per_1000": 25.0,
    "anaphora_max_run_length": 3,
    "tautology_density_per_1000": 3.0,
    "polysyndeton_density_per_1000": 5.0,
    "sentences_over_50_words_pct": 3.0,
}


def verdict(metrics_list: list[dict], doc: dict, thresholds: dict) -> dict:
    warnings: list[str] = []
    blockers: list[str] = []
    passes: list[str] = []

    by_dev = {m["device"]: m for m in metrics_list}

    def check(name: str, actual: float, limit: float, blocker_factor: float = 1.5):
        if actual > limit * blocker_factor:
            blockers.append(f"{name}: {actual} exceeds blocker threshold {limit * blocker_factor}")
        elif actual > limit:
            warnings.append(f"{name}: {actual} exceeds threshold {limit}")
        else:
            passes.append(name)

    if "anaphora" in by_dev:
        check("anaphora_density_per_1000",
              by_dev["anaphora"]["count_per_1k_tokens"],
              thresholds["anaphora_density_per_1000"])
        if "max_run_length" in by_dev["anaphora"]:
            check("anaphora_max_run_length",
                  by_dev["anaphora"]["max_run_length"],
                  thresholds["anaphora_max_run_length"])
    if "tautological_self_equation" in by_dev:
        check("tautology_density_per_1000",
              by_dev["tautological_self_equation"]["count_per_1k_tokens"],
              thresholds["tautology_density_per_1000"])
    if "polysyndeton" in by_dev:
        check("polysyndeton_density_per_1000",
              by_dev["polysyndeton"]["count_per_1k_tokens"],
              thresholds["polysyndeton_density_per_1000"])

    if blockers:
        v = "red"
    elif warnings:
        v = "yellow"
    else:
        v = "green"
    return {"verdict": v, "blockers": blockers, "warnings": warnings, "passes": passes}


# ─── Main ─────────────────────────────────────────────────────────────────

def measure(md_path: Path, dimensions: dict | None = None) -> dict:
    raw = md_path.read_text(encoding="utf-8")
    prose = strip_to_prose(raw)
    sents = sentences(prose)
    doc = document_metrics(prose, sents)

    findings_by_type = {
        "anaphora": detect_anaphora(sents),
        "tautological_self_equation": detect_tautology(prose),
        "asyndeton": detect_asyndeton(sents),
        "polysyndeton": detect_polysyndeton(sents),
        "literal_tricolon": detect_literal_tricolon(sents),
        "epanorthosis": detect_epanorthosis(prose),
    }

    all_findings = [a for anns in findings_by_type.values() for a in anns]
    metrics_list = meters(findings_by_type, doc)
    roll = verdict(metrics_list, doc, DEFAULT_THRESHOLDS)

    return {
        "_schema_version": 2,
        "_schema_status": "handcount-pilot — stdlib-only validation against ch01-departure.trial.md",
        "_schema_notes": "Hand-instrumented; not the real platform. Real platform per .pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md.",
        "chapter_slug": md_path.stem.replace(".trial", ""),
        "source_path": str(md_path.relative_to(CHAPTER_REPO_ROOT)) if md_path.is_relative_to(CHAPTER_REPO_ROOT) else str(md_path),
        "measured_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dimensions": dimensions or {
            "volume": 2,
            "act": 1,
            "chapter_number": 1,
            "icm_stage": "icm/trial",
            "voice_pass_status": "trial-clean-slate",
            "author": "anna",
            "genre": "literary-sf-bobiverse-register",
            "model_version": "handcount-stdlib-2026-05-12",
            "revision": "2026-05-12-bakery-mother-drawings",
            "section": "departure-arc",
        },
        "detected_devices": all_findings,
        "metrics": metrics_list,
        "document_metrics": doc,
        "ear_test_thresholds": DEFAULT_THRESHOLDS,
        "rollup": roll,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", type=Path)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    result = measure(args.chapter)

    out_path = args.out or Path(
        f"/Users/christopherwood/Projects/SunfishSoftware/galley/build/the-inverted-stack/output/qa/{args.chapter.stem}.prose-metrics.json"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    roll = result["rollup"]
    doc = result["document_metrics"]
    print(f"  → {out_path}")
    print(f"  verdict: {roll['verdict']}  warnings: {len(roll['warnings'])}  blockers: {len(roll['blockers'])}")
    print(f"  words: {doc['word_count']}  sentences: {doc['sentence_count']}  paragraphs: {doc['paragraph_count']}")
    print(f"  sentence_length_p50: {doc['sentence_length_p50']}  p90: {doc['sentence_length_p90']}  longest: {doc['longest_sentence_words']}")
    print()
    for m in result["metrics"]:
        extra = f"  max_run={m['max_run_length']}" if "max_run_length" in m else ""
        print(f"  {m['device']:32s} raw={m['raw_count']:>3}  per_1k={m['count_per_1k_tokens']:>6.2f}  sent_cov={m['sentence_coverage_pct']:>5.1f}%{extra}")
    if roll["warnings"]:
        print()
        for w in roll["warnings"]:
            print(f"  ⚠ {w}")
    if roll["blockers"]:
        print()
        for b in roll["blockers"]:
            print(f"  ✗ {b}")


if __name__ == "__main__":
    main()
