"""mtg-mechanics-parser keyword counter features extractor."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.utils.counters_utils import extract_keyword_counters, score_keyword_counter_choice
from mtg_parser.features.utils.parsing import is_modular, get_count_from_text

from mtg_parser.constants.searches import CHOOSE_N_RE


def keyword_counter_features(ability: Ability) -> dict[str, int]:
    effect = ability.normalized_effect()
    
    keywords = extract_keyword_counters(effect)
    
    if not keywords:
        return {}
    
    choose_n = 1
    
    match = CHOOSE_N_RE.search(effect)
    if match:
        choose_n = get_count_from_text(match.group(1))
    
    choose_n = min(choose_n, len(keywords))
    
    is_choice = is_modular(effect)
    
    modular_bonus = int(is_choice)
    
    score = score_keyword_counter_choice(keywords=keywords, choose_n=choose_n, modular_bonus=modular_bonus)
    
    return {
        'keyword_counters': score
    }
    
    

