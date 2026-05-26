"""mtg-mechanics-parser token features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.helpers import get_clauses

from mtg_parser.constants.searches import (
    CREATURE_TOKEN_RE,
    OPPONENT_RE,
    PT_RE,
    TOKEN_EVENT_RE,
    QUANTITY_RE,
    WORD_TO_NUM,
    CLEAN_QUOTES_RE
)

# Clean quoted text for tokens
def strip_quoted_text(effect: str) -> str:
    return CLEAN_QUOTES_RE.sub("", effect)

# Parse token ownership
def get_token_owner(clause: str) -> str:
    if 'you create' in clause or 'under your control' in clause:
        return 'you'
    
    if OPPONENT_RE.search(clause):
        return 'opponent'

    return 'you'

# Get power/toughness of created tokens
def extract_pt(clause: str):
    return PT_RE.findall(clause)


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
def get_token_count(clause: str) -> int:
    if not TOKEN_EVENT_RE.search(clause):
        return 0
    
    matches = QUANTITY_RE.findall(clause)
    
    total = 0
    for m in matches:
        if m.isdigit():
            total += int(m)
        else:
            total += WORD_TO_NUM.get(m, 1)
    
    if total == 0:
        return 1
    
    return total

def has_tokens(ability: Ability) -> dict[str, int]:

    effect = strip_quoted_text(ability.normalized_effect())
    clauses = get_clauses(effect)
    
    total = 0
    
    for clause in clauses:
        if not CREATURE_TOKEN_RE.search(clause):
            continue
        
        owner = get_token_owner(clause)
    
        pt_pairs = extract_pt(clause)
        pt_score = pt_value(pt_pairs)
    
        num_tokens = get_token_count(clause)
        pt_total += pt_score * num_tokens
    
        if owner == 'you':
            total += pt_total
        else:
            total -= pt_total
    
    return {'token_pt_total': total}
