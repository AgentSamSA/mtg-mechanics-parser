"""mtg-mechanics-parser mana feature helper utilities."""


from mtg_parser.features.utils.parsing import get_count_from_text

from mtg_parser.constants.searches import (
    MANA_SYMBOL_RE,
    ADD_RE,
    ANY_COLOR_RE,
    OR_SPLIT_RE
)

# Compute the amount of mana produced
def count_mana_base(clause: str) -> int:
    symbols = MANA_SYMBOL_RE.findall(clause)

    if symbols:
        return len(symbols)

    return get_count_from_text(clause)


# Check if ability is mana producing
def is_mana_producing(clause: str) -> bool:
    return ADD_RE.search(clause) and count_mana_base(clause) > 0


# Check if ability can produce any color mana
def has_any_color_mana(clause: str) -> bool:
    return ANY_COLOR_RE.search(clause) is not None


# Get all mana options from mana ability
def extract_mana_options(clause: str) -> list[int]:
    parts = OR_SPLIT_RE.split(clause)

    return [count_mana_base(p) for p in parts]
