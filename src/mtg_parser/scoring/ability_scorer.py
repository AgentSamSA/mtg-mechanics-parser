"""mtg-mechanics-parser ability scorer.

Use AbilityFeaturePipeline and AbilityFeatures to score each card's abilities.
Outputs a list of AbilityScore objects for the CardScore object."""


from mtg_parser.parsing.ability import Ability
from mtg_parser.features.ability_features import AbilityFeatures
from mtg_parser.scoring.models.ability_score import AbilityScore

from mtg_parser.constants.features import FEATURE_WEIGHTS, ABILITY_PIPELINE

# Sum individual feature scores for ability
def score_ability(features: AbilityFeatures) -> int:
    return sum(
        getattr(features, k) * w
        for k, w in FEATURE_WEIGHTS.items()
    )

# Get scores for each ability in card
def get_ability_scores(abilities: list[Ability]) -> list[AbilityScore]:    
    ability_scores = []
    
    for ability in abilities:
        features = ABILITY_PIPELINE.transform_one(ability)
        
        ability_scores.append(
            AbilityScore(
                ability=ability,
                features=features,
                score=score_ability(features)
            )
        )
        
    return ability_scores

# Aggregate scored abilities
def score_abilities(abilities: list[Ability]) -> int:
    return sum(
        s.score for s in get_ability_scores(abilities)
    )