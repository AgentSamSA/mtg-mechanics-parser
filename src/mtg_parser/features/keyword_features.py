"""mtg-mechanics-parser keyword features definition.

Defines our keyword features based on our scoring criteria."""


from dataclasses import dataclass

@dataclass
class KeywordFeatures:
    features: dict[str, int]
    
    def to_vector(self, keyword_order: list[str]) -> list[int]:
        return [self.features.get(k, 0) for k in keyword_order]