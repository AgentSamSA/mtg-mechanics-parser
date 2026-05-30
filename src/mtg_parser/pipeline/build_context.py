"""mtg-mechanics-parser card context builder.

Identify different text contexts for oracle text.
Separates out keyword-only blocks from the rest of oracle text."""


from mtg_parser.parsing.keyword_router import build_card_keywords


def build_card_context(row):
    return {
        'oracle_text': row['oracle_text'],
        'keywords': build_card_keywords(row),
    }
