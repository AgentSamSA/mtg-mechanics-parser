import re

TRIGGER_RE = re.compile(r'^(Whenever|When|At)\b', re.IGNORECASE)

PLUS1_COUNTER_RE = re.compile(r'\+1/\+1\s+counters?', re.IGNORECASE)

TOKEN_EVENT_RE = re.compile(
    r'\bcreate(s)?\b.*\btoken(s)?\b', re.IGNORECASE
)
CREATURE_TOKEN_RE = re.compile(
    r'\bcreate(s)?\b.*\bcreature\b.*\btoken(s)?\b', re.IGNORECASE
)
OPPONENT_RE = re.compile(r'\bopponent(s)?\b|\beach opponent\b', re.IGNORECASE)

PT_RE = re.compile(r'(\d+|X|\*)\/(\d+|X|\*)', re.IGNORECASE)

QUANTITY_RE = re.compile(
    r'\b(a|an|one|two|three|four|five|six|seven|eight|nine|ten|x|\d+)\b',
    re.IGNORECASE,
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
    'x': 1,
}

LIMITER_RE = re.compile(
    r'\{t\}|\{q\}|tap|untap|sacrifice|exile|discard|return|\{.*?\}',
    re.IGNORECASE,
)
LIFE_COST_RE = re.compile(r'pay \d+ life', re.IGNORECASE)

CREATURE_RE = re.compile(r'\bcreature(s)?\b', re.IGNORECASE)

ZONE_PATTERNS = [
    r'\bgraveyard\b',
    r'\blibrary\b',
    r'\bhand\b',
    r'\bexile\b',
    r'\bbattlefield\b',
    r'\breveal(ed)?\b',
    r'\bput .* into\b',
    r'\bshuffle\b',
    r'\bthis way\b',
]

QUANTIFIER_PATTERNS = [
    r'\ball creatures\b',
    r'\bother creatures\b',
    r'\beach creature\b',
    r'\bcreatures you control\b',
    r'\beach player\b',
    r'\ball players\b',
    r'\beach opponent\b',
    r'\bopponents\b',
]

HAND_GAIN_PATTERNS = [
    r'\bdraw(s)?\b',
    r'\bput(s)? .* into .* hand(s)?\b',
    r'\breturn(s)? .* from (the ) graveyard(s)?\b.*\bto (your|their|owner\'s) hand(s)?\b',
]
HAND_LOSS_PATTERNS = [r'\discard(s)?\b']

REANIMATE_RE = re.compile(
    r'\b(return|put)(s)?\b.*\bgraveyard(s)?\b.*\b(battlefield|play)(s)?\b',
    re.IGNORECASE,
)

IMPULSE_DRAW_RE = re.compile(
    r'\byou may (cast|play)\b.*\bexiled\b|\bexile\b.*\byou may (cast|play)\b',
    re.IGNORECASE,
)

ALL_PLAYERS_RE = re.compile(
    r'\beach player\b|\ball players\b',
    re.IGNORECASE,
)

DESTROY_RE = re.compile(
    r'\b(destroy|exile)\b.*\btarget\b(?!.*\byou control\b)'
)
DESTROY_MASS_RE = re.compile(
    r'\b(destroy|exile)\b.*\b(all|each)\b(?!.*\byou control\b)'
)

DAMAGE_RE = re.compile(r'\bdeal(s)?.*\bdamage\b', re.IGNORECASE)
OPP_DAMAGE_RE = re.compile(r'\b(any target|that player|target opponent|each opponent)\b')
SELF_ONLY_RE = re.compile(r'\byou\b.*\bdamage\b|\bdeal(s)?\b.*\byou\b')

BOUNCE_RE = re.compile(
    r'\breturn\b.*\bto (its owner\'s|their|your) hand\b',
    re.IGNORECASE
)
TOP_LIBRARY_RE = re.compile(
    r'\bput\b.*\bon top of (its owner\'s|their|your) library\b',
    re.IGNORECASE
)

MINUS_X_RE = re.compile(
    r'\b(target|creature)\b.*\bget(s)? -\d+/-\d+\b',
    re.IGNORECASE
)
MINUS_X_MASS_RE = re.compile(
    r'\b(each|all)\b.*\bget(s)? -\d+/-\d+\b',
    re.IGNORECASE
)

MANA_SYMBOL_RE = re.compile(r'\{([^}]+)\}', re.IGNORECASE)
ANY_COLOR_RE = re.compile(r'\badd\b.*\bany\b.*\bcolor(s)?\b')
COST_REDUCTION_RE = re.compile(r'cost.*less to cast', re.IGNORECASE)

ADD_RE = re.compile(r'\badd\b', re.IGNORECASE)
OR_RE = re.compile(r'\bor\b', re.IGNORECASE)
OR_SPLIT_RE = re.compile(r'\s+\bor\b\s+', re.IGNORECASE)

CLEAN_QUOTES_RE = re.compile(r"'.*?'|\".*?\"", re.IGNORECASE)

CLAUSES_RE = re.compile(r'\.\s+|\bthen\b', re.IGNORECASE)
SUBCLAUSE_RE = re.compile(
    r'\band\b(?=\s+(you|target|each|all|an|a|\d))', re.IGNORECASE
)
