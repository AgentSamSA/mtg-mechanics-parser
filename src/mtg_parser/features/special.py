"""mtg-mechanics-parser special features extraction."""


from dataclasses import dataclass

from mtg_parser.parsing.ability import Ability, AbilityType
from mtg_parser.constants.searches import PLUS1_COUNTER_RE

@dataclass
class SpecialFeatures:
    enters_trigger: int = 0
    dies_trigger: int = 0
    has_search: int = 0
    plus1_counter: int = 0

    
def extract_special_features(ability: Ability) -> SpecialFeatures:
    features = SpecialFeatures()
        
    effect = (ability.effect or '').lower()
        
    if 'search' in effect:
        features.has_search = 1
            
    if PLUS1_COUNTER_RE.search(effect):
        features.plus1_counter = 1
            
    if ability.type == AbilityType.TRIGGERED and ability.source:
        trigger = ability.source.lower()
            
        if 'enters' in trigger:
            features.enters_trigger = 1
            
        if 'dies' in trigger:
            features.dies_trigger = 1
        
    return features