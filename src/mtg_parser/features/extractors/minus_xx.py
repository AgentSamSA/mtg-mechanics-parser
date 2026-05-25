"""mtg-mechanics-parser minus X features exctraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import MINUS_X_RE, MINUS_X_MASS_RE

def has_minus_X(ability: Ability) -> dict[str, int]:
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    total = 0
    
    for clause in clauses:
        if MINUS_X_MASS_RE.search(clause):
            total += 2
            
        elif MINUS_X_RE.search(clause):
            total += 1
                      
    return {'has_minus_X': total}