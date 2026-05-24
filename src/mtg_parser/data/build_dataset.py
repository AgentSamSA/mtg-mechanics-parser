"""mtg-mechanics-parser dataset builder.

Calls build_clean_dataset() and saves the cleaned file to disk."""


from mtg_parser.data.cleaning import build_clean_dataset

from mtg_parser.utils.paths import RAW_DIR, PROCESSED_DIR

def save_cleaned_dataset():
    merged = build_clean_dataset(
        creatures_path=RAW_DIR / 'creatures_full.ndjson',
        combined_points_path=RAW_DIR / 'combined_csv_pts.csv',
    )

    merged.to_csv(PROCESSED_DIR / 'combined_points_cleaned.csv', index=False)

    print('[builder] Saved combined_points_cleaned.csv to /data/processed/')
    
if __name__ == '__main__':
    save_cleaned_dataset()