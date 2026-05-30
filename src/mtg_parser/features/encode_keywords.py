"""mtg-mechanics-parser keyword feature encoding.

Tranforms Scryfall keyword data to one-hot encoded features."""


from mtg_parser.features.keyword_features import is_real_keyword
from mtg_parser.utils.normalizer import normalize_keyword

# Get all keywords present in the dataset
def get_true_keywords(df):
    keyword_set = set()

    for keywords in df['keywords']:

        if not isinstance(keywords, list):
            continue

        for keyword in keywords:

            clean_keyword = normalize_keyword(keyword)

            if is_real_keyword(clean_keyword):
                keyword_set.add(clean_keyword)

    return sorted(keyword_set)


# Build one-hot columns for keywords
def build_keyword_columns(df, keyword_list):
    df = df.copy()

    normalized = df['keywords'].apply(
        lambda x: {normalize_keyword(k) for k in x}
        if isinstance(x, list)
        else set()
    )

    for keyword in keyword_list:
        df[f'has_{keyword}'] = normalized.map(lambda s: int(keyword in s))

    return df


def process_keywords(df):
    keywords = get_true_keywords(df)

    return build_keyword_columns(df, keywords)


if __name__ == '__main__':
    import pandas as pd

    from mtg_parser.utils.paths import PROCESSED_DIR

    df = pd.read_csv(PROCESSED_DIR / 'combined_points_cleaned.csv')
    df = process_keywords(df)
