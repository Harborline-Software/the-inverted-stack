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

# ─── Echo-and-confirm detector ────────────────────────────────────────────
# Pattern: generic conditional rule ("if you X") followed by a short
# personal-pronoun sentence (≤6 words) that echoes a key content word from
# the rule. CO ear-flagged this 2026-05-13: "if you let it. I had let it."
# is the textbook case.

# Rule markers — tightened to avoid "if you like / if you happen to / if you
# need to" parenthetical permissions which are NOT generic rules.
_RULE_MARKERS = re.compile(
    r"\b(if you (?!like|happen|wish|prefer|please|will|are\s+going|need|want)"
    r"|when you (?!are|were)"
    r"|you do not|you don't|if one(?!\s+of)"
    r"|the kind of (?:thing|person|man|woman|decision|note|feeling) that)\b",
    re.IGNORECASE,
)
_CONFIRM_OPENERS = {"i", "we", "my", "she", "he"}
_ECHO_STOPWORDS = {
    "have", "been", "this", "that", "with", "from", "they", "them",
    "their", "which", "would", "could", "should", "about", "there",
}


def _content_words(text: str, min_len: int = 4) -> set[str]:
    """Lowercase content words at least min_len chars, excluding common
    stopwords. Used for echo-detection lemma-ish matching."""
    return {
        w.lower()
        for w in re.findall(r"[A-Za-z][A-Za-z'-]{%d,}" % (min_len - 1), text)
        if w.lower() not in _ECHO_STOPWORDS
    }


def detect_echo_and_confirm(sents: list[str]) -> list[dict]:
    """Generic rule + short personal confirmation echoing a verb from the
    rule. Heuristic: pair of consecutive sentences where the first contains
    a rule marker (if you / when you / one) and the second is ≤6 words,
    starts with a personal pronoun, and shares a content word ≥4 letters."""
    findings = []
    for i in range(len(sents) - 1):
        rule_s = sents[i]
        confirm_s = sents[i + 1].strip()
        if not _RULE_MARKERS.search(rule_s):
            continue
        confirm_words = tokens(confirm_s)
        if not (2 <= len(confirm_words) <= 6):
            continue
        if confirm_words[0].lower() not in _CONFIRM_OPENERS:
            continue
        rule_content = _content_words(rule_s)
        confirm_content = _content_words(confirm_s, min_len=3)
        # Allow loose lemma match: strip trailing -ed, -ing, -s, -es
        def stem(w: str) -> str:
            for suffix in ("ing", "ed", "es", "s"):
                if w.endswith(suffix) and len(w) > len(suffix) + 2:
                    return w[: -len(suffix)]
            return w
        rule_stems = {stem(w) for w in rule_content}
        confirm_stems = {stem(w) for w in confirm_content}
        shared = rule_stems & confirm_stems
        if shared:
            findings.append({
                "type": "echo_and_confirm",
                "rule_sentence": rule_s,
                "confirm_sentence": confirm_s,
                "shared_stems": sorted(shared),
                "confidence": 0.7,
                "rule_id": "handcount:echo_and_confirm.rule_then_personal",
            })
    return findings


# ─── Lexical-chain loop detector ─────────────────────────────────────────
# Pattern: same content word repeated 3+ times within a single paragraph.
# CO ear-flagged 2026-05-13: "the feeling was correct… The feeling was correct…
# the feeling was also useless… the smallest possible feeling… the smallest
# possible feeling" — "feeling" five times in one paragraph.
#
# Filters out proper nouns (capitalized in source) and common stopwords.

_LEXICAL_STOPWORDS = {
    # Articles, pronouns, common verbs
    "would", "could", "should", "where", "there", "their", "which",
    "about", "after", "again", "those", "these", "while", "until",
    "before", "since", "every", "other", "another", "first", "second",
    "third", "thought", "myself", "herself", "himself", "themselves",
    "yourself", "without", "between", "through", "during", "against",
    "because", "always", "never", "still", "right", "wrong", "going",
    "really", "anything", "something", "nothing", "everything", "anyone",
    "someone", "everyone", "course", "kind", "thing", "things",
    # Anna-voice high-frequency function words that are register, not loop
    "consortium", "architecture", "mission",
}


def detect_lexical_chain(prose: str) -> list[dict]:
    """Per-paragraph: lowercase content words (≥5 letters) that appear with
    density exceeding the topic-word baseline. Density-based threshold to
    suppress topic-word false positives: a long paragraph about pastry will
    say 'kuchen' four times functionally; that's not a loop. A 100-word
    paragraph saying 'feeling' four times IS a loop.

    Threshold: count >= max(3, paragraph_word_count / 75). So:
       paragraph 150 words: 3 occurrences = flag
       paragraph 300 words: 4 occurrences = flag
       paragraph 450 words: 6 occurrences = flag
    """
    from collections import Counter
    findings = []
    for para in prose.split("\n\n"):
        para = para.strip()
        if not para or len(para) < 80:
            continue
        para_word_count = len(re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", para))
        # Density-based threshold — looser for longer paragraphs.
        threshold = max(3, int(para_word_count / 75) + 1)
        # Match content words starting with lowercase letter (excludes most
        # proper nouns). Negative lookbehind avoids matching mid-word.
        words = re.findall(r"(?<![A-Za-z])([a-z][a-z]{4,})(?![A-Za-z'])", para)
        counts = Counter(w for w in words if w not in _LEXICAL_STOPWORDS)
        for word, n in counts.items():
            if n >= threshold:
                # Density signal: occurrences per 100 words of the paragraph.
                density = round(100 * n / max(para_word_count, 1), 1)
                findings.append({
                    "type": "lexical_chain_loop",
                    "word": word,
                    "count": n,
                    "paragraph_word_count": para_word_count,
                    "density_per_100": density,
                    "paragraph_excerpt": para[:140] + ("..." if len(para) > 140 else ""),
                    "confidence": 0.75,
                    "rule_id": "handcount:lexical_chain.density_above_threshold",
                })
    return findings


# ─── Self-referential frame detector ─────────────────────────────────────
# Pattern: staff-history meta-frame phrases. Per ANNA-VOICE.md anti-pattern
# #6, capped at one occurrence per chapter.

_FRAME_PATTERNS = re.compile(
    r"\b(I am writing this here|I am going to write|I am going to tell you|"
    r"in this account|the staff history|for the record|on the record|"
    r"in retrospect|this version of the account|I am leaving (?:it|the reading) in)\b",
    re.IGNORECASE,
)


def detect_self_referential_frame(prose: str) -> list[dict]:
    """Staff-history meta-frame phrases. Counts every occurrence; verdict
    raises warning at >1 per chapter, blocker at >3."""
    findings = []
    for m in _FRAME_PATTERNS.finditer(prose):
        findings.append({
            "type": "self_referential_frame",
            "phrase": m.group(0).lower(),
            "start_char": m.start(),
            "end_char": m.end(),
            "confidence": 1.0,
            "rule_id": "handcount:self_referential_frame.staff_history_meta",
        })
    return findings


# ─── Bigram chain loop ───────────────────────────────────────────────────
# Pattern: two-word phrases repeating within a paragraph. Catches what the
# single-word lexical_chain detector misses — e.g. "the staff history" as
# a unit, "smallest possible feeling" — when the individual words don't
# trip the threshold but the phrase does.

_STOPWORD_BIGRAMS = {
    ("in", "the"), ("of", "the"), ("to", "the"), ("on", "the"),
    ("at", "the"), ("for", "the"), ("with", "the"), ("from", "the"),
    ("by", "the"), ("as", "the"), ("and", "the"), ("and", "i"),
    ("i", "had"), ("i", "have"), ("i", "was"), ("i", "am"),
    ("she", "had"), ("he", "had"), ("it", "was"), ("there", "was"),
    ("there", "were"), ("would", "have"), ("had", "been"),
    ("did", "not"), ("had", "not"), ("would", "not"), ("could", "have"),
    ("which", "was"), ("which", "is"), ("that", "i"), ("when", "i"),
    ("when", "the"), ("if", "i"), ("if", "you"), ("but", "i"),
    ("but", "the"), ("on", "a"), ("of", "a"), ("to", "a"), ("at", "a"),
    ("i", "did"), ("i", "do"), ("i", "would"), ("i", "could"),
    ("i", "knew"), ("i", "know"), ("i", "said"),
}


def detect_bigram_chain(prose: str, min_repeats: int = 3) -> list[dict]:
    """Per-paragraph: bigrams that appear min_repeats or more times.
    Excludes function-word bigrams. Two-word repetition is one of the most
    audibly noticeable forms of looping ('the staff history' said seven
    times in one chapter loops to a listener even when the individual
    words 'staff' and 'history' don't independently feel repeated)."""
    from collections import Counter
    findings = []
    for para in prose.split("\n\n"):
        para = para.strip()
        if not para or len(para) < 100:
            continue
        # Tokenize and find bigrams, case-folded.
        words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]*", para)]
        bigrams = list(zip(words, words[1:]))
        counts = Counter(bg for bg in bigrams if bg not in _STOPWORD_BIGRAMS)
        for bg, n in counts.items():
            if n >= min_repeats:
                findings.append({
                    "type": "bigram_chain_loop",
                    "bigram": " ".join(bg),
                    "count": n,
                    "paragraph_word_count": len(words),
                    "paragraph_excerpt": para[:140] + ("..." if len(para) > 140 else ""),
                    "confidence": 0.75,
                    "rule_id": "handcount:bigram_chain.phrase_repeat_in_paragraph",
                })
    return findings


# ─── Motif phrase tracker ────────────────────────────────────────────────
# Author-configurable list of phrases that should appear at most once per
# chapter. Per ANNA-VOICE.md anti-pattern #5; retired motifs flagged
# regardless of count to prevent regression.

# Phrases with hard cap of 1 per chapter (any more = warning).
# "what it claimed to be" is RETIRED — any occurrence = blocker.
RETIRED_MOTIFS = [
    "what it claimed to be",
    "what they claimed to be",
    "what he claimed to be",
    "what she claimed to be",
]

# Phrases capped per ANNA-VOICE.md (1 per chapter; 2 = warning; 3+ = blocker).
CAPPED_MOTIFS = [
    "noted and did not yet",
    "I am writing this here",
    "I am going to tell you",
    "I am going to write",
    "in this account",
    "the smallest possible",
    "this version of the account",
    "I am leaving it in",
]


def detect_motif_overuse(prose: str) -> list[dict]:
    """Catches (a) retired motif phrases that should not appear at all,
    and (b) capped motif phrases that appear more than once per chapter."""
    findings = []
    for phrase in RETIRED_MOTIFS:
        pat = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        matches = list(pat.finditer(prose))
        if matches:
            findings.append({
                "type": "motif_overuse",
                "phrase": phrase,
                "count": len(matches),
                "status": "retired",
                "cap": 0,
                "char_positions": [m.start() for m in matches],
                "confidence": 1.0,
                "rule_id": "handcount:motif_overuse.retired_phrase",
            })
    for phrase in CAPPED_MOTIFS:
        pat = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        matches = list(pat.finditer(prose))
        if len(matches) > 1:
            findings.append({
                "type": "motif_overuse",
                "phrase": phrase,
                "count": len(matches),
                "status": "capped",
                "cap": 1,
                "char_positions": [m.start() for m in matches],
                "confidence": 1.0,
                "rule_id": "handcount:motif_overuse.capped_phrase",
            })
    return findings


# ─── Parenthetical density ───────────────────────────────────────────────
# Anna's voice uses em-dashes and parentheticals heavily by design
# (Bobiverse-register move). This detector surfaces paragraphs where
# the density crosses into excess — useful as informational signal rather
# than a hard rule.

def detect_parenthetical_density(prose: str) -> list[dict]:
    """Per-paragraph density of em-dash appositions and parentheses.
    Flags paragraphs where appositions/sentence ratio > 0.5."""
    findings = []
    for para in prose.split("\n\n"):
        para = para.strip()
        if not para or len(para) < 100:
            continue
        em_dashes = len(re.findall(r"\s—\s", para))
        parens = para.count("(")
        appositions = em_dashes // 2 + parens
        sents = sentences(para)
        if not sents:
            continue
        ratio = appositions / len(sents)
        if ratio > 0.5 and appositions >= 3:
            findings.append({
                "type": "parenthetical_density",
                "em_dashes": em_dashes,
                "parens": parens,
                "appositions_estimate": appositions,
                "sentence_count": len(sents),
                "ratio": round(ratio, 2),
                "paragraph_excerpt": para[:140] + ("..." if len(para) > 140 else ""),
                "confidence": 0.6,
                "rule_id": "handcount:parenthetical_density.appositions_per_sentence",
            })
    return findings


# ─── Fragment density ────────────────────────────────────────────────────
# Three or more consecutive short sentences (<5 words). Deliberate fragments
# are fine (Bobiverse uses them); a chain of them suggests breathlessness
# or over-emphasis.

def detect_fragment_density(sents: list[str], min_chain: int = 3) -> list[dict]:
    """Consecutive runs of short sentences (≤4 words) of length min_chain
    or more. Flags fragment cascades like 'Not a thought. A feeling.'
    when they run too long."""
    findings = []
    i = 0
    while i < len(sents):
        run = 0
        while i + run < len(sents) and len(tokens(sents[i + run])) <= 4:
            run += 1
        if run >= min_chain:
            findings.append({
                "type": "fragment_density",
                "run_length": run,
                "sentences": sents[i:i + run],
                "confidence": 0.7,
                "rule_id": "handcount:fragment_density.consecutive_short_sentences",
            })
            i += run
        else:
            i += 1
    return findings


# ─── Statement-then-reversal ─────────────────────────────────────────────
# Per ANNA-VOICE.md anti-pattern #3: a sentence followed immediately by
# one that pivots or negates it via "but", "yet", "from him", etc.
# Janeway dramatic-monologue move.

_REVERSAL_MARKERS = re.compile(
    r"^\s*(but|yet|though|however|from him|from her|in his|in her|"
    r"the same|that is|the difference)\b",
    re.IGNORECASE,
)


def detect_statement_then_reversal(sents: list[str]) -> list[dict]:
    """Consecutive sentence pair where the second starts with a reversal
    marker pivoting the first. Surfaces statement-then-reversal closures."""
    findings = []
    for i in range(len(sents) - 1):
        first = sents[i]
        second = sents[i + 1].strip()
        m = _REVERSAL_MARKERS.match(second)
        if not m:
            continue
        # First must be substantive (not a fragment).
        if len(tokens(first)) < 6:
            continue
        findings.append({
            "type": "statement_then_reversal",
            "first": first,
            "second": second,
            "reversal_marker": m.group(1).lower(),
            "confidence": 0.65,
            "rule_id": "handcount:statement_then_reversal.consecutive_pivot",
        })
    return findings


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
    # CO ear-flagged 2026-05-13 patterns:
    "echo_and_confirm_max_per_chapter": 0,        # any instance = warning; ≥2 = blocker
    "lexical_chain_max_per_chapter": 0,           # any 3+ repeat = warning; 4+ in one paragraph = blocker
    "self_referential_frame_max_per_chapter": 1,  # 1 OK; 2 = warning; 3+ = blocker
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

    # CO ear-flagged 2026-05-13 detector verdicts
    if "echo_and_confirm" in by_dev:
        n = by_dev["echo_and_confirm"]["raw_count"]
        if n >= 2:
            blockers.append(f"echo_and_confirm: {n} instances exceeds blocker threshold of 1")
        elif n >= 1:
            warnings.append(f"echo_and_confirm: {n} instance found (target: 0)")
        else:
            passes.append("echo_and_confirm")
    # Lexical chain: severity by per-paragraph density, not raw count.
    # Many hits are topic-word false positives (a paragraph about pastry will
    # say "kuchen" 4 times functionally). Real loops show as high-density
    # repetition in tighter paragraphs.
    if "lexical_chain_loop" in by_dev:
        # Inspect individual chain findings to find the worst density.
        # Without access to the raw findings list here, fall back to a
        # softer rule: many hits = warning, very many = blocker.
        n = by_dev["lexical_chain_loop"]["raw_count"]
        if n >= 20:
            blockers.append(f"lexical_chain_loop: {n} candidates flagged (likely real looping; investigate top-density hits)")
        elif n >= 8:
            warnings.append(f"lexical_chain_loop: {n} candidates flagged (review top-density hits; many may be topic words)")
        elif n >= 1:
            warnings.append(f"lexical_chain_loop: {n} candidate(s) flagged (review for true positives)")
        else:
            passes.append("lexical_chain_loop")
    if "self_referential_frame" in by_dev:
        n = by_dev["self_referential_frame"]["raw_count"]
        limit = thresholds["self_referential_frame_max_per_chapter"]
        if n > limit * 2:
            blockers.append(f"self_referential_frame: {n} occurrences exceeds blocker threshold of {limit * 2}")
        elif n > limit:
            warnings.append(f"self_referential_frame: {n} occurrences exceeds threshold of {limit}")
        else:
            passes.append("self_referential_frame")

    # Bigram chain loop — phrase-level repetition.
    if "bigram_chain_loop" in by_dev:
        n = by_dev["bigram_chain_loop"]["raw_count"]
        if n >= 5:
            blockers.append(f"bigram_chain_loop: {n} bigrams repeating 3+ times in a paragraph (likely real looping)")
        elif n >= 1:
            warnings.append(f"bigram_chain_loop: {n} bigram(s) flagged (review for true positives)")
        else:
            passes.append("bigram_chain_loop")
    # Motif overuse — retired phrases or capped phrases over threshold.
    if "motif_overuse" in by_dev:
        n = by_dev["motif_overuse"]["raw_count"]
        if n >= 1:
            # Retired-phrase hits are blockers; capped-phrase overuse is warning.
            # The raw_count conflates both; treat any hit as warning by default,
            # leave it to dashboard to upgrade retired-phrase hits to blocker.
            warnings.append(f"motif_overuse: {n} motif phrase(s) over their cap (see findings)")
        else:
            passes.append("motif_overuse")
    # Parenthetical density — informational, not blocker.
    if "parenthetical_density" in by_dev:
        n = by_dev["parenthetical_density"]["raw_count"]
        if n >= 5:
            warnings.append(f"parenthetical_density: {n} paragraphs with high apposition density")
        elif n >= 1:
            passes.append("parenthetical_density")  # informational; not flagged
        else:
            passes.append("parenthetical_density")
    # Fragment density.
    if "fragment_density" in by_dev:
        n = by_dev["fragment_density"]["raw_count"]
        if n >= 3:
            warnings.append(f"fragment_density: {n} fragment-cascade runs detected")
        elif n >= 1:
            passes.append("fragment_density")  # one cascade is intentional, fine
        else:
            passes.append("fragment_density")
    # Statement-then-reversal — anti-pattern #3.
    if "statement_then_reversal" in by_dev:
        n = by_dev["statement_then_reversal"]["raw_count"]
        if n >= 3:
            blockers.append(f"statement_then_reversal: {n} consecutive-pivot pairs (anti-pattern #3)")
        elif n >= 1:
            warnings.append(f"statement_then_reversal: {n} pair(s) flagged")
        else:
            passes.append("statement_then_reversal")

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
        "echo_and_confirm": detect_echo_and_confirm(sents),
        "lexical_chain_loop": detect_lexical_chain(prose),
        "self_referential_frame": detect_self_referential_frame(prose),
        # New 2026-05-13 (later in same session):
        "bigram_chain_loop": detect_bigram_chain(prose),
        "motif_overuse": detect_motif_overuse(prose),
        "parenthetical_density": detect_parenthetical_density(prose),
        "fragment_density": detect_fragment_density(sents),
        "statement_then_reversal": detect_statement_then_reversal(sents),
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
