"""mtg-mechanics-parser keyword features definition.

Defines our keyword features based on our scoring criteria."""


from dataclasses import dataclass
from typing import List

@dataclass
class KeywordFeatures:
    features: dict[str, int]
    
    def to_vector(self, keyword_order: List[str]) -> List[int]:
        return [self.features.get(k, 0) for k in keyword_order]