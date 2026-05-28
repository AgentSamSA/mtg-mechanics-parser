"""mtg-mechanics-parser pipeline orchestrator.

Takes in our cards dataframe, builds card contexts, then obtains blocks.
Filters out blocks that only contain keywords."""


from mtg_parser.parsing.ability import parse_ability

from mtg_parser.pipeline.build_context import build_card_context
from mtg_parser.pipeline.extract_ability_blocks import extract_blocks

from mtg_parser.pipeline.card_ability_bundle import CardAbilityBundle

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
