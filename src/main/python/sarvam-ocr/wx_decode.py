#!/usr/bin/env python3
"""
wx_decode.py — Convert Nudi/Baraha/KGP Kannada font encoding to Unicode.

The Nudi font encoding (also called APS, KGP, Baraha encoding) is a legacy
pre-Unicode DTP encoding used in Kannada PageMaker/Ventura documents.  When
such PDFs are OCR'd without font substitution the output is garbled cp1252
text.  This script converts that garbled text to proper Unicode Kannada.

Algorithm based on:
  https://github.com/aravindavk/ascii2unicode
  (aravindavk's ascii2unicode — the canonical Nudi→Unicode converter)

Usage:
    python wx_decode.py --book 07          # decode book 07 vol1 and vol2
    python wx_decode.py --book 17          # decode book 17
    python wx_decode.py --all              # decode all garbled books
    python wx_decode.py --file <path>      # decode a specific file (in-place)
"""

import argparse
import os
import re
import sys
import unicodedata

# ---------------------------------------------------------------------------
# Nudi / Baraha encoding tables (from aravindavk/ascii2unicode)
# ---------------------------------------------------------------------------

# Multi-byte cp1252 sequences → Unicode Kannada (longest-match first)
MAPPING = {
    "C": "ಅ",
    "D": "ಆ",
    "E": "ಇ",
    "F": "ಈ",
    "G": "ಉ",
    "H": "ಊ",
    "IÄ": "ಋ",
    "J": "ಎ",
    "K": "ಏ",
    "L": "ಐ",
    "M": "ಒ",
    "N": "ಓ",
    "O": "ಔ",
    "A": "ಂ",
    "B": "ಃ",
    "Pï": "ಕ್",
    "PÀ": "ಕ",
    "PÁ": "ಕಾ",
    "Q": "ಕಿ",
    "PÉ": "ಕೆ",
    "PË": "ಕೌ",
    "Sï": "ಖ್",
    "R": "ಖ",
    "SÁ": "ಖಾ",
    "T": "ಖಿ",
    "SÉ": "ಖೆ",
    "SË": "ಖೌ",
    "Uï": "ಗ್",
    "UÀ": "ಗ",
    "UÁ": "ಗಾ",
    "V": "ಗಿ",
    "UÉ": "ಗೆ",
    "UË": "ಗೌ",
    "Wï": "ಘ್",
    "WÀ": "ಘ",
    "WÁ": "ಘಾ",
    "X": "ಘಿ",
    "WÉ": "ಘೆ",
    "WË": "ಘೌ",
    "k": "ಞ",
    "Zï": "ಚ್",
    "ZÀ": "ಚ",
    "ZÁ": "ಚಾ",
    "a": "ಚಿ",
    "ZÉ": "ಚೆ",
    "ZË": "ಚೌ",
    "bï": "ಛ್",
    "bÀ": "ಛ",
    "bÁ": "ಛಾ",
    "c": "ಛಿ",
    "bÉ": "ಛೆ",
    "bË": "ಛೌ",
    "eï": "ಜ್",
    "d": "ಜ",
    "eÁ": "ಜಾ",
    "f": "ಜಿ",
    "eÉ": "ಜೆ",
    "eË": "ಜೌ",
    "gÀhiï": "ಝ್",
    "gÀhÄ": "ಝ",
    "gÀhiÁ": "ಝಾ",
    "jhÄ": "ಝಿ",
    "gÉhÄ": "ಝೆ",
    "gÉhÆ": "ಝೊ",
    "gÀhiË": "ಝೌ",
    "Y": "ಙ",
    "mï": "ಟ್",
    "l": "ಟ",
    "mÁ": "ಟಾ",
    "n": "ಟಿ",
    "mÉ": "ಟೆ",
    "mË": "ಟೌ",
    "oï": "ಠ್",
    "oÀ": "ಠ",
    "oÁ": "ಠಾ",
    "p": "ಠಿ",
    "oÉ": "ಠೆ",
    "oË": "ಠೌ",
    "qï": "ಡ್",
    "qÀ": "ಡ",
    "qÁ": "ಡಾ",
    "r": "ಡಿ",
    "qÉ": "ಡೆ",
    "qË": "ಡೌ",
    "qsï": "ಢ್",
    "qsÀ": "ಢ",
    "qsÁ": "ಢಾ",
    "rü": "ಢಿ",
    "qsÉ": "ಢೆ",
    "qsË": "ಢೌ",
    "uï": "ಣ್",
    "t": "ಣ",
    "uÁ": "ಣಾ",
    "tÂ": "ಣಿ",
    "uÉ": "ಣೆ",
    "uË": "ಣೌ",
    "vï": "ತ್",
    "vÀ": "ತ",
    "vÁ": "ತಾ",
    "w": "ತಿ",
    "vÉ": "ತೆ",
    "vË": "ತೌ",
    "xï": "ಥ್",
    "xÀ": "ಥ",
    "xÁ": "ಥಾ",
    "y": "ಥಿ",
    "xÉ": "ಥೆ",
    "xË": "ಥೌ",
    "zï": "ದ್",
    "zÀ": "ದ",
    "zÁ": "ದಾ",
    "¢": "ದಿ",
    "zÉ": "ದೆ",
    "zË": "ದೌ",
    "zsï": "ಧ್",
    "zsÀ": "ಧ",
    "zsÁ": "ಧಾ",
    "¢ü": "ಧಿ",
    "zsÉ": "ಧೆ",
    "zsË": "ಧೌ",
    "£ï": "ನ್",
    "£À": "ನ",
    "£Á": "ನಾ",
    "¤": "ನಿ",
    "£É": "ನೆ",
    "£Ë": "ನೌ",
    "¥ï": "ಪ್",
    "¥À": "ಪ",
    "¥Á": "ಪಾ",
    "¦": "ಪಿ",
    "¥É": "ಪೆ",
    "¥Ë": "ಪೌ",
    "¥sï": "ಫ್",
    "¥sÀ": "ಫ",
    "¥sÁ": "ಫಾ",
    "¦ü": "ಫಿ",
    "¥sÉ": "ಫೆ",
    "¥sË": "ಫೌ",
    "¨ï": "ಬ್",
    "§": "ಬ",
    "¨Á": "ಬಾ",
    "©": "ಬಿ",
    "¨É": "ಬೆ",
    "¨Ë": "ಬೌ",
    "¨sï": "ಭ್",
    "¨sÀ": "ಭ",
    "¨sÁ": "ಭಾ",
    "©ü": "ಭಿ",
    "¨sÉ": "ಭೆ",
    "¨sË": "ಭೌ",
    "ªÀiï": "ಮ್",
    "ªÀÄ": "ಮ",
    "ªÀiÁ": "ಮಾ",
    "«Ä": "ಮಿ",
    "ªÉÄ": "ಮೆ",
    "ªÀiË": "ಮೌ",
    "AiÀiï": "ಯ್",
    "AiÀÄ": "ಯ",
    "0iÀÄ": "ಯ",
    "AiÀiÁ": "ಯಾ",
    "0iÀiÁ": "ಯಾ",
    "¬Ä": "ಯಿ",
    "0iÀÄÄ": "ಯು",
    "AiÉÄ": "ಯೆ",
    "0iÉÆ": "ಯೊ",
    "AiÉÆ": "ಯೊ",
    "AiÀiË": "ಯೌ",
    "gï": "ರ್",
    "gÀ": "ರ",
    "gÁ": "ರಾ",
    "j": "ರಿ",
    "gÉ": "ರೆ",
    "gË": "ರೌ",
    "¯ï": "ಲ್",
    "®": "ಲ",
    "¯Á": "ಲಾ",
    "°": "ಲಿ",
    "¯É": "ಲೆ",
    "¯Ë": "ಲೌ",
    "ªï": "ವ್",
    "ªÀ": "ವ",
    "ªÁ": "ವಾ",
    "«": "ವಿ",
    "ªÀÅ": "ವು",
    "ªÀÇ": "ವೂ",
    "ªÉ": "ವೆ",
    "ªÉÃ": "ವೇ",
    "ªÉÊ": "ವೈ",
    "ªÉÆ": "ಮೊ",
    "ªÉÆÃ": "ಮೋ",
    "ªÉÇ": "ವೊ",
    "ªÉÇÃ": "ವೋ",
    "¥ÀÅ": "ಪು",
    "¥ÀÇ": "ಪೂ",
    "¥sÀÅ": "ಫು",
    "¥sÀÇ": "ಫೂ",
    "ªË": "ವೌ",
    "±ï": "ಶ್",
    "±À": "ಶ",
    "±Á": "ಶಾ",
    "²": "ಶಿ",
    "±É": "ಶೆ",
    "±Ë": "ಶೌ",
    "µï": "ಷ್",
    "µÀ": "ಷ",
    "µÁ": "ಷಾ",
    "¶": "ಷಿ",
    "µÉ": "ಷೆ",
    "µË": "ಷೌ",
    "¸ï": "ಸ್",
    "¸À": "ಸ",
    "¸Á": "ಸಾ",
    "¹": "ಸಿ",
    "¸É": "ಸೆ",
    "¸Ë": "ಸೌ",
    "ºï": "ಹ್",
    "ºÀ": "ಹ",
    "ºÁ": "ಹಾ",
    "»": "ಹಿ",
    "ºÉ": "ಹೆ",
    "ºË": "ಹೌ",
    "¼ï": "ಳ್",
    "¼À": "ಳ",
    "¼Á": "ಳಾ",
    "½": "ಳಿ",
    "¼É": "ಳೆ",
    "¼Ë": "ಳೌ",
    # Additional entries for common patterns not in the original mapping
    "§À": "ಬ",
}

# Vattaksharagalu (half-consonants / subscript forms used in conjuncts)
# These insert ್ (virama) + the consonant
VATTAKSHARA = {
    "Ì": "ಕ",
    "Í": "ಖ",
    "Î": "ಗ",
    "Ï": "ಘ",
    "Õ": "ಞ",
    "Ñ": "ಚ",
    "Ò": "ಛ",
    "Ó": "ಜ",
    "Ô": "ಝ",
    "Ö": "ಟ",
    "×": "ಠ",
    "Ø": "ಡ",
    "Ù": "ಢ",
    "Ú": "ಣ",
    "Û": "ತ",
    "Ü": "ಥ",
    "Ý": "ದ",
    "Þ": "ಧ",
    "ß": "ನ",
    "à": "ಪ",
    "á": "ಫ",
    "â": "ಬ",
    "ã": "ಭ",
    "ä": "ಮ",
    "å": "ಯ",
    "æ": "ರ",
    "è": "ಲ",
    "é": "ವ",
    "ê": "ಶ",
    "ë": "ಷ",
    "ì": "ಸ",
    "í": "ಹ",
    "î": "ಳ",
    "ç": "ರ",
}

# Arkavattu — ರ subscript (appears as ð)
ARKAVATTU = {"ð": "ರ"}

# Broken-case diacritics — transform the immediately preceding dependent vowel
# Key: the broken-case char; value: dict of (prev-vowel → replacement-vowel)
BROKEN_CASES = {
    "Ã": {"ಿ": "ೀ", "ೆ": "ೇ", "ೊ": "ೋ", "_default": "ೀ"},
    "Ä": {"_default": "ು"},
    "Æ": {"ೆ": "ೊ", "_default": "ೂ"},
    "È": {"_default": "ೃ"},
    "Ê": {"ೆ": "ೈ", "_default": "ೈ"},
}

# Chars to silently drop
IGNORE = {"ö", "÷"}

# Standalone long-vowel continuations (Ã after ಾ / matra contexts)
LONG_VOWEL_EXTENDERS = {
    "Ã": "ೀ",  # default when no preceding short-i/e/o to extend
}

# ---------------------------------------------------------------------------
# Sorting the mapping keys longest-first for greedy matching
# ---------------------------------------------------------------------------
_SORTED_KEYS = sorted(MAPPING.keys(), key=len, reverse=True)

# ---------------------------------------------------------------------------
# Kannada Unicode block helpers
# ---------------------------------------------------------------------------
KN_VIRAMA = "\u0CCD"          # ್
KN_ANUSVARA = "\u0C82"        # ಂ

# Dependent vowel signs (matras) — single Unicode codepoints
# These can be moved across vattakshara boundaries and transformed by broken-cases
_DEPENDENT_VOWELS = {
    "\u0CBF",  # ಿ  (i)
    "\u0CC0",  # ೀ  (ii)
    "\u0CC1",  # ು  (u)
    "\u0CC2",  # ೂ  (uu)
    "\u0CC3",  # ೃ  (ri)
    "\u0CC6",  # ೆ  (e)
    "\u0CC7",  # ೇ  (ee)
    "\u0CC8",  # ೈ  (ai)
    "\u0CCA",  # ೊ  (o)
    "\u0CCB",  # ೋ  (oo)
    "\u0CBE",  # ಾ  (aa)
}


def _extend_result(result: list[str], chars: str) -> None:
    """Append each Unicode codepoint in *chars* individually to *result*.

    This ensures broken-case and vattakshara handlers always see individual
    vowel signs at result[-1], never a consonant+vowel compound string.
    """
    for c in chars:
        result.append(c)


# ---------------------------------------------------------------------------
# Core conversion logic
# ---------------------------------------------------------------------------

def convert_chunk(text: str) -> str:
    """Convert a single word-chunk of Nudi-encoded text to Unicode Kannada.

    Processes the text character-by-character with greedy longest-match
    against MAPPING, then handles vattaksharagalu and broken-case diacritics.

    Two critical rearrangements are applied:

    1. **Broken-case diacritics** (Ã Ä Æ È Ê) transform the immediately
       preceding dependent vowel sign.  Because MAPPING entries are expanded
       codepoint-by-codepoint, result[-1] is always an individual Unicode
       codepoint and the lookup works correctly.

    2. **Vattakshara rearrangement**: When a half-consonant glyph (vattakshara)
       is encountered, if result[-1] is a dependent vowel sign (matra), that
       sign is temporarily removed, the virama + consonant is appended, and
       then the sign is re-appended.  This converts the Nudi visual order
       (vowel before subscript) to correct Unicode logical order
       (virama + consonant before vowel).
    """
    result: list[str] = []
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        # --- Ignore list ---
        if ch in IGNORE:
            i += 1
            continue

        # --- Broken-case diacritics ---
        if ch in BROKEN_CASES:
            bc = BROKEN_CASES[ch]
            if result and result[-1] in bc:
                result[-1] = bc[result[-1]]
            else:
                default = bc.get("_default", "")
                if default:
                    result.append(default)
            i += 1
            continue

        # --- Arkavattu (ð) — ರ subscript ---
        if ch in ARKAVATTU:
            # Same rearrangement as vattakshara: pop trailing vowel, push virama+ra, push vowel
            trailing_vowel = ""
            if result and result[-1] in _DEPENDENT_VOWELS:
                trailing_vowel = result.pop()
            result.append(KN_VIRAMA)
            result.append(ARKAVATTU[ch])
            if trailing_vowel:
                result.append(trailing_vowel)
            i += 1
            continue

        # --- Vattaksharagalu (half-consonant subscript forms) ---
        if ch in VATTAKSHARA:
            # Rearrangement: if preceding char is a vowel sign, pop it, insert
            # ್ + consonant, then re-append the vowel.
            trailing_vowel = ""
            if result and result[-1] in _DEPENDENT_VOWELS:
                trailing_vowel = result.pop()
            result.append(KN_VIRAMA)
            result.append(VATTAKSHARA[ch])
            if trailing_vowel:
                result.append(trailing_vowel)
            i += 1
            continue

        # --- Greedy longest-match against MAPPING ---
        matched = False
        for key in _SORTED_KEYS:
            key_len = len(key)
            if text[i:i + key_len] == key:
                # Expand each codepoint individually so broken-cases work on result[-1]
                _extend_result(result, MAPPING[key])
                i += key_len
                matched = True
                break

        if not matched:
            # Pass through ASCII printable and other non-Nudi chars unchanged
            result.append(ch)
            i += 1

    return "".join(result)


def _is_nudi_line(line: str) -> bool:
    """Return True if this line contains Nudi-encoded (garbled Latin-1) text."""
    # Heuristic: line has significant number of chars in the Latin-1 Supplement /
    # Latin Extended-A range that are NOT Kannada Unicode
    nudi_chars = sum(
        1 for c in line
        if 0x0080 <= ord(c) <= 0x00FF and not (0x0C80 <= ord(c) <= 0x0CFF)
    )
    kannada_chars = sum(1 for c in line if "\u0C80" <= c <= "\u0CFF")
    total = len(line)
    if total == 0:
        return False
    # If more than 15% of chars are Nudi-range Latin-1, treat as Nudi
    return nudi_chars > max(3, total * 0.15) and kannada_chars < nudi_chars


def convert_text(text: str) -> str:
    """Convert Nudi-encoded text to Unicode Kannada, line by line.

    Lines that appear to be pure Unicode Kannada (e.g., the metadata header
    added by our pipeline) are left untouched.  Only lines with Nudi-encoded
    content are converted.
    """
    lines = text.split("\n")
    output_lines = []
    for line in lines:
        if _is_nudi_line(line):
            output_lines.append(convert_chunk(line))
        else:
            output_lines.append(line)
    return "\n".join(output_lines)


# ---------------------------------------------------------------------------
# File-level helpers
# ---------------------------------------------------------------------------

def convert_file(path: str, dry_run: bool = False) -> dict:
    """Convert a single file in-place.  Returns stats dict."""
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    converted = convert_text(original)

    # Count Kannada chars before/after
    kn_before = sum(1 for c in original if "\u0C80" <= c <= "\u0CFF")
    kn_after = sum(1 for c in converted if "\u0C80" <= c <= "\u0CFF")
    nudi_before = sum(
        1 for c in original
        if 0x0080 <= ord(c) <= 0x00FF and not ("\u0C80" <= c <= "\u0CFF")
    )
    nudi_after = sum(
        1 for c in converted
        if 0x0080 <= ord(c) <= 0x00FF and not ("\u0C80" <= c <= "\u0CFF")
    )

    stats = {
        "path": path,
        "kn_before": kn_before,
        "kn_after": kn_after,
        "nudi_before": nudi_before,
        "nudi_after": nudi_after,
        "changed": original != converted,
    }

    if not dry_run and original != converted:
        with open(path, "w", encoding="utf-8") as f:
            f.write(converted)

    return stats


# ---------------------------------------------------------------------------
# Book file registry
# ---------------------------------------------------------------------------

DNSBHAT_BASE = os.path.join(
    os.path.dirname(__file__),
    "../../md/kannada/dnsbhat",
)

# Books with WX-garbled OCR (need decoding)
GARBLED_BOOKS = {
    "07": [
        "07-kannadada-sollarime/07-kannadada-sollarime-vol1-book.md",
        "07-kannadada-sollarime/07-kannadada-sollarime-vol2-book.md",
    ],
    "17": [
        "17-kannada-nudi-nadedu-banda-dari/17-kannada-nudi-nadedu-banda-dari-book.md",
    ],
    "25": [
        "25-kannada-vakyagala-olarachane/25-kannada-vakyagala-olarachane-book.md",
    ],
    "28": [
        "28-kannadakke-beku/28-kannadakke-beku-book.md",
    ],
    "29": [
        "29-kannada-vyakarana-yaake-beku/29-kannada-vyakarana-yaake-beku-book.md",
    ],
}


def get_book_files(book_id: str) -> list[str]:
    """Return absolute paths for a given book ID."""
    rel_paths = GARBLED_BOOKS.get(book_id, [])
    return [os.path.abspath(os.path.join(DNSBHAT_BASE, p)) for p in rel_paths]


def get_all_files() -> list[str]:
    """Return absolute paths for all garbled books."""
    paths = []
    for book_id in GARBLED_BOOKS:
        paths.extend(get_book_files(book_id))
    return paths


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_stats(stats: dict, dry_run: bool) -> None:
    fname = os.path.basename(stats["path"])
    mode = "[DRY RUN] " if dry_run else ""
    if stats["changed"]:
        print(
            f"{mode}✓ {fname}: "
            f"Kannada chars {stats['kn_before']:,} → {stats['kn_after']:,} | "
            f"Nudi chars {stats['nudi_before']:,} → {stats['nudi_after']:,}"
        )
    else:
        print(f"{mode}  {fname}: no changes (already Unicode or nothing to decode)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Nudi/Baraha-encoded Kannada text to Unicode"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--book", metavar="ID", help="Book number (e.g. 07, 17, 25, 28, 29)")
    group.add_argument("--all", action="store_true", help="Convert all garbled books")
    group.add_argument("--file", metavar="PATH", help="Convert a specific file")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    if args.file:
        files = [args.file]
    elif args.all:
        files = get_all_files()
    else:
        files = get_book_files(args.book)
        if not files:
            print(f"ERROR: No files registered for book '{args.book}'.")
            print(f"Known garbled books: {', '.join(sorted(GARBLED_BOOKS))}")
            sys.exit(1)

    if not files:
        print("No files found.")
        sys.exit(1)

    total_stats = {"kn_before": 0, "kn_after": 0, "nudi_before": 0, "nudi_after": 0}
    for path in files:
        if not os.path.exists(path):
            print(f"WARNING: File not found: {path}")
            continue
        stats = convert_file(path, dry_run=args.dry_run)
        print_stats(stats, dry_run=args.dry_run)
        for key in total_stats:
            total_stats[key] += stats[key]

    if len(files) > 1:
        print()
        print(
            f"Total: Kannada chars {total_stats['kn_before']:,} → {total_stats['kn_after']:,} | "
            f"Nudi chars {total_stats['nudi_before']:,} → {total_stats['nudi_after']:,}"
        )


if __name__ == "__main__":
    main()
