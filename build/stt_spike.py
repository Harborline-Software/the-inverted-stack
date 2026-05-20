"""STT QC spike - Phase 1 word-level diff between source markdown and Whisper transcript.

Usage:
    python3 build/stt_spike.py <chapter.mp3> <chapter.md>
    python3 build/stt_spike.py --model base build/output/audiobook/ch01-*.mp3 vol-1/.../ch01-*.md

Output:
    build/output/stt_spike/<chapter-stem>_diff.md  - word-level diff report
    build/output/stt_spike/<chapter-stem>_transcript.txt - raw Whisper output

The report leaves a blank CLASSIFICATION column for human review:
    REAL | VARIANT | NOISE | FOREIGN | STALE
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "build" / "output" / "stt_spike"

CONTEXT_WORDS = 10  # words of context around each diff region

# ── normalisation ─────────────────────────────────────────────────────────────

def _strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter block (--- ... ---)."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def _strip_code_fences(text: str) -> str:
    """Remove fenced code blocks (``` ... ```)."""
    return re.sub(r"```[\s\S]*?```", " ", text)


def _strip_inline_code(text: str) -> str:
    """Strip backticks but PRESERVE content as words.

    TTS reads code refs (`Sunfish.Kernel.Security`) and STT transcribes the
    spoken form ('sunfish kernel security'). If we removed the content
    entirely, the transcript words would appear as REAL insertions in the
    diff - that was the false-positive cluster Phase 1 surfaced (8 sites in
    ch15). Preserving content lets the downstream punctuation-strip
    normalization align 'Sunfish.Kernel.Security' source with 'sunfish
    kernel security' transcript (dots become whitespace; lowercase matches).
    """
    return re.sub(r"`([^`]+)`", r" \1 ", text)


def _strip_markdown(text: str) -> str:
    """Strip Markdown formatting markers."""
    # Links: [text](url) → text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Images: ![alt](url)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    # Bold/italic: **text**, *text*, __text__, _text_
    text = re.sub(r"\*{1,2}([^*]+)\*{1,2}", r"\1", text)
    text = re.sub(r"_{1,2}([^_]+)_{1,2}", r"\1", text)
    # ATX headings: # ## ### etc.
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Blockquotes
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
    # Horizontal rules
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
    # HTML comments
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    # HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    return text


def _strip_punctuation(text: str) -> str:
    """Strip punctuation but keep word boundaries and spaces."""
    # Keep apostrophes inside words (don't → dont)
    text = re.sub(r"(?<!\w)'(?!\w)", " ", text)
    text = re.sub(r"[.,;:!?\"'-–\-()[\]{}|/\\@#$%^&*+=<>~`]", " ", text)
    return text


def normalise(text: str) -> list[str]:
    """Full normalisation pipeline → list of lowercase words."""
    text = _strip_frontmatter(text)
    text = _strip_code_fences(text)
    text = _strip_inline_code(text)
    text = _strip_markdown(text)
    text = _strip_punctuation(text)
    text = text.lower()
    # Collapse whitespace + split
    return [w for w in text.split() if w]


# ── transcript ────────────────────────────────────────────────────────────────

def transcribe(mp3_path: Path, model_size: str) -> tuple[str, list[dict]]:
    """Run Whisper STT. Returns (full_text, segments)."""
    from faster_whisper import WhisperModel

    print(f"  Loading model {model_size!r} …", flush=True)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print(f"  Transcribing {mp3_path.name} ({mp3_path.stat().st_size // 1024 // 1024} MB) …",
          flush=True)
    t0 = time.time()
    segments_iter, info = model.transcribe(
        str(mp3_path),
        word_timestamps=True,
        language="en",
    )
    segments = []
    full_text_parts = []
    for seg in segments_iter:
        seg_dict = {
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip(),
            "avg_logprob": seg.avg_logprob,
        }
        segments.append(seg_dict)
        full_text_parts.append(seg.text)
    elapsed = time.time() - t0
    full_text = " ".join(full_text_parts)
    print(f"  Done in {elapsed:.0f}s  ({len(segments)} segments, "
          f"RTF={elapsed / info.duration:.2f})", flush=True)
    return full_text, segments


# ── diff ──────────────────────────────────────────────────────────────────────

def word_diff(src_words: list[str], tts_words: list[str]) -> list[dict]:
    """Compute word-level diff. Returns list of diff regions with context."""
    matcher = difflib.SequenceMatcher(None, src_words, tts_words, autojunk=False)
    regions = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        ctx_src_before = src_words[max(0, i1 - CONTEXT_WORDS):i1]
        ctx_src_after = src_words[i2:i2 + CONTEXT_WORDS]
        regions.append({
            "tag": tag,
            "src_removed": src_words[i1:i2],
            "tts_added": tts_words[j1:j2],
            "ctx_before": ctx_src_before,
            "ctx_after": ctx_src_after,
            "src_range": (i1, i2),
            "tts_range": (j1, j2),
        })
    return regions


# ── report ────────────────────────────────────────────────────────────────────

def write_report(
    out_path: Path,
    chapter_stem: str,
    mp3_path: Path,
    md_path: Path,
    model_size: str,
    src_words: list[str],
    tts_words: list[str],
    regions: list[dict],
    segments: list[dict],
    elapsed_s: float,
) -> None:
    lines = []
    lines.append(f"# STT Spike Report - {chapter_stem}")
    lines.append(f"")
    lines.append(f"| Field | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| MP3 | `{mp3_path.name}` ({mp3_path.stat().st_size // 1024 // 1024} MB) |")
    lines.append(f"| Source | `{md_path.relative_to(REPO).as_posix()}` |")
    lines.append(f"| Model | `whisper-{model_size}` (faster-whisper, CPU int8) |")
    lines.append(f"| Transcribe time | {elapsed_s:.0f}s |")
    lines.append(f"| Source words | {len(src_words):,} |")
    lines.append(f"| Transcript words | {len(tts_words):,} |")
    lines.append(f"| Diff regions | {len(regions)} |")
    lines.append(f"")
    lines.append(f"## Classification key")
    lines.append(f"")
    lines.append(f"- **REAL** - TTS dropped, duplicated, or audibly mispronounced")
    lines.append(f"- **VARIANT** - TTS correct, STT transcribed differently (e.g. proper noun phonetic rendering)")
    lines.append(f"- **NOISE** - Punctuation / formatting artifact that survived normalisation")
    lines.append(f"- **FOREIGN** - Non-English passage (Bangla, Spanish, Korean, etc.); low STT confidence expected")
    lines.append(f"- **STALE** - Cast-swap residue: old character name in audio that is now different in source")
    lines.append(f"")
    lines.append(f"## Diff regions")
    lines.append(f"")
    lines.append(f"| # | Context before | SOURCE removed | TTS added | Context after | CLASS |")
    lines.append(f"|---|---|---|---|---|---|")

    for n, r in enumerate(regions, 1):
        ctx_before = " ".join(r["ctx_before"][-5:])  # last 5 words of before-context
        ctx_after = " ".join(r["ctx_after"][:5])    # first 5 words of after-context
        src_rm = " ".join(r["src_removed"]) if r["src_removed"] else "-"
        tts_add = " ".join(r["tts_added"]) if r["tts_added"] else "-"
        # Escape pipe chars in content
        for s in (ctx_before, ctx_after, src_rm, tts_add):
            s = s.replace("|", "\\|")
        lines.append(
            f"| {n} | …{ctx_before} | ~~{src_rm}~~ | **{tts_add}** | {ctx_after}… | |"
        )

    lines.append(f"")
    lines.append(f"## Tally (fill in after classification)")
    lines.append(f"")
    lines.append(f"| Category | Count |")
    lines.append(f"|---|---|")
    lines.append(f"| REAL | |")
    lines.append(f"| VARIANT | |")
    lines.append(f"| NOISE | |")
    lines.append(f"| FOREIGN | |")
    lines.append(f"| STALE | |")
    lines.append(f"| **Total diff regions** | {len(regions)} |")
    lines.append(f"")
    lines.append(f"## Notes")
    lines.append(f"")
    lines.append(f"_(classifier notes go here)_")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("mp3", type=Path)
    ap.add_argument("md", type=Path)
    ap.add_argument("--model", default="large-v3",
                    help="Whisper model size (default: large-v3; fallback: medium, base)")
    args = ap.parse_args()

    mp3_path = args.mp3.resolve()
    md_path = args.md.resolve()

    if not mp3_path.exists():
        print(f"ERROR: MP3 not found: {mp3_path}", file=sys.stderr)
        sys.exit(2)
    if not md_path.exists():
        print(f"ERROR: Markdown not found: {md_path}", file=sys.stderr)
        sys.exit(2)

    chapter_stem = mp3_path.stem
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = OUT_DIR / f"{chapter_stem}_diff.md"
    transcript_path = OUT_DIR / f"{chapter_stem}_transcript.txt"

    print(f"\n=== STT spike: {chapter_stem} ===")

    # Transcribe
    t_total = time.time()
    full_text, segments = transcribe(mp3_path, args.model)
    elapsed_s = time.time() - t_total

    # Save raw transcript
    transcript_path.write_text(full_text, encoding="utf-8")
    print(f"  Transcript saved: {transcript_path.relative_to(REPO).as_posix()}")

    # Normalise both sides
    print(f"  Normalising source + transcript …")
    src_text = md_path.read_text(encoding="utf-8")
    src_words = normalise(src_text)
    tts_words = normalise(full_text)

    print(f"  Source words:     {len(src_words):,}")
    print(f"  Transcript words: {len(tts_words):,}")

    # Diff
    print(f"  Computing word-level diff …")
    regions = word_diff(src_words, tts_words)
    print(f"  Diff regions: {len(regions)}")

    # Report
    write_report(
        report_path, chapter_stem, mp3_path, md_path,
        args.model, src_words, tts_words, regions, segments, elapsed_s,
    )
    print(f"\nReport: {report_path.relative_to(REPO).as_posix()}")
    print(f"Total: {time.time() - t_total:.0f}s")


if __name__ == "__main__":
    main()
