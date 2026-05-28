"""mtg-mechanics-parser card ability bundle object."""


from dataclasses import dataclass
from datetime import date

from mtg_parser.parsing.ability import Ability

@dataclass
class CardAbilityBundle:
    oracle_id: str
    name: str
    set: str
    set_name: str
    released_at: date
    
    abilities: list[Ability]