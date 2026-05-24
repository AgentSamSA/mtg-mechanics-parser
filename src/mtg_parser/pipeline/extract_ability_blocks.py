"""mtg-mechanics-parser ability block extractor.

Lexer to split unstructured oracle text into ability blocks
to parse specific ability types."""


from mtg_parser.utils.text_preprocessing import preprocess_oracle_text
from mtg_parser.parsing.keyword_router import is_keyword_line

# Extract ability blocks from the oracle text
def extract_blocks(text: str, card_keywords):
    text = preprocess_oracle_text(text)
    
    blocks = []
    for line in text.split('\n'):
        if not line.strip():
            continue
        
        if is_keyword_line(line, card_keywords):
            continue
        
        blocks.append(line)
    
    return blocks

test = """{T}: Add {U}{R}. Spend this mana only to cast noncreature spells.
Whenever you cast a noncreature spell, draw a card.
Creatures can't be sacrificed."""

test2 = """Other Knights you control get +1/+1.

Whenever you gain life, add a +1/+1 counter to this creature.  
Sacrifice a creature: Other Knights you control gain +2/+2 until end of turn.
{2G}{T}: Draw 2 cards."""

test3 = """
Landfall — When a land enters under your control, gain {W}.

Big Beast gains +1/+1 for each other Beast you control.
When a Beast you control enters, gain 3 life.

Pay 3 life: draw a card.
{3}: Big Beast gains +3/+3 until end of turn. Activate only as a sorcery.

Whenever Big Beast deals combat damage to a player, choose target creature that player controls. The player sacrifices that creature.

Beasts you control gain +1/+1.

Humans opponents control lose -1/-1.

"""


if __name__ == '__main__':
    print(extract_blocks(test3))
