"""mtg-mechanics-parser data cleaning script.

Takes the creatures-full dataset and cleans it for analysis."""

import pandas as pd

# Define features we are interested in
SCRYFALL_COLS = [
    'oracle_id',
    'name',
    'set',
    'released_at',
    'cmc',
    'power',
    'toughness',
    'oracle_text',
    'keywords',
    'color_identity',
    'rarity',
]

POINTS_COLS = ['name', 'set', 'set_name', 'points']


def build_clean_dataset(
    creatures_path: str, combined_points_path: str
) -> pd.DataFrame:

    # Load data
    creatures_full = pd.read_json(creatures_path, lines=True)

    combined_points = pd.read_csv(combined_points_path)

    combined_points = combined_points[POINTS_COLS]

    # Remove duplicates
    creatures_full['arena_priority'] = (
        creatures_full['arena_id'].notna().astype(int)
    )

    creatures_full = creatures_full.sort_values(by='arena_priority')

    creatures_full = creatures_full.drop_duplicates(
        subset=['name', 'set'], keep='first'
    )

    creatures_subset = creatures_full[SCRYFALL_COLS]

    # Merge
    merged = combined_points.merge(
        creatures_subset,
        on=['name', 'set'],
        how='left',
    )

    merged['oracle_text'] = merged['oracle_text'].fillna('')

    # Convert to dates
    merged['released_at'] = pd.to_datetime(
        merged['released_at'], errors='coerce'
    )

    merged['year'] = merged['released_at'].dt.year

    # Get numeric power/toughness values
    merged['power_numeric'] = pd.to_numeric(merged['power'], errors='coerce')

    merged['toughness_numeric'] = pd.to_numeric(
        merged['toughness'], errors='coerce'
    )

    column_order = [
        'oracle_id',
        'name',
        'set',
        'set_name',
        'released_at',
        'year',
        'cmc',
        'power',
        'toughness',
        'power_numeric',
        'toughness_numeric',
        'keywords',
        'oracle_text',
        'color_identity',
        'rarity',
        'points',
    ]

    merged = merged[column_order]

    # Diagnostics
    missing = merged['oracle_id'].isna().sum()

    print(f'[cleaning] Missing oracle_id rows: {missing}')

    dupes = merged.duplicated(subset=['name', 'set']).sum()

    print(f'[cleaning] Duplicate values in rows: {dupes}')

    return merged


if __name__ == '__main__':
    build_clean_dataset()
