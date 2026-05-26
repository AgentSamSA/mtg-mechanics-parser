"""mtg-mechanics-parser global effect features extraction."""


import re

from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import get_clauses
from mtg_parser.features.detect_zone import is_resolution_zone_text

from mtg_parser.features.pattern_builder import GLOBAL_QUANTIFIERS

def has_global(ability: Ability) -> dict[str, int]:
    
    effect = ability.normalized_effect()
    clauses = get_clauses(effect)
    
    found_global = 0
    
    for clause in clauses:
        if is_resolution_zone_text(clause):
            continue
        
        is_global = any(re.search(p, clause) for p in GLOBAL_QUANTIFIERS)
    
        if is_global:
            found_global = 1
    
    return {'has_global': found_global}