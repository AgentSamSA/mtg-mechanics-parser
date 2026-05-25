"""mtg-mechanics-parser special features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import PLUS1_COUNTER_RE

def special_features(ability: Ability) -> dict[str, int]:   
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    counters = 0
    search = 0
    
    for clause in clauses:
        if 'search' in clause:
            search += 1
            
        if PLUS1_COUNTER_RE.search(clause):
            counters += 1
        
    return {'has_search': search, 'plus1_counter': counters}