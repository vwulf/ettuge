#!/usr/bin/env python3
"""
Script to extract ONLY Kannada transcripts from YouTube videos.
No fallback to other languages - if Kannada not available, mark as error.
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

def get_proxy_url():
    return f"http://{SMARTPROXY_USER}:{SMARTPROXY_PASS}@{SMARTPROXY_HOST}:{SMARTPROXY_PORT}"

proxy_url = get_proxy_url()
proxy_config = GenericProxyConfig(https_url=proxy_url)
api = YouTubeTranscriptApi(proxy_config=proxy_config)


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


def get_kannada_transcript(video_id):
    """
    Get ONLY Kannada transcript for a video ID.
    Returns tuple: (transcript_text, error_msg) where error_msg is None on success.
    """
    try:
        transcript_list = api.list(video_id)

        # Try to get Kannada transcript ONLY
        try:
            # Try manually created Kannada first
            transcript = transcript_list.find_manually_created_transcript(['kn'])
            transcript_data = transcript.fetch()
        except NoTranscriptFound:
            try:
                # Try generated Kannada
                transcript = transcript_list.find_generated_transcript(['kn'])
                transcript_data = transcript.fetch()
            except NoTranscriptFound:
                # No Kannada available - report what IS available
                available = [t.language_code for t in transcript_list]
                return None, f"No Kannada transcript. Available: {', '.join(available)}"

        # Combine all transcript segments
        full_text = ' '.join([entry.text if hasattr(entry, 'text') else entry['text'] for entry in transcript_data])
        return full_text, None

    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video"
    except NoTranscriptFound:
        return None, "No transcript found"
    except VideoUnavailable:
        return None, "Video is unavailable"
    except Exception as e:
        return None, f"Error: {str(e)}"


def main():
    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    # Read video links
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()

    success_count = 0
    error_count = 0
    skipped_count = 0

    print(f"Processing {len(lines)} links (Kannada only)...")

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
            print(f"{i}. Could not extract video ID from: {line}")
            error_count += 1
            continue

        output_file = output_dir / f"{video_id}.txt"
        if output_file.exists():
            print(f"{i}. Already exists: {video_id}, skipping...")
            skipped_count += 1
            continue

        print(f"{i}. Processing {video_id}...")

        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        print(f"   Waiting {delay:.1f}s...")
        time.sleep(delay)

        transcript, error_msg = get_kannada_transcript(video_id)

        if error_msg is not None:
            print(f"   NO KANNADA: {error_msg}")
            error_count += 1
            # Save error info
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\nNO_KANNADA: {error_msg}\n")
            continue

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\n{'='*80}\n")
                f.write(f"TRANSCRIPT:\n")
                f.write(f"{'='*80}\n\n")
                f.write(transcript)

            print(f"   SUCCESS: {len(transcript)} chars")
            success_count += 1

        except Exception as e:
            print(f"   ERROR saving: {str(e)}")
            error_count += 1

    print("\n" + "="*80)
    print(f"SUMMARY (Kannada Only):")
    print(f"  Successful: {success_count}")
    print(f"  No Kannada/Errors: {error_count}")
    print(f"  Skipped: {skipped_count}")
    print("="*80)


if __name__ == '__main__':
    main()
