"""mtg-mechanics-parser triggered ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.constants.searches import TRIGGER_RE, UPKEEP_COST_RE, DIES_RE

# Get trigger head
def get_trigger_head(trigger: str) -> str:
    match = TRIGGER_RE.search(trigger)

    return match.group(1).lower() if match else ''


# Check if trigger is repeatable or not
def is_repeatable(trigger: str) -> int:
    head = get_trigger_head(trigger)

    return int(head in {'whenever', 'at'})


# Classify ability as triggered and extract features
def triggered_features(ability: Ability) -> dict[str, int]:

    if ability.type != AbilityType.TRIGGERED:
        return {}

    trigger = ability.normalized_condition()
    
    if UPKEEP_COST_RE.search(ability.normalized_effect()):
        return {}

    found_enters = int('enters' in trigger)
    found_dies = int(bool(DIES_RE.search(trigger)))

    found_repeatable = is_repeatable(trigger)

    if found_repeatable:
        found_enters = 0
        found_dies = 0
        
    if found_enters == 0 and found_dies == 0 and found_repeatable == 0:
        found_repeatable = 1
    
    return {
        'enters_trigger': found_enters,
        'dies_trigger': found_dies,
        'repeatable_trigger': found_repeatable,
    }
