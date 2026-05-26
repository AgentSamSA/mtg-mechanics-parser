"""mtg-mechanics-parser feature extraction helper utilities."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.constants.searches import (
    CLAUSES_RE,
    SUBCLAUSE_RE,
    QUANTITY_RE,
    WORD_TO_NUM,
)

# Get clauses within each ability from oracle text
def get_clauses(text: str) -> list[str]:
    clauses = CLAUSES_RE.split(text)

    final = []
    for c in clauses:
        parts = SUBCLAUSE_RE.split(c)
        final.extend(parts)

    return [p.strip() for p in final if p.strip()]


# Get total value from text
def get_count_from_text(effect: str) -> int:

    matches = QUANTITY_RE.findall(effect)

    total = 0
    for m in matches:
        if m.isdigit():
            total += int(m)
        else:
            total += WORD_TO_NUM.get(m, 1)

    return total
