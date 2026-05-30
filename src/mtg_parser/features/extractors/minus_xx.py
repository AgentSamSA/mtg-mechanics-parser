"""mtg-mechanics-parser minus X features exctraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.utils.parsing import get_clauses

from mtg_parser.constants.searches import MINUS_X_RE, MINUS_X_MASS_RE


def has_minus_X(ability: Ability) -> dict[str, int]:

    effect = ability.normalized_effect()
    clauses = get_clauses(effect)

    found_minus_X = 0
    found_mass_minus_X = 0

    for clause in clauses:
        if MINUS_X_MASS_RE.search(clause):
            found_mass_minus_X = 1

        elif MINUS_X_RE.search(clause):
            found_minus_X = 1

    return {
        'has_minus_X': found_minus_X,
        'has_mass_minus_X': found_mass_minus_X,
    }
