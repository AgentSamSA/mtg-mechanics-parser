# Major Bug fixed
1. In tokens.py, the get_token_count function mistakenly treats “1/1” as two separate tokens. For example, in the text:
<img width="1097" height="122" alt="Screenshot 2026-05-25 at 11 23 31 PM" src="https://github.com/user-attachments/assets/63b8e3b8-11d4-4225-b8c6-e9db745b6820" />
the correct token count should be 1, but get_token_count returns 3 instead. As a result, the generated vector incorrectly contains a value of 6.
Fixed this by filtering out text in the “P/T” format.

2. In Searches.py, the OPP_DAMAGE_RE didn't involve the case like 'deals 2 damages to each player'.
<img width="1165" height="226" alt="Screenshot 2026-05-25 at 11 33 03 PM" src="https://github.com/user-attachments/assets/80833f31-20b2-46d9-8cea-df5a7946ac2f" />
Fixed this by adding 'each player' in the OPP_DAMAGE_RE. the damage.py will see if this is a damage or not.

# mtg-mechanics-parser
An automated mechanics parser and scoring system for creature cards in Magic: The Gathering.

```
git clone https://github.com/AgentSamSA/mtg-mechanics-parser.git
cd your-repo
pip install -e .
```

## Completed
- [x] Initial repository setup
- [x] Data pipeline built

## TODO
- [X] Modify existing criteria into more formal structures
- [X] Convert orcale text into structured mechanics/features
- [X] Construct mechanics vectors from our structured mechanics
- [X] Translate rubric into code to apply mechanics vectors to our dataset
- [ ] Test built components (data pipeline/parser/feature builder/scorer)
- [ ] Evaluate automated scores against manual scores
- [ ] Perform modeling with our automated structure and expand the dataset
  - [ ] Polynomial regression
  - [ ] Residual analysis
  - [ ] Trend fitting over time (set/year)

## Architecture
`src/mtg_parser`
- [x] `data`
- [X] `parser` (Criteria fully implemented via feature extractors)
- [x] `scorer` (initial version: P/T + keywords; oracle-text scoring is a placeholder until the parser lands)
- [x] `utils`
