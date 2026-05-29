"""mtg-mechanics-parser mana production features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import (
    get_clauses,
    count_mana_base,
    has_any_color_mana,
    extract_mana_options
)

from mtg_parser.constants.searches import (
    COST_REDUCTION_RE,
    ADD_RE
)


from mtg_parser.utils.text_preprocessing import preprocess_oracle_text
from mtg_parser.constants.searches import QUANTITY_RE

def mana_production(ability: Ability) -> dict[str, int]:

    effect = ability.normalized_effect()
    clauses = get_clauses(effect)

    mana = 0
    reduced = 0
    any_color_bonus = 0

    for clause in clauses:

        is_mana = ADD_RE.search(clause)
        is_reduction = COST_REDUCTION_RE.search(clause)

        if is_mana:

            options = extract_mana_options(clause)
            base = max(options) if options else count_mana_base(clause)
            
            mana += base
            
            if has_any_color_mana(clause):
                any_color_bonus += 1

        if is_reduction:
            reduced += count_mana_base(clause)

    return {'mana_produced': mana + any_color_bonus, 'mana_reduction': reduced}
