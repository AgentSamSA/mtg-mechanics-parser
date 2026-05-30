"""mtg-mechanics-parser token features helper utilities."""


from mtg_parser.constants.searches import (
    OPPONENT_RE,
    PT_RE,
    TOKEN_EVENT_RE,
    QUANTITY_RE,
    WORD_TO_NUM
)

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

    clause = PT_RE.sub('', clause)

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
