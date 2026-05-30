"""mtg-mechanics-parser keyword scorer.

Use KeywordFeatures to score keyword value based on keyword weights."""


from mtg_parser.features.keyword_features import KeywordFeatures

from mtg_parser.constants.features import KEYWORD_WEIGHTS


def score_keywords(kf: KeywordFeatures) -> int:
    return sum(
        count * KEYWORD_WEIGHTS.get(k, 1) for k, count in kf.features.items()
    )