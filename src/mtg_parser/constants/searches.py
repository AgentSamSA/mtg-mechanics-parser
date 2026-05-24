import re

PLUS1_COUNTER_RE = re.compile(r'\+1/\+1\s+counters?', re.IGNORECASE)

TOKEN_EVENT_RE = re.compile(
    r'\bcreate(s)?\b[^.?!]*?\btoken(s)?\b', re.IGNORECASE
)
CREATURE_TOKEN_RE = re.compile(
    r'\bcreate(s)?\b[^.?!]*?\bcreature\b[^.?!]*?\btoken(s)?\b', re.IGNORECASE
)
OPPONENT_RE = re.compile(r'\bopponent(s)?\b|\beach opponent\b', re.IGNORECASE)

PT_RE = re.compile(r'(\d+|X|\*)\/(\d+|X|\*)', re.IGNORECASE)

QUANTITY_RE = re.compile(
    r'\b(a|an|one|two|three|four|five|six|seven|eight|nine|ten|x)\b(?=.*\btoken\b)',
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
    re.IGNORECASE
)

LIFE_COST_RE = re.compile(r'pay \d+ life', re.IGNORECASE)
