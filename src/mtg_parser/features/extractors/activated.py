"""mtg-mechanics-parser activated ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.constants.searches import LIMITER_RE, LIFE_COST_RE

# Classify type of activation cost
def activated_features(ability: Ability) -> dict[str, int]:

    if ability.type != AbilityType.ACTIVATED:
        return {}

    cost = (ability.cost or '').lower()

    has_limiter = bool(LIMITER_RE.search(cost))
    has_life = bool(LIFE_COST_RE.search(cost))
    has_free = '{0}' in cost

    if not has_limiter and (has_life or has_free):
        return {'activated_no_limiter': 2}

    return {'activated_limiter': 1}
