"""mtg-mechanics-parser card advantage features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import check_ability, get_clauses, get_count_from_text

from mtg_parser.constants.searches import (
    HAND_GAIN_PATTERNS,
    HAND_LOSS_PATTERNS,
    ALL_PLAYERS_RE,
    OPPONENT_RE
)

def card_advantage(ability: Ability) -> dict[str, int]:

    effect = check_ability(ability)
    clauses = get_clauses(effect)
    
    total = 0
    
    for clause in clauses:
        is_gain = HAND_GAIN_PATTERNS.search(clause)
        is_loss = HAND_LOSS_PATTERNS.search(clause)
        
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
