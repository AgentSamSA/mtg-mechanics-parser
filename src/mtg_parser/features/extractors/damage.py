"""mtg-mechanics-parser damage features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import DAMAGE_RE, OPP_DAMAGE_RE, SELF_ONLY_RE

def has_direct_damage(ability: Ability) -> dict[str, int]:
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    found_damage = 0
    
    for clause in clauses:
        if SELF_ONLY_RE.search(clause):
            continue
        
        if DAMAGE_RE.search(clause):
            
            if OPP_DAMAGE_RE.search(clause):
                found_damage = 1
        
    return {'has_direct_damage': found_damage}