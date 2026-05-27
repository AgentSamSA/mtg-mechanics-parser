"""mtg-mechanics-parser card features definition.

Aggregates our existing features for each Card object."""


from dataclasses import dataclass

from mtg_parser.parsing.ability import Ability
from mtg_parser.features.keyword_features import KeywordFeatures

@dataclass
class CardFeatures:
    abilities: list[Ability]
    keyword_features: KeywordFeatures
    
    power: float
    toughness: float

    power_is_star: bool = False