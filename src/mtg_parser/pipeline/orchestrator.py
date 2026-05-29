"""mtg-mechanics-parser pipeline orchestrator.

Takes in our cards dataframe, builds card contexts, then obtains blocks.
Filters out blocks that only contain keywords.
Returns a CardAbilityBundle object containing relevant metadata and a list of Ability objects."""


from mtg_parser.parsing.ability import parse_ability

from mtg_parser.pipeline.build_context import build_card_context
from mtg_parser.pipeline.extract_ability_blocks import extract_blocks

from mtg_parser.pipeline.card_ability_bundle import CardAbilityBundle

# Process row in the dataset and retrieve ability blocks
def build_card_ability_bundle(row):
    card = build_card_context(row)

    blocks = extract_blocks(row['oracle_text'], card['keywords'])

    abilities = [parse_ability(b) for b in blocks]

    return(CardAbilityBundle
        (
            oracle_id=row['oracle_id'],
            name=row['name'],
            set=row['set'],
            set_name=row['set_name'],
            released_at=row['released_at'],
            cmc=row['cmc'],
            abilities=abilities
        )
    )

def extract_abilities(df):
    return [
        build_card_ability_bundle(row)
        for _, row in df.iterrows()
    ]
