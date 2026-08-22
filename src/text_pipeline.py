"""Transparent text features for a small China-Australia document corpus."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

COOPERATION_TERMS = ("合作", "对话", "改善", "修复", "互利", "cooperation", "dialogue", "improve")
FRICTION_TERMS = ("争端", "制裁", "干涉", "AUKUS", "核潜艇", "disagreement", "sanction", "tension")
AUSTRALIA_TERMS = ("澳大利亚", "澳方", "中澳", "Australia", "Australian", "Canberra", "AUKUS")


def clean_text(value: object) -> str:
    """Normalize whitespace without changing the substantive text."""
    return re.sub(r"\s+", " ", str(value or "").replace("\u3000", " ")).strip()


def keyword_count(text: str, terms: tuple[str, ...]) -> int:
    normalized = clean_text(text).lower()
    return sum(normalized.count(term.lower()) for term in terms)


def classify_stage(date_value: str) -> str:
    """Return a descriptive period label; boundaries are explicit and editable."""
    match = re.match(r"(\d{4})", str(date_value))
    if not match:
        return "unknown"
    year = int(match.group(1))
    if 1972 <= year <= 2016:
        return "1972-2016"
    if 2017 <= year <= 2021:
        return "2017-2021"
    if 2022 <= year:
        return "2022-present"
    return "outside-study-period"


def analyse_row(row: dict[str, str]) -> dict[str, str | int | bool]:
    text = clean_text(f"{row.get('title', '')} {row.get('text', '')}")
    cooperation = keyword_count(text, COOPERATION_TERMS)
    friction = keyword_count(text, FRICTION_TERMS)
    return {
        **row,
        "stage": classify_stage(row.get("date", "")),
        "australia_relevant": keyword_count(text, AUSTRALIA_TERMS) > 0,
        "cooperation_count": cooperation,
        "friction_count": friction,
        "frame_balance": cooperation - friction,
    }


def run(input_path: Path, output_path: Path) -> None:
    with input_path.open(encoding="utf-8-sig", newline="") as stream:
        rows = [analyse_row(row) for row in csv.DictReader(stream)]
    if not rows:
        raise ValueError("Input contains no records")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python src/text_pipeline.py INPUT.csv OUTPUT.csv")
    run(Path(sys.argv[1]), Path(sys.argv[2]))
