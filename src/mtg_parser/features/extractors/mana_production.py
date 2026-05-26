"""mtg-mechanics-parser mana production features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import (
    get_clauses,
    get_count_from_text,
)

from mtg_parser.constants.searches import (
    MANA_SYMBOL_RE,
    ANY_COLOR_RE,
    COST_REDUCTION_RE,
    ADD_RE,
    OR_RE,
    OR_SPLIT_RE,
)

# Helper function to compute mana
def count_mana(clause: str) -> int:
    symbols = MANA_SYMBOL_RE.findall(clause)
    symbol_count = len(symbols)

    if ANY_COLOR_RE.search(clause):
        word_count = get_count_from_text(clause)
        return word_count + 1

    return symbol_count


def mana_production(ability: Ability) -> dict[str, int]:

    effect = ability.normalized_effect()
    clauses = get_clauses(effect)

    mana = 0
    reduced = 0

    for clause in clauses:

        is_mana = ADD_RE.search(clause)
        is_reduction = COST_REDUCTION_RE.search(clause)

        if not is_mana and not is_reduction:
            continue

        if is_mana:

            if OR_RE.search(clause):
                parts = OR_SPLIT_RE.split(clause)
                best = max(count_mana(p) for p in parts)
                mana += best
            else:
                mana += count_mana(clause)

        if is_reduction:
            reduced += count_mana(clause)

    return {'mana_production': mana, 'mana_reduction': reduced}
