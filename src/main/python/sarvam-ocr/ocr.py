#!/usr/bin/env python3
"""
ocr.py — OCR a single PDF using the Sarvam Vision API.

The Sarvam Document Intelligence API accepts a maximum of 10 pages per job.
This script splits the PDF into 10-page chunks, OCRs each chunk in sequence,
and concatenates the results into a single Markdown file.

Usage:
    python ocr.py --pdf path/to/book.pdf --out output.md [--lang kn-IN] [--chunk-size 10]

Requires:
    SARVAM_API_KEY environment variable (get key at https://dashboard.sarvam.ai)
    pip install sarvamai pypdf
"""

import argparse
import os
import sys
import tempfile
import zipfile

from pypdf import PdfReader, PdfWriter
from sarvamai import SarvamAI

CHUNK_SIZE = 10  # Sarvam API max pages per job


def ocr_chunk(client: "SarvamAI", chunk_pdf_path: str, lang: str, chunk_num: int, total_chunks: int) -> str:
    """OCR a single chunk PDF, return the extracted Markdown text."""
    print(f"    Chunk {chunk_num}/{total_chunks}: uploading...", end="", flush=True)

    job = client.document_intelligence.create_job(
        language=lang,
        output_format="md",
    )
    job.upload_file(chunk_pdf_path)
    job.start()

    print(" processing...", end="", flush=True)
    result = job.wait_until_complete()
    state = result.job_state
    print(f" {state}")

    if state not in ("Completed", "PartiallyCompleted"):
        print(f"  Error: chunk {chunk_num} ended with state: {state}", file=sys.stderr)
        return ""

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "output.zip")
        job.download_output(zip_path)

        with zipfile.ZipFile(zip_path, "r") as zf:
            md_files = sorted(n for n in zf.namelist() if n.endswith(".md"))
            if not md_files:
                print(f"  Warning: no .md in chunk {chunk_num} ZIP. Contents: {zf.namelist()}", file=sys.stderr)
                return ""
            parts = []
            for md_file in md_files:
                with zf.open(md_file) as f:
                    parts.append(f.read().decode("utf-8"))
            return "\n\n".join(parts)


def split_pdf(pdf_path: str, chunk_size: int, tmpdir: str):
    """Split a PDF into chunk_size-page chunks. Yields (chunk_pdf_path, start_page, end_page)."""
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)

    for start in range(0, total_pages, chunk_size):
        end = min(start + chunk_size, total_pages)
        writer = PdfWriter()
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        chunk_path = os.path.join(tmpdir, f"chunk_{start:04d}_{end:04d}.pdf")
        with open(chunk_path, "wb") as f:
            writer.write(f)

        yield chunk_path, start + 1, end  # 1-based page numbers for display


def ocr_pdf(pdf_path: str, out_path: str, lang: str = "kn-IN", chunk_size: int = CHUNK_SIZE) -> None:
    api_key = os.environ.get("SARVAM_API_KEY")
    if not api_key:
        print("Error: SARVAM_API_KEY environment variable not set.", file=sys.stderr)
        print("Get your key at https://dashboard.sarvam.ai", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    total_chunks = (total_pages + chunk_size - 1) // chunk_size

    print(f"  Language   : {lang}")
    print(f"  Pages      : {total_pages}  →  {total_chunks} chunk(s) of ≤{chunk_size} pages")
    print(f"  Output     : {out_path}")

    client = SarvamAI(api_subscription_key=api_key)

    all_parts = []
    with tempfile.TemporaryDirectory() as tmpdir:
        for chunk_num, (chunk_path, pg_start, pg_end) in enumerate(
            split_pdf(pdf_path, chunk_size, tmpdir), start=1
        ):
            print(f"  [pages {pg_start}–{pg_end}]")
            text = ocr_chunk(client, chunk_path, lang, chunk_num, total_chunks)
            all_parts.append(text)

    content = "\n\n".join(all_parts)

    os.makedirs(os.path.dirname(out_path), exist_ok=True) if os.path.dirname(out_path) else None
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"  ✓ Written {size_kb:.1f} KB to {out_path}")


def main():
    parser = argparse.ArgumentParser(description="OCR a PDF using Sarvam Vision API (auto-splits into chunks)")
    parser.add_argument("--pdf", required=True, help="Path to input PDF")
    parser.add_argument("--out", required=True, help="Path for output Markdown file")
    parser.add_argument("--lang", default="kn-IN", help="Language code (default: kn-IN)")
    parser.add_argument("--chunk-size", type=int, default=CHUNK_SIZE,
                        help=f"Pages per API job (default: {CHUNK_SIZE}, API max: 10)")
    args = parser.parse_args()

    ocr_pdf(args.pdf, args.out, args.lang, args.chunk_size)


if __name__ == "__main__":
    main()
