"""mtg-mechanics-parser keyword feature encoding.

Tranforms Scryfall keyword data to one-hot encoded features."""

# Get all keywords present in the dataset
def get_all_keywords(df):
    keyword_set = set()

    for keywords in df['keywords']:
        if isinstance(keywords, list):
            for keyword in keywords:
                keyword_set.add(keyword)

    keyword_set = sorted(keyword_set)

    return keyword_set


# Normalize keywords
def normalize_keyword(k: str) -> str:
    return k.lower().replace(' ', '_')


# Build one-hot columns for keywords
def build_keyword_columns(df, keyword_list):
    df = df.copy()

    df['keywords_normalized'] = df['keywords'].apply(
        lambda x: [normalize_keyword(k) for k in x]
        if isinstance(x, list)
        else []
    )

    for keyword in keyword_list:
        clean_keyword = normalize_keyword(keyword)
        col = f'has_{clean_keyword}'

        df[col] = df['keywords_normalized'].apply(
            lambda x: int(clean_keyword in x)
        )

    return df


def process_keywords(df):
    keywords = get_all_keywords(df)

    return build_keyword_columns(df, keywords)


if __name__ == '__main__':
    import pandas as pd

    from mtg_parser.utils.paths import PROCESSED_DIR

    df = pd.read_csv(PROCESSED_DIR / 'combined_points_cleaned.csv')
    df = process_keywords(df)
