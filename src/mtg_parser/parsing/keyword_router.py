"""mtg-mechanics-parser keyword router module.

Identify keyword lines in oracle text to avoid reparsing them."""


import re

from mtg_parser.utils.normalizer import normalize_keyword

# Strip additional text for keyword line
def strip_keyword_params(token: str) -> str:
    return re.sub(r'\{.*?}', '', token).strip()

# Build normalized keyword set from keywords column
def build_card_keywords(row):
    if not isinstance(row['keywords'], list):
        return set()
    
    return {
        normalize_keyword(k)
        for k in row['keywords']
    }
    
# Check if line is valid keyword line
def is_keyword_line(line: str, card_keywords: set[str]) -> bool:
    tokens = {
        normalize_keyword(strip_keyword_params(t.strip()))
        for t in line.split(',')
    }
    
    return tokens.issubset(card_keywords)