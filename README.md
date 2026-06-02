# mtg-mechanics-parser

mtg-mechanics-parser is a rule-based parsing and scoring system for creature cards in *Magic: The Gathering*.

The project transforms raw card data from [Scryfall](https://scryfall.com/) into structured gameplay features by parsing a card's oracle text, identifying game mechanics, extracting quantitative features, and assigning a weighted power score.

Unlike traditional tabular datasets, Magic card text contains highly varied natural-language descriptions of game actions, triggered events, costs, restrictions, and continuous effects. As a result, evaluating card strength is a notoriously difficult task even for the most experienced of *Magic* players, requiring interpretation of the mechanics embedded within the card text itself.

To address this challenge, this project implements a complete processing pipeline from scratch:

* Dataset cleaning and building
* Oracle text parsing
* Ability segmentation and classification
* Mechanic-specific feature extraction
* Feature vector generation
* Weighted card scoring

The parser currently analyzes creature cards and detects a wide range of gameplay mechanics including removal, card advantage, token generation, mana production, reanimation, counters, triggered abilities, activated abilities, and global effects.

The resulting feature representations can be used for card evaluation, dataset analysis, machine learning experiments, and gameplay complexity research.

## Why This Project Exists

*Magic: The Gathering* contains tens of thousands of unique cards whose functionality is primarily expressed through natural-language oracle text.

While datasets such as Scryfall provide extensive card metadata, many important gameplay characteristics are not available as structured features. For example, determining whether a card generates card advantage, creates tokens, removes opposing permanents, or reanimates creatures often requires interpreting the card's rules text.

By converting card text into structured mechanic-level features, those nuanced gameplay characteristics can be analyzed computationally.

The long-term goal is to provide a foundation for card evaluation, power-level estimation, and machine learning models operating on gameplay-relevant card characteristics.

## Setup
```
git clone https://github.com/AgentSamSA/mtg-mechanics-parser.git
cd mtg-mechanics-parser
pip install -e .
```

To run this in a virtual python environment:
```
python -m venv .venv
source .venv/bin/activate
```

## System Pipeline

mtg-mechanics-parser processes _Magic: The Gathering_ card data from Scryfall and converts a card's oracle text into structured gameplay features that can be used to estimate card power.

```text
Raw Scryfall Data
        ↓
Creature Card Filtering
        ↓
Dataset Cleaning
        ↓
Ability Parsing
        ↓
Card Object Construction
        ↓
Feature Extraction
        ↓
Feature Scoring
        ↓
Final Card Power Score
```

### Stage 1: Data Preparation

Raw card data is downloaded from Scryfall and is filtered to include only creature cards. The dataset is then cleaned to remove unnecessary fields, invalid records, and filter down to only the columns we are interested in.

### Stage 2: Ability Parsing

Oracle text is segmented into individual ability blocks and converted into structured Ability objects. This separates activated abilities, triggered abilities, and static abilities for downstream processing.

### Stage 3: Card Object Construction

Relevant card information such as mana cost, power/toughness, keywords, and parsed abilities is assembled into a unified Card object that is passed through the extraction pipeline.

### Stage 4: Feature Extraction

Feature extractors analyze card text and identify gameplay mechanics such as:

* Card draw
* Token generation
* Mana production
* Removal effects
* Reanimation
* Damage effects
* Global effects
* Counter placement
* Activated abilities
* Triggered abilities

Each extractor produces structured feature values that quantify the complexity and gameplay impact of the card.

### Stage 5: Scoring

Extracted features are converted into weighted scores using predefined scoring rules. Individual component scores are combined into a final card power score.

The resulting score can be used for downstream analysis, comparison, and evaluation of creature card power level.

## Project Structure
```
data/
  processed/                     # Processed dataset
  raw/                           # Raw dataset sources from Scryfall

notebooks/                       # Python notebook files

src/
  mtg-parser/
    constants/
      features_weights.py        # Weights for scoring ability features
      keyword_weights.py         # Weights for scoring keyword features
      mechanics.py               # Gameplay mechanic related constants
      searches.py                # Regex searches to identify ability features
    data/
      __init__.py                # Package initialization
      build_dataset.py           # Builds and saves cleaned dataset
      cleaning.py                # Cleans filtered dataset
      download.py                # Fetches raw dataset
      extract_creatures.py       # Extracts only creature cards from raw dataset
    features/
      extractors/
        __init__.py              # Package initialization
        activated.py             # Activated ability features
        bounce.py                # Permanent card bounce features
        card_advantage.py        #  Card advantage features
        damage.py                # Direct damage features
        destroy.py               #  Hard removal features
        global_effects.py        # Global effect features
        impulse_draw.py          # Impulsive draw features
        keyword_counters.py      # Keyword counter features
        mana_production.py       # Mana production/reduction features
        minus_xx.py              # -X/-X features
        reanimate.py             # Graveyard reanimation features
        special.py               # Special features
        static.py                # Static ability features
        tokens.py                # Creature token features
        triggered.py             # Triggered ability features
      utils/
        counter_utils.py         # Keyword counter helpers
        mana_utils.py            # Mana ability helpers
        parsing.py               # General feature text parsing helpers
        token_utils.py           # Creature token helpers
      ability_features.py        # AbilityFeatures class definition
      card_features.py           # CardFeatures class definition
      detect_zone.py             # Identify gameplay zone in text
      encode_keywords.py         # One-hot encoding keyword columns
      feature_extractor.py       # Feature extractor pipeline
      keyword_features.py        # KeywordFeatures class definition
      pattern_builder.py         # Identify global ability text patterns
      pipeline.py                # Holds feature extractor pipeline initialization
      registery.py               # Holds our feature list
    parsing/
      __init__.py                # Package initialization
      ability.py                 # Ability class definition
      keyword_router.py          # Keyword line identifier
    pipeline/
      __init__.py                # Package initialization
      build_context.py           # Build card context from row
      card_ability_bundle.py     # CardAbilityBundle class definition
      extract_ability_blocks.py  # Get ability blocks from text
      orchestrator.py            # Pipeline methods to process each row
    scoring/
      models/
        ability_score.py         # AbilityScore class definition
        card_score.py            # CardScore class definition
      __init__.py                # Package initialization
      ability_scorer.py          # Score ability features for each card
      card_scorer.py             # Score combined features for each card
      keyword_scorer.py          # Score keyword features for each card
      pt_scorer.py               # Score power/toughness features for each card
    utils/
      __init__.py                # Package initialization
      normalizer.py              # Normalize keywords
      paths.py                   # Set project paths
      text_preprocessing.py      # Preprocess oracle text
```

## Package Overview

### data/

Responsible for dataset acquisition, cleaning, and preprocessing.

---

### parsing/

Responsible for converting oracle text into structured ability representations.
- Ability types are identified via an `Ability` object which parses the ability from the oracle text

---

### pipeline/

Coordinates end-to-end processing of individual cards.
- `build_context` identifies which lines of text are keyword abilities to avoid double scoring them. While Scryfall preprocesses keywords into a separate column, they retain the keywords inside oracle text
- `card_ability_bundle` defines a CardAbilityBundle object which holds certain card-level metadata and a list of Ability objects for the parsed cards
- `extract_ability_blocks` builds out the list of ability blocks to be parsed downstream

---

### features/

Responsible for extracting gameplay-relevant mechanics from card text. Outputs structured feature vectors describing card functionality.
- Each extractor inside `features/extractors` is responsible for extracting their respective feature from the ability text. For instance, `destroy.py` is responsible for extracting any removal effects (destroy/exile)
- `AbilityFeature`, `CardFeature`, and `KeywordFeature` objects are defined in order to score the cards

---

### scoring/

Converts extracted features into numeric power scores. Utilizes that card's Feature objects and weights to determine final score.

---

### constants/

Stores configuration values used throughout the project, including feature weights and feature extractor pipeline initialization.

---

### utils/

Shared utility functions used across multiple modules.
