"""mtg-mechanics-parser static ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

# Classify ability as static and extract features
def static_features(ability: Ability) -> dict[str, int]:
    
    if ability.type != AbilityType.STATIC:
        return {}
    
    return {'baseline_score': 1}