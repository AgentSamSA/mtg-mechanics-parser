"""mtg-mechanics-parser card scoring object."""


from dataclasses import dataclass

@dataclass
class CardScore:
    ability: float
    keyword: float
    pt: float
    
    @property
    def total(self):
        return self.ability + self.keyword + self.pt