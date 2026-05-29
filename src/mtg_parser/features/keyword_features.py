"""mtg-mechanics-parser keyword features definition.

Defines our keyword features based on our scoring criteria.
Builds out keyword features from the card row."""


from dataclasses import dataclass, field

from mtg_parser.utils.normalizer import normalize_keyword

from mtg_parser.constants.mechanics import ABILITY_WORDS

@dataclass
class KeywordFeatures:
    features: dict[str, int] = field(default_factory=dict)
    
    def to_vector(self, keyword_order: list[str]) -> list[int]:
        return [self.features.get(k, 0) for k in keyword_order]
    
    def __post_init__(self):
        self.features = dict(self.features)

# Filter out ability words from keyword list
def is_real_keyword(keyword: str) -> bool:
    return normalize_keyword(keyword) not in ABILITY_WORDS

# Build our keyword features from dataframe row
def build_keyword_features(row) -> KeywordFeatures:
    keywords = row.get('keywords', [])
    
    if not isinstance(keywords, list):
        keywords = []
        
    normalized = {
        normalize_keyword(k): 1
        for k in keywords
        if is_real_keyword(k)
    }
    
    return KeywordFeatures(features=normalized.copy())    