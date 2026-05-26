"""mtg-mechanics-parser destroy effect features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import DESTROY_RE, DESTROY_MASS_RE

def has_destroy(ability: Ability) -> dict[str, int]:
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    found_destroy = 0
    found_mass_destroy = 0
    
    for clause in clauses:
        if DESTROY_MASS_RE.search(clause):
            found_mass_destroy = 1
        
        elif DESTROY_RE.search(clause):
            found_destroy = 1
    
    return {'has_destroy': found_destroy, 'has_mass_destroy': found_mass_destroy}
