"""mtg-mechanics-parser damage features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.features.utils.parsing import get_clauses

from mtg_parser.constants.searches import (
    DAMAGE_RE,
    LIFE_LOSS_RE,
    OPPONENT_RE,
    OPP_DAMAGE_RE,
    OTHER_DAMAGE_RE,
    SELF_ONLY_RE,
    ALL_PLAYERS_RE
)


def has_direct_damage(ability: Ability) -> dict[str, int]:

    effect = ability.normalized_effect()
    trigger = ability.normalized_condition() if ability.type == AbilityType.TRIGGERED else ''
    
    clauses = get_clauses(effect)

    for clause in clauses:
        
        is_damage_event = (
            bool(DAMAGE_RE.search(clause))
            or bool(LIFE_LOSS_RE.search(clause))
        )
        
        if not is_damage_event:
            continue
        
        if SELF_ONLY_RE.search(clause):
            continue
        if ALL_PLAYERS_RE.search(clause):
            continue
        
        if OPP_DAMAGE_RE.search(clause):
            return {'has_direct_damage': 1}
        
        if ability.type == AbilityType.TRIGGERED:
            if (
                OPPONENT_RE.search(trigger)
                and OTHER_DAMAGE_RE.search(clause)
            ):
                return {'has_direct_damage': 1}

    return {}