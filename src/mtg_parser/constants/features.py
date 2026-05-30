"""mtg-mechanics-parser feature-relevant constants.

Contains either features, feature weights, or the feature pipeline initialization."""


from mtg_parser.features.extractors.activated import activated_features
from mtg_parser.features.extractors.bounce import has_bounce
from mtg_parser.features.extractors.card_advantage import card_advantage
from mtg_parser.features.extractors.damage import has_direct_damage
from mtg_parser.features.extractors.destroy import has_destroy
from mtg_parser.features.extractors.global_effects import has_global
from mtg_parser.features.extractors.impulse_draw import has_impulse_draw
from mtg_parser.features.extractors.mana_production import mana_production
from mtg_parser.features.extractors.minus_xx import has_minus_X
from mtg_parser.features.extractors.reanimate import has_reanimate
from mtg_parser.features.extractors.special import special_features
from mtg_parser.features.extractors.static import static_features
from mtg_parser.features.extractors.tokens import has_tokens
from mtg_parser.features.extractors.triggered import triggered_features
from mtg_parser.features.extractors.keyword_counters import keyword_counter_features

from mtg_parser.features.feature_extractor import AbilityFeaturePipeline


FEATURES = [
    activated_features,
    has_bounce,
    card_advantage,
    has_direct_damage,
    has_destroy,
    has_global,
    has_impulse_draw,
    mana_production,
    has_minus_X,
    has_reanimate,
    special_features,
    static_features,
    has_tokens,
    triggered_features,
    keyword_counter_features
]

FEATURE_WEIGHTS = {
    'baseline_score': 1,
    'has_search': 1,
    'plus1_counter': 1,
    'enters_trigger': 1,
    'dies_trigger': 1,
    'repeatable_trigger': 1,
    'token_pt_total': 1,
    'activated_limiter': 1,
    'activated_no_limiter': 2,
    'has_global': 1,
    'card_advantage': 1,
    'has_recursion_battlefield': 1,
    'has_exile_access': 1,
    'has_destroy': 1,
    'has_mass_destroy': 2,
    'has_bounce': 1,
    'has_deck_stack': 2,
    'has_minus_X': 1,
    'has_mass_minus_X': 2,
    'mana_produced': 1,
    'mana_reduction': 1,
    'has_direct_damage': 1,
    'keyword_counters': 1
}

KEYWORD_WEIGHTS = {
    'haste': 2,
    'double_strike': 2,
    'deathtouch': 2,
    'protection': 2,
    'indestructible': 2,
    'hexproof': 2,
    'offspring': 3,
    'defender': -1
}

ABILITY_PIPELINE = AbilityFeaturePipeline(FEATURES)