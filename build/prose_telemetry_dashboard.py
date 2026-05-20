"""Render prose-telemetry metrics as an HTML dashboard.

Generates a single-page HTML report from one or more chapter prose-metrics
JSON files. Per-chapter cards show verdict, top metrics, and detected
findings; a cross-chapter comparison table surfaces drift between chapters.

Usage:
    python build/prose_telemetry_dashboard.py <metrics.json>...
    python build/prose_telemetry_dashboard.py --glob 'galley/build/the-inverted-stack/output/qa/*.prose-metrics.json'
    python build/prose_telemetry_dashboard.py --out report.html <metrics.json>...

Phase 2 of the prose-telemetry platform per the 2026-05-08 architecture
doc: "Wire <chapter>.prose-metrics.json into the QA dashboard's per-chapter
card."
"""

from __future__ import annotations

import argparse
import glob
import html
import json
import sys
from pathlib import Path


VERDICT_COLORS = {
    "green": "#4ade80",
    "yellow": "#fbbf24",
    "red": "#ef4444",
    "gray": "#9ca3af",
}


def _esc(s: str) -> str:
    return html.escape(s if isinstance(s, str) else str(s))


def render_chapter_card(m: dict) -> str:
    """Render a single chapter as an HTML card."""
    slug = m.get("chapter_slug", "(unknown)")
    roll = m.get("rollup", {})
    verdict = roll.get("verdict", "gray")
    color = VERDICT_COLORS.get(verdict, "#9ca3af")
    doc = m.get("document_metrics", {})
    lex = m.get("lexical_diversity", {})
    starter = m.get("sentence_starter_diversity", {})
    attr = m.get("attribution_variety", {})
    metrics = m.get("metrics", [])
    held_findings = m.get("held_findings_count", 0)

    findings = m.get("detected_devices", [])
    by_type: dict[str, list[dict]] = {}
    for f in findings:
        if f.get("held"):
            continue
        by_type.setdefault(f.get("type", "?"), []).append(f)

    # Top metrics summary
    metrics_rows = []
    for met in sorted(metrics, key=lambda x: -x.get("raw_count", 0)):
        n = met.get("raw_count", 0)
        if n == 0 and met.get("held_count", 0) == 0:
            continue
        held = met.get("held_count", 0)
        held_str = f' <span class="held">+{held} held</span>' if held else ""
        metrics_rows.append(
            f'<tr><td>{_esc(met["device"])}</td>'
            f'<td class="num">{n}</td>'
            f'<td class="num">{met.get("count_per_1k_tokens", 0):.2f}</td>'
            f'<td class="num">{met.get("sentence_coverage_pct", 0):.1f}%</td>'
            f'<td>{held_str}</td></tr>'
        )

    warnings_html = "".join(
        f'<li class="warning">⚠ {_esc(w)}</li>' for w in roll.get("warnings", [])
    )
    blockers_html = "".join(
        f'<li class="blocker">✗ {_esc(b)}</li>' for b in roll.get("blockers", [])
    )

    findings_sections = []
    for dev_type, anns in sorted(by_type.items(), key=lambda kv: -len(kv[1])):
        if len(anns) == 0:
            continue
        items_html = []
        for a in anns[:5]:
            txt = _finding_summary(a)
            items_html.append(f"<li>{_esc(txt)}</li>")
        more = f"<li class='more'>...and {len(anns)-5} more</li>" if len(anns) > 5 else ""
        findings_sections.append(
            f'<details><summary>{_esc(dev_type)} <span class="count">({len(anns)})</span></summary>'
            f'<ul>{"".join(items_html)}{more}</ul></details>'
        )

    return f"""
    <article class="card" data-verdict="{verdict}">
      <header style="border-left: 6px solid {color};">
        <h2>{_esc(slug)}</h2>
        <span class="verdict" style="background:{color};">{verdict.upper()}</span>
      </header>
      <section class="docmetrics">
        <span>{doc.get("word_count", 0)} words</span>
        <span>{doc.get("sentence_count", 0)} sentences</span>
        <span>{doc.get("paragraph_count", 0)} paragraphs</span>
        <span>p50={doc.get("sentence_length_p50", 0)}w</span>
        <span>p90={doc.get("sentence_length_p90", 0)}w</span>
        <span>longest={doc.get("longest_sentence_words", 0)}w</span>
      </section>
      <section class="aggregate">
        <span>TTR <b>{lex.get("ttr", 0):.3f}</b></span>
        <span>MATTR-1000 <b>{lex.get("mattr_1000", 0):.3f}</b></span>
        <span>starter-entropy <b>{starter.get("entropy", 0):.2f}</b>
              <small>(top "{_esc(starter.get("top_starter", ""))}" {starter.get("top_starter_share", 0)*100:.1f}%)</small></span>
        <span>attribution-entropy <b>{attr.get("entropy", 0):.2f}</b>
              <small>(said-share {attr.get("said_share", 0)*100:.0f}%)</small></span>
        {f'<span class="held-count">held findings: <b>{held_findings}</b></span>' if held_findings else ''}
      </section>
      {f'<ul class="blockers">{blockers_html}</ul>' if blockers_html else ''}
      {f'<ul class="warnings">{warnings_html}</ul>' if warnings_html else ''}
      <section class="metrics">
        <h3>Metrics</h3>
        <table>
          <thead><tr><th>device</th><th>n</th><th>/1k</th><th>cov</th><th></th></tr></thead>
          <tbody>{"".join(metrics_rows)}</tbody>
        </table>
      </section>
      <section class="findings">
        <h3>Findings ({sum(len(v) for v in by_type.values())} active)</h3>
        {"".join(findings_sections)}
      </section>
    </article>
    """


def _finding_summary(a: dict) -> str:
    """One-line text representation of a finding."""
    t = a.get("type", "")
    if t == "anaphora":
        return f'run={a.get("run_length")} prefix="{a.get("prefix")}" → {a.get("sentences", [""])[0][:80]}...'
    if t == "lexical_chain_loop":
        return f'{a.get("word")} ×{a.get("count")} (density {a.get("density_per_100", 0)}/100)'
    if t == "bigram_chain_loop":
        return f'"{a.get("bigram")}" ×{a.get("count")} (para {a.get("paragraph_word_count")}w)'
    if t == "trigram_chain_loop":
        return f'"{a.get("trigram")}" ×{a.get("count")}'
    if t == "self_referential_frame":
        return f'"{a.get("phrase")}"'
    if t == "motif_overuse":
        return f'"{a.get("phrase")}" ×{a.get("count")} (cap={a.get("cap")}, status={a.get("status")})'
    if t == "statement_then_reversal":
        return f'[{a.get("reversal_marker")}] ...{a.get("first", "")[-50:]} → {a.get("second", "")[:50]}...'
    if t == "anadiplosis":
        return f'echo "{a.get("echo_word")}"'
    if t == "echo_and_confirm":
        return f'rule→confirm: ...{a.get("rule_sentence", "")[-40:]} | {a.get("confirm_sentence", "")[:40]}'
    if t in ("filter_word", "vague_quantifier", "modal_verb", "adverb_ly",
             "abstract_noun", "conjunctive_adverb", "temporal_marker",
             "gerund", "infinitive_phrase", "redundant_phrase", "cliche"):
        return f'{a.get("word") or a.get("verb") or a.get("phrase") or a.get("match") or a.get("modal")}'
    if t == "tautological_self_equation":
        return f'{a.get("text", "")}'
    if t == "timestamp":
        return f'{a.get("time")}'
    if t == "proper_noun":
        return f'{a.get("word")}'
    if t == "paragraph_length_anomaly":
        return f'{a.get("kind")} ({a.get("word_count")}w vs mean {a.get("chapter_mean")}w)'
    if t == "expletive_construction":
        return f'"{a.get("opener")}" → {a.get("sentence_start", "")[:60]}...'
    if t == "conjunction_start":
        return f'{a.get("conjunction")} → {a.get("sentence_start", "")[:60]}...'
    if t == "paragraph_opener_repeat":
        return f'"{a.get("word")}" opens {a.get("count")} paragraphs (of {a.get("total_paragraphs")})'
    if t == "direct_address":
        return f'"{a.get("phrase")}"'
    if t == "passive_voice":
        return f'"{a.get("match")}"'
    if t == "said_tag":
        return f'{a.get("tag")}'
    return json.dumps({k: v for k, v in a.items() if k not in ("rule_id", "confidence")})[:120]


def render_comparison_table(metrics_list: list[dict]) -> str:
    """Cross-chapter comparison of key metrics."""
    if len(metrics_list) < 2:
        return ""
    rows = []
    chapters = [m.get("chapter_slug", "?") for m in metrics_list]
    header_cells = "".join(f"<th>{_esc(c)}</th>" for c in chapters)
    # Pick the most discriminating metrics
    metric_keys = [
        "anaphora", "self_referential_frame", "bigram_chain_loop",
        "trigram_chain_loop", "lexical_chain_loop", "motif_overuse",
        "statement_then_reversal", "anadiplosis", "filter_word",
        "abstract_noun", "passive_voice", "expletive_construction",
        "conjunctive_adverb", "modal_verb", "adverb_ly", "temporal_marker",
    ]
    for key in metric_keys:
        cells = []
        for m in metrics_list:
            by_dev = {met["device"]: met for met in m.get("metrics", [])}
            if key in by_dev:
                n = by_dev[key]["raw_count"]
                held = by_dev[key].get("held_count", 0)
                per_1k = by_dev[key].get("count_per_1k_tokens", 0)
                cells.append(f'<td class="num">{n}<small> ({per_1k:.1f}/1k)</small>{(" <span class=held>+" + str(held) + "h</span>") if held else ""}</td>')
            else:
                cells.append('<td class="num">-</td>')
        rows.append(f"<tr><th class='rowhead'>{_esc(key)}</th>{''.join(cells)}</tr>")
    # Aggregate metric rows
    rows.append("<tr><td colspan='99'><hr></td></tr>")
    rows.append("<tr><th class='rowhead'>verdict</th>" +
                "".join(f'<td class="num"><span class="verdict-pill" style="background:{VERDICT_COLORS.get(m.get("rollup",{}).get("verdict","gray"),"#9ca3af")};">{m.get("rollup",{}).get("verdict","?")}</span></td>' for m in metrics_list) + "</tr>")
    rows.append("<tr><th class='rowhead'>words</th>" +
                "".join(f'<td class="num">{m.get("document_metrics",{}).get("word_count",0):,}</td>' for m in metrics_list) + "</tr>")
    rows.append("<tr><th class='rowhead'>TTR</th>" +
                "".join(f'<td class="num">{m.get("lexical_diversity",{}).get("ttr",0):.3f}</td>' for m in metrics_list) + "</tr>")
    rows.append("<tr><th class='rowhead'>MATTR-1000</th>" +
                "".join(f'<td class="num">{m.get("lexical_diversity",{}).get("mattr_1000",0):.3f}</td>' for m in metrics_list) + "</tr>")
    rows.append("<tr><th class='rowhead'>starter-entropy</th>" +
                "".join(f'<td class="num">{m.get("sentence_starter_diversity",{}).get("entropy",0):.2f}</td>' for m in metrics_list) + "</tr>")
    return f"""
    <section class="comparison">
      <h2>Cross-chapter comparison</h2>
      <table>
        <thead><tr><th></th>{header_cells}</tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    </section>
    """


CSS = """
:root {
  --bg: #0f172a; --bg2: #1e293b; --fg: #e2e8f0; --muted: #94a3b8;
  --accent: #38bdf8; --border: #334155;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--fg); margin: 0; padding: 2rem; line-height: 1.5; }
h1, h2, h3 { color: var(--fg); margin: 0 0 0.5rem; }
h1 { font-size: 1.8rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; margin-bottom: 1.5rem; }
.card {
  background: var(--bg2); border-radius: 8px; padding: 1.5rem;
  margin-bottom: 1.5rem; border: 1px solid var(--border);
}
.card header {
  display: flex; align-items: center; justify-content: space-between;
  padding-left: 1rem; margin-bottom: 1rem;
}
.card header h2 { margin: 0; font-size: 1.3rem; }
.verdict {
  display: inline-block; padding: 0.3rem 0.8rem; border-radius: 4px;
  color: #000; font-weight: 600; font-size: 0.85rem;
}
.docmetrics, .aggregate {
  display: flex; gap: 1.5rem; flex-wrap: wrap;
  margin-bottom: 0.75rem; color: var(--muted); font-size: 0.9rem;
}
.aggregate b { color: var(--accent); }
.aggregate small { color: var(--muted); }
.held-count { color: #fbbf24; }
ul.blockers, ul.warnings { list-style: none; padding: 0.5rem 1rem; border-radius: 4px; }
ul.blockers { background: rgba(239, 68, 68, 0.1); border-left: 3px solid #ef4444; }
ul.warnings { background: rgba(251, 191, 36, 0.05); border-left: 3px solid #fbbf24; }
li.blocker, li.warning { font-family: ui-monospace, monospace; font-size: 0.85rem; padding: 0.15rem 0; }
li.blocker { color: #fca5a5; }
li.warning { color: #fcd34d; }
.metrics { margin-top: 1rem; }
.metrics table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
.metrics th, .metrics td { padding: 0.3rem 0.6rem; text-align: left; border-bottom: 1px solid var(--border); }
.metrics th { color: var(--muted); font-weight: normal; }
.num { text-align: right; font-variant-numeric: tabular-nums; }
.held { color: #fbbf24; font-size: 0.75rem; }
.findings { margin-top: 1rem; }
.findings details { margin: 0.4rem 0; }
.findings summary {
  cursor: pointer; padding: 0.3rem 0.5rem; background: rgba(56, 189, 248, 0.05);
  border-left: 2px solid var(--accent); border-radius: 2px;
  font-family: ui-monospace, monospace; font-size: 0.85rem;
}
.findings summary .count { color: var(--muted); }
.findings ul { list-style: none; padding-left: 1.5rem; margin: 0.5rem 0; }
.findings li { font-family: ui-monospace, monospace; font-size: 0.8rem;
               padding: 0.1rem 0; color: var(--muted); }
.findings li.more { font-style: italic; }
.comparison { background: var(--bg2); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
.comparison table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.comparison th, .comparison td { padding: 0.4rem 0.8rem; border-bottom: 1px solid var(--border); }
.comparison th { color: var(--muted); font-weight: normal; }
.comparison .rowhead { text-align: left; font-family: ui-monospace, monospace; }
.verdict-pill { padding: 0.15rem 0.5rem; border-radius: 3px; color: #000; font-size: 0.8rem; font-weight: 600; }
hr { border: none; border-top: 1px solid var(--border); margin: 0.5rem 0; }
footer { color: var(--muted); font-size: 0.8rem; margin-top: 2rem; text-align: center; }
"""


def render_dashboard(metrics_list: list[dict], title: str = "Prose Telemetry Dashboard") -> str:
    cards = "".join(render_chapter_card(m) for m in metrics_list)
    comparison = render_comparison_table(metrics_list)
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><title>{_esc(title)}</title>
<style>{CSS}</style>
</head><body>
<h1>{_esc(title)}</h1>
{comparison}
{cards}
<footer>Generated by prose_telemetry_dashboard.py from {len(metrics_list)} chapter metric file(s).</footer>
</body></html>
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--glob", default=None,
                    help="Glob pattern to find metric files (e.g. 'galley/**/*.prose-metrics.json')")
    ap.add_argument("--out", type=Path, default=None,
                    help="Output HTML path (default: galley/build/<book>/output/qa/dashboard.html)")
    ap.add_argument("--title", default="Prose Telemetry Dashboard")
    args = ap.parse_args()

    files: list[Path] = list(args.files)
    if args.glob:
        files.extend(Path(p) for p in glob.glob(args.glob, recursive=True))
    if not files:
        default_glob = "/Users/christopherwood/Projects/SunfishSoftware/galley/build/the-inverted-stack/output/qa/*.prose-metrics.json"
        files = [Path(p) for p in glob.glob(default_glob)]
    if not files:
        sys.exit("No metric files provided or found. Pass paths or --glob.")

    metrics_list = []
    for fp in sorted(files):
        try:
            metrics_list.append(json.loads(fp.read_text(encoding="utf-8")))
        except Exception as e:
            print(f"skipping {fp}: {e}")

    if not metrics_list:
        sys.exit("No valid metric files loaded.")

    html_str = render_dashboard(metrics_list, title=args.title)

    if args.out is None:
        out = Path("/Users/christopherwood/Projects/SunfishSoftware/galley/build/the-inverted-stack/output/qa/dashboard.html")
    else:
        out = args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_str, encoding="utf-8")
    print(f"Dashboard: {out}")
    print(f"  Chapters rendered: {len(metrics_list)}")


if __name__ == "__main__":
    main()
