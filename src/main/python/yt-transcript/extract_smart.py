#!/usr/bin/env python3
"""
Smart transcript extractor for Kannada videos.
Handles cases where YouTube mislabels Kannada subtitles as Hindi.

Strategy:
1. Get any available transcript
2. If content has Kannada Unicode (0C80-0CFF) → use as-is
3. If content has Devanagari Unicode (0900-097F) → transliterate to Kannada
4. Only mark as NO_KANNADA if no Indian script found
"""

import re
import os
import time
import random
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)

# File paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent
INPUT_FILE = REPO_ROOT / 'src/main/md/kannada/malatibhat_dns_bhat_videos_links.txt'
OUTPUT_DIR = REPO_ROOT / 'src/main/md/kannada/transcripts'

# Rate limiting
MIN_DELAY = 25
MAX_DELAY = 45

# Smartproxy configuration
SMARTPROXY_USER = os.environ.get('SMARTPROXY_USER', 'spn3qfngzn')
SMARTPROXY_PASS = os.environ.get('SMARTPROXY_PASS', 'i~b4jNtj59FWQ9swgj')
SMARTPROXY_HOST = 'gate.smartproxy.com'
SMARTPROXY_PORT = 10000

# Devanagari to Kannada transliteration map
DEVANAGARI_TO_KANNADA = {
    # Vowels
    'अ': 'ಅ', 'आ': 'ಆ', 'इ': 'ಇ', 'ई': 'ಈ', 'उ': 'ಉ', 'ऊ': 'ಊ',
    'ऋ': 'ಋ', 'ए': 'ಎ', 'ऐ': 'ಐ', 'ओ': 'ಒ', 'औ': 'ಔ',
    'ॠ': 'ೠ', 'ऌ': 'ಌ', 'ॡ': 'ೡ',
    # Vowel marks
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
    'ं': 'ಂ', 'ः': 'ಃ', '्': '್', 'ँ': 'ಁ', 'ऽ': 'ಽ', '़': '',
    # Nukta variants
    'क़': 'ಕ', 'ख़': 'ಖ', 'ग़': 'ಗ', 'ज़': 'ಜ', 'ड़': 'ಡ', 'ढ़': 'ಢ', 'फ़': 'ಫ',
    # Digits
    '०': '೦', '१': '೧', '२': '೨', '३': '೩', '४': '೪',
    '५': '೫', '६': '೬', '७': '೭', '८': '೮', '९': '೯',
    '।': '।', '॥': '॥',
}


def get_proxy_url():
    return f"http://{SMARTPROXY_USER}:{SMARTPROXY_PASS}@{SMARTPROXY_HOST}:{SMARTPROXY_PORT}"

proxy_url = get_proxy_url()
proxy_config = GenericProxyConfig(https_url=proxy_url)
api = YouTubeTranscriptApi(proxy_config=proxy_config)


def has_kannada(text):
    """Check if text has Kannada Unicode characters."""
    for char in text:
        if '\u0C80' <= char <= '\u0CFF':
            return True
    return False


def has_devanagari(text):
    """Check if text has Devanagari Unicode characters."""
    for char in text:
        if '\u0900' <= char <= '\u097F':
            return True
    return False


def transliterate_to_kannada(text):
    """Transliterate Devanagari text to Kannada."""
    result = []
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            two_char = text[i:i+2]
            if two_char in DEVANAGARI_TO_KANNADA:
                result.append(DEVANAGARI_TO_KANNADA[two_char])
                i += 2
                continue
        char = text[i]
        if char in DEVANAGARI_TO_KANNADA:
            result.append(DEVANAGARI_TO_KANNADA[char])
        else:
            result.append(char)
        i += 1
    return ''.join(result)


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/v\/([a-zA-Z0-9_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_transcript_smart(video_id):
    """
    Get transcript and process it intelligently.
    Returns tuple: (transcript_text, status, original_lang)
    status: 'kannada', 'transliterated', 'no_indian_script', or error message
    """
    try:
        transcript_list = api.list(video_id)
        available_langs = [t.language_code for t in transcript_list]

        # Try to get any transcript (preferring kn, then hi, then any)
        transcript = None
        lang_used = None

        for lang in ['kn', 'hi', 'en']:
            try:
                transcript = transcript_list.find_manually_created_transcript([lang])
                lang_used = lang
                break
            except NoTranscriptFound:
                try:
                    transcript = transcript_list.find_generated_transcript([lang])
                    lang_used = lang
                    break
                except NoTranscriptFound:
                    continue

        if not transcript:
            # Get any available
            transcript = next(iter(transcript_list))
            lang_used = transcript.language_code

        # Fetch the transcript data
        transcript_data = transcript.fetch()
        full_text = ' '.join([entry.text if hasattr(entry, 'text') else entry['text'] for entry in transcript_data])

        # Check content type
        if has_kannada(full_text):
            return full_text, 'kannada', lang_used
        elif has_devanagari(full_text):
            # Transliterate to Kannada
            kannada_text = transliterate_to_kannada(full_text)
            return kannada_text, 'transliterated', lang_used
        else:
            # No Indian script found (likely English or other)
            return full_text, 'no_indian_script', lang_used

    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video", None
    except NoTranscriptFound:
        return None, "No transcript found", None
    except VideoUnavailable:
        return None, "Video is unavailable", None
    except Exception as e:
        return None, f"Error: {str(e)}", None


def main():
    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()

    kannada_count = 0
    transliterated_count = 0
    no_indian_count = 0
    error_count = 0
    skipped_count = 0

    print(f"Processing {len(lines)} links (smart mode)...")
    print(flush=True)

    for i, line in enumerate(lines, 1):
        line = line.strip()

        if not line:
            continue

        if '@MALATIBHAT' in line:
            print(f"{i}. Skipping channel link")
            skipped_count += 1
            continue

        video_id = extract_video_id(line)

        if not video_id:
            print(f"{i}. Could not extract video ID")
            error_count += 1
            continue

        output_file = output_dir / f"{video_id}.txt"
        if output_file.exists():
            print(f"{i}. Already exists: {video_id}")
            skipped_count += 1
            continue

        print(f"{i}. Processing {video_id}...", end='', flush=True)

        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        time.sleep(delay)

        transcript, status, lang = get_transcript_smart(video_id)

        if transcript is None:
            # Error case
            print(f" ERROR: {status}")
            error_count += 1
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\nERROR: {status}\n")
        elif status == 'kannada':
            print(f" KANNADA ({lang})")
            kannada_count += 1
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\n{'='*80}\n")
                f.write(f"TRANSCRIPT:\n")
                f.write(f"{'='*80}\n\n")
                f.write(transcript)
        elif status == 'transliterated':
            print(f" TRANSLITERATED from {lang}")
            transliterated_count += 1
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\n{'='*80}\n")
                f.write(f"TRANSCRIPT (transliterated from {lang}):\n")
                f.write(f"{'='*80}\n\n")
                f.write(transcript)
        else:  # no_indian_script
            print(f" NO INDIAN SCRIPT ({lang})")
            no_indian_count += 1
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\nNO_INDIAN_SCRIPT: Content in {lang}, no Kannada/Devanagari found\n")
                f.write(f"\nOriginal content:\n{transcript}\n")

    print("\n" + "="*80)
    print("SUMMARY:")
    print(f"  Native Kannada: {kannada_count}")
    print(f"  Transliterated: {transliterated_count}")
    print(f"  No Indian script: {no_indian_count}")
    print(f"  Errors: {error_count}")
    print(f"  Skipped: {skipped_count}")
    print("="*80)


if __name__ == '__main__':
    main()
