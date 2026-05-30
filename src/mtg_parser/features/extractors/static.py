"""mtg-mechanics-parser static ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.features.utils.counters_utils import is_keyword_counter_context

def static_features(ability: Ability) -> dict[str, int]:

    if ability.type != AbilityType.STATIC:
        return {}
    
    if is_keyword_counter_context(ability.normalized_effect()):
        return {}

    return {'baseline_score': 1}