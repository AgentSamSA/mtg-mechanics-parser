"""mtg-mechanics-parser destroy effect features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import DESTROY_RE, DESTROY_MASS_RE

def has_destroy(ability: Ability) -> dict[str, int]:
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    destroy = 0
    mass_destroy = 0
    
    for clause in clauses:
        if DESTROY_MASS_RE.search(clause):
            mass_destroy += 2
        
        elif DESTROY_RE.search(clause):
            destroy += 1
    
    return {'has_destroy': destroy, 'has_mass_destroy': mass_destroy}
