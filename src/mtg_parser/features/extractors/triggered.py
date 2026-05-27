"""mtg-mechanics-parser triggered ability features extraction."""


from mtg_parser.parsing.ability import Ability, AbilityType

# Classify ability as triggered and extract features
def triggered_features(ability: Ability) -> dict[str, int]:

    if ability.type != AbilityType.TRIGGERED:
        return {}

    trigger = ability.normalized_condition()

    found_enters = 0
    found_dies = 0
    found_repeatable = 0

    if trigger.startswith('when'):
        if 'enters' in trigger:
            found_enters = 1

        if 'dies' in trigger:
            found_dies = 1

    # Repeatable triggers exclude one-time enters/dies triggers
    if not found_enters and not found_dies:
        if trigger.startswith('whenever') or 'at the beginning' in trigger:
            found_repeatable = 1

    return {
        'baseline_score': 1,
        'enters_trigger': found_enters,
        'dies_trigger': found_dies,
        'repeatable_trigger': found_repeatable,
    }
