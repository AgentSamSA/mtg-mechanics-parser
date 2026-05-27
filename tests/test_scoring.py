"""Scoring tests: representative creatures -> expected rubric scores.

Each case pins one rubric rule (or a previously-fixed bug) so a regression
is easy to spot. Scores are checked as (pt, keyword, ability, total)."""


import pandas as pd
import pytest

from mtg_parser.pipeline.orchestrator import build_card_records
from mtg_parser.scoring import score_card


# Build a one-row dataframe for a single creature
def make_row(power, toughness, cmc, keywords, oracle_text):
    return pd.DataFrame([{
        'oracle_id': 'test',
        'name': 'Test Card',
        'set': 'tst',
        'set_name': 'Test',
        'released_at': pd.Timestamp('2024-01-01'),
        'power': power,
        'toughness': toughness,
        'power_numeric': float(cmc) if power == '*' else float(power),
        'toughness_numeric': float(cmc) if toughness == '*' else float(toughness),
        'keywords': keywords,
        'oracle_text': oracle_text,
    }])


# Score one creature and return (pt, keyword, ability, total)
def score(power, toughness, cmc, keywords, oracle_text):
    record = build_card_records(make_row(power, toughness, cmc, keywords, oracle_text))[0]
    s = score_card(record.features)
    return (s.pt, s.keyword, s.ability, s.total)


# id, (power, toughness, cmc, keywords, oracle_text), (pt, keyword, ability, total)
CASES = [
    ('vanilla', ('2', '2', 2, [], ''), (4, 0, 0, 4)),
    ('flying_keyword', ('2', '2', 2, ['Flying'], 'Flying'), (4, 1, 0, 5)),
    ('mana_ability_excluded_from_activated', ('0', '1', 1, ['Flying'],
        'Flying\n{T}: Add one mana of any color.'), (1, 1, 2, 4)),
    ('enters_draw_stacks', ('2', '2', 3, [],
        'When this creature enters, draw a card.'), (4, 0, 3, 7)),
    ('dies_has_no_special_bonus', ('2', '2', 3, [],
        'When this creature dies, draw a card.'), (4, 0, 2, 6)),
    ('repeatable_attack_trigger', ('2', '2', 3, [],
        'Whenever this creature attacks, draw a card.'), (4, 0, 3, 7)),
    ('search_and_plus1_counter', ('2', '2', 3, [],
        'When this creature enters, search your library for a card, '
        'then put a +1/+1 counter on it.'), (4, 0, 4, 8)),
    ('opponent_discard', ('2', '2', 3, [],
        'When this creature enters, target opponent discards a card.'), (4, 0, 3, 7)),
    ('token_maker', ('3', '3', 4, ['Haste'],
        'Haste\nWhen this creature enters, create a 1/1 white Soldier creature token.'),
        (6, 2, 4, 12)),
    ('star_pt_uses_cmc_no_bonus', ('*', '*', 6, [], ''), (12, 0, 0, 12)),
    ('defender_net_zero', ('0', '4', 2, ['Defender'], 'Defender'), (4, 0, 0, 4)),
]


@pytest.mark.parametrize(
    'card, expected',
    [(c[1], c[2]) for c in CASES],
    ids=[c[0] for c in CASES],
)
def test_score_card(card, expected):
    assert score(*card) == expected
