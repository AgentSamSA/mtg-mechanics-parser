"""mtg-mechanics-parser card advantage features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.utils.parsing import (
    get_clauses,
    get_count_from_text,
    classify_target,
    is_all_players_effect
)

from mtg_parser.constants.searches import (
    DRAW_RE,
    PUT_INTO_HAND_RE,
    RETURN_TO_HAND_RE,
    DISCARD_RE,
)
from mtg_parser.constants.mechanics import EVENT_VALUE

# Determine card advantage value for the ability
def score_clause_card_advantage(clause: str) -> int:
    if is_all_players_effect(clause):
        return 0

    score = 0
    direction = classify_target(clause)

    draw_match = DRAW_RE.search(clause)
    if draw_match:
        count = get_count_from_text(draw_match.group())
        score += EVENT_VALUE['draw'] * direction * count

    put_match = PUT_INTO_HAND_RE.search(clause)
    if put_match:
        count = get_count_from_text(put_match.group())
        score += EVENT_VALUE['put_into_hand'] * direction * count

    return_match = RETURN_TO_HAND_RE.search(clause)
    if return_match:
        count = get_count_from_text(put_match.group())
        score += EVENT_VALUE['return_to_hand'] * direction * count

    discard_match = DISCARD_RE.search(clause)
    if discard_match:
        count = get_count_from_text(discard_match.group())
        score += EVENT_VALUE['discard'] * direction * count

    return score


def card_advantage(ability: Ability) -> dict[str, int]:

    effect = ability.normalized_effect()
    clauses = get_clauses(effect)

    total = 0

    for clause in clauses:
        total += score_clause_card_advantage(clause)

    return {'card_advantage': max(total, 0)}
