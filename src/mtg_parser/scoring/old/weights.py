"""Tunable scoring weights.

All values are PROVISIONAL placeholders pending the rubric in
'MTG Power Score Criteria.docx' and the oracle-text parser. Do not
retune from eval residuals yet -- see notebooks/scoring_evaluation.ipynb.
"""

PT_WEIGHTS = {
    'power': 1.0,
    'toughness': 1.0,
    'cmc_discount': -0.5,
}

PT_SCORE_FLOOR = 0.0
PT_SCORE_CEILING = 20.0

DEFAULT_KEYWORD_WEIGHT = 1.0

KEYWORD_WEIGHTS = {
    # Evasion
    'Flying': 2.0,
    'Shadow': 2.0,
    'Skulk': 1.5,
    'Menace': 1.5,
    'Unblockable': 3.0,
    # Protection / resilience
    'Hexproof': 2.5,
    'Shroud': 2.0,
    'Indestructible': 3.0,
    'Ward': 1.5,
    'Protection': 2.5,
    # Combat
    'First strike': 1.5,
    'Double strike': 2.5,
    'Deathtouch': 2.0,
    'Trample': 1.5,
    'Lifelink': 1.5,
    'Vigilance': 1.0,
    'Reach': 0.5,
    # Speed
    'Haste': 1.5,
    'Flash': 1.5,
    # Utility
    'Prowess': 1.0,
    'Convoke': 1.0,
    # Drawback
    'Defender': -1.5,
    'Banding': 0.0,
}

# Populated once the parser emits structured oracle features.
ORACLE_FEATURE_WEIGHTS: dict[str, float] = {}

CATEGORY_WEIGHTS = {
    'pt': 1.0,
    'keyword': 1.0,
    'oracle': 1.0,
}
