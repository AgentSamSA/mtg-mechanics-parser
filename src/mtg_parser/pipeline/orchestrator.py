"""mtg-mechanics-parser pipeline orchestrator."""


from mtg_parser.pipeline.build_context import build_card_context
from mtg_parser.pipeline.extract_ability_blocks import extract_blocks

# Process dataset and retrieve ability blocks
def process_dataset(df):
    results = []
    
    for _, row in df.iterrows():
        card = build_card_context(row)
        
        blocks = extract_blocks(
            row['oracle_text'],
            card['keywords']
        )
        
        results.append(blocks)
    
    return results