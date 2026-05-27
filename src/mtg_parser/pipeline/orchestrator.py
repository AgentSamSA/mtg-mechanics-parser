"""mtg-mechanics-parser pipeline orchestrator.

Takes in our cards dataframe, builds card contexts, then obtains blocks.
Filters out blocks that only contain keywords."""


from mtg_parser.parsing.ability import parse_ability

from mtg_parser.pipeline.build_context import build_card_context
from mtg_parser.pipeline.extract_ability_blocks import extract_blocks

# Process dataset and retrieve ability blocks
def process_dataset(df):
    abilities = []
    
    for _, row in df.iterrows():
        card = build_card_context(row)
        
        blocks = extract_blocks(
            row['oracle_text'],
            card['keywords']
        )
        
        for block in blocks:
            abilities.append(parse_ability(block))
    
    return abilities