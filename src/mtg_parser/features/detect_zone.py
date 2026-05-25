"""mtg-mechanics-parser zone detection.

Identify zones in oracle text."""


import re

from mtg_parser.constants.searches import ZONE_PATTERNS

def is_resolution_zone_text(text: str) -> bool:
    text = (text or '').lower()
    return any(re.search(p, text) for p in ZONE_PATTERNS)