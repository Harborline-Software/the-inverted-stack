"""Export prose-telemetry detector rules as Vale-compatible YAML.

Vale (https://vale.sh) is a config-driven prose linter that runs in VS Code,
Sublime, and on the command line. Our high-precision exact-match detectors
translate cleanly to Vale rules; this script generates a Vale style pack
under .vale/inverted-stack/ that Yeoman can use during drafting to catch
these patterns in-editor *before* render.

Vale's rule types we use:
  - existence: word/phrase appearing N+ times in a doc
  - occurrence: word/phrase occurring more than N times in a doc
  - substitution: suggest a replacement
  - repetition: same word/phrase repeated in close succession

Per the architecture-doc Phase 2 brief: "Vale rules export for VS Code
in-editor highlighting in Yeoman's drafting workflow."

Usage:
    python build/prose_telemetry_vale_export.py
        # → writes .vale/styles/InvertedStack/*.yml
"""

from __future__ import annotations

import sys
from pathlib import Path

OUT_DIR = Path(".vale/styles/InvertedStack")


# ─── Retired motifs (any occurrence = error) ─────────────────────────────

RETIRED_MOTIFS = [
    "what it claimed to be",
    "what they claimed to be",
    "what he claimed to be",
    "what she claimed to be",
]


# ─── Capped motifs (more than 1 per chapter = warning) ───────────────────

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


# ─── Redundant phrases (cut on sight) ────────────────────────────────────

REDUNDANT_PHRASES = [
    "in order to", "the fact that", "for the first time",
    "needless to say", "it goes without saying", "at this point in time",
    "in the event that", "due to the fact that", "in spite of the fact that",
    "with regard to", "with respect to", "in terms of",
    "for all intents and purposes", "first and foremost", "last but not least",
    "each and every", "one and the same", "completely and utterly",
    "absolutely essential", "very unique", "totally complete",
    "end result", "past history", "future plans", "advance planning",
    "currently underway", "personal opinion",
]


# ─── Vague quantifiers (existence, warn) ─────────────────────────────────

VAGUE_QUANTIFIERS = [
    "very", "really", "quite", "rather", "somewhat", "fairly", "pretty",
    "just", "almost", "nearly", "basically", "essentially", "literally",
    "actually", "definitely", "certainly", "probably", "perhaps", "maybe",
]


# ─── Conjunctive adverbs (formal-register marker) ────────────────────────

CONJUNCTIVE_ADVERBS = [
    "however", "therefore", "moreover", "furthermore", "nevertheless",
    "nonetheless", "consequently", "accordingly", "hence", "thus",
    "indeed", "otherwise", "likewise", "similarly", "conversely",
]


# ─── Clichés (cut on sight) ──────────────────────────────────────────────

CLICHES = [
    "at the end of the day", "back to square one",
    "better safe than sorry", "burning the midnight oil",
    "calm before the storm", "cool as a cucumber",
    "easy as pie", "fish out of water",
    "hit the nail on the head", "in the nick of time",
    "needle in a haystack", "only time will tell",
    "out of the blue", "piece of cake", "raining cats and dogs",
    "read between the lines", "think outside the box",
    "tip of the iceberg", "two birds with one stone",
    "when push comes to shove", "with bated breath",
    "writing on the wall", "between a rock and a hard place",
    "easier said than done", "fall by the wayside",
]


def _yaml_rule(extends: str, message: str, level: str, tokens: list[str],
                ignorecase: bool = True, link: str = "") -> str:
    """Render a single Vale YAML rule."""
    lines = [
        f"extends: {extends}",
        f'message: "{message}"',
        f"level: {level}",
    ]
    if ignorecase:
        lines.append("ignorecase: true")
    if link:
        lines.append(f"link: {link}")
    lines.append("tokens:")
    for t in tokens:
        lines.append(f"  - {t!r}")
    return "\n".join(lines) + "\n"


def _yaml_substitution(message: str, level: str, swap: dict[str, str]) -> str:
    lines = [
        "extends: substitution",
        f'message: "{message}"',
        f"level: {level}",
        "ignorecase: true",
        "swap:",
    ]
    for k, v in swap.items():
        lines.append(f"  '{k}': '{v}'")
    return "\n".join(lines) + "\n"


def _yaml_occurrence(message: str, level: str, scope: str, max_n: int, token: str) -> str:
    return (
        "extends: occurrence\n"
        f'message: "{message}"\n'
        f"level: {level}\n"
        f"scope: {scope}\n"
        f"max: {max_n}\n"
        f"token: '{token}'\n"
    )


def write_pack(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    # Retired motifs — error level.
    (out_dir / "RetiredMotifs.yml").write_text(_yaml_rule(
        "existence",
        'Retired motif "%s" — do not use (voice-spec 2026-05-13).',
        "error",
        RETIRED_MOTIFS,
    ))

    # Capped motifs — suggestion level (Vale's occurrence rule).
    capped_text = ""
    for m in CAPPED_MOTIFS:
        capped_text += _yaml_occurrence(
            f'Motif "{m}" should appear at most once per chapter.',
            "warning",
            "raw",
            1,
            m,
        ) + "---\n"
    (out_dir / "CappedMotifs.yml").write_text(capped_text.rstrip("---\n").strip() + "\n")

    # Redundant phrases — cut.
    (out_dir / "RedundantPhrases.yml").write_text(_yaml_rule(
        "existence",
        'Redundant filler "%s" — cut.',
        "warning",
        REDUNDANT_PHRASES,
    ))

    # Vague quantifiers — review.
    (out_dir / "VagueQuantifiers.yml").write_text(_yaml_rule(
        "existence",
        'Weakening intensifier "%s" — review whether it strengthens or weakens the sentence.',
        "suggestion",
        VAGUE_QUANTIFIERS,
    ))

    # Conjunctive adverbs — academic register marker.
    (out_dir / "ConjunctiveAdverbs.yml").write_text(_yaml_rule(
        "existence",
        'Conjunctive adverb "%s" — academic register marker; consider cutting or rephrasing.',
        "suggestion",
        CONJUNCTIVE_ADVERBS,
    ))

    # Clichés.
    (out_dir / "Cliches.yml").write_text(_yaml_rule(
        "existence",
        'Cliché "%s" — cut.',
        "warning",
        CLICHES,
    ))

    # Expletive constructions (sentence start).
    (out_dir / "Expletives.yml").write_text(_yaml_rule(
        "existence",
        'Weak opener "%s" — consider rewriting to put the subject first.',
        "suggestion",
        [
            "(?i)^there is", "(?i)^there are", "(?i)^there was", "(?i)^there were",
            "(?i)^it is", "(?i)^it was",
        ],
    ))

    # Filter words.
    (out_dir / "FilterWords.yml").write_text(_yaml_rule(
        "existence",
        'Narrator filter verb "%s" — consider narrating directly without the filter.',
        "suggestion",
        [
            r"I felt", r"I saw", r"I noticed", r"I realized", r"I realised",
            r"I observed", r"I watched", r"I sensed", r"I thought",
            r"I wondered", r"I considered", r"I recognized", r"I recognised",
            r"I understood", r"I knew", r"I believed",
        ],
    ))

    # Style config — point Vale at this folder.
    config_yaml = """# Vale config for the-inverted-stack
# Generated by build/prose_telemetry_vale_export.py — do not edit by hand.

StylesPath = .vale/styles

MinAlertLevel = suggestion

# Apply to all markdown files in vol-1 and vol-2.
[*.md]
BasedOnStyles = InvertedStack
"""
    # .vale.ini lives at repo root, not inside .vale/.
    vale_ini = out_dir.parent.parent.parent / ".vale.ini"
    vale_ini.write_text(config_yaml)

    print(f"Vale style pack written to: {out_dir}")
    print(f"  Files: {len(list(out_dir.glob('*.yml')))}")
    print(f"Vale config at: {vale_ini}")
    print()
    print("To use in VS Code: install the Vale extension and the rules apply automatically.")
    print("To run from CLI: brew install vale; vale vol-2/act-1/ch01-departure.md")


def main() -> None:
    out_dir = OUT_DIR
    # Resolve relative to repo root.
    repo_root = Path("/Users/christopherwood/Projects/SunfishSoftware/the-inverted-stack")
    out_dir = repo_root / out_dir
    write_pack(out_dir)


if __name__ == "__main__":
    main()
