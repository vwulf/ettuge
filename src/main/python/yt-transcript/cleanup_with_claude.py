#!/usr/bin/env python3
"""
Clean up garbled transliterated Kannada text using Claude API.

The transliterated text is phonetically similar to proper Kannada but semantically
garbled because YouTube's Hindi ASR transcribed Kannada speech. Claude can
reconstruct the proper Kannada text from the phonetic approximation.

USAGE:
    # Set your API key first:
    export ANTHROPIC_API_KEY="your-api-key"

    # Activate the virtual environment:
    source venv/bin/activate

    # Run the script:
    python cleanup_with_claude.py
"""

import os
import re
import sys
import time
import anthropic
from pathlib import Path

# Check for API key
if not os.environ.get('ANTHROPIC_API_KEY'):
    print("ERROR: ANTHROPIC_API_KEY environment variable not set")
    print("Please set it with: export ANTHROPIC_API_KEY='your-api-key'")
    print("Get your API key from: https://console.anthropic.com/")
    sys.exit(1)

# File paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent
TRANSCRIPTS_DIR = REPO_ROOT / 'src/main/md/kannada/transcripts'
CLEANED_DIR = REPO_ROOT / 'src/main/md/kannada/transcripts_cleaned'

# Rate limiting
DELAY_BETWEEN_REQUESTS = 2  # seconds

# Claude API
client = anthropic.Anthropic()

CLEANUP_PROMPT = """You are an expert in Kannada language. The following text is a garbled Kannada transcript that was created when YouTube's Hindi automatic speech recognition (ASR) tried to transcribe Kannada speech, and then the Hindi text was transliterated character-by-character to Kannada script.

The result is phonetically similar to proper Kannada but semantically incorrect. Your task is to reconstruct the proper Kannada text by:
1. Reading the garbled text phonetically
2. Understanding what Kannada words/phrases were likely spoken
3. Writing the correct Kannada text

Important guidelines:
- This is likely from a lecture about Kannada grammar by DNS Bhat
- Preserve the meaning and flow of the original speech
- Use proper Kannada grammar and vocabulary
- Keep technical terms accurate (grammar terms like ಎಸಕ ಪದ, ಹೆಸರು ಪದ, ಒಟ್ಟು, etc.)
- Output ONLY the cleaned Kannada text, no explanations

Garbled text to clean:
{text}

Cleaned Kannada text:"""


def is_transliterated_file(filepath):
    """Check if a file contains transliterated content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(500)  # Read first 500 chars
    return 'transliterated from' in content.lower()


def extract_transcript(filepath):
    """Extract just the transcript text from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the transcript section (after the separator line)
    match = re.search(r'={50,}\n\n(.+)$', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def extract_header(filepath):
    """Extract the header (video link, ID, etc.) from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get everything before the transcript
    match = re.search(r'^(.+?={50,}\n)', content, re.DOTALL)
    if match:
        return match.group(1)
    return ""


def cleanup_text(text):
    """Send text to Claude for cleanup."""
    # Truncate if too long (Claude has limits)
    max_chars = 15000
    if len(text) > max_chars:
        text = text[:max_chars] + "..."

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        messages=[
            {"role": "user", "content": CLEANUP_PROMPT.format(text=text)}
        ]
    )

    return message.content[0].text


def process_file(filepath, output_dir):
    """Process a single file."""
    filename = filepath.name
    output_file = output_dir / filename

    # Skip if already processed
    if output_file.exists():
        return "skipped", "Already processed"

    # Extract transcript
    transcript = extract_transcript(filepath)
    if not transcript:
        return "error", "Could not extract transcript"

    # Get header
    header = extract_header(filepath)

    try:
        # Clean up with Claude
        cleaned = cleanup_text(transcript)

        # Save cleaned version
        with open(output_file, 'w', encoding='utf-8') as f:
            # Update header to show it's been cleaned
            header = header.replace('transliterated from', 'cleaned, originally transliterated from')
            f.write(header)
            f.write("\n")
            f.write(cleaned)

        return "success", f"{len(cleaned)} chars"

    except Exception as e:
        return "error", str(e)


def main():
    # Create output directory
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)

    # Find all transliterated files
    transliterated_files = []
    for filepath in sorted(TRANSCRIPTS_DIR.glob('*.txt')):
        if is_transliterated_file(filepath):
            transliterated_files.append(filepath)

    print(f"Found {len(transliterated_files)} transliterated files to clean up")
    print(f"Output directory: {CLEANED_DIR}")
    print()

    success_count = 0
    error_count = 0
    skipped_count = 0

    for i, filepath in enumerate(transliterated_files, 1):
        print(f"{i}/{len(transliterated_files)}. Processing {filepath.name}...", end='', flush=True)

        status, message = process_file(filepath, CLEANED_DIR)

        if status == "success":
            print(f" SUCCESS: {message}")
            success_count += 1
            time.sleep(DELAY_BETWEEN_REQUESTS)
        elif status == "skipped":
            print(f" SKIPPED: {message}")
            skipped_count += 1
        else:
            print(f" ERROR: {message}")
            error_count += 1

    print("\n" + "="*80)
    print("SUMMARY:")
    print(f"  Cleaned: {success_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors: {error_count}")
    print("="*80)


if __name__ == '__main__':
    main()
