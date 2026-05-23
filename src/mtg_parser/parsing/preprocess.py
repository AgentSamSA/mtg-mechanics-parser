"""mtg-mechanics-parser proprocessing utilities.

Cleans and normalizes oracle text before parsing."""

import re

# ABILITY_WORD_RE = re.compile(r"^([A-Za-z0-9' ]+)\s+—\s*")

# # Extract ability words from oracle text
# def extract_ability_word(text):
#     match = ABILITY_WORD_RE.match(text)
#     if match:
#         return match.group(1).strip()
#     return None

# # remove ability word prefix
# def strip_ability_word(text: str):
#     return ABILITY_WORD_RE.sub('', text)

# Fix oracle text encoding issues
def fix_encoding(text: str) -> str:
    return (
        text.replace('â€”', '—')
            .replace('â€“', '–')
    )

# Remove reminder text from oracle text
def remove_reminder_text(text: str):
    return re.sub(r'\([^)]*\)', '', text)

# Normalize oracle text whitespace
def normalize_whitespace(text: str):
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'[ \t]+', ' ', text)
    
    return text.strip()

def preprocess_oracle_text(text: str):
    text = fix_encoding(text)
    text = remove_reminder_text(text)
    text = normalize_whitespace(text)
    
    return text