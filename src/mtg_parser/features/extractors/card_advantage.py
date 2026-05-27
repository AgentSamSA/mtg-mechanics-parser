"""mtg-mechanics-parser card advantage features extraction."""


import re

from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import get_clauses, get_count_from_text

from mtg_parser.constants.searches import (
    HAND_GAIN_PATTERNS,
    HAND_LOSS_PATTERNS,
    ALL_PLAYERS_RE,
    OPPONENT_RE
)

def card_advantage(ability: Ability) -> dict[str, int]:

    effect = ability.normalized_effect()
    clauses = get_clauses(effect)
    
    total = 0
    
    for clause in clauses:
        is_gain = any(re.search(p, clause) for p in HAND_GAIN_PATTERNS)
        is_loss = any(re.search(p, clause) for p in HAND_LOSS_PATTERNS)
        
        multiplier = 0 if ALL_PLAYERS_RE.search(clause) else 1
        
        if is_gain:
            num_cards = get_count_from_text(clause)
                            
            if OPPONENT_RE.search(clause):
                total -= multiplier * num_cards
            else:
                total += multiplier * num_cards
                    
        if is_loss:
            num_cards = get_count_from_text(clause)
            
            if OPPONENT_RE.search(clause):
                total += multiplier * num_cards
            else:
                total -= multiplier * num_cards

    return {'card_advantage': total if total >= 0 else 0}
