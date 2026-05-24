"""mtg-mechanics-parser token features extraction."""


from dataclasses import dataclass

from mtg_parser.parsing.ability import Ability
from mtg_parser.constants.searches import (
    CREATURE_TOKEN_RE,
    OPPONENT_RE,
    PT_RE,
    QUANTITY_RE,
    WORD_TO_NUM,
)

@dataclass
class TokenFeatures:
    pt_total: int = 0


# Parse token ownership
def get_token_owner(effect: str) -> str:
    if OPPONENT_RE.search(effect):
        return 'opponent'

    return 'you'

# Get power/toughness of created tokens
def extract_pt(effect: str):
    return PT_RE.findall(effect)


# Get numeric values from power/toughness
def pt_value(pt_pairs):
    total = 0
    for p, t in pt_pairs:
        if p == 'X' or t == 'X':
            total += 1
        if p.isdigit() and t.isdigit():
            total += int(p) + int(t)

    return total

# Get total quantity of tokens
def extract_token_count(effect: str) -> int:
    matches = QUANTITY_RE.findall(effect.lower())
    
    total = 0
    for m in matches:
        if m.isdigit():
            total += int(m)
        else:
            total += WORD_TO_NUM.get(m, 1)
    
    if total == 0 and 'token' in effect:
        return 1
    
    return total

def extract_token_features(ability: Ability) -> TokenFeatures:
    features = TokenFeatures()

    effect = (ability.effect or '').lower()

    if not CREATURE_TOKEN_RE.search(effect):
        return features

    owner = get_token_owner(effect)
    
    pt_pairs = extract_pt(effect)
    pt_score = pt_value(pt_pairs)
    
    num_tokens = extract_token_count(effect)
    total = pt_score * num_tokens
    
    if owner == 'you':
        features.pt_total = total
    else:
        features.pt_total = -total
    
    return features
