"""mtg-mechanics-parser triggered ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

# Classify ability as triggered and extract features
def triggered_features(ability: Ability) -> dict[str, int]:
    
    if ability.type != AbilityType.TRIGGERED:
        return {}
    
    trigger = (ability.condition or '').lower()
    
    enters = 0
    dies = 0
    repeatable = 0
    
    if 'whenever' in trigger or 'at' in trigger:
        repeatable += 1
            
    if trigger.startswith('when'):
        if 'enters' in trigger:
            enters += 1
            
        if 'dies' in trigger:
            dies += 1
    
    return {'enters_trigger': enters, 'dies_trigger': dies, 'repeatable_trigger': repeatable}