import os
import sys
import json

from mtg_parser.utils.paths import RAW_DIR

RAW_PATH = RAW_DIR / 'default-cards.json'
CREATURES_PATH = RAW_DIR / 'creatures_full.ndjson'

def build_creatures_dataset():
    
    # Ensure raw dataset exists, otherwise download from Scryfall API
    if not os.path.exists(RAW_PATH):
        print('[pipeline] Default-cards dataset not found. Downloading...')
    
        try:
            from data.download import download_data
            download_data()
        except Exception as e:
            print('[pipeline] Download failed:', e)
            return
        
    else:
        print('[pipeline] Default-cards dataset already exists.')

    # Build the creatures dataset
    if not os.path.exists(CREATURES_PATH):
        print('[pipeline] Creatures dataset not found. Creating creatures dataset...')
        
        try:
            import ijson
        except ImportError:
            print('[pipeline] ijson not found. Installing...')
            import subprocess
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ijson'])
            import ijson

        count = 0
        
        with open(RAW_PATH, 'rb') as f, open(CREATURES_PATH, 'w') as out:
            for card in ijson.items(f, 'item'):
                if 'Creature' in card.get('type_line', ''):
                    out.write(json.dumps(card, default=float) + '\n')
                    count += 1
        
        print(f'[pipeline] Processing complete! Creatures written: {count}')
    
    else:
        print('[pipeline] Creatures dataset already exists.')

if __name__ == '__main__':
    build_creatures_dataset()