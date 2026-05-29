"""mtg-mechanics-parser card scoring object.

Contains a list of AbilityScore objects and the score for keywords and power/toughness as floats.
Includes aggregation function in ability property for obtaining total score from abilities.
Includes aggregation function to sum total score from all three categories."""


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