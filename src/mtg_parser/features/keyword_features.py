"""mtg-mechanics-parser keyword features definition.

Defines our keyword features based on our scoring criteria.
Builds out keyword features from the card row."""


from dataclasses import dataclass

from mtg_parser.utils.normalizer import normalize_keyword

@dataclass
class KeywordFeatures:
    features: dict[str, int]
    
    def to_vector(self, keyword_order: list[str]) -> list[int]:
        return [self.features.get(k, 0) for k in keyword_order]

def build_keyword_features(row) -> KeywordFeatures:
    keywords = row.get('keywords', [])
    
    if not isinstance(keywords, list):
        keywords = []
        
    normalized = {
        normalize_keyword(k): 1
        for k in keywords
    }
    
    return KeywordFeatures(features=normalized)
        