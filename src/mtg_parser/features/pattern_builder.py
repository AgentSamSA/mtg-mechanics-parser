"""mtg-mechanics-parser global pattern builder.

Build patterns for detecting global effects in oracle text."""


import re

from mtg_parser.constants.mechanics import CREATURE_TYPES
from mtg_parser.constants.searches import QUANTIFIER_PATTERNS

def build_creature_quantifier_patterns():
    types = '|'.join(map(re.escape, CREATURE_TYPES))
    
    return [
        rf'\ball ({types})s?\b',
        rf'\bother ({types})s?\b',
        rf'\beach ({types})s?\b',
        rf'\b({types})s?.*\byou control\b',
        rf'\b({types})s?\b(?!.*\byou control\b)',
    ]

CREATURE_QUANTIFIERS = build_creature_quantifier_patterns()

GLOBAL_QUANTIFIERS = QUANTIFIER_PATTERNS + CREATURE_QUANTIFIERS

GLOBAL_PATTERNS = [re.compile(p, re.IGNORECASE) for p in GLOBAL_QUANTIFIERS]