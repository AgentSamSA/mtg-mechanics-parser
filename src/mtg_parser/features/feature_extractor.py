"""mtg-mechanics-parser ability feature pipeline.

Defines AbilityFeaturePipeline to apply our feature extractors. 
Applies feature extractors to an ability and aggregates their outputs into a feature vector."""


from mtg_parser.parsing.ability import Ability
from mtg_parser.features.ability_features import AbilityFeatures

class AbilityFeaturePipeline:
    def __init__(self, features):
        self.features = features
    
    def transform_one(self, ability: Ability) -> AbilityFeatures:
        f = AbilityFeatures()
        
        for extractor in self.features:
            updates = extractor(ability)
            f.add(updates)
            
        return f
    
    def transform(self, abilities):
        return [self.transform_one(a).to_vector() for a in abilities]