"""mtg-mechanics-parser special features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import get_clauses

from mtg_parser.constants.searches import PLUS1_COUNTER_RE

def special_features(ability: Ability) -> dict[str, int]:   
    
    effect = ability.normalized_effect()
    clauses = get_clauses(effect)
    
    found_counters = 0
    found_search = 0
    
    for clause in clauses:
        if 'search' in clause:
            found_search = 1
            
        if PLUS1_COUNTER_RE.search(clause):
            found_counters = 1
        
    return {'has_search': found_search, 'plus1_counter': found_counters}