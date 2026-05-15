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

# anaphora detector retired — migrated to galley/prose registry
# (detectors/classical_rhetoric/anaphora.py). Phase 8 batch 1.


# tautological_self_equation detector retired — migrated to galley/prose
# registry under detectors/pivot_inference/tautology.py. Phase 8 batch 3.


# asyndeton / polysyndeton / literal_tricolon detectors retired —
# migrated to galley/prose registry under
# detectors/classical_rhetoric/. Phase 8 batch 1.


# epanorthosis + echo_and_confirm detectors retired — migrated to
# galley/prose registry under detectors/repetition/. Phase 8 batch 2a.


# lexical_chain_loop detector retired — migrated to galley/prose
# registry under detectors/chain/lexical_chain.py. Generic English
# stopwords are detector defaults; Anna's high-frequency register words
# (consortium, architecture, mission) live in book.editorial.yaml
# under detectors.lexical_chain_loop.stopwords. Phase 8 batch 2b.


# self_referential_frame detector retired — migrated to galley/prose
# registry. Phrase list lives in book.editorial.yaml under
# `detectors.self_referential_frame.self_referential_frames`. Thresholds
# in the same yaml are consumed by galley/prose's verdict.rollup_registry.


# bigram_chain_loop detector retired — migrated to galley/prose
# registry under detectors/chain/bigram_chain.py. Phase 8 batch 2b.


# ─── Motif phrase tracker ────────────────────────────────────────────────
# Author-configurable list of phrases that should appear at most once per
# chapter. Per ANNA-VOICE.md anti-pattern #5; retired motifs flagged
# regardless of count to prevent regression.

# motif_overuse detector retired — migrated to galley/prose registry.
# Retired-motif blacklist + capped-motif cap-dict live in
# book.editorial.yaml under `detectors.motif_overuse`. The registry
# version emits one finding per over-cap occurrence (rather than the
# legacy one-per-phrase) so the verdict layer can count crossings.


# ─── Parenthetical density ───────────────────────────────────────────────
# Anna's voice uses em-dashes and parentheticals heavily by design
# (Bobiverse-register move). This detector surfaces paragraphs where
# the density crosses into excess — useful as informational signal rather
# than a hard rule.

# parenthetical_density + fragment_density retired — migrated to galley/prose
# registry under detectors/density_style/. Phase 8 batch 4.


# ─── Statement-then-reversal ─────────────────────────────────────────────
# Per ANNA-VOICE.md anti-pattern #3: a sentence followed immediately by
# one that pivots or negates it via "but", "yet", "from him", etc.
# Janeway dramatic-monologue move.

# statement_then_reversal detector retired — migrated to galley/prose
# registry under detectors/pivot_inference/. Phase 8 batch 3.


# ─── Filter-word density ─────────────────────────────────────────────────
# "I felt," "I saw," "I noticed," "I realized" — narrator filter verbs that
# distance the reader from the sensory experience. Bob narrates directly;
# Anna currently filters. Reducing filter words is one of the highest-yield
# moves toward immediacy.

# filter_words detector retired — migrated to galley/prose registry.
# Verb list lives in book.editorial.yaml under
# `detectors.filter_words.filter_words`. Threshold + verdict handled
# by galley/prose's verdict.rollup_registry against the same yaml.


# ─── Redundant-phrase detector ───────────────────────────────────────────
# Stock filler phrases that mark amateur or academic prose. High-precision
# exact-match detection.

# redundant_phrase retired — migrated to galley/prose registry under
# detectors/density_style/redundant_phrases.py. Phase 8 batch 4.


# ─── Internal anaphora ───────────────────────────────────────────────────
# Within-sentence same-word echoes: "which was X, which was Y, which was Z."
# Different from sentence-level anaphora (already detected) — this is
# clause-level repetition inside one sentence.

# _INTERNAL_ANAPHORA_FUNCTION_STARTS retired with detector — Phase 8 batch 2a.


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

# confirmation_tag detector retired — migrated to galley/prose registry
# under detectors/pivot_inference/confirmation_tag.py. Phase 8 batch 3.


# ─── Inference cascade (which meant / which was / which gave ...) ──────
# Three-or-more clauses opening with the same "which <verb>" connector
# inside a single sentence. This is the Bobiverse cascading-inference
# move — intentional once, audibly looping at three. The single-word
# internal_anaphora detector excludes "which" as a function-word start
# (otherwise it would false-positive on inventories like "the bunk,
# the desk, the bookshelf"), so this dedicated bigram-cascade detector
# catches the specific looping pattern. CO ear-flagged 2026-05-13.

# inference_cascade detector retired — migrated to galley/prose registry
# under detectors/pivot_inference/inference_cascade.py. Phase 8 batch 3.


# detect_internal_anaphora + detect_anadiplosis retired — migrated
# to galley/prose registry under detectors/repetition/. Phase 8 batch 2a.


# ─── Modal-verb density ──────────────────────────────────────────────────
# would / could / should / might frequency. Hedging modals are a marker of
# narrator uncertainty; over-use makes prose tentative.

# modal_verb / vague_quantifier / abstract_noun / adverb_ly / said_tag /
# paragraph_length_anomaly detectors retired — migrated to galley/prose
# registry under detectors/density_style/. Phase 8 batch 4.


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

# trigram_chain_loop detector retired — migrated to galley/prose
# registry under detectors/chain/trigram_chain.py. Phase 8 batch 2b.


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


# cliche detector retired — migrated to galley/prose registry under
# detectors/density_style/cliche.py. Phase 8 batch 4.


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

# Local copy of the said-tags regex for attribution-variety stats.
# The said_tag detector itself was migrated to galley/prose in batch 4,
# but this function uses the same regex purely for per-chapter entropy
# stats and is unrelated to the detector's finding emission.
_ATTRIBUTION_TAGS = re.compile(
    r"\b(he|she|I|they|we)\s+(said|replied|asked|answered|told|added|stated|"
    r"declared|whispered|murmured|continued|repeated)\b",
    re.IGNORECASE,
)


def compute_attribution_variety(prose: str) -> dict:
    """Distribution of dialogue-attribution verbs."""
    import math
    from collections import Counter
    tags = list(_ATTRIBUTION_TAGS.finditer(prose))
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


# detect_epanorthosis retired — migrated to galley/prose registry
# under detectors/repetition/epanorthosis.py. Phase 8 batch 2a.


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
    # anaphora run-length branch retired with Phase 8 batch 1 migration.
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
        out.append(m)
    return out


# ─── Verdict / rollup ─────────────────────────────────────────────────────

DEFAULT_THRESHOLDS = {
    # anaphora / polysyndeton thresholds migrated to galley/prose
    # verdict.rollup_registry (Phase 8 batch 1).
    # tautology_density threshold migrated to galley/prose (Phase 8 batch 3).
    "sentences_over_50_words_pct": 3.0,
    # CO ear-flagged 2026-05-13 patterns:
    "echo_and_confirm_max_per_chapter": 0,        # any instance = warning; ≥2 = blocker
    "lexical_chain_max_per_chapter": 0,           # any 3+ repeat = warning; 4+ in one paragraph = blocker
    # self_referential_frame threshold migrated to book.editorial.yaml.
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

    # anaphora / polysyndeton / literal_tricolon / asyndeton verdict
    # blocks migrated to galley/prose registry. See book.editorial.yaml
    # detectors.<name>.{warning_raw_count,blocker_raw_count} if
    # per-chapter thresholds are desired.
    # tautological_self_equation rollup migrated to galley/prose
    # verdict.rollup_registry (Phase 8 batch 3).

    # echo_and_confirm rollup migrated to galley/prose registry
    # (verdict.rollup_registry consumes book.editorial.yaml thresholds).
    # Phase 8 batch 2a.
    # lexical_chain_loop / bigram_chain_loop rollups migrated to
    # galley/prose verdict.rollup_registry (Phase 8 batch 2b).
    # self_referential_frame migrated to registry: see book.editorial.yaml
    # `detectors.self_referential_frame`. Galley/prose's registry detector
    # fires under family='voice', and `verdict.rollup_registry` classifies
    # against `warning_raw_count` / `blocker_raw_count` in that yaml.
    # motif_overuse migrated to registry: see book.editorial.yaml
    # `detectors.motif_overuse` (retired_motifs + motifs cap dict). The
    # registry version emits one finding per over-cap occurrence rather
    # than one per phrase, so verdict thresholds in the yaml reflect
    # per-occurrence counting.

    # parenthetical_density / fragment_density rollups migrated to
    # galley/prose verdict.rollup_registry (Phase 8 batch 4).
    # statement_then_reversal rollup migrated to galley/prose
    # verdict.rollup_registry (Phase 8 batch 3).

    # ─── Phase 1.7 detector verdicts ────────────────────────────────────
    word_count = doc.get("word_count", 0) or 1

    # filter_words migrated to registry: see book.editorial.yaml
    # `detectors.filter_words.filter_words` (verb list). The registry
    # detector + galley/prose verdict layer handle the >8/1k threshold.

    # redundant_phrase / modal_verb / vague_quantifier / abstract_noun /
    # adverb_ly / said_tag / paragraph_length_anomaly rollups migrated to
    # galley/prose verdict.rollup_registry (Phase 8 batch 4).
    # internal_anaphora / anadiplosis / epanorthosis rollups migrated
    # to galley/prose verdict.rollup_registry (Phase 8 batch 2a).

    # trigram_chain_loop rollup migrated to galley/prose
    # verdict.rollup_registry (Phase 8 batch 2b).
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
    # cliche rollup migrated to galley/prose verdict.rollup_registry (batch 4).
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
    # inference_cascade rollup migrated to galley/prose
    # verdict.rollup_registry (Phase 8 batch 3).
    if "proximity_echo" in by_dev:
        n = by_dev["proximity_echo"]["raw_count"]
        if n >= 30:
            blockers.append(f"proximity_echo: {n} close-range word repetitions (likely real looping)")
        elif n >= 10:
            warnings.append(f"proximity_echo: {n} close-range word repetitions (review top hits)")
        else:
            passes.append("proximity_echo")
    # confirmation_tag rollup migrated to galley/prose
    # verdict.rollup_registry (Phase 8 batch 3).

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
        # anaphora / asyndeton / polysyndeton / literal_tricolon migrated
        # to registry (detectors/classical_rhetoric/). Phase 8 batch 1.
        # tautological_self_equation migrated to registry — batch 3.
        # epanorthosis / echo_and_confirm migrated to registry — batch 2a.
        # lexical_chain_loop migrated to registry — batch 2b.
        # self_referential_frame migrated to registry (book.editorial.yaml).
        # bigram_chain_loop migrated to registry — batch 2b.
        # motif_overuse migrated to registry (book.editorial.yaml).
        # parenthetical_density / fragment_density migrated to registry — batch 4.
        # statement_then_reversal migrated to registry — batch 3.
        # filter_word migrated to registry (book.editorial.yaml).
        # redundant_phrase migrated to registry — batch 4.
        # internal_anaphora / anadiplosis migrated to registry — batch 2a.
        # modal_verb / vague_quantifier / abstract_noun / adverb_ly /
        # said_tag / paragraph_length_anomaly migrated to registry — batch 4.
        # Phase 1.8 (final round):
        # trigram_chain_loop migrated to registry — batch 2b.
        "passive_voice": detect_passive_voice(prose),
        "expletive_construction": detect_expletive_constructions(sents),
        "conjunction_start": detect_conjunction_starts(sents),
        "conjunctive_adverb": detect_conjunctive_adverbs(prose),
        "double_negative": detect_double_negatives(prose),
        "comma_splice": detect_comma_splices(prose),
        # cliche migrated to registry — batch 4.
        "direct_address": detect_direct_address(prose),
        "timestamp": detect_timestamps(prose),
        "temporal_marker": detect_temporal_markers(prose),
        "paragraph_opener_repeat": detect_paragraph_opener_repeats(prose),
        "proper_noun": detect_proper_nouns(prose),
        "infinitive_phrase": detect_infinitives(prose),
        "gerund": detect_gerunds(prose),
        # inference_cascade migrated to registry — batch 3.
        "proximity_echo": detect_proximity_echo(sents),
        # confirmation_tag migrated to registry — batch 3.
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
