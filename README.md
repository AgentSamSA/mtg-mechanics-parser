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
