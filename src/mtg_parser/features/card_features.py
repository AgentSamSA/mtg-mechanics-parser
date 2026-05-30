"""mtg-mechanics-parser card features definition.

Aggregates our existing features for each card we have parsed."""


from dataclasses import dataclass

from mtg_parser.parsing.ability import Ability
from mtg_parser.features.keyword_features import (
    KeywordFeatures,
    build_keyword_features
)
from mtg_parser.pipeline.card_ability_bundle import CardAbilityBundle


@dataclass
class CardFeatures:
    abilities: list[Ability]
    keyword_features: KeywordFeatures

    power: float
    toughness: float


def build_card_features(bundle: CardAbilityBundle, row) -> CardFeatures:
    return CardFeatures(
        abilities=bundle.abilities,
        keyword_features=build_keyword_features(row),
        power=row['power_numeric'],
        toughness=row['toughness_numeric']
    )
