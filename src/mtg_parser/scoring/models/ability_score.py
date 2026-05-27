"""mtg-mechanics-parser ability scoring object.

Provides structured breakdown of each ability's score contribution."""


from dataclasses import dataclass

from mtg_parser.parsing.ability import Ability
from mtg_parser.features.ability_features import AbilityFeatures

@dataclass
class AbilityScore:
    ability: Ability
    features: AbilityFeatures
    
    score: int