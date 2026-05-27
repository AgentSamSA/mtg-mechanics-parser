"""mtg-mechanics-parser card scorer.

Scores each card based on power/toughness, keywords, and abilities."""

from mtg_parser.scoring.ability_scorer import score_abilities
from mtg_parser.scoring.keyword_scorer import score_keywords
from mtg_parser.scoring.pt_scorer import score_pt

from mtg_parser.scoring.models.card_score import CardScore
from mtg_parser.features.card_features import CardFeatures

def score_card(card: CardFeatures) -> CardScore:
    return CardScore(
        ability=score_abilities(card.abilities),
        keyword=score_keywords(card.keyword_features),
        pt=score_pt(card.power, card.toughness)
    )