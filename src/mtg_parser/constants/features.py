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
]
