"""mtg-mechanics-parser reanimate features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import REANIMATE_RE

def has_reanimate(ability: Ability) -> dict[str, int]:
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    total = 0
    
    for clause in clauses:
        if REANIMATE_RE.search(clause):
            total += 1

    return {'has_recursion_battlefield': total}