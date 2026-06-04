"""mtg-mechanics-parser power/toughness scorer.

Use numeric values from dataset to score power/toughness."""


# Bonuses for higher power values
def power_bonus(power: float) -> float:
    if power >= 20:
        return 5
    elif power >= 10:
        return 4
    elif power >= 7:
        return 3
    elif power >= 5:
        return 2
    elif power >= 4:
        return 1
    else:
        return 0


def score_pt(power: float, toughness: float, power_from_cmc: bool) -> float:
    base = power + toughness
    
    if power_from_cmc:
        return base
    
    return base + power_bonus(power)