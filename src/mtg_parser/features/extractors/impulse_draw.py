"""mtg-mechanics-parser impulse draw features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import IMPULSE_DRAW_RE

def has_impulse_draw(ability: Ability) -> dict[str, int]:
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    total = 0
    
    for clause in clauses:
        if IMPULSE_DRAW_RE.search(clause):
            total += 1
    
    return {'has_exile_access', total}