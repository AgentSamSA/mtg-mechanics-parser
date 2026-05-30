"""mtg-mechanics parser regex search library.

Stores various regex searches for parsing and feature extraction."""


import re

ABILITY_WORD_RE = re.compile(r'^[^—–—]+[—–]\s*')

TRIGGER_RE = re.compile(r'(?:^|—)\s*(Whenever|When|At)\b', re.IGNORECASE)

PLUS1_COUNTER_RE = re.compile(
    r'\b(put|place|get)\b.*\+1/\+1\s+counters?', re.IGNORECASE
)
PLUS_STAT_RE = re.compile(
    r'\+\d+/\+\d+|gets \+\d+/\+\d+|power and toughness',
    re.IGNORECASE
)

TOKEN_EVENT_RE = re.compile(r'\bcreates?\b.*\btokens?\b', re.IGNORECASE)
CREATURE_TOKEN_RE = re.compile(
    r'\bcreates?\b.*\bcreature\b.*\btokens?\b', re.IGNORECASE
)
OPPONENT_RE = re.compile(r'\bopponents?\b|\beach opponent\b', re.IGNORECASE)

PT_RE = re.compile(r'(\d+|X|\*)\/(\d+|X|\*)', re.IGNORECASE)

QUANTITY_RE = re.compile(
    r'\b(a|an|one|two|three|four|five|six|seven|eight|nine|ten|x|\d+)\b',
    re.IGNORECASE
)
WORD_TO_NUM = {
    'a': 1,
    'an': 1,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'x': 1
}

LIMITER_RE = re.compile(
    r'\{t\}|\{q\}|tap|untap|sacrifice|exile|discard|return|\{.*?\}',
    re.IGNORECASE
)
LIFE_COST_RE = re.compile(r'pay \d+ life', re.IGNORECASE)

CREATURE_RE = re.compile(r'\bcreatures?\b', re.IGNORECASE)

ZONE_PATTERNS = [
    r'\bgraveyard\b',
    r'\blibrary\b',
    r'\bhand\b',
    r'\bexile\b',
    r'\bbattlefield\b',
    r'\breveal(ed)?\b',
    r'\bput .* into\b',
    r'\bshuffle\b',
    r'\bthis way\b'
]

QUANTIFIER_PATTERNS = [
    r'\ball creatures\b',
    r'\bother creatures\b',
    r'\beach creature\b',
    r'\bcreatures you control\b',
    r'\beach player\b',
    r'\ball players\b',
    r'\beach opponent\b',
    r'\bopponents\b'
]

DRAW_RE = re.compile(r'\bdraws?\b\s+(a\s+)?cards?\b', re.IGNORECASE)
PUT_INTO_HAND_RE = re.compile(
    r'\bputs?\b.*\binto\b.*\bhands?\b', re.IGNORECASE
)
RETURN_TO_HAND_RE = re.compile(
    r'\breturns?\b.*\bfrom (the )?graveyards?\b.*\bto (your|their|owner\'s) hands?\b',
    re.IGNORECASE
)
DISCARD_RE = re.compile(r'\discards?\b', re.IGNORECASE)

REANIMATE_RE = re.compile(
    r'\b(return|put)s?\b.*\bgraveyards?\b.*\b(battlefield|play)s?\b',
    re.IGNORECASE
)

IMPULSE_DRAW_RE = re.compile(
    r'\byou may (cast|play)\b.*\bexiled\b|\bexile\b.*\byou may (cast|play)\b',
    re.IGNORECASE
)

ALL_PLAYERS_RE = re.compile(r'\beach player\b|\ball players\b', re.IGNORECASE)

DESTROY_RE = re.compile(
    r'\b(destroy|exile)\b.*\btarget\b(?!.*\byou control\b)'
)
DESTROY_MASS_RE = re.compile(
    r'\b(destroy|exile)\b.*\b(all|each)\b(?!.*\byou control\b)'
)

DAMAGE_RE = re.compile(r'\bdeals?.*\bdamage\b', re.IGNORECASE)
LIFE_LOSS_RE = re.compile(r'\b(loses?\s+\d+\s+life|loses? life equal to|they lose.*life)\b', re.IGNORECASE)
OPP_DAMAGE_RE = re.compile(
    r'\b(any target|that player|that opponent|target opponent|each opponent)\b'
)
OTHER_DAMAGE_RE = re.compile(r'\b(they|that player|that opponent)\b', re.IGNORECASE)
SELF_ONLY_RE = re.compile(r'\byou\b.*\bdamage\b|\bdeals?\b.*\byou\b')

BOUNCE_RE = re.compile(
    r'\breturn\b.*\bto (its owner\'s|their|your) hand\b', re.IGNORECASE
)
TOP_LIBRARY_RE = re.compile(
    r'\bput\b.*\bon top of (its owner\'s|their|your) library\b', re.IGNORECASE
)

MINUS_X_RE = re.compile(
    r'\b(target|creature)\b.*\bgets? -\d+/-\d+\b', re.IGNORECASE
)
MINUS_X_MASS_RE = re.compile(
    r'\b(each|all)\b.*\bgets? -\d+/-\d+\b', re.IGNORECASE
)

MANA_SYMBOL_RE = re.compile(
    r'\{(?:[WUBRGCXPS]|\d+|[WUBRGCXPS]/[WUBRGCXPS]|\d+/[WUBRGCXPS])\}',
    re.IGNORECASE
)
ANY_COLOR_RE = re.compile(r'\badd\b.*\bmana\b.*\bany\b.*\bcolors?\b')
COST_REDUCTION_RE = re.compile(r'cost.*less to cast', re.IGNORECASE)

KEYWORD_COUNTER_RE = re.compile(
    r'\b(enters with|as this enters|choose|from among)\b.*?\b(counter|counters)\b',
    re.IGNORECASE
)
CHOOSE_N_RE = re.compile(
    r'\b(one|two|three|\d+)\s+different counters?\b', re.IGNORECASE
)

NON_SCORING_PATTERNS = [
    r"\b(this|your) creatures? can't (attack or block|attack|block)\b[.\s]*(unless.*)?",
    r'\b(this|your) creatures? enters? tapped\b',
    r'\bsacrifice (this|a) creature\b[.\s]*(unless.*)?',
    r'\bas an additional cost to cast this spell\b',
    r"'s power and toughness are each equal to\b",
    r"'s power is equal to\b",
    r"'s toughness is equal to\b",
]

NON_SCORING_RE = re.compile(
    '|'.join(f'(?:{p})' for p in NON_SCORING_PATTERNS), re.IGNORECASE
)

CHOICE_RE = re.compile(r'\byour choice of\b', re.IGNORECASE)
COUNTER_CHOICE_RE = re.compile(
    r'(enters with.*counter|choose.*counter|from among.*counter)',
    re.IGNORECASE
)
FROM_AMONG_RE = re.compile(r'\bfrom among\b\s+(.*)?', re.IGNORECASE)

ADD_RE = re.compile(r'\badd\b', re.IGNORECASE)
OR_RE = re.compile(r'\bor\b', re.IGNORECASE)
OR_SPLIT_RE = re.compile(r'\s+\bor\b\s+', re.IGNORECASE)

CLEAN_QUOTES_RE = re.compile(r"'.*?'|\".*?\"", re.IGNORECASE)

CLAUSES_RE = re.compile(r'\.\s+|\bthen\b', re.IGNORECASE)
SUBCLAUSE_RE = re.compile(
    r'\band\b(?=\s+(you|target|each|all|an|a|\d))', re.IGNORECASE
)

COLON_OUTSIDE_QUOTES = re.compile(r':(?=(?:[^"]*"[^"]*")*[^"]*$)')