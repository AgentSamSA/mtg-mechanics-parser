"""Core scoring functions for MTG creature cards.

The parser should eventually turn oracle text into structured features.
This module only converts existing card fields/features into scores.

Weights are provisional and live in ``weights.py``.
"""

from __future__ import annotations

import ast
import math
from typing import Any, Mapping

from mtg_parser.scoring.weights import (
    CATEGORY_WEIGHTS,
    DEFAULT_KEYWORD_WEIGHT,
    KEYWORD_WEIGHTS,
    ORACLE_FEATURE_WEIGHTS,
    PT_SCORE_CEILING,
    PT_SCORE_FLOOR,
    PT_WEIGHTS,
)

CardLike = Mapping[str, Any]


# Helpers

def _get(card: CardLike, key: str, default: Any = None) -> Any:
    """Read a field from a dict-like or pandas Series safely."""
    try:
        value = card[key]
    except (KeyError, IndexError, TypeError):
        return default
    # pandas exposes NaN for missing numerics; treat as default.
    if isinstance(value, float) and math.isnan(value):
        return default
    if value is None:
        return default
    return value


def _coerce_keywords(raw: Any) -> list[str]:
    """Return keywords as a list, including CSV string-repr values."""
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(k) for k in raw]
    if isinstance(raw, str):
        s = raw.strip()
        if not s or s == '[]':
            return []
        try:
            parsed = ast.literal_eval(s)
        except (ValueError, SyntaxError):
            return []
        if isinstance(parsed, list):
            return [str(k) for k in parsed]
    return []


# Scoring functions

def score_power_toughness(card: CardLike) -> float:
    """Score power/toughness, with a small CMC discount."""
    power = _get(card, 'power_numeric', 0.0) or 0.0
    toughness = _get(card, 'toughness_numeric', 0.0) or 0.0
    cmc = _get(card, 'cmc', 0.0) or 0.0

    raw = (
        PT_WEIGHTS['power'] * float(power)
        + PT_WEIGHTS['toughness'] * float(toughness)
        + PT_WEIGHTS['cmc_discount'] * float(cmc)
    )
    return max(PT_SCORE_FLOOR, min(PT_SCORE_CEILING, raw))


def score_keywords(card: CardLike) -> float:
    """Score keyword abilities using provisional weights."""
    keywords = _coerce_keywords(_get(card, 'keywords'))
    total = 0.0
    for kw in keywords:
        total += KEYWORD_WEIGHTS.get(kw, DEFAULT_KEYWORD_WEIGHT)
    return total


def score_oracle_text(card: CardLike) -> float:
    """Placeholder until oracle-text parser features are available."""
    del card
    _ = ORACLE_FEATURE_WEIGHTS
    return 0.0


def score_card(card: CardLike) -> dict[str, float]:
    """Return separate subscores and the combined total score."""
    pt = score_power_toughness(card)
    kw = score_keywords(card)
    oracle = score_oracle_text(card)

    total = (
        CATEGORY_WEIGHTS['pt'] * pt
        + CATEGORY_WEIGHTS['keyword'] * kw
        + CATEGORY_WEIGHTS['oracle'] * oracle
    )

    return {
        'pt_score': pt,
        'keyword_score': kw,
        'oracle_score': oracle,
        'total_power_score': total,
    }
