"""mtg-mechanics-parser triggered ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

from mtg_parser.constants.searches import TRIGGER_RE

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

    found_enters = int('enters' in trigger)
    found_dies = int('dies' in trigger)

    found_repeatable = is_repeatable(trigger)

    if found_repeatable:
        found_enters = 0

    return {
        'enters_trigger': found_enters,
        'dies_trigger': found_dies,
        'repeatable_trigger': found_repeatable,
    }
