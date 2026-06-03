"""mtg-mechanics-parser static ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.features.utils.counters_utils import is_keyword_counter_context
from mtg_parser.features.utils.mana_utils import is_mana_producing, is_mana_reduction
from mtg_parser.features.utils.parsing import is_top_level_activated

from mtg_parser.constants.searches import ENTERS_WITH_RE, INIT_CHOOSE_RE

def static_features(ability: Ability) -> dict[str, int]:

    if ability.type != AbilityType.STATIC:
        return {}
    
    effect = ability.normalized_effect()
    
    if is_keyword_counter_context(effect):
        return {}
    
    if (is_mana_producing(effect) or is_mana_reduction(effect)) and not is_top_level_activated(effect):
        return {}
    
    if ENTERS_WITH_RE.search(effect) or INIT_CHOOSE_RE.search(effect):
        return {}

    return {'baseline_score': 1}