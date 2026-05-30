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