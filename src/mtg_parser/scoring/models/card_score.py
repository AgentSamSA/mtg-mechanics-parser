"""mtg-mechanics-parser card scoring object."""


from dataclasses import dataclass

from mtg_parser.scoring.models.ability_score import AbilityScore

@dataclass
class CardScore:
    abilities: list[AbilityScore] 
    keyword: float
    pt: float
    
    @property
    def ability(self):
        return sum(a.score for a in self.abilities)
    
    @property
    def total(self):
        return self.ability + self.keyword + self.pt