"""mtg-mechanics-parser keyword router module.

Identify keyword lines in oracle text to avoid reparsing them for ability feature detection."""


import re
import ast

from mtg_parser.utils.normalizer import normalize_keyword

# Convert keywords column into actual list
def parse_keywords_column(df):
    def fix_type(x):
        if isinstance(x, list):
            return x
        if isinstance(x, str):
            return ast.literal_eval(x)
        return []
    
    df = df.copy()
    df['keywords'] = df['keywords'].apply(fix_type)
    
    return df

# Strip additional text for keyword line
def strip_keyword_params(token: str) -> str:
    token = re.sub(r'\{[^}]+\}', '', token)
    token = re.sub(r'\b\d+\b', '', token)
    
    return ' '.join(token.split()).strip()

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
    if ':' in line:
        return False
    if '—' in line:
        return False
    
    tokens = {
        normalize_keyword(strip_keyword_params(t.strip()))
        for t in line.split(',')
        if t.strip()
    }
    
    if not tokens:
        return False
    
    return all(t in card_keywords for t in tokens)