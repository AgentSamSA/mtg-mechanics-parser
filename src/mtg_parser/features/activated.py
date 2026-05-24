"""mtg-mechanics-parser activated ability features extraction."""


from enum import Enum

from mtg_parser.parsing.ability import Ability, AbilityType
from mtg_parser.constants.searches import LIMITER_RE, LIFE_COST_RE

class ActivationType(Enum):
    LIMITER = 1
    NO_LIMITER = 2
    

# Classify type of activation cost
def classify_cost(ability: Ability) -> ActivationType:
    if ability.type != AbilityType.ACTIVATED:
        return None
    
    cost = (ability.source or '').lower()
    
    has_limiter = bool(LIMITER_RE.search(cost))
    has_life = bool(LIFE_COST_RE.search(cost))
    has_free = '{0}' in cost
    
    if not has_limiter and (has_life or has_free):
        return ActivationType.NO_LIMITER
    
    return ActivationType.LIMITER