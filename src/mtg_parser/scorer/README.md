# Current Scoring Status

Implemented:

- Power/toughness scoring
- Keyword scoring
- Modular scorer structure
- Separate subscores:
  - pt_score
  - keyword_score
  - oracle_score
  - total_power_score

Current scorer shows strong correlation with manual scores even before oracle-text parsing:

- Pearson r ≈ 0.85
- Spearman ρ ≈ 0.82

Known limitation:

- Oracle/rules-text mechanics are not yet parsed.
