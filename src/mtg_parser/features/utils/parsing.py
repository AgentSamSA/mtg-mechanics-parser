"""mtg-mechanics-parser oracle text parsing helper utilities."""


from mtg_parser.constants.searches import (
    CLAUSES_RE,
    SUBCLAUSE_RE,
    QUANTITY_RE,
    WORD_TO_NUM,
    NON_SCORING_RE,
    OPPONENT_RE,
    ALL_PLAYERS_RE,
    CLEAN_QUOTES_RE,
    COLON_OUTSIDE_QUOTES,
    CHOICE_RE,
    FROM_AMONG_RE,
    ENTERS_CHOICE_RE
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


# Ensure activated ability is outside of granted ability
def is_top_level_activated(block: str) -> bool:
    return bool(COLON_OUTSIDE_QUOTES.search(block))


# Check ability target (you or opponent)
def classify_target(clause: str) -> int:
    if OPPONENT_RE.search(clause):
        return -1

    return 1


# See if all players are affected by ability
def is_all_players_effect(clause: str) -> bool:
    return bool(ALL_PLAYERS_RE.search(clause))


# Strip text inside quotes
def strip_quoted_text(effect: str) -> str:
    return CLEAN_QUOTES_RE.sub('', effect)

# Identify if ability involves choice (is modular)
def is_modular(text: str) -> bool:
    return bool(
        CHOICE_RE.search(text)
        or FROM_AMONG_RE.search(text)
        or ENTERS_CHOICE_RE.search(text)
    )