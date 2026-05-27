"""mtg-mechanics-parser pipeline orchestrator.

Takes in our cards dataframe, builds card contexts, then obtains blocks.
Filters out blocks that only contain keywords."""


from mtg_parser.parsing.ability import parse_ability

from mtg_parser.pipeline.build_context import build_card_context
from mtg_parser.pipeline.extract_ability_blocks import extract_blocks

from mtg_parser.pipeline.card_ability_bundle import CardAbilityBundle
from mtg_parser.pipeline.card_record import CardRecord

from mtg_parser.features.card_features import CardFeatures
from mtg_parser.features.encode_keywords import build_keyword_features

# Process dataset and retrieve ability blocks
def extract_abilities(df):
    all_abilities = []

    for _, row in df.iterrows():
        card = build_card_context(row)

        blocks = extract_blocks(row['oracle_text'], card['keywords'])

        abilities = [parse_ability(b) for b in blocks]

        all_abilities.append(CardAbilityBundle
            (
                oracle_id=row['oracle_id'],
                name=row['name'],
                set=row['set'],
                set_name=row['set_name'],
                released_at=row['released_at'],
                abilities=abilities,
            )
        )

    return all_abilities


# Star/variable power has no fixed value; flagged to skip the power bonus
def is_star_power(value) -> bool:
    try:
        float(value)
        return False
    except (TypeError, ValueError):
        return True


# Process dataset and build scoring records
def build_card_records(df):
    records = []

    for _, row in df.iterrows():
        card = build_card_context(row)

        blocks = extract_blocks(row['oracle_text'], card['keywords'])

        abilities = [parse_ability(b) for b in blocks]

        features = CardFeatures(
            abilities=abilities,
            keyword_features=build_keyword_features(row),
            power=row['power_numeric'],
            toughness=row['toughness_numeric'],
            power_is_star=is_star_power(row['power']),
        )

        records.append(CardRecord
            (
                oracle_id=row['oracle_id'],
                name=row['name'],
                set=row['set'],
                set_name=row['set_name'],
                released_at=row['released_at'],
                features=features,
            )
        )

    return records
