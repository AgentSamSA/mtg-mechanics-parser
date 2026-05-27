"""mtg-mechanics-parser card record object."""


from dataclasses import dataclass
from datetime import date

from mtg_parser.features.card_features import CardFeatures

@dataclass
class CardRecord:
    oracle_id: str
    name: str
    set: str
    set_name: str
    released_at: date

    features: CardFeatures
