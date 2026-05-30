"""mtg-mechanics-parser normalizer for keywords.

Normalize keyword text to help obtain canonical text form."""


import re


def normalize_keyword(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[\s-]+', '_', text)
    text = re.sub(r'[^a-z0-9_]', '', text)

    return text