"""mtg-mechanics-parser feature extraction helper utilities."""


from mtg_parser.constants.searches import (
    CLAUSES_RE,
    SUBCLAUSE_RE,
    QUANTITY_RE,
    WORD_TO_NUM,
    NON_SCORING_RE,
    OPPONENT_RE,
    ALL_PLAYERS_RE,
    MANA_SYMBOL_RE,
    ANY_COLOR_RE,
    ADD_RE,
    COLON_OUTSIDE_QUOTES,
    OR_SPLIT_RE
)

# Get clauses within each ability from oracle text
def get_clauses(text: str) -> list[str]:
    clauses = CLAUSES_RE.split(text)

    final = []
    for c in clauses:
        parts = SUBCLAUSE_RE.split(c)
        final.extend(parts)

    return [p.strip() for p in final if p.strip()]

# Get total value from text
def get_count_from_text(clause: str) -> int:
    matches = QUANTITY_RE.findall(clause)

    total = 0
    for m in matches:
        if m.isdigit():
            total += int(m)
        else:
            total += WORD_TO_NUM.get(m, 1)

    return total

# Get non-scoring abilities from text
def is_non_scoring(text: str) -> bool:
    return bool(NON_SCORING_RE.search(text))

# Check ability target (you or opponent)
def classify_target(clause: str) -> int:
    if OPPONENT_RE.search(clause):
        return -1
    
    return 1

# See if all players are affected by ability
def is_all_players_effect(clause: str) -> bool:
    return bool(ALL_PLAYERS_RE.search(clause))

# Compute the amount of mana produced
def count_mana_base(clause: str) -> int:
    symbols = MANA_SYMBOL_RE.findall(clause)
    
    if symbols:
        return len(symbols)
    
    return get_count_from_text(clause)

# Check if ability is mana producing
def is_mana_producing(clause: str) -> bool:
    return ADD_RE.search(clause) and count_mana_base(clause) > 0

# Check if ability can produce any color mana
def has_any_color_mana(clause: str) -> bool:
    return ANY_COLOR_RE.search(clause) is not None

# Ensure activated ability is outside of granted ability
def is_top_level_activated(block: str) -> bool:
    return bool(COLON_OUTSIDE_QUOTES.search(block))

# Get all mana options from mana ability
def extract_mana_options(clause: str) -> list[int]:
    parts = OR_SPLIT_RE.split(clause)
    
    return [count_mana_base(p) for p in parts]
