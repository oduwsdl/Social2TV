#!/usr/bin/env python3
"""Detect social media mentions in CNN caption rows and label columns.

Fills:
  - Social Media Mention: Yes / No
  - Social Media Platform: platform name(s), or "-" when No

Also recovers terms split across consecutive caption lines, including:
  - "SOCIAL" / "MEDIA"
  - "TIK" / "TOK"
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import List, Sequence, Set, Tuple

INPUT_CSV = Path(__file__).resolve().parent / "all_captions - CNN.csv"
OUTPUT_CSV = Path(__file__).resolve().parent / "all_captions - CNN.csv"

# Ordered (platform_label, compiled_pattern).
PLATFORM_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("Facebook", re.compile(r"\bFACEBOOK\b", re.IGNORECASE)),
    ("Instagram", re.compile(r"\bINSTAGRAM\b|\bINSTA\b", re.IGNORECASE)),
    (
        "Twitter (bird logo)",
        re.compile(
            r"\bTWITTER\b|\bTWEETS?\b|\bTWEETED\b|\bTWEETING\b",
            re.IGNORECASE,
        ),
    ),
    ("Threads", re.compile(r"\bTHREADS\b", re.IGNORECASE)),
    (
        "TikTok",
        re.compile(
            r"\b(?:"
            r"TIK[\s-]?TOK(?:ERS?)?|"
            r"TIK[\s-]?TOCK(?:ERS?)?|"
            r"TICK[\s-]?TOCK(?:ERS?)?"
            r")\b",
            re.IGNORECASE,
        ),
    ),
    (
        "Truth Social",
        re.compile(r"\bTRUTH[\s-]?SOCIAL\b", re.IGNORECASE),
    ),
    ("LinkedIn", re.compile(r"\bLINKEDIN\b", re.IGNORECASE)),
    ("Meta", re.compile(r"\bMETA\b", re.IGNORECASE)),
    ("Parler", re.compile(r"\bPARLER\b", re.IGNORECASE)),
    ("Pinterest", re.compile(r"\bPINTEREST\b", re.IGNORECASE)),
    ("Rumble", re.compile(r"\bRUMBLE\b", re.IGNORECASE)),
    (
        "Snapchat",
        re.compile(
            r"\bSNAP(?:[\s-]?CHAT)?\b",
            re.IGNORECASE,
        ),
    ),
    (
        "YouTube",
        re.compile(r"\bYOU[\s-]?TUBE\b", re.IGNORECASE),
    ),
    ("Discord", re.compile(r"\bDISCORD\b", re.IGNORECASE)),
    (
        "Social Media",
        re.compile(
            r"\bSOCIAL[\s-]?(?:"
            r"MEDIA(?:[\s-]+PLATFORMS?)?|"
            r"NETWORKS?|"
            r"PLATFORMS?"
            r")\b",
            re.IGNORECASE,
        ),
    ),
]

# "X" is ambiguous, so require social-media context or clear wording that
# identifies X as the platform.
X_PATTERN = re.compile(r"(?<![A-Za-z0-9])X(?![A-Za-z0-9])")

X_AS_PLATFORM = re.compile(
    r"\bON\s+X\b|"
    r"\bX\s+(?:APP|PLATFORM|ACCOUNT|POST|POSTS|WILL)\b|"
    r"\bPOSTED\s+(?:IT\s+)?TO\s+X\b|"
    r"\bTWITTER\s*,?\s+(?:NOW\s+)?X\b|"
    r"\bX\s*,?\s+FORMERLY\s+(?:KNOWN\s+AS\s+)?TWITTER\b|"
    r"\bFORMERLY\s+(?:KNOWN\s+AS\s+)?TWITTER\b|"
    r"\bAND\s+X\b|"
    r"\bTOP\s+X\b",
    re.IGNORECASE,
)

X_CONTEXT = re.compile(
    r"\b(?:"
    r"TWITTER|TWEETS?|TWEETED|TWEETING|"
    r"SOCIAL[\s-]?(?:MEDIA|NETWORKS?|PLATFORMS?)|"
    r"FACEBOOK|INSTAGRAM|THREADS|TIK[\s-]?TOK|"
    r"TRUTH[\s-]?SOCIAL|SNAP(?:[\s-]?CHAT)?|DISCORD|"
    r"META|PARLER|PINTEREST|RUMBLE|YOUTUBE|PLATFORM|ELON|MUSK"
    r")\b",
    re.IGNORECASE,
)

# Detect "SOCIAL" and "MEDIA" split across neighboring caption rows.
SOCIAL_END = re.compile(r"\bSOCIAL[\s-]*$", re.IGNORECASE)
MEDIA_START = re.compile(r"^[\s,.:;!?-]*MEDIA\b", re.IGNORECASE)
SOCIAL_START = re.compile(r"\bSOCIAL\b", re.IGNORECASE)
MEDIA_ONLY = re.compile(r"^[\s,.:;!?-]*MEDIA\b", re.IGNORECASE)

# Detect TikTok variants split across neighboring caption rows:
#   "... TIK"  /  "TOK ..."
#   "... TICK" /  "TOCK ..."
TIK_PART_END = re.compile(
    r"\b(?:TIK|TICK)[\s-]*$",
    re.IGNORECASE,
)

TOK_PART_START = re.compile(
    r"^[\s,.:;!?-]*(?:TOK|TOCK)(?:ERS?)?\b",
    re.IGNORECASE,
)

MENTION_COL = "Social Media Mention"
PLATFORM_COL = "Social Media Platform"

TWITTER_LABEL = "Twitter (bird logo)"
X_LABEL = "X (X logo)"


def _add(found: List[str], seen: Set[str], label: str) -> None:
    """Append a label only when it has not already been found."""
    if label not in seen:
        found.append(label)
        seen.add(label)


def _add_to_row(platforms_per_row: List[List[str]], row_index: int, label: str) -> None:
    """Add a unique label to one row."""
    existing = set(platforms_per_row[row_index])
    _add(platforms_per_row[row_index], existing, label)


def detect_platforms(caption: str) -> List[str]:
    """Return ordered, unique platform labels found in caption text."""
    if not caption or not caption.strip():
        return []

    found: List[str] = []
    seen: Set[str] = set()

    for label, pattern in PLATFORM_PATTERNS:
        if pattern.search(caption):
            _add(found, seen, label)

    if X_LABEL not in seen and X_PATTERN.search(caption):
        if X_AS_PLATFORM.search(caption) or X_CONTEXT.search(caption):
            if TWITTER_LABEL in seen:
                twitter_index = found.index(TWITTER_LABEL)
                found.insert(twitter_index + 1, X_LABEL)
                seen.add(X_LABEL)
            elif "Instagram" in seen:
                instagram_index = found.index("Instagram")
                found.insert(instagram_index + 1, X_LABEL)
                seen.add(X_LABEL)
            else:
                _add(found, seen, X_LABEL)

    return found


def label_rows(captions: Sequence[str]) -> List[Tuple[str, str]]:
    """Label captions and recover terms split across neighboring rows."""
    row_count = len(captions)

    platforms_per_row: List[List[str]] = [
        detect_platforms(caption) for caption in captions
    ]

    for i, caption in enumerate(captions):
        current_caption = caption.strip()
        previous_caption = captions[i - 1].strip() if i > 0 else ""
        next_caption = captions[i + 1].strip() if i + 1 < row_count else ""

        # Current row ends with SOCIAL and next row starts with MEDIA.
        if (
            i + 1 < row_count
            and SOCIAL_END.search(current_caption)
            and MEDIA_START.search(next_caption)
        ):
            _add_to_row(platforms_per_row, i, "Social Media")
            _add_to_row(platforms_per_row, i + 1, "Social Media")

        # Current row starts with MEDIA and previous row contains SOCIAL.
        if (
            i > 0
            and MEDIA_ONLY.search(current_caption)
            and SOCIAL_START.search(previous_caption)
            and not re.search(
                r"\bSOCIAL[\s-]?MEDIA\b",
                previous_caption,
                re.IGNORECASE,
            )
        ):
            _add_to_row(platforms_per_row, i - 1, "Social Media")
            _add_to_row(platforms_per_row, i, "Social Media")

        # Current row ends with TIK/TICK and next starts with TOK/TOCK.
        if (
            i + 1 < row_count
            and TIK_PART_END.search(current_caption)
            and TOK_PART_START.search(next_caption)
        ):
            _add_to_row(platforms_per_row, i, "TikTok")
            _add_to_row(platforms_per_row, i + 1, "TikTok")

    labels: List[Tuple[str, str]] = []

    for platforms in platforms_per_row:
        if platforms:
            labels.append(("Yes", ", ".join(platforms)))
        else:
            labels.append(("No", "-"))

    return labels


def main() -> None:
    """Read the CSV, label each caption row, and write the results."""
    with INPUT_CSV.open(newline="", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)

        fieldnames = [
            column
            for column in (reader.fieldnames or [])
            if column and column.strip()
        ]

        if MENTION_COL not in fieldnames:
            fieldnames.append(MENTION_COL)

        if PLATFORM_COL not in fieldnames:
            fieldnames.append(PLATFORM_COL)

        rows = list(reader)

    captions = [row.get("caption") or "" for row in rows]
    labels = label_rows(captions)

    yes_count = 0

    for row, (mention, platform) in zip(rows, labels):
        row[MENTION_COL] = mention
        row[PLATFORM_COL] = platform

        if mention == "Yes":
            yes_count += 1

    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=fieldnames,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV.name}")
    print(f"Social media mentions (Yes): {yes_count}")


if __name__ == "__main__":
    main()