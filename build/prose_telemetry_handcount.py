"""Hand-count prose-telemetry detectors against a single chapter markdown.

One-shot stdlib-only implementation of the v1 detector list from
.pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md, used to:

  1. Validate the prose-metrics.json schema against a real chapter.
  2. Produce a ground-truth fixture for the engineering session to validate
     Freestylo / StyloMetrix output against.
  3. Surface a first measurement of Anna's new (Filchner / Bobiverse register)
     trial chapter for comparison against the old Vol 2 baseline.

This is intentionally not the real platform — it's a calibration tool. Real
platform lives at galley/prose/lib/prose_telemetry/ (promoted from
galley/lib/ as of 2026-05-14, ADR-0005) and absorbs this script as the
stdlib tier in Phase 1. Anything this script flags should also flag in the
real platform; anything the real platform finds that this script misses is
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
    """Unicode-aware word tokenization. Handles 'Tomás', 'Wanjiru', 'café',
    and other diacritic-bearing words as single tokens. The earlier ASCII-only
    regex split 'Tomás' into 'Tom' + 's' which polluted the bigram detector;
    this version keeps it as one token."""
    return re.findall(r"[^\W\d_]+(?:[''’-][^\W\d_]+)*", text, re.UNICODE)


def _is_dialogue(s: str) -> bool:
    """A sentence sits inside dialogue if it begins or ends with a quote
    character. Used to exclude dialogue interiors from narrator-only
    detectors (statement-then-reversal, rhetorical questions, etc.)."""
    s = s.strip()
    if not s:
        return False
    return s[0] in ('"', '“', '”') or s[-1] in ('"', '“', '”')


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


def detect_bigram_chain(prose: str) -> list[dict]:
    """Per-paragraph: bigrams whose count exceeds a density-aware threshold.
    Catches phrase-level loops the single-word lexical detector misses
    (the 'the staff history' ×7 case). Uses Unicode tokenization to keep
    diacritic-bearing names ('Tomás', 'Wanjiru') as single tokens, and a
    density threshold to suppress topic-phrase false positives in long
    paragraphs."""
    from collections import Counter
    findings = []
    for para in prose.split("\n\n"):
        para = para.strip()
        if not para or len(para) < 100:
            continue
        words = [w.lower() for w in tokens(para)]
        # Density-aware threshold: longer paragraphs need more repeats to flag.
        threshold = max(3, int(len(words) / 100) + 2)
        bigrams = list(zip(words, words[1:]))
        counts = Counter(bg for bg in bigrams if bg not in _STOPWORD_BIGRAMS)
        for bg, n in counts.items():
            if n >= threshold:
                density = round(100 * n / max(len(words), 1), 1)
                findings.append({
                    "type": "bigram_chain_loop",
                    "bigram": " ".join(bg),
                    "count": n,
                    "paragraph_word_count": len(words),
                    "density_per_100": density,
                    "threshold_used": threshold,
                    "paragraph_excerpt": para[:140] + ("..." if len(para) > 140 else ""),
                    "confidence": 0.75,
                    "rule_id": "handcount:bigram_chain.density_above_threshold",
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
    marker pivoting the first. Skips dialogue interiors (sentences inside
    quotes) since Joel/Mikael dialogue often contains conversational pivots
    that aren't the narrator's anti-pattern #3 move."""
    findings = []
    for i in range(len(sents) - 1):
        first = sents[i]
        second = sents[i + 1].strip()
        # Skip if either sentence is dialogue.
        if _is_dialogue(first) or _is_dialogue(second):
            continue
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
            "confidence": 0.7,
            "rule_id": "handcount:statement_then_reversal.consecutive_pivot",
        })
    return findings


# ─── Filter-word density ─────────────────────────────────────────────────
# "I felt," "I saw," "I noticed," "I realized" — narrator filter verbs that
# distance the reader from the sensory experience. Bob narrates directly;
# Anna currently filters. Reducing filter words is one of the highest-yield
# moves toward immediacy.

_FILTER_VERBS = re.compile(
    r"\bI\s+(felt|saw|noticed|realized|realised|registered|"
    r"observed|watched|sensed|thought|wondered|considered|recognized|"
    r"recognised|understood|knew|believed|imagined|remembered|recalled|"
    r"experienced|perceived|decided|figured|determined)\b",
    re.IGNORECASE,
)


def detect_filter_words(prose: str) -> list[dict]:
    """Count narrator filter-verb constructions ('I felt X', 'I noticed X').
    These distance the reader from the sensory present. Heavy use is a
    Janeway / formal-narrator move; Bobiverse narrates direct."""
    findings = []
    for m in _FILTER_VERBS.finditer(prose):
        findings.append({
            "type": "filter_word",
            "verb": m.group(1).lower(),
            "match": m.group(0),
            "start_char": m.start(),
            "end_char": m.end(),
            "confidence": 1.0,
            "rule_id": "handcount:filter_word.narrator_distance_verb",
        })
    return findings


# ─── Redundant-phrase detector ───────────────────────────────────────────
# Stock filler phrases that mark amateur or academic prose. High-precision
# exact-match detection.

_REDUNDANT_PHRASES = [
    "in order to",
    "the fact that",
    "for the first time",
    "needless to say",
    "it goes without saying",
    "at this point in time",
    "in the event that",
    "due to the fact that",
    "in spite of the fact that",
    "with regard to",
    "with respect to",
    "in terms of",
    "for all intents and purposes",
    "first and foremost",
    "last but not least",
    "each and every",
    "one and the same",
    "completely and utterly",
    "absolutely essential",
    "very unique",
    "totally complete",
    "end result",
    "past history",
    "future plans",
    "advance planning",
    "currently underway",
    "personal opinion",
]


def detect_redundant_phrases(prose: str) -> list[dict]:
    """Stock filler phrases that should be cut. Strict exact-match."""
    findings = []
    for phrase in _REDUNDANT_PHRASES:
        pat = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        for m in pat.finditer(prose):
            findings.append({
                "type": "redundant_phrase",
                "phrase": phrase,
                "start_char": m.start(),
                "end_char": m.end(),
                "confidence": 1.0,
                "rule_id": "handcount:redundant_phrase.filler_match",
            })
    return findings


# ─── Internal anaphora ───────────────────────────────────────────────────
# Within-sentence same-word echoes: "which was X, which was Y, which was Z."
# Different from sentence-level anaphora (already detected) — this is
# clause-level repetition inside one sentence.

_INTERNAL_ANAPHORA_FUNCTION_STARTS = {
    "the", "a", "an", "this", "that", "these", "those", "which", "who", "whom",
    "and", "but", "or", "nor", "so", "yet", "for",
    "to", "of", "in", "on", "at", "by", "from", "with",
    "i", "he", "she", "it", "we", "they", "you",
    "is", "was", "are", "were", "be", "been",
    "his", "her", "their", "my", "your", "our",
}


# ─── Proximity echo (catch-all for close-range word repetition) ─────────
# Within a single sentence (or an adjacent-sentence pair), any content
# word appearing twice within ≤MAX_DISTANCE token positions. Catches the
# loop-family in one rule: anadiplosis ("nervous, and nervous"), within-
# sentence echo ("like X and like Y"), same-clause hammering ("the staff
# history begins... because the staff history..."), and proximity-tight
# anaphora that the sentence-level detector misses. CO ear-flagged
# 2026-05-13 (multiple instances).

_PROXIMITY_STOPWORDS = {
    # Function words / auxiliaries / common modifiers
    "have", "been", "this", "that", "with", "from", "they", "them",
    "their", "which", "would", "could", "should", "about", "there",
    "than", "then", "when", "what", "where", "while", "after", "before",
    "into", "over", "under", "only", "even", "much", "many", "some",
    "very", "just", "also", "always", "never", "still", "every",
    "because", "though", "since", "until", "however", "therefore",
    "other", "another", "same", "such", "those", "these", "where",
    # High-frequency content words that recur naturally in narrative
    "thing", "things", "kind", "part", "place", "time", "times",
    "matter", "people", "person", "year", "years", "minute", "minutes",
    "hour", "hours", "morning", "evening", "night", "today",
    "first", "second", "third", "last", "next", "three", "four", "five",
    "good", "well", "back", "down", "again", "around", "between",
    "took", "made", "gave", "kept", "knew", "said", "told", "went",
    "came", "saw", "got", "let", "put", "set", "had", "did", "was",
    "were", "wanted", "needed", "tried", "found", "left", "asked",
    "called", "began", "started", "stopped", "looked", "turned",
    # Common to-be / aux forms in -ing
    "going", "coming", "making", "saying", "doing", "looking", "thinking",
    "knowing", "having", "being", "trying", "telling", "asking",
    # Common adjectives that recur naturally
    "much", "more", "less", "most", "least", "many", "few",
}


def detect_proximity_echo(sents: list[str], max_distance: int = 12,
                          min_word_len: int = 5) -> list[dict]:
    """Content word appearing twice within max_distance token positions
    inside a SINGLE sentence. Anadiplosis detector already handles cross-
    sentence echoes; this detector handles same-sentence proximity that
    the within-sentence detectors miss.

    Tightened from initial cut: single-sentence only, min_word_len=5,
    max_distance=12, and expanded stopwords. Single-sentence content-word
    echo at ≤12 tokens is audibly noticeable; across-sentence echo is
    handled separately."""
    findings = []
    for sent in sents:
        toks = tokens(sent)
        seen: dict[str, int] = {}
        for pos, w in enumerate(toks):
            wl = w.lower()
            if len(wl) < min_word_len:
                continue
            if wl in _PROXIMITY_STOPWORDS:
                continue
            # Skip proper nouns: capitalized mid-sentence.
            if pos > 0 and w[0].isupper() and w[0].isalpha():
                continue
            if wl in seen:
                distance = pos - seen[wl]
                if distance <= max_distance:
                    findings.append({
                        "type": "proximity_echo",
                        "word": wl,
                        "distance_tokens": distance,
                        "sentence": sent[:200] + ("..." if len(sent) > 200 else ""),
                        "confidence": 0.75,
                        "rule_id": "handcount:proximity_echo.content_word_near_repeat_in_sentence",
                    })
            seen[wl] = pos
    return findings


# ─── Confirmation-tag detector ──────────────────────────────────────────
# Sentence-final tags like ", which she was." / ", which he did." /
# ", which I had." — Anna's staff-history confirmation move. Often
# redundant; the prose has already made the claim and the tag just
# re-verifies. CO ear-flagged 2026-05-13.

_CONFIRMATION_TAG_RE = re.compile(
    r",\s*which\s+(I|he|she|it|they|we|you)\s+"
    r"(was|were|is|are|did|do|had|have|has)"
    r"(?:\s+(?:not|n't))?"
    r"(?:\s+\w{2,7})?\s*\.",
    re.IGNORECASE,
)


def detect_confirmation_tag(prose: str) -> list[dict]:
    """Sentence-final ', which <pronoun> <aux>' confirmation tags."""
    findings = []
    for m in _CONFIRMATION_TAG_RE.finditer(prose):
        findings.append({
            "type": "confirmation_tag",
            "match": m.group(0).strip(),
            "pronoun": m.group(1).lower(),
            "auxiliary": m.group(2).lower(),
            "start_char": m.start(),
            "end_char": m.end(),
            "confidence": 0.9,
            "rule_id": "handcount:confirmation_tag.which_pronoun_aux_period",
        })
    return findings


# ─── Inference cascade (which meant / which was / which gave ...) ──────
# Three-or-more clauses opening with the same "which <verb>" connector
# inside a single sentence. This is the Bobiverse cascading-inference
# move — intentional once, audibly looping at three. The single-word
# internal_anaphora detector excludes "which" as a function-word start
# (otherwise it would false-positive on inventories like "the bunk,
# the desk, the bookshelf"), so this dedicated bigram-cascade detector
# catches the specific looping pattern. CO ear-flagged 2026-05-13.

_INFERENCE_CASCADE = re.compile(
    r"\bwhich\s+(meant|was|were|made|gave|put|left|brought|caused|forced|"
    r"allowed|kept|told|showed|sent|carried|placed|set|fixed|knew|did|"
    r"is|has|had|would)\b[^.!?]{1,120}?"
    r"\bwhich\s+\1\b[^.!?]{1,120}?"
    r"\bwhich\s+\1\b",
    re.IGNORECASE,
)


def detect_inference_cascade(prose: str) -> list[dict]:
    """Three-or-more 'which <same-verb>' clause openers in a single
    sentence. The signature Bobiverse cascading-inference move; intentional
    once, audibly looping at three. Detects '...which meant X, which meant
    Y, which meant Z' style chains."""
    findings = []
    for m in _INFERENCE_CASCADE.finditer(prose):
        findings.append({
            "type": "inference_cascade",
            "connector": f"which {m.group(1).lower()}",
            "match": m.group(0)[:200] + ("..." if len(m.group(0)) > 200 else ""),
            "start_char": m.start(),
            "end_char": m.end(),
            "confidence": 0.9,
            "rule_id": "handcount:inference_cascade.which_verb_triple",
        })
    return findings


def detect_internal_anaphora(sents: list[str], min_repeats: int = 3) -> list[dict]:
    """Same CONTENT word starting 3+ comma-or-em-dash-delimited clauses
    within a single sentence. Function-word starts (the, which, a, etc.)
    are intentional Bobiverse parallelism — 'the bunk, the desk, the
    bookshelf' is functional inventory, not looping; 'which meant X, which
    meant Y, which meant Z' is the deliberate cascading-inference move.
    Only flags when a substantive word (verb, noun, adverb) opens 3+
    clauses in a row."""
    findings = []
    for sent in sents:
        parts = re.split(r"\s*[,;—–]\s*", sent)
        if len(parts) < min_repeats:
            continue
        first_words = []
        for p in parts:
            ws = tokens(p)
            if ws:
                first_words.append(ws[0].lower())
        # Consecutive-run check on content words only.
        run = 1
        for i in range(1, len(first_words)):
            w = first_words[i]
            if (w == first_words[i - 1]
                    and len(w) >= 3
                    and w not in _INTERNAL_ANAPHORA_FUNCTION_STARTS):
                run += 1
                if run >= min_repeats:
                    findings.append({
                        "type": "internal_anaphora",
                        "word": w,
                        "run_length": run,
                        "sentence": sent,
                        "confidence": 0.85,
                        "rule_id": "handcount:internal_anaphora.content_word_clause_echo",
                    })
                    break
            else:
                run = 1
    return findings


# ─── Anadiplosis chain ───────────────────────────────────────────────────
# Last word of one clause/sentence is the first word of the next.
# "...the room. The room was empty." Classic Janeway dramatic move.

def detect_anadiplosis(sents: list[str]) -> list[dict]:
    """Detect anadiplosis: a sentence ends on a word that is also the
    first content word of the next sentence. Common in dramatic/Janeway
    prose; rare in Bobiverse."""
    findings = []
    for i in range(len(sents) - 1):
        a_words = tokens(sents[i])
        b_words = tokens(sents[i + 1])
        if len(a_words) < 4 or len(b_words) < 2:
            continue
        last_a = a_words[-1].lower()
        first_b = b_words[0].lower()
        # The first word of B might be a pronoun-skipping article.
        if first_b in {"the", "a", "an", "this", "that", "these", "those"} and len(b_words) >= 2:
            first_b = b_words[1].lower()
        if last_a == first_b and len(last_a) >= 4 and last_a not in _ECHO_STOPWORDS:
            findings.append({
                "type": "anadiplosis",
                "echo_word": last_a,
                "first_sentence": sents[i],
                "second_sentence": sents[i + 1],
                "confidence": 0.7,
                "rule_id": "handcount:anadiplosis.cross_sentence_echo",
            })
    return findings


# ─── Modal-verb density ──────────────────────────────────────────────────
# would / could / should / might frequency. Hedging modals are a marker of
# narrator uncertainty; over-use makes prose tentative.

_MODALS = re.compile(
    r"\b(would|could|should|might|may|must|shall|ought|will|won't|"
    r"wouldn't|couldn't|shouldn't|mightn't|mustn't|shan't)\b",
    re.IGNORECASE,
)


def detect_modal_density(prose: str, total_words: int) -> list[dict]:
    """Total modal-verb count. Reported as informational metric; the
    verdict checks density per 1k tokens (>40/1k = heavy hedging)."""
    findings = []
    for m in _MODALS.finditer(prose):
        findings.append({
            "type": "modal_verb",
            "modal": m.group(1).lower(),
            "start_char": m.start(),
            "confidence": 1.0,
            "rule_id": "handcount:modal_density.hedging_marker",
        })
    return findings


# ─── Vague-quantifier density ────────────────────────────────────────────
# "very," "really," "quite," "rather," "somewhat" — intensifiers that
# weaken rather than strengthen. Strunk-and-White perennial.

_VAGUE_QUANTIFIERS = re.compile(
    r"\b(very|really|quite|rather|somewhat|fairly|pretty|just|"
    r"almost|nearly|basically|essentially|literally|actually|"
    r"definitely|certainly|probably|perhaps|maybe)\b",
    re.IGNORECASE,
)


def detect_vague_quantifiers(prose: str) -> list[dict]:
    """Weakening intensifiers and hedge adverbs."""
    findings = []
    for m in _VAGUE_QUANTIFIERS.finditer(prose):
        findings.append({
            "type": "vague_quantifier",
            "word": m.group(1).lower(),
            "start_char": m.start(),
            "confidence": 0.85,
            "rule_id": "handcount:vague_quantifier.weakening_intensifier",
        })
    return findings


# ─── Abstract-noun density (-tion, -ness, -ity suffixes) ─────────────────
# Words ending in -tion, -ness, -ity, -ment, -ance are abstract nouns. Heavy
# use signals academic register. Bobiverse uses concrete nouns; Janeway
# leans abstract in command-monologue mode.

_ABSTRACT_SUFFIX = re.compile(
    r"\b[a-z]{3,}(?:tion|tions|ness|ity|ities|ment|ments|ance|ances|ence|ences)\b",
    re.IGNORECASE,
)


def detect_abstract_nouns(prose: str) -> list[dict]:
    """Words ending in abstract-noun suffixes. Informational metric."""
    findings = []
    for m in _ABSTRACT_SUFFIX.finditer(prose):
        word = m.group(0).lower()
        if word in {"three", "vacation", "destination", "stations"}:  # benign technicals
            continue
        findings.append({
            "type": "abstract_noun",
            "word": word,
            "start_char": m.start(),
            "confidence": 0.7,
            "rule_id": "handcount:abstract_noun.suffix_match",
        })
    return findings


# ─── Adverb density (-ly words) ──────────────────────────────────────────
# -ly adverbs are weak-writing markers in fiction. Anna's voice is
# adverb-light; an uptick would signal drift toward telling.

_ADVERB_LY = re.compile(r"\b[a-z]{4,}ly\b", re.IGNORECASE)
_ADVERB_EXCLUDE = {"only", "early", "really", "family", "ugly", "lovely", "lonely",
                   "deadly", "daily", "yearly", "weekly", "kindly", "friendly",
                   "lively", "monthly", "deadly", "homely", "july"}


def detect_adverbs(prose: str) -> list[dict]:
    """-ly adverbs. Excludes common false positives (only, family, etc.)."""
    findings = []
    for m in _ADVERB_LY.finditer(prose):
        word = m.group(0).lower()
        if word in _ADVERB_EXCLUDE:
            continue
        findings.append({
            "type": "adverb_ly",
            "word": word,
            "start_char": m.start(),
            "confidence": 0.85,
            "rule_id": "handcount:adverb.ly_suffix",
        })
    return findings


# ─── Dialogue-attribution overuse (he said / she said) ───────────────────
# Most dialogue should self-attribute via context. Over-use of "he said" /
# "she said" reads as amateur tagging.

_SAID_TAGS = re.compile(
    r"\b(he|she|I|they|we)\s+(said|replied|asked|answered|told|added|stated|"
    r"declared|whispered|murmured|continued|repeated)\b",
    re.IGNORECASE,
)


def detect_said_overuse(prose: str) -> list[dict]:
    """Dialogue attribution tags."""
    findings = []
    for m in _SAID_TAGS.finditer(prose):
        findings.append({
            "type": "said_tag",
            "tag": m.group(0).lower(),
            "verb": m.group(2).lower(),
            "start_char": m.start(),
            "confidence": 1.0,
            "rule_id": "handcount:said_tag.attribution_verb",
        })
    return findings


# ─── Paragraph-length anomaly ────────────────────────────────────────────
# A paragraph more than 4× the chapter mean is a wall of text; one less
# than 0.2× the mean is a fragment. Both are register signals.

def detect_paragraph_length_anomaly(prose: str) -> list[dict]:
    """Paragraphs whose length is anomalous against the chapter's mean."""
    findings = []
    paras = [p.strip() for p in prose.split("\n\n") if p.strip() and len(p.strip()) > 30]
    if len(paras) < 5:
        return findings
    lengths = [len(tokens(p)) for p in paras]
    mean_len = sum(lengths) / len(lengths)
    for i, (p, n) in enumerate(zip(paras, lengths)):
        if n > 4 * mean_len:
            findings.append({
                "type": "paragraph_length_anomaly",
                "kind": "oversized",
                "word_count": n,
                "chapter_mean": round(mean_len, 1),
                "ratio": round(n / mean_len, 1),
                "paragraph_excerpt": p[:120] + ("..." if len(p) > 120 else ""),
                "confidence": 0.6,
                "rule_id": "handcount:paragraph_length.over_4x_mean",
            })
        elif n < 0.2 * mean_len and n >= 5:
            findings.append({
                "type": "paragraph_length_anomaly",
                "kind": "undersized",
                "word_count": n,
                "chapter_mean": round(mean_len, 1),
                "ratio": round(n / mean_len, 2),
                "paragraph_excerpt": p,
                "confidence": 0.4,
                "rule_id": "handcount:paragraph_length.under_0.2x_mean",
            })
    return findings


# ═══════════════════════════════════════════════════════════════════════════
# Phase 1.8 — final round of stdlib detectors. Mostly density / variety
# metrics rather than pattern-matching, plus a few high-precision error
# detectors (comma splice, double negative, cliché).
# ═══════════════════════════════════════════════════════════════════════════


# ─── Trigram chain loop ──────────────────────────────────────────────────
# Three-word phrases repeating within a paragraph. The strongest signal for
# phrase-level looping ("the staff history" exactly, not just "staff" +
# "history" or "the staff" + "staff history"). High precision because
# three-word collisions are unlikely by chance in narrative prose.

_STOPWORD_TRIGRAMS = {
    ("one", "of", "the"), ("the", "rest", "of"), ("part", "of", "the"),
    ("in", "the", "way"), ("at", "the", "same"), ("for", "the", "first"),
    ("in", "the", "case"), ("by", "the", "way"), ("on", "the", "other"),
    ("the", "other", "hand"), ("in", "the", "end"), ("at", "the", "end"),
}


def detect_trigram_chain(prose: str, min_repeats: int = 3) -> list[dict]:
    """Per-paragraph: 3-grams that appear min_repeats or more times."""
    from collections import Counter
    findings = []
    for para in prose.split("\n\n"):
        para = para.strip()
        if not para or len(para) < 120:
            continue
        words = [w.lower() for w in tokens(para)]
        threshold = max(2, int(len(words) / 150) + 1)
        trigrams = list(zip(words, words[1:], words[2:]))
        counts = Counter(tg for tg in trigrams if tg not in _STOPWORD_TRIGRAMS)
        for tg, n in counts.items():
            if n >= max(threshold, min_repeats):
                findings.append({
                    "type": "trigram_chain_loop",
                    "trigram": " ".join(tg),
                    "count": n,
                    "paragraph_word_count": len(words),
                    "paragraph_excerpt": para[:140] + ("..." if len(para) > 140 else ""),
                    "confidence": 0.85,
                    "rule_id": "handcount:trigram_chain.phrase_repeat_in_paragraph",
                })
    return findings


# ─── Passive voice density ───────────────────────────────────────────────
# Heuristic: be-verb + past participle. Catches the standard passive
# constructions. False-positive prone on copulative adjectives, but useful
# as a density signal.

_BE_VERBS = (
    "is|was|were|are|been|being|am|be"
)
_PASSIVE_RE = re.compile(
    r"\b(" + _BE_VERBS + r")\s+"
    r"((?:[a-z]+ly\s+)?(?:[a-z]+ed|known|seen|made|done|been|gone|"
    r"taken|given|written|told|said|broken|frozen|chosen|driven|"
    r"thrown|found|held|kept|left|paid|set|cut|hit|put|shut|spread|"
    r"shown))\b",
    re.IGNORECASE,
)
# Common past participles that are usually adjectival (false-positive source).
_PASSIVE_FALSE_POSITIVES = {
    "is fine", "was fine", "is right", "was right", "is wrong",
    "was wrong", "is open", "was open", "is closed", "was closed",
}


def detect_passive_voice(prose: str) -> list[dict]:
    """Be-verb + past participle as passive heuristic. Density metric."""
    findings = []
    for m in _PASSIVE_RE.finditer(prose):
        snippet = m.group(0).lower()
        if any(fp in snippet for fp in _PASSIVE_FALSE_POSITIVES):
            continue
        findings.append({
            "type": "passive_voice",
            "match": m.group(0),
            "start_char": m.start(),
            "confidence": 0.55,
            "rule_id": "handcount:passive_voice.be_plus_past_participle",
        })
    return findings


# ─── Expletive constructions ─────────────────────────────────────────────
# "There is / There was / It is / It was" sentence starters. Weak openings
# that delay the actual subject. High-precision detector.

_EXPLETIVE_START = re.compile(
    r"^(There\s+(?:is|are|was|were|will\s+be|has\s+been|have\s+been)|"
    r"It\s+(?:is|was|will\s+be|has\s+been|seemed|seems|appeared|appears))\b",
    re.IGNORECASE,
)


def detect_expletive_constructions(sents: list[str]) -> list[dict]:
    """Sentences starting with expletive 'there'/'it' constructions."""
    findings = []
    for s in sents:
        if _is_dialogue(s):
            continue
        m = _EXPLETIVE_START.match(s.strip())
        if m:
            findings.append({
                "type": "expletive_construction",
                "opener": m.group(0).lower(),
                "sentence_start": s[:80],
                "confidence": 0.9,
                "rule_id": "handcount:expletive_construction.weak_opener",
            })
    return findings


# ─── Conjunction-start sentences (And / But / So density) ───────────────
# Sentences starting with And/But/So. Per modern usage these are fine in
# moderation but density signals casualness or list-rhythm.

_CONJUNCTION_START = re.compile(r"^(And|But|So|Or|Yet|Nor)\b")


def detect_conjunction_starts(sents: list[str]) -> list[dict]:
    """Sentences starting with And/But/So/Or/Yet/Nor."""
    findings = []
    for s in sents:
        if _is_dialogue(s):
            continue
        m = _CONJUNCTION_START.match(s.strip())
        if m:
            findings.append({
                "type": "conjunction_start",
                "conjunction": m.group(1),
                "sentence_start": s[:80],
                "confidence": 1.0,
                "rule_id": "handcount:conjunction_start.coordinating",
            })
    return findings


# ─── Conjunctive adverbs (academic register marker) ─────────────────────
# However, therefore, moreover, furthermore — formal academic register.
# Anna's voice should be light on these.

_CONJUNCTIVE_ADVERB = re.compile(
    r"\b(however|therefore|moreover|furthermore|nevertheless|nonetheless|"
    r"consequently|accordingly|hence|thus|indeed|otherwise|likewise|"
    r"similarly|conversely)\b",
    re.IGNORECASE,
)


def detect_conjunctive_adverbs(prose: str) -> list[dict]:
    """Formal conjunctive adverbs (academic register marker)."""
    findings = []
    for m in _CONJUNCTIVE_ADVERB.finditer(prose):
        findings.append({
            "type": "conjunctive_adverb",
            "word": m.group(1).lower(),
            "start_char": m.start(),
            "confidence": 1.0,
            "rule_id": "handcount:conjunctive_adverb.academic_register",
        })
    return findings


# ─── Double negative ─────────────────────────────────────────────────────
# "did not... no" / "could not... never" / "had not... nothing" — error or
# stylistic choice. Anna does this *deliberately* sometimes ("I did not
# tell him about it"); detect for visibility.

_DOUBLE_NEG_RE = re.compile(
    r"\b(?:not|n't)\b[^.!?]{1,40}\b(?:no|none|nothing|never|nobody|nowhere|neither)\b",
    re.IGNORECASE,
)


def detect_double_negatives(prose: str) -> list[dict]:
    """Double-negative patterns within close range."""
    findings = []
    for m in _DOUBLE_NEG_RE.finditer(prose):
        findings.append({
            "type": "double_negative",
            "match": m.group(0)[:80],
            "start_char": m.start(),
            "confidence": 0.7,
            "rule_id": "handcount:double_negative.proximity_match",
        })
    return findings


# ─── Comma splice (heuristic) ────────────────────────────────────────────
# Independent clause + comma + independent clause (no conjunction). Rough
# heuristic: comma followed by a personal pronoun + verb without an
# intervening conjunction.

_COMMA_SPLICE_RE = re.compile(
    r"[a-z],\s+(I|he|she|it|they|we|you)\s+(was|were|is|are|"
    r"had|have|did|do|went|came|said|knew|told|saw|felt|made|took|gave|got)\b",
)


def detect_comma_splices(prose: str) -> list[dict]:
    """Pronoun+verb after comma without conjunction (comma splice heuristic)."""
    findings = []
    for m in _COMMA_SPLICE_RE.finditer(prose):
        # Skip if surrounding context contains "and", "but", "or" within 30 chars
        # before the comma (compound predicate, not splice).
        context_start = max(0, m.start() - 50)
        context = prose[context_start:m.start() + 10].lower()
        if any(w in context for w in (" and ", " but ", " or ", " yet ", " for ", " so ")):
            continue
        findings.append({
            "type": "comma_splice",
            "match": m.group(0),
            "start_char": m.start(),
            "confidence": 0.5,
            "rule_id": "handcount:comma_splice.pronoun_after_comma",
        })
    return findings


# ─── Cliché detection ────────────────────────────────────────────────────
# List of common fiction clichés. Exact-match.

_CLICHES = [
    "at the end of the day", "all that glitters", "back to square one",
    "better safe than sorry", "burning the midnight oil", "by the skin of",
    "calm before the storm", "cat got your tongue", "cool as a cucumber",
    "cry over spilt milk", "dead as a doornail", "easy as pie",
    "every cloud has a silver lining", "fish out of water",
    "for what it's worth", "hit the nail on the head", "in the nick of time",
    "it's not rocket science", "needle in a haystack",
    "only time will tell", "out of the blue", "piece of cake",
    "raining cats and dogs", "read between the lines", "see the light",
    "the calm before", "the apple of his eye", "the apple of her eye",
    "think outside the box", "thinking outside the box", "tip of the iceberg",
    "tomorrow is another day", "two birds with one stone",
    "when push comes to shove", "with bated breath", "writing on the wall",
    "a stitch in time", "all in a day's work", "all walks of life",
    "as luck would have it", "avoid like the plague",
    "between a rock and a hard place", "beyond the pale",
    "blood is thicker than", "calm as a hindu cow", "diamond in the rough",
    "dyed in the wool", "easier said than done", "every fiber of my being",
    "fall by the wayside", "fall on deaf ears", "from the get-go",
    "gentle as a lamb", "grass is always greener", "in the same boat",
    "last but not least", "let the cat out of the bag", "lock, stock, and barrel",
    "lost in the shuffle", "make a long story short", "no pain, no gain",
    "off the beaten path", "on the wrong side of the bed",
    "play it by ear", "pull yourself up by your bootstraps",
    "put two and two together", "rolling in the dough",
    "sharp as a tack", "stick out like a sore thumb",
]


def detect_cliches(prose: str) -> list[dict]:
    """Exact-match common fiction clichés."""
    findings = []
    low = prose.lower()
    for phrase in _CLICHES:
        if phrase in low:
            for m in re.finditer(re.escape(phrase), low):
                findings.append({
                    "type": "cliche",
                    "phrase": phrase,
                    "start_char": m.start(),
                    "confidence": 1.0,
                    "rule_id": "handcount:cliche.exact_match",
                })
    return findings


# ─── Direct-address ("dear reader" etc.) ─────────────────────────────────
# Lines that directly address the reader. Anna's staff-history frame does
# this deliberately; detect for visibility.

_DIRECT_ADDRESS = re.compile(
    r"\b(dear reader|gentle reader|you must understand|"
    r"you may|you should know|you will see|let me|let us|trust me|"
    r"believe me|you can imagine|imagine|consider)\b",
    re.IGNORECASE,
)


def detect_direct_address(prose: str) -> list[dict]:
    """Narrator addressing the reader directly."""
    findings = []
    for m in _DIRECT_ADDRESS.finditer(prose):
        # Skip if inside dialogue (these are normal in dialogue).
        # Crude check: look back for unmatched quote.
        context_start = max(0, m.start() - 200)
        context = prose[context_start:m.start()]
        if context.count('"') % 2 == 1:
            continue
        findings.append({
            "type": "direct_address",
            "phrase": m.group(0).lower(),
            "start_char": m.start(),
            "confidence": 0.7,
            "rule_id": "handcount:direct_address.reader_addressed",
        })
    return findings


# ─── Time-stamp density ──────────────────────────────────────────────────
# Specific times (HH:MM, "at 09:14", "by 03:17"). Anna's voice has many.

_TIMESTAMP_RE = re.compile(r"\b\d{1,2}:\d{2}\b")


def detect_timestamps(prose: str) -> list[dict]:
    """HH:MM time stamps in narration."""
    findings = []
    for m in _TIMESTAMP_RE.finditer(prose):
        findings.append({
            "type": "timestamp",
            "time": m.group(0),
            "start_char": m.start(),
            "confidence": 1.0,
            "rule_id": "handcount:timestamp.hh_mm_match",
        })
    return findings


# ─── Temporal-marker overuse ─────────────────────────────────────────────
# "then", "now", "soon", "suddenly", "eventually" — narrative-time
# adverbs. Heavy use signals reliance on telling-not-showing transitions.

_TEMPORAL_MARKERS = re.compile(
    r"\b(then|now|soon|suddenly|eventually|finally|immediately|"
    r"presently|shortly|previously|currently|formerly|"
    r"earlier|later|afterwards|afterward|meanwhile)\b",
    re.IGNORECASE,
)


def detect_temporal_markers(prose: str) -> list[dict]:
    """Narrative-time adverbs."""
    findings = []
    for m in _TEMPORAL_MARKERS.finditer(prose):
        findings.append({
            "type": "temporal_marker",
            "marker": m.group(1).lower(),
            "start_char": m.start(),
            "confidence": 0.9,
            "rule_id": "handcount:temporal_marker.transition_adverb",
        })
    return findings


# ─── Lexical diversity (type-token ratio) ────────────────────────────────
# Unique words / total words. Higher = richer vocabulary. Single number
# per chapter; informational metric for register comparison.

def compute_lexical_diversity(prose: str) -> dict:
    """Type-token ratio for the chapter prose."""
    ws = [w.lower() for w in tokens(prose)]
    if not ws:
        return {"types": 0, "tokens": 0, "ttr": 0.0}
    types = len(set(ws))
    tokens_n = len(ws)
    return {
        "types": types,
        "tokens": tokens_n,
        "ttr": round(types / tokens_n, 4),
        # Moving-average TTR over 1000-token windows is more comparable
        # across chapter lengths than raw TTR; report both.
        "mattr_1000": _mattr(ws, window=1000),
    }


def _mattr(words: list[str], window: int = 1000) -> float:
    """Moving-Average Type-Token Ratio over fixed-size windows."""
    if len(words) <= window:
        return round(len(set(words)) / max(len(words), 1), 4)
    ratios = []
    for i in range(0, len(words) - window + 1, window // 2):
        chunk = words[i:i + window]
        ratios.append(len(set(chunk)) / len(chunk))
    return round(sum(ratios) / len(ratios), 4) if ratios else 0.0


# ─── Sentence-starter diversity (Shannon entropy) ────────────────────────
# Entropy of the distribution of sentence-starting words. Low entropy =
# Anna keeps starting sentences with the same words (looping signature);
# high entropy = varied openings (Bobiverse-style).

def compute_sentence_starter_entropy(sents: list[str]) -> dict:
    """Shannon entropy of sentence-starter word distribution."""
    import math
    from collections import Counter
    starters = []
    for s in sents:
        s = s.strip().lstrip('"').lstrip()
        ws = tokens(s)
        if ws:
            starters.append(ws[0].lower())
    if not starters:
        return {"unique_starters": 0, "total_sentences": 0, "entropy": 0.0, "top_starter_share": 0.0}
    counts = Counter(starters)
    total = sum(counts.values())
    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values() if c > 0)
    top_word, top_count = counts.most_common(1)[0]
    return {
        "unique_starters": len(counts),
        "total_sentences": total,
        "entropy": round(entropy, 3),
        "max_entropy": round(math.log2(len(counts)), 3) if len(counts) > 1 else 0.0,
        "top_starter": top_word,
        "top_starter_count": top_count,
        "top_starter_share": round(top_count / total, 3),
    }


# ─── Paragraph-opening diversity ─────────────────────────────────────────
# Same as sentence-starter but for paragraph openings. Smaller sample,
# louder signal — if 3+ paragraphs in a chapter start with the same word,
# it's noticeable to a reader.

def detect_paragraph_opener_repeats(prose: str, min_repeats: int = 3) -> list[dict]:
    """Words that open min_repeats or more paragraphs in the chapter."""
    from collections import Counter
    findings = []
    paras = [p.strip() for p in prose.split("\n\n") if p.strip()]
    openers = []
    for p in paras:
        if _is_dialogue(p):
            continue
        ws = tokens(p)
        if ws:
            openers.append(ws[0].lower())
    counts = Counter(openers)
    for word, n in counts.items():
        if n >= min_repeats and word not in {"the", "a", "an", "this", "that", "it", "he", "she", "they"}:
            findings.append({
                "type": "paragraph_opener_repeat",
                "word": word,
                "count": n,
                "total_paragraphs": len(openers),
                "confidence": 0.85,
                "rule_id": "handcount:paragraph_opener.repeat_above_threshold",
            })
    return findings


# ─── Dialogue-attribution variety (Shannon entropy) ──────────────────────
# Distribution of attribution verbs. "Said" should dominate; if other verbs
# (replied / answered / continued) are over-represented, attribution is
# self-conscious.

def compute_attribution_variety(prose: str) -> dict:
    """Distribution of dialogue-attribution verbs."""
    import math
    from collections import Counter
    tags = list(_SAID_TAGS.finditer(prose))
    if not tags:
        return {"total_attributions": 0, "unique_verbs": 0, "entropy": 0.0}
    verb_counts = Counter(m.group(2).lower() for m in tags)
    total = sum(verb_counts.values())
    entropy = -sum((c / total) * math.log2(c / total) for c in verb_counts.values() if c > 0)
    return {
        "total_attributions": total,
        "unique_verbs": len(verb_counts),
        "entropy": round(entropy, 3),
        "said_share": round(verb_counts.get("said", 0) / total, 3),
        "verb_distribution": dict(verb_counts.most_common(8)),
    }


# ─── Proper-noun density ─────────────────────────────────────────────────
# Capitalized-mid-sentence words. Heuristic for proper nouns. Used as a
# density metric and as input for named-entity tracking.

_PROPER_NOUN_RE = re.compile(r"(?<![.!?]\s)(?<!^)\b([A-Z][a-z]{2,})\b")


def detect_proper_nouns(prose: str) -> list[dict]:
    """Mid-sentence capitalized words as proper-noun heuristic. Density
    metric; useful for tracking name-heavy paragraphs."""
    findings = []
    for m in _PROPER_NOUN_RE.finditer(prose):
        word = m.group(1)
        # Skip common false positives (sentence-start words wrapped by
        # markdown italics).
        if word in {"The", "A", "An", "I", "It", "He", "She", "We", "They", "You", "But", "And", "So"}:
            continue
        findings.append({
            "type": "proper_noun",
            "word": word,
            "start_char": m.start(),
            "confidence": 0.7,
            "rule_id": "handcount:proper_noun.mid_sentence_capitalized",
        })
    return findings


# ─── Infinitive-phrase density ───────────────────────────────────────────
# "to be," "to have," "to know" — abstract / academic register marker.

_INFINITIVE_RE = re.compile(r"\bto\s+([a-z]{2,})\b", re.IGNORECASE)


def detect_infinitives(prose: str) -> list[dict]:
    """to-infinitive phrases. Density metric."""
    findings = []
    for m in _INFINITIVE_RE.finditer(prose):
        verb = m.group(1).lower()
        # Skip prepositional "to" patterns (to the / to him / to her)
        if verb in {"the", "him", "her", "them", "us", "me", "you", "it"}:
            continue
        findings.append({
            "type": "infinitive_phrase",
            "verb": verb,
            "start_char": m.start(),
            "confidence": 0.7,
            "rule_id": "handcount:infinitive_phrase.to_verb_pattern",
        })
    return findings


# ─── Gerund density (-ing nouns and participles) ─────────────────────────

_GERUND_RE = re.compile(r"\b([a-z]{3,}ing)\b", re.IGNORECASE)
_GERUND_EXCLUDE = {"during", "morning", "evening", "nothing", "anything", "everything",
                   "something", "feeling", "meeting", "writing", "reading",
                   "having", "being", "going", "coming", "looking", "thinking",
                   "wedding", "ceiling", "ring", "spring", "string", "thing",
                   "wing", "king", "bring", "sing"}


def detect_gerunds(prose: str) -> list[dict]:
    """-ing forms. Density metric."""
    findings = []
    for m in _GERUND_RE.finditer(prose):
        word = m.group(1).lower()
        if word in _GERUND_EXCLUDE:
            continue
        if word.endswith("thing"):
            continue
        findings.append({
            "type": "gerund",
            "word": word,
            "start_char": m.start(),
            "confidence": 0.6,
            "rule_id": "handcount:gerund.ing_suffix",
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
        # Exclude held annotations from verdict-relevant counts; report both.
        live = [a for a in anns if not a.get("held")]
        held = [a for a in anns if a.get("held")]
        m = {
            "device": dev,
            "raw_count": len(live),
            "held_count": len(held),
            "count_per_1k_tokens": per_1k(len(live), total_w),
            "sentence_coverage_pct": sentence_coverage(live, total_s, dev),
        }
        if dev == "anaphora" and live:
            m["max_run_length"] = max(a["run_length"] for a in live)
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

    # ─── Phase 1.7 detector verdicts ────────────────────────────────────
    word_count = doc.get("word_count", 0) or 1

    # Filter words — narrator-distance verbs. >20/1k = heavy filtering.
    if "filter_word" in by_dev:
        n = by_dev["filter_word"]["raw_count"]
        per_1k = n * 1000 / word_count
        if per_1k > 15:
            blockers.append(f"filter_word: {per_1k:.1f}/1k narrator-distance verbs (target <8/1k)")
        elif per_1k > 8:
            warnings.append(f"filter_word: {per_1k:.1f}/1k filter verbs (above 8/1k target)")
        else:
            passes.append("filter_word")

    # Redundant phrases — exact-match filler.
    if "redundant_phrase" in by_dev:
        n = by_dev["redundant_phrase"]["raw_count"]
        if n >= 3:
            blockers.append(f"redundant_phrase: {n} filler phrases (cut all)")
        elif n >= 1:
            warnings.append(f"redundant_phrase: {n} filler phrase(s) — cut")
        else:
            passes.append("redundant_phrase")

    # Internal anaphora — within-sentence clause-start echo.
    if "internal_anaphora" in by_dev:
        n = by_dev["internal_anaphora"]["raw_count"]
        if n >= 3:
            warnings.append(f"internal_anaphora: {n} within-sentence clause-start echoes")
        elif n >= 1:
            warnings.append(f"internal_anaphora: {n} clause-echo case(s) flagged")
        else:
            passes.append("internal_anaphora")

    # Anadiplosis — cross-sentence echo.
    if "anadiplosis" in by_dev:
        n = by_dev["anadiplosis"]["raw_count"]
        if n >= 2:
            warnings.append(f"anadiplosis: {n} cross-sentence echo pair(s)")
        elif n >= 1:
            warnings.append(f"anadiplosis: {n} pair flagged (review)")
        else:
            passes.append("anadiplosis")

    # Modal verbs — hedging density.
    if "modal_verb" in by_dev:
        n = by_dev["modal_verb"]["raw_count"]
        per_1k = n * 1000 / word_count
        if per_1k > 50:
            warnings.append(f"modal_verb: {per_1k:.1f}/1k modal/hedging verbs (heavy hedging)")
        else:
            passes.append("modal_verb")

    # Vague quantifiers.
    if "vague_quantifier" in by_dev:
        n = by_dev["vague_quantifier"]["raw_count"]
        per_1k = n * 1000 / word_count
        if per_1k > 10:
            warnings.append(f"vague_quantifier: {per_1k:.1f}/1k weakening intensifiers")
        else:
            passes.append("vague_quantifier")

    # Abstract nouns — academic register marker.
    if "abstract_noun" in by_dev:
        n = by_dev["abstract_noun"]["raw_count"]
        per_1k = n * 1000 / word_count
        if per_1k > 30:
            warnings.append(f"abstract_noun: {per_1k:.1f}/1k abstract-suffix words (academic register)")
        else:
            passes.append("abstract_noun")

    # -ly adverbs.
    if "adverb_ly" in by_dev:
        n = by_dev["adverb_ly"]["raw_count"]
        per_1k = n * 1000 / word_count
        if per_1k > 15:
            warnings.append(f"adverb_ly: {per_1k:.1f}/1k -ly adverbs (weak-writing marker)")
        else:
            passes.append("adverb_ly")

    # Said-tags — dialogue attribution density.
    if "said_tag" in by_dev:
        n = by_dev["said_tag"]["raw_count"]
        if n >= 30:
            warnings.append(f"said_tag: {n} dialogue-attribution tags (consider context-based attribution)")
        else:
            passes.append("said_tag")

    # Paragraph-length anomalies.
    if "paragraph_length_anomaly" in by_dev:
        n = by_dev["paragraph_length_anomaly"]["raw_count"]
        if n >= 4:
            warnings.append(f"paragraph_length_anomaly: {n} paragraphs with anomalous length (4x or <0.2x mean)")
        else:
            passes.append("paragraph_length_anomaly")

    # ─── Phase 1.8 detector verdicts ────────────────────────────────────
    if "trigram_chain_loop" in by_dev:
        n = by_dev["trigram_chain_loop"]["raw_count"]
        if n >= 3:
            blockers.append(f"trigram_chain_loop: {n} three-word phrases repeating (strong looping signal)")
        elif n >= 1:
            warnings.append(f"trigram_chain_loop: {n} trigram(s) flagged")
        else:
            passes.append("trigram_chain_loop")
    if "passive_voice" in by_dev:
        n = by_dev["passive_voice"]["raw_count"]
        per_1k_val = n * 1000 / word_count
        if per_1k_val > 15:
            warnings.append(f"passive_voice: {per_1k_val:.1f}/1k passive constructions")
        else:
            passes.append("passive_voice")
    if "expletive_construction" in by_dev:
        n = by_dev["expletive_construction"]["raw_count"]
        if n >= 8:
            warnings.append(f"expletive_construction: {n} weak openers (There is / It was)")
        else:
            passes.append("expletive_construction")
    if "conjunction_start" in by_dev:
        n = by_dev["conjunction_start"]["raw_count"]
        per_1k_val = n * 1000 / word_count
        if per_1k_val > 8:
            warnings.append(f"conjunction_start: {per_1k_val:.1f}/1k And/But/So sentence openers")
        else:
            passes.append("conjunction_start")
    if "conjunctive_adverb" in by_dev:
        n = by_dev["conjunctive_adverb"]["raw_count"]
        if n >= 5:
            warnings.append(f"conjunctive_adverb: {n} however/therefore/moreover (academic register)")
        else:
            passes.append("conjunctive_adverb")
    if "double_negative" in by_dev:
        n = by_dev["double_negative"]["raw_count"]
        if n >= 3:
            warnings.append(f"double_negative: {n} proximity-pair instances (review)")
        else:
            passes.append("double_negative")
    if "comma_splice" in by_dev:
        n = by_dev["comma_splice"]["raw_count"]
        if n >= 1:
            warnings.append(f"comma_splice: {n} suspected splice(s) (low-confidence; review)")
        else:
            passes.append("comma_splice")
    if "cliche" in by_dev:
        n = by_dev["cliche"]["raw_count"]
        if n >= 1:
            blockers.append(f"cliche: {n} stock fiction cliché(s) — cut")
        else:
            passes.append("cliche")
    if "direct_address" in by_dev:
        n = by_dev["direct_address"]["raw_count"]
        if n >= 10:
            warnings.append(f"direct_address: {n} reader-address phrases (heavy staff-history frame)")
        else:
            passes.append("direct_address")
    if "timestamp" in by_dev:
        n = by_dev["timestamp"]["raw_count"]
        # informational only
        if n >= 15:
            warnings.append(f"timestamp: {n} HH:MM stamps (verify intentional density)")
        else:
            passes.append("timestamp")
    if "temporal_marker" in by_dev:
        n = by_dev["temporal_marker"]["raw_count"]
        per_1k_val = n * 1000 / word_count
        if per_1k_val > 8:
            warnings.append(f"temporal_marker: {per_1k_val:.1f}/1k then/now/soon transitions")
        else:
            passes.append("temporal_marker")
    if "paragraph_opener_repeat" in by_dev:
        n = by_dev["paragraph_opener_repeat"]["raw_count"]
        if n >= 2:
            warnings.append(f"paragraph_opener_repeat: {n} word(s) opening 3+ paragraphs")
        else:
            passes.append("paragraph_opener_repeat")
    if "proper_noun" in by_dev:
        # Informational only — high count is name-heavy chapter, normal.
        passes.append("proper_noun")
    if "infinitive_phrase" in by_dev:
        n = by_dev["infinitive_phrase"]["raw_count"]
        per_1k_val = n * 1000 / word_count
        if per_1k_val > 30:
            warnings.append(f"infinitive_phrase: {per_1k_val:.1f}/1k 'to-verb' phrases (abstract register)")
        else:
            passes.append("infinitive_phrase")
    if "gerund" in by_dev:
        passes.append("gerund")  # informational
    if "inference_cascade" in by_dev:
        n = by_dev["inference_cascade"]["raw_count"]
        if n >= 1:
            blockers.append(f"inference_cascade: {n} 'which X' triple-cascade(s) — cut to two or fewer")
        else:
            passes.append("inference_cascade")
    if "proximity_echo" in by_dev:
        n = by_dev["proximity_echo"]["raw_count"]
        if n >= 30:
            blockers.append(f"proximity_echo: {n} close-range word repetitions (likely real looping)")
        elif n >= 10:
            warnings.append(f"proximity_echo: {n} close-range word repetitions (review top hits)")
        else:
            passes.append("proximity_echo")
    if "confirmation_tag" in by_dev:
        n = by_dev["confirmation_tag"]["raw_count"]
        if n >= 5:
            blockers.append(f"confirmation_tag: {n} 'which <pronoun> <aux>' tags — many likely redundant")
        elif n >= 2:
            warnings.append(f"confirmation_tag: {n} confirmation tag(s) — review each for redundancy")
        elif n >= 1:
            passes.append("confirmation_tag")  # 1 is acceptable
        else:
            passes.append("confirmation_tag")

    if blockers:
        v = "red"
    elif warnings:
        v = "yellow"
    else:
        v = "green"
    return {"verdict": v, "blockers": blockers, "warnings": warnings, "passes": passes}


# ─── Main ─────────────────────────────────────────────────────────────────

def _load_held_lines(md_path: Path) -> list[dict]:
    """Load author-approved held_lines exceptions for this chapter.
    Schema: a JSON file alongside the markdown with name <stem>.held-lines.json
    containing a list of {device, at: {start_char, end_char}, reason,
    approved_by, approved_at} entries. Findings whose char-range falls
    inside any held_lines entry get a 'held: true' flag and are excluded
    from verdict computation."""
    held_path = md_path.with_suffix(".held-lines.json")
    if not held_path.exists():
        return []
    try:
        data = json.loads(held_path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _apply_held_lines(findings: list[dict], held: list[dict]) -> tuple[list[dict], int]:
    """Annotate findings that fall inside any held_lines entry.
    Supports two match modes:
      1. char-range: hold entry has {at: {start_char, end_char}}, finding
         has start_char/end_char fields (most exact-match detectors).
      2. text-pattern: hold entry has {match: {text_contains: "..."}},
         finding has 'sentences' / 'paragraph_excerpt' / 'sentence' /
         'text' / 'match' fields. Finding is held if any of its text
         fields contains the pattern.
    Device matching: held entry's 'device' = '*' or matches finding type.
    """
    if not held:
        return findings, 0
    held_count = 0

    def _finding_text(f: dict) -> str:
        parts = []
        for k in ("sentences", "sentence", "paragraph_excerpt", "text", "match",
                  "first", "second", "first_sentence", "second_sentence",
                  "rule_sentence", "confirm_sentence"):
            v = f.get(k)
            if isinstance(v, list):
                parts.extend(str(x) for x in v)
            elif v:
                parts.append(str(v))
        return " ".join(parts)

    for f in findings:
        for h in held:
            device = h.get("device")
            if device not in (None, "*", f.get("type")):
                continue
            matched = False
            # Char-range match.
            at = h.get("at") or {}
            if "start_char" in at:
                f_start = f.get("start_char")
                f_end = f.get("end_char", f_start)
                h_start = at.get("start_char", -1)
                h_end = at.get("end_char", -1)
                if f_start is not None and h_start <= f_start and (f_end is None or f_end <= h_end):
                    matched = True
            # Text-pattern match (fallback or alternative).
            if not matched:
                pat = (h.get("match") or {}).get("text_contains")
                if pat and pat in _finding_text(f):
                    matched = True
            # Sentence-list match: hold entry can specify a sentence prefix
            # that should appear in finding's sentences[] / sentence field.
            if not matched:
                spfx = (h.get("match") or {}).get("sentence_starts_with")
                if spfx:
                    txt = _finding_text(f)
                    if spfx in txt:
                        matched = True
            if matched:
                f["held"] = True
                f["held_reason"] = h.get("reason", "")
                f["held_approved_by"] = h.get("approved_by", "")
                held_count += 1
                break
    return findings, held_count


def measure(md_path: Path, dimensions: dict | None = None) -> dict:
    raw = md_path.read_text(encoding="utf-8")
    prose = strip_to_prose(raw)
    sents = sentences(prose)
    doc = document_metrics(prose, sents)
    held_lines = _load_held_lines(md_path)

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
        "bigram_chain_loop": detect_bigram_chain(prose),
        "motif_overuse": detect_motif_overuse(prose),
        "parenthetical_density": detect_parenthetical_density(prose),
        "fragment_density": detect_fragment_density(sents),
        "statement_then_reversal": detect_statement_then_reversal(sents),
        "filter_word": detect_filter_words(prose),
        "redundant_phrase": detect_redundant_phrases(prose),
        "internal_anaphora": detect_internal_anaphora(sents),
        "anadiplosis": detect_anadiplosis(sents),
        "modal_verb": detect_modal_density(prose, doc.get("word_count", 0)),
        "vague_quantifier": detect_vague_quantifiers(prose),
        "abstract_noun": detect_abstract_nouns(prose),
        "adverb_ly": detect_adverbs(prose),
        "said_tag": detect_said_overuse(prose),
        "paragraph_length_anomaly": detect_paragraph_length_anomaly(prose),
        # Phase 1.8 (final round):
        "trigram_chain_loop": detect_trigram_chain(prose),
        "passive_voice": detect_passive_voice(prose),
        "expletive_construction": detect_expletive_constructions(sents),
        "conjunction_start": detect_conjunction_starts(sents),
        "conjunctive_adverb": detect_conjunctive_adverbs(prose),
        "double_negative": detect_double_negatives(prose),
        "comma_splice": detect_comma_splices(prose),
        "cliche": detect_cliches(prose),
        "direct_address": detect_direct_address(prose),
        "timestamp": detect_timestamps(prose),
        "temporal_marker": detect_temporal_markers(prose),
        "paragraph_opener_repeat": detect_paragraph_opener_repeats(prose),
        "proper_noun": detect_proper_nouns(prose),
        "infinitive_phrase": detect_infinitives(prose),
        "gerund": detect_gerunds(prose),
        "inference_cascade": detect_inference_cascade(prose),
        "proximity_echo": detect_proximity_echo(sents),
        "confirmation_tag": detect_confirmation_tag(prose),
    }

    # Apply held_lines annotations.
    total_held = 0
    for dev_type, anns in findings_by_type.items():
        anns, n_held = _apply_held_lines(anns, held_lines)
        findings_by_type[dev_type] = anns
        total_held += n_held

    all_findings = [a for anns in findings_by_type.values() for a in anns]
    metrics_list = meters(findings_by_type, doc)
    roll = verdict(metrics_list, doc, DEFAULT_THRESHOLDS)

    # Aggregate chapter-level metrics (single-number metrics that aren't
    # per-finding device counts). These slot alongside `document_metrics`
    # in the schema.
    lex = compute_lexical_diversity(prose)
    starter = compute_sentence_starter_entropy(sents)
    attribution = compute_attribution_variety(prose)

    return {
        "_schema_version": 3,
        "_schema_status": "handcount-phase-1.8 — 39 detectors + aggregate metrics + held_lines schema",
        "_schema_notes": "Real platform per .pao-inbox/_decisions/2026-05-08-prose-telemetry-platform.md. held_lines support: place {stem}.held-lines.json beside the source markdown.",
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
        "lexical_diversity": lex,
        "sentence_starter_diversity": starter,
        "attribution_variety": attribution,
        "held_lines_applied": len(held_lines),
        "held_findings_count": total_held,
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
