#!/usr/bin/env python3
"""
Script to extract transcripts from YouTube videos listed in malatibhat_dns_bhat_videos_links.txt
and save them as text files with the original link.

QUICK START:
    1. Install dependencies: pip install -r src/main/python/yt-transcript/requirements.txt
    2. Run the script from repository root: python3 src/main/python/yt-transcript/extract_transcripts.py
    3. Transcripts will be saved in: src/main/md/kannada/transcripts/

REQUIREMENTS:
    - Python 3.6+
    - youtube-transcript-api library (see requirements.txt)
    - Internet access to YouTube

FEATURES:
    - Extracts transcripts from 349 video links
    - Prefers Kannada, English, then Hindi transcripts
    - Handles missing transcripts gracefully
    - Resumes from where it left off (skips existing transcripts)
    - Saves transcripts in UTF-8 format (supports Kannada text)
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

# File paths - relative to script location
SCRIPT_DIR = Path(__file__).parent
# Navigate up to repository root: yt-transcript -> python -> main -> src -> repo_root
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent
INPUT_FILE = REPO_ROOT / 'src/main/md/kannada/malatibhat_dns_bhat_videos_links.txt'
OUTPUT_DIR = REPO_ROOT / 'src/main/md/kannada/transcripts'

# Rate limiting settings - longer delays to avoid detection
MIN_DELAY = 25  # Minimum seconds between requests
MAX_DELAY = 45  # Maximum seconds between requests (randomized to avoid detection)

# Smartproxy configuration - using rotating residential proxy
SMARTPROXY_USER = os.environ.get('SMARTPROXY_USER', 'spn3qfngzn')
SMARTPROXY_PASS = os.environ.get('SMARTPROXY_PASS', 'i~b4jNtj59FWQ9swgj')
SMARTPROXY_HOST = 'gate.smartproxy.com'
SMARTPROXY_PORT = 10000  # Rotating proxy port (new IP per request)


def get_proxy_url():
    """Get proxy URL for Smartproxy residential."""
    return f"http://{SMARTPROXY_USER}:{SMARTPROXY_PASS}@{SMARTPROXY_HOST}:{SMARTPROXY_PORT}"


# Create API instance with proxy
proxy_url = get_proxy_url()
proxy_config = GenericProxyConfig(https_url=proxy_url)
api = YouTubeTranscriptApi(proxy_config=proxy_config)


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    # Pattern for standard YouTube URLs
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


def get_transcript(video_id):
    """
    Get transcript for a video ID.
    Returns tuple: (transcript_text, error_msg) where error_msg is None on success.
    """
    try:
        # Try to get transcript in any available language
        # Try Kannada (kn) first, then English (en), then Hindi (hi), then any available
        transcript_list = api.list(video_id)
        
        # Try to get manually created transcript first
        try:
            transcript = transcript_list.find_manually_created_transcript(['kn', 'en', 'hi'])
            transcript_data = transcript.fetch()
        except NoTranscriptFound:
            # If no manual transcript, get any generated transcript
            try:
                transcript = transcript_list.find_generated_transcript(['kn', 'en', 'hi'])
                transcript_data = transcript.fetch()
            except NoTranscriptFound:
                # Get any available transcript
                transcript = next(iter(transcript_list))
                transcript_data = transcript.fetch()
        
        # Combine all transcript segments into one text
        # Note: newer API uses .text attribute, older uses ['text'] dict access
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
    # Use module-level constants for file paths
    input_file = INPUT_FILE
    output_dir = OUTPUT_DIR
    
    # Create output directory if it doesn't exist (including parent directories)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Read video links
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Process each video link
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    print(f"Processing {len(lines)} links...")
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Skip channel link (first link)
        if '@MALATIBHAT' in line:
            print(f"{i}. Skipping channel link: {line}")
            skipped_count += 1
            continue
        
        # Extract video ID
        video_id = extract_video_id(line)
        
        if not video_id:
            print(f"{i}. Could not extract video ID from: {line}")
            error_count += 1
            continue
        
        # Check if transcript already exists
        output_file = output_dir / f"{video_id}.txt"
        if output_file.exists():
            print(f"{i}. Transcript already exists for {video_id}, skipping...")
            skipped_count += 1
            continue
        
        print(f"{i}. Processing video {video_id}...")

        # Add random delay to avoid rate limiting
        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        print(f"   Waiting {delay:.1f}s before request...")
        time.sleep(delay)

        # Get transcript (returns tuple: transcript_text, error_msg)
        transcript, error_msg = get_transcript(video_id)
        
        if error_msg is not None:
            print(f"   ERROR: {error_msg}")
            error_count += 1
            # Save error info
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\nERROR: {error_msg}\n")
            continue
        
        # Save transcript with original link
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\n{'='*80}\n")
                f.write(f"TRANSCRIPT:\n")
                f.write(f"{'='*80}\n\n")
                f.write(transcript)
            
            print(f"   SUCCESS: Saved transcript ({len(transcript)} characters)")
            success_count += 1
            
        except Exception as e:
            print(f"   ERROR saving transcript: {str(e)}")
            error_count += 1
    
    print("\n" + "="*80)
    print(f"SUMMARY:")
    print(f"  Total processed: {len(lines)}")
    print(f"  Successful: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Transcripts saved to: {output_dir}")
    print("="*80)


if __name__ == '__main__':
    main()
