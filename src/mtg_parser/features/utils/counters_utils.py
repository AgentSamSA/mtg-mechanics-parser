"""mtg-mechanics-parser keyword counter features helper utilities."""


import re

from mtg_parser.constants.mechanics import KEYWORD_COUNTERS
from mtg_parser.constants.features import KEYWORD_WEIGHTS
from mtg_parser.constants.searches import FROM_AMONG_RE

EXPLICIT_COUNTER_RE = re.compile(
    r'\b(' + '|'.join(map(re.escape, KEYWORD_COUNTERS)) + r'\s+counters?\b',
    re.IGNORECASE,
)

# Get explicit keyword counters from ability
def extract_explicit_keyword_counters(text: str) -> list[str]:
    return EXPLICIT_COUNTER_RE.findall(text)


# Get keyword counters from pool
def extract_counter_pool(text: str) -> list[str]:
    match = FROM_AMONG_RE.search(text)

    if not match:
        return []

    pool_text = match.group(1).lower()

    raw_items = re.split(r',|\bor\b', pool_text)

    keywords = []

    for item in raw_items:
        item = item.strip()

        for kw in KEYWORD_COUNTERS:
            if kw in item:
                keywords.append(item)

    return keywords


def extract_keyword_counters(text: str) -> list[str]:
    explicit = set(extract_explicit_keyword_counters(text))
    pool = set(extract_counter_pool(text))

    return list(explicit | pool)

# Get score of keyword counters
def score_keyword_counter_choice(
    keywords: list[str], choose_n: int = 1, modular_bonus: int = 0
) -> int:

    keywords = list(set(keywords))

    values = sorted(
        (KEYWORD_WEIGHTS.get(k, 1) for k in keywords), reverse=True
    )

    return sum(values[:choose_n]) + modular_bonus
