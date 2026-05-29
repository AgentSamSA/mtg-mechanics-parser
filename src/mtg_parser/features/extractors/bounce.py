"""mtg-mechanics-parser bounce features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import get_clauses

from mtg_parser.constants.searches import BOUNCE_RE, TOP_LIBRARY_RE

def has_bounce(ability: Ability) -> dict[str, int]:
    
    effect = ability.normalized_effect()
    clauses = get_clauses(effect)
    
    found_bounce = 0
    found_deck_stack = 0
    
    for clause in clauses:
        if 'you control' in clause:
            continue

        if TOP_LIBRARY_RE.search(clause):
            found_deck_stack = 1
            
        elif BOUNCE_RE.search(clause):
            found_bounce = 1
        
    return {'has_bounce': found_bounce, 'has_deck_stack': found_deck_stack}