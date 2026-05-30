"""mtg-mechanics-parser keyword counter features extractor."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.features.utils.counters_utils import (
    is_keyword_counter_context,
    extract_keyword_counters,
    score_keyword_counter_choice,
)
from mtg_parser.features.utils.parsing import is_modular, get_count_from_text

from mtg_parser.constants.searches import COUNTER_CHOICE_RE, CHOOSE_N_RE


def keyword_counter_features(ability: Ability) -> dict[str, int]:
    if ability.type != AbilityType.STATIC:
        return {}

    effect = ability.normalized_effect()

    if not is_keyword_counter_context(effect):
        return {}

    if not COUNTER_CHOICE_RE.search(effect):
        return {}

    keywords = extract_keyword_counters(effect)

    if not keywords:
        return {}

    choose_n = 1

    match = CHOOSE_N_RE.search(effect)
    if match:
        choose_n = get_count_from_text(match.group(1))

    choose_n = min(choose_n, len(keywords))

    modular_bonus = int(is_modular(effect))

    score = score_keyword_counter_choice(
        keywords=keywords, choose_n=choose_n, modular_bonus=modular_bonus
    )

    return {'keyword_counters': score}