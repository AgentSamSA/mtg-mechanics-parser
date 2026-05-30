"""mtg-mechanics-parser token features extraction."""


from mtg_parser.parsing.ability import Ability

from mtg_parser.features.utils.parsing import get_clauses, strip_quoted_text
from mtg_parser.features.utils.token_utils import (
    get_token_owner,
    get_token_count,
    extract_pt,
    pt_value
)

from mtg_parser.constants.searches import CREATURE_TOKEN_RE


def has_tokens(ability: Ability) -> dict[str, int]:

    effect = strip_quoted_text(ability.normalized_effect())
    clauses = get_clauses(effect)

    total = 0

    for clause in clauses:
        if not CREATURE_TOKEN_RE.search(clause):
            continue

        owner = get_token_owner(clause)

        pt_pairs = extract_pt(clause)
        pt_score = pt_value(pt_pairs)

        num_tokens = get_token_count(clause)
        pt_total = pt_score * num_tokens

        if owner == 'you':
            total += pt_total
        else:
            total -= pt_total

    return {'token_pt_total': total}
