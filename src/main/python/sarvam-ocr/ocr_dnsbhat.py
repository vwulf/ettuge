#!/usr/bin/env python3
"""
ocr_dnsbhat.py — OCR all WX-encoded DNS Bhat PDFs using Sarvam Vision.

Reads PDFs from Google Drive DNS-Bhat folder, writes clean Unicode Kannada
Markdown to the ettuge repository, replacing the garbled pdfminer extractions.

Usage:
    python ocr_dnsbhat.py              # process all books
    python ocr_dnsbhat.py --book 03   # process one book by number
    python ocr_dnsbhat.py --dry-run   # show what would be done, don't run

Requires:
    SARVAM_API_KEY environment variable
    pip install sarvamai
"""

import argparse
import os
import sys

from ocr import ocr_pdf

# ─── Paths ────────────────────────────────────────────────────────────────────

GDRIVE = os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-vishwasms@gmail.com/My Drive/Books/DNS-Bhat"
)

ETTUGE = "/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat"

# ─── Book registry ────────────────────────────────────────────────────────────
# Each entry: (book_number, pdf_filename, output_slug, volume_suffix)
# volume_suffix is appended before -book.md, e.g. "-vol1" → "07-...-vol1-book.md"

BOOKS = [
    {
        "num": "03",
        "pdf": "KannadaPadagalaOlarachane.pdf",
        "slug": "kannada-padagala-olarachane",
        "vol": "",
        "pages": 239,
        "title": "ಕನ್ನಡ ಪದಗಳ ಒಳರಚನೆ",
        "header": (
            "# ಕನ್ನಡ ಪದಗಳ ಒಳರಚನೆ\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
    {
        "num": "07",
        "pdf": "sollarime-1.pdf",
        "slug": "kannadada-sollarime",
        "vol": "-vol1",
        "pages": 327,
        "title": "ಕನ್ನಡದ ಸೊಲ್ಲರಿಮೆ (ಸಂಪುಟ ೧)",
        "header": (
            "# ಕನ್ನಡದ ಸೊಲ್ಲರಿಮೆ — ಸಂಪುಟ ೧\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
    {
        "num": "07",
        "pdf": "sollarime-2.pdf",
        "slug": "kannadada-sollarime",
        "vol": "-vol2",
        "pages": 301,
        "title": "ಕನ್ನಡದ ಸೊಲ್ಲರಿಮೆ (ಸಂಪುಟ ೨)",
        "header": (
            "# ಕನ್ನಡದ ಸೊಲ್ಲರಿಮೆ — ಸಂಪುಟ ೨\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
    {
        "num": "17",
        "pdf": "kannada-nudi-nadedu-banda-dari.pdf",
        "slug": "kannada-nudi-nadedu-banda-dari",
        "vol": "",
        "pages": 405,
        "title": "ಕನ್ನಡ ನುಡಿ ನಡೆದು ಬಂದ ದಾರಿ",
        "header": (
            "# ಕನ್ನಡ ನುಡಿ ನಡೆದು ಬಂದ ದಾರಿ\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
    {
        "num": "25",
        "pdf": "KannadaVakyagalaOlaracane.pdf",
        "slug": "kannada-vakyagala-olarachane",
        "vol": "",
        "pages": 289,
        "title": "ಕನ್ನಡ ವಾಕ್ಯಗಳ ಒಳರಚನೆ",
        "header": (
            "# ಕನ್ನಡ ವಾಕ್ಯಗಳ ಒಳರಚನೆ\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
    {
        "num": "27",
        "pdf": "baasheyaBagge.pdf",
        "slug": "baasheya-bagge",
        "vol": "",
        "pages": 208,
        "title": "ಭಾಷೆಯ ಬಗ್ಗೆ ನೀವೇನು ಬಲ್ಲಿರಿ?",
        "header": (
            "# ಭಾಷೆಯ ಬಗ್ಗೆ ನೀವೇನು ಬಲ್ಲಿರಿ?\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
    {
        "num": "28",
        "pdf": "kannadakkeBeku.pdf",
        "slug": "kannadakke-beku",
        "vol": "",
        "pages": 253,
        "title": "ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ",
        "header": (
            "# ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
    {
        "num": "29",
        "pdf": "kannadavyakaranayaakebeku.pdf",
        "slug": "kannada-vyakarana-yaake-beku",
        "vol": "",
        "pages": 260,
        "title": "ಕನ್ನಡ ವ್ಯಾಕರಣ ಯಾಕೆ ಬೇಕು?",
        "header": (
            "# ಕನ್ನಡ ವ್ಯಾಕರಣ ಯಾಕೆ ಬೇಕು?\n\n"
            "**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಭಟ್\n"
            "**ಮೂಲ:** PDF (Sarvam Vision OCR)\n\n---\n\n"
        ),
    },
]


def book_key(b):
    """Unique key for a book entry."""
    return f"{b['num']}{b['vol']}"


def out_path(b):
    folder = f"{b['num']}-{b['slug']}"
    filename = f"{b['num']}-{b['slug']}{b['vol']}-book.md"
    return os.path.join(ETTUGE, folder, filename)


def pdf_path(b):
    return os.path.join(GDRIVE, b["pdf"])


def process_book(b, dry_run=False):
    pdf = pdf_path(b)
    out = out_path(b)

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Book {b['num']}{b['vol']}: {b['title']}")
    print(f"  PDF  : {pdf}")
    print(f"  Out  : {out}")
    print(f"  Pages: {b['pages']}")

    if not os.path.exists(pdf):
        print(f"  ⚠️  PDF not found — skipping")
        return False

    if dry_run:
        return True

    # Run OCR
    ocr_pdf(pdf, out, lang="kn-IN")

    # Prepend header (book title, author, source note)
    with open(out, "r", encoding="utf-8") as f:
        ocr_text = f.read()
    with open(out, "w", encoding="utf-8") as f:
        f.write(b["header"] + ocr_text)

    print(f"  ✓ Done")
    return True


def main():
    parser = argparse.ArgumentParser(description="OCR DNS Bhat WX-encoded PDFs with Sarvam Vision")
    parser.add_argument("--book", help="Process only this book number (e.g. 03, 07, 27)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without running")
    args = parser.parse_args()

    books = BOOKS
    if args.book:
        num = args.book.zfill(2)
        books = [b for b in BOOKS if b["num"] == num]
        if not books:
            print(f"Error: no book with number '{args.book}' in registry", file=sys.stderr)
            sys.exit(1)

    if not args.dry_run and not os.environ.get("SARVAM_API_KEY"):
        print("Error: SARVAM_API_KEY not set. Get your key at https://dashboard.sarvam.ai", file=sys.stderr)
        sys.exit(1)

    total = len(books)
    done = 0
    skipped = 0

    print(f"DNS Bhat WX OCR pipeline — {total} book(s) to process")
    if args.dry_run:
        print("(DRY RUN — no API calls will be made)")

    for b in books:
        ok = process_book(b, dry_run=args.dry_run)
        if ok:
            done += 1
        else:
            skipped += 1

    print(f"\n{'─' * 60}")
    print(f"Done: {done}  Skipped: {skipped}  Total: {total}")


if __name__ == "__main__":
    main()
