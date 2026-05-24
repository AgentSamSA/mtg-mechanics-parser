"""mtg-mechanics-parser proprocessing utilities.

Cleans and normalizes oracle text before parsing."""

import re

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