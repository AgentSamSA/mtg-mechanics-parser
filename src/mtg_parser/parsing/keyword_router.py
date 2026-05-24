"""mtg-mechanics-parser keyword router module.

Identify keyword lines in oracle text to avoid reparsing them."""


from mtg_parser.utils.normalizer import normalize_keyword

# Build normalized keyword set from keywords column
def build_card_keywords(row):
    return {
        normalize_keyword(k)
        for k in row['keywords']
        if isinstance(row['keywords'], list)
    }
    
# Check if line is valid keyword line
def is_keyword_line(line: str, card_keywords: set[str]) -> bool:
    tokens = {
        normalize_keyword(t.strip())
        for t in line.split(',')
    }
    
    return tokens.issubset(card_keywords)