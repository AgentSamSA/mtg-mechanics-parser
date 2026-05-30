"""mtg-mechanics-parser global effect features extraction."""


import re

from mtg_parser.parsing.ability import Ability

from mtg_parser.features.utils.parsing import get_clauses
from mtg_parser.features.detect_zone import is_resolution_zone_text

from mtg_parser.features.pattern_builder import GLOBAL_PATTERNS


def has_global(ability: Ability) -> dict[str, int]:

    text = ability.raw.lower()
    clauses = get_clauses(text)
    
    found_global = 0

    for clause in clauses:
        if is_resolution_zone_text(clause):
            continue

        if any(re.search(p, clause) for p in GLOBAL_PATTERNS):
            found_global = 1
            break
    
    return {'has_global': found_global}
