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

# Star power/toughness uses the CMC value with no bonus applied
def score_pt(power: float, toughness: float, power_is_star: bool = False) -> float:
    bonus = 0 if power_is_star else power_bonus(power)

    return power + toughness + bonus