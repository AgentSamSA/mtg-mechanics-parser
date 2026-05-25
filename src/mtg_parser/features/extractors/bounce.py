"""mtg-mechanics-parser bouncing features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses

from mtg_parser.constants.searches import BOUNCE_RE, TOP_LIBRARY_RE

def has_bounce(ability: Ability) -> dict[str, int]:
    
    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    bounce = 0
    deck_stack = 0
    
    for clause in clauses:
        if 'you control' in clause:
            continue

        if TOP_LIBRARY_RE.search(clause):
            deck_stack += 2
            
        elif BOUNCE_RE.search(clause):
            bounce += 1
        
    return {'has_bounce': bounce, 'has_deck_stack': deck_stack}