#!/usr/bin/env python3
"""
Transliterate Devanagari (Hindi) text to Kannada script in transcript files.
"""

import os
from pathlib import Path

# Devanagari to Kannada character mapping
DEVANAGARI_TO_KANNADA = {
    # Vowels
    'अ': 'ಅ', 'आ': 'ಆ', 'इ': 'ಇ', 'ई': 'ಈ', 'उ': 'ಉ', 'ऊ': 'ಊ',
    'ऋ': 'ಋ', 'ए': 'ಎ', 'ऐ': 'ಐ', 'ओ': 'ಒ', 'औ': 'ಔ',
    'ॠ': 'ೠ', 'ऌ': 'ಌ', 'ॡ': 'ೡ',

    # Vowel marks (matras)
    'ा': 'ಾ', 'ि': 'ಿ', 'ी': 'ೀ', 'ु': 'ು', 'ू': 'ೂ',
    'ृ': 'ೃ', 'ॄ': 'ೄ', 'े': 'ೆ', 'ै': 'ೈ', 'ो': 'ೊ', 'ौ': 'ೌ',
    'ॢ': 'ೢ', 'ॣ': 'ೣ',

    # Consonants
    'क': 'ಕ', 'ख': 'ಖ', 'ग': 'ಗ', 'घ': 'ಘ', 'ङ': 'ಙ',
    'च': 'ಚ', 'छ': 'ಛ', 'ज': 'ಜ', 'झ': 'ಝ', 'ञ': 'ಞ',
    'ट': 'ಟ', 'ठ': 'ಠ', 'ड': 'ಡ', 'ढ': 'ಢ', 'ण': 'ಣ',
    'त': 'ತ', 'थ': 'ಥ', 'द': 'ದ', 'ध': 'ಧ', 'न': 'ನ',
    'प': 'ಪ', 'फ': 'ಫ', 'ब': 'ಬ', 'भ': 'ಭ', 'म': 'ಮ',
    'य': 'ಯ', 'र': 'ರ', 'ल': 'ಲ', 'व': 'ವ',
    'श': 'ಶ', 'ष': 'ಷ', 'स': 'ಸ', 'ह': 'ಹ',
    'ळ': 'ಳ',

    # Special characters
    'ं': 'ಂ',  # Anusvara
    'ः': 'ಃ',  # Visarga
    '्': '್',  # Virama/Halant
    'ँ': 'ಁ',  # Chandrabindu
    'ऽ': 'ಽ',  # Avagraha
    '़': '',   # Nukta (no equivalent, remove)

    # Nukta variants (common in Hindi)
    'क़': 'ಕ', 'ख़': 'ಖ', 'ग़': 'ಗ', 'ज़': 'ಜ', 'ड़': 'ಡ', 'ढ़': 'ಢ', 'फ़': 'ಫ',

    # Digits
    '०': '೦', '१': '೧', '२': '೨', '३': '೩', '४': '೪',
    '५': '೫', '६': '೬', '७': '೭', '८': '೮', '९': '೯',

    # Punctuation
    '।': '।',  # Danda (same in both)
    '॥': '॥',  # Double danda
}


def transliterate_text(text):
    """Transliterate Devanagari text to Kannada script."""
    result = []
    i = 0
    while i < len(text):
        # Try 2-character match first (for nukta combinations)
        if i + 1 < len(text):
            two_char = text[i:i+2]
            if two_char in DEVANAGARI_TO_KANNADA:
                result.append(DEVANAGARI_TO_KANNADA[two_char])
                i += 2
                continue

        # Single character match
        char = text[i]
        if char in DEVANAGARI_TO_KANNADA:
            result.append(DEVANAGARI_TO_KANNADA[char])
        else:
            result.append(char)
        i += 1

    return ''.join(result)


def has_devanagari(text):
    """Check if text contains Devanagari characters."""
    for char in text:
        if '\u0900' <= char <= '\u097F':  # Devanagari Unicode block
            return True
    return False


def has_kannada(text):
    """Check if text contains Kannada characters."""
    for char in text:
        if '\u0C80' <= char <= '\u0CFF':  # Kannada Unicode block
            return True
    return False


def process_file(filepath):
    """Process a single transcript file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has Kannada or no Devanagari
    if has_kannada(content):
        return False, "Already has Kannada text"
    if not has_devanagari(content):
        return False, "No Devanagari text found"

    # Transliterate
    new_content = transliterate_text(content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "Transliterated"


def main():
    transcripts_dir = Path(__file__).parent.parent.parent.parent.parent / 'src/main/md/kannada/transcripts'

    if not transcripts_dir.exists():
        print(f"Directory not found: {transcripts_dir}")
        return

    converted = 0
    skipped = 0

    for filepath in sorted(transcripts_dir.glob('*.txt')):
        success, reason = process_file(filepath)
        if success:
            print(f"Converted: {filepath.name}")
            converted += 1
        else:
            skipped += 1

    print(f"\nSummary:")
    print(f"  Converted: {converted}")
    print(f"  Skipped: {skipped}")


if __name__ == '__main__':
    main()
